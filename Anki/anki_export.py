#!/usr/bin/env python3
"""Export flashcards from the Obsidian lecture archive to Anki (.apkg).

Standard library only, no pip install needed.

Sources:
  <SUBJ>/Přednášky/*.md  callouts  > [!anki|ID]- Question  (body = answer)
  <SUBJ>/Pojmy/*.md      one card per term (skipped if frontmatter has anki: false)

Usage (from anywhere):
  python3 anki_export.py              all subjects   -> Anki/<SUBJ>.apkg
  python3 anki_export.py LAG          one subject    -> Anki/LAG.apkg
  python3 anki_export.py LAG 3        one lecture    -> Anki/LAG 03.apkg
  python3 anki_export.py --check      only validate and count cards

Re-importing a file updates existing cards (stable GUIDs), never duplicates them.
Edit cards in Obsidian, not in Anki: the next import overwrites Anki-side edits.
"""

import argparse
import hashlib
import html
import itertools
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import urllib.parse
import zipfile

DECK_PREFIX = "ČVUT"
MODEL_NAME = "ČVUT · Obsidian"
FIELDS = ["Otázka", "Odpověď", "Kontext", "Obsidian", "Klíč"]
LECTURE_DIR = "Přednášky"
TERM_DIR = "Pojmy"

CALLOUT_RE = re.compile(r"^>\s*\[!anki\|([^\]]+)\]([+-]?)\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")

# ---------- ids ----------

BASE91 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          "!#$%&()*+,-./:;<=>?@[]^_`{|}~")


def guid_for(key):
    # same scheme as genanki.guid_for(key)
    n = int.from_bytes(hashlib.sha256(key.encode("utf-8")).digest()[:8], "big")
    out = []
    while n > 0:
        n, r = divmod(n, 91)
        out.append(BASE91[r])
    return "".join(reversed(out))


def stable_id(text):
    # deterministic id < 2^53 (safe in JSON)
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16)


MODEL_ID = stable_id("model:" + MODEL_NAME)

# ---------- markdown helpers ----------


def read_note(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
                if not m:
                    continue
                k, v = m.group(1), m.group(2).strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
                else:
                    v = v.strip("\"'")
                    if v.lower() in ("true", "false"):
                        v = v.lower() == "true"
                meta[k] = v
            body = text[end + 4:].lstrip("\n")
    return meta, body


class Converter:
    """Obsidian markdown -> Anki HTML (MathJax \\( \\) and \\[ \\])."""

    def __init__(self, media_index):
        self.media_index = media_index  # basename -> path
        self.media_used = {}
        self.missing_media = set()

    def inline(self, s):
        store = []

        def keep(val):
            store.append(val)
            return "\x00%d\x00" % (len(store) - 1)

        s = re.sub(r"%%.*?%%", "", s, flags=re.S)
        s = re.sub(r"`([^`]+)`", lambda m: keep("<code>%s</code>" % html.escape(m.group(1))), s)
        s = re.sub(r"(?<!\\)\$\$(.+?)\$\$",
                   lambda m: keep("\\[%s\\]" % html.escape(m.group(1).strip(), quote=False)), s, flags=re.S)
        s = re.sub(r"(?<![\\$])\$(?=\S)(.+?)(?<=\S)(?<!\\)\$(?!\d)",
                   lambda m: keep("\\(%s\\)" % html.escape(m.group(1), quote=False)), s)
        s = re.sub(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", lambda m: keep(self.image(m.group(1).strip())), s)
        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                   lambda m: keep('<a href="%s">%s</a>' % (html.escape(m.group(2)), html.escape(m.group(1)))), s)
        s = re.sub(r"\[\[([^\]]+)\]\]", lambda m: self.wikilink(m.group(1)), s)
        s = re.sub(r"\s\^[A-Za-z0-9-]+\s*$", "", s)
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
        s = re.sub(r"==(.+?)==", r"<mark>\1</mark>", s)
        s = re.sub(r"(?<![\\*])\*(?!\s)(.+?)(?<![\s\\])\*(?!\*)", r"<i>\1</i>", s)
        s = s.replace("\\*", "*")
        return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], s)

    @staticmethod
    def wikilink(inner):
        target, _, alias = inner.partition("|")
        return alias if alias else target.split("#")[0]

    def image(self, name):
        path = self.media_index.get(name)
        if not path:
            self.missing_media.add(name)
            return ""
        self.media_used[name] = path
        return '<img src="%s">' % html.escape(name)

    def block(self, text):
        lines = text.split("\n")
        out, para, i = [], [], 0

        def flush():
            if para:
                out.append("<div>%s</div>" % "<br>".join(self.inline(p) for p in para))
                para.clear()

        while i < len(lines):
            line = lines[i]
            st = line.strip()
            if re.fullmatch(r"\^[A-Za-z0-9-]+", st):
                i += 1
                continue
            if not st:
                flush()
                i += 1
                continue
            if st.startswith("$$"):
                # display math spanning lines
                flush()
                buf = [st]
                if not (st.endswith("$$") and len(st) > 2):
                    i += 1
                    while i < len(lines):
                        buf.append(lines[i].strip())
                        if lines[i].strip().endswith("$$"):
                            break
                        i += 1
                out.append('<div class="math">%s</div>' % self.inline("\n".join(buf)))
                i += 1
                continue
            if st.startswith(">"):
                flush()
                quote = []
                while i < len(lines) and lines[i].strip().startswith(">"):
                    quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                head = re.match(r"^\[!(\w+)[^\]]*\][+-]?\s*(.*)$", quote[0]) if quote else None
                if head:
                    title = self.inline(head.group(2)) or head.group(1)
                    out.append('<blockquote><div class="bqt">%s</div>%s</blockquote>'
                               % (title, self.block("\n".join(quote[1:]))))
                else:
                    out.append("<blockquote>%s</blockquote>" % self.block("\n".join(quote)))
                continue
            if st.startswith("|"):
                flush()
                rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                        rows.append(cells)
                    i += 1
                body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c) for c in r) for r in rows)
                out.append("<table>%s</table>" % body)
                continue
            m = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", line)
            if m:
                flush()
                ordered = m.group(2)[0].isdigit()
                start = int(re.sub(r"\D", "", m.group(2))) if ordered else 1
                items = []
                while i < len(lines):
                    m = re.match(r"^\s*([-*]|\d+[.)])\s+(.*)$", lines[i])
                    if not m:
                        break
                    items.append(m.group(2))
                    i += 1
                tag = "ol" if ordered else "ul"
                attr = ' start="%d"' % start if start != 1 else ""
                out.append("<%s%s>%s</%s>" % (tag, attr, "".join("<li>%s</li>" % self.inline(x) for x in items), tag))
                continue
            para.append(st)
            i += 1
        flush()
        return "".join(out)


# ---------- vault scanning ----------


def obsidian_uri(vault_name, rel_path):
    rel = rel_path[:-3] if rel_path.endswith(".md") else rel_path
    q = urllib.parse.urlencode({"vault": vault_name, "file": rel.replace(os.sep, "/")},
                               quote_via=urllib.parse.quote)
    return "obsidian://open?" + q


def subjects_in(vault):
    return sorted(d for d in os.listdir(vault)
                  if not d.startswith(".") and os.path.isdir(os.path.join(vault, d))
                  and (os.path.isdir(os.path.join(vault, d, LECTURE_DIR))
                       or os.path.isdir(os.path.join(vault, d, TERM_DIR))))


def media_index_for(vault):
    idx = {}
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
                idx.setdefault(f, os.path.join(root, f))
    return idx


def to_int(v, default=0):
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return default


def lecture_cards(vault, subj, conv, vault_name, only=None):
    cards, errors = [], []
    d = os.path.join(vault, subj, LECTURE_DIR)
    if not os.path.isdir(d):
        return cards, errors
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(d, fn)
        meta, body = read_note(path)
        num = to_int(meta.get("prednaska"))
        if only is not None and num != only:
            continue
        title = fn[:-3]
        short = "%s %02d" % (subj, num)
        section = ""
        seen = {}
        lines = body.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            h = HEADING_RE.match(line)
            if h and len(h.group(1)) == 2:
                section = re.sub(r"^§\d+\s*", "", h.group(2))
            m = CALLOUT_RE.match(line)
            if not m:
                i += 1
                continue
            cid, question = m.group(1).strip(), m.group(3).strip()
            line_no = i + 1
            ans = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                ans.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            where = "%s: [!anki|%s]" % (fn, cid)
            if cid in seen:
                errors.append("%s duplicitní ID (už na řádku %d)" % (where, seen[cid]))
                continue
            seen[cid] = line_no
            if not question or not "".join(ans).strip():
                errors.append("%s chybí otázka nebo odpověď" % where)
                continue
            ctx_sec = section if section and section.lower() not in ("kartičky", "otázky k opakování") \
                else title.split(" – ", 1)[-1]
            cards.append({
                "key": "%s:P%02d:%s" % (subj, num, cid),
                "q": conv.inline(question),
                "a": conv.block("\n".join(ans)),
                "ctx": "%s · %s" % (short, conv.inline(ctx_sec)),
                "uri": obsidian_uri(vault_name, os.path.relpath(path, vault)),
                "tags": [subj, "%s::P%02d" % (subj, num), "prednaska"],
                "order": num * 1000 + 500 + len(cards),
            })
    return cards, errors


def term_cards(vault, subj, conv, vault_name, only=None):
    cards, errors = [], []
    d = os.path.join(vault, subj, TERM_DIR)
    if not os.path.isdir(d):
        return cards, errors
    for fn in sorted(os.listdir(d), key=str.lower):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(d, fn)
        meta, body = read_note(path)
        if meta.get("anki") is False:
            continue
        num = to_int(meta.get("prednaska"))
        if only is not None and num != only:
            continue
        name = fn[:-3]
        lidsky, formal, ref = [], "", ""
        lines = body.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            if re.match(r"^>\s*\[!lidsky\]", line):
                i += 1
                while i < len(lines) and lines[i].startswith(">"):
                    lidsky.append(re.sub(r"^>\s?", "", lines[i]))
                    i += 1
                continue
            m = re.match(r"^\*\*Formálně:\*\*\s*(.*)$", line)
            if m:
                formal = m.group(1)
            m = re.match(r"^\*\*Definice:\*\*\s*(.*)$", line)
            if m:
                ref = m.group(1)
            i += 1
        if not lidsky and not formal:
            errors.append("%s: pojem nemá box lidsky ani řádek Formálně" % fn)
            continue
        ans = conv.block("\n".join(lidsky)) if lidsky else ""
        if formal:
            ans += '<div class="formal"><b>Formálně:</b> %s</div>' % conv.inline(formal)
        if ref:
            ans += '<div class="ref">Definice: %s</div>' % conv.inline(ref)
        cards.append({
            "key": "%s:pojem:%s" % (subj, name),
            "q": '<span class="term">%s</span>' % html.escape(name),
            "a": ans,
            "ctx": "%s · pojem · přednáška %d" % (subj, num) if num else "%s · pojem" % subj,
            "uri": obsidian_uri(vault_name, os.path.relpath(path, vault)),
            "tags": [subj, "%s::P%02d" % (subj, num), "pojem"],
            "order": num * 1000 + len(cards),
        })
    return cards, errors


# ---------- apkg writer ----------

CSS = """
.card { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif;
  font-size: 19px; line-height: 1.5; color: #1d1f24; background: #fff; text-align: left; }
.wrap { max-width: 680px; margin: 0 auto; }
.ctx { font-size: 13px; color: #6a7080; margin-bottom: 10px; }
.q { font-size: 21px; font-weight: 600; }
.term { font-size: 27px; color: #2447B3; }
hr#answer { border: 0; border-top: 1px solid #d0d4dc; margin: 16px 0; }
.a > div { margin: 0 0 8px; }
.formal { margin-top: 10px; padding: 8px 10px; background: #f1f4fb; border-radius: 6px; }
.ref, .src { margin-top: 12px; font-size: 13px; color: #6a7080; }
.src a { color: #2447B3; text-decoration: none; }
.math { overflow-x: auto; }
mark { background: #fde7a9; color: inherit; padding: 0 2px; border-radius: 3px; }
img { max-width: 100%; border-radius: 6px; background: #fff; }
table { border-collapse: collapse; margin: 6px 0; font-size: 16px; }
td { border: 1px solid #d0d4dc; padding: 3px 8px; }
blockquote { margin: 8px 0; padding: 6px 12px; border-left: 3px solid #c3cad8; }
.bqt { font-weight: 600; margin-bottom: 4px; }
ul, ol { margin: 4px 0 8px; padding-left: 24px; }
code { font-size: 15px; background: #eef0f4; padding: 1px 4px; border-radius: 4px; }
.nightMode.card, .night_mode .card { color: #e4e6eb; background: #1e1f22; }
.nightMode .term { color: #93aaff; }
.nightMode .formal { background: #2a2d35; }
.nightMode .src a { color: #93aaff; }
.nightMode mark { background: #6b5a1e; }
.nightMode td, .nightMode hr#answer { border-color: #444a55; }
.nightMode code { background: #2a2d35; }
"""

QFMT = '<div class="wrap"><div class="ctx">{{Kontext}}</div><div class="q">{{Otázka}}</div></div>'
AFMT = ('<div class="wrap"><div class="ctx">{{Kontext}}</div><div class="q">{{Otázka}}</div>'
        '<hr id="answer"><div class="a">{{Odpověď}}</div>'
        '{{#Obsidian}}<div class="src"><a href="{{Obsidian}}">Otevřít v Obsidianu ↗</a></div>{{/Obsidian}}'
        '</div>')

SCHEMA = """
CREATE TABLE col (id integer primary key, crt integer not null, mod integer not null, scm integer not null,
  ver integer not null, dty integer not null, usn integer not null, ls integer not null, conf text not null,
  models text not null, decks text not null, dconf text not null, tags text not null);
CREATE TABLE notes (id integer primary key, guid text not null, mid integer not null, mod integer not null,
  usn integer not null, tags text not null, flds text not null, sfld integer not null, csum integer not null,
  flags integer not null, data text not null);
CREATE TABLE cards (id integer primary key, nid integer not null, did integer not null, ord integer not null,
  mod integer not null, usn integer not null, type integer not null, queue integer not null, due integer not null,
  ivl integer not null, factor integer not null, reps integer not null, lapses integer not null,
  left integer not null, odue integer not null, odid integer not null, flags integer not null, data text not null);
CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null, ease integer not null,
  ivl integer not null, lastIvl integer not null, factor integer not null, time integer not null,
  type integer not null);
CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);
CREATE INDEX ix_notes_usn on notes (usn);
CREATE INDEX ix_cards_usn on cards (usn);
CREATE INDEX ix_revlog_usn on revlog (usn);
CREATE INDEX ix_cards_nid on cards (nid);
CREATE INDEX ix_cards_sched on cards (did, queue, due);
CREATE INDEX ix_revlog_cid on revlog (cid);
CREATE INDEX ix_notes_csum on notes (csum);
"""

DCONF = {"1": {
    "id": 1, "name": "Default", "mod": 0, "usn": 0, "maxTaken": 60, "autoplay": True, "timer": 0,
    "replayq": True, "dyn": False,
    "new": {"bury": True, "delays": [1, 10], "initialFactor": 2500, "ints": [1, 4, 7], "order": 1,
            "perDay": 20, "separate": True},
    "lapse": {"delays": [10], "leechAction": 0, "leechFails": 8, "minInt": 1, "mult": 0},
    "rev": {"bury": True, "ease4": 1.3, "fuzz": 0.05, "ivlFct": 1, "maxIvl": 36500, "minSpace": 1,
            "perDay": 200}}}


def deck_json(did, name, desc, now):
    return {"id": did, "name": name, "desc": desc, "mod": now, "usn": -1, "collapsed": False,
            "browserCollapsed": False, "dyn": 0, "conf": 1, "extendNew": 0, "extendRev": 0,
            "lrnToday": [0, 0], "revToday": [0, 0], "newToday": [0, 0], "timeToday": [0, 0]}


def model_json(did, now):
    return {
        "id": MODEL_ID, "name": MODEL_NAME, "type": 0, "mod": now, "usn": -1, "sortf": 0, "did": did,
        "tmpls": [{"name": "Karta", "ord": 0, "qfmt": QFMT, "afmt": AFMT, "did": None,
                   "bqfmt": "", "bafmt": "", "bfont": "", "bsize": 0}],
        "flds": [{"name": n, "ord": i, "sticky": False, "rtl": False, "font": "Arial", "size": 20,
                  "media": []} for i, n in enumerate(FIELDS)],
        "css": CSS, "latexPre": "", "latexPost": "", "latexsvg": False,
        "req": [[0, "any", [0, 2]]], "tags": [], "vers": []}


def strip_html(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def write_apkg(out_path, deck_name, deck_desc, cards, media):
    now = int(time.time())
    did = stable_id("deck:" + deck_name)
    ids = itertools.count(now * 1000)
    fd, db = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    try:
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.executescript(SCHEMA)
        decks = {"1": deck_json(1, "Default", "", now), str(did): deck_json(did, deck_name, deck_desc, now)}
        conf = {"activeDecks": [1], "curDeck": 1, "newSpread": 0, "collapseTime": 1200, "timeLim": 0,
                "estTimes": True, "dueCounts": True, "curModel": str(MODEL_ID), "nextPos": 1,
                "sortType": "noteFld", "sortBackwards": False, "addToCur": True}
        cur.execute("INSERT INTO col VALUES (1,?,?,?,11,0,0,0,?,?,?,?,?)",
                    (now - now % 86400, now * 1000, now * 1000, json.dumps(conf),
                     json.dumps({str(MODEL_ID): model_json(did, now)}), json.dumps(decks),
                     json.dumps(DCONF), "{}"))
        for c in sorted(cards, key=lambda c: c["order"]):
            fields = [c["q"], c["a"], c["ctx"], html.escape(c["uri"]), c["key"]]
            sfld = strip_html(fields[0])
            csum = int(hashlib.sha1(sfld.encode("utf-8")).hexdigest()[:8], 16)
            nid = next(ids)
            cur.execute("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (nid, guid_for(c["key"]), MODEL_ID, now, -1, " %s " % " ".join(c["tags"]),
                         "\x1f".join(fields), sfld, csum, 0, ""))
            cur.execute("INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (next(ids), nid, did, 0, now, -1, 0, 0, c["order"], 0, 0, 0, 0, 0, 0, 0, 0, ""))
        con.commit()
        con.close()
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(db, "collection.anki2")
            names = sorted(media)
            z.writestr("media", json.dumps({str(i): n for i, n in enumerate(names)}, ensure_ascii=False))
            for i, n in enumerate(names):
                z.write(media[n], str(i))
    finally:
        os.remove(db)


# ---------- main ----------


def subject_title(vault, subj):
    d = os.path.join(vault, subj)
    for fn in os.listdir(d):
        if fn.startswith(subj + " – ") and fn.endswith(".md"):
            return fn[:-3]
    return subj


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Obsidian archiv přednášek -> Anki .apkg")
    ap.add_argument("subject", nargs="?", help="kód předmětu, např. LAG (výchozí: všechny)")
    ap.add_argument("lecture", nargs="?", type=int, help="číslo přednášky (jen tahle přednáška)")
    ap.add_argument("--vault", default=os.path.dirname(here), help="kořen vaultu (výchozí: nadřazená složka)")
    ap.add_argument("--vault-name", help="název vaultu v Obsidianu (výchozí: název složky)")
    ap.add_argument("--out", help="kam uložit .apkg (výchozí: <vault>/Anki)")
    ap.add_argument("--check", action="store_true", help="jen zkontrolovat a spočítat karty")
    args = ap.parse_args()

    vault = os.path.abspath(args.vault)
    vault_name = args.vault_name or os.path.basename(vault.rstrip(os.sep))
    out_dir = os.path.abspath(args.out or os.path.join(vault, "Anki"))
    subjects = [args.subject] if args.subject else subjects_in(vault)
    if not subjects:
        sys.exit("Ve vaultu %s jsem nenašel žádný předmět se složkou %s/." % (vault, LECTURE_DIR))
    media_index = media_index_for(vault)
    failed = False

    for subj in subjects:
        if not os.path.isdir(os.path.join(vault, subj)):
            sys.exit("Předmět %s ve vaultu není." % subj)
        conv = Converter(media_index)
        t_cards, t_err = term_cards(vault, subj, conv, vault_name, args.lecture)
        l_cards, l_err = lecture_cards(vault, subj, conv, vault_name, args.lecture)
        cards = t_cards + l_cards
        for e in t_err + l_err:
            print("CHYBA  " + e, file=sys.stderr)
        for m in sorted(conv.missing_media):
            print("VAROVÁNÍ  obrázek %s ve vaultu není" % m, file=sys.stderr)
        if t_err or l_err:
            failed = True
            continue
        if not cards:
            print("%s: žádné karty" % subj)
            continue
        name = "%s %02d.apkg" % (subj, args.lecture) if args.lecture else "%s.apkg" % subj
        summary = "%s: %d karet (%d pojmů, %d z přednášek)" % (subj, len(cards), len(t_cards), len(l_cards))
        if args.check:
            print(summary)
            continue
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, name)
        write_apkg(path, "%s::%s" % (DECK_PREFIX, subj), subject_title(vault, subj), cards, conv.media_used)
        print("%s -> %s" % (summary, path))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

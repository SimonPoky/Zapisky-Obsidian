---
aliases: ["syntaktického stromu", "strom formule", "podformule"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 1
zdroj: "slajd 7"
---

# syntaktický strom

> [!lidsky] Lidsky
> Obrázek stavby formule: listy jsou proměnné, nad nimi spojky, kořen je poslední použitá spojka. Každý podstrom je podformule.
>
> *Příklad:* strom formule (a ∧ b) ⇒ ¬c má v kořeni ⇒, vlevo podstrom ∧ s listy a, b, vpravo podstrom ¬ s listem c. Podformule jsou a, b, c, a ∧ b, ¬c a celá formule.

> [!obrazek] Strom formule $(\neg b \Rightarrow a) \vee c$
> ![[lgr01-strom.png]]
> *Modře spojky, oranžově proměnné (listy). Zelené číslo u vrcholu je hloubka podformule, která v něm začíná; celá formule má hloubku 3.*

**Formálně:** a ↦ vrchol a; ¬α ↦ kořen ¬ se synem strom(α); α ∘ β ↦ kořen ∘ se syny strom(α), strom(β)

**Definice:** [[LGR 01 – Syntax a sémantika výrokové logiky#^def-strom|přednáška 1, 24. 9. 2026]] · slajd 7 · predikátová logika: [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-strom-pl|přednáška 8]], handout 5, slajd 12

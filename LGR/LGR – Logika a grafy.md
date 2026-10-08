---
predmet: LGR
kod: B0B01LGR
tags: [predmet, LGR]
---

# LGR – Logika a grafy

*B0B01LGR · přednáší Alena Gollová · 5 kreditů · 3 h přednášek + 2 h cvičení týdně · zápočet a zkouška*

[Přednášky: prezentace a videa ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr-prednaska.html) · [Prezentace 1 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1.pdf) · [Stránka předmětu ↗](https://math.fel.cvut.cz/en/people/gollova/lgr.html) · [Literatura ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr-literatura.html) · [Testy v Moodle ↗](https://moodle.fel.cvut.cz/course/view.php?id=10550) · [Videopřednášky (YouTube) ↗](https://www.youtube.com/playlist?list=PLQL6z4JeTTQkjV5JYF0gB599ekq4zFfPK)

**Kartičky:** 71 povinných + 23 příkladů · [otevřít aplikaci ↗](https://claude.ai/artifact/3CKfKeuwtwrWiz3FSfSh5B) · [[Archiv přednášek#Kartičky|jak to funguje]]

## Přednášky

- **24. 9. 2026** [[LGR 01 – Syntax a sémantika výrokové logiky|Syntax a sémantika výrokové logiky]] · formule, syntaktický strom, hloubka, ohodnocení, tautologie
- **25. 9. 2026** [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek|Tautologická ekvivalence a úplné systémy spojek]] · formalizace, booleovské funkce, |=|, NAND, NOR, XOR, úplné systémy spojek
- **1. 10. 2026** [[LGR 03 – Disjunktivní a konjunktivní normální forma|Disjunktivní a konjunktivní normální forma]] · literál, minterm, maxterm, DNF, CNF, úplná DNF/CNF
- **8. 10. 2026** [[LGR 04 – Sémantický důsledek a klauzální tvar|Sémantický důsledek a klauzální tvar]] · splnitelnost množiny, prázdná množina, S ⊨ φ, důkaz sporem, klauzální tvar, rezolventa

## Plán semestru

*Podle stránky přednášek (ZS 2026/27). Prezentace k týdnu N jsou `lgr_N.pdf`, verze k tisku `lgr_Na.pdf`.*

| týden | od | téma |
|---|---|---|
| 1 | 21. 9. | Syntax a sémantika výrokové logiky, splnitelnost, tautologická ekvivalence, úplné systémy spojek |
| 2 | 28. 9. | Booleovské funkce, konjunktivní a disjunktivní normální forma, sémantický důsledek |
| 3 | 5. 10. | Rezoluční metoda ve výrokové logice, převod na klauzule |
| 4 | 12. 10. | Přirozená dedukce ve výrokové logice, korektnost a úplnost |
| 5 | 19. 10. | Syntax a sémantika predikátové logiky, model sentence |
| 6 | 26. 10. | Splnitelné sentence, tautologie, sémantický důsledek, prenexní tvar |
| 7 | 2. 11. | Rezoluce v predikátové logice, unifikace |
| 8 | 9. 11. | Neorientované grafy, základní pojmy |
| 9 | 16. 11. | Stromy, minimální kostra grafu |
| 10 | 23. 11. | Grafové algoritmy, eulerovské grafy |
| 11 | 30. 11. | Orientované grafy, acyklické grafy, topologické očíslování, jádro grafu |
| 12 | 7. 12. | Silně souvislé komponenty |
| 13 | 14. 12. | Barevnost grafů |
| 14 | 4. 1. | Rovinné grafy |

## Slovníček pojmů

*Najetím myší na pojem uvidíš náhled, klepnutím otevřeš jeho poznámku.*

- [[booleovská funkce]] · Sloupec pravdivostní tabulky: f : {0, 1}ⁿ → {0, 1}. Pro n proměnných jich je 2^(2ⁿ).
- [[disjunktivní normální forma]] · DNF: disjunkce mintermů. Má ji každá formule.
- [[formule]] · Výrok zapsaný z proměnných, spojek a závorek podle pravidel. α, β zastupují libovolnou formuli.
- [[hloubka formule]] · Počet pater syntaktického stromu; proměnná 0, každá spojka +1.
- [[implikace]] · Slib „jestliže α, pak β“. Nepravdivá jen pro 1 ⇒ 0.
- [[klauzální tvar]] · Kl(S): formule rozsekané přes CNF na klauzule bez tautologií; splnitelný iff S splnitelná.
- [[konjunktivní normální forma]] · CNF: konjunkce maxtermů. Má ji každá formule.
- [[kontradikce]] · Formule nepravdivá v každém ohodnocení, např. a ∧ ¬a.
- [[literál]] · Proměnná nebo její negace: a, ¬a.
- [[logická proměnná]] · Písmenko za jednoduchý výrok; atomická formule, list stromu.
- [[maxterm]] · Disjunkce literálů (nebo literál, nebo ff), též klauzule.
- [[minterm]] · Konjunkce literálů (nebo literál, nebo tt), např. a ∧ ¬b.
- [[Peirceova šipka]] · NOR, „ani jedno“. Sama tvoří úplný systém spojek.
- [[pravdivostní ohodnocení]] · Přiřazení 0/1 všem formulím podle tabulky spojek. Určí ho hodnoty proměnných; pro n proměnných 2ⁿ možností.
- [[rezolventa]] · Ze α ∨ x a β ∨ ¬x vznikne α ∨ β; plyne z obou. Prázdná rezolventa ff znamená nesplnitelnost.
- [[sémantický důsledek]] · S ⊨ φ: kdykoli platí všechny předpoklady, platí i závěr; u(S) ≤ u(φ).
- [[Shefferova čárka]] · NAND, „ne obojí zároveň“. Sama tvoří úplný systém spojek.
- [[splnitelná formule]] · Pravdivá aspoň v jednom ohodnocení.
- [[splnitelná množina formulí]] · Existuje ohodnocení, kde platí všechny formule naráz. Prázdná množina je splnitelná.
- [[syntaktický strom]] · Stavba formule: listy proměnné, kořen poslední spojka, podstromy podformule.
- [[tautologická ekvivalence]] · Dvě formule se stejnou hodnotou v každém ohodnocení (stejný sloupec tabulky).
- [[tautologie]] · Formule pravdivá v každém ohodnocení, např. a ∨ ¬a.
- [[úplná normální forma]] · DNF/CNF, kde každý term obsahuje všechny proměnné; vzniká z tabulky.
- [[úplný systém logických spojek]] · Spojky, kterými jde zapsat každá booleovská funkce: {¬, ∧, ∨}, {¬, ⇒}, {|}, {↓}.
- [[vylučovací nebo]] · XOR, „buď, anebo“: pravdivé, když se hodnoty liší.
- [[výrok]] · Oznamovací věta, u které se dá rozhodnout o pravdivosti.

## Jak se předmět hodnotí

*Podle stránky [Informace o zápočtu a zkoušce ↗](https://moodle.fel.cvut.cz/mod/page/view.php?id=419981) v Moodle (ZS 2026/27). Ukázka písemky je tamtéž.*

| část | pravidla |
|---|---|
| Účast | Aktivní účast aspoň na 70 % cvičení. |
| Online testy v Moodle | Aspoň 10 ze 14 týdenních testů úspěšně (71 %). Test se otevře večer po cvičení v 18:30 a zavře se za týden před dalším cvičením ve 23:59. Dva pokusy, podmínka úspěchu je u každého testu. |
| Test 1 | 9. týden (od 16. 11. 2026), na cvičení, 40 min, max. 15 b., na zápočet aspoň 5 b. Logika: rezoluce ve výrokové logice, syntax a sémantika výrokové a predikátové logiky (handouty 1–3 a 5–6). |
| Test 2 | 13. týden (od 14. 12. 2026), 40 min, max. 15 b., aspoň 5 b. Teorie grafů: základní pojmy a grafové algoritmy (handouty 8–11). |
| Opravy | Každý test jen jednou a jen při neúspěchu, **bez bonusu**. Při nemoci náhradní termín i s bonusem. Opravy i náhrady centrálně na konci semestru. |
| Domácí práce | Cvičící může zadat další domácí úkoly. |
| Bonus ze semestru | Oba testy napoprvé: součet − 10. Jen jeden napoprvé: jeho body − 5. Žádný napoprvé: 0. Rozsah 0–20 b. |
| Zkouška | Jen se zápočtem, přihlášení v KOSu. Písemná, 135 min, max. 80 b. Celkem = písemka + bonus. |
| Ústní zkouška | Nepovinná, možná od 75 b. celkem; −10 až +10 b., tedy o stupeň oběma směry. Zkoušející ji může nařídit. |
| Stupnice | A 90–100 · B 80–89 · C 70–79 · D 60–69 · E 50–59 · F < 50 |

> [!note] Co z toho plyne v číslech
> - Každý bod z testu nad povinných 5 je bod ke zkoušce: 2 × (15 − 5) = **20 b.** maximálně. Oprava testu dá zápočet, ale bonus z něj je **0**.
> - Bez bonusu je strop 80 b. z písemky, tedy nejvýš **B**. Na E je potřeba 50 z 80 (62,5 %).
> - S plným bonusem stačí na E 30 b. z 80 (37,5 %) a na **A** 70 z 80 (87,5 %).
> - Na rozdíl od LAG a MA1 nemá písemka uvedené nutné minimum: rozhoduje jen součet.
> - Ústní zkouška se otevírá od 75 b. (C). Riziko je symetrické: ±10 b. může známku zlepšit i zhoršit o stupeň.

> [!navic] K písemce
> Přijď aspoň 10 minut předem s průkazem (index, OP, pas). Vezmi čisté nelinkované listy A4 a modrou nebo černou propisku; tužkou psát nelze. Na lavici smí být jen zadání, papíry, psací potřeby a svačina, mobil vypnutý v zavřené tašce. Na titulní straně si poznač termín náhledu.

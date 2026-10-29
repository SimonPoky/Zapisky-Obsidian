---
predmet: LGR
kod: B0B01LGR
tags: [predmet, LGR]
---

# LGR – Logika a grafy

*B0B01LGR · přednáší Alena Gollová · 5 kreditů · 3 h přednášek + 2 h cvičení týdně · zápočet a zkouška*

[Přednášky: prezentace a videa ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr-prednaska.html) · [Prezentace 1 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1.pdf) · [Stránka předmětu ↗](https://math.fel.cvut.cz/en/people/gollova/lgr.html) · [Literatura ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr-literatura.html) · [Testy v Moodle ↗](https://moodle.fel.cvut.cz/course/view.php?id=10550) · [Videopřednášky (YouTube) ↗](https://www.youtube.com/playlist?list=PLQL6z4JeTTQkjV5JYF0gB599ekq4zFfPK)

**Kartičky:** 230 povinných + 70 příkladů · [otevřít aplikaci ↗](https://claude.ai/artifact/3CKfKeuwtwrWiz3FSfSh5B) · [[Archiv přednášek#Kartičky|jak to funguje]]

## Přednášky

- **24. 9. 2026** [[LGR 01 – Syntax a sémantika výrokové logiky|Syntax a sémantika výrokové logiky]] · formule, syntaktický strom, hloubka, ohodnocení, tautologie
- **25. 9. 2026** [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek|Tautologická ekvivalence a úplné systémy spojek]] · formalizace, booleovské funkce, |=|, NAND, NOR, XOR, úplné systémy spojek
- **1. 10. 2026** [[LGR 03 – Disjunktivní a konjunktivní normální forma|Disjunktivní a konjunktivní normální forma]] · literál, minterm, maxterm, DNF, CNF, úplná DNF/CNF
- **8. 10. 2026** [[LGR 04 – Sémantický důsledek a klauzální tvar|Sémantický důsledek a klauzální tvar]] · splnitelnost množiny, prázdná množina, S ⊨ φ, důkaz sporem, klauzální tvar, rezolventa
- **9. 10. 2026** [[LGR 05 – Rezoluční princip|Rezoluční princip]] · R*(S), zamítací strom, rezoluční princip, 3ⁿ klauzulí, eliminace proměnné, rezoluční tabulka
- **15. 10. 2026** [[LGR 06 – Rezoluční tabulka a přirozená dedukce|Rezoluční tabulka a přirozená dedukce]] · tabulka na příkladu, svědek pozpátku, S ⊢ φ, korektní a úplný systém, přirozená dedukce, ∧i, ⇒i, boxy, odvození
- **22. 10. 2026** [[LGR 07 – Odvozená pravidla, korektnost a úplnost|Odvozená pravidla, korektnost a úplnost]] · ¬¬i, MT, RAA, TND, ⊣⊢, kompaktnost, věta o dedukci, indukce, korektnost, úplnost, literály řádku
- **23. 10. 2026** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky|Dokončení úplnosti a syntaxe predikátové logiky]] · krok lemmatu pro ⇒, predikátová logika, jazyk, termy, formule, volné a vázané proměnné, sentence, interpretace, formalizace
- **29. 10. 2026** [[LGR 09 – Pravdivost formulí, model a tautologie|Pravdivost formulí, model a tautologie]] · jazyk teorie čísel, kontext ρ, update ρ[x:=d], ⟦t⟧ρ, pravdivost při kontextu, svědek, model, splnitelná sentence, tautologie, nemodel

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

- [[absorpce]] · α ∨ (β ∧ α) ⊨⊨ α a duálně; přidaný člen nic nezmění.
- [[Aristotelův sylogismus]] · Každý člověk je smrtelný, Sokrates je člověk, tedy je smrtelný; výroková logika to neověří.
- [[arita]] · Počet argumentů symbolu: S(x) má aritu 1, P(x, y) aritu 2.
- [[atomická formule]] · Predikát s dosazenými termy P(t₁, …, tₙ) nebo rovnost t₁ = t₂; nejjednodušší tvrzení.
- [[booleovská funkce]] · Sloupec pravdivostní tabulky: f : {0, 1}ⁿ → {0, 1}. Pro n proměnných jich je 2^(2ⁿ).
- [[čisté proměnné]] · Žádná proměnná není ve formuli volná i vázaná; dosáhne se legálním přejmenováním.
- [[disjunktivní normální forma]] · DNF: disjunkce mintermů. Má ji každá formule.
- [[ekvisplnitelné množiny]] · Obě splnitelné, nebo obě ne; svědky se lišit mohou.
- [[eliminace disjunkce]] · ∨e, rozbor případů: platí-li φ ∨ ψ a z každého případu plyne χ, platí χ.
- [[eliminace dvojité negace]] · ¬¬e: z ¬¬φ odvoď φ (jen klasická logika).
- [[eliminace konjunkce]] · ∧e₁, ∧e₂: z φ ∧ ψ smíš vzít φ i ψ.
- [[eliminace negace]] · ¬e: φ a ¬φ naráz dají spor ⊥.
- [[eliminace sporu]] · ⊥e: ze sporu plyne cokoli.
- [[formule]] · Výrok zapsaný z proměnných, spojek a závorek podle pravidel. α, β zastupují libovolnou formuli.
- [[formule predikátové logiky]] · Z atomických formulí spojkami a kvantifikátory ∀x, ∃x.
- [[funkční symbol]] · Jméno operace, která z objektů vyrobí objekt: f(x) následník; v interpretaci Uⁿ → U.
- [[hloubka formule]] · Počet pater syntaktického stromu; proměnná 0, každá spojka +1.
- [[hodnota termu]] · Prvek universa, který term označuje při kontextu: ⟦x + 1⟧ρ = 8 pro ρ(x) = 7.
- [[implikace]] · Slib „jestliže α, pak β“. Nepravdivá jen pro 1 ⇒ 0.
- [[interpretace]] · (U, ⟦−⟧): universum a význam každého predikátu, funkce a konstanty.
- [[iterace]] · it: už odvozenou formuli smíš zopakovat, i do vnořeného boxu.
- [[jazyk predikátové logiky]] · Logické symboly (proměnné, spojky, ∀, ∃, =) a speciální: Pred, Func, Kons s aritami.
- [[klauzální tvar]] · Kl(S): formule rozsekané přes CNF na klauzule bez tautologií; splnitelný iff S splnitelná.
- [[komplementární literály]] · x a ¬x: stejná proměnná jednou pozitivně, jednou negativně.
- [[konjunktivní normální forma]] · CNF: konjunkce maxtermů. Má ji každá formule.
- [[konstantní symbol]] · Jméno jednoho konkrétního objektu, např. a pro dvojku.
- [[kontext proměnných]] · ρ : Var → U, tabulka dosazení: za co právě stojí každá proměnná.
- [[kontradikce]] · Formule nepravdivá v každém ohodnocení, např. a ∧ ¬a.
- [[kontradikce predikátové logiky]] · Sentence bez modelu, nepravdivá v každé interpretaci.
- [[korektní důkazový systém]] · Co jde odvodit, to platí: S ⊢ φ ⇒ S ⊨ φ.
- [[kvantifikátor]] · ∀x „pro každé“, ∃x „existuje“; váže silněji než spojky.
- [[legální přejmenování]] · Přejmenování vázané proměnné, při kterém se žádná volná proměnná nestane vázanou.
- [[lemma o literálech řádku]] · u(φ) = 1 ⇒ L_u ⊢ φ, jinak L_u ⊢ ¬φ.
- [[literál]] · Proměnná nebo její negace: a, ¬a.
- [[literály řádku]] · L_u: x, nebo ¬x podle u(x); řádek tabulky jako množina literálů.
- [[logická ekvivalence]] · φ ⊣⊢ ψ: každá jde odvodit z druhé; totéž co |=| díky úplnosti.
- [[logická proměnná]] · Písmenko za jednoduchý výrok; atomická formule, list stromu.
- [[logický důsledek]] · S ⊢ φ: φ jde z S odvodit podle pravidel (odvoditelnost, syntax).
- [[maxterm]] · Disjunkce literálů (nebo literál, nebo ff), též klauzule.
- [[minterm]] · Konjunkce literálů (nebo literál, nebo tt), např. a ∧ ¬b.
- [[model sentence]] · Interpretace, ve které je sentence pravdivá; „svět, kde to platí“.
- [[modus ponens]] · Z a a a ⇒ b plyne b.
- [[modus tollens]] · MT: z φ ⇒ ψ a ¬ψ plyne ¬φ.
- [[nezávislost sentence na kontextu]] · Sentence platí v I buď při každém kontextu, nebo při žádném.
- [[obměněná implikace]] · φ ⇒ ψ ⊨⊨ ¬ψ ⇒ ¬φ; základ důkazu obměnou.
- [[odvozené pravidlo]] · Zkratka poskládaná ze základních pravidel; nic nového nedokáže.
- [[odvození]] · Důkaz po řádcích, každý řádek s pravidlem a odkazem; na konci φ, boxy zavřené.
- [[otevřená formule]] · Formule bez vázaných proměnných, např. S(x).
- [[Peirceova šipka]] · NOR, „ani jedno“. Sama tvoří úplný systém spojek.
- [[pomocný předpoklad]] · Lokální předpoklad otevírá box; jeho formule platí jen uvnitř boxu.
- [[populace rezolvent]] · R*(S): S a všechny rezolventy, rezolventy rezolvent atd.; pravdivá tam, kde S.
- [[pravdivost formule při kontextu]] · Atomická dosazením do relace, spojky tabulkou, ∃ aspoň jeden update, ∀ všechny.
- [[pravdivost sentence]] · Sentence je pravdivá v I, platí-li při každém (ekvivalentně aspoň jednom) kontextu.
- [[pravdivostní ohodnocení]] · Přiřazení 0/1 všem formulím podle tabulky spojek. Určí ho hodnoty proměnných; pro n proměnných 2ⁿ možností.
- [[pravidlo slučování]] · (α ∨ x) ∧ (α ∨ ¬x) ⊨⊨ α a duálně; proměnná, na které nezáleží, zmizí.
- [[prázdná klauzule]] · Disjunkce bez literálů, ff; nepravdivá vždy. Vzniká jako res(x, ¬x).
- [[predikátová logika]] · Vidí dovnitř výroků: proměnné jsou objekty, predikáty vlastnosti a vztahy, přibývají ∀ a ∃.
- [[predikátový symbol]] · Jméno vlastnosti nebo vztahu: S(x) „x je sudé“, P(x, y) „x < y“.
- [[příliš agresivní systém]] · Odvodí i to, co neplyne; nekorektní.
- [[princip silné indukce]] · Krok smí použít všechna čísla n₀, …, n, ne jen n.
- [[princip slabé indukce]] · Domino: základ n₀ a krok z n na n + 1.
- [[přirozená dedukce]] · Důkazový systém bez axiomů: ke každé spojce pravidlo zavedení (i) a odstranění (e).
- [[reductio ad absurdum]] · RAA, důkaz sporem: z ¬φ vyjde spor, tedy φ.
- [[rezoluční princip]] · Konečná S je splnitelná, právě když ff ∉ R*(S).
- [[rezoluční tabulka]] · Vyrezolvuje proměnné jednu po druhé; konec {ff} = nesplnitelná, ∅ = splnitelná.
- [[rezolventa]] · Ze α ∨ x a β ∨ ¬x vznikne α ∨ β; plyne z obou. Prázdná rezolventa ff znamená nesplnitelnost.
- [[rovnost formulí]] · dvě formule jsou si rovny, jen když se píšou znak po znaku stejně
- [[sémantická věta o kompaktnosti]] · S ⊨ φ, právě když S′ ⊨ φ pro konečnou S′ ⊆ S; nejtěžší krok úplnosti.
- [[sémantický důsledek]] · S ⊨ φ: kdykoli platí všechny předpoklady, platí i závěr; u(S) ≤ u(φ).
- [[sentence]] · Formule bez volných proměnných (uzavřená), např. ∀x P(x, f(x)).
- [[Shefferova čárka]] · NAND, „ne obojí zároveň“. Sama tvoří úplný systém spojek.
- [[slabá věta o úplnosti]] · ⊢ φ ⟺ ⊨ φ: věty výrokové logiky jsou právě tautologie.
- [[splnitelná formule]] · Pravdivá aspoň v jednom ohodnocení.
- [[splnitelná množina formulí]] · Existuje ohodnocení, kde platí všechny formule naráz. Prázdná množina je splnitelná.
- [[splnitelná sentence]] · Sentence, která má aspoň jeden model.
- [[sporný důkazový systém]] · Odvodí úplně všechno, i φ a ¬φ; nic nerozliší.
- [[strukturální indukce]] · Vlastnost pro proměnné a její zachování každou spojkou ⇒ platí pro všechny formule.
- [[svědek pravdivosti]] · Prvek d, jehož dosazením za x platí φ; dokazuje ∃x φ.
- [[svědek splnitelnosti]] · Ohodnocení, kde platí celá množina; z rezoluční tabulky se hledá pozpátku.
- [[symbol rovnosti]] · = je logický symbol: v každé interpretaci znamená „tentýž prvek universa“.
- [[syntaktická věta o dedukci]] · S ∪ {φ} ⊢ ψ, právě když S ⊢ φ ⇒ ψ.
- [[syntaktická věta o kompaktnosti]] · S ⊢ φ, právě když S′ ⊢ φ pro nějakou konečnou S′ ⊆ S.
- [[syntaktický strom]] · Stavba formule: listy proměnné, kořen poslední spojka, podstromy podformule.
- [[tautologická ekvivalence]] · Dvě formule se stejnou hodnotou v každém ohodnocení (stejný sloupec tabulky).
- [[tautologie]] · Formule pravdivá v každém ohodnocení, např. a ∨ ¬a.
- [[tautologie predikátové logiky]] · Sentence pravdivá v každé interpretaci, např. ∀x (x = x).
- [[term]] · Jméno objektu: proměnná, konstanta, f(t₁, …, tₙ); nic netvrdí.
- [[universum]] · Neprázdná množina objektů, o kterých se mluví, např. ℕ.
- [[update kontextu]] · ρ[x:=d]: stejný kontext, jen x přepsáno na d.
- [[úplná normální forma]] · DNF/CNF, kde každý term obsahuje všechny proměnné; vzniká z tabulky.
- [[úplný důkazový systém]] · Odvodí přesně to, co platí: S ⊢ φ ⟺ S ⊨ φ.
- [[úplný systém logických spojek]] · Spojky, kterými jde zapsat každá booleovská funkce: {¬, ∧, ∨}, {¬, ⇒}, {|}, {↓}.
- [[vázaná proměnná]] · Má ve formuli aspoň jeden vázaný výskyt.
- [[vázaný výskyt]] · Cestou ke kořeni stromu leží ∀x nebo ∃x s touto proměnnou.
- [[věta o dedukci]] · Předpoklad jde přesunout do závěru: S ∪ {φ} ⊨ ψ iff S ⊨ φ ⇒ ψ.
- [[věta o eliminaci proměnné]] · S splnitelná iff S₀ ∪ Rₓ splnitelná; klauzule s x jde po rezoluci zahodit.
- [[věta o korektnosti]] · S ⊢ φ ⇒ S ⊨ φ: přirozená dedukce nedokáže nepravdu.
- [[věta o normálních formách]] · Ke každé formuli existuje ekvivalentní DNF i CNF (ne jednoznačně).
- [[věta o sémantickém důkazu sporem]] · S ⊨ φ právě když S ∪ {¬φ} je nesplnitelná.
- [[věta o úplnosti]] · S ⊢ φ ⟺ S ⊨ φ: odvoditelné = pravdivé.
- [[věta výrokové logiky]] · Formule φ s ⊢ φ, dokazatelná bez předpokladů.
- [[volná proměnná]] · Má ve formuli aspoň jeden volný výskyt.
- [[volný výskyt]] · Nad výskytem není kvantifikátor s touto proměnnou.
- [[vylučovací nebo]] · XOR, „buď, anebo“: pravdivé, když se hodnoty liší.
- [[výrok]] · Oznamovací věta, u které se dá rozhodnout o pravdivosti.
- [[základní tvar klauzulí]] · Každá proměnná je v klauzuli nejvýš jednou; bez tautologií.
- [[zákon vyloučeného třetího]] · TND: φ ∨ ¬φ platí vždy; základ rozboru případů.
- [[zamítací strom]] · Strom rezolucí od klauzulí z S ke kořeni ff; důkaz nesplnitelnosti.
- [[zavedení disjunkce]] · ∨i: z φ smíš odvodit φ ∨ ψ i ψ ∨ φ.
- [[zavedení dvojité negace]] · ¬¬i: z φ odvoď ¬¬φ (odvozené pravidlo).
- [[zavedení implikace]] · ⇒i, přímý důkaz: předpokládej φ v boxu, odvoď ψ, máš φ ⇒ ψ.
- [[zavedení konjunkce]] · ∧i: z φ a ψ odvoď φ ∧ ψ.
- [[zavedení negace]] · ¬i: když z předpokladu φ vyjde spor, platí ¬φ.

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

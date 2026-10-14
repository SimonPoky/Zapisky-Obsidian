---
predmet: LAG
kod: B0B01LAG
tags: [predmet, LAG]
---

# LAG – Lineární algebra

*B0B01LAG · přednáší Daniel Gromada*

[Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf) · [Stránka přednášky ↗](https://math.fel.cvut.cz/cz/lide/gromadan/lag26p.html) · [Sbírka příkladů (Velebil) ↗](https://math.fel.cvut.cz/en/people/velebil/files/lag_2026_podzim/lag_sbirka_2026_01_21.pdf)

**Kartičky:** 128 povinných + 49 příkladů · [otevřít aplikaci ↗](https://claude.ai/artifact/3CKfKeuwtwrWiz3FSfSh5B) · [[Archiv přednášek#Kartičky|jak to funguje]]

## Přednášky

- **23. 9. 2026** [[LAG 01 – Úvod do lineární algebry|Úvod do lineární algebry]] · číselné těleso, soustavy 2 × 2, axiomy, lineární prostor
- **25. 9. 2026** [[LAG 02 – Příklady lineárních prostorů|Příklady lineárních prostorů]] · 𝔽ⁿ, matice, eukleidovské vektory, posloupnosti, 𝔽ᴬ, polynomy
- **30. 9. 2026** [[LAG 03 – Lineární podprostor a lineární obal|Lineární podprostor a lineární obal]] · podprostor, věta 2.2, homogenní soustava, lineární kombinace, span
- **2. 10. 2026** [[LAG 04 – Lineární závislost a nezávislost|Lineární závislost a nezávislost]] · důkaz věty 2.13, LZ a LN, pozorování 3.2, věty 3.3 a 3.6
- **7. 10. 2026** [[LAG 05 – Báze a dimenze|Báze a dimenze]] · věta 3.7, generující posloupnost, báze, kanonická báze, dimenze, výběr a doplnění báze
- **9. 10. 2026** [[LAG 06 – Souřadnice, součet a průnik podprostorů|Souřadnice, součet a průnik podprostorů]] · dimenze podprostoru, souřadnice, souřadnicový vektor, linearita souřadnic, průnik a součet podprostorů, dimenze součtu a průniku

## Zápočtové testy

*Cvičení vede Jakub Rondoš · pondělí 12:45–14:15, KN:A-224 · [stránka cvičení ↗](https://math.fel.cvut.cz/en/people/rondojak/linearni-algebra-zs-26-27) · konzultace po domluvě: rondojak@fel.cvut.cz*

- **Zápočet:** nejvýš 3 absence na cvičení a 2 úspěšné testy, z každého aspoň **10 z 20 b.** Body z testů se přičítají ke zkouškové písemce. Neúspěšný test jde opakovat na hromadném termínu na konci semestru.
- **Každý test:** 1 početní příklad (**10 b.**) + 1 teoretický příklad (**5 b.**) + 1 definice (**5 b.**). Každé tvrzení je potřeba řádně zdůvodnit.
- **1. test: pondělí 16. 11. 2026** (8. cvičení, termín se ještě může změnit) · [ukázka početních příkladů ↗](https://math.fel.cvut.cz/en/people/rondojak/linearni-algebra/LAG_Ukazka%20pocetnich%20prikladu%201.pdf) · [ukázka teoretických příkladů ↗](https://math.fel.cvut.cz/en/people/rondojak/linearni-algebra/LAG_Ukazka%20teoretickych%20prikladu%201.pdf) · [seznam definic ↗](https://math.fel.cvut.cz/en/people/rondojak/linearni-algebra/LAG_Definice%201.pdf)
- **2. test:** nejspíš 12. cvičení (podle rozvrhu 14. 12. 2026), materiály zatím nevyšly.

### Definice na 1. test

Na testu se zadá jedna z nich a je potřeba ji napsat přesně, s tím, co je dané předem („Buď L lineární prostor nad 𝔽…“). Přesné znění je v kartičce každého pojmu, řádek **Formálně**.

| # | definice ze seznamu | pojem | stav |
|---|---|---|---|
| 1 | Lineární obal | [[lineární obal]] | přednáška 3 |
| 2 | Lineární podprostor | [[lineární podprostor]] | přednáška 3 |
| 3 | Lineární nezávislost a závislost | [[lineární nezávislost]], [[lineární závislost]] | přednáška 4 |
| 4 | Generování lineárního prostoru | [[generující posloupnost]] | přednáška 5 |
| 5 | Báze | [[báze]] | přednáška 5 |
| 6 | Dimenze | [[dimenze]] | přednáška 5 |
| 7 | Lineární zobrazení | | přijde v kap. 6 |
| 8 | Souřadnice vektoru vzhledem k bázi | [[souřadnice]], [[souřadnicový vektor]] | přednáška 6 |
| 9 | Matice lineárního zobrazení vzhledem k bázím B a C | | přijde v kap. 6 |
| 10 | Matice transformace souřadnic z báze B do báze C | | přijde v kap. 6.3 |
| 11 | Jádro | | přijde v kap. 7 |
| 12 | Obraz | | přijde v kap. 7 |
| 13 | Monomorfismus, epimorfismus, izomorfismus | [[izomorfismus]] (zatím jen neformálně) | přijde v kap. 6–7 |
| 14 | Hodnost | | přijde v kap. 7 |
| 15 | Defekt | | přijde v kap. 7 |

### Typy příkladů z ukázky

| typ úlohy | část testu | kde procvičit |
|---|---|---|
| Je daná množina podprostor ($\mathbb{R}^2$, $\mathbb{R}^{\le 2}[x]$)? | teoretický | [[LAG 03 – Lineární podprostor a lineární obal#Typové příklady na zápočtový test\|LAG 03]], příklady 17–21 |
| Je zobrazení lineární? Je to mono-, epi-, izomorfismus? Urči $\operatorname{Im}$. | teoretický | přijde s kap. 6–7 |
| Dokaž, že posloupnost je báze (s využitím dimenze) | dílčí krok početního | [[LAG 05 – Báze a dimenze#Typové příklady na zápočtový test\|LAG 05]], příklady 27–28 |
| Souřadnice polynomu nebo matice vzhledem k bázi | dílčí krok početního | [[LAG 06 – Souřadnice, součet a průnik podprostorů#Typové příklady na zápočtový test\|LAG 06]], příklady 22–23 |
| Matice zobrazení vůči bázím, skládání = maticový součin, matice transformace souřadnic | jádro početního | přijde s kap. 6 |

> [!note] Co z toho plyne v číslech
> - Z 15 definic je zatím probraných **8 (53 %)**; zbylých 7 přijde s lineárními zobrazeními (kap. 6–7).
> - Všech **6 z 6** ukázkových početních příkladů staví na matici lineárního zobrazení nebo matici transformace souřadnic. Těch **10 b. (50 % testu)** tedy stojí na látce, která se začíná přednášet 14. 10.
> - Z 7 teoretických ukázek se **3 (43 %)** dají řešit už teď (podprostory), **4 (57 %)** jsou o lineárních zobrazeních.
> - Do testu zbývá **9 přednášek** (28. 10. je svátek), kap. 6–7 by měly být probrané s rezervou.

> [!navic] Značení na cvičení a na přednášce
> - Souřadnice: na přednášce $[\vec{v}]^{\mathcal{X}}$, na cvičení $[\vec{v}]_{\mathcal{X}}$ nebo $\operatorname{coord}_{\mathcal{X}}(\vec{v})$. Je to totéž.
> - „Uspořádaná báze“ na cvičení = báze jako posloupnost z přednášky (záleží na pořadí).
> - $[A]_{X \to Y}$ = matice lineárního zobrazení $A$ vůči bázím $X$ (vstup) a $Y$ (výstup); $T_{X \to Y}$ = matice transformace souřadnic z báze $X$ do báze $Y$.

## Slovníček pojmů

*Najetím myší na pojem uvidíš náhled, klepnutím otevřeš jeho poznámku.*

- [[alternativní definice lineární závislosti]] · LZ právě když je některý vektor kombinací ostatních (i jen předchozích).
- [[axiomy lineárního prostoru]] · 8 pravidel počítání, která se nedokazují, ale požadují. Říkají, že se sčítáním a násobením vektorů zacházíš jako u čísel.
- [[báze]] · Souřadnicový systém: vektory, ze kterých poskládáš každý vektor prostoru, a to jediným způsobem. LN a generuje.
- [[charakterizace báze]] · Báze = minimální generující = maximální LN posloupnost.
- [[číselné těleso]] · Sada čísel, ve které můžeš sčítat, odčítat, násobit i dělit (ne nulou) a nikdy z ní nevypadneš. ℚ, ℝ, ℂ ano; ℤ ne, protože 1 : 2 = 0,5 v ℤ není.
- [[dimenze]] · Počet prvků báze, tedy počet nezávislých směrů: přímka 1, rovina 2, 𝔽ⁿ má n, všechny polynomy ∞.
- [[dobře definovaná operace]] · Operace nevyvede z množiny ven: součet dvou polynomů stupně ≤ n je zase polynom stupně ≤ n.
- [[eukleidovské vektory]] · Šipky vycházející z jednoho pevného bodu. Sčítají se rovnoběžníkem, násobí se natažením.
- [[generující posloupnost]] · Vektory, ze kterých jde poskládat úplně všechno: L = span{x₁, …, xₙ}.
- [[homogenní soustava]] · Soustava s nulovými pravými stranami. Její řešení tvoří podprostor, řešení nehomogenní soustavy ne.
- [[izomorfismus]] · Převodník mezi dvěma prostory, který zachová sčítání i násobení. Izomorfní prostory jsou stejné, jen jinak zapsané. Přesně se zavádí v kap. 7.
- [[kanonická báze]] · Báze 𝔽ⁿ z vektorů s jedničkou na jednom místě a nulami jinde, např. ((1; 0), (0; 1)).
- [[lineární kombinace]] · Recept „vezmi α₁ krát první vektor, α₂ krát druhý… a všechno sečti“. Čísla αᵢ jsou dávky jednotlivých ingrediencí.
- [[lineární nezávislost]] · Nula jde z vektorů namíchat jen triviálně, žádný vektor není navíc. Např. ((1; 0), (0; 1)).
- [[lineární obal]] · Všechno, co se dá z vektorů M namíchat: span{x} je přímka, span{x, y} rovina. Nejmenší podprostor obsahující M.
- [[lineární podprostor]] · Neprázdný kousek prostoru uzavřený na sčítání a násobení číslem. V ℝ² jen {0}, přímky přes počátek a celá rovina.
- [[lineární prostor]] · Sbírka věcí, které umíš mezi sebou sčítat a násobit číslem, výsledek zůstane ve sbírce a platí obvyklá pravidla počítání. Co ty věci jsou, je jedno.
- [[lineární rovnice]] · Úloha „kolikrát musím vzít a, abych dostal b“. Když a ≠ 0, je odpověď jediná: b/a.
- [[lineární závislost]] · Nula jde z vektorů namíchat i netriviálně, takže aspoň jeden vektor jde poskládat z ostatních. Např. ((1; 2), (2; 4)).
- [[matice]] · Tabulka čísel s m řádky a n sloupci. Pro sčítání je to jen sloupec m·n čísel poskládaný do obdélníku.
- [[netriviální lineární kombinace]] · Kombinace s aspoň jedním nenulovým koeficientem.
- [[nulový polynom]] · Polynom, který má všechny koeficienty nulové. Je to nulový vektor prostoru polynomů a jeho stupeň je dohodou −∞.
- [[nulový vektor]] · Vektor, který nic nezmění, když ho přičteš. Obdoba nuly u čísel; v každém prostoru je právě jeden (věta 1.8).
- [[opačný vektor]] · Vektor, který daný vektor „vynuluje“. U šipek je to stejná šipka opačným směrem.
- [[operace po složkách]] · Každá pozice se počítá zvlášť: první s první, druhá s druhou. (1; 2) + (3; 4) = (4; 6).
- [[polynom]] · Součet mocnin x s čísly před nimi. Pro lineární algebru je to hlavně seznam koeficientů.
- [[polynomiální funkce]] · Polynom je recept, polynomiální funkce hotové jídlo: co vyjde po dosazení. Nad číselnými tělesy si odpovídají jedna ku jedné.
- [[posloupnosti]] · Nekonečně dlouhý sloupec čísel. Sčítá se člen po členu.
- [[prostor funkcí]] · Funkce je vektor, jehož „pozice“ nejsou 1, …, n, ale prvky množiny A. Hodnota f(t) je složka na pozici t.
- [[prostor polynomů stupně nejvýše n]] · Polynomy se stupněm nejvýše n; podprostor 𝔽[x] dimenze n + 1.
- [[průnik podprostorů]] · Vektory ležící v obou podprostorech; vždy obsahuje 0.
- [[rozšířená matice soustavy]] · Soustava zapsaná jen čísly: koeficienty u neznámých v tabulce, pravé strany za svislou čarou. Neznámé se nepíšou, poznají se podle sloupce.
- [[skalár]] · Obyčejné číslo z tělesa 𝔽, kterým vektory natahuješ, zkracuješ nebo otáčíš.
- [[sloupcové vektory]] · Sloupce n čísel. Nejběžnější lineární prostor; skoro všechno se do něj nakonec převede.
- [[součet podprostorů]] · Všechny součty v + w; nejmenší podprostor obsahující V i W, obdoba sjednocení.
- [[souřadnice]] · Čísla α₁, …, αₙ v jediném zápisu v = α₁x₁ + … + αₙxₙ pomocí báze: kolik kroků kterým směrem.
- [[souřadnicový vektor]] · Souřadnice vektoru v bázi 𝒳 pod sebou ve sloupci: [v]^𝒳 ∈ 𝔽ⁿ.
- [[Steinitzova věta]] · LN posloupnost nemá víc prvků než generující posloupnost.
- [[stopa matice]] · Součet prvků na diagonále čtvercové matice.
- [[stupeň polynomu]] · Nejvyšší mocnina x, která v polynomu opravdu je, tedy s nenulovým číslem před sebou.
- [[triviální lineární kombinace]] · Všechny koeficienty nulové, výsledek je vždy nulový vektor.
- [[triviální podprostor]] · Podprostor {0}, nejmenší podprostor každého prostoru.
- [[vedoucí člen]] · Člen s nejvyšší mocninou x, která v polynomu je. U 2 + 3x − x² je to −x².
- [[vektor]] · Cokoliv, co jde sčítat s jinými takovými věcmi a násobit číslem podle 8 pravidel: šipka, sloupec čísel, polynom i funkce.
- [[věta o dimenzi podprostoru]] · Podprostor má nejvýš takovou dimenzi jako prostor; při konečné dimenzi rovnost jen pro V = L.
- [[věta o dimenzi součtu a průniku]] · dim(V + W) + dim(V ∩ W) = dim V + dim W, obdoba počtu prvků sjednocení.
- [[věta o doplnění na bázi]] · LN posloupnost v prostoru konečné dimenze jde doplnit na bázi.
- [[věta o jednoznačnosti vyjádření]] · LN právě když se každý vektor dá vyjádřit nejvýš jedním způsobem.
- [[věta o linearitě souřadnic]] · Souřadnice součtu jsou součet souřadnic, souřadnice násobku násobek souřadnic.
- [[věta o lineárním obalu]] · span M je vždy podprostor, a to nejmenší podprostor obsahující M.
- [[věta o odebírání a přidávání vektorů]] · Odebráním z LN posloupnosti zůstane LN, přidáním k LZ zůstane LZ.
- [[věta o počtu prvků báze]] · Všechny báze prostoru mají stejný počet prvků.
- [[věta o podprostoru]] · Podprostor je sám lineární prostor, stačí ověřit neprázdnost a dvě uzavřenosti.
- [[věta o přidání vektoru k LN posloupnosti]] · K LN posloupnosti jde přidat v se zachováním LN, právě když v neleží v jejím obalu.
- [[věta o průniku podprostorů]] · Průnik dvou podprostorů je podprostor.
- [[věta o součtu obalů]] · span M + span N = span(M ∪ N): generátory součtu se sjednotí.
- [[věta o součtu podprostorů]] · Součet dvou podprostorů je podprostor (sjednocení obecně ne).
- [[věta o vlastnostech lineárního prostoru]] · Nulový i opačný vektor jsou jediné, α ⊙ x = 0 jen pro α = 0 nebo x = 0 a −x = (−1) ⊙ x.
- [[věta o výběru báze]] · Z konečné generující množiny jde vybrat bázi.

## Jak se předmět hodnotí

*Podle stránky přednášky (ZS 2026/27). Podmínky zápočtu upřesňuje cvičící.*

> [!navic] Body zadarmo: kvízy na Moodle · nevynechat
> Po každé přednášce vyjde na Moodle krátký kvíz. Vyplnit ho je třeba týž den, nejpozději druhý den.
>
> - Aspoň 80 % kvízů vyplněných včas: **+2 body** ke zkoušce.
> - Aspoň 80 % kvízů správně: dalších **+2 body**.

| část | pravidla |
|---|---|
| Zápočtové testy | 2 testy, nejspíš v 8. a 12. týdnu. Každý max. 20 b., na úspěch aspoň 10 b. Opravný termín bude hromadný. |
| Zkoušková písemka | 60 minut, 3 části po 20 b.: A kvíz (správně +5, špatně −2), B definice a důkaz, C výpočet. Nutné minimum je 30 b. |
| Bonus ze semestru | Body z testů minus 3 b. za každý absolvovaný pokus (oba testy napoprvé: −6 b.) plus body za kvízy. |
| Ústní zkouška | Nepovinná, od 45 b. celkem. Lze získat až +15 b., ztratit nejvýš 5 b. |
| Stupnice | A ≥ 90 · B 80–89 · C 70–79 · D 60–69 · E 50–59 · F 0–49 |

> [!note] Co z toho plyne v číslech
> - Maximální bonus: 2 × 20 − 6 = **34 b.** z testů + **4 b.** z kvízů = **38 b.**
> - Bez bonusu je strop písemky 60 b., tedy nejvýš **D**.
> - S plným bonusem dá minimálních 30 b. z písemky rovnou 68 b. (D) a na **A** stačí 52 b. z 60 (87 %).

> [!navic] Značky v oficiálních poznámkách k přednáškám
> - **♥** definice, které se zkouší v části B1: musíš je umět sám zformulovat.
> - **\*** odstavce a kapitoly, které nejsou nutné ke zkouškové písemce (srdíčko hvězdičku přebíjí).
> - Důkazy se nazpaměť učit nemusíš. V části B2 se dokazuje jednoduché tvrzení, které typicky není mezi číslovanými větami.

---
predmet: LAG
kod: B0B01LAG
tags: [predmet, LAG]
---

# LAG – Lineární algebra

*B0B01LAG · přednáší Daniel Gromada*

[Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf) · [Stránka přednášky ↗](https://math.fel.cvut.cz/cz/lide/gromadan/lag26p.html) · [Sbírka příkladů (Velebil) ↗](https://math.fel.cvut.cz/en/people/velebil/files/lag_2026_podzim/lag_sbirka_2026_01_21.pdf)

**Kartičky:** 77 povinných + 25 příkladů · [otevřít aplikaci ↗](https://claude.ai/artifact/3CKfKeuwtwrWiz3FSfSh5B) · [[Archiv přednášek#Kartičky|jak to funguje]]

## Přednášky

- **23. 9. 2026** [[LAG 01 – Úvod do lineární algebry|Úvod do lineární algebry]] · číselné těleso, soustavy 2 × 2, axiomy, lineární prostor
- **25. 9. 2026** [[LAG 02 – Příklady lineárních prostorů|Příklady lineárních prostorů]] · 𝔽ⁿ, matice, eukleidovské vektory, posloupnosti, 𝔽ᴬ, polynomy
- **30. 9. 2026** [[LAG 03 – Lineární podprostor a lineární obal|Lineární podprostor a lineární obal]] · podprostor, věta 2.2, homogenní soustava, lineární kombinace, span
- **2. 10. 2026** [[LAG 04 – Lineární závislost a nezávislost|Lineární závislost a nezávislost]] · důkaz věty 2.13, LZ a LN, pozorování 3.2, věty 3.3 a 3.6

## Slovníček pojmů

*Najetím myší na pojem uvidíš náhled, klepnutím otevřeš jeho poznámku.*

- [[axiomy lineárního prostoru]] · 8 pravidel počítání, která se nedokazují, ale požadují. Říkají, že se sčítáním a násobením vektorů zacházíš jako u čísel.
- [[číselné těleso]] · Sada čísel, ve které můžeš sčítat, odčítat, násobit i dělit (ne nulou) a nikdy z ní nevypadneš. ℚ, ℝ, ℂ ano; ℤ ne, protože 1 : 2 = 0,5 v ℤ není.
- [[dobře definovaná operace]] · Operace nevyvede z množiny ven: součet dvou polynomů stupně ≤ n je zase polynom stupně ≤ n.
- [[eukleidovské vektory]] · Šipky vycházející z jednoho pevného bodu. Sčítají se rovnoběžníkem, násobí se natažením.
- [[homogenní soustava]] · Soustava s nulovými pravými stranami. Její řešení tvoří podprostor, řešení nehomogenní soustavy ne.
- [[izomorfismus]] · Převodník mezi dvěma prostory, který zachová sčítání i násobení. Izomorfní prostory jsou stejné, jen jinak zapsané. Přesně se zavádí v kap. 7.
- [[lineární kombinace]] · Recept „vezmi α₁ krát první vektor, α₂ krát druhý… a všechno sečti“. Čísla αᵢ jsou dávky jednotlivých ingrediencí.
- [[lineární nezávislost]] · Nula jde z vektorů namíchat jen triviálně, žádný vektor není navíc. Např. ((1; 0), (0; 1)).
- [[lineární obal]] · Všechno, co se dá z vektorů M namíchat: span{x} je přímka, span{x, y} rovina. Nejmenší podprostor obsahující M.
- [[lineární podprostor]] · Neprázdný kousek prostoru uzavřený na sčítání a násobení číslem. V ℝ² jen {0}, přímky přes počátek a celá rovina.
- [[lineární prostor]] · Sbírka věcí, které umíš mezi sebou sčítat a násobit číslem, výsledek zůstane ve sbírce a platí obvyklá pravidla počítání. Co ty věci jsou, je jedno.
- [[lineární rovnice]] · Úloha „kolikrát musím vzít a, abych dostal b“. Když a ≠ 0, je odpověď jediná: b/a.
- [[lineární závislost]] · Nula jde z vektorů namíchat i netriviálně, takže aspoň jeden vektor jde poskládat z ostatních. Např. ((1; 2), (2; 4)).
- [[matice]] · Tabulka čísel s m řádky a n sloupci. Pro sčítání je to jen sloupec m·n čísel poskládaný do obdélníku.
- [[nulový polynom]] · Polynom, který má všechny koeficienty nulové. Je to nulový vektor prostoru polynomů a jeho stupeň je dohodou −∞.
- [[nulový vektor]] · Vektor, který nic nezmění, když ho přičteš. Obdoba nuly u čísel; v každém prostoru je právě jeden (věta 1.8).
- [[opačný vektor]] · Vektor, který daný vektor „vynuluje“. U šipek je to stejná šipka opačným směrem.
- [[operace po složkách]] · Každá pozice se počítá zvlášť: první s první, druhá s druhou. (1; 2) + (3; 4) = (4; 6).
- [[polynom]] · Součet mocnin x s čísly před nimi. Pro lineární algebru je to hlavně seznam koeficientů.
- [[polynomiální funkce]] · Polynom je recept, polynomiální funkce hotové jídlo: co vyjde po dosazení. Nad číselnými tělesy si odpovídají jedna ku jedné.
- [[posloupnosti]] · Nekonečně dlouhý sloupec čísel. Sčítá se člen po členu.
- [[prostor funkcí]] · Funkce je vektor, jehož „pozice“ nejsou 1, …, n, ale prvky množiny A. Hodnota f(t) je složka na pozici t.
- [[rozšířená matice soustavy]] · Soustava zapsaná jen čísly: koeficienty u neznámých v tabulce, pravé strany za svislou čarou. Neznámé se nepíšou, poznají se podle sloupce.
- [[skalár]] · Obyčejné číslo z tělesa 𝔽, kterým vektory natahuješ, zkracuješ nebo otáčíš.
- [[sloupcové vektory]] · Sloupce n čísel. Nejběžnější lineární prostor; skoro všechno se do něj nakonec převede.
- [[souřadnice]] · Návod „kolik kroků kterým směrem“ vede k bodu. Změníš-li směry kroků, změní se čísla v návodu, bod zůstane stejný.
- [[stupeň polynomu]] · Nejvyšší mocnina x, která v polynomu opravdu je, tedy s nenulovým číslem před sebou.
- [[triviální lineární kombinace]] · Všechny koeficienty nulové, výsledek je vždy nulový vektor.
- [[vedoucí člen]] · Člen s nejvyšší mocninou x, která v polynomu je. U 2 + 3x − x² je to −x².
- [[vektor]] · Cokoliv, co jde sčítat s jinými takovými věcmi a násobit číslem podle 8 pravidel: šipka, sloupec čísel, polynom i funkce.

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

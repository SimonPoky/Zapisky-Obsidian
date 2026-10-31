---
aliases: ["spojitost", "spojitá", "spojitá v bodě", "spojitosti", "spojitou", "nespojitá"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 5
zdroj: "handout 3A, slajd 3"
---

# spojitost v bodě

> [!lidsky] Lidsky
> Funkce stojí v bodě p přesně tam, kam se její graf blíží: limita v p existuje a rovná se f(p). Graf jde přes p bez zvednutí tužky.
>
> *Příklad:* f(x) = x² je spojitá v 3: lim_{x→3} x² = 9 = f(3). Funkce sgn (−1 pro x < 0, 0 v nule, 1 pro x > 0) spojitá v 0 není: zleva jde k −1, zprava k 1, limita v 0 neexistuje.

> [!obrazek] Spojitá a nespojitá funkce v bodě p
> ![[ma105-spojitost.png]]
> *Vlevo spojitá: modrý bod f(p) leží přesně tam, kam graf míří; nad oranžovým okolím p leží zelená část grafu celá v modrém terči kolem f(p). Vpravo nespojitá: graf míří k L (prázdné kolečko), ale červená hodnota f(p) je jinde.*

> [!obrazek] Spojitost přes okolí
> ![[ma106-okoli.png]]
> *Oranžové okolí V bodu p (i s bodem p) se zobrazí do zelené množiny f[V], která celá leží v modrém terči U kolem f(p). Pro každý, jakkoli malý terč U musí jít takové V najít.*

**Formálně:** f definovaná na okolí p ∈ ℝ; f je spojitá v p ⇔ lim_{x→p} f(x) = f(p)

**Definice:** [[MA1 05 – Aritmetika limit a substituce#^def-spojitost|přednáška 5, 7. 10. 2026]] · handout 3A, slajd 3 · tři ekvivalentní zápisy (limita, okolí, ε-δ): [[MA1 06 – Spojitost a spojité funkce na intervalu#^spojitost-tri-zapisy|přednáška 6]]

**Další zápisy:** přes okolí a přes ε-δ v [[MA1 06 – Spojitost a spojité funkce na intervalu#^spojitost-tri-zapisy|přednášce 6, 8. 10. 2026]]

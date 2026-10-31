---
aliases: ["souřadnice v bázi", "souřadnice vektoru vzhledem k bázi"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 1
zdroj: "pozn. 4.17 ♥"
---

# souřadnice

> [!lidsky] Lidsky
> Návod „kolik kroků kterým směrem“ vede k vektoru; směry kroků jsou vektory báze. Změníš-li bázi, změní se čísla v návodu, vektor zůstane stejný. Souřadnice jsou čísla z 𝔽, ne vektory.
>
> *Příklad:* v bázi 𝒳 = ((1; 1), (1; −1)) prostoru ℝ² je (3; 1) = 2·(1; 1) + 1·(1; −1), takže souřadnice vektoru (3; 1) jsou 2 a 1. V kanonické bázi jsou to 3 a 1: stejný vektor, jiná čísla.

> [!obrazek] Stejný vektor ve dvou bázích $\mathbb{R}^2$
> ![[lag05-souradnice.png]]
> *Vlevo kanonická báze: zelený $\vec{v} = (3; 2)$ je 3 modré kroky $\vec{e}_1$ a 2 oranžové kroky $\vec{e}_2$. Vpravo báze $\vec{b}_1 = (1; 0)$, $\vec{b}_2 = (1; 1)$: tentýž vektor je 1 modrý krok a 2 oranžové, $(3; 2) = 1 \cdot (1; 0) + 2 \cdot (1; 1)$.*

> [!obrazek] Rovina $V$ a její vlastní souřadnicová síť
> ![[lag06-souradnice.png]]
> *Vlevo zelená rovina $V$ uvnitř $\mathbb{R}^3$ s modrým $\vec{x}_1$, oranžovým $\vec{x}_2$ a červeným čárkovaným $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$. Vpravo tatáž rovina „položená na papír“: síť tvoří kroky ve směru $\vec{x}_1$ a $\vec{x}_2$ a každý bod má dvě souřadnice, např. černý bod $(1; 3; 2) = \vec{x}_1 + 2\vec{x}_2$ má souřadnice $(1; 2)$.*

**Formálně:** Buď L lineární prostor nad 𝔽, 𝒳 = (x₁, …, xₙ) báze L a v ∈ L. Čísla α₁, …, αₙ ∈ 𝔽 z (jediného) vyjádření v = α₁x₁ + … + αₙxₙ jsou souřadnice vektoru v vzhledem k bázi 𝒳

**Definice:** [[LAG 06 – Souřadnice, součet a průnik podprostorů#^def-souradnice|přednáška 6, 9. 10. 2026]] · pozn. 4.17 ♥ · poprvé v [[LAG 01 – Úvod do lineární algebry#Změna souřadnicového systému|přednášce 1]]

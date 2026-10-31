---
aliases: ["im A", "Im A", "obraz A", "obrazu lineárního zobrazení", "column space"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 11
zdroj: "pozn. 7.12 ♥"
---

# obraz lineárního zobrazení

> [!lidsky] Lidsky
> Všechno, kam se lineární zobrazení „trefí“: jeho obor hodnot. Leží ve výstupním prostoru W a je to vždy podprostor. U matice je to obal jejích sloupců.
>
> *Příklad:* pro A = $\begin{pmatrix}0&2&1\\0&4&2\end{pmatrix}$ je im A = span{(0; 0), (2; 4), (1; 2)} = span{(1; 2)}, přímka y = 2x. Bod (1; 0) v obrazu není.

> [!obrazek] Jádro a obraz obecně
> ![[lag11-jadro-obraz.png]]
> *Modrý prostor $V$ se zobrazí do oranžového $\operatorname{im} A$ uvnitř šedého $W$. Celé zelené jádro skončí v jediném bodě, nulovém vektoru $W$. Body $W$ mimo $\operatorname{im} A$ (červený křížek) nemají vzor.*

> [!obrazek] Jádro a obraz matice $\begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$
> ![[lag11-priklad.png]]
> *Vlevo $\mathbb{R}^3$: zelená rovina je $\ker A$ se zelenými generátory $(1; 0; 0)$ a $(0; 1; -2)$, modrá rovnoběžná rovina je vzor bodu $(1; 2)$, tedy zelená rovina posunutá o červený bod $(0; 0; 1)$. Vpravo $\mathbb{R}^2$: oranžová přímka je $\operatorname{im} A$, modrý bod $(1; 2)$ v ní leží, červený $(1; 0)$ ne a nemá žádný vzor.*

**Formálně:** Buďte V a W lineární prostory nad 𝔽, A ∈ Lin(V, W). Obraz A je jeho obor hodnot: im A = A(V) = {Ax | x ∈ V} ⊆ W

**Definice:** [[LAG 11 – Jádro, obraz, hodnost a defekt#^def-jadro-obraz|přednáška 11, 30. 10. 2026]] · pozn. 7.12 ♥

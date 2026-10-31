---
aliases: ["ker A", "ker", "jádra", "jádrem", "jádře"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 11
zdroj: "pozn. 7.12 ♥"
---

# jádro

> [!lidsky] Lidsky
> Všechny vektory, které zobrazení „zabije“, tedy pošle na nulu. Leží ve vstupním prostoru V a je to vždy podprostor. Pro matici jsou to řešení homogenní soustavy Ax = 0.
>
> *Příklad:* pro A = $\begin{pmatrix}0&2&1\\0&4&2\end{pmatrix}$ je ker A = span{(1; 0; 0), (0; 1; −2)}: z 2y + z = 0 je z = −2y. Vektor (0; 1; 0) v jádře není, jde na (2; 4).

> [!obrazek] Jádro a obraz obecně
> ![[lag11-jadro-obraz.png]]
> *Modrý prostor $V$ se zobrazí do oranžového $\operatorname{im} A$ uvnitř šedého $W$. Celé zelené jádro skončí v jediném bodě, nulovém vektoru $W$. Body $W$ mimo $\operatorname{im} A$ (červený křížek) nemají vzor.*

> [!obrazek] Jádro a obraz matice $\begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$
> ![[lag11-priklad.png]]
> *Vlevo $\mathbb{R}^3$: zelená rovina je $\ker A$ se zelenými generátory $(1; 0; 0)$ a $(0; 1; -2)$, modrá rovnoběžná rovina je vzor bodu $(1; 2)$, tedy zelená rovina posunutá o červený bod $(0; 0; 1)$. Vpravo $\mathbb{R}^2$: oranžová přímka je $\operatorname{im} A$, modrý bod $(1; 2)$ v ní leží, červený $(1; 0)$ ne a nemá žádný vzor.*

**Formálně:** Buďte V a W lineární prostory nad 𝔽, A ∈ Lin(V, W). Jádro A je vzor nulového vektoru: ker A = A⁻¹({0}) = {x ∈ V | Ax = 0} ⊆ V

**Definice:** [[LAG 11 – Jádro, obraz, hodnost a defekt#^def-jadro-obraz|přednáška 11, 30. 10. 2026]] · pozn. 7.12 ♥

---
aliases: ["charakteristického polynomu", "charakteristickým polynomem", "p_A(x)", "p_A"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 16
zdroj: "pozn. 11.11 ♥"
---

# charakteristický polynom

> [!lidsky] Lidsky
> Determinant matice A, od jejíž diagonály odečteš neznámou x. Jeho kořeny jsou vlastní čísla A.
>
> *Příklad:* A = (3 0; 1 2): p_A(x) = det(3 − x, 0; 1, 2 − x) = (3 − x)(2 − x) = x² − 5x + 6, kořeny 2 a 3 jsou vlastní čísla.

**Formálně:** Pro A ∈ 𝔽ⁿˣⁿ je p_A(x) = det(A − xE) ∈ 𝔽[x] charakteristický polynom matice A. Pro operátor A ∈ Lin(L), dim L < ∞: p_A(x) = det([A]^𝒳 − xE) v libovolné bázi 𝒳

**Definice:** [[LAG 16 – Vlastní čísla, charakteristický polynom a diagonalizace#^def-charakteristicky-polynom|přednáška 16, 18. 11. 2026]] · pozn. 11.11 ♥

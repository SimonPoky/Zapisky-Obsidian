---
aliases: ["[A + B] = [A] + [B]", "matice součtu zobrazení"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 9
zdroj: "věta 6.31"
---

# věta o matici součtu a násobku zobrazení

> [!lidsky] Lidsky
> Sčítání zobrazení a sčítání matic je totéž v jiném jazyce: matice součtu je součet matic, matice násobku je násobek matice.
>
> *Příklad:* A(x; y) = (x + y; 2y), B(x; y) = (y; x − y): [A]^ℰ + [B]^ℰ = $\begin{pmatrix}1&1\\0&2\end{pmatrix}$ + $\begin{pmatrix}0&1\\1&-1\end{pmatrix}$ = $\begin{pmatrix}1&2\\1&1\end{pmatrix}$ = [A + B]^ℰ, protože (A + B)(x; y) = (x + 2y; x + y).

**Formálně:** Buďte V, W lineární prostory nad 𝔽 konečné dimenze, 𝒳 báze V, 𝒴 báze W. Pak [A + B]^{𝒳→𝒴} = [A]^{𝒳→𝒴} + [B]^{𝒳→𝒴} pro A, B ∈ Lin(V, W) a [αA]^{𝒳→𝒴} = α[A]^{𝒳→𝒴} pro α ∈ 𝔽, A ∈ Lin(V, W)

**Definice:** [[LAG 09 – Algebra matic a transformace souřadnic#^veta-matice-souctu|přednáška 9, 21. 10. 2026]] · věta 6.31

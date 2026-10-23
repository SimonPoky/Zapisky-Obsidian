---
aliases: ["součinu matic", "násobení matic", "maticové násobení", "maticový součin", "AB"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 8
zdroj: "pozn. 6.9 ♥"
---

# součin matic

> [!lidsky] Lidsky
> Prvek na místě (i, j) je i-tý řádek A krát j-tý sloupec B: vynásobíš po dvojicích a sečteš. Jde to, jen když má A tolik sloupců, kolik má B řádků. Po sloupcích: j-tý sloupec AB je A krát j-tý sloupec B.
>
> *Příklad:* $\begin{pmatrix}1&2\\3&4\end{pmatrix}$$\begin{pmatrix}0&1\\1&0\end{pmatrix}$ = $\begin{pmatrix}2&1\\4&3\end{pmatrix}$, ale v opačném pořadí vyjde $\begin{pmatrix}3&4\\1&2\end{pmatrix}$: AB ≠ BA.

**Formálně:** Buďte A ∈ 𝔽^{n×m}, B ∈ 𝔽^{m×l}. Součin AB ∈ 𝔽^{n×l} je definován předpisem [AB]ᵢⱼ = Σₖ₌₁ᵐ aᵢₖbₖⱼ (i = 1, …, n; j = 1, …, l). Po sloupcích A(b₁ ⋯ bₗ) = (Ab₁ ⋯ Abₗ); obecně AB ≠ BA

**Definice:** [[LAG 08 – Matice lineárního zobrazení a součin matic#^def-soucin-matic|přednáška 8, 16. 10. 2026]] · pozn. 6.9 ♥ · po sloupcích: [[LAG 08 – Matice lineárního zobrazení a součin matic#^sloupce-soucinu|A(b₁ ⋯ bₗ) = (Ab₁ ⋯ Abₗ)]]

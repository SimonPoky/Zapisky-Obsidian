---
aliases: ["vedlejší sloupce", "vedlejších sloupců", "volné neznámé", "volná neznámá"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 12
zdroj: "pozn. 8.4"
---

# vedlejší sloupec

> [!lidsky] Lidsky
> Sloupec stupňovité matice bez pivotu. Neznámé u vedlejších sloupců jsou volné: při řešení se za ně volí parametry, a jejich počet je dimenze množiny řešení homogenní soustavy.
>
> *Příklad:* V $\begin{pmatrix}0&1&0&2&5&0&1\\0&0&0&2&3&1&0\\0&0&0&0&1&1&2\end{pmatrix}$ jsou vedlejší sloupce 1, 3, 6, 7, takže x₁, x₃, x₆, x₇ jsou parametry a dim S₀ = 7 − 3 = 4.

**Formálně:** Pro A ∈ 𝔽^{m×n} v horním stupňovitém tvaru s hlavními sloupci k₁, …, k_r jsou vedlejší sloupce všechny sloupce j ∉ {k₁, …, k_r}; je jich n − r

**Definice:** [[LAG 12 – Frobeniova věta a Gaussova eliminace#^def-stupnovity-tvar|přednáška 12, 4. 11. 2026]] · pozn. 8.4

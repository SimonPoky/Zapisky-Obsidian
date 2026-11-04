---
aliases: ["stupňovitý tvar", "horním stupňovitém tvaru", "horní stupňovitý tvar matice", "odstupňovaný tvar", "schodovitý tvar"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 12
zdroj: "pozn. 8.4"
---

# horní stupňovitý tvar

> [!lidsky] Lidsky
> Matice, jejíž nenulové řádky jsou nahoře a každý začíná prvním nenulovým číslem (pivotem) víc vpravo než řádek nad ním. Pod pivoty je schodiště nul a soustava se v tomto tvaru vyřeší zpětnou substitucí.
>
> *Příklad:* $\begin{pmatrix}0&3&1&0\\0&0&0&2\\0&0&0&0\end{pmatrix}$ v tvaru je (pivoty ve sloupcích 2 a 4). $\begin{pmatrix}1&2&0\\0&0&1\\0&1&0\end{pmatrix}$ není: pivot třetího řádku (sloupec 2) je vlevo od pivotu druhého (sloupec 3).

**Formálně:** Matice A ∈ 𝔽^{m×n} je v horním stupňovitém tvaru, jestliže existuje 0 ≤ r ≤ m tak, že aᵢⱼ = 0 pro všechna i > r a j = 1, …, n, a existují 0 < k₁ < k₂ < … < k_r ≤ n tak, že pro i = 1, …, r je a_{ik_i} ≠ 0 a aᵢⱼ = 0 pro všechna j < kᵢ

**Definice:** [[LAG 12 – Frobeniova věta a Gaussova eliminace#^def-stupnovity-tvar|přednáška 12, 4. 11. 2026]] · pozn. 8.4

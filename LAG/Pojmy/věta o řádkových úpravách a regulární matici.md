---
aliases: ["věta 8.16", "B = TA", "řádkově ekvivalentní matice"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 13
zdroj: "věta 8.16"
---

# věta o řádkových úpravách a regulární matici

> [!lidsky] Lidsky
> „Matici A jde řádkovými úpravami převést na B“ znamená přesně „B = TA pro nějakou regulární T“. Sloupce B jsou izomorfní obrazy sloupců A, takže lineární vztahy mezi sloupci zůstávají stejné.
>
> *Příklad:* (1 3; 2 5) se úpravami r₂ − 2r₁ (T₁ = (1 0; −2 1)) a r₁ + 3r₂, r₂·(−1) (T₂ = (1 3; 0 −1)) změní na E, a T = T₂T₁ = (−5 3; 2 −1) = A⁻¹.

**Formálně:** Buďte A, B ∈ 𝔽^{m×n}. A lze sledem elementárních řádkových úprav převést na B ⟺ existuje regulární T ∈ 𝔽^{m×m} s B = TA (pak T = T_l ⋯ T₁ pro matice jednotlivých úprav)

**Definice:** [[LAG 13 – Inverzní matice eliminací, transpozice a grupy#^veta-upravy-regularni|přednáška 13, 6. 11. 2026]] · věta 8.16

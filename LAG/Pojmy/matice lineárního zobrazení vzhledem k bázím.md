---
aliases: ["matice lineárního zobrazení vzhledem k bázím B a C", "matice zobrazení vůči bázím", "matice zobrazení v bázích", "matici lineárního zobrazení", "[A]^{X→Y}", "[A]_{B→C}"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 8
zdroj: "pozn. 6.11 ♥"
---

# matice lineárního zobrazení vzhledem k bázím

> [!lidsky] Lidsky
> Recept: vezmi j-tý vektor vstupní báze, zobraz ho a výsledek rozlož do výstupní báze; koeficienty napiš jako j-tý sloupec. Sloupců je dim V, řádků dim W.
>
> *Příklad:* derivace D z polynomů stupně ≤ 2 do polynomů stupně ≤ 1, báze 𝒳 = (1, x, x²) a 𝒴 = (1, x): D1 = 0 → (0; 0), Dx = 1 → (1; 0), Dx² = 2x → (0; 2). Tyto tři sloupce dají [D]^{𝒳→𝒴} = $\begin{pmatrix}0&1&0\\0&0&2\end{pmatrix}$.

**Formálně:** Buďte V, W lineární prostory nad 𝔽 konečné dimenze, 𝒳 = (x₁, …, xₘ) báze V a 𝒴 = (y₁, …, yₙ) báze W. Pro A ∈ Lin(V, W) je matice zobrazení A vzhledem k bázím 𝒳 a 𝒴 matice [A]^{𝒳→𝒴} = ([Ax₁]^𝒴 ⋯ [Axₘ]^𝒴) ∈ 𝔽^{n×m}, tj. j-tý sloupec tvoří souřadnice obrazu Axⱼ vzhledem k bázi 𝒴 (na cvičení [A]_{𝒳→𝒴})

**Definice:** [[LAG 08 – Matice lineárního zobrazení a součin matic#^def-matice-v-bazich|přednáška 8, 16. 10. 2026]] · pozn. 6.11 ♥ · k čemu je: [[věta o souřadnicích obrazu]]

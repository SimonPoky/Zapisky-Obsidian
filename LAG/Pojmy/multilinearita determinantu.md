---
aliases: []
tags: [pojem, LAG]
predmet: LAG
prednaska: 15
zdroj: "věta 10.12\*"
---

# multilinearita determinantu

> [!lidsky] Lidsky
> Determinant je lineární v každém sloupci (i řádku) zvlášť: součet v jednom sloupci se rozdělí na dva determinanty a násobek se vytkne. Lineární jako celek není, det(αA) = αⁿ det A.
>
> *Příklad:* det(1 2 + 3; 4 1 + 0) = det(1 2; 4 1) + det(1 3; 4 0) = −7 − 12 = −19, a přímo 1 · 1 − 5 · 4 = −19. Naopak det(2E₂) = 4 ≠ 2 det E₂.

**Formálně:** Pro každé i: det(a⃗₁ ⋯ a⃗ᵢ + αa⃗ᵢ′ ⋯ a⃗ₙ) = det(a⃗₁ ⋯ a⃗ᵢ ⋯ a⃗ₙ) + α det(a⃗₁ ⋯ a⃗ᵢ′ ⋯ a⃗ₙ), tj. (a⃗₁, …, a⃗ₙ) ↦ det(a⃗₁ ⋯ a⃗ₙ) je multilineární; důsledek det(αA) = αⁿ det A pro A ∈ 𝔽ⁿˣⁿ

**Definice:** [[LAG 15 – Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci#^veta-multilinearita|přednáška 15, 13. 11. 2026]] · věta 10.12\*

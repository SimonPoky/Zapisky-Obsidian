---
aliases: []
tags: [pojem, MA1]
predmet: MA1
prednaska: 14
zdroj: "handout 7B, slajd 4"
---

# nevlastní integrál

> [!lidsky] Lidsky
> Integrál funkce, která je spojitá jen do kraje intervalu (u kraje může utíkat do nekonečna nebo nebýt definovaná): spočítáš plochu do x a pošleš x ke kraji. Výsledek je ta limita, klidně i ±∞.
>
> *Příklad:* ∫₀¹ 1/√(1 − t) dt: ∫₀ˣ = 2 − 2√(1 − x) → 2 pro x → 1⁻, tedy integrál je 2. ∫₀¹ 1/t dt = lim_{x→0⁺} (−ln x) = +∞.

**Formálně:** f spojitá na každém [a; x] s x < b ⇒ ∫ₐᵇ f := lim_{x→b⁻} ∫ₐˣ f, pokud limita existuje (vlastní nebo nevlastní); analogicky f spojitá na každém [x; b] s a < x ⇒ ∫ₐᵇ f := lim_{x→a⁺} ∫ₓᵇ f

**Definice:** [[MA1 14 – Nevlastní integrál, délka křivky a objem rotačního tělesa#^def-nevlastni-integral|přednáška 14, 11. 11. 2026]] · handout 7B, slajd 4

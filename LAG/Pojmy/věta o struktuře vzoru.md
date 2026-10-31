---
aliases: ["{xₚ} + ker A", "partikulární řešení", "věta 7.18"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 11
zdroj: "věta 7.18"
---

# věta o struktuře vzoru

> [!lidsky] Lidsky
> Všechna řešení Ax = b jsou jedno konkrétní řešení plus cokoli z jádra. Vzor bodu je jádro posunuté o jedno řešení.
>
> *Příklad:* pro A = $\begin{pmatrix}0&2&1\\0&4&2\end{pmatrix}$ a b = (1; 2) je xₚ = (0; 0; 1), takže A⁻¹{(1; 2)} = {(0; 0; 1)} + span{(1; 0; 0), (0; 1; −2)}, rovina rovnoběžná s jádrem.

> [!obrazek] Jádro a obraz matice $\begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$
> ![[lag11-priklad.png]]
> *Vlevo $\mathbb{R}^3$: zelená rovina je $\ker A$ se zelenými generátory $(1; 0; 0)$ a $(0; 1; -2)$, modrá rovnoběžná rovina je vzor bodu $(1; 2)$, tedy zelená rovina posunutá o červený bod $(0; 0; 1)$. Vpravo $\mathbb{R}^2$: oranžová přímka je $\operatorname{im} A$, modrý bod $(1; 2)$ v ní leží, červený $(1; 0)$ ne a nemá žádný vzor.*

**Formálně:** V, W lineární prostory nad 𝔽, A ∈ Lin(V, W), b ∈ W, xₚ ∈ V s Axₚ = b ⇒ A⁻¹{b} = {xₚ} + ker A = {xₚ + x₀ | x₀ ∈ ker A}

**Definice:** [[LAG 11 – Jádro, obraz, hodnost a defekt#^veta-struktura-vzoru|přednáška 11, 30. 10. 2026]] · věta 7.18

---
aliases: ["věta 3.6", "kombinace předchozích"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 4
zdroj: "věta 3.6"
---

# alternativní definice lineární závislosti

> [!lidsky] Lidsky
> Posloupnost je závislá, právě když je v ní zbytečný vektor, který jde poskládat z ostatních. Dokonce existuje vektor, který jde poskládat jen z těch před ním.
>
> *Příklad:* ((1; 0), (0; 1), (2; 3)) je LZ, protože (2; 3) = 2·(1; 0) + 3·(0; 1) se dá poskládat z vektorů před ním.

**Formálně:** (x₁, …, xₙ) LZ ⟺ ∃i: xᵢ ∈ span{xⱼ | j ≠ i} ⟺ ∃i: xᵢ ∈ span{x₁, …, xᵢ₋₁}

**Definice:** [[LAG 04 – Lineární závislost a nezávislost#^veta-36|přednáška 4, 2. 10. 2026]] · věta 3.6

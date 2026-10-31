---
aliases: ["důsledek 4.15", "n LN vektorů je báze", "n generujících vektorů je báze"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 5
zdroj: "pozn. 4.15"
---

# věta o bázi z n vektorů

> [!lidsky] Lidsky
> Když znáš dimenzi a máš přesně tolik vektorů, stačí ověřit polovinu definice báze: buď nezávislost, nebo generování. V praxi se ověřuje nezávislost, protože je to jedna homogenní soustava.
>
> *Příklad:* dim ℝ² = 2 a ((1; 2), (3; 4)) jsou dva vektory. Stačí LN: α(1; 2) + β(3; 4) = (0; 0) dá α + 3β = 0 a 2α + 4β = 0, tedy α = β = 0. Je to báze a generování se už nekontroluje.

> [!obrazek] Kolik vektorů mají LN a generující posloupnosti
> ![[lag05-pocty.png]]
> *Prostor dimenze 3. Modře: nezávislá posloupnost má nejvýš 3 vektory a doplňováním dojde k bázi. Oranžově: generující posloupnost má aspoň 3 vektory a výběrem (věta 4.11) dojde k bázi. Zelená čára: báze má přesně 3 vektory.*

**Formálně:** Buď L lineární prostor nad 𝔽, dim L = n < ∞, x₁, …, xₙ ∈ L (přesně n vektorů). Pak jsou ekvivalentní: (x₁, …, xₙ) je báze L ⟺ (x₁, …, xₙ) je LN ⟺ (x₁, …, xₙ) generuje L

**Definice:** [[LAG 05 – Báze a dimenze#^dusledek-n|přednáška 5, 7. 10. 2026]] · pozn. 4.15

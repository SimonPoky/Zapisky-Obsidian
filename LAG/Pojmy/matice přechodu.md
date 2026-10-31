---
aliases: ["matice transformace souřadnic", "matice transformace souřadnic z báze B do báze C", "matici přechodu", "matice přechodu od báze", "T_{X→Y}"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 9
zdroj: "pozn. 6.26 ♥"
---

# matice přechodu

> [!lidsky] Lidsky
> Překladová tabulka mezi dvěma bázemi: do j-tého sloupce napíšeš, jak se j-tý vektor staré báze vyjádří ve vektorech nové báze. Pak souřadnice přeložíš jedním násobením.
>
> *Příklad:* pro 𝒳 = ((2; 1), (1; 1)) v ℝ² je [id]^{𝒳→ℰ} = $\begin{pmatrix}2&1\\1&1\end{pmatrix}$ (sloupce jsou vektory báze) a [id]^{ℰ→𝒳} = $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$, protože e₁ = (2; 1) − (1; 1) a e₂ = −(2; 1) + 2(1; 1).

> [!obrazek] Stejný vektor, dvoje souřadnice
> ![[lag09-prechod.png]]
> *Šedá mřížka patří kanonické bázi, zelená bázi $\mathcal{X}$ (modrý $\vec{x}_1$, oranžový $\vec{x}_2$). Červený vektor $\vec{v}$ je v kanonické mřížce $(1; 3)$, v zelené mřížce dva kroky po $\vec{x}_1$ a jeden po $\vec{x}_2$, tedy $[\vec{v}]^{\mathcal{X}} = (2; 1)$.*

**Formálně:** Buď V lineární prostor nad tělesem 𝔽 konečné dimenze a nechť 𝒳 = (x₁, …, xₙ) a 𝒴 jsou jeho báze. Matici [id_V]^{𝒳→𝒴} = ([x₁]^𝒴 ⋯ [xₙ]^𝒴) ∈ 𝔽^{n×n} nazýváme matice přechodu (matice transformace souřadnic) od báze 𝒳 k bázi 𝒴. Na cvičení T_{𝒳→𝒴}

**Definice:** [[LAG 09 – Algebra matic a transformace souřadnic#^def-matice-prechodu|přednáška 9, 21. 10. 2026]] · pozn. 6.26 ♥

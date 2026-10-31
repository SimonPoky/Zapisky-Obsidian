---
aliases: ["lineárně závislá", "lineárně závislá posloupnost", "lineárně závislé", "lineární závislosti", "LZ"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 4
zdroj: "pozn. 3.1 ♥"
---

# lineární závislost

> [!lidsky] Lidsky
> Vektory jsou závislé, když z nich jde nula namíchat i jinak než „od všeho nula dávek“. Pak se navzájem ruší a aspoň jeden z nich jde poskládat z ostatních, je v sadě zbytečný. Např. ((1; 2), (2; 4)): 2·(1; 2) − (2; 4) = 0.

> [!obrazek] Dvojice vektorů v $\mathbb{R}^2$
> ![[lag04-dvojice.png]]
> *Vlevo modrý $\vec{x}$ a oranžový $\vec{y}$ leží na jedné modré čárkované přímce, $\vec{y}$ je násobek $\vec{x}$: LZ. Uprostřed míří různými směry: LN. Vpravo červený nulový vektor: dvojice je LZ, i když $\vec{y}$ není násobkem $\vec{x}$, protože $\vec{x} = 0 \cdot \vec{y}$.*

> [!obrazek] Tři závislé vektory leží v jedné rovině
> ![[lag04-uloha35.png]]
> *Modrá x₁ a oranžová x₂ určují zelenou rovinu span{x₁, x₂}. Červená x₃ = x₁ + x₂ je úhlopříčka rovnoběžníku (tečkovaně), leží ve stejné rovině a nic nového nepřidá.*

**Formálně:** Buď L lineární prostor nad 𝔽, x₁, …, xₙ ∈ L. Posloupnost (x₁, …, xₙ) je lineárně závislá, jestliže lze 0 zapsat jako netriviální lineární kombinaci: (∃α₁, …, αₙ ∈ 𝔽, ne všechna nulová)(α₁x₁ + … + αₙxₙ = 0)

**Definice:** [[LAG 04 – Lineární závislost a nezávislost#^def-lz|přednáška 4, 2. 10. 2026]] · pozn. 3.1

---
aliases: ["integrál", "integrálu", "∫ᵤᵛ f", "integrál f od a do b", "axiomy integrálu"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 11
zdroj: "handout 6A, slajd 5"
---

# určitý integrál

> [!lidsky] Lidsky
> Číslo, které funkci na intervalu přiřadí „plochu pod grafem“ (se znaménkem). Zavádí se dvěma vlastnostmi, aditivitou a omezeností, a tím je určený jednoznačně.
>
> *Příklad:* ∫₀² x = 2 (trojúhelník se základnou 2 a výškou 2). Aditivita: ∫₀¹ x + ∫₁² x = 1/2 + 3/2 = 2; omezenost: 2 · 0 ≤ 2 ≤ 2 · 2.

> [!obrazek] Dva axiomy
> ![[ma111-aditivita-omezenost.png]]
> *Vlevo aditivita: oranžová plocha od a do u plus zelená od u do v je plocha od a do v. Vpravo omezenost: modrá plocha od u do v leží mezi zeleným obdélníkem s výškou min f a červeným čárkovaným s výškou max f.*

**Formálně:** Ať f je spojitá na [a; b]. Přiřazení (u, v) ↦ ∫ᵤᵛ f ∈ ℝ pro a ≤ u ≤ v ≤ b je určitý integrál, jestliže (1) ∫ₐᵛ f = ∫ₐᵘ f + ∫ᵤᵛ f a (2) (v − u) · min_{[u; v]} f ≤ ∫ᵤᵛ f ≤ (v − u) · max_{[u; v]} f

**Definice:** [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál#^def-urcity-integral|přednáška 11, 29. 10. 2026]] · handout 6A, slajd 5

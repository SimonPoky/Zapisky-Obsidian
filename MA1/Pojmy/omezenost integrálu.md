---
aliases: ["omezenosti integrálu", "omezenost určitého integrálu"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 11
zdroj: "handout 6A, slajd 5"
---

# omezenost integrálu

> [!lidsky] Lidsky
> Plocha pod grafem je aspoň obdélník s výškou minima a nejvýš obdélník s výškou maxima funkce na daném intervalu.
>
> *Příklad:* f(x) = x na [1; 2]: (2 − 1) · 1 = 1 ≤ ∫₁² x = 3/2 ≤ (2 − 1) · 2 = 2.

> [!obrazek] Dva axiomy
> ![[ma111-aditivita-omezenost.png]]
> *Vlevo aditivita: oranžová plocha od a do u plus zelená od u do v je plocha od a do v. Vpravo omezenost: modrá plocha od u do v leží mezi zeleným obdélníkem s výškou min f a červeným čárkovaným s výškou max f.*

**Formálně:** pro f spojitou na [a; b] a a ≤ u ≤ v ≤ b: (v − u) · min_{t∈[u; v]} f(t) ≤ ∫ᵤᵛ f ≤ (v − u) · max_{t∈[u; v]} f(t)

**Definice:** [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál#^def-urcity-integral|přednáška 11, 29. 10. 2026]] · handout 6A, slajd 5

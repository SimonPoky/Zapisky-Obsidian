---
aliases: ["matice rotace", "otočení roviny", "rotace", "R_α"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 8
zdroj: "pozn. 6.17"
---

# matice otočení

> [!lidsky] Lidsky
> První sloupec je místo, kam se otočí (1; 0), druhý, kam se otočí (0; 1). Ten je o čtvrt otáčky dál, proto má nahoře −sin α.

> [!obrazek] Kam se otočí jednotkové vektory
> ![[lag08-otoceni.png]]
> *Světlé šipky jsou $\vec{e}_1$, $\vec{e}_2$, syté jejich obrazy po otočení o $\alpha$ (zelené oblouky). Tečkované čáry ukazují složky: modrý obraz má $(\cos\alpha; \sin\alpha)$, oranžový $(-\sin\alpha; \cos\alpha)$.*

> [!obrazek] Co $A$ udělá s jednotkovým čtvercem
> ![[lag09-otoceni.png]]
> *Vlevo modrý $\vec{e}_1$ a oranžový $\vec{e}_2$, vpravo jejich obrazy $A\vec{e}_1 = (1; 1)$ a $A\vec{e}_2 = (-1; 1)$ (sloupce $[A]^{\mathcal{E}}$). Zelený čtverec je otočený o $45°$ (červený oblouk) a má stranu $\sqrt{2}$.*

**Formálně:** Otočení R_α: ℝ² → ℝ² o úhel α proti směru hodinových ručiček je lineární a [R_α]^𝓔 = (cos α  −sin α; sin α  cos α), tj. R_α(x; y) = (x cos α − y sin α; x sin α + y cos α)

**Definice:** [[LAG 08 – Matice lineárního zobrazení a součin matic#^def-matice-otoceni|přednáška 8, 16. 10. 2026]] · pozn. 6.17

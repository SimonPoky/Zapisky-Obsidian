---
aliases: ["sup L = inf U", "Riemannův integrál", "Darbouxův integrál"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 11
zdroj: "handout 6A, slajd 13"
---

# existence určitého integrálu

> [!lidsky] Lidsky
> Pro spojitou funkci se dolní a horní součty při zjemňování potkají v jednom čísle, a to je integrál. Tím je dokázáno, že integrál existuje.
>
> *Příklad:* x² na [0; 2]: dělení na 2 kousky dá L = 1, U = 5, na 4 kousky L = 1,75, U = 3,75; obojí se blíží 8/3 ≈ 2,67.

> [!obrazek] Dolní a horní součet
> ![[ma111-darboux.png]]
> *Modrý graf x² na [0; 2] rozdělený na čtyři proužky šířky 0,5. Vlevo zelené obdélníky s výškou minima (dolní součet 1,75), vpravo červené s výškou maxima (horní součet 3,75).*

**Formálně:** f spojitá na [a; b] ⇒ L(f; Δ) ≤ U(f; Δ), pro jemnější Δ′: L(f; Δ) ≤ L(f; Δ′) ≤ U(f; Δ′) ≤ U(f; Δ), a sup_Δ L(f; Δ) = inf_Δ U(f; Δ) = ∫ₐᵇ f

**Definice:** [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál#^veta-existence-integralu|přednáška 11, 29. 10. 2026]] · handout 6A, slajd 13

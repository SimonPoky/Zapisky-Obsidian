---
aliases: ["A(αx + y) = αAx + Ay"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 7
zdroj: "pozn. 6.3"
---

# kritérium linearity

> [!lidsky] Lidsky
> Místo dvou podmínek (sčítání, násobení) stačí ověřit jednu smíšenou.
>
> *Příklad:* A(a; b) = (a + b; 2a): A(α(a; b) + (c; d)) = (α(a + b) + c + d; 2αa + 2c) = αA(a; b) + A(c; d), takže je lineární. A(a; b) = (a + 1; b) ne: A(2·(0; 0) + (0; 0)) = (1; 0), ale 2·A(0; 0) + A(0; 0) = (3; 0).

> [!obrazek] Otočení zachovává rovnoběžník
> ![[lag07-aditivita.png]]
> *Vlevo modré $\vec{x}$, oranžové $\vec{y}$ a zelený součet. Vpravo totéž otočené o $90°$: obraz součtu je součet obrazů.*

**Formálně:** A: V → W je lineární ⟺ (∀x, y ∈ V)(∀α ∈ 𝔽)(A(αx + y) = αAx + Ay)

**Definice:** [[LAG 07 – Lineární zobrazení#^veta-kriterium-linearity|přednáška 7, 14. 10. 2026]] · pozn. 6.3

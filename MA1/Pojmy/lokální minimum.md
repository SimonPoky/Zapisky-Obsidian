---
aliases: ["lokálního minima", "lokální minima", "lokálním minimu", "lokální minimum v p"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 9
zdroj: "handout 4B, slajd 3"
---

# lokální minimum

> [!lidsky] Lidsky
> Dno důlku: dost blízko p nemá funkce menší hodnotu než f(p), i když jinde může klesnout níž.
>
> *Příklad:* f(x) = x³ − 3x má lokální minimum v p = 1: f(1) = −2 a blízko je větší, f(0,9) = −1,971 a f(1,1) = −1,969. Jinde jde níž, f(−3) = −18.

> [!obrazek] Lokální minimum a ostré lokální minimum
> ![[ma109-lokalni-minimum.png]]
> *Vlevo: na zeleném okolí (p − δ; p + δ) je graf rovný, f(p) je nejmenší hodnota, ale ne přísně, takže jde o lokální minimum, které není ostré. Vpravo: kolem červeného bodu p je všechno přísně výš, ostré lokální minimum (derivace v p navíc neexistuje).*

**Formálně:** f je definována v p a ve směru x → p; f má v p lokální minimum ⇔ f(p) ≤ f ve směru x → p, tj. ∃δ > 0 ∀x ∈ (p − δ; p + δ), x ≠ p: f(p) ≤ f(x)

**Definice:** [[MA1 09 – Taylorův polynom, extrémy a monotonie#^def-lokalni-extrem|přednáška 9, 21. 10. 2026]] · handout 4B, slajd 3

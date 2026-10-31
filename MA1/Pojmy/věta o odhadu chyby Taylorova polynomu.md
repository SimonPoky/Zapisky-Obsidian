---
aliases: ["odhad chyby", "odhadu chyby", "Lagrangeův tvar zbytku", "chyba Taylorovy aproximace"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 9
zdroj: "handout 4A, slajd 22"
---

# věta o odhadu chyby Taylorova polynomu

> [!lidsky] Lidsky
> Chyba Taylorova polynomu vypadá jako jeho další člen, jen s derivací v neznámém bodě t mezi x a p. Omezíš-li tu derivaci, máš zaručenou mez chyby. Pro n = 0 je to Lagrangeova věta.
>
> *Příklad:* eˣ ≈ 1 + x pro x = 0,1: chyba je e^t/2 · 0,01 pro nějaké t ∈ (0; 0,1), tedy nejvýš e^{0,1}/2 · 0,01 < 0,006. Skutečně e^{0,1} − 1,1 = 0,0052.

> [!obrazek] Chyba Taylorovy aproximace
> ![[ma109-chyba.png]]
> *Vlevo červeně chyba $e^x - T_2(e^x, 0)(x)$, šedě čárkovaně $x^2$: chyba je u nuly mnohem plošší. Vpravo oranžově podíl chyba / $x^2$, který jde v nule k zelené hodnotě 0, přesně jak říká věta (1).*

**Formálně:** f má n + 1 derivací na otevřeném intervalu (a; b), p ∈ (a; b) ⇒ pro každé x ∈ (a; b) existuje t mezi x a p: f(x) − Tₙ(f, p)(x) = f⁽ⁿ⁺¹⁾(t)/(n + 1)! · (x − p)ⁿ⁺¹

**Definice:** [[MA1 09 – Taylorův polynom, extrémy a monotonie#^veta-odhad-chyby|přednáška 9, 21. 10. 2026]] · handout 4A, slajd 22

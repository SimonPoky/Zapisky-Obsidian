---
aliases: ["derivace", "derivaci", "derivací", "f′(p)", "má derivaci", "derivovat"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 7
zdroj: "handout 3B, slajd 3"
---

# derivace v bodě

> [!lidsky] Lidsky
> Okamžitá rychlost změny funkce v bodě p: limita průměrných změn (f(p+h) − f(p))/h pro h → 0. Geometricky směrnice tečny ke grafu. Musí to být reálné číslo.
>
> *Příklad:* f(x) = x², p = 3: (f(3 + h) − f(3))/h = (6h + h²)/h = 6 + h → 6, takže f′(3) = 6. Pro |x| v 0 vyjde |h|/h = ±1, limita neexistuje a derivace taky ne.

> [!obrazek] Sečny se blíží k tečně
> ![[ma107-secny.png]]
> *Modrý graf f, červený bod [p; f(p)]. Oranžové sečny vedou k bodům x₁, x₂, x₃, x₄, které se blíží k p; čím blíž, tím je sečna sytější. Jejich směrnice se blíží ke směrnici zelené tečny, a to je f′(p).*

> [!obrazek] Zub v nule
> ![[ma107-abs.png]]
> *Modrý graf |x| má v červeném bodě zub. Zleva se k němu přimyká oranžová tečna se směrnicí −1, zprava zelená se směrnicí 1. Jedna společná tečna neexistuje.*

**Formálně:** f′(p) = lim_{h→0} (f(p+h) − f(p))/h, pokud tato limita existuje a je vlastní; ekvivalentně f′(p) = lim_{x→p} (f(x) − f(p))/(x − p)

**Definice:** [[MA1 07 – Derivace a Carathéodoryho trik#^def-derivace|přednáška 7, 14. 10. 2026]] · handout 3B, slajd 3

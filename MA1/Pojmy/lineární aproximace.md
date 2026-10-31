---
aliases: ["T₁(f, p)", "T1", "Taylorův polynom stupně 1", "lineární aproximaci"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 8
zdroj: "handout 4A, slajd 15"
---

# lineární aproximace

> [!lidsky] Lidsky
> Nahrazení funkce její tečnou blízko bodu p. Chyba je zanedbatelná i vůči vzdálenosti x − p.
>
> *Příklad:* √x u p = 4: T₁(x) = 2 + (x − 4)/4, takže √4,1 ≈ 2,025; přesně je √4,1 = 2,02485…

> [!obrazek] Tečna jako aproximace
> ![[ma108-linearni-aproximace.png]]
> *Vlevo modře f(x) = eˣ⁻¹, zeleně její tečna T₁(f, 1)(x) = x v červeném bodě, červená úsečka je chyba v x = 1,9. Vpravo červeně chyba jako funkce vzdálenosti x − p, šedě čárkovaně samotné x − p a oranžově podíl chyba / (x − p), který jde v nule k 0.*

**Formálně:** f′(p) existuje, T₁(f, p)(x) = f(p) + f′(p)(x − p) ⇒ lim_{x→p} (f(x) − T₁(f, p)(x))/(x − p) = 0

**Definice:** [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo#^def-linearni-aproximace|přednáška 8, 15. 10. 2026]] · handout 4A, slajd 15

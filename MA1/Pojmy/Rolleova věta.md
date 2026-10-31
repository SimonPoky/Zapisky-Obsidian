---
aliases: ["Rolle", "Rolleovy věty", "Rolleovu větu", "první věta o střední hodnotě"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 8
zdroj: "handout 4A, slajd 4"
---

# Rolleova věta

> [!lidsky] Lidsky
> Když hladká funkce začne a skončí ve stejné výšce, má někde uvnitř vodorovnou tečnu, třeba na vrcholu nebo na dně.
>
> *Příklad:* f(x) = x² − 2x na [0; 2]: f(0) = f(2) = 0 a f′(t) = 2t − 2 = 0 v t = 1, kde je dno paraboly.

> [!obrazek] Rolle a Lagrange
> ![[ma108-rolle-lagrange.png]]
> *Vlevo: modrý graf začíná a končí ve stejné výšce (červené body, šedá čára). Ve vrcholu t je zelená tečna vodorovná, f′(t) = 0. Vpravo: oranžová sečna spojuje červené krajní body; v bodě t je zelená tečna s ní rovnoběžná, takže f′(t) je směrnice sečny.*

> [!obrazek] Proč je v maximu derivace nulová
> ![[ma108-rolle-dukaz.png]]
> *Červený bod je maximum v t. Oranžové sečny k bodům vpravo (h > 0) mají směrnici ≤ 0, zelené sečny k bodům vlevo (h < 0) směrnici ≥ 0. Derivace je limita obou, takže musí být zároveň ≤ 0 i ≥ 0, tedy 0 (šedá vodorovná tečna).*

**Formálně:** f má první derivaci na [a; b] a f(a) = f(b) ⇒ ∃t ∈ (a; b): f′(t) = 0

**Definice:** [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo#^veta-rolle|přednáška 8, 15. 10. 2026]] · handout 4A, slajd 4

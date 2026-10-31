---
aliases: ["Cauchy", "Cauchyovy věty", "Cauchyovu větu", "třetí věta o střední hodnotě", "Cauchyova věta o střední hodnotě"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 8
zdroj: "handout 4A, slajd 7"
---

# Cauchyova věta

> [!lidsky] Lidsky
> Lagrange pro dvě funkce se společným bodem t: křivka [g(x); f(x)] má někde tečnu rovnoběžnou s tětivou mezi krajními body.
>
> *Příklad:* f(x) = x², g(x) = x³ na [0; 1]: (1 − 0)·3t² = (1 − 0)·2t dá t = 2/3 ∈ (0; 1).

> [!obrazek] Cauchyova věta geometricky
> ![[ma108-cauchy.png]]
> *Modrá křivka x ↦ [g(x); f(x)] se smí i zatočit do smyčky (není to graf funkce). Oranžová tětiva spojuje červené krajní body. V zeleném bodě je tečna ke křivce s tětivou rovnoběžná.*

**Formálně:** f, g mají první derivaci na [a; b] ⇒ ∃t ∈ (a; b): (f(b) − f(a))·g′(t) = (g(b) − g(a))·f′(t); je-li navíc g′ ≠ 0 na (a; b), pak g(a) ≠ g(b) a (f(b) − f(a))/(g(b) − g(a)) = f′(t)/g′(t)

**Definice:** [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo#^veta-cauchy|přednáška 8, 15. 10. 2026]] · handout 4A, slajd 7

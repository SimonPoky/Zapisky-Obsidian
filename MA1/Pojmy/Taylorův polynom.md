---
aliases: ["Taylorova polynomu", "Taylorovým polynomem", "Tₙ(f, p)", "Taylorův polynom stupně ≤ n"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 9
zdroj: "handout 4A, slajd 16"
---

# Taylorův polynom

> [!lidsky] Lidsky
> Polynom, který v bodě p kopíruje hodnotu funkce i jejích prvních n derivací, a proto ji blízko p věrně napodobuje. Pro n = 1 je to tečna.
>
> *Příklad:* cos x a p = 0: f(0) = 1, f′(0) = 0, f″(0) = −1, takže T₂(x) = 1 − x²/2. Pro x = 0,1 dá 0,995, přesně je cos 0,1 = 0,99500…

**Formálně:** f má alespoň n derivací v p: Tₙ(f, p)(x) = Σ_{k=0}^{n} f⁽ᵏ⁾(p)/k! · (x − p)ᵏ = f(p) + f′(p)(x − p) + f″(p)/2 · (x − p)² + … + f⁽ⁿ⁾(p)/n! · (x − p)ⁿ

**Definice:** [[MA1 09 – Taylorův polynom, extrémy a monotonie#^def-taylor|přednáška 9, 21. 10. 2026]] · handout 4A, slajd 16

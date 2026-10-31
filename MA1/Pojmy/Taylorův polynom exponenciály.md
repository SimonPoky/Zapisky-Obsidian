---
aliases: ["Taylorův polynom eˣ", "Taylorova polynomu exponenciály"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 9
zdroj: "handout 4A, slajd 20"
---

# Taylorův polynom exponenciály

> [!lidsky] Lidsky
> Všechny derivace eˣ jsou eˣ a e⁰ = 1, takže zbudou jen faktoriály: 1 + x + x²/2 + x³/6 + … Je dobré si ho pamatovat.

> [!obrazek] Taylorovy polynomy $e^x$ a $\sin x$
> ![[ma109-taylor.png]]
> *Vlevo modře $e^x$, oranžově tečna $T_1$, zeleně $T_2$, červeně čárkovaně $T_3$. Vpravo modře $\sin x$, oranžově $T_1 = T_2 = x$, zeleně $T_3$, červeně čárkovaně $T_5$. Čím vyšší stupeň, tím delší úsek kolem středu (černý bod) polynom věrně kopíruje; daleko od středu se ale všechny rozjedou.*

**Formálně:** Tₙ(eˣ, p)(x) = Σ_{k=0}^{n} eᵖ/k! · (x − p)ᵏ, speciálně Tₙ(eˣ, 0)(x) = Σ_{k=0}^{n} xᵏ/k! = 1 + x + x²/2! + … + xⁿ/n!

**Definice:** [[MA1 09 – Taylorův polynom, extrémy a monotonie#^veta-taylor-exp|přednáška 9, 21. 10. 2026]] · handout 4A, slajd 20

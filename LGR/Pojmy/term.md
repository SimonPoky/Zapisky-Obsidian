---
aliases: ["termy", "termu", "termů"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 8"
---

# term

> [!lidsky] Lidsky
> Jméno objektu včetně toho, jak vznikl: x, a, f(f(a)) „následník následníka dvojky“. Nic netvrdí, nemá pravdivostní hodnotu.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

**Formálně:** (1) proměnná a konstantní symbol jsou termy; (2) f ∈ Func arity n, t₁, …, tₙ termy ⇒ f(t₁, …, tₙ) term; (3) nic jiného, jen konečně mnoho kroků 1, 2

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-term|přednáška 8, 23. 10. 2026]] · handout 5, slajd 8

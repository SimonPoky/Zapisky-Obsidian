---
aliases: ["volný výskyt proměnné", "volné výskyty"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 13"
---

# volný výskyt

> [!lidsky] Lidsky
> Výskyt proměnné, nad kterým není kvantifikátor s touto proměnnou; čeká na dosazení, jako n v ∑ᵢ₌₁ⁿ i².
>
> *Příklad:* v ∀x P(x, y) je výskyt y volný a výskyty x vázané. Ve formuli S(x) ∧ ∀x L(x) je první x volné a druhé vázané.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

**Formálně:** výskyt x ve φ je volný ⟺ na cestě od jeho listu ke kořeni syntaktického stromu neleží ∀x ani ∃x

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-volny-vazany|přednáška 8, 23. 10. 2026]] · handout 5, slajd 13

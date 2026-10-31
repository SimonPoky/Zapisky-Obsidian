---
aliases: ["vázané proměnné", "vázaná"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 13"
---

# vázaná proměnná

> [!lidsky] Lidsky
> Proměnná, která má ve formuli aspoň jeden vázaný výskyt. V ∀x P(x, f(x)) ∨ S(x) je x vázaná i volná.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

**Formálně:** x je vázaná ve φ ⟺ x má ve φ aspoň jeden vázaný výskyt (může být zároveň volná)

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-volny-vazany|přednáška 8, 23. 10. 2026]] · handout 5, slajd 13

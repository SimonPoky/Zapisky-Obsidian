---
aliases: ["vázaný výskyt proměnné", "vázané výskyty"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 13"
---

# vázaný výskyt

> [!lidsky] Lidsky
> Výskyt proměnné, který „patří“ nějakému kvantifikátoru, jako i v ∑ᵢ i²: nic se za něj nedosazuje.
>
> *Příklad:* v ∃y P(x, y) je výskyt y vázaný (patří ∃y) a výskyt x volný. Formule říká „k x existuje y s P(x, y)“; za y se nic nedosazuje.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

**Formálně:** výskyt x ve φ je vázaný ⟺ na cestě od jeho listu ke kořeni syntaktického stromu leží ∀x nebo ∃x

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-volny-vazany|přednáška 8, 23. 10. 2026]] · handout 5, slajd 13

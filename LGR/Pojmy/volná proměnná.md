---
aliases: ["volné proměnné", "volná"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 13"
---

# volná proměnná

> [!lidsky] Lidsky
> Proměnná, která má ve formuli aspoň jeden volný výskyt. Pravdivost formule na ní závisí.
>
> *Příklad:* v P(x, a) ∨ ∀y S(y) je x volná a y vázaná. Na ℕ s P jako „<“, ⟦a⟧ = 2 a S jako „je sudé“ je ∀y S(y) nepravdivé, takže formule platí pro x = 1 (1 < 2) a pro x = 5 ne: záleží na x.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

**Formálně:** x je volná ve φ ⟺ x má ve φ aspoň jeden volný výskyt (může být zároveň vázaná)

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-volny-vazany|přednáška 8, 23. 10. 2026]] · handout 5, slajd 13

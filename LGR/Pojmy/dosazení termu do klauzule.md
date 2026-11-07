---
aliases: ["α[x := t]", "dosazení termu", "instance klauzule", "dosazení za proměnnou"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 11
zdroj: "handout 7, slajd 21"
---

# dosazení termu do klauzule

> [!lidsky] Lidsky
> Co platí pro všechny prvky universa, platí i pro ty, které jmenuje term: za obecně vázanou proměnnou smíš dosadit libovolný term a dostaneš důsledek. Takhle se v rezoluci hledá konflikt.
>
> *Příklad:* ∀x (P(x) ∨ Q(x)) ⊨ P(a) ∨ Q(a) a ⊨ ∀y (P(f(y)) ∨ Q(f(y))). Za konstantu a ani za f(x) dosadit nejde.

**Formálně:** α = ∀x γ klauzule, t term ⇒ α ⊨ γ[x := t] (proměnné z t zůstanou obecně vázané)

**Definice:** [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice#^veta-dosazeni|přednáška 11, 6. 11. 2026]] · handout 7, slajd 21

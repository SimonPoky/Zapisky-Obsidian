---
aliases: []
tags: [pojem, LGR]
predmet: LGR
prednaska: 10
zdroj: "handout 6, slajdy 18–23"
---

# vytýkání kvantifikátorů

> [!lidsky] Lidsky
> ∀ je velká konjunkce, ∃ velká disjunkce: ∀x jde vytknout před ∧ a ∃x před ∨, opačně platí jen jeden směr důsledku. Když druhá podformule neobsahuje volné x, jde vytknout cokoliv; z předpokladu implikace se kvantifikátor otočí.
>
> *Příklad:* ∀x P(x) ∨ ∀x Q(x) ⊨ ∀x (P(x) ∨ Q(x)), ale ne naopak: U = {0, 1, 2}, ⟦P⟧ = {0, 1}, ⟦Q⟧ = {1, 2}. S jinými jmény ∀x P(x) ∨ ∀y Q(y) |=| ∀x ∀y (P(x) ∨ Q(y)).

**Formálně:** ∀x α ∧ ∀x β |=| ∀x (α ∧ β); ∃x α ∨ ∃x β |=| ∃x (α ∨ β); ∀x α ∨ ∀x β ⊨ ∀x (α ∨ β); ∃x (α ∧ β) ⊨ ∃x α ∧ ∃x β; β bez volné x ⇒ (∇x α) ◇ β |=| ∇x (α ◇ β) pro ∇ ∈ {∀, ∃}, ◇ ∈ {∧, ∨}, (∇x α) ⇒ β |=| Δx (α ⇒ β), β ⇒ ∇x α |=| ∇x (β ⇒ α), Δ opačný k ∇

**Definice:** [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace#^veta-vytykani-kvantifikatoru|přednáška 10, 5. 11. 2026]] · handout 6, slajdy 18–23

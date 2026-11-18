---
aliases: []
tags: [pojem, LGR]
predmet: LGR
prednaska: 10
zdroj: "handout 7, slajdy 8–11"
---

# skolemizace

> [!lidsky] Lidsky
> Odstranění ∃: svědka pojmenuješ novým symbolem. Pokud svědek závisí na proměnných z ∀ před ním, pojmenuješ ho funkcí těchto proměnných. Zachová jen splnitelnost, ne modely.
>
> *Příklad:* ∃x P(x) → P(c); ∀x ∃y R(x, y) → ∀x R(x, f(x)); ∃x ∀y ∃z (R(x, y) ∧ R(y, z)) → ∀y (R(c, y) ∧ R(y, f(y))).

**Formálně:** y volná a jen volná v α: ∃y α ≈ α[y := c], ∀x₁ … ∀xₙ ∃y α ≈ ∀x₁ … ∀xₙ α[y := f(x₁, …, xₙ)], c, f nové symboly (f arity n); skolemizovaná sentence ⊨ původní, opačně obecně ne; skolemizuje se postupně od prvního ∃

**Definice:** [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace#^def-skolemizace|přednáška 10, 5. 11. 2026]] · handout 7, slajdy 8–11

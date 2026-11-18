---
aliases: ["rezoluční princip v predikátové logice", "R*(S) v predikátové logice"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajd 34"
---

# rezoluční princip predikátové logiky

> [!lidsky] Lidsky
> Stejně jako ve výrokové logice: konečná množina klauzulí je nesplnitelná, právě když rezolucí vznikne ff. Výroba rezolvent R*(S) se ale nemusí zastavit, takže splnitelnost se tím poznat nemusí.
>
> *Příklad:* {∀x ¬S(f(x)), S(f(a))}: x := a dá ff, množina je nesplnitelná. {∀x ¬S(f(x)), S(a)}: žádná rezolventa, R*(S) = S, splnitelná.

**Formálně:** S konečná množina klauzulí s různými proměnnými, R⁰(S) = S, Rⁱ⁺¹(S) = R(Rⁱ(S)), R*(S) = ⋃ Rⁱ(S): S nesplnitelná ⟺ ff ∈ R*(S)

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^veta-rezolucni-princip-pl|přednáška 12, 12. 11. 2026]] · [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-populace-pl|populace R*(S)]] · handout 7, slajd 34

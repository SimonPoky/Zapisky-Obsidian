---
aliases: []
tags: [pojem, LGR]
predmet: LGR
prednaska: 10
zdroj: "handout 6, slajd 9"
---

# sémantický důsledek predikátové logiky

> [!lidsky] Lidsky
> Ze sentencí S plyne sentence φ: v žádném světě, kde platí všechny předpoklady, nemůže závěr selhat. Vyvrátit stačí jedna interpretace (model S, který není modelem φ), dokázat je potřeba úvaha o libovolném modelu.
>
> *Příklad:* ∀x P(x) ⊨ ∃x P(x), protože U ≠ ∅. Ale ∃x P(x) ⊭ ∀x P(x): U = ℕ, ⟦P⟧ = sudá čísla je model první, ne druhé.

**Formálně:** S ⊨ φ ⟺ každý model množiny sentencí S je modelem φ; ⊨ φ ⟺ φ je tautologie; S ⊨ φ ⟺ S ∪ {¬φ} je nesplnitelná; S ∪ {φ} ⊨ ψ ⟺ S ⊨ φ ⇒ ψ

**Definice:** [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace#^def-semanticky-dusledek-pl|přednáška 10, 5. 11. 2026]] · handout 6, slajd 9 · převod na nesplnitelnost: [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace#^veta-prevod-na-nesplnitelnost|slajd 10]]

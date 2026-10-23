---
aliases: ["rezoluční tabulky", "rezoluční tabulce", "rezoluční tabulkou"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 5
zdroj: "slajdy 23–25"
---

# rezoluční tabulka

> [!lidsky] Lidsky
> Úsporná rezoluce: proměnné se „vyrezolvují“ jedna po druhé a klauzule s už zpracovanou proměnnou se zahodí. Na konci zbyde {ff} (nesplnitelná), nebo ∅ (splnitelná); svědka dostaneš pozpátku.
>
> *Příklad:* S = {a ∨ b, ¬a ∨ b, ¬b}. Eliminace a: rezolventa b, zbude {¬b, b}. Eliminace b: rezolventa ff, zbude {ff}, takže S je nesplnitelná.

**Formálně:** S konečná, v základním tvaru, proměnné x₁, …, xₙ; pro i = 1, …, n: S := S₀ ∪ R_{xᵢ}; konec S = {ff} ⇒ nesplnitelná, S = ∅ ⇒ splnitelná

**Definice:** [[LGR 05 – Rezoluční princip#^def-rezolucni-tabulka|přednáška 5, 9. 10. 2026]] · slajdy 23–24

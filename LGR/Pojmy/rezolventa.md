---
aliases: ["rezolventy", "rezolvent", "rezoluce", "rezoluční metoda", "rezoluční metodou"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 4
zdroj: "slajd 14"
---

# rezolventa

> [!lidsky] Lidsky
> Ze dvou klauzulí, kde je stejná proměnná jednou s negací a jednou bez, ji škrtneš a zbytky spojíš „nebo“. Výsledek z obou plyne. Když vyjde prázdná klauzule ff, množina je nesplnitelná.
>
> *Příklad:* z klauzulí a ∨ b a ¬b ∨ c vznikne škrtnutím b rezolventa a ∨ c. Z a a ¬a vznikne prázdná klauzule ff, takže {a, ¬a} je nesplnitelná.

**Formálně:** res_x(α ∨ x, β ∨ ¬x) = α ∨ β; {α ∨ x, β ∨ ¬x} ⊨ α ∨ β; res_x(x, ¬x) = ff

**Definice:** [[LGR 04 – Sémantický důsledek a klauzální tvar#^def-rezolventa|přednáška 4, 8. 10. 2026]] · slajd 14 · přidání rezolventy nemění pravdivost: [[LGR 05 – Rezoluční princip#^res-dusledek|přednáška 5, slajd 15]]

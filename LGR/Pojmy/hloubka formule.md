---
aliases: ["hloubka", "hloubku formule", "hl(φ)"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 1
zdroj: "k slajdu 7"
---

# hloubka formule

> [!lidsky] Lidsky
> Počet pater syntaktického stromu na nejdelší cestě od kořene k listu. Proměnná má hloubku 0, každá spojka přidá 1.
>
> *Příklad:* hl(¬(a ∧ b)) = 1 + hl(a ∧ b) = 1 + 1 = 2. hl((a ∨ b) ⇒ ¬¬c) = 1 + max{hl(a ∨ b), hl(¬¬c)} = 1 + max{1, 2} = 3.

**Formálně:** hl(a) = 0; hl(¬α) = 1 + hl(α); hl(α ∘ β) = 1 + max{hl(α), hl(β)}

**Definice:** [[LGR 01 – Syntax a sémantika výrokové logiky#^def-hloubka|přednáška 1, 24. 9. 2026]] · k slajdu 7

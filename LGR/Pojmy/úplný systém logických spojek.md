---
aliases: ["úplný systém spojek", "úplné systémy spojek", "ÚSS"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 2
zdroj: "k slajdům 19–22"
---

# úplný systém logických spojek

> [!lidsky] Lidsky
> Sada spojek, kterou jde zapsat každá booleovská funkce. Úplné jsou {¬, ∧, ∨}, {¬, ⇒}, {|}, {↓}; neúplné {¬} a {∧, ∨, ⇒, ⇔}.

> [!obrazek] Všechno z jediné spojky NAND
> ![[lgr02-nand.png]]
> *Syntaktické stromy jen se spojkou | (modře). Vlevo negace: a | a je pravdivé, právě když a není. Vpravo konjunkce: (a | b) je ¬(a ∧ b) a další | ho znovu zneguje. Z ¬ a ∧ se pak dá složit cokoliv.*

> [!obrazek] Všechno z jediné spojky NOR
> ![[lgr02-nor.png]]
> *Stejný trik se spojkou ↓ (modře). Vlevo negace: a ↓ a je pravdivé, právě když a není. Vpravo disjunkce: (a ↓ b) je ¬(a ∨ b) a další ↓ ho znovu zneguje. Z ¬ a ∨ se pak dá složit cokoliv.*

**Formálně:** ∀f : {0, 1}ⁿ → {0, 1} ∃φ ze spojek systému, která určuje f

**Definice:** [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek#^def-uss|přednáška 2, 25. 9. 2026]] · k slajdům 19–22

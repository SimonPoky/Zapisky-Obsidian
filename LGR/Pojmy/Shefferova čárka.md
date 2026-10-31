---
aliases: ["NAND", "Shefferovy čárky"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 2
zdroj: "slajdy 19–21"
---

# Shefferova čárka

> [!lidsky] Lidsky
> NAND, „ne obojí zároveň“: nepravdivá jen pro 1, 1. Sama tvoří úplný systém spojek, proto se z ní staví čipy.
>
> *Příklad:* a | b = „ne obojí“: 1 | 1 = 0, jinak 1. Negace je a | a, konjunkce (a | b) | (a | b) |=| a ∧ b, protože čárka sama se sebou neguje.

> [!obrazek] Všechno z jediné spojky NAND
> ![[lgr02-nand.png]]
> *Syntaktické stromy jen se spojkou | (modře). Vlevo negace: a | a je pravdivé, právě když a není. Vpravo konjunkce: (a | b) je ¬(a ∧ b) a další | ho znovu zneguje. Z ¬ a ∧ se pak dá složit cokoliv.*

**Formálně:** α | β |=| ¬(α ∧ β); ¬α |=| α | α

**Definice:** [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek#^def-spojky|přednáška 2, 25. 9. 2026]] · slajdy 19–21 · vyjádření základními spojkami: [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek#^veta-vyjadreni-spojek|slajd 21]]

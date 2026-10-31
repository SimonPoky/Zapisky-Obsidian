---
aliases: ["supremum pomocí ε", "ε-charakterizace suprema"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 2
zdroj: "handout 1B, slajd 13"
---

# charakterizace suprema

> [!lidsky] Lidsky
> Supremum je strop, který nejde snížit ani o kousek: je nad celou množinou, a kdybys ho snížil o libovolně malé ε, nějaký prvek množiny už bude nad ním.
>
> *Příklad:* M = [0; 1), s = 1: všechna x ∈ M jsou ≤ 1 a pro ε = 0,01 leží v M číslo 0,995 > 1 − 0,01. Číslo 1,1 supremum není: pro ε = 0,05 v M žádné x nad 1,05 neleží.

> [!obrazek] Strop, který nejde snížit
> ![[ma102-supremum.png]]
> *M = {1 − 1/n}: čárky jsou prvky M, prázdné kolečko je s = sup M = 1 (v M neleží). Zelený pás (s − ε; s] obsahuje nekonečně mnoho prvků M, ať je ε jakkoli malé; nad s neleží nic.*

**Formálně:** M ⊆ ℝ, s ∈ ℝ: s = sup M ⟺ (1) (∀x ∈ M)(x ≤ s) a (2) (∀ε > 0)(∃x ∈ M)(s − ε < x ≤ s)

**Definice:** [[MA1 02 – Celá, racionální a reálná čísla#^veta-eps-sup|přednáška 2, 24. 9. 2026]] · handout 1B, slajd 13

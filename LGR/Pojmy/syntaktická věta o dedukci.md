---
aliases: ["věta o dedukci pro ⊢"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4, slajd 13"
---

# syntaktická věta o dedukci

> [!lidsky] Lidsky
> „Chci dokázat φ ⇒ ψ, tak předpokládám φ a dokážu ψ.“ Předpoklad se dá přesunout do implikace a zpět.
>
> *Příklad:* z {a ∧ b} ⊢ a (∧e₁) plyne ⊢ (a ∧ b) ⇒ a: předpoklad a ∧ b se změní na pomocný předpoklad boxu a ⇒i ho přesune do implikace.

**Formálně:** pro každou S, φ, ψ: S ∪ {φ} ⊢ ψ ⟺ S ⊢ φ ⇒ ψ (⇒: φ otevře box, ⇒i; ⇐: přidej φ, ⇒e)

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-synt-dedukce|přednáška 7, 22. 10. 2026]] · handout 4, slajd 13

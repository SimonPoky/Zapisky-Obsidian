---
aliases: ["existence DNF a CNF", "věty o normálních formách"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 3
zdroj: "slajd 14"
---

# věta o normálních formách

> [!lidsky] Lidsky
> Každou formuli jde přepsat do DNF i do CNF tak, že se nezmění její tabulka. Takových tvarů je obecně víc, normální forma není jednoznačná.
>
> *Příklad:* a ⇔ b má DNF (a ∧ b) ∨ (¬a ∧ ¬b) a CNF (¬a ∨ b) ∧ (a ∨ ¬b). Normální forma není jednoznačná: a i (a ∧ b) ∨ (a ∧ ¬b) jsou DNF téže formule a.

**Formálně:** ∀φ ∃ φ_DNF v DNF a φ_CNF v CNF: φ ⊨⊨ φ_DNF a φ ⊨⊨ φ_CNF

**Definice:** [[LGR 03 – Disjunktivní a konjunktivní normální forma#^veta-nf|přednáška 3, 1. 10. 2026]] · slajd 14

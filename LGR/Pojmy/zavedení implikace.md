---
aliases: ["⇒i", "pravidlo ⇒i", "přímý důkaz implikace"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 6
zdroj: "slajdy 5–8 (prez. 4)"
---

# zavedení implikace

> [!lidsky] Lidsky
> Přímý důkaz implikace: předpokládej φ (otevři box), odvoď ψ, zavři box a máš φ ⇒ ψ, už bez předpokladu.
>
> *Příklad:* ⊢ (a ∧ b) ⇒ a: box 1. a ∧ b (P), 2. a (∧e₁ 1); po uzavření 3. (a ∧ b) ⇒ a (⇒i 1–2).

**Formálně:** box s pomocným předpokladem φ končící ψ ⊢ φ ⇒ ψ; respektuje pravdivost: S ∪ {φ} ⊨ ψ ⇒ S ⊨ φ ⇒ ψ (věta o dedukci)

**Definice:** [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^def-impl-i|přednáška 6, 15. 10. 2026]] · slajdy 5–8 · korektnost: [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^impl-i-korektni|přednáška 6, 15. 10. 2026]]

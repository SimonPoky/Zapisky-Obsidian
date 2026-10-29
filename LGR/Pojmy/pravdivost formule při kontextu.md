---
aliases: ["pravdivá v I při ρ", "pravdivost formule v interpretaci", "pravdivá při kontextu"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 9
zdroj: "handout 5, slajdy 26–28"
---

# pravdivost formule při kontextu

> [!lidsky] Lidsky
> Formule se vyhodnotí odspodu stromu: atomickou formuli rozhodneš dosazením hodnot termů do relace, spojky jako ve výrokové logice, ∃x „aspoň jedno dosazení za x vyjde“, ∀x „každé dosazení za x vyjde“.
>
> *Příklad:* na ℕ při ρ: x ↦ 7, y ↦ 15: y < x znamená 15 < 7, nepravdivá; ∃y (y < x) je pravdivá díky updatu y := 1 (1 < 7).

**Formálně:** v I = (U, ⟦−⟧) při ρ: P(t₁, …, tₙ) pravdivá ⟺ (⟦t₁⟧ρ, …, ⟦tₙ⟧ρ) ∈ ⟦P⟧; t₁ = t₂ pravdivá ⟺ ⟦t₁⟧ρ = ⟦t₂⟧ρ; spojky jako ve výrokové logice; ∀x φ pravdivá ⟺ φ pravdivá při každém ρ[x:=d], d ∈ U; ∃x φ pravdivá ⟺ φ pravdivá při aspoň jednom ρ[x:=d], d ∈ U

**Definice:** [[LGR 09 – Pravdivost formulí, model a tautologie#^def-pravdivost-formule|přednáška 9, 29. 10. 2026]] · handout 5, slajdy 26–28

---
aliases: []
tags: [pojem, LGR]
predmet: LGR
prednaska: 10
zdroj: "handout 6, slajdy 25–27"
---

# prenexní tvar

> [!lidsky] Lidsky
> Všechny kvantifikátory vpředu, za nimi formule bez kvantifikátorů (otevřené jádro). Získá se přejmenováním vázaných proměnných, převodem na ¬, ∧, ∨, protlačením negace dovnitř a vytknutím kvantifikátorů. Není jednoznačný.
>
> *Příklad:* ∀x P(x) ⇒ ∀x ∃y R(x, y) |=| ∃x ¬P(x) ∨ ∀z ∃y R(z, y) |=| ∃x ∀z ∃y (¬P(x) ∨ R(z, y)), jádro ¬P(x) ∨ R(z, y).

**Formálně:** φ = ∇₁x₁ … ∇ₙxₙ ψ, ∇ᵢ ∈ {∀, ∃}, x₁, …, xₙ všechny vázané proměnné φ, ψ otevřená formule; ke každé sentenci φ existuje sentence φₚ v prenexním tvaru s φ |=| φₚ

**Definice:** [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace#^def-prenexni-tvar|přednáška 10, 5. 11. 2026]] · handout 6, slajdy 25–27

---
aliases: ["detekce limity", "věta o detekci limity substitucemi"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 5
zdroj: "handout 2B, slajd 21"
---

# věta o detekci limity

> [!lidsky] Lidsky
> Limitu poznáš z několika „dílčích pohledů“: když všechny substituce vedou ke stejnému L a jejich obrazy dohromady pokryjí nějaký kus směru, je L limitou. Typicky: sudé a liché členy posloupnosti.
>
> *Příklad:* pro aₙ = (−1)ⁿ/n jsou dvě substituce n = 2k a n = 2k + 1. Obě dají limitu 0 a sudé a liché indexy dohromady pokryjí celý ocas posloupnosti, takže lim aₙ = 0.

> [!obrazek] Které substituce pokryjí kus směru n → +∞
> ![[ma105-indexy.png]]
> *Šedé čtverečky jsou indexy k, kolečka indexy n. Barevná kolečka jsou ta, kam substituce dopadne, šedá zůstala netrefená. Nahoře k ↦ k² + 6 trefí jen 6, 7, 10, 15, 22, …, na detekci limity to nestačí. Uprostřed posun k ↦ k + 3 trefí všechna n ≥ 3. Dole sudé (modře) a liché (oranžově) indexy dohromady trefí úplně všechno.*

**Formálně:** lim_𝒯 f = L ⟺ ∃ neprázdná kolekce (φᵢ, 𝒮ᵢ): lim_𝒮ᵢ (f ∘ φᵢ) = L ∀i a pro každou volbu Pᵢ ∈ 𝒮ᵢ ∃P ∈ 𝒯: P ⊆ ⋃ φᵢ[Pᵢ]

**Definice:** [[MA1 05 – Aritmetika limit a substituce#^veta-detekce|přednáška 5, 7. 10. 2026]] · handout 2B, slajd 21

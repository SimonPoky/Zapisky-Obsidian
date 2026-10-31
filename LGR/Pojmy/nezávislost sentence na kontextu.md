---
aliases: ["pravdivost sentence nezávisí na kontextu"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 9
zdroj: "handout 5, slajd 30"
---

# nezávislost sentence na kontextu

> [!lidsky] Lidsky
> Pravdivost formule závisí jen na hodnotách jejích volných proměnných. Sentence žádné volné proměnné nemá, takže v dané interpretaci platí buď při každém kontextu, nebo při žádném.
>
> *Příklad:* ∃x (0 < x ∧ x < 1) je na ℕ nepravdivá při ρ(x) = 7 i při ρ(x) = 0, kvantifikátor si x stejně přepíše. Formule y < x (volné x, y) při x ↦ 7, y ↦ 15 neplatí, při x ↦ 7, y ↦ 1 platí.

> [!obrazek] Táž sentence v ℕ a v ℚ
> ![[lgr09-n-vs-q.png]]
> *Oranžový pruh je místo, kde by musel ležet svědek pro $\beta = \exists x\,(0 < x \wedge x < 1)$. V ℕ (nahoře) v něm žádný prvek universa neleží, v ℚ (dole) ano, např. zelené $\tfrac{1}{2}$.*

**Formálně:** I interpretace, φ formule, ρ, σ kontexty s ρ(x) = σ(x) pro každou volnou proměnnou x formule φ ⇒ (φ pravdivá v I při ρ ⟺ φ pravdivá v I při σ); speciálně pro sentenci φ: pravdivá při jednom kontextu ⇒ pravdivá při každém

**Definice:** [[LGR 09 – Pravdivost formulí, model a tautologie#^veta-nezavislost|přednáška 9, 29. 10. 2026]] · handout 5, slajd 30

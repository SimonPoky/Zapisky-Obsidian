---
aliases: ["sémantickým důsledkem", "sémantického důsledku", "sémantické důsledky", "důsledek"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 4
zdroj: "slajd 5"
---

# sémantický důsledek

> [!lidsky] Lidsky
> Z předpokladů S plyne závěr φ: kdykoli platí všechny předpoklady, platí i závěr. Řádky, kde nějaký předpoklad neplatí, se nekontrolují.
>
> *Příklad:* {a ⇒ b, a} ⊨ b: oba předpoklady platí jen pro u(a) = u(b) = 1 a tam platí i b. Ale {a ∨ b} ⊭ a: pro u(a) = 0, u(b) = 1 předpoklad platí a závěr ne.

**Formálně:** S ⊨ φ iff ∀u: u(S) = 1 ⇒ u(φ) = 1 iff ∀u: u(S) ≤ u(φ) iff S ∪ {¬φ} nesplnitelná; α ⊨ φ iff α ⇒ φ je tautologie; S ⊨ ff iff S nesplnitelná

**Definice:** [[LGR 04 – Sémantický důsledek a klauzální tvar#^def-dusledek|přednáška 4, 8. 10. 2026]] · slajd 5 · tvrzení: [[LGR 04 – Sémantický důsledek a klauzální tvar#^veta-le|slajd 6]], [[LGR 04 – Sémantický důsledek a klauzální tvar#^veta-implikace|α ⊨ φ a implikace]]

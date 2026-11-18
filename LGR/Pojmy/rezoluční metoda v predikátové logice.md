---
aliases: ["rezoluční metoda", "rezoluční metodou", "ověření důsledku rezolucí"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajdy 34–40"
---

# rezoluční metoda v predikátové logice

> [!lidsky] Lidsky
> Recept na S ⊨ φ: přidej negovaný závěr, převeď na klauzule a hledej rezolucí spor. Spor znamená, že důsledek platí; když se výroba zastaví bez sporu, důsledek neplatí. Zastavit se ale nemusí.
>
> *Příklad:* ∃x ∀y R(x, y) ⊨ ∀y ∃x R(x, y): Kl = {∀y R(a, y), ∀x ¬R(x, b)}, unifikátor (x := a, y := b), rezolventa ff, důsledek platí.

**Formálně:** S ⊨ φ ⟺ S ∪ {¬φ} nesplnitelná ⟺ Kl(S ∪ {¬φ}) nesplnitelná ⟺ ff ∈ R*(Kl(S ∪ {¬φ}))

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-rezolucni-metoda-pl|přednáška 12, 12. 11. 2026]] · handout 7, slajdy 34–40

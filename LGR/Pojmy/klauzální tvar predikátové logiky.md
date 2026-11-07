---
aliases: ["Kl(φ)", "klauzální tvar sentence", "algoritmus 1", "převod na klauzule"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 11
zdroj: "handout 7, slajdy 12–13"
---

# klauzální tvar predikátové logiky

> [!lidsky] Lidsky
> Množina klauzulí Kl(φ), na kterou sentenci převedeš osmi kroky: přejmenovat, jen ¬ ∧ ∨, negace k atomům, vytknout kvantifikátory, CNF, skolemizovat, ∀ pod ∧, rozdělit. Je s φ jen stejně splnitelná, ne ekvivalentní.
>
> *Příklad:* ∀x P(x) ⇒ ∀x ∃y (R(x, y) ∧ Q(a)) dá prenexní tvar ∃x ∀z ∃y ((¬P(x) ∨ R(z, y)) ∧ (¬P(x) ∨ Q(a))) a po skolemizaci x := c, y := f(z) klauzule ∀z (¬P(c) ∨ R(z, f(z))) a ¬P(c) ∨ Q(a).

**Formálně:** Kl(φ) vznikne kroky (1) přejmenování vázaných proměnných, (2) spojky ¬, ∧, ∨, (3) negace k atomům, (4) vytknutí kvantifikátorů, (5) CNF otevřené části, (6) skolemizace, (7) ∀ pod ∧ k podformulím s jejich proměnnou, (8) rozdělení v místech ∧; kroky 1–5 a 7 zachovávají |=|, krok 6 jen ≈

**Definice:** [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice#^def-klauzalni-tvar-pl|přednáška 11, 6. 11. 2026]] · handout 7, slajdy 12–13

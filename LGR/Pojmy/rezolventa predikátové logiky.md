---
aliases: ["rezolventa v predikátové logice", "rezolventy v predikátové logice", "res(α, β)", "konflikt literálů"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 11
zdroj: "handout 7, slajdy 18–22, 31–33"
---

# rezolventa predikátové logiky

> [!lidsky] Lidsky
> Klauzule, která plyne ze dvou klauzulí, protože jejich literály s P a ¬P se po dosazení termů srazí na nějaké části universa: na celém U, v jednom bodě nebo na obrazu funkce. Kde se nesrazí, rezolventa není.
>
> *Příklad:* z ∀x (P(x) ∨ Q(x)) a ¬P(a) ∨ S(a) vznikne dosazením x := a rezolventa Q(a) ∨ S(a). Z ∀x (P(f(x)) ∨ Q(x)) a ¬P(a) ∨ S(a) žádná nevznikne.

**Formálně:** α, β klauzule s různými proměnnými, α obsahuje P(t₁, …, tₙ), β obsahuje ¬P(s₁, …, sₙ) a ϑ je maximální unifikátor P(t₁, …, tₙ) a P(s₁, …, sₙ) ⇒ res(α, β) = ∀(zbylé proměnné) disjunkce ostatních literálů α(ϑ) a β(ϑ); bez unifikátoru rezolventa není. Platí {α, β} ⊨ res(α, β)

**Definice:** [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice#^def-rezolventa-pl|přednáška 11, 6. 11. 2026]] · handout 7, slajdy 18–22 · formálně: [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-rezolventa-formalne|přednáška 12, 12. 11. 2026]] · důsledek: [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^veta-dusledek-rezolventy|slajd 33]]

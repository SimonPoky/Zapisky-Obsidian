---
aliases: ["rezolventa v predikátové logice", "rezolventy v predikátové logice", "res(α, β)", "konflikt literálů"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 11
zdroj: "handout 7, slajdy 18–22"
---

# rezolventa predikátové logiky

> [!lidsky] Lidsky
> Klauzule, která plyne ze dvou klauzulí, protože jejich literály s P a ¬P se po dosazení termů srazí na nějaké části universa: na celém U, v jednom bodě nebo na obrazu funkce. Kde se nesrazí, rezolventa není.
>
> *Příklad:* z ∀x (P(x) ∨ Q(x)) a ¬P(a) ∨ S(a) vznikne dosazením x := a rezolventa Q(a) ∨ S(a). Z ∀x (P(f(x)) ∨ Q(x)) a ¬P(a) ∨ S(a) žádná nevznikne.

**Formálně:** res(α, β) je klauzule s {α, β} ⊨ res(α, β), složená z ostatních literálů α′, β′ (důsledků α, β dosazením termů), mezi nimiž jsou komplementární literály; ff mezi rezolventami ⟺ množina klauzulí je nesplnitelná

**Definice:** [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice#^def-rezolventa-pl|přednáška 11, 6. 11. 2026]] · handout 7, slajdy 18–22

---
aliases: ["R*(S)", "populace všech rezolvent", "R(S)", "generace rezolvent"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 5
zdroj: "slajd 16"
---

# populace rezolvent

> [!lidsky] Lidsky
> Celý „rodokmen“ množiny klauzulí: původní klauzule, jejich rezolventy, rezolventy rezolvent atd. Je pravdivý ve stejných ohodnoceních jako S a nad konečně mnoha proměnnými je konečný.
>
> *Příklad:* S = {a ∨ b, ¬a, ¬b}: z a ∨ b a ¬a vznikne b, z a ∨ b a ¬b vznikne a, z b a ¬b (nebo a a ¬a) vznikne ff. R*(S) = {a ∨ b, ¬a, ¬b, a, b, ff}.

**Formálně:** R(S) = S ∪ {rezolventy dvojic z S}; R⁰(S) = S, Rⁱ⁺¹(S) = R(Rⁱ(S)); R*(S) = ⋃ Rⁱ(S)

**Definice:** [[LGR 05 – Rezoluční princip#^def-populace|přednáška 5, 9. 10. 2026]] · slajd 16

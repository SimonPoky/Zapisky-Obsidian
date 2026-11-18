---
aliases: ["nerozhodnutelnost", "nerozhodnutelný problém", "nerozhodnutelnost predikátové logiky"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajdy 37–38"
---

# nerozhodnutelnost splnitelnosti v predikátové logice

> [!lidsky] Lidsky
> Neexistuje program, který by o každé konečné množině klauzulí predikátové logiky v konečném čase správně řekl, zda je splnitelná. Rezoluce spor vždy najde, ale bez sporu může běžet donekonečna.
>
> *Příklad:* pro {∀x (P(x) ∨ ¬P(f(x))), ∀y (P(y) ∨ ¬P(f(f(y))))} vznikají rezolventy s f³, f⁴, … bez konce, přitom množina je splnitelná (⟦P⟧ = U).

**Formálně:** neexistuje algoritmus, který pro každou konečnou množinu klauzulí S zastaví a správně rozhodne, zda je S splnitelná; tedy ani zda je sentence tautologie

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^veta-nerozhodnutelnost|přednáška 12, 12. 11. 2026]] · handout 7, slajdy 37–38

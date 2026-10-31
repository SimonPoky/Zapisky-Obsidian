---
aliases: ["úplný systém", "úplnost důkazového systému"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 6
zdroj: "slajd 3 (prez. 4)"
---

# úplný důkazový systém

> [!lidsky] Lidsky
> Korektní systém, který navíc nic nevynechá: každý sémantický důsledek v něm jde i dokázat. Odvoditelné a pravdivé formule splývají.
>
> *Příklad:* v přirozené dedukci jde odvodit každá tautologie, třeba ⊢ a ∨ ¬a nebo ⊢ (a ∧ b) ⇒ a, a každý sémantický důsledek, třeba {a ⇒ b, ¬b} ⊢ ¬a (MT).

> [!obrazek] Korektní, úplný, agresivní a sporný systém
> ![[lgr06-systemy.png]]
> *Šedě všechny formule $\mathrm{Fla}(A)$, modře pravdivé ($S \models \varphi$), oranžově šrafované odvoditelné ($S \vdash \varphi$). Korektní: oranžová leží uvnitř modré. Úplný: kryjí se. Agresivní: oranžová přečnívá ven. Sporný: oranžová je celé $\mathrm{Fla}(A)$.*

**Formálně:** pro každé S a φ: S ⊢ φ ⟺ S ⊨ φ (odvoditelné = pravdivé)

**Definice:** [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^def-korektni-uplny|přednáška 6, 15. 10. 2026]] · slajd 3 · věta o úplnosti přirozené dedukce: slajd 14

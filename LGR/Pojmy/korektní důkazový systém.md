---
aliases: ["korektní systém", "korektnost", "korektní", "nekorektní"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 6
zdroj: "slajd 3 (prez. 4)"
---

# korektní důkazový systém

> [!lidsky] Lidsky
> Systém, který nikdy nedokáže nepravdu: všechno, co se v něm dá odvodit, opravdu sémanticky plyne. Odvoditelné formule tvoří podmnožinu pravdivých.
>
> *Příklad:* přirozená dedukce je korektní: když jde odvodit a ∧ b ⊢ a, platí i a ∧ b ⊨ a. Systém s pravidlem „z a ∨ b odvoď a“ korektní není, protože a ∨ b ⊭ a (u(a) = 0, u(b) = 1).

> [!obrazek] Korektní, úplný, agresivní a sporný systém
> ![[lgr06-systemy.png]]
> *Šedě všechny formule $\mathrm{Fla}(A)$, modře pravdivé ($S \models \varphi$), oranžově šrafované odvoditelné ($S \vdash \varphi$). Korektní: oranžová leží uvnitř modré. Úplný: kryjí se. Agresivní: oranžová přečnívá ven. Sporný: oranžová je celé $\mathrm{Fla}(A)$.*

**Formálně:** pro každé S a φ: S ⊢ φ ⇒ S ⊨ φ (odvoditelné ⊆ pravdivé)

**Definice:** [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^def-korektni-uplny|přednáška 6, 15. 10. 2026]] · slajd 3

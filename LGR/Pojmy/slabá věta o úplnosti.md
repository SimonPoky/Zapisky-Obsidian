---
aliases: []
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4, slajd 15"
---

# slabá věta o úplnosti

> [!lidsky] Lidsky
> Věty výrokové logiky jsou právě tautologie: bez předpokladů jde dokázat přesně to, co platí vždy.
>
> *Příklad:* a ∨ ¬a je tautologie, takže jde dokázat bez předpokladů (TND). a ⇒ b tautologie není (u(a) = 1, u(b) = 0), takže ⊢ a ⇒ b odvodit nejde.

> [!obrazek] Řetěz důkazu věty o úplnosti
> ![[lgr07-retez-uplnosti.png]]
> *Vlevo modře sémantika ($\models$), vpravo oranžově syntax ($\vdash$). Červeně dokazovaná věta, zeleně slabá věta o úplnosti, přes kterou se celý důkaz převede na tautologie.*

> [!obrazek] Skládání odvození tautologie
> ![[lgr07-skladani-tnd.png]]
> *Listy (modře) jsou odvození z lemmatu pro osm řádků tabulky. Každý oranžový uzel je jedno TND s rozborem případů ∨e, který zahodí předpoklad jedné proměnné. Kořen je odvození $\vdash \varphi$ bez předpokladů.*

**Formálně:** pro každou φ: ⊢ φ ⟺ ⊨ φ; „⇐“: lemma o literálech řádku + slepení řádků přes TND a ∨e

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-slaba-uplnost|přednáška 7, 22. 10. 2026]] · handout 4, slajd 15 · důkaz: handout 4D, slajd 13

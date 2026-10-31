---
aliases: ["důkaz sporem", "sémantický důkaz sporem"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 4
zdroj: "slajd 7"
---

# věta o sémantickém důkazu sporem

> [!lidsky] Lidsky
> Chceš ukázat, že z předpokladů plyne závěr? Přidej k nim opak závěru a ukaž, že to nejde splnit naráz. Díky tomu se každá otázka (tautologie, důsledek, ekvivalence) převede na nesplnitelnost.
>
> *Příklad:* {a ⇒ b, a} ⊨ b, protože {a ⇒ b, a, ¬b} je nesplnitelná: a a ¬b vynutí u(a) = 1, u(b) = 0, a pak je a ⇒ b nepravdivá.

> [!obrazek] Důsledek jako vnoření množin
> ![[lgr04-mnoziny.png]]
> *Vlevo: zeleně ohodnocení, kde platí celé $S$, modře ohodnocení, kde platí $\varphi$. $S \models \varphi$ znamená, že zelená leží celá v modré. Vpravo: červeně ohodnocení, kde platí $\neg\varphi$. Zelená a červená se nepotkají, takže $S \cup \{\neg\varphi\}$ nemá žádné ohodnocení: je nesplnitelná (§4).*

**Formálně:** S ⊨ φ ⟺ S ∪ {¬φ} je nesplnitelná

**Definice:** [[LGR 04 – Sémantický důsledek a klauzální tvar#^veta-spor|přednáška 4, 8. 10. 2026]] · slajd 7

---
aliases: ["rezoluční tabulky", "rezoluční tabulce", "rezoluční tabulkou"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 5
zdroj: "slajdy 23–25"
---

# rezoluční tabulka

> [!lidsky] Lidsky
> Úsporná rezoluce: proměnné se „vyrezolvují“ jedna po druhé a klauzule s už zpracovanou proměnnou se zahodí. Na konci zbyde {ff} (nesplnitelná), nebo ∅ (splnitelná); svědka dostaneš pozpátku.
>
> *Příklad:* S = {a ∨ b, ¬a ∨ b, ¬b}. Eliminace a: rezolventa b, zbude {¬b, b}. Eliminace b: rezolventa ff, zbude {ff}, takže S je nesplnitelná.

> [!obrazek] Rezoluční tabulka pro $S$
> ![[lgr06-tabulka.png]]
> *Sloupce jsou klauzule: oranžově z $S$, modře rezolventa přes $x$, červeně tautologická rezolventa (vypustí se). Číslo stojí v řádku proměnné, při jejíž eliminaci se klauzule použije naposledy: $1$ = obsahuje ji pozitivně, $0$ = negativně. Šrafované buňky pod ním: klauzule je „umrtvená“. Zeleně dole literály, díky kterým je klauzule ve výsledném svědkovi pravdivá; šipka vlevo ukazuje směr hledání svědka.*

> [!obrazek] Co vyrobí tabulka oproti R*(S)
> ![[lgr05-mnoziny.png]]
> *Šedě všech $3^n$ klauzulí nad $A$, modře $R^*(S)$, zeleně $T$: klauzule z $S$ a rezolventy, které vyrobí rezoluční tabulka, oranžově $S$. Tabulka vyrobí jen část rezolvent, ale $\mathrm{ff}$ najde právě tehdy, když je v $R^*(S)$ (červeně).*

**Formálně:** S konečná, v základním tvaru, proměnné x₁, …, xₙ; pro i = 1, …, n: S := S₀ ∪ R_{xᵢ}; konec S = {ff} ⇒ nesplnitelná, S = ∅ ⇒ splnitelná

**Definice:** [[LGR 05 – Rezoluční princip#^def-rezolucni-tabulka|přednáška 5, 9. 10. 2026]] · slajdy 23–24

---
aliases: ["zamítacího stromu", "zamítací stromy"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 5
zdroj: "slajd 18"
---

# zamítací strom

> [!lidsky] Lidsky
> Rodokmen jednoho sporu: od klauzulí z S přes rezolventy až ke kořeni ff. Jeden nalezený strom stačí jako důkaz nesplnitelnosti; jeho nenalezení splnitelnost nedokazuje.
>
> *Příklad:* pro S = {a ∨ b, ¬a, ¬b}: listy a ∨ b a ¬a dají vrchol b, ten s listem ¬b dá kořen ff. Tento strom je důkaz, že S je nesplnitelná.

> [!obrazek] Zamítací strom ze slajdu 18
> ![[lgr05-zamitaci-strom.png]]
> *Oranžově klauzule z $S$ (list $\neg x$ se smí použít dvakrát), modře rezolventy, červeně kořen $\mathrm{ff}$, šedě proměnná, přes kterou se rezolvuje.*

**Formálně:** listy ∈ S, vnitřní vrchol = rezolventa svých dvou potomků, kořen ff ⇒ ff ∈ R*(S)

**Definice:** [[LGR 05 – Rezoluční princip#^def-zamitaci-strom|přednáška 5, 9. 10. 2026]]

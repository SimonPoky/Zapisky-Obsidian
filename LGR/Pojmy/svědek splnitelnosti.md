---
aliases: ["svědek", "svědka", "svědkem", "svědci", "svědky"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 6
zdroj: "slajdy 3–4, 25 (prez. 3)"
---

# svědek splnitelnosti

> [!lidsky] Lidsky
> Konkrétní ohodnocení, ve kterém jsou všechny formule množiny pravdivé naráz; dokazuje, že množina jde splnit. Z rezoluční tabulky se najde pozpátku: od prázdné množiny (svědkem je cokoli) se postupně doplňují hodnoty eliminovaných proměnných.
>
> *Příklad:* pro S = {a ∨ b, ¬a} je svědek u(a) = 0, u(b) = 1: platí a ∨ b i ¬a. Ohodnocení u(a) = 1 svědek není, ¬a by bylo nepravdivé.

> [!obrazek] Svědek se staví pozpátku
> ![[lgr06-svedek.png]]
> *Modře množiny z jednotlivých kroků tabulky, zeleně volba hodnoty eliminované proměnné, vpravo klauzule, která volbu vynutí.*

**Formálně:** u je svědek splnitelnosti S ⟺ u(S) = 1, tj. u(φ) = 1 pro každou φ ∈ S; z tabulky: svědek pro S₀ ∪ R_x se volbou u(x) ∈ {0, 1} změní na svědka pro S

**Definice:** [[LGR 04 – Sémantický důsledek a klauzální tvar#^def-splnitelnost-mnoziny|přednáška 4, 8. 10. 2026]] · slajdy 3–4 · hledání pozpátku: [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^veta-svedek-postup|přednáška 6, 15. 10. 2026]] · slajd 25

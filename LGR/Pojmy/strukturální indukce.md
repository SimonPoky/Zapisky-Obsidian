---
aliases: ["princip strukturální indukce"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4D, slajd 7"
---

# strukturální indukce

> [!lidsky] Lidsky
> Indukce po stavebních krocích: ověř vlastnost pro základní kousky (proměnné) a ukaž, že ji každé tvořící pravidlo (spojka) zachová.
>
> *Příklad:* „Každá formule má stejně levých jako pravých závorek“: proměnná má 0 a 0, a každá spojka přidá jednu levou a jednu pravou, např. (α ∧ β). Tedy to platí pro všechny formule.

> [!obrazek] Slabá, silná a strukturální indukce
> ![[lgr07-indukce.png]]
> *Zeleně základ, oranžově krok. Slabá: z $n$ na $n + 1$. Silná: ze všech $0, \dots, n$ na $n + 1$. Strukturální: v syntaktickém stromu formule od listů (proměnné) ke kořeni.*

**Formálně:** M induktivně definovaná, V vlastnost: (1) prvky ze základních pravidel mají V, (2) každé tvořící pravidlo: předpoklady mají V ⇒ výsledek má V; pak každý prvek M má V

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-strukturalni-indukce|přednáška 7, 22. 10. 2026]] · handout 4D, slajd 7

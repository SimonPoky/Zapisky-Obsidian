---
aliases: ["slabá indukce", "matematická indukce"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4D, slajd 4"
---

# princip slabé indukce

> [!lidsky] Lidsky
> Domino: platí to pro první číslo, a když pro n, tak i pro n + 1. Pak to platí pro všechna.
>
> *Příklad:* 1 + 2 + … + n = n(n + 1)/2. Základ n = 1: 1 = 1·2/2. Krok: přičtením n + 1 vznikne n(n + 1)/2 + (n + 1) = (n + 1)(n + 2)/2.

> [!obrazek] Slabá, silná a strukturální indukce
> ![[lgr07-indukce.png]]
> *Zeleně základ, oranžově krok. Slabá: z $n$ na $n + 1$. Silná: ze všech $0, \dots, n$ na $n + 1$. Strukturální: v syntaktickém stromu formule od listů (proměnné) ke kořeni.*

**Formálně:** V vlastnost čísel n ≥ n₀: V(n₀) a (∀ n ≥ n₀: V(n) ⇒ V(n + 1)) ⇒ ∀ n ≥ n₀: V(n)

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-slaba-indukce|přednáška 7, 22. 10. 2026]] · handout 4D, slajd 4

---
aliases: ["složení", "skládání zobrazení", "složení zobrazení", "B∘A", "BA"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 7
zdroj: "pozn. 6.2"
---

# složené zobrazení

> [!lidsky] Lidsky
> Výrobní linka: vektor projde nejdřív strojem A, pak strojem B. Píše se BA a čte zprava doleva jako g(f(x)).
>
> *Příklad:* A(x) = 2x (zvětšení) a B(a; b) = (−b; a) (otočení o 90°). Pak (BA)(1; 0) = B(2; 0) = (0; 2): nejdřív zvětšení, potom otočení.

> [!obrazek] Skládání zobrazení
> ![[lag07-skladani.png]]
> *Modrá šipka: $A$ pošle $\vec{x} \in U$ na $A\vec{x} \in V$. Oranžová: $B$ pošle $A\vec{x}$ dál do $W$. Zelený oblouk: složené zobrazení $BA$ udělá obojí najednou.*

**Formálně:** Pro A: U → V a B: V → W je BA = B ∘ A: U → W, (BA)x = B(Ax); jsou-li A, B lineární, je i BA lineární

**Definice:** [[LAG 07 – Lineární zobrazení#^def-slozene-zobrazeni|přednáška 7, 14. 10. 2026]] · pozn. 6.2 · matice: [[věta o matici složeného zobrazení]]

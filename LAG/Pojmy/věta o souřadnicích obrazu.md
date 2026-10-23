---
aliases: ["[Ax]^Y = [A][x]^X", "souřadnice obrazu"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 8
zdroj: "pozn. 6.13"
---

# věta o souřadnicích obrazu

> [!lidsky] Lidsky
> Místo zobrazení vektoru stačí vynásobit maticí jeho souřadnice: vyjdou souřadnice obrazu. Matice je překladač zobrazení do sloupců čísel.
>
> *Příklad:* pro derivaci v bázích (1, x, x²) a (1, x) je [D] = $\begin{pmatrix}0&1&0\\0&0&2\end{pmatrix}$. Pro p = 5 + 3x + x² je [p] = (5; 3; 1) a [D][p] = (3; 2), tedy Dp = 3 + 2x. Sedí: (5 + 3x + x²)′ = 3 + 2x.

**Formálně:** V, W lineární prostory konečné dimenze nad 𝔽, 𝒳 báze V, 𝒴 báze W, A ∈ Lin(V, W), x ∈ V ⇒ [Ax]^𝒴 = [A]^{𝒳→𝒴} · [x]^𝒳

**Definice:** [[LAG 08 – Matice lineárního zobrazení a součin matic#^veta-souradnice-obrazu|přednáška 8, 16. 10. 2026]] · pozn. 6.13

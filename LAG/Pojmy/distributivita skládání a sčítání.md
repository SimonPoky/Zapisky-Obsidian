---
aliases: ["distributivita", "distributivita násobení matic", "(A + B)C = AC + BC"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 10
zdroj: "věta 6.32"
---

# distributivita skládání a sčítání

> [!lidsky] Lidsky
> Závorky jde roznásobit jako u čísel, (A + B)C = AC + BC a A(C + D) = AC + AD, jen pořadí činitelů musí zůstat. Druhý zákon potřebuje linearitu A.
>
> *Příklad:* A = $\begin{pmatrix}1&2\\0&1\end{pmatrix}$, B = $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, C = $\begin{pmatrix}2&1\\1&3\end{pmatrix}$: (A + B)C = $\begin{pmatrix}5&10\\3&4\end{pmatrix}$ = AC + BC = $\begin{pmatrix}4&7\\1&3\end{pmatrix}$ + $\begin{pmatrix}1&3\\2&1\end{pmatrix}$.

**Formálně:** Buďte U, V, W lineární prostory nad 𝔽, A, B ∈ Lin(V, W), C, D ∈ Lin(U, V) ⇒ (A + B)C = AC + BC a A(C + D) = AC + AD; totéž pro matice A, B ∈ 𝔽^{l×m}, C, D ∈ 𝔽^{m×n}

**Definice:** [[LAG 10 – Obraz a vzor při lineárním zobrazení#^veta-distributivita|přednáška 10, 23. 10. 2026]] · věta 6.32

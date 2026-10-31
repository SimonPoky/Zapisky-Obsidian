---
aliases: ["matice lineárního zobrazení v kanonické bázi", "kanonická matice zobrazení"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 7
zdroj: "pozn. 6.6–6.8"
---

# matice zobrazení v kanonické bázi

> [!lidsky] Lidsky
> Sloupce matice jsou obrazy jednotkových vektorů e₁, …, eₙ. S ní se A počítá jako matice krát vektor.
>
> *Příklad:* A(a; b) = (a + b; 2a): Ae₁ = (1; 2) a Ae₂ = (1; 0), takže matice je $\begin{pmatrix}1&1\\2&0\end{pmatrix}$. Kontrola: $\begin{pmatrix}1&1\\2&0\end{pmatrix}$(3; 4) = (7; 6) = A(3; 4).

> [!obrazek] Co zkosení udělá se sítí
> ![[lag07-mrizka.png]]
> *Vlevo kanonická síť s modrým $\vec{e}_1$, oranžovým $\vec{e}_2$ a zeleným vektorem $(2; 1) = 2\vec{e}_1 + \vec{e}_2$. Vpravo obrazy: síť se zkosí, $\vec{e}_1$ zůstane, $\vec{e}_2$ přejde na $(1; 1)$ a $(2; 1)$ přejde na $2\vec{a}_1 + \vec{a}_2 = (3; 1)$. Bod zůstane „2 kroky po prvním sloupci a 1 krok po druhém“, jen jsou kroky jiné.*

> [!obrazek] Co $A$ udělá s mřížkou
> ![[lag08-mrizka.png]]
> *Vlevo kanonická síť, modré $\vec{e}_1$ a oranžové $\vec{e}_2$. Vpravo jejich obrazy, sloupce matice: $(1; 1)$ a $(-1; 1)$. Celá síť se otočí o $45°$ a natáhne $\sqrt{2}$-krát, protože $\lvert(1; 1)\rvert = \sqrt{2} \approx 1{,}41$.*

**Formálně:** Buď A: 𝔽ⁿ → 𝔽ᵐ lineární a (e₁, …, eₙ) kanonická báze 𝔽ⁿ. Matice zobrazení A je (Ae₁ ⋯ Aeₙ) ∈ 𝔽^{m×n}; pak Ax = (Ae₁ ⋯ Aeₙ)x pro všechna x ∈ 𝔽ⁿ

**Definice:** [[LAG 07 – Lineární zobrazení#^def-matice-zobrazeni|přednáška 7, 14. 10. 2026]] · pozn. 6.6–6.8 · určení kanonickou bází: [[LAG 08 – Matice lineárního zobrazení a součin matic#^veta-urceni-kanonickou|přednáška 8]] · obecně: [[matice lineárního zobrazení vzhledem k bázím]]

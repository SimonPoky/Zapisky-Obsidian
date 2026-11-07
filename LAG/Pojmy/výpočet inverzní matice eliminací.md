---
aliases: ["inverze eliminací", "výpočet inverzní matice", "inverzi eliminací", "pozn. 8.19"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 13
zdroj: "úloha 8.14, pozn. 8.19"
---

# výpočet inverzní matice eliminací

> [!lidsky] Lidsky
> Inverzi spočítáš tak, že za čáru napíšeš jednotkovou matici a řádkovými úpravami uděláš z levé části E; vpravo pak stojí A⁻¹. Stejně z (A | B) vznikne (E | A⁻¹B), což řeší maticovou rovnici AX = B. Když vlevo vznikne nulový řádek, A inverzi nemá.
>
> *Příklad:* (1 3 | 1 0; 2 5 | 0 1) → r₂ − 2r₁, r₁ + 3r₂, r₂·(−1) → (1 0 | −5 3; 0 1 | 2 −1), tedy $\begin{pmatrix}1&3\\2&5\end{pmatrix}^{-1} = \begin{pmatrix}-5&3\\2&-1\end{pmatrix}$.

**Formálně:** Buď A ∈ 𝔽^{n×n} regulární a B ∈ 𝔽^{n×p}. Gaussova–Jordanova eliminace převede (A | B) na (E | A⁻¹B), speciálně (A | E) na (E | A⁻¹); důvod: úpravy = násobení regulární T zleva, T(A | B) = (TA | TB) a TA = E ⇒ T = A⁻¹

**Definice:** [[LAG 13 – Inverzní matice eliminací, transpozice a grupy#^veta-inverze-eliminaci|přednáška 13, 6. 11. 2026]] · úloha 8.14, pozn. 8.19

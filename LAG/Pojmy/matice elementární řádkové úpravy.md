---
aliases: ["matice elementární úpravy", "matice řádkové úpravy", "elementární matice", "lemma 8.15"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 13
zdroj: "lemma 8.15*"
---

# matice elementární řádkové úpravy

> [!lidsky] Lidsky
> Každá řádková úprava je násobení zleva jednou regulární maticí T. Tu najdeš tak, že stejnou úpravu uděláš s jednotkovou maticí. Celá eliminace je pak součin takových matic.
>
> *Příklad:* úprava „ke 3. řádku přičti dvojnásobek 1.“ má T = $\begin{pmatrix}1&0&0\\0&1&0\\2&0&1\end{pmatrix}$ a pro X = (1 2; 3 4; 5 6) je TX = (1 2; 3 4; 7 10).

**Formálně:** Buď B ∈ 𝔽^{m×n}. Každou elementární řádkovou úpravu B lze realizovat jako TB s regulární T = (t₁ ⋯ t_m) ∈ 𝔽^{m×m}: (1) prohození řádků k, l: tᵢ = eᵢ pro i ≠ k, l, t_k = e_l, t_l = e_k; (2) k-tý řádek krát α ≠ 0: t_k = αe_k, jinak tᵢ = eᵢ; (3) přičtení α-násobku k-tého řádku k l-tému: t_k = e_k + αe_l, jinak tᵢ = eᵢ

**Definice:** [[LAG 13 – Inverzní matice eliminací, transpozice a grupy#^veta-matice-uprav|přednáška 13, 6. 11. 2026]] · lemma 8.15\*

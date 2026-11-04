---
aliases: ["Gaussovy eliminace", "Gaussovu eliminaci", "Gaussova eliminační metoda", "eliminace", "algoritmus 8.10"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 12
zdroj: "algoritmus 8.10"
---

# Gaussova eliminace

> [!lidsky] Lidsky
> Algoritmus, který matici převede na stupňovitý tvar: sloupec po sloupci zleva najdi nenulový prvek, přesuň jeho řádek nahoru a odečítáním jeho násobků vynuluj vše pod ním, pak pokračuj vpravo dole.
>
> *Příklad:* (1 1 1 | 6; 2 3 1 | 11; 1 2 3 | 14) → r₂ − 2r₁, r₃ − r₁ → (1 1 1 | 6; 0 1 −1 | −1; 0 1 2 | 8) → r₃ − r₂ → (…; 0 0 3 | 9), odkud z = 3, y = 2, x = 1.

**Formálně:** Vstup B ∈ 𝔽^{m×n}, l = 1, j = 1; dokud j ≤ n a l ≤ m: (1) je-li bᵢⱼ = 0 pro všechna i ≥ l, polož j = j + 1 a opakuj (1); (2) je-li b_{lj} = 0, najdi k > l s b_{kj} ≠ 0 a prohoď řádky k, l; (3) pro každé i > l odečti od i-tého řádku (bᵢⱼ / b_{lj})-násobek l-tého, polož l = l + 1, j = j + 1 a vrať se k (1)

**Definice:** [[LAG 12 – Frobeniova věta a Gaussova eliminace#^def-gaussova-eliminace|přednáška 12, 4. 11. 2026]] · algoritmus 8.10

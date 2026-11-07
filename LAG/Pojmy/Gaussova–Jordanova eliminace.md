---
aliases: ["Gaussovy–Jordanovy eliminace", "Gaussovu–Jordanovu eliminaci", "úplná Gaussova eliminace", "redukovaný stupňovitý tvar", "algoritmus 8.12"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 13
zdroj: "algoritmus 8.12"
---

# Gaussova–Jordanova eliminace

> [!lidsky] Lidsky
> Gaussova eliminace dotažená až do konce: po vynulování pod pivoty jdeš zdola nahoru, každý pivot vydělíš na jedničku a vynuluješ i čísla nad ním. Vznikne redukovaný stupňovitý tvar, ze kterého řešení přečteš bez dosazování.
>
> *Příklad:* (2 4 | 6; 0 3 | 3) → r₂ : 3 → (0 1 | 1) → r₁ − 4r₂ → (2 0 | 2) → r₁ : 2 → (1 0 | 1; 0 1 | 1), tedy x = 1, y = 1.

**Formálně:** Vstup B ∈ 𝔽^{m×n}. Proveď Gaussovu eliminaci, hlavní sloupce k₁, …, k_r. Pro i = r, r − 1, …, 1: (1) vyděl i-tý řádek pivotem b_{ik_i}, (2) pro každé j < i odečti od j-tého řádku b_{jk_i}-násobek i-tého. Výsledek je redukovaný stupňovitý tvar (pivoty 1, nad i pod nimi nuly)

**Definice:** [[LAG 13 – Inverzní matice eliminací, transpozice a grupy#^def-gauss-jordan|přednáška 13, 6. 11. 2026]] · algoritmus 8.12

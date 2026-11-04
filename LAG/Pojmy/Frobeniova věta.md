---
aliases: ["Frobeniovy věty", "Frobeniovu větu", "Rouchéova–Capelliho věta", "Kroneckerova–Capelliho věta", "věta 8.1"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 12
zdroj: "věta 8.1"
---

# Frobeniova věta

> [!lidsky] Lidsky
> Návod na soustavu Ax = b: řešení existuje, právě když přidáním sloupce b nevyskočí hodnost; řešení homogenní soustavy tvoří podprostor dimenze n − rank A; všechna řešení jsou jedno řešení plus cokoli z homogenních.
>
> *Příklad:* x − y + 2z = 3: rank A = rank(A | b) = 1, takže řešení existuje, dim S₀ = 3 − 1 = 2 a S = (3; 0; 0) + span{(1; 1; 0), (−2; 0; 1)}. Soustava x + 2y = 3, 2x + 4y = 5 má rank A = 1 < 2 = rank(A | b), řešení nemá.

**Formálně:** Buď 𝔽 těleso, A ∈ 𝔽^{m×n}, b ∈ 𝔽ᵐ. (1) Množina řešení S₀ soustavy Ax = 0 je podprostor 𝔽ⁿ dimenze n − rank A. (2) Ax = b má řešení ⟺ rank A = rank(A | b). (3) Je-li xₚ řešení Ax = b, je množina řešení S = xₚ + S₀ = {xₚ + x₀ | x₀ ∈ S₀}

**Definice:** [[LAG 12 – Frobeniova věta a Gaussova eliminace#^veta-frobenius|přednáška 12, 4. 11. 2026]] · věta 8.1

---
aliases: []
tags: [pojem, LAG]
predmet: LAG
prednaska: 15
zdroj: "pozn. 10.23"
---

# determinant lineárního operátoru

> [!lidsky] Lidsky
> Determinant zobrazení prostoru do sebe: vezmi jeho matici v libovolné bázi a spočítej její determinant. Výsledek na bázi nezávisí, protože přechodové matice se vykrátí.
>
> *Příklad:* posun p(x) ↦ p(x + 1) na ℝ^{≤2}[x] má v bázi (1, x, x²) matici (1 1 1; 0 1 2; 0 0 1), det = 1; derivace p ↦ p′ má det = 0.

**Formálně:** Buď L lineární prostor, dim L < ∞, 𝒳 báze L, A ∈ Lin(L). Determinant operátoru A je det A = det [A]^𝒳; nezávisí na 𝒳, protože det[A]^𝒴 = det T · det[A]^𝒳 · (det T)⁻¹ pro T = [id]^{𝒳→𝒴}

**Definice:** [[LAG 15 – Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci#^def-det-operatoru|přednáška 15, 13. 11. 2026]] · pozn. 10.23

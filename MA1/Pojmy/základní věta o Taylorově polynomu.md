---
aliases: ["základní věty o Taylorově polynomu", "Taylorova věta"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 9
zdroj: "handout 4A, slajd 17"
---

# základní věta o Taylorově polynomu

> [!lidsky] Lidsky
> Chyba Taylorova polynomu jde k nule rychleji než (x − p)ⁿ a polynom má v p stejné derivace až do řádu n jako f. Jiný polynom stupně ≤ n to neumí.
>
> *Příklad:* pro sin x a p = 0 je T₃(x) = x − x³/6. Pro x = 0,1 je chyba sin 0,1 − T₃(0,1) ≈ 8·10⁻⁸, zanedbatelná i vůči x³ = 0,001.

**Formálně:** f má alespoň n derivací v p ⇒ (1) lim_{x→p} (f(x) − Tₙ(f, p)(x))/(x − p)ⁿ = 0, (2) (Tₙ(f, p))⁽ᵏ⁾(p) = f⁽ᵏ⁾(p) pro 0 ≤ k ≤ n; Tₙ(f, p) je jediný polynom stupně ≤ n s těmito vlastnostmi

**Definice:** [[MA1 09 – Taylorův polynom, extrémy a monotonie#^veta-taylor|přednáška 9, 21. 10. 2026]] · handout 4A, slajd 17

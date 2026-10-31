---
aliases: ["důležité lemma", "tečna pod grafem konvexní funkce", "lokální minimum konvexní funkce je globální"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 11
zdroj: "handout 5B, slajd 8"
---

# lemma o konvexních funkcích

> [!lidsky] Lidsky
> U konvexní funkce s derivací leží každá tečna pod grafem. Proto je každé lokální minimum zároveň globální a platí Jensenova nerovnost.
>
> *Příklad:* pro eˣ a p = 0 je tečna y = 1 + x, takže 1 + x ≤ eˣ pro všechna x. x² má jediné lokální minimum 0 a to je globální.

> [!obrazek] Tečna pod grafem a myšlenka důkazu
> ![[ma111-tecna-pod-grafem.png]]
> *Vlevo: oranžová tečna v bodě p leží celá pod modrým grafem konvexní funkce, zelené úsečky jsou nezáporné rozdíly f(x) − (tečna). Vpravo případ x < p: červená sečna z x do p má podle Lagrange směrnici f′(t) pro nějaké t mezi nimi, a protože f′ je neklesající, je nejvýš směrnice tečny f′(p).*

**Formálně:** f má první derivaci na ℝ a je na ℝ konvexní ⇒ (1) f′(p)(x − p) + f(p) ≤ f(x) pro všechna p, x; (2) každé lokální minimum f je globální; (3) f(∑ aᵢxᵢ) ≤ ∑ aᵢ f(xᵢ) pro aᵢ ≥ 0, ∑ aᵢ = 1

**Definice:** [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál#^veta-lemma-konvexni|přednáška 11, 29. 10. 2026]] · handout 5B, slajd 8

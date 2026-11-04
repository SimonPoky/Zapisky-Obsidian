---
aliases: ["substituce v integrálu", "substituční metoda", "substituce v určitém integrálu"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 12
zdroj: "handout 6B, slajd 9"
---

# věta o substituci v určitém integrálu

> [!lidsky] Lidsky
> Otočená Chain Rule: když integrand obsahuje vnitřní funkci φ(z) i její derivaci φ′(z), nahradíš dvojici novou proměnnou t = φ(z) a meze přepočítáš stejnou funkcí.
>
> *Příklad:* ∫₀^√(π/2) cos(z²)·2z dz = ∫₀^(π/2) cos t dt = 1 (φ(z) = z², meze 0 ↦ 0, √(π/2) ↦ π/2).

**Formálně:** Ať φ je spojitá na [a; b] a má spojitou derivaci; ať f je taková, že f ∘ φ je spojitá na [a; b]. Potom ∫_{φ(a)}^{φ(b)} f(t) dt = ∫ₐᵇ f(φ(z))·φ′(z) dz

**Definice:** [[MA1 12 – Linearita, per partes a substituce v integrálu#^veta-substituce-integral|přednáška 12, 4. 11. 2026]] · handout 6B, slajd 9

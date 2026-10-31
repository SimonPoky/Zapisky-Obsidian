---
aliases: ["gradientní sestup", "gradient descentu", "Gradient-Descent"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 11
zdroj: "handout 5B, slajdy 5–7"
---

# gradient descent

> [!lidsky] Lidsky
> Iterační metoda hledání lokálního minima: ze současného bodu udělej krok proti směru růstu funkce a opakuj. Takhle se (ve více proměnných) učí neuronové sítě.
>
> *Příklad:* f(x) = x², x₀ = 1, γ = 1/4: x₁ = 1 − 1/4 · 2 = 0,5, x₂ = 0,25, x₃ = 0,125, blíží se k minimu 0.

> [!obrazek] Proč gradient descent chce konvexitu
> ![[ma111-gradient-descent.png]]
> *Oranžové body jsou kroky metody. Vlevo konvexní funkce: lokální minimum je podle lemmatu globální (zelená hvězda), metoda dojde tam, kam má. Vpravo nekonvexní funkce: kroky skončí v lokálním minimu (červený kroužek) a globální minimum vlevo nenajdou.*

**Formálně:** vstup f s první derivací, x₀, γ > 0, T ∈ ℕ; xᵢ₊₁ = xᵢ − γ · f′(xᵢ) pro i = 0, …, T − 1; výstup x_avg = (1/T) ∑ xᵢ; pro konvexní f je |f(x_avg) − f(x_min)| ≤ RL/√T

**Definice:** [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál#^gradient-descent|přednáška 11, 29. 10. 2026]] · handout 5B, slajdy 5–7

---
aliases: ["limita je lineární", "podprostor funkcí s vlastní limitou"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 5
zdroj: "handout 2B, slajd 17"
---

# linearita limity

> [!lidsky] Lidsky
> Limita lineární kombinace je lineární kombinace limit, pokud jsou všechny limity vlastní. Funkce s vlastní limitou tvoří podprostor prostoru funkcí a limita je na něm lineární zobrazení.
>
> *Příklad:* lim_{x→+∞} (3 + 2/x) = 3 + 2·lim 1/x = 3 + 0 = 3. Pro nevlastní limity to neplatí: x a −x mají limity +∞ a −∞, ale x + (−x) = 0.

> [!obrazek] Limita jako lineární zobrazení
> ![[ma105-podprostor.png]]
> *Šedá brambora jsou všechny funkce na D, modrý rovnoběžník W ty s vlastní limitou. Červená funkce limitu nemá nebo je nevlastní, leží mimo W. Modrá šipka lim𝒮 posílá každou funkci z W na číslo; zelená kombinace rf + sg jde na stejnou kombinaci čísel.*

**Formálně:** lim_𝒮 fᵢ ∈ ℝ ⇒ lim_𝒮 Σ rᵢfᵢ = Σ rᵢ lim_𝒮 fᵢ; {f | lim_𝒮 f ∈ ℝ} ≤ Func(D; ℝ)

**Definice:** [[MA1 05 – Aritmetika limit a substituce#^dusledek-linearita|přednáška 5, 7. 10. 2026]] · handout 2B, slajd 17

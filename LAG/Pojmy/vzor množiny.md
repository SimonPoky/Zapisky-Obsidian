---
aliases: ["f⁻¹(N)", "vzor", "vzor vektoru", "vzor bodu", "vzorem"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 10
zdroj: "pozn. 7.4"
---

# vzor množiny

> [!lidsky] Lidsky
> Odkud se dá dostat do N: všechny body definičního oboru, které f pošle do N. Existuje pro každé zobrazení, i bez inverze; může být i prázdný.
>
> *Příklad:* pro f(x) = x² je f⁻¹([1; 4]) = [−2; −1] ∪ [1; 2] a f⁻¹({−1}) = ∅. Pro A = $\begin{pmatrix}1&-1\\0&0\end{pmatrix}$ je A⁻¹{(−3; 0)} = {(−3; 0)} + span{(1; 1)}, přímka x − y = −3.

> [!obrazek] Kam se co zobrazí
> ![[lag10-vzory.png]]
> *Vlevo vzory: červená přímka $x - y = -3$ se celá zobrazí do červeného bodu $(-3; 0)$ (třeba $(-1; 2) \mapsto (-3; 0)$), zelená přímka $x - y = 0$ do nuly, modrá $x - y = 2$ do $(2; 0)$. Vpravo obraz: celá rovina skončí na oranžové ose $x$. Zobrazení tedy promítá rovinu na osu $x$ pod úhlem $45°$.*

**Formálně:** f: A → B, N ⊆ B ⇒ f⁻¹(N) = {x ∈ A | f(x) ∈ N}; vzor vektoru b je f⁻¹({b})

**Definice:** [[LAG 10 – Obraz a vzor při lineárním zobrazení#^def-obraz-vzor-mnoziny|přednáška 10, 23. 10. 2026]] · pozn. 7.4

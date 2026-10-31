---
aliases: ["transformace souřadnic", "přepočet souřadnic"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 9
zdroj: "pozn. 6.27"
---

# věta o transformaci souřadnic

> [!lidsky] Lidsky
> Znáš souřadnice v jedné bázi a chceš je v jiné? Vynásob je maticí přechodu; šipka v indexu ukazuje směr překladu.
>
> *Příklad:* pro 𝒳 = ((1; 1), (−1; 1)) je [id]^{ℰ→𝒳} = $\begin{pmatrix}1/2&1/2\\-1/2&1/2\end{pmatrix}$ a [(1; 3)]^𝒳 = (½ + 3/2; −½ + 3/2) = (2; 1); kontrola 2(1; 1) + 1·(−1; 1) = (1; 3).

> [!obrazek] Stejný vektor, dvoje souřadnice
> ![[lag09-prechod.png]]
> *Šedá mřížka patří kanonické bázi, zelená bázi $\mathcal{X}$ (modrý $\vec{x}_1$, oranžový $\vec{x}_2$). Červený vektor $\vec{v}$ je v kanonické mřížce $(1; 3)$, v zelené mřížce dva kroky po $\vec{x}_1$ a jeden po $\vec{x}_2$, tedy $[\vec{v}]^{\mathcal{X}} = (2; 1)$.*

**Formálně:** V lineární prostor nad 𝔽 konečné dimenze, 𝒳, 𝒴 báze V, v ∈ V ⇒ [v]^𝒴 = [id]^{𝒳→𝒴} · [v]^𝒳 (věta o souřadnicích obrazu pro A = id)

**Definice:** [[LAG 09 – Algebra matic a transformace souřadnic#^veta-transformace-souradnic|přednáška 9, 21. 10. 2026]] · pozn. 6.27

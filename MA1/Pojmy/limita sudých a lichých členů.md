---
aliases: ["sudé a liché členy", "a_{2k} a a_{2k+1}"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 5
zdroj: "handout 2B, slajd 22"
---

# limita sudých a lichých členů

> [!lidsky] Lidsky
> Sudé a liché indexy dohromady pokryjí všechny. Jdou-li sudé i liché členy ke stejnému L, jde tam celá posloupnost; jdou-li jinam, limita neexistuje.
>
> *Příklad:* aₙ = (−1)ⁿ: sudé členy jsou 1, liché −1, limity se liší, takže lim aₙ neexistuje. bₙ = (−1)ⁿ/n: sudé i liché jdou k 0, tedy lim bₙ = 0.

> [!obrazek] (−1)ⁿ rozdělená na sudé a liché členy
> ![[ma105-minus-jedna.png]]
> *Zeleně sudé členy, všechny rovné 1, oranžově liché, všechny −1. Každá z obou podposloupností má limitu, ale jinou, takže celá posloupnost limitu nemá.*

> [!obrazek] Které substituce pokryjí kus směru n → +∞
> ![[ma105-indexy.png]]
> *Šedé čtverečky jsou indexy k, kolečka indexy n. Barevná kolečka jsou ta, kam substituce dopadne, šedá zůstala netrefená. Nahoře k ↦ k² + 6 trefí jen 6, 7, 10, 15, 22, …, na detekci limity to nestačí. Uprostřed posun k ↦ k + 3 trefí všechna n ≥ 3. Dole sudé (modře) a liché (oranžově) indexy dohromady trefí úplně všechno.*

**Formálně:** lim_{n→+∞} aₙ = L ⟺ lim_{k→+∞} a_{2k} = L a lim_{k→+∞} a_{2k+1} = L

**Definice:** [[MA1 05 – Aritmetika limit a substituce#^dusledek-suda-licha|přednáška 5, 7. 10. 2026]] · handout 2B, slajd 22

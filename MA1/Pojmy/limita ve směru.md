---
aliases: ["limita", "limity", "limitu", "lim"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 3
zdroj: "handout 2A, slajd 17"
---

# limita ve směru

> [!lidsky] Lidsky
> Hra: soupeř zvolí jakkoli malý terč kolem L, ty najdeš kus směru, jehož celý obraz padne do terče. Umíš-li vyhrát vždy, je limita L. Limita je nejvýš jedna.
>
> *Příklad:* lim 1/x pro x → +∞ je 0: zvolí-li soupeř terč (−0,01; 0,01), stačí kus směru (100; +∞), protože tam je 0 < 1/x < 0,01. Na menší terč odpovíš větším číslem místo 100.

> [!obrazek] Dva terče: definice limity obrázkem
> ![[ma103-terce.png]]
> *Vpravo modrý čárkovaný terč U kolem L, soupeř ho volí jakkoli malý. Vlevo oranžový kus směru P kolem p bez bodu p, ten hledáš ty. Zelená skvrna f[P] (obraz P) musí ležet celá v terči. Dole menší terč, a proto i menší P. Kruhy jsou schéma, v ℝ jde o intervaly.*

> [!obrazek] Limita v bodě: pás ε a pás δ
> ![[ma103-epsdelta.png]]
> *Modrý pás: hodnoty vzdálené od L méně než ε (terč). Oranžový pás: x vzdálená od p méně než δ, bez samotného p. Zelený kus grafu nad oranžovým pásem leží celý v modrém pásu. Červený bod: hodnota f(p) může být kdekoli, nebo nemusí existovat vůbec.*

**Formálně:** lim_𝒮 f = L ⇔ ∀U ∈ 𝒩(L) ∃P ∈ 𝒮: f[P] ⊆ U, kde f[P] = {f(x) | x ∈ P}

**Definice:** [[MA1 03 – Rozšířená reálná čísla a limita ve směru#^def-limita|přednáška 3, 30. 9. 2026]] · handout 2A, slajd 17

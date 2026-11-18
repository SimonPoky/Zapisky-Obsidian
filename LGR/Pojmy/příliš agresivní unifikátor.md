---
aliases: ["agresivní unifikátor", "příliš agresivní substituce"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajd 36"
---

# příliš agresivní unifikátor

> [!lidsky] Lidsky
> Unifikátor, který kromě nutných substitucí dosadí i něco navíc. Výsledek z klauzulí sice plyne, ale konflikt zúží a rezolventou není; dalším krokem se pak může minout spor.
>
> *Příklad:* pro R(b, t) a R(u, f(v)) je θ = (u := b, v := b, t := f(b)) příliš agresivní: dá ¬S(f(b)) místo ∀v ¬S(f(v)) a ten už s S(f(a)) spor nedá.

**Formálně:** θ srovná L₁, L₂, ale obsahuje substituci, která není nutná (není maximální unifikátor); res(α(θ), β(θ)) plyne z {α, β}, ale není res(α, β)

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-agresivni|přednáška 12, 12. 11. 2026]] · handout 7, slajd 36

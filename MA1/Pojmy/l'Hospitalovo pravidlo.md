---
aliases: ["l'Hospital", "l'Hospitala", "l'Hospitalova pravidla", "de l'Hospitalovo pravidlo", "L'Hôpitalovo pravidlo"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 8
zdroj: "handout 4A, slajd 9"
---

# l'Hospitalovo pravidlo

> [!lidsky] Lidsky
> U limit typu 0/0 nebo ?/|±∞| rozhoduje o podílu poměr rychlostí změny: lim f/g = lim f′/g′, pokud ta druhá limita existuje. Je to implikace, ne ekvivalence.
>
> *Příklad:* lim_{x→0} sin x/x je typu 0/0 a podíl derivací cos x/1 → 1, takže limita je 1. lim_{x→+∞} x/eˣ je typu ?/+∞ a podíl derivací 1/eˣ → 0.

> [!obrazek] Podíl funkcí konverguje, podíl derivací ne
> ![[ma108-lhospital.png]]
> *Vlevo modře (x + cos x)/x, tlumeně kmitá kolem zelené úrovně 1 a k ní konverguje. Vpravo oranžově podíl derivací 1 − sin x, který kmitá mezi 0 a 2 pořád stejně, takže limitu nemá.*

**Formálně:** 𝒮 je x → ±∞, x → p, x → p⁻ nebo x → p⁺; f, g mají derivaci na kusu P ∈ 𝒮, g ≠ 0 a g′ ≠ 0 na P; (lim f = lim g = 0 nebo lim |g| = +∞); existuje lim f′/g′ (vlastní nebo nevlastní) ⇒ existuje lim f/g a lim f/g = lim f′/g′

**Definice:** [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo#^veta-lhospital|přednáška 8, 15. 10. 2026]] · handout 4A, slajd 9

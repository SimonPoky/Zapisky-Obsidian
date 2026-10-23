---
aliases: ["Kalmárovo lemma"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4D, slajd 13"
---

# lemma o literálech řádku

> [!lidsky] Lidsky
> Pravdivostní tabulka jde přepsat do důkazů: z literálů každého řádku jde odvodit φ, nebo ¬φ, podle toho, co je v tom řádku pravda.
>
> *Příklad:* φ = a ∧ ¬b a u(a) = 1, u(b) = 0: u(φ) = 1, L_u = {a, ¬b} a lemma dá L_u ⊢ a ∧ ¬b (stačí ∧i). Pro u(a) = 0, u(b) = 0 je u(φ) = 0 a lemma dá {¬a, ¬b} ⊢ ¬(a ∧ ¬b).

**Formálně:** φ formule, u ohodnocení, L_u literály řádku u: u(φ) = 1 ⇒ L_u ⊢ φ; u(φ) = 0 ⇒ L_u ⊢ ¬φ; důkaz strukturální indukcí podle φ

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-lemma-literaly|přednáška 7, 22. 10. 2026]] · handout 4D, slajd 13 · krok pro ⇒: [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^veta-lemma-implikace|přednáška 8]]

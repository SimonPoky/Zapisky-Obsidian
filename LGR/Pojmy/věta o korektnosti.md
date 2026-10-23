---
aliases: ["korektnost přirozené dedukce"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 7
zdroj: "handout 4, slajd 14"
---

# věta o korektnosti

> [!lidsky] Lidsky
> Přirozená dedukce nedokáže nepravdu: co jde odvodit, to z předpokladů opravdu plyne.
>
> *Příklad:* jde odvodit a ⇒ b, ¬b ⊢ ¬a (MT), takže platí i a ⇒ b, ¬b ⊨ ¬a. Obráceně: a ∨ b ⊭ a (u(a) = 0, u(b) = 1), a proto ani a ∨ b ⊢ a odvodit nejde.

**Formálně:** pro každou S a φ: S ⊢ φ ⇒ S ⊨ φ; důkaz silnou indukcí podle délky odvození (každé pravidlo respektuje pravdivost)

**Definice:** [[LGR 07 – Odvozená pravidla, korektnost a úplnost#^veta-korektnost|přednáška 7, 22. 10. 2026]] · handout 4, slajd 14 · důkaz: handout 4D, slajd 10

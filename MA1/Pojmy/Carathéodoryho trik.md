---
aliases: ["Carathéodoryho lemma", "Carathéodoryho triku", "Carathéodoryho funkce", "f*"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 7
zdroj: "handout 3B, slajd 8"
---

# Carathéodoryho trik

> [!lidsky] Lidsky
> Derivaci lze převést na spojitost: f(x) − f(p) se dá napsat jako f*(x) · (x − p), kde f*(x) je směrnice sečny a v bodě p směrnice tečny. Derivace existuje, právě když je tahle funkce f* v p spojitá.
>
> *Příklad:* f(x) = x², p = 3: x² − 9 = (x + 3)(x − 3), takže f*(x) = x + 3. Ta je spojitá v 3 a f′(3) = f*(3) = 6.

> [!obrazek] f* pro x² v bodě 1
> ![[ma107-fstar.png]]
> *Vlevo modře x², červený bod [1; 1], oranžová sečna k bodu x = 2 má směrnici 3, zelená tečna směrnici 2. Vpravo modře f*(x) = x + 1, protože x² − 1 = (x + 1)(x − 1): oranžový bod f*(2) = 3 je směrnice sečny, zelený bod f*(1) = 2 je směrnice tečny, tedy f′(1). Graf f* je spojitý, žádná díra v bodě 1.*

**Formálně:** f definovaná na (a; b), p ∈ (a; b): f′(p) existuje ⇔ existuje f* spojitá v p s f(x) − f(p) = f*(x)·(x − p) pro všechna x ∈ (a; b); pak f′(p) = f*(p)

**Definice:** [[MA1 07 – Derivace a Carathéodoryho trik#^veta-caratheodory|přednáška 7, 14. 10. 2026]] · handout 3B, slajd 8

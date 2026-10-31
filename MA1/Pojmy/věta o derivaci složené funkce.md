---
aliases: ["Chain Rule", "derivace složené funkce", "řetízkové pravidlo", "řetízkového pravidla"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 7
zdroj: "handout 3B, slajd 13"
---

# věta o derivaci složené funkce

> [!lidsky] Lidsky
> Derivace složené funkce je součin derivací vrstev: vnější derivace (vyhodnocená tam, kam ukazuje vnitřní funkce) krát vnitřní derivace. Jako převody: dvakrát krát třikrát je šestkrát.
>
> *Příklad:* (sin(x²))′ = cos(x²)·2x a (e^{3x})′ = e^{3x}·3. V prvním případě je vnější funkce sin, vnitřní x².

> [!obrazek] Řetízek vrstev
> ![[ma107-retizek.png]]
> *Modré rámečky jsou mezivýsledky, oranžové šipky funkce u, v, w, zeleně pod nimi jejich derivace. Červený vzorec: derivace celku je součin derivací vrstev, každá vyhodnocená v bodě, kam zrovna ukazuje předchozí vrstva.*

**Formálně:** f′(p) a g′(f(p)) existují ⇒ (g ∘ f)′(p) = g′(f(p)) · f′(p)

**Definice:** [[MA1 07 – Derivace a Carathéodoryho trik#^veta-chain-rule|přednáška 7, 14. 10. 2026]] · handout 3B, slajd 13

---
aliases: ["IVT", "Bolzanova věta", "věty o mezihodnotě", "Intermediate Value Theorem"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 6
zdroj: "handout 3A, slajd 14"
---

# věta o mezihodnotě

> [!lidsky] Lidsky
> Spojitá funkce na [a; b] nabude každé hodnoty mezi f(a) a f(b): aby se graf dostal z jedné výšky do druhé, musí projít všemi mezi nimi.
>
> *Příklad:* f(x) = x³ − x − 1 je spojitá, f(1) = −1 < 0 a f(2) = 5 > 0, takže rovnice x³ − x − 1 = 0 má kořen v [1; 2].

> [!obrazek] IVT, BT, EVT a PIT
> ![[ma106-vety.png]]
> *Vlevo nahoře: oranžová výška r leží mezi modrými f(a) a f(b) a graf ji protne v zeleném bodě. Vpravo nahoře: celý graf se vejde do oranžového pásu. Vlevo dole: zelený nejvyšší a červený nejnižší bod existují. Vpravo dole: oranžová úsečka na svislé ose je obraz, celý interval od minima po maximum.*

> [!obrazek] Proč musí být interval uzavřený
> ![[ma106-otevreny.png]]
> *Vlevo modře $\frac{1}{x}$ na $(0; 1]$: je spojitá, ale u nuly (červená šipka) roste nade všechny meze, BT selže. Vpravo $x$ na $(0; 1)$: je omezená, ale oranžové hranice $0$ a $1$ (prázdné kroužky) nenabude, EVT selže.*

**Formálně:** f spojitá na [a; b], r mezi f(a) a f(b) ⇒ ∃t ∈ [a; b]: f(t) = r

**Definice:** [[MA1 06 – Spojitost a spojité funkce na intervalu#^veta-ctyri|přednáška 6, 8. 10. 2026]] · handout 3A, slajd 14

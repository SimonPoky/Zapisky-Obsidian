---
predmet: MA1
prednaska: 8
datum: 2026-10-15
zdroj: "Handout 4A (Složitější věty o derivacích), slajdy 3–15"
tags: [prednaska, MA1]
---

# MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo

*Přednáška 8 · čtvrtek 15. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 4A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout04a.pdf)

Témata: `derivace na [a; b]` · `Rolleova věta` · `determinant D(x)` · `Lagrangeova věta` · `f′ = 0 ⇒ konstanta` · `Cauchyova věta` · `l'Hospitalovo pravidlo` · `typ 0/0 a ?/|±∞|` · `implikace, ne ekvivalence` · `0 · ∞ a 1^∞` · `lineární aproximace T₁`

Minule jsme derivaci zavedli v jednom bodě. Dnes jde o to, co derivace říká o funkci na celém intervalu: tři věty o střední hodnotě (Rolle, Lagrange, Cauchy) spojují přírůstek $f(b) - f(a)$ s hodnotou derivace v nějakém bodě uvnitř. Z Cauchyovy věty plyne l'Hospitalovo pravidlo, nástroj na „podivné“ limity typu $\frac{0}{0}$. Na konci začíná motivace Taylorova polynomu: tečna jako nejlepší lineární aproximace funkce.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| derivace na $[a; b]$ | | $f'(p)$ uvnitř, $f'_+(a)$, $f'_-(b)$; pak je $f$ spojitá na $[a; b]$ |
| Rolle | $f'$ na $[a; b]$, $f(a) = f(b)$ | $\exists t \in (a; b)$: $f'(t) = 0$ |
| důsledek Rolleovy věty | $f, g, h$ mají derivaci na $[a; b]$ | $D(x) = \det(\text{sloupce } a, x, b)$ má $D'(t) = 0$ pro nějaké $t \in (a; b)$ |
| Lagrange | $f'$ na $[a; b]$ | $\exists t \in (a; b)$: $\frac{f(b) - f(a)}{b - a} = f'(t)$ |
| nulová derivace | $f' = 0$ na $[a; b]$ | $f$ je na $[a; b]$ konstantní |
| Cauchy | $f', g'$ na $[a; b]$ | $\exists t$: $\big(f(b) - f(a)\big) g'(t) = \big(g(b) - g(a)\big) f'(t)$; při $g' \neq 0$ uvnitř $\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(t)}{g'(t)}$ |
| l'Hospital | $f', g'$ na kusu $P$ směru, $g, g' \neq 0$ na $P$; $\lim f = \lim g = 0$ nebo $\lim \lvert g \rvert = +\infty$; $\lim \frac{f'}{g'}$ existuje | $\lim \frac{f}{g} = \lim \frac{f'}{g'}$ |
| lineární aproximace | $f'(p)$ existuje | $\lim_{x \to p} \frac{f(x) - T_1(f, p)(x)}{x - p} = 0$, $T_1(f, p)(x) = f(p) + f'(p)(x - p)$ |

## §1 Derivace na uzavřeném intervalu

Všechny dnešní věty předpokládají, že $f$ má derivaci na celém $[a; b]$. Co to přesně znamená:

> [!definice] Derivace na uzavřeném intervalu · handout 4A, slajd 3
> Funkce $f$ **má první derivaci na uzavřeném omezeném intervalu $[a; b]$**, když:
>
> 1. $f$ má [[derivace v bodě|derivaci]] $f'(p)$ v každém vnitřním bodě $p \in (a; b)$,
> 2. $f$ má [[jednostranná derivace|derivaci zprava]] $f'_+(a)$ v bodě $a$,
> 3. $f$ má derivaci zleva $f'_-(b)$ v bodě $b$.
>
> Taková funkce je nutně [[spojitost na intervalu|spojitá na $[a; b]$]]: spojitá v každém vnitřním bodě, zprava spojitá v $a$ a zleva spojitá v $b$.

^def-derivace-interval

> [!lidsky] Lidsky
> [[derivace na intervalu|Derivace na $[a; b]$]] znamená, že graf má tečnu všude, kam se dá dojít: uvnitř normální, na krajích jen tu „z vnitřní strany“, protože ven z intervalu se nedíváme. Spojitost plyne z [[věta o spojitosti funkce s derivací|věty „derivace ⇒ spojitost“]], která platí i jednostranně (důkaz přes Carathéodoryho trik jde stejně).

## §2 Rolleova věta

> [!veta] Rolleova věta (první věta o střední hodnotě) · handout 4A, slajd 4
> ==Ať $f$ má první derivaci na $[a; b]$ a ať $f(a) = f(b)$.== Potom **existuje $t \in (a; b)$ takové, že $f'(t) = 0$.**
>
> > [!note]- Důkaz
> > **(i) $f$ je na $[a; b]$ konstantní.** Pak $f'(t) = 0$ pro každé $t \in (a; b)$.
> >
> > **(ii) $f$ není konstantní.** $f$ je spojitá na $[a; b]$ (§1), takže podle [[věta o extrémech|věty o extrémech]] (EVT) nabývá maxima i minima. Protože $f$ není konstantní a $f(a) = f(b)$, existuje bod s hodnotou různou od $f(a)$; je-li větší, leží maximum **uvnitř** $(a; b)$, je-li menší, leží uvnitř minimum. Ať je to maximum v bodě $t \in (a; b)$ (minimum obdobně). Ukážeme $f'(t) = 0$ sporem.
> >
> > Ať $f'(t) > 0$ ($f'(t) < 0$ analogicky). Protože $\lim_{h \to 0} \frac{f(t + h) - f(t)}{h} = f'(t) > 0$, je podle [[věta o znaménku limity|věty o znaménku limity]] $\frac{f(t + h) - f(t)}{h} > 0$ pro všechna dost malá $h \neq 0$. Pro malé **$h > 0$** z toho plyne
> >
> > $$
> > \frac{f(t + h) - f(t)}{h} > 0 \iff f(t + h) - f(t) > 0 \iff f(t + h) > f(t),
> > $$
> >
> > což je spor s tím, že $f(t)$ je maximum. Pro $f'(t) < 0$ dává spor $h < 0$: podíl je pak záporný a $h < 0$, takže čitatel $f(t + h) - f(t) > 0$, tedy opět $f(t + h) > f(t)$. Zbývá $f'(t) = 0$.

^veta-rolle

> [!lidsky] Lidsky
> [[Rolleova věta]]: když vyjdeš z údolí a vrátíš se do stejné výšky, musel jsi někde být na vrcholu (nebo na dně), a tam jsi na okamžik šel přesně vodorovně. Hladká funkce se nemůže otočit z „nahoru“ na „dolů“ bez okamžiku s nulovým sklonem.

> [!obrazek] Rolle a Lagrange
> ![[ma108-rolle-lagrange.png]]
> *Vlevo: modrý graf začíná a končí ve stejné výšce (červené body, šedá čára). Ve vrcholu t je zelená tečna vodorovná, f′(t) = 0. Vpravo: oranžová sečna spojuje červené krajní body; v bodě t je zelená tečna s ní rovnoběžná, takže f′(t) je směrnice sečny.*

> [!obrazek] Proč je v maximu derivace nulová
> ![[ma108-rolle-dukaz.png]]
> *Červený bod je maximum v t. Oranžové sečny k bodům vpravo (h > 0) mají směrnici ≤ 0, zelené sečny k bodům vlevo (h < 0) směrnici ≥ 0. Derivace je limita obou, takže musí být zároveň ≤ 0 i ≥ 0, tedy 0 (šedá vodorovná tečna).*

> [!pozor] Spojitost nestačí
> Bez derivace uvnitř věta neplatí: $f(x) = \lvert x \rvert$ na $[-1; 1]$ splňuje $f(-1) = f(1)$ a je spojitá, ale $f'(t) = \pm 1$ všude, kde existuje. Vadí jediný bod $0$, kde derivace chybí. Bod $t$ z věty navíc nemusí být jediný a věta neříká, jak ho najít.

## §3 Důsledek Rolleovy věty: determinant tří funkcí

Lagrangeova i Cauchyova věta jsou speciální případy jednoho triku: Rolleovu větu použijeme na šikovně postavený determinant.

> [!veta] Důsledek Rolleovy věty · handout 4A, slajd 5
> ==Ať $f$, $g$ a $h$ mají první derivaci na $[a; b]$.== Na $[a; b]$ definujme
>
> $$
> D(x) = \begin{vmatrix} f(a) & f(x) & f(b) \\ g(a) & g(x) & g(b) \\ h(a) & h(x) & h(b) \end{vmatrix}.
> $$
>
> Potom:
>
> 1. **$D$ má první derivaci na $[a; b]$** a $D'(x) = \begin{vmatrix} f(a) & f'(x) & f(b) \\ g(a) & g'(x) & g(b) \\ h(a) & h'(x) & h(b) \end{vmatrix}$.
> 2. **Existuje $t \in (a; b)$ takové, že $D'(t) = 0$.**
>
> > [!note]- Důkaz
> > (1) Rozviň $D(x)$ podle druhého sloupce: $D(x) = -f(x)\,M_{12} + g(x)\,M_{22} - h(x)\,M_{32}$, kde minory $M_{12}, M_{22}, M_{32}$ obsahují jen hodnoty v $a$ a $b$, tedy jsou to **konstanty**. $D$ je tedy lineární kombinace $f$, $g$, $h$ a podle [[věta o aritmetice derivací|aritmetiky derivací]] (uvnitř i jednostranně na krajích) má derivaci $D'(x) = -f'(x)\,M_{12} + g'(x)\,M_{22} - h'(x)\,M_{32}$, což je přesně determinant s derivacemi ve druhém sloupci.
> >
> > (2) $D(a)$ má první dva sloupce stejné a $D(b)$ druhý a třetí sloupec stejný, takže **$D(a) = D(b) = 0$**. Stačí použít Rolleovu větu na $D$.

^veta-rolle-dusledek

> [!lidsky] Lidsky
> [[důsledek Rolleovy věty|Determinant $D(x)$]] je stroj na věty o střední hodnotě. V krajních bodech má dva stejné sloupce, takže je nulový na obou koncích, a Rolle hned dá bod s nulovou derivací. Volbou $g$ a $h$ pak z rovnosti $D'(t) = 0$ vypadne buď Lagrange, nebo Cauchy.

> [!pozor] Častá chyba při opisování $D'(t)$
> V $D'(t)$ se derivuje **jen prostřední sloupec**; první a třetí sloupec zůstávají hodnoty v $a$ a v $b$. Poslední řádek je tedy $h(a) \;\; h'(t) \;\; h(b)$, ne $h(a) \;\; h'(t) \;\; h(a)$: s dvakrát $h(a)$ by determinant neodpovídal funkci $D$.

## §4 Lagrangeova věta

> [!veta] Lagrangeova věta (druhá věta o střední hodnotě) · handout 4A, slajd 6
> ==Ať $f$ má první derivaci na $[a; b]$.== Potom **existuje $t \in (a; b)$ takové, že**
>
> $$
> \frac{f(b) - f(a)}{b - a} = f'(t).
> $$
>
> > [!note]- Důkaz
> > V důsledku Rolleovy věty zvol $g(x) = x$ a $h(x) = 1$, takže $g'(x) = 1$, $h'(x) = 0$. Pro nějaké $t \in (a; b)$ je
> >
> > $$
> > 0 = D'(t) = \begin{vmatrix} f(a) & f'(t) & f(b) \\ a & 1 & b \\ 1 & 0 & 1 \end{vmatrix} = f(a) + f'(t) \cdot b \cdot 1 - f(b) - a \cdot f'(t).
> > $$
> >
> > (Sarrusovo pravidlo; nenulové jsou jen čtyři součiny.) Tedy $f'(t)\,(b - a) = f(b) - f(a)$ a po vydělení $b - a > 0$ dostaneme tvrzení.

^veta-lagrange

> [!lidsky] Lidsky
> [[Lagrangeova věta]]: ujedeš-li za 2 hodiny 180 km, ukazoval tachometr v nějakém okamžiku přesně 90 km/h. Průměrná rychlost $\frac{f(b) - f(a)}{b - a}$ se někde nabude jako okamžitá rychlost $f'(t)$. Geometricky: někde je tečna rovnoběžná se sečnou krajních bodů. Rolleova věta je speciální případ s vodorovnou sečnou.

> [!veta] Funkce s nulovou derivací je konstantní · handout 4A, slajd 6
> ==Ať $f'(x) = 0$ pro všechna $x \in [a; b]$== (jednostranně v krajních bodech). Potom **$f$ je na $[a; b]$ konstantní.**
>
> > [!note]- Důkaz
> > Ať $x \in (a; b]$. Na $[a; x]$ má $f$ derivaci, takže podle Lagrangeovy věty existuje $t \in (a; x)$ s $f(x) - f(a) = f'(t)\,(x - a) = 0 \cdot (x - a) = 0$. Tedy $f(x) = f(a)$ pro každé $x$.

^veta-nulova-derivace

> [!lidsky] Lidsky
> [[věta o nulové derivaci]]: auto, které nikdy nemá nenulovou rychlost, stojí na místě. Zní to samozřejmě, ale bez Lagrangeovy věty to dokázat nejde. V integrálním počtu z toho plyne, že dvě primitivní funkce se liší jen o konstantu.

> [!pozor] Jen na intervalu
> Na sjednocení intervalů to neplatí: $f(x) = \frac{x}{\lvert x \rvert}$ má na $(-\infty; 0) \cup (0; +\infty)$ derivaci $0$, ale nabývá hodnot $-1$ i $1$. Lagrangeova věta se dá použít jen na úsek bez „děr“.

## §5 Cauchyova věta

> [!veta] Cauchyova věta (třetí věta o střední hodnotě) · handout 4A, slajd 7
> ==Ať $f$ a $g$ mají první derivaci na $[a; b]$.== Potom:
>
> 1. **Existuje $t \in (a; b)$ takové, že $\big(f(b) - f(a)\big) \cdot g'(t) = \big(g(b) - g(a)\big) \cdot f'(t)$.**
> 2. Pokud navíc ==$g'(x) \neq 0$ pro všechna $x \in (a; b)$==, potom **$g(a) \neq g(b)$** a rovnost z (1) lze psát ve tvaru
>
> $$
> \frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(t)}{g'(t)}.
> $$
>
> > [!note]- Důkaz (1)
> > V důsledku Rolleovy věty zvol $h(x) = 1$, tedy $h'(x) = 0$. Rozvoj podle třetího řádku dá pro nějaké $t \in (a; b)$
> >
> > $$
> > 0 = D'(t) = \begin{vmatrix} f(a) & f'(t) & f(b) \\ g(a) & g'(t) & g(b) \\ 1 & 0 & 1 \end{vmatrix} = f'(t)\big(g(b) - g(a)\big) - g'(t)\big(f(b) - f(a)\big).
> > $$
>
> > [!note]- Důkaz (2)
> > Kdyby $g(a) = g(b)$, dala by Rolleova věta pro $g$ bod $s \in (a; b)$ s $g'(s) = 0$, spor s předpokladem. Takže $g(b) - g(a) \neq 0$, navíc $g'(t) \neq 0$, a rovností z (1) smíme obojím vydělit.

^veta-cauchy

> [!lidsky] Lidsky
> [[Cauchyova věta]] je Lagrange pro dvě funkce najednou. Představ si bod, který se v čase $x \in [a; b]$ pohybuje po rovině po křivce $\big[g(x); f(x)\big]$. Tětiva z počátečního do koncového bodu má směrnici $\frac{f(b) - f(a)}{g(b) - g(a)}$ a v nějakém okamžiku $t$ jede bod přesně v jejím směru, se směrnicí $\frac{f'(t)}{g'(t)}$. Lagrange je případ $g(x) = x$, kdy je křivka obyčejný graf.

> [!obrazek] Cauchyova věta geometricky
> ![[ma108-cauchy.png]]
> *Modrá křivka x ↦ [g(x); f(x)] se smí i zatočit do smyčky (není to graf funkce). Oranžová tětiva spojuje červené krajní body. V zeleném bodě je tečna ke křivce s tětivou rovnoběžná.*

> [!pozor] Proč nestačí použít Lagrange dvakrát
> Lagrange pro $f$ a pro $g$ zvlášť dá $f(b) - f(a) = f'(t_1)(b - a)$ a $g(b) - g(a) = g'(t_2)(b - a)$, ale **obecně s různými body $t_1 \neq t_2$**. Podíl pak není $\frac{f'(t)}{g'(t)}$ v jednom bodě. Cauchyova věta zaručí jeden společný bod $t$, a přesně to je potřeba pro l'Hospitala.

> [!navic] Nerovnosti o konečném přírůstku · handout 4A, slajd 8
> Věty o střední hodnotě lze nahradit dvěma nerovnostmi, které platí i pro funkce více proměnných: mají-li $f$ a $g$ první derivaci na $[a; b]$ a $\lvert f' \rvert < g'$ na $[a; b]$, je $\lvert f(b) - f(a) \rvert < g(b) - g(a)$ (a totéž s $\le$). Dál se s nimi nepracuje: důkazy jsou zdlouhavé a Cauchyova věta dává přímý důkaz l'Hospitalova pravidla.

## §6 l'Hospitalovo pravidlo

> [!veta] l'Hospitalovo pravidlo · handout 4A, slajd 9
> Ať ==$\mathcal{S}$ je některý ze [[směr|směrů]] $x \to +\infty$, $x \to -\infty$, $x \to p$, $x \to p^-$, $x \to p^+$==. Ať ==$f$ a $g$ mají derivaci na nějakém kusu $P \in \mathcal{S}$== a ==$g$ i $g'$ jsou na $P$ nenulové==. Ať je splněna jedna z podmínek:
>
> 1. (typ „$\frac{0}{0}$“) $\lim_{\mathcal{S}} f = 0$ a $\lim_{\mathcal{S}} g = 0$,
> 2. (typ „$\frac{?}{\lvert \pm\infty \rvert}$“) $\lim_{\mathcal{S}} \lvert g \rvert = +\infty$.
>
> Ať ==existuje (vlastní nebo nevlastní) $\lim_{\mathcal{S}} \frac{f'}{g'}$==. Potom **existuje i $\lim_{\mathcal{S}} \frac{f}{g}$ a platí**
>
> $$
> \lim_{\mathcal{S}} \frac{f}{g} = \lim_{\mathcal{S}} \frac{f'}{g'}.
> $$
>
> Důkaz se zde neuvádí (není těžký, ale je technický); jeho jádrem je Cauchyova věta.
>
> > [!note]- Idea důkazu pro typ $\frac{0}{0}$ a $x \to p^+$
> > Dodefinuj $f(p) = g(p) = 0$; tím jsou $f$, $g$ spojité zprava v $p$. Pro $x > p$ blízko $p$ dá Cauchyova věta na $[p; x]$ bod $t_x \in (p; x)$ s
> >
> > $$
> > \frac{f(x)}{g(x)} = \frac{f(x) - f(p)}{g(x) - g(p)} = \frac{f'(t_x)}{g'(t_x)}.
> > $$
> >
> > Pro $x \to p^+$ je i $t_x \to p^+$ (je sevřené mezi $p$ a $x$), takže pravá strana jde k $\lim_{x \to p^+} \frac{f'}{g'}$.

^veta-lhospital

> [!lidsky] Lidsky
> [[l'Hospitalovo pravidlo]]: když čitatel i jmenovatel společně mizí (nebo jmenovatel utíká do nekonečna), rozhoduje o podílu to, **jak rychle** se mění, tedy podíl jejich derivací. Dvě auta, která obě míří do nuly: poměr jejich vzdáleností od cíle je nakonec poměr jejich rychlostí. Derivuje se čitatel a jmenovatel **zvlášť**, ne podíl jako celek.

> [!pozor] Častá chyba: derivovat podíl
> V pravidle je $\frac{f'}{g'}$, ne $\left(\frac{f}{g}\right)'$. Pravidlo pro derivaci podílu tady nemá co dělat.

### Implikace, ne ekvivalence

> [!pozor] Extrémně důležité upozornění 1 · handout 4A, slajd 10
> l'Hospitalovo pravidlo je **implikace**: z existence $\lim \frac{f'}{g'}$ plyne existence $\lim \frac{f}{g}$. Když $\lim \frac{f'}{g'}$ neexistuje, **neříká pravidlo nic**.
>
> Příklad: $\lim_{x \to +\infty} \frac{x + \cos x}{x}$ je typ $\frac{?}{\lvert \pm\infty \rvert}$ ($f(x) = x + \cos x$, $g(x) = x$).
>
> 1. $\lim_{x \to +\infty} \frac{(x + \cos x)'}{(x)'} = \lim_{x \to +\infty} (1 - \sin x)$ **neexistuje** ([[Heineova věta]]: na $x_n = 2\pi n$ jde o $1$, na $x_n = \frac{\pi}{2} + 2\pi n$ o $0$).
> 2. Ale přímo: $\lim_{x \to +\infty} \frac{x + \cos x}{x} = \lim_{x \to +\infty} \frac{x}{x} \cdot \left(1 + \frac{\cos x}{x}\right) = 1$, protože $\frac{\cos x}{x} \to 0$ ([[věta o součinu nulové a omezené funkce|nula krát omezená]]).
>
> Nelze tedy bezmyšlenkovitě psát $\lim \frac{f}{g} = \lim \frac{f'}{g'}$, protože pravá strana nemusí existovat.

^pozor-implikace

> [!obrazek] Podíl funkcí konverguje, podíl derivací ne
> ![[ma108-lhospital.png]]
> *Vlevo modře (x + cos x)/x, tlumeně kmitá kolem zelené úrovně 1 a k ní konverguje. Vpravo oranžově podíl derivací 1 − sin x, který kmitá mezi 0 a 2 pořád stejně, takže limitu nemá.*

> [!pozor] Extrémně důležité upozornění 2 · handout 4A, slajd 11
> Pravidlo řeší **jen** situace $\frac{0}{0}$ a $\frac{?}{\lvert \pm\infty \rvert}$. Jinde podíl derivací použít nelze:
>
> $$
> \lim_{x \to 3} \frac{x^2}{x - 1} = \frac{9}{2}, \qquad \text{ale} \qquad \lim_{x \to 3} \frac{(x^2)'}{(x - 1)'} = \lim_{x \to 3} \frac{2x}{1} = 6.
> $$

### Kdy l'Hospitala použít

> [!navic] Neurčitý výraz („typ limity“) · termín z literatury; handout 4A (slajd 11) ho nepoužívá
> V literatuře se mluví o **typech limit** neboli **neurčitých výrazech**: $\frac{0}{0}$, $\frac{\pm\infty}{\pm\infty}$, $0 \cdot (\pm\infty)$, $(+\infty) - (+\infty)$, $1^{\pm\infty}$, $0^0$, $(+\infty)^0$. Zápis popisuje, k čemu jdou jednotlivé části výrazu; výsledek se z toho určit nedá, protože [[věta o aritmetice limit|aritmetika limit]] tyto kombinace nedefinuje. Typ $\frac{?}{\lvert \pm\infty \rvert}$ znamená: jmenovatel jde v absolutní hodnotě do $+\infty$, o čitateli nevíme nic.

^def-neurcity-vyraz

> [!lidsky] Lidsky
> [[neurčitý výraz|Neurčitý výraz]] je přetahovaná: v $\frac{0}{0}$ malý čitatel táhne podíl k nule, malý jmenovatel k nekonečnu, a kdo vyhraje, z typu nepoznáš. Proto se musí počítat dál. Velebil tuhle terminologii moc nepoužívá, protože svádí k memorování mnoha pravidel; stačí jedno pravidlo níže.

Jediné pravidlo (handout 4A, slajd 11):

1. Nedaří se limitu spočítat běžnými prostředky (aritmetika limit, vytýkání, sevření)? Chová se výraz ve směru nezvykle? Pokud ano, krok 2.
2. Zkus l'Hospitalovo pravidlo. Většinou to vyžaduje úpravu, aby vznikl typ $\frac{0}{0}$ nebo $\frac{?}{\lvert \pm\infty \rvert}$.

Typické úpravy: součin $f \cdot g$ přepiš jako $\frac{f}{1/g}$; mocninu $u^v$ přepiš jako $e^{v \ln u}$ a počítej limitu exponentu (exponenciála je spojitá, takže $\lim e^{(\ldots)} = e^{\lim (\ldots)}$).

> [!example] Typ $0 \cdot (-\infty)$: $\lim_{x \to 0^+} x^a \ln x$ pro pevné $a > 0$ · handout 4A, slajd 12
> 1. Převeď na typ $\frac{-\infty}{+\infty}$: $x^a \ln x = \frac{\ln x}{x^{-a}}$.
> 2. Podíl derivací:
>
> $$
> \lim_{x \to 0^+} \frac{(\ln x)'}{(x^{-a})'} = \lim_{x \to 0^+} \frac{\frac{1}{x}}{-a\,x^{-a-1}} = -\frac{1}{a} \lim_{x \to 0^+} x^{a} = 0.
> $$
>
> 3. Podle l'Hospitalova pravidla **$\lim_{x \to 0^+} x^a \ln x = 0$**: libovolně malá mocnina „přemůže“ logaritmus.

^priklad-xa-lnx

> [!example] Typ $1^{\pm\infty}$: $\lim_{x \to 1} x^{\frac{1}{x - 1}}$ · handout 4A, slajd 13
> 1. Uprav: $x^{\frac{1}{x - 1}} = e^{\ln x \cdot \frac{1}{x - 1}}$, takže stačí spočítat $\lim_{x \to 1} \frac{\ln x}{x - 1}$, typ $\frac{0}{0}$.
> 2. $\lim_{x \to 1} \frac{(\ln x)'}{(x - 1)'} = \lim_{x \to 1} \frac{1/x}{1} = 1$, tedy $\lim_{x \to 1} \frac{\ln x}{x - 1} = 1$.
> 3. Závěr: **$\lim_{x \to 1} x^{\frac{1}{x - 1}} = e^1 = e$.**

^priklad-1-na-nekonecno

> [!example] Opakované použití: $\lim_{x \to +\infty} \frac{x^3 - 2x + 1}{e^{3x}}$ · handout 4A, slajd 14
> Typ $\frac{+\infty}{+\infty}$. Třikrát po sobě:
>
> $$
> \lim \frac{(x^3 - 2x + 1)'}{(e^{3x})'} = \lim \frac{3x^2 - 2}{3e^{3x}} \;\to\; \lim \frac{6x}{9e^{3x}} \;\to\; \lim \frac{6}{27 e^{3x}} = 0.
> $$
>
> Poslední limita existuje, takže zpětně existují i předchozí a všechny jsou $0$. **Výsledek $0$**: exponenciála roste rychleji než každý polynom.

> [!pozor] Opakované použití se čte odzadu
> Při řetězení l'Hospitala nejde psát „$=$“ mezi kroky, dokud nevíš, že poslední limita existuje. Logika jde od poslední limity k první: existuje poslední, tedy existuje předposlední, a tak dál. Před každým krokem znovu ověř, že jde o typ $\frac{0}{0}$ nebo $\frac{?}{\lvert \pm\infty \rvert}$.

## §7 Lineární aproximace: motivace Taylorova polynomu

Z definice derivace pro $x$ blízko $p$, $x \neq p$:

$$
\frac{f(x) - f(p)}{x - p} \approx f'(p) \qquad \Longrightarrow \qquad f(x) \approx f(p) + f'(p)\,(x - p).
$$

> [!definice] Lineární aproximace $T_1(f, p)$ · handout 4A, slajd 15
> Ať $f$ má derivaci v bodě $p$. Funkce
>
> $$
> T_1(f, p)(x) = f(p) + f'(p)\,(x - p)
> $$
>
> je **lineární aproximace** $f$ v bodě $p$ (Taylorův polynom stupně $\le 1$); její graf je [[tečna]] v $[p; f(p)]$. Splňuje
>
> $$
> \lim_{x \to p} \frac{f(x) - T_1(f, p)(x)}{x - p} = 0.
> $$
>
> > [!note]- Důkaz limity přímo z definice
> > $\frac{f(x) - T_1(f, p)(x)}{x - p} = \frac{f(x) - f(p)}{x - p} - f'(p) \to f'(p) - f'(p) = 0$ pro $x \to p$.
>
> > [!note]- Důkaz l'Hospitalovým pravidlem
> > Typ $\frac{0}{0}$. Podíl derivací (derivuje se podle $x$, $f(p)$ a $f'(p)$ jsou konstanty):
> >
> > $$
> > \lim_{x \to p} \frac{f'(x) - f'(p)}{1} = 0,
> > $$
> >
> > pokud **$f'$ existuje na okolí $p$ a je spojitá v $p$**. Tenhle postup potřebuje silnější předpoklad než přímý důkaz výše, ale zobecní se na Taylorův polynom vyššího stupně.

^def-linearni-aproximace

> [!lidsky] Lidsky
> [[lineární aproximace|Lineární aproximace]]: zblízka vypadá každý hladký graf jako přímka, jeho tečna. Chyba $f(x) - T_1(x)$ není jen malá, je **zanedbatelná i vůči vzdálenosti $x - p$**: když se k $p$ přiblížíš 10×, chyba se zmenší víc než 10×. Kalkulačka tak třeba odhadne $\sqrt{4{,}1} \approx 2 + \frac{1}{4} \cdot 0{,}1 = 2{,}025$ (přesně $2{,}02485\ldots$).

> [!obrazek] Tečna jako aproximace
> ![[ma108-linearni-aproximace.png]]
> *Vlevo modře f(x) = eˣ⁻¹, zeleně její tečna T₁(f, 1)(x) = x v červeném bodě, červená úsečka je chyba v x = 1,9. Vpravo červeně chyba jako funkce vzdálenosti x − p, šedě čárkovaně samotné x − p a oranžově podíl chyba / (x − p), který jde v nule k 0.*

> [!navic] Co bude dál · handout 4A, slajdy 15–22
> Taylorův polynom $T_n(f, p)$ vylepšuje lineární aproximaci o další členy $\frac{f^{(k)}(p)}{k!}(x - p)^k$, aby chyba byla zanedbatelná i vůči $(x - p)^n$. Základní věta o Taylorově polynomu, odhad chyby a příklady ($\sin$, $e^x$, $\ln(1 + x)$) následují v další přednášce.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč je funkce, která má první derivaci na $[a; b]$, spojitá na $[a; b]$?
> **Derivace ⇒ spojitost** platí i jednostranně: uvnitř z $f'(p)$ plyne spojitost v $p$, z $f'_+(a)$ spojitost zprava v $a$, z $f'_-(b)$ spojitost zleva v $b$. To je přesně spojitost na $[a; b]$.

> [!karta|02]- Dokaž Rolleovu větu (náčrt: dva případy).
> Konstantní $f$: $f' = 0$ všude. Jinak podle **EVT** nabývá $f$ maxima i minima a aspoň jedno leží **uvnitř** $(a; b)$, protože $f(a) = f(b)$ a $f$ někde nabývá jiné hodnoty. V tomto vnitřním extrému je $f'(t) = 0$.

> [!karta|03]- V důkazu Rolleovy věty: proč $f'(t) > 0$ v bodě maxima $t$ vede ke sporu?
> Podle **věty o znaménku limity** je $\frac{f(t + h) - f(t)}{h} > 0$ pro malá $h \neq 0$. Pro $h > 0$ odtud **$f(t + h) > f(t)$**, spor s maximem.

> [!karta|04]- Proč v Rolleově větě nestačí předpokládat spojitost na $[a; b]$?
> Protipříklad **$\lvert x \rvert$ na $[-1; 1]$**: spojitá, $f(-1) = f(1)$, ale derivace je $\pm 1$ všude, kde existuje. V bodě $0$ (vrchol, kde by měla být nula) derivace chybí.

> [!karta|05]- Proč je v důsledku Rolleovy věty $D(a) = D(b) = 0$?
> V $D(a)$ jsou **první a druhý sloupec stejné**, v $D(b)$ **druhý a třetí**. Determinant se dvěma stejnými sloupci je $0$.

> [!karta|06]- Proč je derivace determinantu $D(x)$ determinant s derivacemi ve druhém sloupci?
> Rozvoj podle **druhého sloupce**: $D(x) = -f(x) M_{12} + g(x) M_{22} - h(x) M_{32}$ s **konstantními** minory. Derivace lineární kombinace je lineární kombinace derivací.

> [!karta|07]- Jak z důsledku Rolleovy věty dostaneš Lagrangeovu větu?
> Zvol **$g(x) = x$, $h(x) = 1$**. Pak $0 = D'(t) = f(a) + f'(t)\,b - f(b) - a\,f'(t)$, tedy $f'(t)(b - a) = f(b) - f(a)$.

> [!karta|08]- Jak z důsledku Rolleovy věty dostaneš Cauchyovu větu?
> Zvol **$h(x) = 1$** a rozviň $D'(t)$ podle třetího řádku: $0 = f'(t)\big(g(b) - g(a)\big) - g'(t)\big(f(b) - f(a)\big)$.

> [!karta|09]- V Cauchyově větě: proč z $g' \neq 0$ na $(a; b)$ plyne $g(a) \neq g(b)$?
> Kdyby $g(a) = g(b)$, dala by **Rolleova věta** pro $g$ bod $s \in (a; b)$ s $g'(s) = 0$, spor.

> [!karta|10]- Proč Cauchyovu větu nedostaneš dvojím použitím Lagrangeovy věty (na $f$ a na $g$)?
> Lagrange dá dva body **$t_1$ pro $f$ a $t_2$ pro $g$**, obecně různé. Cauchy zaručí **jeden společný** $t$, což l'Hospitalovo pravidlo potřebuje.

> [!karta|11]- Dokaž: $f' = 0$ na $[a; b]$ ⇒ $f$ je na $[a; b]$ konstantní.
> Pro $x \in (a; b]$ dá **Lagrange na $[a; x]$** bod $t$ s $f(x) - f(a) = f'(t)(x - a) = 0$. Tedy $f(x) = f(a)$.

> [!karta|12]- Co plyne z l'Hospitalova pravidla, když $\lim \frac{f'}{g'}$ neexistuje? Uveď příklad.
> **Nic**, pravidlo je implikace. Např. $\lim_{x \to +\infty} \frac{x + \cos x}{x} = 1$, ale $\lim \frac{1 - \sin x}{1}$ neexistuje.

> [!karta|13]- Co se pokazí, když l'Hospitala použiješ na limitu, která není typu $\frac{0}{0}$ ani $\frac{?}{\lvert \pm\infty \rvert}$?
> Výsledek **může být špatně**: $\lim_{x \to 3} \frac{x^2}{x - 1} = \frac{9}{2}$, ale $\lim_{x \to 3} \frac{2x}{1} = 6$. Typ je předpoklad věty.

> [!karta|14]- Jak převedeš limitu typu $0 \cdot \infty$ a typu $1^{\infty}$ na tvar pro l'Hospitala?
> Součin $f \cdot g$ **přepiš jako $\frac{f}{1/g}$** (typ $\frac{0}{0}$ nebo $\frac{\infty}{\infty}$). Mocninu $u^v$ **přepiš jako $e^{v \ln u}$** a l'Hospitalem počítej limitu exponentu; díky spojitosti $e^x$ je $\lim e^{(\ldots)} = e^{\lim(\ldots)}$.

> [!karta|15]- Proč při řetězení l'Hospitalova pravidla nelze psát „$=$“ dopředu?
> Každý krok je **implikace odzadu**: rovnost $\lim \frac{f}{g} = \lim \frac{f'}{g'}$ platí, až když pravá limita existuje. Teprve existence poslední limity zpětně potvrdí všechny předchozí.

> [!karta|16]- Dokaž přímo z definice derivace, že $\lim_{x \to p} \frac{f(x) - T_1(f, p)(x)}{x - p} = 0$.
> $\frac{f(x) - f(p) - f'(p)(x - p)}{x - p} = \frac{f(x) - f(p)}{x - p} - f'(p) \to$ **$f'(p) - f'(p) = 0$**.

### Příklady na procvičení

> [!priklad|17]- Najdi bod $t$ z Rolleovy věty pro $f(x) = x^2 - 2x$ na $[0; 2]$.
> $f(0) = f(2) = 0$, $f'(x) = 2x - 2 = 0$, tedy **$t = 1$**.

> [!priklad|18]- Najdi bod $t$ z Lagrangeovy věty pro $f(x) = x^3$ na $[0; 3]$.
> $\frac{27 - 0}{3} = 9 = 3t^2$, tedy $t^2 = 3$ a **$t = \sqrt{3} \approx 1{,}732 \in (0; 3)$**.

> [!priklad|19]- Najdi bod $t$ z Cauchyovy věty pro $f(x) = x^3$, $g(x) = x^2$ na $[0; 1]$.
> $(1 - 0) \cdot 2t = (1 - 0) \cdot 3t^2$, tedy $t(3t - 2) = 0$ a v $(0; 1)$ je **$t = \frac{2}{3}$**.

> [!priklad|20]- Spočítej $\lim_{x \to 0^+} x^2 \ln x$.
> Typ $0 \cdot (-\infty)$: $\frac{\ln x}{x^{-2}}$, podíl derivací $\frac{1/x}{-2x^{-3}} = -\frac{x^2}{2} \to 0$. **Výsledek $0$.**

> [!priklad|21]- Spočítej $\lim_{x \to 1} x^{\frac{1}{x - 1}}$.
> $= e^{\lim \frac{\ln x}{x - 1}}$ a $\lim_{x \to 1} \frac{\ln x}{x - 1} = \lim \frac{1/x}{1} = 1$. **Výsledek $e$.**

> [!priklad|22]- Spočítej $\lim_{x \to +\infty} \frac{x^3 - 2x + 1}{e^{3x}}$.
> Třikrát l'Hospital: $\frac{3x^2 - 2}{3e^{3x}}$, $\frac{6x}{9e^{3x}}$, $\frac{6}{27e^{3x}} \to 0$. **Výsledek $0$.**

> [!priklad|23]- Spočítej $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$.
> Typ $\frac{0}{0}$: $\frac{\sin x}{2x}$, znovu $\frac{0}{0}$: $\frac{\cos x}{2} \to \frac{1}{2}$. **Výsledek $\frac{1}{2}$.**

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 1. semestrálnímu testu (J. Velebil, 9.–13. 11. 2026). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|24]- Dokažte nebo vyvraťte: Jestliže $f$ a $g$ mají derivaci na $(-1; 0) \cup (0; 1)$, $\lim_{x \to 0} f = \lim_{x \to 0} g = 0$ a $\lim_{x \to 0} \frac{f(x)}{g(x)}$ existuje, potom existuje i $\lim_{x \to 0} \frac{f'(x)}{g'(x)}$.
> **Neplatí.** Protipříklad $f(x) = x^2 \sin\frac{1}{x}$, $g(x) = x$. Obě mají derivaci pro $x \neq 0$ a jdou k $0$. $\frac{f(x)}{g(x)} = x \sin\frac{1}{x} \to 0$, protože jde o součin funkce s limitou $0$ a omezené funkce. Ale $\frac{f'(x)}{g'(x)} = 2x \sin\frac{1}{x} - \cos\frac{1}{x}$ limitu nemá: první člen jde k $0$ a pro $x_n = \frac{1}{2n\pi} \to 0$ je $\cos\frac{1}{x_n} = 1$, pro $y_n = \frac{1}{(2n + 1)\pi} \to 0$ je $\cos\frac{1}{y_n} = -1$, takže podle Heineovy věty dostaneme limity $-1$ a $1$. **Tvrzení je vyvráceno.**

> [!priklad|25]- Dokažte nebo vyvraťte: Jestliže $f$ má první derivaci na $[0; 1]$ a $f'(x) \neq 0$ pro všechna $x \in (0; 1)$, potom $f(0) \neq f(1)$.
> **Platí.** Sporem: ať $f(0) = f(1)$. Funkce $f$ má první derivaci na $[0; 1]$, takže podle Rolleovy věty existuje $t \in (0; 1)$ s $f'(t) = 0$, což je spor s předpokladem $f' \neq 0$ na $(0; 1)$. **Tedy $f(0) \neq f(1)$.**

> [!priklad|26]- Definujte pojem: funkce $f$ má první derivaci na intervalu $[2; 5]$. (Přesný zápis pomocí limit, se všemi předpoklady, českými větami.)
> Funkce $f$ má první derivaci na intervalu $[2; 5]$, jestliže je splněno: pro každý bod $p \in (2; 5)$ existuje **vlastní** limita $\lim_{h \to 0} \frac{f(p + h) - f(p)}{h}$; v bodě $2$ existuje vlastní limita $\lim_{h \to 0^+} \frac{f(2 + h) - f(2)}{h}$ (derivace zprava); v bodě $5$ existuje vlastní limita $\lim_{h \to 0^-} \frac{f(5 + h) - f(5)}{h}$ (derivace zleva). (Implicitně: $f$ je definovaná na $[2; 5]$.)

> [!priklad|27]- Spočtěte $\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$.
> Typ $\frac{0}{0}$, čitatel i jmenovatel mají derivaci a $(x^2)' = 2x \neq 0$ pro $x \neq 0$. Podíl derivací $\frac{e^x - 1}{2x}$ je znovu typ $\frac{0}{0}$ a další podíl derivací je $\frac{e^x}{2} \to \frac{1}{2}$. Protože poslední limita existuje, dává l'Hospitalovo pravidlo dvakrát zpětně **$\lim_{x \to 0} \frac{e^x - 1 - x}{x^2} = \frac{1}{2}$**.

> [!priklad|28]- Spočtěte $\lim_{x \to +\infty} x \left(e^{1/x} - 1\right)$.
> Typ $(+\infty) \cdot 0$; přepiš jako $\frac{e^{1/x} - 1}{1/x}$, typ $\frac{0}{0}$. Podíl derivací: $\frac{e^{1/x} \cdot \left(-\frac{1}{x^2}\right)}{-\frac{1}{x^2}} = e^{1/x} \to e^0 = 1$ (spojitost $e^x$). Podle l'Hospitalova pravidla **je limita rovna $1$**.

---
← [[MA1 07 – Derivace a Carathéodoryho trik|14. 10. 2026 Derivace a Carathéodoryho trik]]

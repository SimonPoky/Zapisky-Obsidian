---
predmet: MA1
prednaska: 9
datum: 2026-10-21
zdroj: "Handout 4A (Složitější věty o derivacích), slajdy 16–22; handout 4B (Derivace, monotonie a extrémy), slajdy 3–10"
tags: [prednaska, MA1]
---

# MA1 09 – Taylorův polynom, extrémy a monotonie

*Přednáška 9 · středa 21. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 4A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout04a.pdf) · [Handout 4B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout04b.pdf)

Témata: `derivace vyššího řádu` · `Taylorův polynom` · `základní věta o Taylorově polynomu` · `Taylorův polynom eˣ` · `odhad chyby` · `lokální extrémy` · `stacionární bod` · `f′(p) = 0 v extrému` · `největší a nejmenší hodnota na [a; b]` · `monotonie a znaménko f′` · `x³ je rostoucí`

Minule skončila přednáška u tečny jako nejlepší lineární aproximace funkce. Dnes ji vylepšíme na Taylorův polynom: polynom stupně $\le n$, který kopíruje funkci v bodě $p$ i s prvními $n$ derivacemi a jehož chyba mizí rychleji než $(x - p)^n$. Druhá půlka přednášky (handout 4B) ukazuje, co derivace říká o tvaru grafu: kde může mít funkce lokální extrém, jak najít největší a nejmenší hodnotu na $[a; b]$ a jak znaménko $f'$ určuje, jestli funkce roste nebo klesá.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| Taylorův polynom | $f^{(n)}(p)$ existuje | $T_n(f, p)(x) = \sum_{k=0}^{n} \frac{f^{(k)}(p)}{k!}(x - p)^k$ |
| základní věta o Taylorově polynomu | $f^{(n)}(p)$ existuje | $\lim_{x \to p} \frac{f(x) - T_n(f, p)(x)}{(x - p)^n} = 0$ a $T_n^{(k)}(p) = f^{(k)}(p)$ pro $0 \le k \le n$ |
| exponenciála | | $T_n(e^x, 0)(x) = \sum_{k=0}^{n} \frac{x^k}{k!}$ (zapamatovat) |
| odhad chyby | $f^{(n+1)}$ na otevřeném intervalu s $p$ | $f(x) - T_n(f, p)(x) = \frac{f^{(n+1)}(t)}{(n + 1)!}(x - p)^{n+1}$, $t$ mezi $x$ a $p$ |
| lokální minimum v $p$ | | $f(p) \le f(x)$ pro všechna $x$ z nějakého okolí $p$ (ostré: $<$ pro $x \neq p$) |
| nutná podmínka extrému | lokální extrém v $p$, $f'(p)$ existuje | $f'(p) = 0$ ($p$ je stacionární bod); obráceně neplatí ($x^3$) |
| největší a nejmenší hodnota | $f$ spojitá na $[a; b]$, $f'$ uvnitř | $x_{\min}$, $x_{\max}$ jsou krajní body nebo stacionární body uvnitř |
| monotonie | $I$ otevřený interval, $f'$ na $I$ | neklesající $\iff f' \ge 0$; rostoucí $\iff f' \ge 0$ a $f'$ není nulová na žádném podintervalu |

## §1 Taylorův polynom

### Derivace vyšších řádů

> [!definice] Derivace vyššího řádu · handout 3B, slajd 19
> Má-li $f$ derivaci $f'(x)$ v každém bodě nějakého intervalu, můžeme zkusit derivovat funkci $f'$. Výsledná funkce $f'' = (f')'$ je **druhá derivace** $f$, obecně $f^{(k)} = \big(f^{(k-1)}\big)'$ je **$k$-tá derivace**, s konvencí $f^{(0)} = f$ (takže $f^{(1)} = f'$, $f^{(2)} = f''$).
>
> Funkce **má alespoň $n$ derivací v bodě $p$**, když existuje (vlastní) $f^{(n)}(p)$. K tomu musí $f^{(n-1)}$ existovat na nějakém okolí $p$, jinak by se v $p$ nedala derivovat.

^def-vyssi-derivace

> [!lidsky] Lidsky
> [[derivace vyššího řádu|Druhá derivace]] je „rychlost změny rychlosti“, tedy zrychlení: když $f(t)$ je poloha auta, $f'(t)$ je rychlost a $f''(t)$ zrychlení. Třetí derivace popisuje, jak rychle se mění zrychlení (cukání při rozjezdu). Pro $f(x) = x^3$ je $f' = 3x^2$, $f'' = 6x$, $f''' = 6$ a všechny další derivace jsou $0$.

### Definice Taylorova polynomu

Cíl (handout 4A, slajd 15): najít polynom $T_n(f, p)$ stupně nejvýš $n$, který pro $x$ blízko $p$ „velmi dobře“ aproximuje $f(x)$, lépe než [[lineární aproximace]] $T_1(f, p)(x) = f(p) + f'(p)(x - p)$.

> [!definice] Taylorův polynom · handout 4A, slajd 16
> Ať $f$ má alespoň $n$ derivací v bodě $p$. **Taylorův polynom stupně $\le n$ funkce $f$ se středem v bodě $p$** je polynomiální funkce $x \mapsto T_n(f, p)(x)$, kde
>
> $$
> T_n(f, p)(x) = \sum_{k=0}^{n} \frac{f^{(k)}(p)}{k!}(x - p)^k = \frac{f(p)}{0!} + \frac{f'(p)}{1!}(x - p) + \frac{f''(p)}{2!}(x - p)^2 + \dots + \frac{f^{(n)}(p)}{n!}(x - p)^n.
> $$
>
> $T_n(f, p)$ je polynom (závisí na $n$, $f$ a $p$), $T_n(f, p)(x)$ je jeho hodnota v bodě $x$.

^def-taylor

> [!lidsky] Lidsky
> [[Taylorův polynom]] je „padělek“ funkce v okolí bodu $p$: polynom, který má v $p$ stejnou hodnotu, stejný sklon, stejné zakřivení… až po $n$-tou derivaci. Každý další člen opraví další „vrstvu“ chování. Faktoriál $k!$ ve jmenovateli je tam proto, že $k$-tá derivace $(x - p)^k$ je $k!$; vydělením se v $p$ trefíme přesně do $f^{(k)}(p)$.

> [!example] Případ $n = 2$
> Má-li $f$ v $p$ derivace $f^{(0)}(p) = f(p)$, $f^{(1)}(p) = f'(p)$ a $f^{(2)}(p) = f''(p)$, je
>
> $$
> T_2(f, p)(x) = \frac{f(p)}{0!}(x - p)^0 + \frac{f'(p)}{1!}(x - p)^1 + \frac{f''(p)}{2!}(x - p)^2 = f(p) + f'(p)(x - p) + \frac{f''(p)}{2}(x - p)^2.
> $$
>
> Je to tečna plus parabolická oprava, která zachytí zakřivení grafu.

> [!pozor] Stupeň, ne „řád“
> Velebil píše „Taylorův polynom **stupně $\le n$**“. Stupeň může vyjít menší než $n$, když $f^{(n)}(p) = 0$: pro $\sin$ v bodě $0$ je $T_2(\sin, 0) = T_1(\sin, 0) = x$.

## §2 Základní věta o Taylorově polynomu

> [!veta] Základní věta o Taylorově polynomu · handout 4A, slajd 17
> ==Ať $f$ má alespoň $n$ derivací v bodě $p$.== Potom platí:
>
> 1. $\displaystyle\lim_{x \to p} \frac{f(x) - T_n(f, p)(x)}{(x - p)^n} = 0$. **Čitatel $f(x) - T_n(f, p)(x)$ je chyba aproximace a ta jde k nule rychleji než $(x - p)^n$.**
> 2. **$\big(T_n(f, p)\big)^{(k)}(p) = f^{(k)}(p)$ pro všechna $0 \le k \le n$.**
>
> Navíc je $T_n(f, p)$ **jediná** polynomiální funkce stupně $\le n$ s těmito vlastnostmi.
>
> > [!note]- Důkaz (1) pro $n = 2$
> > Z předpokladu existuje $f''(p)$, takže $f'$ existuje na nějakém okolí $p$. Limita
> >
> > $$
> > \lim_{x \to p} \frac{f(x) - T_2(f, p)(x)}{(x - p)^2} = \lim_{x \to p} \frac{f(x) - f(p) - f'(p)(x - p) - \frac{f''(p)}{2}(x - p)^2}{(x - p)^2}
> > $$
> >
> > je typu $\frac{0}{0}$. Podíl derivací (derivuje se podle $x$; $f(p)$, $f'(p)$, $f''(p)$ jsou konstanty):
> >
> > $$
> > \lim_{x \to p} \frac{f'(x) - f'(p) - 2 \cdot \frac{f''(p)}{2}(x - p)}{2(x - p)} = \frac{1}{2} \lim_{x \to p} \left( \frac{f'(x) - f'(p)}{x - p} - f''(p) \right) = \frac{1}{2}\big(f''(p) - f''(p)\big) = 0.
> > $$
> >
> > Prostřední rovnost je **definice** $f''(p)$ jako derivace funkce $f'$ v bodě $p$. Protože limita podílu derivací existuje, dává [[l'Hospitalovo pravidlo]] i původní limitu $0$.
>
> > [!note]- Důkaz (2)
> > Derivuj člen $\frac{f^{(j)}(p)}{j!}(x - p)^j$ celkem $k$-krát. Pro $j < k$ vyjde $0$; pro $j > k$ zůstane mocnina $(x - p)^{j-k}$ s kladným exponentem, která je v $p$ nulová; pro $j = k$ vyjde $\frac{f^{(k)}(p)}{k!} \cdot k! = f^{(k)}(p)$. Součet v bodě $p$ je tedy $f^{(k)}(p)$.

^veta-taylor

> [!lidsky] Lidsky
> [[základní věta o Taylorově polynomu]]: (1) říká, že chyba je zanedbatelná i vůči $(x - p)^n$. Pro $n = 2$: když se přiblížíš k $p$ desetkrát, $(x - p)^2$ se zmenší stokrát a chyba ještě víc. (2) říká, že polynom má v $p$ stejné „chování“, o kterém rozhodují derivace do řádu $n$: monotonii, zakřivení, extrémy (handout 4B). Jedinost znamená, že kdo najde polynom s vlastností (1), našel Taylorův polynom, ať už ho počítal jakkoli.

> [!pozor] Proč l'Hospital jen jednou
> Po prvním kroku zbude $\frac{f'(x) - f'(p) - f''(p)(x - p)}{2(x - p)}$, zase typu $\frac{0}{0}$. Druhý l'Hospital by vedl na $\lim_{x \to p} \frac{f''(x) - f''(p)}{2}$, a to potřebuje $f''$ **na okolí** $p$ a **spojitou** v $p$. Věta ale předpokládá jen existenci $f''(p)$ v jediném bodě. Proto se druhý krok dělá přímo z definice $f''(p)$.

> [!obrazek] Chyba Taylorovy aproximace
> ![[ma109-chyba.png]]
> *Vlevo červeně chyba $e^x - T_2(e^x, 0)(x)$, šedě čárkovaně $x^2$: chyba je u nuly mnohem plošší. Vpravo oranžově podíl chyba / $x^2$, který jde v nule k zelené hodnotě 0, přesně jak říká věta (1).*

> [!navic] Každý polynom je svůj vlastní Taylorův polynom · handout 4A, slajd 21
> Pro $f(x) = \sum_{k=0}^{n} a_k x^k$ je $f^{(k)}(0) = k! \cdot a_k$, takže $T_n(f, 0) = f$. Taylorův polynom stupně $\le n$ polynomu stupně $n$ je původní polynom. Plyne to i z jedinosti: $f$ sám splňuje (1), protože jeho chyba je nulová.

## §3 Taylorův polynom exponenciály

> [!veta] Taylorův polynom exponenciály · handout 4A, slajd 20
> Pro $f(x) = e^x$ je $f^{(k)}(x) = e^x$ pro každé $k$, takže
>
> $$
> T_n(e^x, p)(x) = \sum_{k=0}^{n} \frac{e^p}{k!}(x - p)^k, \qquad \textbf{speciálně}\quad T_n(e^x, 0)(x) = \sum_{k=0}^{n} \frac{1}{k!}x^k = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \dots + \frac{x^n}{n!}.
> $$
>
> Tento polynom je doporučeno si **zapamatovat**.

^veta-taylor-exp

> [!lidsky] Lidsky
> [[Taylorův polynom exponenciály]] je nejjednodušší ze všech: každá derivace $e^x$ je zase $e^x$ a $e^0 = 1$, takže zbudou jen faktoriály. Dosazením $x = 1$ dostaneš $e \approx 1 + 1 + \frac{1}{2} + \frac{1}{6} = 2{,}667$; s více členy se to rychle blíží k $e = 2{,}71828\ldots$

> [!navic] Další Taylorovy polynomy · handout 4A, slajdy 18–20
> - $\sin$ v bodě $0$: derivace v $0$ jsou postupně $0, 1, 0, -1, 0, 1, \ldots$, takže $T_3(\sin, 0)(x) = x - \frac{x^3}{6}$ a $T_5(\sin, 0)(x) = x - \frac{x^3}{6} + \frac{x^5}{120}$.
> - $\sin$ v bodě $1$: $T_3(\sin, 1)(x) = \sin 1 + \cos 1 \cdot (x - 1) - \frac{\sin 1}{2}(x - 1)^2 - \frac{\cos 1}{6}(x - 1)^3$.
> - $\ln(1 + x)$ v bodě $0$: $T_n(f, 0)(x) = \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k} x^k = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$
>
> Tyhle si pamatovat **není nutné**, stačí je umět spočítat z definice.

> [!obrazek] Taylorovy polynomy $e^x$ a $\sin x$
> ![[ma109-taylor.png]]
> *Vlevo modře $e^x$, oranžově tečna $T_1$, zeleně $T_2$, červeně čárkovaně $T_3$. Vpravo modře $\sin x$, oranžově $T_1 = T_2 = x$, zeleně $T_3$, červeně čárkovaně $T_5$. Čím vyšší stupeň, tím delší úsek kolem středu (černý bod) polynom věrně kopíruje; daleko od středu se ale všechny rozjedou.*

## §4 Odhad chyby

> [!navic] Připomenutí: Lagrangeova věta · handout 4A, slajd 6
> Má-li $f$ první derivaci na $[a; b]$, existuje $t \in (a; b)$ s $\frac{f(b) - f(a)}{b - a} = f'(t)$ ([[Lagrangeova věta]], přednáška 8). Stačí i slabší předpoklad: $f$ je **spojitá na $[a; b]$** a má derivaci v každém bodě $(a; b)$.

> [!pozor] Častá chyba: „$f(a)$, $f(b)$ jsou definované“ nestačí
> Pro Lagrangeovu větu nestačí derivace na $(a; b)$ a pouhá existence hodnot $f(a)$, $f(b)$; potřeba je spojitost v krajních bodech. Protipříklad: $f(x) = x$ na $(0; 1]$ a $f(0) = 1$. Uvnitř je $f' = 1$, ale $\frac{f(1) - f(0)}{1 - 0} = 0$, takže bod $t$ neexistuje.

> [!veta] Odhad chyby při Taylorově aproximaci · handout 4A, slajd 22
> ==Ať $f$ má $n + 1$ derivací na otevřeném intervalu $(a; b)$ a ať $p \in (a; b)$.== Potom **pro každé $x \in (a; b)$ existuje $t$ mezi $x$ a $p$ takové, že**
>
> $$
> \underbrace{f(x) - T_n(f, p)(x)}_{\text{chyba aproximace}} = \frac{f^{(n+1)}(t)}{(n + 1)!}(x - p)^{n+1}.
> $$
>
> Důkaz se zde neuvádí (je mírně technický, používá Lagrangeovu větu).

^veta-odhad-chyby

> [!lidsky] Lidsky
> [[věta o odhadu chyby Taylorova polynomu|Odhad chyby]]: chyba vypadá skoro jako další, $(n + 1)$-ní člen Taylorova polynomu, jen se derivace nepočítá v $p$, ale v neznámém bodě $t$ mezi $x$ a $p$. Bod $t$ neznáme, ale stačí umět omezit $\lvert f^{(n+1)} \rvert$ na úseku mezi $x$ a $p$ a dostaneme zaručenou horní mez chyby. Pro $n = 0$ je to přesně Lagrangeova věta: $f(x) - f(p) = f'(t)(x - p)$.

> [!example] Jak přesně je $e \approx 2{,}667$?
> 1. $T_3(e^x, 0)(1) = 1 + 1 + \frac{1}{2} + \frac{1}{6} = \frac{8}{3} \approx 2{,}667$.
> 2. Odhad chyby s $n = 3$, $p = 0$, $x = 1$: $e - \frac{8}{3} = \frac{e^t}{4!} \cdot 1^4$ pro nějaké $t \in (0; 1)$.
> 3. Protože $e^t < e^1 < 3$, je chyba **menší než $\frac{3}{24} = 0{,}125$**. Skutečná chyba je $0{,}0516$.

## §5 Lokální extrémy

> [!definice] Lokální minimum a maximum · handout 4B, slajd 3
> Ať $f$ je definována v bodě $p$ a ve [[směr|směru]] $x \to p$. Řekneme, že
>
> 1. $f$ má **lokální minimum** v $p$, pokud $f(p) \le f$ ve směru $x \to p$,
> 2. $f$ má **ostré lokální minimum** v $p$, pokud $f(p) < f$ ve směru $x \to p$,
> 3. $f$ má **lokální maximum** v $p$, pokud $f \le f(p)$ ve směru $x \to p$,
> 4. $f$ má **ostré lokální maximum** v $p$, pokud $f < f(p)$ ve směru $x \to p$.
>
> Nerovnost ve směru $x \to p$ ([[nerovnost ve směru]]) znamená: existuje $\delta > 0$ tak, že nerovnost platí pro všechna $x \in (p - \delta; p + \delta)$, $x \neq p$. **Lokální extrém** = lokální minimum nebo lokální maximum, **ostrý lokální extrém** = ostré lokální minimum nebo ostré lokální maximum.

^def-lokalni-extrem

> [!lidsky] Lidsky
> [[lokální minimum]] je dno důlku: dost blízko $p$ není nic níž než $f(p)$, i když jinde může graf klesnout mnohem hlouběji. [[ostrý lokální extrém|Ostré minimum]] je špička dna, kolem které je všechno **přísně** výš; neostré minimum může ležet na rovném úseku, kde je kolem stejná hodnota. [[lokální maximum]] je vrchol kopce, [[lokální extrém]] je společné jméno pro obojí. Šetření práce: $f$ má v $p$ (ostré) lokální maximum, právě když $-f$ má v $p$ (ostré) lokální minimum.

> [!obrazek] Lokální minimum a ostré lokální minimum
> ![[ma109-lokalni-minimum.png]]
> *Vlevo: na zeleném okolí (p − δ; p + δ) je graf rovný, f(p) je nejmenší hodnota, ale ne přísně, takže jde o lokální minimum, které není ostré. Vpravo: kolem červeného bodu p je všechno přísně výš, ostré lokální minimum (derivace v p navíc neexistuje).*

> [!definice] Stacionární bod · handout 4B, slajd 4
> Bod $p$ je **stacionární bod** funkce $f$, právě když $f'(p) = 0$.

^def-stacionarni-bod

> [!lidsky] Lidsky
> [[stacionární bod]] je místo, kde je tečna vodorovná: funkce se tam na okamžik „zastaví“ (auto s nulovou rychlostí). Může to být vrchol, dno, ale i jen zastavení na schodu, po kterém funkce pokračuje stejným směrem.

> [!veta] Nutná podmínka lokálního extrému · handout 4B, slajd 4
> ==Ať $f$ má v bodě $p$ lokální extrém a ať $f'(p)$ existuje.== Potom **$f'(p) = 0$**, tedy $p$ je stacionární bod.
>
> > [!note]- Důkaz (pro lokální minimum, maximum analogicky)
> > Sporem: ať $f'(p) > 0$. Protože $\lim_{x \to p} \frac{f(x) - f(p)}{x - p} = f'(p) > 0$, je podle [[věta o znaménku limity|věty o znaménku limity]] $\frac{f(x) - f(p)}{x - p} > 0$ pro všechna $x \neq p$ z nějakého okolí $(p - \delta; p + \delta)$; zmenšením $\delta$ zařídíme, že na něm platí i $f(p) \le f(x)$ (lokální minimum). Vezmi $x \in (p - \delta; p)$. Pak $x - p < 0$, takže čitatel musí být záporný:
> >
> > $$
> > f(x) - f(p) < 0 \iff f(p) > f(x),
> > $$
> >
> > spor s $f(p) \le f(x)$. Pro $f'(p) < 0$ dá spor bod $x \in (p; p + \delta)$: podíl je záporný a $x - p > 0$, takže opět $f(x) < f(p)$. Zbývá $f'(p) = 0$.

^veta-nutna-podminka

> [!lidsky] Lidsky
> [[nutná podmínka lokálního extrému]]: na vrcholu ani na dně nemůže tečna stoupat ani klesat. Kdyby v bodě minima stoupala ($f'(p) > 0$), stačilo by udělat malý krok **doleva** a byl bys níž než v „minimu“. Stejný argument jsme viděli v důkazu Rolleovy věty.

> [!obrazek] Proč v minimu nemůže být $f'(p) > 0$
> ![[ma109-nutna-podminka.png]]
> *Modrá funkce má v červeném bodě p kladnou derivaci. Na zeleném okolí mají všechny sečny z p kladnou směrnici, takže oranžový bod x vlevo od p leží níž než p. Bod p tedy nemůže být lokální minimum.*

### Příklady a protipříklady · handout 4B, slajd 5

> [!example] Stacionární bod, který je extrémem
> $f(x) = (x - 5)^2 + 7$, $x \in \mathbb{R}$. Pak $f'(x) = 2(x - 5)$ a $f'(5) = 0$, takže **$5$ je stacionární bod**. To samo o sobě extrém nezaručuje; tady ho ale vidíme přímo: $(x - 5)^2 \ge 0$, tedy $f(x) \ge 7 = f(5)$ pro všechna $x$. **$f$ má v bodě $5$ (ostré) minimum.**

> [!example] Extrém bez stacionárního bodu
> $f(x) = -\lvert x + 7 \rvert$, $x \in \mathbb{R}$. $f(x) \le 0 = f(-7)$, takže $f$ má v $-7$ **lokální maximum**. Ale **$-7$ není stacionární bod**, protože $f'(-7)$ neexistuje (zleva je směrnice $1$, zprava $-1$). Věta nic neporušuje: předpokládá, že $f'(p)$ existuje.

> [!example] Stacionární bod, který extrémem není
> $f(x) = x^3 - 1$, $x \in \mathbb{R}$. $f'(x) = 3x^2$, takže $f'(0) = 0$ a **$0$ je stacionární bod**. Ale $f(x) < -1 = f(0)$ pro $x < 0$ a $f(x) > f(0)$ pro $x > 0$, takže **$f$ nemá v $0$ ani lokální minimum, ani maximum**.

> [!obrazek] Tři případy
> ![[ma109-stacionarni.png]]
> *Vlevo parabola se zelenou vodorovnou tečnou v minimu. Uprostřed špička −|x + 7|: maximum v červeném bodě, ale tečna tam neexistuje. Vpravo x³ − 1: zelená tečna v 0 je vodorovná, graf ale přes ni prochází nahoru, extrém tam není.*

> [!pozor] Implikace, ne ekvivalence
> Věta říká **extrém + derivace existuje ⇒ $f'(p) = 0$**. Obrácená implikace neplatí ($x^3 - 1$ v bodě $0$). Kandidáti na extrém jsou proto dvojího druhu: stacionární body **a** body, kde derivace neexistuje; každého kandidáta je potřeba ještě ověřit.

## §6 Největší a nejmenší hodnota na $[a; b]$

> [!veta] Věta o největší a nejmenší hodnotě · handout 4B, slajd 8
> ==Ať $f$ je spojitá na $[a; b]$ a má derivaci ve vnitřních bodech $(a; b)$.== Potom:
>
> 1. **V $[a; b]$ existují body $x_{\min}$ a $x_{\max}$ takové, že $f(x_{\min})$ je na $[a; b]$ nejmenší a $f(x_{\max})$ největší hodnota.**
> 2. **Každý z bodů $x_{\min}$, $x_{\max}$ je buď krajní bod $[a; b]$, nebo vnitřní bod $[a; b]$, který je stacionárním bodem $f$.**
>
> > [!note]- Důkaz
> > (1) je [[věta o extrémech]] (EVT) z přednášky 6. (2): ať $x_{\max} \in (a; b)$. Největší hodnota na celém $[a; b]$ je tím spíš největší na malém okolí $x_{\max}$, takže $f$ má v $x_{\max}$ lokální maximum. Derivace v $x_{\max}$ existuje (je to vnitřní bod), takže podle nutné podmínky lokálního extrému $f'(x_{\max}) = 0$. Pro $x_{\min}$ stejně.

^veta-nejvetsi-hodnota

> [!lidsky] Lidsky
> [[věta o největší a nejmenší hodnotě]] dává hotový recept: nemusíš zkoumat nekonečně mnoho bodů intervalu, stačí porovnat hodnoty v krajních bodech a ve stacionárních bodech uvnitř. Nejvyšší z nich je maximum, nejnižší minimum. Nové oproti EVT je právě (2): **kde** extrém hledat.

> [!example] $f(x) = 4x^4 + 16x^3 - 80x^2 + 12$ na $[0; 3]$ · handout 4B, slajd 9
> 1. Hodnoty v krajních bodech: $f(0) = 12$, $f(3) = 324 + 432 - 720 + 12 = 48$.
> 2. Stacionární body uvnitř $(0; 3)$: $f'(x) = 16x^3 + 48x^2 - 160x = 16x(x + 5)(x - 2)$. Nuly jsou $0$, $-5$ a $2$, uvnitř $(0; 3)$ leží **jen $2$**. $f(2) = 64 + 128 - 320 + 12 = -116$.
> 3. Porovnání $12$, $48$, $-116$: **$x_{\min} = 2$ s hodnotou $-116$, $x_{\max} = 3$ s hodnotou $48$.**

> [!obrazek] Největší a nejmenší hodnota na $[0; 3]$
> ![[ma109-nejvetsi-hodnota.png]]
> *Modře f na [0; 3], šedě čárkovaně mimo interval. Oranžově krajní bod 0, červeně krajní bod 3 s největší hodnotou 48, zeleně jediný stacionární bod uvnitř, 2, s nejmenší hodnotou −116.*

> [!pozor] Krajní body se nesmí vynechat
> Maximum zde leží v krajním bodě $3$, kde $f'(3) = 432 + 432 - 480 = 384 \neq 0$. Kdo porovná jen stacionární body, maximum mine. Bod $0$ je sice nulou $f'$, ale jako krajní bod se bere ve skupině krajních bodů.

## §7 Monotonie a znaménko derivace

> [!definice] Monotonie na intervalu · handout 4B, slajd 6 (připomenutí)
> Ať $f$ je definována na intervalu $I$. Řekneme, že $f$ je na $I$
>
> 1. **neklesající**, pokud pro $x_1, x_2 \in I$ z $x_1 < x_2$ plyne $f(x_1) \le f(x_2)$,
> 2. **rostoucí**, pokud pro $x_1, x_2 \in I$ z $x_1 < x_2$ plyne $f(x_1) < f(x_2)$,
> 3. **nerostoucí**, pokud pro $x_1, x_2 \in I$ z $x_1 < x_2$ plyne $f(x_1) \ge f(x_2)$,
> 4. **klesající**, pokud pro $x_1, x_2 \in I$ z $x_1 < x_2$ plyne $f(x_1) > f(x_2)$.
>
> **Monotónní** = neklesající nebo nerostoucí, **ryze monotónní** = rostoucí nebo klesající.

^def-monotonie

> [!lidsky] Lidsky
> [[neklesající funkce]] je schodiště nahoru, na kterém smíš i stát na místě (rovné úseky povolené). [[ryze monotónní funkce|Rostoucí]] je výtah jen nahoru, bez zastavení. Šetření práce: $f$ je neklesající/rostoucí na $I$, právě když $-f$ je nerostoucí/klesající.

> [!veta] Znaménko derivace a monotonie · handout 4B, slajd 10
> ==Ať $I$ je **otevřený** interval a $f$ má derivaci na $I$.==
>
> 1. **$f$ je neklesající na $I$, právě když $f' \ge 0$ na $I$.**
> 2. **$f$ je rostoucí na $I$, právě když $f' \ge 0$ na $I$ a navíc v každém podintervalu $(x_1; x_2) \subseteq I$ existuje bod $p$ s $f'(p) > 0$.**
> 3. **Má-li $f$ lokální extrém v nějakém bodě $I$, je to stacionární bod $f$.**
>
> Přechodem k $-f$ dostaneme stejnou charakterizaci nerostoucích a klesajících funkcí.
>
> > [!note]- Důkaz (1) „⇒“
> > Sporem: ať $f$ je neklesající na $I$ a existuje $p \in I$ s $f'(p) < 0$. Pak $\frac{f(x) - f(p)}{x - p} < 0$ pro všechna $x \neq p$ z nějakého okolí $(p - \delta; p + \delta) \subseteq I$ (věta o znaménku limity). Pro $x \in (p - \delta; p)$ je $x - p < 0$, tedy $f(x) - f(p) > 0$, čili $f(x) > f(p)$, přestože $x < p$. To je spor s tím, že $f$ je neklesající.
>
> > [!note]- Důkaz (1) „⇐“
> > Sporem: ať $f' \ge 0$ na $I$, ale $f$ není neklesající, tedy existují $x_1 < x_2$ v $I$ s $f(x_1) > f(x_2)$. $f$ má derivaci na $[x_1; x_2] \subseteq I$, takže podle Lagrangeovy věty existuje $t \in (x_1; x_2)$ s
> >
> > $$
> > 0 > \frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(t) \ge 0,
> > $$
> >
> > spor.
>
> > [!note]- Důkaz (2) „⇒“
> > Rostoucí funkce je neklesající, takže podle (1) je $f' \ge 0$ na $I$. Zbývá podmínka o podintervalech. Sporem: ať existuje $(x_1; x_2) \subseteq I$, na kterém $f' \le 0$. Dohromady s $f' \ge 0$ je $f' = 0$ na $(x_1; x_2)$, takže podle (1) pro $f$ i pro $-f$ je $f$ na $(x_1; x_2)$ neklesající i nerostoucí, tedy konstantní. Konstantní funkce není rostoucí, spor.
>
> > [!note]- Důkaz (2) „⇐“
> > Podle (1) je $f$ neklesající. Sporem: ať $f$ není rostoucí, tedy existují $x_1 < x_2$ v $I$ s $f(x_1) \ge f(x_2)$. Pro každé $x \in [x_1; x_2]$ je díky neklesání $f(x_1) \le f(x) \le f(x_2) \le f(x_1)$, takže **$f$ je na $[x_1; x_2]$ konstantní** a $f' = 0$ na $(x_1; x_2)$. To je spor s předpokladem, že v $(x_1; x_2)$ existuje bod $p$ s $f'(p) > 0$.
>
> > [!note]- Důkaz (3)
> > Každý bod otevřeného intervalu je jeho vnitřní bod a $f'$ v něm existuje, takže stačí nutná podmínka lokálního extrému.

^veta-monotonie

> [!lidsky] Lidsky
> [[věta o znaménku derivace a monotonii]]: tachometr nikdy neukazuje couvání ($f' \ge 0$) ⇔ auto nikdy necouvne (neklesající). Aby šlo o „rostoucí“, nesmí auto navíc **stát** po celý nějaký úsek času: jednotlivé okamžiky s nulovou rychlostí nevadí, celý úsek stání ano.

> [!pozor] Častá chyba v důkazu (2) „⇐“
> Lagrangeova věta tady **nestačí přímo**: z $f(x_1) \ge f(x_2)$ dostaneš bod $t$ s $f'(t) \le 0$, ale o tomhle konkrétním $t$ předpoklad nic neříká (zaručuje jen **nějaký** bod s $f' > 0$, ne všechny). Psát „$f'(t) > 0$, spor“ je chyba. Správně: neklesající funkce s $f(x_1) \ge f(x_2)$ je na $[x_1; x_2]$ konstantní, takže $f' = 0$ na celém $(x_1; x_2)$.

> [!example] Poznámka k (2): $f(x) = x^3$ je rostoucí, i když není $f' > 0$
> $f(x) = x^3$ na $I = \mathbb{R}$, $f'(x) = 3x^2 \ge 0$ pro všechna $x \in \mathbb{R}$. **Neplatí** $f' > 0$ na $\mathbb{R}$, protože $f'(0) = 0$. Přesto je $f$ rostoucí:
>
> - podle (2): $f' \ge 0$ a $f'$ je nulová jen v bodě $0$, takže každý podinterval obsahuje bod s $f' > 0$;
> - přímo: pro $x_1 < x_2$ je $x_2^3 - x_1^3 = \underbrace{(x_2 - x_1)}_{> 0}\,(x_1^2 + x_1 x_2 + x_2^2)$ a druhá závorka je $\left(x_1 + \frac{x_2}{2}\right)^2 + \frac{3}{4}x_2^2 > 0$, protože by byla nulová jen pro $x_1 = x_2 = 0$. Tedy $x_1^3 < x_2^3$.

> [!obrazek] Monotonie a derivace
> ![[ma109-monotonie.png]]
> *Vlevo modře x³ se zelenou vodorovnou tečnou v 0: f′(0) = 0, a funkce přesto roste. Vpravo idea důkazu (1) „⇐“: když f(x₁) > f(x₂), má oranžová sečna zápornou směrnici a podle Lagrangeovy věty je někde mezi zelená tečna se stejnou zápornou směrnicí, tedy f′(t) < 0.*

> [!pozor] Jen na intervalu
> Věta mluví o (otevřeném) **intervalu**. Na sjednocení intervalů neplatí: $f(x) = -\frac{1}{x}$ má $f'(x) = \frac{1}{x^2} > 0$ na $(-\infty; 0) \cup (0; +\infty)$, ale $f(-1) = 1 > -1 = f(1)$, takže na tomto sjednocení rostoucí není. Rostoucí je zvlášť na $(-\infty; 0)$ a zvlášť na $(0; +\infty)$.

> [!navic] Co bude dál · handout 4B, slajdy 11–18
> Praktická verze věty: $f' > 0$ na $I$ ⇒ rostoucí, $f' < 0$ ⇒ klesající; ve stacionárním bodě, kde se neklesání mění v nerůst, je lokální maximum (a naopak minimum). Dál přijde druhá derivace: $f''(p) > 0$ ve stacionárním bodě znamená ostré lokální minimum, $f''(p) < 0$ ostré maximum, a pomocí $f''$ se popíše konvexita, konkávnost a inflexní body. Pokračuje v [[MA1 10 – Druhá derivace, konvexita a inflexe|MA1 10]].

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč je ve jmenovateli $k$-tého členu Taylorova polynomu $k!$?
> $k$-tá derivace $(x - p)^k$ je **$k!$**. Vydělením $k!$ vyjde $k$-tá derivace členu $\frac{f^{(k)}(p)}{k!}(x - p)^k$ přesně $f^{(k)}(p)$, takže polynom má v $p$ **stejné derivace jako $f$**.

> [!karta|02]- Co zaručuje $T_2(f, p)$ navíc oproti lineární aproximaci $T_1(f, p)$?
> Chyba $T_1$ je zanedbatelná vůči $(x - p)$, chyba $T_2$ dokonce vůči **$(x - p)^2$**. $T_2$ má navíc v $p$ stejnou **druhou derivaci** jako $f$, takže zachytí i zakřivení grafu.

> [!karta|03]- V důkazu základní věty o Taylorově polynomu pro $n = 2$: proč se l'Hospital použije jen jednou a druhý krok jde z definice $f''(p)$?
> Druhý l'Hospital by potřeboval **$f''$ na okolí $p$ spojitou v $p$**, ale předpoklad je jen existence $f''(p)$. Po prvním kroku je $\frac{f'(x) - f'(p)}{x - p} \to f''(p)$ přímo **z definice** $f''(p)$.

> [!karta|04]- Dokaž základní větu o Taylorově polynomu (1) pro $n = 2$ (náčrt).
> Typ $\frac{0}{0}$, **jednou l'Hospital**: $\lim \frac{f'(x) - f'(p) - f''(p)(x - p)}{2(x - p)} = \frac{1}{2}\left(\lim \frac{f'(x) - f'(p)}{x - p} - f''(p)\right) = \frac{1}{2}\big(f''(p) - f''(p)\big) = 0$. Limita podílu derivací existuje, takže i původní limita je **$0$**.

> [!karta|05]- Jak souvisí věta o odhadu chyby Taylorova polynomu s Lagrangeovou větou?
> Pro **$n = 0$** je $T_0(f, p)(x) = f(p)$ a odhad chyby říká $f(x) - f(p) = f'(t)(x - p)$, což je **Lagrangeova věta**. Odhad chyby je její zobecnění na vyšší stupně.

> [!karta|06]- Plyne z $f'(p) = 0$, že $f$ má v $p$ lokální extrém? Protipříklad.
> **Ne.** $f(x) = x^3 - 1$: $f'(0) = 0$, ale $f(x) < f(0)$ pro $x < 0$ a $f(x) > f(0)$ pro $x > 0$, takže v $0$ **extrém není**.

> [!karta|07]- Může mít funkce lokální extrém v bodě, který není stacionární? Příklad.
> **Ano**, když tam **derivace neexistuje**: $f(x) = -\lvert x + 7 \rvert$ má v $-7$ maximum, ale $f'(-7)$ neexistuje. Nutná podmínka $f'(p) = 0$ platí jen tam, kde $f'(p)$ existuje.

> [!karta|08]- V důkazu nutné podmínky lokálního extrému: proč $f'(p) > 0$ vede ke sporu s lokálním minimem v $p$?
> Podle **věty o znaménku limity** je $\frac{f(x) - f(p)}{x - p} > 0$ blízko $p$. Pro $x < p$ je jmenovatel záporný, takže **$f(x) < f(p)$**, spor s minimem.

> [!karta|09]- Jak najdeš největší a nejmenší hodnotu spojité funkce na $[a; b]$, která má derivaci uvnitř?
> Spočítej hodnoty v **krajních bodech** $a$, $b$ a ve **stacionárních bodech uvnitř** $(a; b)$ ($f'(x) = 0$). Největší z nich je maximum, nejmenší minimum (jinde extrém být nemůže).

> [!karta|10]- Platí „$f' > 0$ na $(-\infty; 0) \cup (0; +\infty)$ ⇒ $f$ je rostoucí na $(-\infty; 0) \cup (0; +\infty)$“? Protipříklad.
> **Neplatí.** $f(x) = -\frac{1}{x}$: $f'(x) = \frac{1}{x^2} > 0$, ale $f(-1) = 1 > -1 = f(1)$. Věta o monotonii platí jen na **intervalu**.

> [!karta|11]- Platí: $f$ je rostoucí na $\mathbb{R}$ ⇒ $f' > 0$ na $\mathbb{R}$? Protipříklad.
> **Neplatí.** $f(x) = x^3$ je rostoucí, ale **$f'(0) = 0$**. Rostoucí funkce zaručuje jen $f' \ge 0$.

> [!karta|12]- Co v charakterizaci rostoucí funkce znamená podmínka „v každém $(x_1; x_2) \subseteq I$ existuje $p$ s $f'(p) > 0$“?
> $f'$ nesmí být **nulová na celém podintervalu**. Jednotlivé body s $f' = 0$ nevadí (jako u $x^3$), ale úsek s $f' = 0$ znamená, že je tam $f$ **konstantní**, a pak není rostoucí.

> [!karta|13]- Dokaž: $f' \ge 0$ na otevřeném intervalu $I$ ⇒ $f$ je na $I$ neklesající.
> Sporem: $x_1 < x_2$ s $f(x_1) > f(x_2)$. **Lagrange na $[x_1; x_2]$**: $0 > \frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(t) \ge 0$, spor.

> [!karta|14]- Dokaž: $f$ neklesající na otevřeném intervalu $I$ ⇒ $f' \ge 0$ na $I$.
> Sporem: $f'(p) < 0$. Pak $\frac{f(x) - f(p)}{x - p} < 0$ blízko $p$ (**znaménko limity**). Pro $x < p$ je tedy **$f(x) > f(p)$**, spor s neklesáním.

> [!karta|15]- Dokaž: $f' \ge 0$ na $I$ a v každém podintervalu je bod s $f' > 0$ ⇒ $f$ je rostoucí.
> Podle (1) je $f$ neklesající. Kdyby $f(x_1) \ge f(x_2)$ pro $x_1 < x_2$, bylo by $f(x_1) \le f(x) \le f(x_2) \le f(x_1)$, tedy $f$ **konstantní na $[x_1; x_2]$** a $f' = 0$ na celém $(x_1; x_2)$, spor.

### Příklady na procvičení

> [!priklad|16]- Spočítej $T_4(f, 0)$ pro $f(x) = \cos x$.
> Derivace v $0$: $\cos 0 = 1$, $-\sin 0 = 0$, $-\cos 0 = -1$, $\sin 0 = 0$, $\cos 0 = 1$. Tedy **$T_4(\cos, 0)(x) = 1 - \frac{x^2}{2} + \frac{x^4}{24}$**.

> [!priklad|17]- Spočítej $T_3(f, 1)$ pro $f(x) = \ln x$.
> $f(1) = 0$, $f'(x) = \frac{1}{x}$, $f''(x) = -\frac{1}{x^2}$, $f'''(x) = \frac{2}{x^3}$, v bodě $1$: $1$, $-1$, $2$. **$T_3(\ln, 1)(x) = (x - 1) - \frac{(x - 1)^2}{2} + \frac{(x - 1)^3}{3}$**.

> [!priklad|18]- Odhadni $e$ pomocí $T_3(e^x, 0)(1)$ a omez chybu.
> $T_3(1) = 1 + 1 + \frac{1}{2} + \frac{1}{6} = \frac{8}{3} \approx 2{,}667$. Odhad chyby: $e - \frac{8}{3} = \frac{e^t}{24}$ pro $t \in (0; 1)$, a protože $e^t < 3$, je **chyba menší než $0{,}125$** (skutečně $0{,}052$).

> [!priklad|19]- Najdi stacionární body a lokální extrémy funkce $f(x) = x^3 - 3x$ na $\mathbb{R}$.
> $f'(x) = 3(x - 1)(x + 1)$, stacionární body **$\pm 1$**. $f' > 0$ na $(-\infty; -1)$ a $(1; +\infty)$, $f' < 0$ na $(-1; 1)$. V $-1$ je **ostré lokální maximum** $f(-1) = 2$, v $1$ **ostré lokální minimum** $f(1) = -2$.

> [!priklad|20]- Najdi největší a nejmenší hodnotu $f(x) = x^3 - 3x$ na $[0; 3]$.
> Krajní body: $f(0) = 0$, $f(3) = 18$. Stacionární bod uvnitř: $1$ s $f(1) = -2$ ($-1$ neleží v intervalu). **Maximum $18$ v bodě $3$, minimum $-2$ v bodě $1$.**

> [!priklad|21]- Urči intervaly monotonie funkce $f(x) = x e^{-x}$ na $\mathbb{R}$.
> $f'(x) = e^{-x} - x e^{-x} = (1 - x)e^{-x}$, a $e^{-x} > 0$. **Rostoucí na $(-\infty; 1)$, klesající na $(1; +\infty)$**, v bodě $1$ ostré lokální maximum $f(1) = \frac{1}{e}$.

> [!priklad|22]- Dokaž přímo z definice, že $f(x) = x^3$ je rostoucí na $\mathbb{R}$.
> Pro $x_1 < x_2$: $x_2^3 - x_1^3 = (x_2 - x_1)(x_1^2 + x_1 x_2 + x_2^2)$. První závorka je kladná, druhá je $\left(x_1 + \frac{x_2}{2}\right)^2 + \frac{3}{4}x_2^2 > 0$ (nulová jen pro $x_1 = x_2 = 0$). Tedy **$x_1^3 < x_2^3$**.

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 1. semestrálnímu testu (J. Velebil, 9.–13. 11. 2026). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|23]- Definujte pojem: funkce $f$ má v bodě $3$ ostré lokální maximum. (Přesně, se všemi předpoklady, českými větami.)
> Ať je funkce $f$ definována v bodě $3$ a na nějakém prstencovém okolí bodu $3$. Funkce $f$ má v bodě $3$ ostré lokální maximum, jestliže **existuje $\delta > 0$ takové, že pro všechna $x \in (3 - \delta; 3 + \delta)$, $x \neq 3$, platí $f(x) < f(3)$**. (Ekvivalentně: $f < f(3)$ ve směru $x \to 3$.)

> [!priklad|24]- Dokažte nebo vyvraťte: Jestliže $f$ má derivaci v bodě $p$ a $f'(p) = 0$, potom má $f$ v bodě $p$ lokální extrém.
> **Neplatí.** Protipříklad $f(x) = x^3$, $p = 0$: $f'(x) = 3x^2$, tedy $f'(0) = 0$. Pro každé $\delta > 0$ je $f\left(-\frac{\delta}{2}\right) = -\frac{\delta^3}{8} < 0 = f(0)$, takže v $0$ není lokální minimum, a $f\left(\frac{\delta}{2}\right) = \frac{\delta^3}{8} > 0 = f(0)$, takže ani lokální maximum. **Tvrzení je vyvráceno.**

> [!priklad|25]- Dokažte nebo vyvraťte: Jestliže $f$ má derivaci na $(0; 2)$ a $f'(x) \ge 0$ pro všechna $x \in (0; 2)$, potom pro všechna $x_1 < x_2$ z $(0; 2)$ platí $f(x_1) \le f(x_2)$.
> **Platí.** Ať $0 < x_1 < x_2 < 2$. Funkce $f$ má derivaci na $[x_1; x_2] \subseteq (0; 2)$, takže podle Lagrangeovy věty existuje $t \in (x_1; x_2)$ s $f(x_2) - f(x_1) = f'(t)(x_2 - x_1)$. Platí $f'(t) \ge 0$ a $x_2 - x_1 > 0$, tedy $f(x_2) - f(x_1) \ge 0$. **Tvrzení je dokázáno.**

> [!priklad|26]- Spočtěte největší a nejmenší hodnotu funkce $f(x) = x^4 - 2x^2$ na intervalu $[-2; 1]$.
> $f$ je polynom, tedy spojitá a s derivací všude. $f'(x) = 4x^3 - 4x = 4x(x - 1)(x + 1)$, stacionární body uvnitř $(-2; 1)$ jsou $-1$ a $0$. Hodnoty: $f(-2) = 8$, $f(-1) = -1$, $f(0) = 0$, $f(1) = -1$. Podle věty o největší a nejmenší hodnotě je **maximum $8$ v bodě $-2$ a minimum $-1$ v bodech $-1$ a $1$**.

> [!priklad|27]- Spočtěte $T_2(f, 0)$ pro $f(x) = \sqrt{1 + x}$ a pomocí něj $\lim_{x \to 0} \frac{\sqrt{1 + x} - 1 - \frac{x}{2}}{x^2}$.
> $f(0) = 1$, $f'(x) = \frac{1}{2}(1 + x)^{-1/2}$, $f''(x) = -\frac{1}{4}(1 + x)^{-3/2}$, tedy $f'(0) = \frac{1}{2}$, $f''(0) = -\frac{1}{4}$ a $T_2(f, 0)(x) = 1 + \frac{x}{2} - \frac{x^2}{8}$. Čitatel je $\big(f(x) - T_2(f, 0)(x)\big) - \frac{x^2}{8}$, takže limita je $\lim \frac{f(x) - T_2(f, 0)(x)}{x^2} - \frac{1}{8} = 0 - \frac{1}{8}$ podle základní věty o Taylorově polynomu. **Výsledek $-\frac{1}{8}$.**

---
← [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo|15. 10. 2026 Věty o střední hodnotě a l'Hospitalovo pravidlo]] · [[MA1 10 – Druhá derivace, konvexita a inflexe|22. 10. 2026 Druhá derivace, konvexita a inflexe]] →

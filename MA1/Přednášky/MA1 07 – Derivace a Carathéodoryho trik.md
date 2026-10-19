---
predmet: MA1
prednaska: 7
datum: 2026-10-14
zdroj: "Handout 3A, slajd 18; handout 3B (Derivace funkce v bodě), slajdy 3–10 a 12–14"
tags: [prednaska, MA1]
---

# MA1 07 – Derivace a Carathéodoryho trik

*Přednáška 7 · středa 14. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 3B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout03b.pdf) · [Handout 3A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout03a.pdf)

Témata: `spojitost inverzní funkce` · `rostoucí ⇒ prostá` · `derivace v bodě` · `derivace zleva a zprava` · `sečna a tečna` · `|x| nemá derivaci v 0` · `Carathéodoryho trik` · `derivace ⇒ spojitost` · `derivace xⁿ` · `aritmetika derivací` · `derivace složené funkce`

Přednáška nejdřív dokončila spojité funkce na $[a; b]$: spojitá funkce má inverzní funkci, právě když je rostoucí nebo klesající, a ta inverze je zase spojitá. Pak přišel nový pojem, [[derivace v bodě|derivace]]: limita směrnic sečen, tedy směrnice tečny. Hlavní nástroj dneška je Carathéodoryho trik, který převádí derivaci na spojitost jedné pomocné funkce $f^*$. Díky němu se věty o derivacích (součet, součin, podíl, složená funkce) dokazují stejně snadno jako věty o spojitosti z minula.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| inverzní funkce | $f$ spojitá na $[a; b]$ | $f^{-1}$ existuje $\iff$ $f$ rostoucí nebo klesající; pak je $f^{-1}$ spojitá |
| derivace | | $f'(p) = \lim_{h \to 0} \frac{f(p+h) - f(p)}{h} = \lim_{x \to p} \frac{f(x) - f(p)}{x - p}$, vlastní limita |
| jednostranné derivace | | $f'(p)$ existuje $\iff$ $f'_-(p) = f'_+(p)$ (obě vlastní) |
| Carathéodoryho trik | $f$ na $(a; b)$, $p \in (a; b)$ | $f'(p)$ existuje $\iff$ $f(x) - f(p) = f^*(x)(x - p)$ s $f^*$ spojitou v $p$; pak $f'(p) = f^*(p)$ |
| derivace ⇒ spojitost | $f'(p)$ existuje | $f$ je spojitá v $p$ (obráceně ne: $\lvert x \rvert$ v $0$) |
| mocnina | $n \ge 0$ | $(x^n)' = n x^{n-1}$ (pro $n = 0$ je $x^0 = 1$ a derivace $0$) |
| aritmetika | $f'(p)$, $g'(p)$ existují | $(rf + sg)' = rf' + sg'$, $(fg)' = f'g + fg'$, $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ při $g(p) \neq 0$ |
| složená funkce | $f'(p)$, $g'(f(p))$ existují | $(g \circ f)'(p) = g'(f(p)) \cdot f'(p)$ |

## §1 Spojitost inverzní funkce

Navazuje na věty o funkcích spojitých na $[a; b]$ z minula.

> [!definice] Prostá a ryze monotónní funkce, inverzní funkce · handout 3A, slajd 18
> Ať $f$ je definovaná na $[a; b]$.
>
> - $f$ je **rostoucí**, když $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$, a **klesající**, když $x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$. Rostoucí nebo klesající funkci se říká **ryze monotónní**.
> - $f$ je **prostá**, když $x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)$.
> - $f$ má **inverzní funkci** $f^{-1}$ na obrazu $f\big[[a; b]\big]$, když je prostá: $f^{-1}(y)$ je to jediné $x \in [a; b]$, pro které $f(x) = y$.

^def-inverzni

> [!lidsky] Lidsky
> [[ryze monotónní funkce|Rostoucí funkce]] je výtah, který jede jen nahoru: s každým krokem doprava je výš. [[prostá funkce|Prostá funkce]] nikdy nevrátí stejnou hodnotu dvakrát. A jen taková funkce jde „pustit pozpátku“: z výšky $y$ jednoznačně poznáš, v kterém místě $x$ jsi byl. To je [[inverzní funkce]] $f^{-1}$; její graf je graf $f$ zrcadlený podle přímky $y = x$.

> [!veta] Věta o spojitosti inverzní funkce · handout 3A, slajd 18
> ==Ať $f$ je spojitá na $[a; b]$.== Potom:
>
> 1. **$f^{-1}$ existuje, právě když je $f$ na $[a; b]$ rostoucí nebo klesající.**
> 2. **Pokud $f^{-1}$ existuje, je spojitá** na $[f(a); f(b)]$ (když $f$ roste), resp. na $[f(b); f(a)]$ (když $f$ klesá).
>
> > [!note]- Důkaz (1), směr ⇐
> > Ať $f$ je rostoucí (klesající obdobně). **$f$ je prostá**, sporem: ať $x_1 \neq x_2$ a $f(x_1) = f(x_2)$. Buď $x_1 < x_2$, pak $f(x_1) < f(x_2)$ ↯, nebo $x_2 < x_1$, pak $f(x_2) < f(x_1)$ ↯.
> >
> > **Obraz je celý $[f(a); f(b)]$**: pro $r$ mezi $f(a)$ a $f(b)$ dá [[věta o mezihodnotě]] $s \in [a; b]$ s $f(s) = r$, a díky prostotě je $s$ jediné. Tedy $f^{-1}(r) = s$ je definovaná na celém $[f(a); f(b)]$.
> >
> > Důkaz směru ⇒ se zde neuvádí.
>
> > [!note]- Důkaz (2), náznak
> > Ať $f$ roste (klesající obdobně), $y \in [f(a); f(b)]$ a $x = f^{-1}(y)$. Ať $\varepsilon > 0$ (dost malé, aby $x \pm \varepsilon$ ležely v $[a; b]$; u krajního bodu bereme jen jednu stranu). Protože $f$ roste, je $f(x - \varepsilon) < y < f(x + \varepsilon)$. Pro $y'$ ostře mezi $f(x - \varepsilon)$ a $f(x + \varepsilon)$ leží $f^{-1}(y')$ ostře mezi $x - \varepsilon$ a $x + \varepsilon$ (inverze k rostoucí funkci je rostoucí). Takže okolí $\big(f(x - \varepsilon); f(x + \varepsilon)\big)$ bodu $y$ se zobrazí do $(x - \varepsilon; x + \varepsilon)$, a to je přesně [[spojitost v bodě|spojitost]] $f^{-1}$ v $y$.

^veta-inverzni-spojitost

> [!lidsky] Lidsky
> [[věta o spojitosti inverzní funkce|Věta o spojitosti inverzní funkce]]: spojitá funkce na $[a; b]$ jde obrátit jen tehdy, když pořád roste nebo pořád klesá; jinak by nějakou výšku navštívila dvakrát. A obrácená funkce nemá kde „skočit“: je monotónní a její hodnoty vyplní celý interval $[a; b]$ bez děr, takže skok by musel nějakou hodnotu přeskočit.

> [!obrazek] Kdy existuje inverzní funkce
> ![[ma107-inverzni.png]]
> *Vlevo: modrá funkce, která není monotónní, nabude oranžové výšky ve dvou červených bodech, takže z výšky nejde poznat x. Uprostřed: rostoucí funkce nabude každé výšky r mezi f(a) a f(b) v jediném zeleném bodě s, a f⁻¹(r) = s. Vpravo: graf f⁻¹ (zeleně) je graf f (modře) zrcadlený podle šedé přímky y = x.*

> [!example] Odmocnina · handout 3A, slajd 18
> $x \mapsto x^n$ je spojitá a rostoucí na $[0; 1]$, proto je $x \mapsto \sqrt[n]{x}$ spojitá a rostoucí na $[0; 1]$. Spojitost odmocniny tedy není potřeba dokazovat přes ε-δ.

## §2 Derivace v bodě

> [!definice] Derivace v bodě · handout 3B, slajd 3
> $f$ **má derivaci v bodě $p$**, když existuje **vlastní** limita
>
> $$
> f'(p) = \lim_{h \to 0} \frac{f(p + h) - f(p)}{h}.
> $$
>
> Číslu $f'(p)$ se říká hodnota derivace $f$ v $p$. Jiné zápisy: $\frac{\mathrm{d}f}{\mathrm{d}x}(p)$, $\left(\frac{\mathrm{d}}{\mathrm{d}x} f\right)(p)$.

^def-derivace

> [!lidsky] Lidsky
> Zlomek $\frac{f(p+h) - f(p)}{h}$ je průměrná rychlost změny na úseku délky $h$: o kolik se změnila hodnota, děleno o kolik se změnil vstup. Když úsek zmenšuješ k nule, dostaneš okamžitou rychlost v bodě $p$. Tachometr v autě ukazuje přesně derivaci ujeté dráhy podle času. [[derivace v bodě|Derivace]] musí být reálné číslo; limita $\pm\infty$ se nepočítá.

> [!navic] Druhý zápis: $x \to p$ · handout 3B, slajd 6
> Dosazením $x = p + h$ (podle [[věta o substituci|věty o substituci]]) dostaneš
>
> $$
> f'(p) = \lim_{x \to p} \frac{f(x) - f(p)}{x - p}.
> $$
>
> Obě formy říkají totéž; podle příkladu je jedna nebo druhá pohodlnější. Carathéodoryho trik níže používá tu druhou.

### Derivace zleva a zprava

> [!definice] Jednostranné derivace · handout 3B, slajd 3
> **Derivace zprava** $f'_+(p) = \lim_{h \to 0^+} \frac{f(p + h) - f(p)}{h}$ a **derivace zleva** $f'_-(p) = \lim_{h \to 0^-} \frac{f(p + h) - f(p)}{h}$, pokud tyto limity existují a jsou vlastní. Ekvivalentně s $x \to p^+$, resp. $x \to p^-$ v zápisu přes $x$.
>
> **$f'(p)$ existuje, právě když existují $f'_-(p)$ i $f'_+(p)$ a jsou si rovny.**

^def-jednostranna-derivace

> [!lidsky] Lidsky
> [[jednostranná derivace|Jednostranná derivace]] je sklon grafu, když se díváš jen z jedné strany. Oboustranná derivace existuje, když se oba sklony shodují, stejně jako oboustranná [[jednostranná limita|limita]] existuje, když se shodují jednostranné.

### Sečna a tečna

> [!definice] Geometrický význam · handout 3B, slajd 4
> Pro $x \neq p$ je $\frac{f(x) - f(p)}{x - p}$ **směrnice sečny** grafu $f$ body $[p; f(p)]$ a $[x; f(x)]$. Má-li $f$ v $p$ derivaci, je přímka
>
> $$
> y = f(p) + f'(p)\,(x - p)
> $$
>
> **tečna** ke grafu $f$ v bodě $[p; f(p)]$: limitní poloha sečen pro $x \to p$. Jednostranně obdobně (tečna zleva, zprava).

^def-tecna

> [!lidsky] Lidsky
> [[tečna|Sečna]] protíná graf ve dvou bodech. Když druhý bod posouváš k prvnímu, sečna se otáčí a ustálí se v tečně, přímce, která se grafu v $[p; f(p)]$ jen „dotkne“. Derivace je její sklon: o kolik tečna stoupne, když jdeš o 1 doprava.

> [!obrazek] Sečny se blíží k tečně
> ![[ma107-secny.png]]
> *Modrý graf f, červený bod [p; f(p)]. Oranžové sečny vedou k bodům x₁, x₂, x₃, x₄, které se blíží k p; čím blíž, tím je sečna sytější. Jejich směrnice se blíží ke směrnici zelené tečny, a to je f′(p).*

### Příklad: spojitá funkce bez derivace

> [!example] $f(x) = \lvert x \rvert$ v bodě $0$ · handout 3B, slajd 5
> $$
> f'_+(0) = \lim_{h \to 0^+} \frac{\lvert 0 + h \rvert - \lvert 0 \rvert}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1, \qquad f'_-(0) = \lim_{h \to 0^-} \frac{-h}{h} = -1.
> $$
>
> Jednostranné derivace jsou různé, takže **$f'(0)$ neexistuje**, i když je $\lvert x \rvert$ v nule [[spojitost v bodě|spojitá]]. V ostatních bodech derivace existuje: $f'(p) = -1$ pro $p < 0$ a $f'(p) = 1$ pro $p > 0$.

^priklad-abs

> [!obrazek] Zub v nule
> ![[ma107-abs.png]]
> *Modrý graf |x| má v červeném bodě zub. Zleva se k němu přimyká oranžová tečna se směrnicí −1, zprava zelená se směrnicí 1. Jedna společná tečna neexistuje.*

> [!navic] Zub = různé jednostranné derivace · handout 3B, slajdy 5 a 20
> Je-li $f$ spojitá v $p$ a $f'_-(p) \neq f'_+(p)$ jsou dvě reálná čísla, má graf v $p$ zub. Spojitá funkce na $[a; b]$ s jednostrannými derivacemi všude jich může mít nekonečně mnoho, ale nejvýš spočetně. A existuje dokonce spojitá funkce, která nemá derivaci **nikde** (Weierstrassova funkce, 1872).

> [!navic] Nevlastní derivace · handout 3B, slajd 7
> Handout varuje před zápisem typu $f'(3) = +\infty$. Třeba pro $f(x) = \sqrt[3]{x}$ se píše $f'(0) = +\infty$: znamená to jen, že $\lim_{h \to 0} \frac{\sqrt[3]{h}}{h} = \lim_{h \to 0} h^{-2/3} = +\infty$, tečna je svislá. Derivace v pravém smyslu (vlastní) tam neexistuje.

## §3 Carathéodoryho trik

> [!veta] Carathéodoryho trik (lemma) · handout 3B, slajd 8
> ==Ať $f$ je definovaná na otevřeném intervalu $(a; b)$ a $p \in (a; b)$.== Následující je ekvivalentní:
>
> 1. **$f'(p)$ existuje** (a je to reálné číslo).
> 2. **Existuje funkce $f^*$ spojitá v $p$ taková, že**
>
> $$
> f(x) - f(p) = f^*(x) \cdot (x - p) \quad \text{pro všechna } x \in (a; b).
> $$
>
> Potom **$f'(p) = f^*(p)$**. Funkce $f^*$ závisí na $f$ i na bodu $p$.
>
> > [!note]- Důkaz (1) ⇒ (2)
> > Definuj
> >
> > $$
> > f^*(x) = \begin{cases} \dfrac{f(x) - f(p)}{x - p}, & x \neq p, \\[2mm] f'(p), & x = p. \end{cases}
> > $$
> >
> > Pro $x \neq p$ rovnost $f(x) - f(p) = f^*(x)(x - p)$ platí vynásobením, pro $x = p$ jsou obě strany $0$. Spojitost v $p$: $\lim_{x \to p} f^*(x) = \lim_{x \to p} \frac{f(x) - f(p)}{x - p} = f'(p) = f^*(p)$.
>
> > [!note]- Důkaz (2) ⇒ (1)
> > Pro $x \neq p$ smíš rovností vydělit: $\frac{f(x) - f(p)}{x - p} = f^*(x)$. Limita levé strany pro $x \to p$ je derivace, limita pravé strany je díky spojitosti $f^*$ v $p$ rovna $f^*(p)$. Tedy $f'(p)$ existuje a $f'(p) = f^*(p)$.

^veta-caratheodory

> [!lidsky] Lidsky
> [[Carathéodoryho trik]] schová limitu do spojitosti. Funkce $f^*(x)$ je směrnice sečny z bodu $p$ do bodu $x$; v samotném $p$ do ní „doplníš“ směrnici tečny. Derivace existuje přesně tehdy, když se tím doplněním nic neroztrhne. Výhoda: místo počítání limit zlomků stačí najít $f^*$ (často vytknutím $x - p$) a ověřit, že je spojitá, a na to už máme celou aritmetiku spojitých funkcí.

> [!obrazek] f* pro x² v bodě 1
> ![[ma107-fstar.png]]
> *Vlevo modře x², červený bod [1; 1], oranžová sečna k bodu x = 2 má směrnici 3, zelená tečna směrnici 2. Vpravo modře f*(x) = x + 1, protože x² − 1 = (x + 1)(x − 1): oranžový bod f*(2) = 3 je směrnice sečny, zelený bod f*(1) = 2 je směrnice tečny, tedy f′(1). Graf f* je spojitý, žádná díra v bodě 1.*

> [!navic] Proč „trik“
> Zlomek $\frac{f(x) - f(p)}{x - p}$ v bodě $p$ dává $\frac{0}{0}$, takže se s ním nedá přímo počítat. Rovnost $f(x) - f(p) = f^*(x)(x - p)$ žádné dělení nemá a platí i v $x = p$. Proto se s ní v důkazech pracuje jako s obyčejnou algebrou: dosazuje, sčítá, násobí.

### Příklad: derivace mocniny

> [!example] $f(x) = x^n$, $n \ge 0$ přirozené · handout 3B, slajd 10
> Vytkni $x - p$:
>
> $$
> \underbrace{x^n - p^n}_{f(x) - f(p)} = \underbrace{\left(x^{n-1} + x^{n-2} p + x^{n-3} p^2 + \dots + x p^{n-2} + p^{n-1}\right)}_{f^*(x)} \cdot (x - p).
> $$
>
> $f^*$ je polynom, tedy spojitý v $p$, a v $p$ má $n$ sčítanců, každý roven $p^{n-1}$. Proto
>
> $$
> f'(p) = f^*(p) = n \cdot p^{n-1}.
> $$
>
> Pro $n = 2$: $x^2 - p^2 = (x + p)(x - p)$, $f^*(x) = x + p$ a $f'(p) = 2p$.

^priklad-mocnina

## §4 Derivace ⇒ spojitost

> [!veta] Derivace implikuje spojitost · handout 3B, slajd 9
> ==Ať $f$ má derivaci v bodě $p$.== Potom **$f$ je spojitá v $p$**.
>
> > [!note]- Důkaz
> > Podle Carathéodoryho triku existuje $f^*$ spojitá v $p$ s $f(x) - f(p) = f^*(x)(x - p)$. Chceme $\lim_{x \to p} f(x) = f(p)$, neboli $\lim_{x \to p} \big(f(x) - f(p)\big) = 0$. Podle [[věta o aritmetice limit|aritmetiky limit]]
> >
> > $$
> > \lim_{x \to p} \big(f^*(x)(x - p)\big) = \underbrace{\lim_{x \to p} f^*(x)}_{= f'(p)} \cdot \underbrace{\lim_{x \to p} (x - p)}_{= 0} = 0.
> > $$

^veta-derivace-spojitost

> [!lidsky] Lidsky
> [[věta o spojitosti funkce s derivací|Funkce s derivací je spojitá]]: rozdíl $f(x) - f(p)$ je (rozumně velká směrnice) krát (vzdálenost $x - p$, která jde k nule), a to jde k nule. Kde má graf skok, tečna být nemůže. Obráceně to **neplatí**: $\lvert x \rvert$ je v nule spojitá, ale derivaci tam nemá.

> [!pozor] Častá chyba: obrácená implikace
> „Spojitá ⇒ má derivaci“ neplatí. Protipříklad, který stačí znát: $\lvert x \rvert$ v bodě $0$. Platí jen obměna: **nespojitá v $p$ ⇒ nemá derivaci v $p$**.

## §5 Aritmetika derivací

> [!veta] Věta o aritmetice derivací · handout 3B, slajd 12
> ==Ať $f$ a $g$ mají derivaci v bodě $p$.== Potom:
>
> 1. Pro všechna $r, s \in \mathbb{R}$: **$(r f + s g)'(p) = r f'(p) + s g'(p)$.**
> 2. **$(f \cdot g)'(p) = f'(p)\, g(p) + f(p)\, g'(p)$.**
> 3. Je-li ==$g(p) \neq 0$==: $\displaystyle \left(\frac{f}{g}\right)'(p) = \frac{f'(p)\, g(p) - f(p)\, g'(p)}{\big(g(p)\big)^2}$.

^veta-aritmetika-derivaci

> [!lidsky] Lidsky
> [[věta o aritmetice derivací|Aritmetika derivací]]: derivace se chová lineárně (konstanty se vytknou, součet se derivuje po částech), ale součin **ne** člen po členu: derivuje se vždy jen jeden činitel a druhý se nechá. Představ si obdélník se stranami $f$ a $g$, které rostou: plocha $fg$ přibude o pruh $f' \cdot g$ podél jedné strany a pruh $f \cdot g'$ podél druhé.

Všechny tři důkazy mají stejný vzor: napsat rozdíl $(\ldots)(x) - (\ldots)(p)$ jako (něco spojitého v $p$) $\cdot (x - p)$ a to „něco“ vyhodnotit v $p$.

> [!note]- Důkaz (1): lineární kombinace
> $$
> \begin{aligned}
> (rf + sg)(x) - (rf + sg)(p) &= r\big(f(x) - f(p)\big) + s\big(g(x) - g(p)\big) \\
> &= r f^*(x)(x - p) + s g^*(x)(x - p) \\
> &= \big(r f^*(x) + s g^*(x)\big)(x - p).
> \end{aligned}
> $$
>
> Funkce $r f^* + s g^*$ je spojitá v $p$ ([[věta o aritmetice spojitých funkcí|aritmetika spojitých funkcí]]), takže podle Carathéodoryho triku $(rf + sg)'(p) = r f^*(p) + s g^*(p) = r f'(p) + s g'(p)$.

^dukaz-linearita

> [!note]- Důkaz (2): součin
> Trik „přičti a odečti“ $f(p)\, g(x)$:
>
> $$
> \begin{aligned}
> f(x) g(x) - f(p) g(p) &= f(x) g(x) - f(p) g(x) + f(p) g(x) - f(p) g(p) \\
> &= \big(f(x) - f(p)\big) g(x) + f(p)\big(g(x) - g(p)\big) \\
> &= \big(f^*(x)\, g(x) + f(p)\, g^*(x)\big)(x - p).
> \end{aligned}
> $$
>
> Závorka je spojitá v $p$: $f^*$ a $g^*$ jsou spojité v $p$ a **$g$ je spojitá v $p$, protože má derivaci** (§4). V bodě $p$ dá $f'(p)\, g(p) + f(p)\, g'(p)$.

^dukaz-soucin

> [!note]- Důkaz (3): podíl
> Nejdřív $\frac{1}{g}$. Z $g(p) \neq 0$ a spojitosti $g$ v $p$ plyne $g \neq 0$ na nějakém okolí $p$ ([[věta o znaménku limity|věta o znaménku]]), takže $\frac{1}{g}$ je tam definovaná. Pak
>
> $$
> \frac{1}{g(x)} - \frac{1}{g(p)} = \frac{g(p) - g(x)}{g(x)\, g(p)} = \frac{-g^*(x)}{g(x)\, g(p)} \cdot (x - p).
> $$
>
> Zlomek $\frac{-g^*(x)}{g(x)\, g(p)}$ je spojitý v $p$ (jmenovatel je v $p$ nenulový), takže
>
> $$
> \left(\frac{1}{g}\right)'(p) = \frac{-g'(p)}{\big(g(p)\big)^2}.
> $$
>
> Obecný podíl je součin $f \cdot \frac{1}{g}$, a podle (2):
>
> $$
> \left(\frac{f}{g}\right)'(p) = f'(p) \cdot \frac{1}{g(p)} + f(p) \cdot \frac{-g'(p)}{g(p)^2} = \frac{f'(p)\, g(p) - f(p)\, g'(p)}{g(p)^2}.
> $$

^dukaz-podil

> [!pozor] Častá chyba v derivaci $\frac{1}{g}$
> V čitateli je **$-g'(p)$**, ne $-g(p)$. Kontrola na $g(x) = x$: $\left(\frac{1}{x}\right)' = \frac{-1}{x^2}$, tedy čitatel je $-g' = -1$. A u podílu záleží na pořadí: $f'g - fg'$, ne obráceně.

> [!pozor] Derivace součinu není součin derivací
> $(fg)' \neq f' g'$. Protipříklad: $f = g = x$, pak $(x \cdot x)' = (x^2)' = 2x$, ale $f' g' = 1 \cdot 1 = 1$.

## §6 Derivace složené funkce (Chain Rule)

> [!veta] Věta o derivaci složené funkce · handout 3B, slajd 13
> ==Ať existují $f'(p)$ a $g'(f(p))$== (tedy $f$ je definovaná v $p$ a ve směru $x \to p$ a $g$ v $f(p)$ a ve směru $z \to f(p)$). Potom $g \circ f: x \mapsto g(f(x))$ má derivaci v $p$ a
>
> $$
> \mathbf{(g \circ f)'(p) = g'\big(f(p)\big) \cdot f'(p).}
> $$
>
> > [!note]- Důkaz
> > Ať $f^*$ je Carathéodoryho funkce $f$ v bodě $p$ a $g^*$ Carathéodoryho funkce $g$ v bodě $f(p)$, tedy $g(z) - g(f(p)) = g^*(z)\,(z - f(p))$. Dosaď $z = f(x)$:
> >
> > $$
> > \begin{aligned}
> > (g \circ f)(x) - (g \circ f)(p) &= g\big(f(x)\big) - g\big(f(p)\big) \\
> > &= g^*\big(f(x)\big) \cdot \big(f(x) - f(p)\big) \\
> > &= \underbrace{g^*\big(f(x)\big) \cdot f^*(x)}_{\text{spojitá v } p} \cdot (x - p).
> > \end{aligned}
> > $$
> >
> > $g^* \circ f$ je spojitá v $p$ podle [[věta o spojitosti složené funkce|věty o spojitosti složené funkce]]: $f$ je spojitá v $p$ (má derivaci, §4) a $g^*$ je spojitá v $f(p)$. Součin s $f^*$ je spojitý v $p$, takže $(g \circ f)'(p) = g^*(f(p)) \cdot f^*(p) = g'(f(p)) \cdot f'(p)$.

^veta-chain-rule

> [!lidsky] Lidsky
> [[věta o derivaci složené funkce|Derivace složené funkce]] je řetěz převodů: když $f$ zrychlí vstup dvakrát a $g$ výsledek ještě třikrát, celek zrychluje šestkrát. Derivace „vrstev“ se násobí. Pozor jen, kde se vnější derivace bere: v bodě $f(p)$, tedy tam, kam vnitřní funkce zrovna ukazuje.

> [!pozor] Kde se počítá vnější derivace
> $g'$ se vyhodnotí v **$f(p)$**, ne v $p$. Častá chyba je napsat $(\sin x^2)' = \cos x \cdot 2x$; správně je $\cos(x^2) \cdot 2x$.

> [!example] Typický příklad · handout 3B, slajdy 13 a 14
> Spočítej $f'(p)$ pro $f(x) = e^{\cos\left(\frac{x - 1}{x + 1}\right)}$ a $p \neq -1$.
>
> Rozlož $f = w \circ v \circ u$:
>
> $$
> u(x) = \frac{x - 1}{x + 1}, \qquad v(z) = \cos z, \qquad w(t) = e^t.
> $$
>
> Derivace vrstev (u $u$ podle pravidla pro podíl):
>
> $$
> u'(x) = \frac{1 \cdot (x + 1) - (x - 1) \cdot 1}{(x + 1)^2} = \frac{2}{(x + 1)^2}, \qquad v'(z) = -\sin z, \qquad w'(t) = e^t.
> $$
>
> Věta o složené funkci použitá dvakrát dá $f'(p) = w'\big(v(u(p))\big) \cdot v'\big(u(p)\big) \cdot u'(p)$, tedy
>
> $$
> f'(p) = e^{\cos\left(\frac{p - 1}{p + 1}\right)} \cdot \left(-\sin \frac{p - 1}{p + 1}\right) \cdot \frac{2}{(p + 1)^2}.
> $$

^priklad-retizek

> [!obrazek] Řetízek vrstev
> ![[ma107-retizek.png]]
> *Modré rámečky jsou mezivýsledky, oranžové šipky funkce u, v, w, zeleně pod nimi jejich derivace. Červený vzorec: derivace celku je součin derivací vrstev, každá vyhodnocená v bodě, kam zrovna ukazuje předchozí vrstva.*

> [!navic] Co bude dál
> Handout 3B pokračuje větou o derivaci inverzní funkce, $(f^{-1})'(f(p)) = \frac{1}{f'(p)}$ při $f'(p) \neq 0$, tabulkou derivací ($\sin$, $\cos$, $e^x$, $\ln$, …) a vyššími derivacemi.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Dokaž: rostoucí funkce je prostá.
> Sporem: $x_1 \neq x_2$ a $f(x_1) = f(x_2)$. Buď $x_1 < x_2$, pak **$f(x_1) < f(x_2)$** ↯, nebo $x_2 < x_1$, pak $f(x_2) < f(x_1)$ ↯.

> [!karta|02]- Proč je inverzní funkce k rostoucí spojité $f$ na $[a; b]$ definovaná na celém $[f(a); f(b)]$?
> Každé $r$ mezi $f(a)$ a $f(b)$ se podle **věty o mezihodnotě** nabude v nějakém $s$, a díky prostotě v jediném. Proto $f^{-1}(r) = s$ existuje pro každé takové $r$.

> [!karta|03]- Proč je $\lim_{h \to 0} \frac{f(p+h) - f(p)}{h} = \lim_{x \to p} \frac{f(x) - f(p)}{x - p}$?
> Je to **substituce $x = p + h$**: $h \to 0$ právě když $x \to p$ a $h \neq 0$ právě když $x \neq p$. Obě limity tedy existují současně a rovnají se.

> [!karta|04]- Platí: $f$ spojitá v $p$ ⇒ $f'(p)$ existuje? Protipříklad.
> **Ne.** $\lvert x \rvert$ je v $0$ spojitá, ale $f'_+(0) = 1 \neq -1 = f'_-(0)$, takže $f'(0)$ neexistuje (graf má zub).

> [!karta|05]- Dokaž v Carathéodoryho triku (1) ⇒ (2): jak sestrojíš $f^*$?
> $f^*(x) = \frac{f(x) - f(p)}{x - p}$ pro $x \neq p$ a **$f^*(p) = f'(p)$**. Rovnost $f(x) - f(p) = f^*(x)(x - p)$ platí (v $p$ jsou obě strany $0$) a $\lim_{x \to p} f^* = f'(p) = f^*(p)$, tedy $f^*$ je spojitá v $p$.

> [!karta|06]- Dokaž v Carathéodoryho triku (2) ⇒ (1).
> Pro $x \neq p$ je $\frac{f(x) - f(p)}{x - p} = f^*(x)$. Ze **spojitosti $f^*$ v $p$** má pravá strana pro $x \to p$ limitu $f^*(p)$, tedy $f'(p)$ existuje a rovná se $f^*(p)$.

> [!karta|07]- Jaký geometrický význam má funkce $f^*$ z Carathéodoryho triku?
> Pro $x \neq p$ je $f^*(x)$ **směrnice sečny** bodů $[p; f(p)]$ a $[x; f(x)]$. Spojitost v $p$ říká, že se tyto směrnice spojitě blíží ke $f^*(p)$, **směrnici tečny**.

> [!karta|08]- Dokaž: má-li $f$ derivaci v $p$, je v $p$ spojitá.
> $f(x) - f(p) = f^*(x)(x - p)$ a $\lim_{x \to p} f^*(x) \cdot \lim_{x \to p}(x - p) = f'(p) \cdot 0 = 0$. Tedy $\lim_{x \to p} f(x) = f(p)$.

> [!karta|09]- Dokaž Carathéodoryho trikem, že $(x^n)' = n x^{n-1}$.
> $x^n - p^n = (x^{n-1} + x^{n-2}p + \dots + p^{n-1})(x - p)$. Závorka je polynom, tedy spojitá, a v $p$ má **$n$ sčítanců $p^{n-1}$**, takže $f'(p) = n p^{n-1}$.

> [!karta|10]- Dokaž Carathéodoryho trikem, že $(rf + sg)'(p) = r f'(p) + s g'(p)$.
> $(rf + sg)(x) - (rf + sg)(p) = \big(r f^*(x) + s g^*(x)\big)(x - p)$ a **$r f^* + s g^*$ je spojitá v $p$**. Hodnota v $p$ je $r f'(p) + s g'(p)$.

> [!karta|11]- Dokaž pravidlo pro derivaci součinu (náčrt). Kde se použije, že $g$ má derivaci?
> Přičti a odečti $f(p) g(x)$: $fg(x) - fg(p) = \big(f^*(x) g(x) + f(p) g^*(x)\big)(x - p)$. Závorka je spojitá v $p$, protože **$g$ je spojitá v $p$ (má derivaci)**. V $p$ dá $f'(p) g(p) + f(p) g'(p)$.

> [!karta|12]- Dokaž, že $\left(\frac{1}{g}\right)'(p) = \frac{-g'(p)}{g(p)^2}$. Proč je potřeba $g(p) \neq 0$?
> $\frac{1}{g(x)} - \frac{1}{g(p)} = \frac{-g^*(x)}{g(x) g(p)}(x - p)$, zlomek je spojitý v $p$. **$g(p) \neq 0$** se spojitostí dá $g \neq 0$ na okolí $p$, takže $\frac{1}{g}$ je tam definovaná a jmenovatel v $p$ není nula.

> [!karta|13]- Jak z derivace $\frac{1}{g}$ a pravidla pro součin dostaneš derivaci podílu $\frac{f}{g}$?
> $\frac{f}{g} = f \cdot \frac{1}{g}$, takže $\left(\frac{f}{g}\right)' = \frac{f'}{g} + f \cdot \frac{-g'}{g^2} = \frac{f' g - f g'}{g^2}$.

> [!karta|14]- Dokaž větu o derivaci složené funkce (náčrt). Kde se použije spojitost?
> $g(f(x)) - g(f(p)) = g^*(f(x))\big(f(x) - f(p)\big) = g^*(f(x)) f^*(x)(x - p)$. **$g^* \circ f$ je spojitá v $p$**, protože $f$ je spojitá v $p$ (má derivaci) a $g^*$ v $f(p)$. V $p$ dá $g'(f(p)) \cdot f'(p)$.

> [!karta|15]- Co znamená zápis $f'(0) = +\infty$ pro $f(x) = \sqrt[3]{x}$? Má $f$ v $0$ derivaci?
> Jen to, že $\lim_{h \to 0} \frac{\sqrt[3]{h}}{h} = +\infty$ (**svislá tečna**). Derivace v pravém smyslu musí být vlastní, takže **neexistuje**; $+\infty$ není hodnota nějaké funkce $f'$.

### Příklady na procvičení

> [!priklad|16]- Najdi Carathéodoryho funkci $f^*$ pro $f(x) = x^2$ v bodě $p$ a spočítej $f'(p)$.
> $x^2 - p^2 = (x + p)(x - p)$, takže $f^*(x) = x + p$, spojitá. **$f'(p) = 2p$**.

> [!priklad|17]- Spočítej $f'_+(0)$ a $f'_-(0)$ pro $f(x) = \lvert x \rvert$.
> $f'_+(0) = \lim_{h \to 0^+} \frac{h}{h} =$ **1**, $f'_-(0) = \lim_{h \to 0^-} \frac{-h}{h} =$ **−1**. Různé, $f'(0)$ neexistuje.

> [!priklad|18]- Carathéodoryho trikem spočítej derivaci $f(x) = \frac{1}{x}$ v bodě $p \neq 0$.
> $\frac{1}{x} - \frac{1}{p} = \frac{p - x}{xp} = -\frac{1}{xp}(x - p)$, $f^*(x) = -\frac{1}{xp}$ je spojitá v $p$. **$f'(p) = -\frac{1}{p^2}$**.

> [!priklad|19]- Carathéodoryho trikem spočítej derivaci $f(x) = \sqrt{x}$ v bodě $p > 0$.
> $\sqrt{x} - \sqrt{p} = \frac{x - p}{\sqrt{x} + \sqrt{p}}$, tedy $f^*(x) = \frac{1}{\sqrt{x} + \sqrt{p}}$, spojitá v $p$. **$f'(p) = \frac{1}{2\sqrt{p}}$**.

> [!priklad|20]- Má $f(x) = x \lvert x \rvert$ derivaci v $0$?
> $f(x) - f(0) = \lvert x \rvert \cdot (x - 0)$, takže $f^*(x) = \lvert x \rvert$, a ta je spojitá v $0$. **Ano, $f'(0) = 0$.**

> [!priklad|21]- Spočítej derivaci $f(x) = \frac{x^2 + 1}{x - 2}$ v bodě $3$.
> $f'(x) = \frac{2x(x - 2) - (x^2 + 1)}{(x - 2)^2} = \frac{x^2 - 4x - 1}{(x - 2)^2}$, takže $f'(3) = \frac{9 - 12 - 1}{1} =$ **−4**.

> [!priklad|22]- Spočítej $f'(0)$ pro $f(x) = e^{\cos\left(\frac{x - 1}{x + 1}\right)}$.
> $u(0) = -1$, $u'(0) = \frac{2}{1} = 2$, takže $f'(0) = e^{\cos(-1)} \cdot \big(-\sin(-1)\big) \cdot 2 =$ **$2 e^{\cos 1} \sin 1 \approx 2{,}889$**.

> [!priklad|23]- Má $f(x) = x^2$ inverzní funkci na $[-1; 1]$? A na $[0; 1]$?
> Na $[-1; 1]$ **ne**: $f(-1) = f(1) = 1$, není prostá (ani monotónní). Na $[0; 1]$ **ano**: je rostoucí, $f^{-1}(y) = \sqrt{y}$ je spojitá na $[0; 1]$.

---
← [[MA1 06 – Spojitost a spojité funkce na intervalu|8. 10. 2026 Spojitost a spojité funkce na intervalu]] · [[MA1 08 – Věty o střední hodnotě a l'Hospitalovo pravidlo|15. 10. 2026 Věty o střední hodnotě a l'Hospitalovo pravidlo]] →

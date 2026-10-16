---
predmet: LAG
prednaska: 7
datum: 2026-10-14
zdroj: "V poznámkách kap. 6.1 (úvod) a 6.2 (skládání)"
tags: [prednaska, LAG]
---

# LAG 07 – Lineární zobrazení

*Přednáška 7 · středa 14. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `lineární zobrazení` · `Lin(V, W)` · `lineární operátor` · `skládání zobrazení` · `A(0) = 0` · `kritérium linearity` · `zachování lineárních kombinací` · `příklady v rovině` · `součin matice a vektoru` · `matice zobrazení`

Doteď jsme zkoumali prostory samotné: podprostory, báze, dimenzi a souřadnice. Dnes začíná nová kapitola o **zobrazeních mezi prostory**, a to těch, která se slučují se sčítáním a násobením číslem. Minule jsme jedno takové potkali: přiřazení souřadnic $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$. Na konci přednášky uvidíme, že každé takové zobrazení $\mathbb{F}^n \to \mathbb{F}^m$ je vlastně násobení maticí.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[lineární zobrazení]] | $A(\vec{x} + \vec{y}) = A\vec{x} + A\vec{y}$ a $A(\alpha\vec{x}) = \alpha A\vec{x}$ | otočení roviny, derivace polynomů |
| [[množina lineárních zobrazení]] | $\operatorname{Lin}(V, W)$ = všechna lineární zobrazení $V \to W$ | |
| [[lineární operátor]] | lineární zobrazení $V \to V$; $\operatorname{Lin}(V) = \operatorname{Lin}(V, V)$ | stejnolehlost |
| [[složené zobrazení]] | $BA = B \circ A$: nejdřív $A$, potom $B$ | otočení a pak souměrnost |
| [[asociativita skládání zobrazení]] | $C(BA) = (CB)A$, závorky jde vynechat | |
| [[věta o obrazu nulového vektoru]] | $A(\vec{o}_V) = \vec{o}_W$ | $2x + 1$ proto lineární není |
| [[kritérium linearity]] | stačí jedna podmínka $A(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y}$ | |
| [[věta o zachování lineárních kombinací]] | $A(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n) = \alpha_1 A\vec{x}_1 + \dots + \alpha_n A\vec{x}_n$ | |
| [[nulové zobrazení]], [[identické zobrazení]], [[stejnolehlost]] | $\vec{x} \mapsto \vec{o}$, $\vec{x} \mapsto \vec{x}$, $\vec{x} \mapsto k\vec{x}$ | |
| [[věta o zobrazení zadaném sloupci]] | $(x_1; \dots; x_n) \mapsto x_1\vec{a}_1 + \dots + x_n\vec{a}_n$ je lineární | |
| [[součin matice a vektoru]] | matice krát vektor = kombinace sloupců s koeficienty ze složek vektoru | $\begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = x\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + y\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$ |
| [[matice zobrazení v kanonické bázi]] | $i$-tý sloupec je $A\vec{e}_i$ | zkosení: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ |

## §1 Definice lineárního zobrazení

Funkce ze školy přiřazuje číslu číslo. Teď budeme přiřazovat **vektoru vektor**: polynomu polynom, šipce šipku, sloupci sloupec. Zajímají nás jen zobrazení, která nerozbijí to, co z množiny dělá [[lineární prostor]], tedy sčítání a násobení číslem.

> [!definice] Definice · lineární zobrazení · kap. 6.1
> Buďte $V$, $W$ lineární prostory nad (stejným) tělesem $\mathbb{F}$. Zobrazení $A : V \to W$ se nazývá *lineární*, jestliže
>
> 1. $(\forall \vec{x}, \vec{y} \in V)\ \big(A(\vec{x} + \vec{y}) = A(\vec{x}) + A(\vec{y})\big)$,
> 2. $(\forall \alpha \in \mathbb{F})(\forall \vec{x} \in V)\ \big(A(\alpha\vec{x}) = \alpha A(\vec{x})\big)$.

^def-linearni-zobrazeni

> [!lidsky] Lidsky
> Lineární zobrazení „komutuje s počítáním“: je jedno, jestli vektory nejdřív sečteš a pak zobrazíš, nebo nejdřív zobrazíš a pak sečteš. Představ si kopírku, která zvětšuje na 200 %. Okopíruješ-li dva obrázky položené vedle sebe, dostaneš totéž, jako když každý okopíruješ zvlášť a pak je položíš vedle sebe. A obrázek dvakrát tmavší dá dvakrát tmavší kopii. Podmínce 1 se říká *aditivita*, podmínce 2 *homogenita*.

> [!pozor] Dvě různá plus i dvě různá krát
> V $A(\vec{x} + \vec{y}) = A(\vec{x}) + A(\vec{y})$ se vlevo sčítá ve $V$, vpravo ve $W$. Třeba u derivace polynomů je to obojí sčítání polynomů, ale u $A : \mathbb{R}^3 \to \mathbb{R}^2$ jde vlevo o trojice a vpravo o dvojice. Totéž platí pro násobení číslem. Proto musí být oba prostory nad **stejným** tělesem: číslo $\alpha$ násobí vlevo vektor z $V$ a vpravo vektor z $W$.

> [!definice] Definice · $\operatorname{Lin}(V, W)$ a lineární operátor · kap. 6.1
> Množinu všech lineárních zobrazení z $V$ do $W$ značíme $\operatorname{Lin}(V, W)$.
> Jestliže $V = W$, lineární zobrazení $A : V \to V$ se rovněž nazývá *lineární operátor na $V$*. Množinu všech lineárních operátorů na $V$ značíme $\operatorname{Lin}(V) = \operatorname{Lin}(V, V)$.

^def-lin-operator

> [!lidsky] Lidsky
> $\operatorname{Lin}(V, W)$ je „katalog“ všech lineárních zobrazení z $V$ do $W$; zápis $A \in \operatorname{Lin}(V, W)$ je zkratka pro „$A : V \to W$ je lineární“. Operátor je zobrazení, které zůstává v témže prostoru: otočení roviny pošle rovinu zase do roviny, derivace pošle polynom zase na polynom.

> [!navic] Odkud to známe
> Na [[LAG 01 – Úvod do lineární algebry#Matice jako transformace|první přednášce]] matice $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ zkosila čtvercovou síť. A minule jsme dokázali [[věta o linearitě souřadnic|linearitu souřadnic]]: $[\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$ a $[\gamma\vec{x}]^{\mathcal{X}} = \gamma[\vec{x}]^{\mathcal{X}}$. To jsou přesně podmínky 1 a 2, takže $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$ je lineární zobrazení $L \to \mathbb{F}^n$.

> [!navic] Značení na cvičení
> Na cvičení a v testech se lineární zobrazení často značí malými písmeny ($f$, $g$) a obraz $f(\vec{x})$. Je to totéž jako $A\vec{x}$ z přednášky.

## §2 Značení a skládání zobrazení

U [[lineární zobrazení|lineárních zobrazení]] se závorky kolem argumentu vynechávají: $A\vec{x} = A(\vec{x})$, podobně jako se u násobení píše $2x$ místo $2 \cdot x$. Důvod uvidíme v §6: $A\vec{x}$ bude doslova součin matice a vektoru.

> [!definice] Definice · složené zobrazení · kap. 6.2
> Pro zobrazení $A : U \to V$ a $B : V \to W$ píšeme
>
> $$
> BA\vec{x} = B(A\vec{x}), \qquad BA = B \circ A,
> $$
>
> tj. $BA : U \to W$ je *složené zobrazení* „nejdřív $A$, potom $B$“. Je to totéž jako u funkcí: $g(f(x)) = (g \circ f)(x)$. Zápisy $(BA)(\vec{x})$, $(BA)\vec{x}$, $BA\vec{x}$ a $B(A\vec{x})$ znamenají totéž.

^def-slozene-zobrazeni

> [!lidsky] Lidsky
> Skládání je výrobní linka: vektor projde napřed strojem $A$ a jeho výstup pak strojem $B$. Čte se **zprava doleva**, jako $g(f(x))$: blíž k $\vec{x}$ je ten, kdo jde na řadu první. Linka dává smysl, jen když výstup $A$ padá do prostoru, který $B$ umí zpracovat.

> [!obrazek] Skládání zobrazení
> ![[lag07-skladani.png]]
> *Modrá šipka: $A$ pošle $\vec{x} \in U$ na $A\vec{x} \in V$. Oranžová: $B$ pošle $A\vec{x}$ dál do $W$. Zelený oblouk: složené zobrazení $BA$ udělá obojí najednou.*

> [!pozor] Pořadí ve složení
> $BA$ znamená **nejdřív $A$**, i když se $A$ píše až druhé. Obecně $BA \ne AB$ (příklad v §4), a jsou-li prostory různé, druhé složení často ani nedává smysl: pro $A : \mathbb{R}^3 \to \mathbb{R}^2$ a $B : \mathbb{R}^2 \to \mathbb{R}$ existuje $BA$, ale $AB$ ne.

> [!veta] Věta (asociativita skládání)
> ==Pro zobrazení $A : U \to V$, $B : V \to W$, $C : W \to Z$== platí **$C(BA) = (CB)A$**.
>
> > [!note]- Důkaz
> > Obě strany jsou zobrazení $U \to Z$, stačí ukázat, že dají totéž v každém bodě. Ve funkčním zápisu:
> >
> > $$
> > \big(h \circ (g \circ f)\big)(x) = h\big((g \circ f)(x)\big) = h\big(g(f(x))\big), \qquad \big((h \circ g) \circ f\big)(x) = (h \circ g)\big(f(x)\big) = h\big(g(f(x))\big).
> > $$
> >
> > Obě strany jsou „nejdřív $f$, pak $g$, pak $h$“.

^veta-asociativita

> [!lidsky] Lidsky
> U výrobní linky se třemi stroji je jedno, jestli si první dva stroje (nebo poslední dva) představíš jako jeden větší stroj. Vektor stejně projde $A$, pak $B$, pak $C$. Proto se závorky vynechávají a píše se $CBA$. Linearita k tomu není potřeba, platí to pro jakákoli zobrazení.

> [!navic] Složení lineárních zobrazení je lineární
> Jsou-li $A \in \operatorname{Lin}(U, V)$ a $B \in \operatorname{Lin}(V, W)$, je [[složené zobrazení]] $BA \in \operatorname{Lin}(U, W)$:
>
> $$
> BA(\vec{x} + \vec{y}) = B(A\vec{x} + A\vec{y}) = BA\vec{x} + BA\vec{y}, \qquad BA(\alpha\vec{x}) = B(\alpha A\vec{x}) = \alpha BA\vec{x}.
> $$
>
> V obou rovnostech se nejdřív použila linearita $A$ a pak linearita $B$. O skládání a jeho vztahu k násobení matic je kap. 6.2.

## §3 Základní vlastnosti

> [!veta] Tvrzení (obraz nulového vektoru)
> ==Pro libovolné $A \in \operatorname{Lin}(V, W)$== je **$A(\vec{o}_V) = \vec{o}_W$**.
>
> > [!note]- Důkaz
> > Vezmi libovolné $\vec{x} \in V$. Protože $0 \cdot \vec{x} = \vec{o}_V$ ([[věta o vlastnostech lineárního prostoru]]), z homogenity
> >
> > $$
> > A(\vec{o}_V) = A(0 \cdot \vec{x}) = 0 \cdot A(\vec{x}) = \vec{o}_W.
> > $$

^veta-obraz-nuly

> [!lidsky] Lidsky
> [[lineární zobrazení|Lineární zobrazení]] vždycky nechá počátek na místě (u $V \to W$ přesněji: pošle nulu na nulu). Je to nejrychlejší test: když $f(\vec{o}) \ne \vec{o}$, zobrazení **lineární není** a nic dalšího se počítat nemusí. Obráceně to ale nefunguje: z $f(\vec{o}) = \vec{o}$ linearita neplyne.

> [!veta] Tvrzení (kritérium linearity)
> ==$A : V \to W$== je lineární, právě když
>
> $$
> (\forall \vec{x}, \vec{y} \in V)(\forall \alpha \in \mathbb{F})\ \big(A(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y}\big).
> $$
>
> > [!note]- Důkaz
> > **$\Rightarrow$:** Z aditivity a pak homogenity: $A(\alpha\vec{x} + \vec{y}) = A(\alpha\vec{x}) + A\vec{y} = \alpha A\vec{x} + A\vec{y}$.
> >
> > **$\Leftarrow$:** Volbou $\alpha = 1$ dostaneme $A(\vec{x} + \vec{y}) = A\vec{x} + A\vec{y}$, tedy aditivitu. Odtud $A\vec{o} = A(\vec{o} + \vec{o}) = A\vec{o} + A\vec{o}$, a přičtením $-A\vec{o}$ k oběma stranám $A\vec{o} = \vec{o}$. Volbou $\vec{y} = \vec{o}$ pak
> >
> > $$
> > A(\alpha\vec{x}) = A(\alpha\vec{x} + \vec{o}) = \alpha A\vec{x} + A\vec{o} = \alpha A\vec{x},
> > $$
> >
> > tedy homogenitu.

^veta-kriterium-linearity

> [!lidsky] Lidsky
> Místo dvou podmínek stačí ověřit jednu „smíšenou“. V testu to ušetří půlku psaní: stačí jeden výpočet $A(\alpha\vec{x} + \vec{y})$.

> [!pozor] Kruh v důkazu
> Ve směru $\Leftarrow$ ještě nevíme, že $A$ je lineární, takže nesmíme použít tvrzení $A\vec{o} = \vec{o}$ z předchozí věty (to linearitu předpokládá). Rovnost $A\vec{o} = \vec{o}$ je potřeba dokázat znovu, tady z už odvozené aditivity. Typická chyba v písemných důkazech: použít to, co se teprve dokazuje.

> [!veta] Tvrzení (zachování lineárních kombinací)
> ==$A : V \to W$== je lineární, právě když pro všechna $n \in \mathbb{N}_0$, $\alpha_1, \dots, \alpha_n \in \mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in V$ platí
>
> $$
> \mathbf{A(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n) = \alpha_1 A\vec{x}_1 + \dots + \alpha_n A\vec{x}_n.}
> $$
>
> > [!note]- Důkaz
> > **$\Leftarrow$:** Volba $n = 2$, $\alpha_1 = \alpha$, $\alpha_2 = 1$ dá $A(\alpha\vec{x}_1 + \vec{x}_2) = \alpha A\vec{x}_1 + A\vec{x}_2$, a to je [[kritérium linearity]].
> >
> > **$\Rightarrow$:** Indukcí podle $n$. Pro $n = 0$ je vlevo i vpravo prázdný součet, tedy nulový vektor, a $A\vec{o} = \vec{o}$ platí podle tvrzení výše. Pro $n = 1$ je to homogenita $A(\alpha_1\vec{x}_1) = \alpha_1 A\vec{x}_1$. Předpokládejme, že tvrzení platí pro nějaké $n \in \mathbb{N}$, a dokažme ho pro $n + 1$. Kombinaci rozdělíme na prvních $n$ členů a poslední:
> >
> > $$
> > A\big((\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n) + \alpha_{n+1}\vec{x}_{n+1}\big) = A(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n) + A(\alpha_{n+1}\vec{x}_{n+1}) = \alpha_1 A\vec{x}_1 + \dots + \alpha_n A\vec{x}_n + \alpha_{n+1}A\vec{x}_{n+1}.
> > $$
> >
> > První rovnost je aditivita, druhá indukční předpoklad a homogenita.

^veta-zachovani-kombinaci

> [!lidsky] Lidsky
> Lineární zobrazení respektuje „recepty“: obraz směsi je stejná směs obrazů. Když víš, kam jdou ingredience $\vec{x}_1, \dots, \vec{x}_n$, víš, kam jde každá jejich [[lineární kombinace]]. Na tom stojí celá §6: v $\mathbb{F}^n$ je každý vektor kombinací $\vec{e}_1, \dots, \vec{e}_n$, takže stačí znát $n$ obrazů $A\vec{e}_i$.

> [!example] Cvičení: totéž pro podprostory
> Stejným postupem (jedna smíšená podmínka, indukce) se dokáže, že pro $V \subseteq L$ jsou ekvivalentní:
>
> 1. $V \le L$ ($V$ je [[lineární podprostor]]),
> 2. $V \ne \emptyset$ a $(\forall \alpha \in \mathbb{F})(\forall \vec{x}, \vec{y} \in V)\ (\alpha\vec{x} + \vec{y} \in V)$,
> 3. $(\forall n \in \mathbb{N}_0)(\forall \alpha_1, \dots, \alpha_n \in \mathbb{F})(\forall \vec{x}_1, \dots, \vec{x}_n \in V)\ (\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n \in V)$.
>
> Neprázdnost ve 2 je nutná: prázdná množina splňuje uzavřenost „naprázdno“, a podprostor to není. Ve 3 se neprázdnost schovává v případu $n = 0$: prázdná kombinace je $\vec{o}$, takže $\vec{o} \in V$.

## §4 Příklady

> [!definice] Definice · nulové a identické zobrazení · kap. 6.1
> - *Nulové zobrazení* $O : V \to W$, $O(\vec{x}) = \vec{o}$, je lineární: $O(\vec{x} + \vec{y}) = \vec{o} = \vec{o} + \vec{o} = O\vec{x} + O\vec{y}$ a $O(\alpha\vec{x}) = \vec{o} = \alpha\vec{o} = \alpha O\vec{x}$.
> - *Identické zobrazení* $\operatorname{id} : V \to V$, $\operatorname{id}(\vec{x}) = \vec{x}$, je lineární: obě podmínky jsou rovnou $\vec{x} + \vec{y} = \vec{x} + \vec{y}$ a $\alpha\vec{x} = \alpha\vec{x}$.

^def-nulove-identicke

> [!lidsky] Lidsky
> Nulové zobrazení je „černá díra“: všechno spolkne do počátku. Identita je „nedělej nic“. Obě jsou nudné, ale při skládání hrají roli jedničky a nuly: $A\operatorname{id} = \operatorname{id}A = A$ a složení s nulovým zobrazením dá zase nulové zobrazení.

### Lineární funkce na $\mathbb{R}$

> [!pozor] „Lineární funkce“ ze školy není lineární zobrazení
> Funkce $f : \mathbb{R} \to \mathbb{R}$, $f(x) = kx + q$ **není** lineární, ledaže $q = 0$. Pro $q \ne 0$ je $f(0) = q \ne 0$, a to podle [[věta o obrazu nulového vektoru|věty o obrazu nuly]] lineární zobrazení nedovolí. Školní „lineární funkce“ se správně jmenuje *afinní*; lineární jsou jen přímky **přes počátek**.

> [!obrazek] Lineární a afinní funkce
> ![[lag07-afinni.png]]
> *Modrá $f(x) = 2x$ prochází počátkem a je lineární. Červená $g(x) = 2x + 1$ je jen posunutá: $g(0) = 1 \ne 0$ a i aditivita selže, $g(1) + g(1) = 6$, ale $g(1 + 1) = 5$.*

> [!veta] Tvrzení (lineární funkce $\mathbb{R} \to \mathbb{R}$)
> ==$f : \mathbb{R} \to \mathbb{R}$== je lineární, právě když **$f(x) = kx$ pro nějaké $k \in \mathbb{R}$**.
>
> > [!note]- Důkaz
> > **$\Leftarrow$:** je to stejnolehlost níže s $V = \mathbb{R}$.
> >
> > **$\Rightarrow$:** Polož $k = f(1)$. Pro každé $x \in \mathbb{R}$ je $x = x \cdot 1$ (číslo $x$ je skalár, $1$ je vektor), takže z homogenity $f(x) = f(x \cdot 1) = x f(1) = kx$.

^veta-linearni-funkce

> [!lidsky] Lidsky
> Lineární zobrazení $\mathbb{R} \to \mathbb{R}$ je úplně určené jediným číslem $k = f(1)$, „kam jde jednička“. Totéž ve větším: lineární zobrazení $\mathbb{F}^n \to \mathbb{F}^m$ je určené tím, kam jdou $\vec{e}_1, \dots, \vec{e}_n$ (§6). Číslo $k$ je jeho „matice $1 \times 1$“.

### Stejnolehlost

> [!definice] Definice · stejnolehlost · kap. 6.1
> Pro pevné $k \in \mathbb{F}$ je zobrazení $A : V \to V$, $A\vec{x} = k\vec{x}$, lineární. Nazývá se *stejnolehlost* (s koeficientem $k$).
>
> **Důkaz linearity:** $A(\vec{x} + \vec{y}) = k(\vec{x} + \vec{y}) = k\vec{x} + k\vec{y} = A\vec{x} + A\vec{y}$ a $A(\alpha\vec{x}) = k\alpha\vec{x} = \alpha k\vec{x} = \alpha A\vec{x}$. V druhém výpočtu se použilo $k\alpha = \alpha k$, tedy komutativita násobení v tělese.

^def-stejnolehlost

> [!lidsky] Lidsky
> Stejnolehlost je kopírka se zoomem $k$: všechno zvětší $k$-krát se středem v počátku. Pro $k = 2$ je obrázek dvakrát větší, pro $k = -1$ se překlopí přes počátek (středová souměrnost), $k = 1$ je identita a $k = 0$ nulové zobrazení.

> [!obrazek] Stejnolehlost s koeficientem 1, 2 a −1
> ![[lag07-stejnolehlost.png]]
> *Modrý domeček je původní ($k = 1$), oranžový je jeho obraz pro $k = 2$, zelený pro $k = -1$ (otočený o 180° kolem počátku). Tečkované čáry ukazují, že se špička střechy posouvá po přímce přes počátek.*

### Zobrazení roviny $\mathbb{R}^2 \to \mathbb{R}^2$

| předpis | co dělá | obraz $\vec{e}_1$, $\vec{e}_2$ |
| --- | --- | --- |
| $A(x; y) = (-y; x)$ | otočení o $90°$ proti směru hodinových ručiček | $(0; 1)$, $(-1; 0)$ |
| $A(x; y) = (x; -y)$ | osová souměrnost podle osy $x$ | $(1; 0)$, $(0; -1)$ |
| $A(x; y) = (kx; y)$ | natažení $k$-krát ve směru osy $x$ | $(k; 0)$, $(0; 1)$ |
| $A(x; y) = (x + y; y)$ | zkosení podél osy $x$ | $(1; 0)$, $(1; 1)$ |
| $A(x; y) = (x; 0)$ | průmět (projekce) na osu $x$ | $(1; 0)$, $(0; 0)$ |

> [!obrazek] Pět lineárních zobrazení roviny na domečku
> ![[lag07-domecek.png]]
> *Modrý čárkovaný domeček je vzor, oranžový jeho obraz. Modrá šipka je obraz $\vec{e}_1$, zelená obraz $\vec{e}_2$. Přímky zůstávají přímkami a počátek zůstává na místě. U průmětu se celý domeček „zplacatí“ na úsečku na ose $x$.*

Linearitu otočení jde vidět i geometricky. Otočíš-li celý rovnoběžník ze šipek $\vec{x}$, $\vec{y}$, otočí se i jeho úhlopříčka $\vec{x} + \vec{y}$ a zůstane úhlopříčkou otočeného rovnoběžníku. To je přesně $A(\vec{x} + \vec{y}) = A\vec{x} + A\vec{y}$.

> [!obrazek] Otočení zachovává rovnoběžník
> ![[lag07-aditivita.png]]
> *Vlevo modré $\vec{x}$, oranžové $\vec{y}$ a zelený součet. Vpravo totéž otočené o $90°$: obraz součtu je součet obrazů.*

### Derivace a „integrál“ polynomů

Na $\mathbb{R}[x]$ (všechny reálné polynomy) jsou lineární i dvě zobrazení z analýzy:

$$
D(\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n) = \alpha_1 + 2\alpha_2 x + \dots + n\alpha_n x^{n-1},
$$

$$
S(\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n) = \alpha_0 x + \tfrac{1}{2}\alpha_1 x^2 + \dots + \tfrac{1}{n+1}\alpha_n x^{n+1}.
$$

$D$ je derivace, $S$ primitivní funkce s nulovou konstantou. Obě jsou lineární, protože pracují s každým koeficientem zvlášť a s každým lineárně: derivace součtu je součet derivací a konstanta se vytkne. Obě jsou [[lineární operátor|lineární operátory]] na $\mathbb{R}[x]$.

> [!navic] $DS = \operatorname{id}$, ale $SD \ne \operatorname{id}$
> Derivace primitivní funkce vrátí původní polynom: $DS(p) = p$ pro každé $p$, tedy $DS = \operatorname{id}$. Obráceně ne: $SD(1) = S(0) = 0 \ne 1$, protože derivace zapomene absolutní člen. Skládání tedy **není komutativní**, ani u operátorů na stejném prostoru. Totéž ukazují zobrazení roviny: otočení $A(x; y) = (-y; x)$ a souměrnost $B(x; y) = (x; -y)$ dají $BA(x; y) = (-y; -x)$, kdežto $AB(x; y) = (y; x)$.

## §5 Zobrazení zadané sloupci

Všechny příklady roviny výše vypadají stejně: každá složka obrazu je součet násobků $x$ a $y$. Obecně:

> [!veta] Tvrzení (zobrazení zadané sloupci) · kap. 6.1
> ==Buďte $\vec{a}_1, \dots, \vec{a}_n \in \mathbb{F}^m$.== Potom je zobrazení $A : \mathbb{F}^n \to \mathbb{F}^m$ dané předpisem
>
> $$
> A\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = x_1\vec{a}_1 + \dots + x_n\vec{a}_n
> $$
>
> **lineární**.
>
> > [!note]- Důkaz
> > **1)** Pro $(x_1; \dots; x_n), (y_1; \dots; y_n) \in \mathbb{F}^n$:
> >
> > $$
> > A\left(\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} + \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}\right) = A\begin{pmatrix} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{pmatrix} = (x_1 + y_1)\vec{a}_1 + \dots + (x_n + y_n)\vec{a}_n = x_1\vec{a}_1 + \dots + x_n\vec{a}_n + y_1\vec{a}_1 + \dots + y_n\vec{a}_n,
> > $$
> >
> > a to je $A(x_1; \dots; x_n) + A(y_1; \dots; y_n)$.
> >
> > **2)** Pro $\alpha \in \mathbb{F}$ a $(x_1; \dots; x_n) \in \mathbb{F}^n$:
> >
> > $$
> > A\left(\alpha\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}\right) = A\begin{pmatrix} \alpha x_1 \\ \vdots \\ \alpha x_n \end{pmatrix} = \alpha x_1\vec{a}_1 + \dots + \alpha x_n\vec{a}_n = \alpha(x_1\vec{a}_1 + \dots + x_n\vec{a}_n) = \alpha A\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.
> > $$
> >
> > Použili jsme jen axiomy v $\mathbb{F}^m$ (distributivitu, komutativitu a asociativitu sčítání).

^veta-zobrazeni-sloupci

> [!lidsky] Lidsky
> Zvol si $n$ „ingrediencí“ $\vec{a}_1, \dots, \vec{a}_n$. Zobrazení vezme sloupec čísel jako recept („kolik dávek čeho“) a vrátí hotovou směs. Takové zobrazení je vždycky lineární. Za chvíli uvidíme, že platí i opak: **každé** [[lineární zobrazení]] $\mathbb{F}^n \to \mathbb{F}^m$ vypadá právě takhle.

Sloupce $\vec{a}_1, \dots, \vec{a}_n$ se zapisují vedle sebe do [[matice]] a zobrazení se pak píše jako součin:

> [!definice] Definice · součin matice a vektoru
> Pro matici se sloupci $\vec{a}_1, \dots, \vec{a}_n \in \mathbb{F}^m$ a vektor $\vec{x} = (x_1; \dots; x_n) \in \mathbb{F}^n$ je
>
> $$
> (\vec{a}_1 \cdots \vec{a}_n)\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = x_1\vec{a}_1 + \dots + x_n\vec{a}_n \in \mathbb{F}^m.
> $$

^def-soucin-matice-vektoru

> [!lidsky] Lidsky
> Matice krát vektor = **lineární kombinace sloupců matice**, koeficienty jsou složky vektoru. Například
>
> $$
> \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = x\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + y\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} x + y \\ 2x \\ 3x + y \end{pmatrix}.
> $$
>
> Vektor musí mít tolik složek, kolik má matice sloupců. Výsledek má tolik složek, kolik má matice řádků.

> [!navic] Řádkově to vyjde stejně
> Ze školy (nebo z [[LAG 01 – Úvod do lineární algebry#Algebraicky a maticově|1. přednášky]]) znáš pravidlo „řádek krát sloupec“: $i$-tá složka výsledku je $a_{i1}x_1 + \dots + a_{in}x_n$. To je totéž číslo jako $i$-tá složka kombinace $x_1\vec{a}_1 + \dots + x_n\vec{a}_n$. Sloupcový pohled je ale užitečnější: říká, co zobrazení **dělá** (kam pošle $\vec{e}_i$).

## §6 Matice zobrazení v kanonické bázi

Teď opačný směr. Máme libovolné [[lineární zobrazení|lineární]] $A : \mathbb{F}^n \to \mathbb{F}^m$ a chceme ho zapsat maticí. Označme
$$
\vec{a}_i = A\vec{e}_i \quad (i = 1, \dots, n),
$$
kde $\vec{e}_1, \dots, \vec{e}_n$ je [[kanonická báze]] $\mathbb{F}^n$. Každý vektor je kombinací $\vec{e}_i$, takže podle [[věta o zachování lineárních kombinací|zachování lineárních kombinací]]

$$
A\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = A(x_1\vec{e}_1 + \dots + x_n\vec{e}_n) = x_1 A\vec{e}_1 + \dots + x_n A\vec{e}_n = x_1\vec{a}_1 + \dots + x_n\vec{a}_n = (\vec{a}_1 \cdots \vec{a}_n)\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.
$$

> [!definice] Definice · matice zobrazení v kanonické bázi · kap. 6.1
> Buď $A : \mathbb{F}^n \to \mathbb{F}^m$ lineární a $\vec{e}_1, \dots, \vec{e}_n$ kanonická báze $\mathbb{F}^n$. Matice
>
> $$
> (\vec{a}_1 \cdots \vec{a}_n) = (A\vec{e}_1 \cdots A\vec{e}_n) \in \mathbb{F}^{m \times n}
> $$
>
> se nazývá *matice zobrazení $A$* (v kanonické bázi). Pro každé $\vec{x} \in \mathbb{F}^n$ je $A\vec{x}$ součin této matice s $\vec{x}$.

^def-matice-zobrazeni

> [!lidsky] Lidsky
> **Sloupce matice jsou obrazy jednotkových vektorů.** Chceš matici zobrazení? Zjisti, kam jde $\vec{e}_1$, napiš to jako první sloupec, kam jde $\vec{e}_2$, to jako druhý, a tak dál. Lineární zobrazení $\mathbb{F}^n \to \mathbb{F}^m$ je tedy totéž co matice $m \times n$: každé matici patří zobrazení (§5) a každému zobrazení matice (tady).

> [!example] Zkosení
> $A : \mathbb{R}^2 \to \mathbb{R}^2$, $A(x; y) = (x + y; y)$. Obrazy jednotkových vektorů:
>
> $$
> A\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad A\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad\text{matice}\quad \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.
> $$
>
> Kontrola: $\begin{pmatrix} x \\ y \end{pmatrix} = x\begin{pmatrix} 1 \\ 0 \end{pmatrix} + y\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, takže
>
> $$
> A\begin{pmatrix} x \\ y \end{pmatrix} = xA\begin{pmatrix} 1 \\ 0 \end{pmatrix} + yA\begin{pmatrix} 0 \\ 1 \end{pmatrix} = x\begin{pmatrix} 1 \\ 0 \end{pmatrix} + y\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} x + y \\ y \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}.
> $$
>
> Je to přesně matice z 1. přednášky, která zkosila čtvercovou síť. Pro $f : \mathbb{R} \to \mathbb{R}$, $f(x) = kx$ je matice $1 \times 1$ prostě $(k)$.

> [!obrazek] Co zkosení udělá se sítí
> ![[lag07-mrizka.png]]
> *Vlevo kanonická síť s modrým $\vec{e}_1$, oranžovým $\vec{e}_2$ a zeleným vektorem $(2; 1) = 2\vec{e}_1 + \vec{e}_2$. Vpravo obrazy: síť se zkosí, $\vec{e}_1$ zůstane, $\vec{e}_2$ přejde na $(1; 1)$ a $(2; 1)$ přejde na $2\vec{a}_1 + \vec{a}_2 = (3; 1)$. Bod zůstane „2 kroky po prvním sloupci a 1 krok po druhém“, jen jsou kroky jiné.*

> [!navic] Kam to vede
> Matice zde patří ke kanonickým bázím. Na cvičení a v testu přijde obecnější *matice lineárního zobrazení vzhledem k bázím $\mathcal{B}$ a $\mathcal{C}$* (značení $[A]_{\mathcal{B} \to \mathcal{C}}$): do sloupců se místo $A\vec{e}_i$ píšou souřadnice $[A\vec{b}_i]^{\mathcal{C}}$. Skládání zobrazení pak odpovídá násobení matic (kap. 6.2).

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč musí být v definici lineárního zobrazení $A : V \to W$ oba prostory nad stejným tělesem?
> V podmínce $A(\alpha\vec{x}) = \alpha A\vec{x}$ násobí **totéž číslo** $\alpha$ vlevo vektor z $V$ a vpravo vektor z $W$. Musí to tedy být skalár obou prostorů.

> [!karta|02]- Jak dokážeš, že lineární zobrazení posílá nulový vektor na nulový?
> Pro libovolné $\vec{x} \in V$: $A\vec{o}_V = A(0 \cdot \vec{x}) = 0 \cdot A\vec{x} = \vec{o}_W$. Použije se **homogenita** a $0 \cdot \vec{v} = \vec{o}$.

> [!karta|03]- Jak z jediné podmínky $A(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y}$ odvodíš homogenitu?
> Nejdřív $\alpha = 1$ dá aditivitu, z ní $A\vec{o} = A\vec{o} + A\vec{o}$, tedy $A\vec{o} = \vec{o}$. Pak $\vec{y} = \vec{o}$: $A(\alpha\vec{x}) = \alpha A\vec{x} + A\vec{o} = \alpha A\vec{x}$. **Pozor:** $A\vec{o} = \vec{o}$ se tu musí dokázat znovu, linearita ještě není známa.

> [!karta|04]- Jak indukcí dokážeš, že lineární zobrazení zachovává lineární kombinace?
> $n = 0$: $A\vec{o} = \vec{o}$; $n = 1$: homogenita. Krok $n \to n + 1$: kombinaci rozděl na prvních $n$ členů a poslední, použij **aditivitu**, na první část **indukční předpoklad**, na poslední homogenitu.

> [!karta|05]- Proč $f(x) = kx + q$ s $q \ne 0$ není lineární zobrazení $\mathbb{R} \to \mathbb{R}$?
> $f(0) = q \ne 0$, ale lineární zobrazení musí poslat **nulu na nulu**. Školní „lineární funkce“ je afinní; lineární jsou jen přímky přes počátek.

> [!karta|06]- Proč je každé lineární $f : \mathbb{R} \to \mathbb{R}$ tvaru $f(x) = kx$?
> Polož $k = f(1)$. Pak z homogenity $f(x) = f(x \cdot 1) = x f(1) = kx$. Zobrazení je určené **obrazem jedničky**.

> [!karta|07]- V jakém pořadí se v $BA$ provádějí zobrazení a kdy složení $BA$ existuje?
> $BA\vec{x} = B(A\vec{x})$: **nejdřív $A$, potom $B$** (čte se zprava doleva jako $g(f(x))$). Existuje, když $A : U \to V$ a $B : V \to W$, tedy když obor hodnot $A$ leží v definičním oboru $B$. Výsledek je $BA : U \to W$.

> [!karta|08]- Proč platí $C(BA) = (CB)A$?
> Obě strany pošlou $\vec{x}$ na $C(B(A\vec{x}))$: **nejdřív $A$, pak $B$, pak $C$**. Platí to pro jakákoli zobrazení, linearita není potřeba. Proto se píše jen $CBA$.

> [!karta|09]- Jak dokážeš, že složení dvou lineárních zobrazení je lineární?
> $BA(\vec{x} + \vec{y}) = B(A\vec{x} + A\vec{y}) = BA\vec{x} + BA\vec{y}$ a $BA(\alpha\vec{x}) = B(\alpha A\vec{x}) = \alpha BA\vec{x}$. Vždy nejdřív **linearita $A$**, pak **linearita $B$**.

> [!karta|10]- Proč skládání zobrazení obecně není komutativní? Uveď příklad.
> Záleží na pořadí kroků. Derivace $D$ a „integrál“ $S$ na $\mathbb{R}[x]$: $DS = \operatorname{id}$, ale $SD(1) = S(0) = 0$, takže **$SD \ne DS$**. Nebo otočení a souměrnost roviny: $BA(x; y) = (-y; -x)$, $AB(x; y) = (y; x)$.

> [!karta|11]- Jak dokážeš aditivitu zobrazení $A(x_1; \dots; x_n) = x_1\vec{a}_1 + \dots + x_n\vec{a}_n$?
> $A(\vec{x} + \vec{y}) = (x_1 + y_1)\vec{a}_1 + \dots + (x_n + y_n)\vec{a}_n$; roznásob (**distributivita**) a přeskládej (komutativita, asociativita) na $x_1\vec{a}_1 + \dots + x_n\vec{a}_n + y_1\vec{a}_1 + \dots + y_n\vec{a}_n = A\vec{x} + A\vec{y}$.

> [!karta|12]- Proč je lineární zobrazení $A : \mathbb{F}^n \to \mathbb{F}^m$ úplně určené obrazy $A\vec{e}_1, \dots, A\vec{e}_n$?
> Každé $\vec{x} = x_1\vec{e}_1 + \dots + x_n\vec{e}_n$, a lineární zobrazení **zachovává lineární kombinace**: $A\vec{x} = x_1 A\vec{e}_1 + \dots + x_n A\vec{e}_n$. Stačí tedy znát $n$ vektorů $A\vec{e}_i$.

> [!karta|13]- Proč má matice lineárního zobrazení $\mathbb{F}^n \to \mathbb{F}^m$ rozměr $m \times n$, a ne $n \times m$?
> Sloupců je tolik, kolik je vektorů $\vec{e}_1, \dots, \vec{e}_n$, tedy **$n$ (dimenze vstupu)**. Každý sloupec $A\vec{e}_i$ leží v $\mathbb{F}^m$, takže má **$m$ složek (dimenze výstupu)**. Proto $m$ řádků a $n$ sloupců.

> [!karta|14]- Proč v podmínce „$V \le L$ ⟺ $(\forall \alpha)(\forall \vec{x}, \vec{y} \in V)\ (\alpha\vec{x} + \vec{y} \in V)$“ chybí předpoklad a který?
> **Neprázdnost** $V$. Prázdná množina splňuje uzavřenost naprázdno, ale podprostor to není (podprostor obsahuje $\vec{o}$). Ve verzi s $n \in \mathbb{N}_0$ to řeší případ $n = 0$: prázdná kombinace $\vec{o}$ musí ležet ve $V$.

### Příklady na procvičení

> [!priklad|15]- Dokaž podle kritéria linearity, že otočení $A(x; y) = (-y; x)$ je lineární.
> $A\big(\alpha(x_1; y_1) + (x_2; y_2)\big) = A(\alpha x_1 + x_2;\ \alpha y_1 + y_2) = (-\alpha y_1 - y_2;\ \alpha x_1 + x_2) = \alpha(-y_1; x_1) + (-y_2; x_2) = \alpha A(x_1; y_1) + A(x_2; y_2)$.
>
> **Je lineární.**

> [!priklad|16]- Urči matici zobrazení $A(x; y) = (x + y; y)$ v kanonické bázi a spočítej s ní $A(2; 3)$.
> $A\vec{e}_1 = (1; 0)$, $A\vec{e}_2 = (1; 1)$, matice **$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$**. $A(2; 3) = 2(1; 0) + 3(1; 1) = $ **$(5; 3)$**.

> [!priklad|17]- Spočítej $\begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix}$ jako kombinaci sloupců.
> $2(1; 2; 3) - 1 \cdot (1; 0; 1) = (2; 4; 6) - (1; 0; 1) = $ **$(1; 4; 5)$**.

> [!priklad|18]- Je $f : \mathbb{R} \to \mathbb{R}$, $f(x) = 3x + 2$ lineární?
> $f(0) = 2 \ne 0$, lineární zobrazení ale posílá nulu na nulu. **Není lineární.**

> [!priklad|19]- Urči matici otočení $A(x; y) = (-y; x)$, průmětu $P(x; y) = (x; 0)$ a stejnolehlosti $H(x; y) = (kx; ky)$ v kanonické bázi.
> Sloupce jsou obrazy $\vec{e}_1$, $\vec{e}_2$: otočení **$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$**, průmět **$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$**, stejnolehlost **$\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$**.

> [!priklad|20]- Spočítej $D(3 - 2x + 5x^3)$ a $S(1 + 4x)$ pro derivaci $D$ a „integrál“ $S$ na $\mathbb{R}[x]$.
> $D(3 - 2x + 5x^3) = $ **$-2 + 15x^2$**. $S(1 + 4x) = 1 \cdot x + \tfrac{1}{2} \cdot 4x^2 = $ **$x + 2x^2$**.

> [!priklad|21]- Pro $A(x; y) = (-y; x)$ a $B(x; y) = (x; -y)$ spočítej $BA(x; y)$ a $AB(x; y)$.
> $BA(x; y) = B(-y; x) = $ **$(-y; -x)$** (souměrnost podle přímky $y = -x$). $AB(x; y) = A(x; -y) = $ **$(y; x)$** (souměrnost podle $y = x$). Výsledky se liší.

> [!priklad|22]- Lineární $A : \mathbb{R}^2 \to \mathbb{R}^3$ splňuje $A(1; 0) = (1; 2; 3)$ a $A(0; 1) = (1; 0; 1)$. Urči $A(x; y)$.
> $A(x; y) = xA(1; 0) + yA(0; 1) = x(1; 2; 3) + y(1; 0; 1) = $ **$(x + y;\ 2x;\ 3x + y)$**, matice $\begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 3 & 1 \end{pmatrix}$.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|23]- Dokaž, že $g : \mathbb{R}^3 \to \mathbb{R}^2$, $g(x, y, z) = (2x + z,\ y - 3z)$ je lineární zobrazení.
> Buďte $\vec{u} = (u_1, u_2, u_3)$, $\vec{w} = (w_1, w_2, w_3) \in \mathbb{R}^3$ a $\alpha \in \mathbb{R}$. Podle kritéria linearity stačí jedna rovnost:
>
> $$
> g(\alpha\vec{u} + \vec{w}) = \big(2(\alpha u_1 + w_1) + (\alpha u_3 + w_3),\ (\alpha u_2 + w_2) - 3(\alpha u_3 + w_3)\big) = \alpha(2u_1 + u_3,\ u_2 - 3u_3) + (2w_1 + w_3,\ w_2 - 3w_3) = \alpha g(\vec{u}) + g(\vec{w}).
> $$
>
> **$g$ je lineární.** (Jinak: $g$ je zadané sloupci $(2; 0)$, $(0; 1)$, $(1; -3)$, tedy násobení maticí $\begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & -3 \end{pmatrix}$.)

> [!priklad|24]- Je $f : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $f(ax^2 + bx + c) = (a + 1)x^2 + bx + c$ lineární?
> Nulový polynom ($a = b = c = 0$) přejde na $f(0) = x^2 \ne 0$. Lineární zobrazení posílá nulový vektor na nulový. **Není lineární.**

> [!priklad|25]- Je $f : \mathbb{R}^{2 \times 2} \to \mathbb{R}$, $f\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad$ lineární?
> Protipříklad na homogenitu s jednotkovou maticí $I$: $f(2I) = 2 \cdot 2 = 4$, ale $2f(I) = 2 \cdot 1 = 2$. Přitom $f(\vec{o}) = 0$, takže test nulou tu nestačí. **Není lineární.**

> [!priklad|26]- Je $f : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $f(p)(x) = p(x + 1)$ lineární? Zapiš $f(ax^2 + bx + c)$.
> Pro $p, q$ a $\alpha \in \mathbb{R}$: $f(\alpha p + q)(x) = (\alpha p + q)(x + 1) = \alpha p(x + 1) + q(x + 1) = \alpha f(p)(x) + f(q)(x)$ pro každé $x$ (sčítání a násobení polynomů je po hodnotách). Stupeň se posunutím nezvětší, takže $f$ opravdu vede do $\mathbb{R}^{\le 2}[x]$. **Je lineární**; $f(ax^2 + bx + c) = a(x + 1)^2 + b(x + 1) + c = $ **$ax^2 + (2a + b)x + (a + b + c)$**.

> [!priklad|27]- Je $f : \mathbb{R}^2 \to \mathbb{R}^2$, $f(x, y) = (y, \lvert x \rvert)$ lineární?
> Protipříklad na homogenitu s $\alpha = -1$, $\vec{v} = (1, 0)$: $f(-\vec{v}) = f(-1, 0) = (0, 1)$, ale $-f(\vec{v}) = -(0, 1) = (0, -1)$. **Není lineární**, i když $f(0, 0) = (0, 0)$.

---
← [[LAG 06 – Souřadnice, součet a průnik podprostorů|9. 10. 2026 Souřadnice, součet a průnik podprostorů]] · [[LAG 08 – Matice lineárního zobrazení a součin matic|16. 10. 2026 Matice lineárního zobrazení a součin matic]] →

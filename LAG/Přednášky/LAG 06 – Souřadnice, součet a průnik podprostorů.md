---
predmet: LAG
prednaska: 6
datum: 2026-10-09
zdroj: "V poznámkách kap. 4.2 (souřadnice) a kap. 5 (součet a průnik)"
tags: [prednaska, LAG]
---

# LAG 06 – Souřadnice, součet a průnik podprostorů

*Přednáška 6 · pátek 9. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `dimenze podprostoru` · `souřadnice` · `souřadnicový vektor` · `linearita souřadnic` · `průnik podprostorů` · `součet podprostorů` · `obal sjednocení` · `dimenze součtu a průniku`

Minule jsme zavedli [[báze|bázi]] a [[dimenze|dimenzi]]. Dnes z báze vyrobíme [[souřadnice]]: každý vektor libovolného prostoru dimenze $n$ jde popsat $n$ čísly, a hlavně se s těmi čísly dá počítat místo s vektory samotnými. Ve druhé části dvěma podprostorům přiřadíme jejich průnik a součet, obdobu průniku a sjednocení množin, a uvidíme, že dimenze se u nich chovají jako počty prvků u množin.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[věta o dimenzi podprostoru]] | $V \le L \Rightarrow \dim V \le \dim L$; při $\dim L < \infty$: $V = L \iff \dim V = \dim L$ | rovina v $\mathbb{R}^3$: $2 < 3$ |
| [[souřadnice]] | $\vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$, čísla $\alpha_i$ jsou jednoznačná, protože $\mathcal{X}$ je báze | $(3; 2) = 1 \cdot (1; 0) + 2 \cdot (1; 1)$ |
| [[souřadnicový vektor]] | $[\vec{v}]^{\mathcal{X}} = (\alpha_1; \dots; \alpha_n) \in \mathbb{F}^n$ | $[(3; 2)]^{\mathcal{E}} = (3; 2)$ |
| [[věta o linearitě souřadnic]] | $[\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$, $[\gamma\vec{x}]^{\mathcal{X}} = \gamma[\vec{x}]^{\mathcal{X}}$ | s polynomy lze počítat jako se sloupci |
| [[průnik podprostorů]] | $V \cap W$ je zase podprostor | dvě roviny v $\mathbb{R}^3$ $\to$ přímka |
| [[součet podprostorů]] | $V + W = \{\vec{v} + \vec{w} \mid \vec{v} \in V, \vec{w} \in W\}$, nejmenší podprostor obsahující $V$ i $W$ | dvě přímky $\to$ rovina |
| [[věta o součtu obalů]] | $\operatorname{span} M + \operatorname{span} N = \operatorname{span}(M \cup N)$: generátory se sjednotí | |
| [[věta o dimenzi součtu a průniku]] | $\dim(V + W) + \dim(V \cap W) = \dim V + \dim W$ | $2 + 2 = 3 + 1$ |

## §1 Dimenze podprostoru (dokončení)

Přednáška začala dokončením [[LAG 05 – Báze a dimenze#^veta-dim-podprostoru|věty o dimenzi podprostoru]]: je-li $\dim L = n < \infty$ a $V \le L$, pak $\dim V \le n$, a rovnost nastane jen pro $V = L$. Myšlenka důkazu ve třech krocích:

1. Každá LN posloupnost ve $V$ je LN i v $L$, takže má nejvýš $n$ prvků ([[Steinitzova věta]]). Proto má i $V$ konečnou dimenzi $k$ a bázi $(\vec{x}_1, \dots, \vec{x}_k)$.
2. Tuhle bázi jde podle [[věta o doplnění na bázi|věty o doplnění]] doplnit na bázi $L$, takže $n \ge k$.
3. Je-li $k = n$, nic se nedoplnilo: $(\vec{x}_1, \dots, \vec{x}_k)$ je báze $L$, a tedy $L = \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_k\} = V$.

> [!pozor] Bez konečné dimenze druhá část neplatí
> V nekonečně rozměrném prostoru může mít vlastní podprostor stejnou (nekonečnou) dimenzi. Polynomy bez absolutního členu tvoří podprostor $\mathbb{F}[x]$, oba mají dimenzi $\infty$, a přece $1$ v tom podprostoru není.

## §2 Souřadnice

Na první přednášce jsme vektoru $(3; 2)$ v rovině přiřadili návod „tři kroky doprava a dva nahoru“. Ty kroky jsou vektory [[kanonická báze|kanonické báze]] a čísla $3, 2$ jsou koeficienty lineární kombinace. Teď už víme, proč to jde s **libovolnou** bází: aby se dal zapsat každý vektor, posloupnost musí [[generující posloupnost|generovat]], a aby zápis byl jediný, musí být [[lineární nezávislost|LN]] ([[věta o jednoznačnosti vyjádření|věta 4.2]]). Obojí dohromady je přesně báze.

> [!definice] Definice · souřadnice
> Buď $L$ lineární prostor nad tělesem $\mathbb{F}$, $n \in \mathbb{N}$, nechť $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ je báze $L$ a $\vec{v} \in L$. Potom (jednoznačně určené) koeficienty $\alpha_1, \dots, \alpha_n \in \mathbb{F}$ lineární kombinace
>
> $$
> \vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n
> $$
>
> nazýváme *souřadnice vektoru $\vec{v}$ v bázi $\mathcal{X}$*. Číslo $\alpha_i$ nazýváme *$i$-tá souřadnice* a značíme $[\vec{v}]^{\mathcal{X}}_i = \alpha_i$.

^def-souradnice

> [!lidsky] Lidsky
> Báze je sada „směrů kroků“ a souřadnice jsou počty kroků v jednotlivých směrech. Každý vektor má v dané bázi jediný takový recept. Souřadnice jsou **čísla** z $\mathbb{F}$, ne vektory. Vektor $\vec{v}$ přitom může být cokoli (polynom, matice, funkce), čísla jeho receptu jsou vždycky obyčejná čísla.

Z definice je vidět i jedna drobnost: existuje-li báze s $n$ prvky, je $\dim L = n$ konečná. Souřadnice v tomhle smyslu má tedy jen prostor konečné dimenze.

> [!definice] Definice · souřadnicový vektor
> Za předpokladů předchozí definice nazýváme sloupcový vektor
>
> $$
> [\vec{v}]^{\mathcal{X}} = \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_n \end{pmatrix} \in \mathbb{F}^n
> $$
>
> *souřadnicový vektor* vektoru $\vec{v}$ v bázi $\mathcal{X}$.

^def-souradnicovy-vektor

> [!lidsky] Lidsky
> Souřadnice se jen napíšou pod sebe do sloupce. Z vektoru „čehokoli“ tím vznikne obyčejný sloupec $n$ čísel, se kterým umíme počítat. Index nahoře ($\mathcal{X}$) říká, ve které bázi, index dole ($i$) kterou složku chceme.

> [!pozor] Souřadnice závisí na bázi
> Bez báze nemá zápis $[\vec{v}]$ smysl. Tentýž vektor $(3; 2) \in \mathbb{R}^2$ má v kanonické bázi souřadnice $(3; 2)$, v bázi $((1; 0), (1; 1))$ souřadnice $(1; 2)$ a v bázi $((0; 1), (1; 0))$ souřadnice $(2; 3)$. Proto se index báze píše vždy.

> [!navic] Sloupce v kanonické bázi
> Pro $\vec{v} = (v_1; \dots; v_n) \in \mathbb{F}^n$ platí $\vec{v} = v_1\vec{e}_1 + \dots + v_n\vec{e}_n$, takže $[\vec{v}]^{\mathcal{E}} = \vec{v}$. Proto jsme u sloupců rozdíl mezi vektorem a jeho souřadnicemi doteď nevnímali: v kanonické bázi jsou to totéž. U polynomů nebo funkcí už rozdíl vidět je.

### Příklad: souřadnice v rovině uvnitř $\mathbb{R}^3$

Z [[LAG 05 – Báze a dimenze#§7 Výběr báze z generátorů|minula]] známe

$$
V = \operatorname{span}\left\{\vec{x}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \vec{x}_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \vec{x}_3 = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}\right\} \le \mathbb{R}^3,
$$

kde $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$, takže $\mathcal{X} = (\vec{x}_1, \vec{x}_2)$ je báze $V$ a $\dim V = 2$. Souřadnice v bázi $\mathcal{X}$:

$$
\vec{x}_1 = 1\vec{x}_1 + 0\vec{x}_2,\quad \vec{x}_2 = 0\vec{x}_1 + 1\vec{x}_2,\quad \vec{x}_3 = 1\vec{x}_1 + 1\vec{x}_2
\quad\Longrightarrow\quad
[\vec{x}_1]^{\mathcal{X}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\ [\vec{x}_2]^{\mathcal{X}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix},\ [\vec{x}_3]^{\mathcal{X}} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$

Vektory $V$ mají tři složky, ale souřadnice jen **dvě**, protože $V$ je rovina. Je to jako na zeměkouli: polohu na povrchu popisuješ dvěma čísly (šířkou a délkou), ne třemi souřadnicemi v prostoru.

> [!obrazek] Rovina $V$ a její vlastní souřadnicová síť
> ![[lag06-souradnice.png]]
> *Vlevo zelená rovina $V$ uvnitř $\mathbb{R}^3$ s modrým $\vec{x}_1$, oranžovým $\vec{x}_2$ a červeným čárkovaným $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$. Vpravo tatáž rovina „položená na papír“: síť tvoří kroky ve směru $\vec{x}_1$ a $\vec{x}_2$ a každý bod má dvě souřadnice, např. černý bod $(1; 3; 2) = \vec{x}_1 + 2\vec{x}_2$ má souřadnice $(1; 2)$.*

> [!example] Příklad: polynom jako sloupec
> V $\mathbb{R}^{\le 2}[x]$ s bází $\mathcal{B} = (1, x, x^2)$ je $[2 + 3x - x^2]^{\mathcal{B}} = (2; 3; -1)$. V jiné bázi $\mathcal{C} = (1, 1 + x, x^2)$ hledáme $a, b, c$ s $2 + 3x - x^2 = a \cdot 1 + b(1 + x) + cx^2$. Porovnáním koeficientů: u $x^2$ je $c = -1$, u $x$ je $b = 3$, u $1$ je $a + b = 2$, tedy $a = -1$. Proto $[2 + 3x - x^2]^{\mathcal{C}} = (-1; 3; -1)$.

## §3 Proč jsou souřadnice užitečné: linearita

Přiřazení $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$ je vzájemně jednoznačné (bijekce) mezi $L$ a $\mathbb{F}^n$: každý vektor má jediný souřadnicový vektor a každý sloupec $(\alpha_1; \dots; \alpha_n)$ patří vektoru $\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$. To samo o sobě ale moc neznamená.

> [!navic] Samotná bijekce nestačí
> Bijekce existuje i mezi $\mathbb{R}$ a $\mathbb{R}^2$: dvojici čísel jde zakódovat do jednoho čísla prokládáním číslic (až na technické detaily s rozvoji končícími samými devítkami), např. $(157{,}24;\ 34{,}18)$ dá (po doplnění na stejný počet číslic $157{,}24$ a $034{,}18$) číslo $105374{,}2148$. Existuje dokonce spojité zobrazení úsečky **na** celý čtverec, Hilbertova křivka (spojité a zároveň prosté takové zobrazení ale neexistuje). Kdyby stačila bijekce, byly by všechny prostory „stejné“ a dimenze by nic neznamenala. Souřadnice jsou cenné tím, že se **zachovávají operace**: s čísly $[\vec{v}]^{\mathcal{X}}$ jde počítat místo s vektory. Prokládání číslic tohle nesplňuje, sčítání by se v něm rozbilo kvůli přenosům mezi řády.

> [!veta] Věta (linearita souřadnic)
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ báze $L$.== Potom
>
> 1. **$(\forall \vec{x}, \vec{y} \in L)\ \ [\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$,**
> 2. **$(\forall \gamma \in \mathbb{F})(\forall \vec{x} \in L)\ \ [\gamma\vec{x}]^{\mathcal{X}} = \gamma[\vec{x}]^{\mathcal{X}}$.**
>
> > [!note]- Důkaz
> > **1)** Označme $[\vec{x}]^{\mathcal{X}} = (\alpha_1; \dots; \alpha_n)$ a $[\vec{y}]^{\mathcal{X}} = (\beta_1; \dots; \beta_n)$, tj. $\vec{x} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$ a $\vec{y} = \beta_1\vec{x}_1 + \dots + \beta_n\vec{x}_n$. Sečteme, přerovnáme (komutativita a asociativita) a vytkneme (distributivita):
> >
> > $$
> > \vec{x} + \vec{y} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n + \beta_1\vec{x}_1 + \dots + \beta_n\vec{x}_n = (\alpha_1 + \beta_1)\vec{x}_1 + \dots + (\alpha_n + \beta_n)\vec{x}_n.
> > $$
> >
> > Souřadnice jsou jednoznačné, takže
> >
> > $$
> > [\vec{x} + \vec{y}]^{\mathcal{X}} = \begin{pmatrix} \alpha_1 + \beta_1 \\ \vdots \\ \alpha_n + \beta_n \end{pmatrix} = \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_n \end{pmatrix} + \begin{pmatrix} \beta_1 \\ \vdots \\ \beta_n \end{pmatrix} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}.
> > $$
> >
> > **2)** Označme $[\vec{x}]^{\mathcal{X}}_i = \alpha_i$, tj. $\vec{x} = \sum_{i=1}^n \alpha_i\vec{x}_i$. Pak
> >
> > $$
> > \gamma\vec{x} = \gamma\sum_{i=1}^n \alpha_i\vec{x}_i = \sum_{i=1}^n (\gamma\alpha_i)\vec{x}_i,
> > $$
> >
> > takže $[\gamma\vec{x}]^{\mathcal{X}}_i = \gamma\alpha_i = \gamma[\vec{x}]^{\mathcal{X}}_i = \big[\gamma[\vec{x}]^{\mathcal{X}}\big]_i$ pro každé $i$ (poslední rovnost je definice násobení sloupce číslem po složkách). Sloupce se shodují ve všech složkách, tedy $[\gamma\vec{x}]^{\mathcal{X}} = \gamma[\vec{x}]^{\mathcal{X}}$.

^veta-linearita-souradnic

> [!lidsky] Lidsky
> Je jedno, jestli nejdřív sečteš vektory a pak se podíváš na souřadnice, nebo nejdřív vezmeš souřadnice a sečteš je. V příkladu z §2: $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$, a opravdu $[\vec{x}_3]^{\mathcal{X}} = (1; 0) + (0; 1) = (1; 1)$. Prakticky to znamená, že úlohu o polynomech nebo maticích přeložíš do sloupců čísel, vyřešíš ji tam a výsledek přeložíš zpět.

> [!pozor] Dvě různá plus
> V rovnosti $[\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$ jsou dvě **různé** operace. Vlevo je sčítání v $L$ (třeba polynomů), $+ : L \times L \to L$. Vpravo je sčítání sloupců po složkách, $+ : \mathbb{F}^n \times \mathbb{F}^n \to \mathbb{F}^n$. Totéž platí pro násobení číslem.

> [!navic] Síla věty
> O $L$ jsme nepředpokládali nic kromě [[axiomy lineárního prostoru|axiomů]] a existence báze. Důkaz tedy funguje pro polynomy, matice, funkce i cokoli dalšího. Zobrazení $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$ je bijekce $L \to \mathbb{F}^n$, která zachovává sčítání i násobení, tedy [[izomorfismus]]. Každý prostor dimenze $n$ nad $\mathbb{F}$ je tak „převlečené“ $\mathbb{F}^n$. Zobrazení, která zachovávají operace (lineární zobrazení), budou téma příštích přednášek.

> [!question]- Platí $[\vec{x} - \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} - [\vec{y}]^{\mathcal{X}}$?
> Ano: $\vec{x} - \vec{y} = \vec{x} + (-1)\vec{y}$, takže podle obou bodů věty $[\vec{x} - \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + (-1)[\vec{y}]^{\mathcal{X}}$. Obecně se tak přenáší každá lineární kombinace.

## §4 Průnik podprostorů

Pro množiny známe dvě základní operace, sjednocení a průnik, a pro konečné množiny vztah mezi počty prvků. Zkusíme totéž s podprostory, kde roli „počtu prvků“ hraje dimenze.

> [!definice] Připomenutí · sjednocení a průnik množin
> Pro množiny $A, B$ je
>
> $$
> A \cup B = \{x \mid x \in A \lor x \in B\}, \qquad A \cap B = \{x \mid x \in A \land x \in B\}.
> $$
>
> Pro [[lineární podprostor|podprostory]] $V, W \le L$ nazýváme $V \cap W$ *průnik podprostorů*.

^def-prunik

Pro konečné množiny platí $\vert A \cup B\vert = \vert A\vert + \vert B\vert - \vert A \cap B\vert$, protože prvky průniku se v $\vert A\vert + \vert B\vert$ započítají dvakrát. Například pro $\vert A\vert = \vert B\vert = 5$ a $\vert A \cap B\vert = 2$ je $\vert A \cup B\vert = 5 + 5 - 2 = 8$.

> [!veta] Věta (průnik podprostorů)
> ==Buď $L$ lineární prostor a $V, W \le L$.== Potom **$V \cap W \le L$**.
>
> > [!note]- Důkaz
> > Ověříme tři podmínky z definice podprostoru.
> >
> > **0) Neprázdnost:** $\vec{0} \in V$ a $\vec{0} \in W$ (každý podprostor obsahuje nulu, [[věta o podprostoru|věta 2.2]]), takže $\vec{0} \in V \cap W \neq \emptyset$.
> >
> > **1) Sčítání:** Buďte $\vec{x}, \vec{y} \in V \cap W$. Chceme $\vec{x} + \vec{y} \in V \cap W$. Z definice průniku $\vec{x}, \vec{y} \in V$ a zároveň $\vec{x}, \vec{y} \in W$. $V$ je podprostor, tedy $\vec{x} + \vec{y} \in V$; $W$ je podprostor, tedy $\vec{x} + \vec{y} \in W$. Dohromady $\vec{x} + \vec{y} \in V \cap W$.
> >
> > **2) Násobení:** stejně. Pro $\alpha \in \mathbb{F}$ a $\vec{x} \in V \cap W$ je $\alpha\vec{x} \in V$ i $\alpha\vec{x} \in W$, tedy $\alpha\vec{x} \in V \cap W$.

^veta-prunik

> [!lidsky] Lidsky
> Co se nedá opustit sčítáním ani násobením ve $V$ a zároveň ve $W$, nedá se opustit ani v jejich společné části. Dvě roviny procházející počátkem v $\mathbb{R}^3$ se protnou v přímce (nebo splývají), dvě různé přímky přes počátek jen v bodě $\vec{0}$.

> [!pozor] Průnik podprostorů není nikdy prázdný
> Každý podprostor obsahuje $\vec{0}$, takže $V \cap W \ni \vec{0}$. Roli „prázdného průniku“ u množin hraje [[triviální podprostor]] $\{\vec{0}\}$ s dimenzí $0$. (Roviny, které se neprotínají, uvidíme až v afinní geometrii na konci semestru, kde roviny nemusí procházet počátkem.)

## §5 Součet podprostorů

Sjednocení podprostorů obecně podprostor **není**. Dvě přímky $V = \operatorname{span}\{\vec{x}\}$ a $W = \operatorname{span}\{\vec{y}\}$ s různými směry: $\vec{x} \in V$, $\vec{y} \in W$, ale $\vec{x} + \vec{y}$ neleží ani na jedné z nich.

> [!obrazek] Sjednocení dvou přímek není podprostor
> ![[lag06-sjednoceni.png]]
> *Modrá přímka $V$ a oranžová $W$. Jejich sjednocení (kříž) není uzavřené na sčítání: červený čárkovaný součet $\vec{x} + \vec{y}$ z kříže vypadne. Nejmenší podprostor, který obsahuje oba, je celá rovina.*

Místo sjednocení proto vezmeme nejmenší podprostor, který obsahuje $V$ i $W$. Ten musí obsahovat všechny součty $\vec{v} + \vec{w}$, a ukáže se, že nic víc není potřeba.

> [!definice] Definice · součet podmnožin
> Buď $L$ lineární prostor a $A, B \subseteq L$. Definujeme
>
> $$
> A + B = \{\vec{a} + \vec{b} \mid \vec{a} \in A, \vec{b} \in B\}.
> $$
>
> Pro podprostory $V, W \le L$ nazýváme $V + W$ *součet podprostorů*.

^def-soucet

> [!lidsky] Lidsky
> Sečti každý prvek $A$ s každým prvkem $B$ a posbírej výsledky. Pro dvě přímky přes počátek s různými směry je to celá rovina, kterou určují: každý bod roviny je součet kroku po první přímce a kroku po druhé.

> [!veta] Věta (součet podprostorů)
> ==Buď $L$ lineární prostor a $V, W \le L$.== Potom **$V + W \le L$**.
>
> > [!note]- Důkaz
> > **0) Neprázdnost:** $\vec{0} \in V$, $\vec{0} \in W$, takže $\vec{0} = \vec{0} + \vec{0} \in V + W$.
> >
> > **1) Sčítání:** Buďte $\vec{x}, \vec{y} \in V + W$, tedy $\vec{x} = \vec{v} + \vec{w}$ a $\vec{y} = \vec{v}' + \vec{w}'$ pro nějaká $\vec{v}, \vec{v}' \in V$, $\vec{w}, \vec{w}' \in W$. Pak
> >
> > $$
> > \vec{x} + \vec{y} = (\vec{v} + \vec{v}') + (\vec{w} + \vec{w}'),
> > $$
> >
> > kde $\vec{v} + \vec{v}' \in V$ a $\vec{w} + \vec{w}' \in W$ (podprostory), takže $\vec{x} + \vec{y} \in V + W$.
> >
> > **2) Násobení:** Buď $\alpha \in \mathbb{F}$ a $\vec{x} \in V + W$, tj. existují $\vec{v} \in V$, $\vec{w} \in W$ s $\vec{x} = \vec{v} + \vec{w}$. Pak
> >
> > $$
> > \alpha\vec{x} = \alpha(\vec{v} + \vec{w}) = \underbrace{\alpha\vec{v}}_{\in V} + \underbrace{\alpha\vec{w}}_{\in W} \in V + W.
> > $$

^veta-soucet

> [!navic] $V + W$ je nejmenší podprostor obsahující $V$ i $W$
> Obsahuje oba: $\vec{v} = \vec{v} + \vec{0}$ a $\vec{w} = \vec{0} + \vec{w}$. A každý podprostor $U \supseteq V \cup W$ je uzavřený na sčítání, takže obsahuje všechny součty $\vec{v} + \vec{w}$, tedy $U \supseteq V + W$. Součet je proto pro podprostory přesně to, čím je sjednocení pro množiny, podobně jako [[lineární obal]] je nejmenší podprostor obsahující danou množinu.

> [!obrazek] Součet a průnik dvou přímek a dvou rovin
> ![[lag06-soucet.png]]
> *Vlevo modrá přímka $V$ a oranžová $W$ v $\mathbb{R}^3$: průnik je jen červený počátek, součet je zelená rovina. Vpravo modrá a oranžová rovina přes počátek: průnik je červená přímka, součet celé $\mathbb{R}^3$.*

### Generátory součtu a průniku

V praxi je podprostor skoro vždy zadaný generátory, třeba $V = \operatorname{span}\{\vec{x}_1, \vec{x}_2\}$. U součtu je to snadné.

> [!veta] Věta (součet obalů)
> ==Buď $L$ lineární prostor a $M, N \subseteq L$.== Potom
>
> $$
> \operatorname{span} M + \operatorname{span} N = \operatorname{span}(M \cup N).
> $$
>
> > [!note]- Důkaz
> > Stačí rozepsat obě strany podle definice.
> >
> > **⊆:** Prvek levé strany je $\vec{a} + \vec{b}$, kde $\vec{a}$ je lineární kombinace prvků $M$ a $\vec{b}$ lineární kombinace prvků $N$. Dohromady je to lineární kombinace prvků $M \cup N$.
> >
> > **⊇:** Lineární kombinaci prvků $M \cup N$ rozdělíme na členy s vektory z $M$ (to je $\vec{a} \in \operatorname{span} M$) a zbylé členy s vektory z $N$ (to je $\vec{b} \in \operatorname{span} N$). Vektor ležící v $M$ i $N$ přiřadíme k $M$. Prázdná část dá $\vec{0}$, který leží v každém obalu. Tedy kombinace $= \vec{a} + \vec{b} \in \operatorname{span} M + \operatorname{span} N$.

^veta-soucet-obalu

> [!lidsky] Lidsky
> Generátory součtu dostaneš tak, že **sjednotíš generátory** obou podprostorů. Rovina $\operatorname{span}\{\vec{x}_1, \vec{x}_2\}$ plus rovina $\operatorname{span}\{\vec{x}_3, \vec{x}_4\}$ je $\operatorname{span}\{\vec{x}_1, \vec{x}_2, \vec{x}_3, \vec{x}_4\}$.

> [!pozor] Sjednocení bází nemusí být báze součtu
> $(\vec{x}_1, \vec{x}_2, \vec{x}_3, \vec{x}_4)$ součet **generuje**, ale nemusí být LN, i když $(\vec{x}_1, \vec{x}_2)$ i $(\vec{x}_3, \vec{x}_4)$ LN jsou. Pro bázi součtu je potřeba přebytečné vektory vyhodit ([[věta o výběru báze]]).

> [!pozor] Průnik generátorů ≠ generátory průniku
> Pro průnik obdoba neplatí: obecně $\operatorname{span} M \cap \operatorname{span} N \neq \operatorname{span}(M \cap N)$. Dvě roviny v $\mathbb{R}^3$ mohou mít čtyři úplně různé generátory, žádný z nich neleží v průniku, a roviny se přesto protínají v přímce. Průnik se proto musí **spočítat** soustavou rovnic, viz příklad níže.

### Příklad: průnik a součet v $\mathbb{R}^4$

Najdi $V \cap W$ a $V + W$ pro $V = \operatorname{span}\{\vec{x}_1, \vec{x}_2\}$, $W = \operatorname{span}\{\vec{x}_3, \vec{x}_4\}$, kde

$$
\vec{x}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix},\quad
\vec{x}_2 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix},\quad
\vec{x}_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix},\quad
\vec{x}_4 = \begin{pmatrix} 0 \\ 1 \\ 1 \\ -1 \end{pmatrix}.
$$

**Součet:** podle věty o součtu obalů $V + W = \operatorname{span}\{\vec{x}_1, \vec{x}_2, \vec{x}_3, \vec{x}_4\}$.

**Průnik:** vypíšeme obecné prvky obou podprostorů:

$$
V = \left\{\alpha\vec{x}_1 + \beta\vec{x}_2 = \begin{pmatrix} \alpha \\ \alpha \\ \beta \\ 0 \end{pmatrix} \;\middle|\; \alpha, \beta \in \mathbb{R}\right\}, \qquad
W = \left\{\gamma\vec{x}_3 + \delta\vec{x}_4 = \begin{pmatrix} \gamma \\ \delta \\ \delta \\ \gamma - \delta \end{pmatrix} \;\middle|\; \gamma, \delta \in \mathbb{R}\right\}.
$$

Vektor leží v průniku, právě když jde zapsat oběma způsoby, tedy když existují $\alpha, \beta, \gamma, \delta$ s

$$
\alpha = \gamma, \qquad \alpha = \delta, \qquad \beta = \delta, \qquad 0 = \gamma - \delta.
$$

Zvolíme $\delta = t \in \mathbb{R}$ libovolně; pak $\gamma = t$ (ze čtvrté rovnice), $\beta = t$, $\alpha = t$ a první rovnice $\alpha = \gamma$ platí. Dosazením do tvaru prvků $V$:

$$
V \cap W = \left\{\begin{pmatrix} t \\ t \\ t \\ 0 \end{pmatrix} \;\middle|\; t \in \mathbb{R}\right\} = \operatorname{span}\left\{\begin{pmatrix} 1 \\ 1 \\ 1 \\ 0 \end{pmatrix}\right\}.
$$

Kontrola dosazením do $W$: $\gamma = \delta = t$ dává $(t; t; t; 0)$, sedí. Navíc $\vec{x}_1 + \vec{x}_2 = (1; 1; 1; 0) = \vec{x}_3 + \vec{x}_4$.

**Dimenze:** $\dim V = 2$, $\dim W = 2$ (v obou případech dva vektory, které nejsou násobky), $\dim(V \cap W) = 1$. Ze vztahu $\vec{x}_1 + \vec{x}_2 = \vec{x}_3 + \vec{x}_4$ je $\vec{x}_4 = \vec{x}_1 + \vec{x}_2 - \vec{x}_3$, takže $\vec{x}_4$ jde z generátorů součtu vyhodit. Zbylé $(\vec{x}_1, \vec{x}_2, \vec{x}_3)$ jsou LN: z $a\vec{x}_1 + b\vec{x}_2 + c\vec{x}_3 = \vec{0}$ plyne ze 4. složky $c = 0$, z 1. složky $a = 0$ a z 3. složky $b = 0$. Proto **$\dim(V + W) = 3$** a $(\vec{x}_1, \vec{x}_2, \vec{x}_3)$ je báze $V + W$.

> [!navic] Neumíš si představit $\mathbb{R}^4$? Nevadí
> Dvě roviny v $\mathbb{R}^4$ si nikdo pořádně nepředstaví. Výpočet výše žádnou představu nepotřebuje, jen definice a soustavu rovnic. Intuici je dobré brát z $\mathbb{R}^2$ a $\mathbb{R}^3$ a ve vyšších dimenzích ji ověřovat počítáním.

## §6 Dimenze součtu a průniku

V příkladech se opakuje stejný vzorec jako u počtu prvků množin:

| situace | $\dim V$ | $\dim W$ | $\dim(V \cap W)$ | $\dim(V + W)$ |
| --- | --- | --- | --- | --- |
| dvě různé přímky přes počátek | 1 | 1 | 0 | 2 |
| dvě různé roviny přes počátek v $\mathbb{R}^3$ | 2 | 2 | 1 | 3 |
| příklad v $\mathbb{R}^4$ | 2 | 2 | 1 | 3 |

> [!veta] Věta (dimenze součtu a průniku)
> ==Buď $L$ lineární prostor a $V, W \le L$ s $\dim V, \dim W < \infty$.== Potom
>
> $$
> \dim(V + W) + \dim(V \cap W) = \dim V + \dim W.
> $$

^veta-dimenze-souctu

Důkaz zatím nezazněl; myšlenka je doplnit bázi průniku jednou na bázi $V$ a jednou na bázi $W$ a ukázat, že všechny tyto vektory dohromady tvoří bázi $V + W$.

> [!lidsky] Lidsky
> Obdoba $\vert A \cup B\vert = \vert A\vert + \vert B\vert - \vert A \cap B\vert$: směry společné oběma podprostorům se v $\dim V + \dim W$ započítají dvakrát, proto je jednou odečteš. Sjednocení odpovídá součet, prázdné množině triviální podprostor $\{\vec{0}\}$.

> [!example] Proč se dvě roviny v $\mathbb{R}^3$ vždy protnou v přímce
> Pro dvě roviny $V, W \le \mathbb{R}^3$ je $V + W \le \mathbb{R}^3$, takže $\dim(V + W) \le 3$. Ze vzorce $\dim(V \cap W) = 2 + 2 - \dim(V + W) \ge 4 - 3 = 1$. Průnik tedy obsahuje aspoň přímku; jsou-li roviny různé, je to přesně přímka.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč se souřadnice definují jen vzhledem k bázi, a ne k libovolné posloupnosti?
> Aby souřadnice **existovaly**, musí posloupnost generovat; aby byly **jednoznačné**, musí být LN ([[věta o jednoznačnosti vyjádření]]). Obojí dohromady je báze.

> [!karta|02]- Čemu se rovná souřadnicový vektor $\vec{v} \in \mathbb{F}^n$ v kanonické bázi a proč?
> **$[\vec{v}]^{\mathcal{E}} = \vec{v}$**, protože $\vec{v} = v_1\vec{e}_1 + \dots + v_n\vec{e}_n$: koeficienty jsou přímo složky.

> [!karta|03]- Jak dokážeš $[\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$?
> Z $\vec{x} = \sum\alpha_i\vec{x}_i$, $\vec{y} = \sum\beta_i\vec{x}_i$ je $\vec{x} + \vec{y} = \sum(\alpha_i + \beta_i)\vec{x}_i$ (komutativita, distributivita). Souřadnice jsou **jednoznačné**, tedy $[\vec{x} + \vec{y}]^{\mathcal{X}} = (\alpha_i + \beta_i)_i$, což je součet sloupců.

> [!karta|04]- Jak dokážeš $[\gamma\vec{x}]^{\mathcal{X}} = \gamma[\vec{x}]^{\mathcal{X}}$?
> $\gamma\vec{x} = \gamma\sum\alpha_i\vec{x}_i = \sum(\gamma\alpha_i)\vec{x}_i$, takže $i$-tá souřadnice je **$\gamma\alpha_i$**, což je $i$-tá složka $\gamma[\vec{x}]^{\mathcal{X}}$ (násobení po složkách).

> [!karta|05]- Proč na užitečnosti souřadnic nestačí, že $L \to \mathbb{F}^n$ je bijekce?
> Bijekce existuje i mezi $\mathbb{R}$ a $\mathbb{R}^2$ (prokládání číslic). Souřadnice jsou cenné, protože **zachovávají sčítání a násobení**, takže se se sloupci dá počítat místo s vektory.

> [!karta|06]- Které dvě různé operace „plus“ vystupují v $[\vec{x} + \vec{y}]^{\mathcal{X}} = [\vec{x}]^{\mathcal{X}} + [\vec{y}]^{\mathcal{X}}$?
> Vlevo sčítání v **$L$** ($L \times L \to L$), vpravo sčítání sloupců **po složkách v $\mathbb{F}^n$**.

> [!karta|07]- Proč sjednocení dvou podprostorů obecně není podprostor?
> Není uzavřené na sčítání: pro dvě přímky s různými směry je $\vec{x} \in V$, $\vec{y} \in W$, ale **$\vec{x} + \vec{y}$ neleží v $V$ ani ve $W$**.

> [!karta|08]- Jak dokážeš, že průnik $V \cap W$ je uzavřený na sčítání?
> $\vec{x}, \vec{y} \in V \cap W$ znamená $\vec{x}, \vec{y} \in V$ i $\vec{x}, \vec{y} \in W$. Oba jsou podprostory, takže **$\vec{x} + \vec{y} \in V$ i $\vec{x} + \vec{y} \in W$**, tedy $\vec{x} + \vec{y} \in V \cap W$.

> [!karta|09]- Jak dokážeš, že součet $V + W$ je uzavřený na násobení číslem?
> $\vec{x} = \vec{v} + \vec{w}$, pak $\alpha\vec{x} = \underbrace{\alpha\vec{v}}_{\in V} + \underbrace{\alpha\vec{w}}_{\in W} \in V + W$ (**distributivita** a uzavřenost $V$, $W$).

> [!karta|10]- Proč je $V + W$ nejmenší podprostor obsahující $V$ i $W$?
> Obsahuje je ($\vec{v} = \vec{v} + \vec{0}$). Každý podprostor obsahující $V \cup W$ je **uzavřený na sčítání**, takže obsahuje všechny součty $\vec{v} + \vec{w}$.

> [!karta|11]- Proč průnik dvou podprostorů nikdy není prázdný a co v lineární algebře hraje roli prázdného průniku?
> Oba obsahují **$\vec{0}$**. Roli prázdné množiny hraje triviální podprostor **$\{\vec{0}\}$** s dimenzí $0$.

> [!karta|12]- Proč nestačí jako generátory průniku $\operatorname{span} M \cap \operatorname{span} N$ vzít $M \cap N$?
> Generátory mohou být úplně různé, a podprostory se přesto protínají: dvě roviny v $\mathbb{R}^3$ se čtyřmi různými generátory mají společnou přímku, ale $M \cap N = \emptyset$. Průnik se musí **spočítat soustavou**.

> [!karta|13]- Proč sjednocení bází $V$ a $W$ nemusí být báze $V + W$?
> **Generuje** (věta o součtu obalů), ale je **LZ, právě když $V \cap W \neq \{\vec{0}\}$**: nenulový vektor průniku jde zapsat z obou bází a rozdíl zápisů je netriviální kombinace nuly.

> [!karta|14]- Proč se dvě roviny přes počátek v $\mathbb{R}^3$ vždy protnou aspoň v přímce?
> $\dim(V + W) \le 3$, takže **$\dim(V \cap W) = 2 + 2 - \dim(V + W) \ge 1$**.

### Příklady na procvičení

> [!priklad|15]- Urči souřadnice $\vec{x}_3 = (1; 2; 1)$ v bázi $\mathcal{X} = ((1; 1; 0), (0; 1; 1))$ roviny $V$.
> $(1; 2; 1) = 1 \cdot (1; 1; 0) + 1 \cdot (0; 1; 1)$, tedy **$[\vec{x}_3]^{\mathcal{X}} = (1; 1)$**. Jen dvě souřadnice, protože $\dim V = 2$.

> [!priklad|16]- Urči souřadnice polynomu $2 + 3x - x^2$ v bázích $(1, x, x^2)$ a $(1, 1 + x, x^2)$.
> V první **$(2; 3; -1)$**. Ve druhé z $a + b(1 + x) + cx^2$: $c = -1$, $b = 3$, $a + b = 2 \Rightarrow a = -1$, tedy **$(-1; 3; -1)$**.

> [!priklad|17]- Je $[\vec{x}]^{\mathcal{X}} = (1; 2)$ a $[\vec{y}]^{\mathcal{X}} = (3; -1)$. Urči $[2\vec{x} - \vec{y}]^{\mathcal{X}}$.
> Linearita: $2(1; 2) - (3; -1) = $ **$(-1; 5)$**.

> [!priklad|18]- Najdi $V \cap W$ pro $V = \operatorname{span}\{(1; 1; 0; 0), (0; 0; 1; 0)\}$, $W = \operatorname{span}\{(1; 0; 0; 1), (0; 1; 1; -1)\}$.
> $(\alpha; \alpha; \beta; 0) = (\gamma; \delta; \delta; \gamma - \delta)$ dává $\gamma = \delta = \alpha = \beta = t$. **$V \cap W = \operatorname{span}\{(1; 1; 1; 0)\}$**, dimenze 1.

> [!priklad|19]- Najdi bázi a dimenzi $V + W$ pro $V = \operatorname{span}\{(1; 1; 0; 0), (0; 0; 1; 0)\}$, $W = \operatorname{span}\{(1; 0; 0; 1), (0; 1; 1; -1)\}$.
> $V + W$ generují $\vec{x}_1 = (1; 1; 0; 0)$, $\vec{x}_2 = (0; 0; 1; 0)$, $\vec{x}_3 = (1; 0; 0; 1)$, $\vec{x}_4 = (0; 1; 1; -1)$ a platí $\vec{x}_4 = \vec{x}_1 + \vec{x}_2 - \vec{x}_3$. Báze **$(\vec{x}_1, \vec{x}_2, \vec{x}_3)$**, **$\dim(V + W) = 3$**; sedí $3 + 1 = 2 + 2$.

> [!priklad|20]- Jaké jsou dimenze součtu a průniku dvou různých přímek přes počátek v $\mathbb{R}^3$?
> Průnik $\{\vec{0}\}$, **dimenze 0**; součet je rovina, **dimenze 2**. Kontrola: $2 + 0 = 1 + 1$.

> [!priklad|21]- Je sjednocení osy $x$ a osy $y$ v $\mathbb{R}^2$ podprostor? A jejich součet?
> Sjednocení **ne**: $(1; 0) + (0; 1) = (1; 1)$ neleží na žádné ose. Součet **ano**, je to celé $\mathbb{R}^2$.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|22]- Urči souřadnice polynomu $3x^2 - x + 2$ vzhledem k bázi $\mathcal{C} = (1 + x,\ x + x^2,\ 1 + x^2)$ prostoru $\mathbb{R}^{\le 2}[x]$.
> Hledáme $\alpha, \beta, \gamma$ s $\alpha(1 + x) + \beta(x + x^2) + \gamma(1 + x^2) = 2 - x + 3x^2$. Porovnání koeficientů: $\alpha + \gamma = 2$ (u $1$), $\alpha + \beta = -1$ (u $x$), $\beta + \gamma = 3$ (u $x^2$). Sečtením $\alpha + \beta + \gamma = 2$, odtud $\beta = 0$, $\gamma = 3$, $\alpha = -1$.
>
> $[3x^2 - x + 2]^{\mathcal{C}} = $ **$(-1; 0; 3)$**. Zkouška: $-(1 + x) + 3(1 + x^2) = 2 - x + 3x^2$.

> [!priklad|23]- Urči souřadnice matice $\begin{pmatrix} 3 & 1 \\ 2 & 5 \end{pmatrix}$ vzhledem k bázi $\mathcal{Y} = \left(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}\right)$ prostoru $\mathbb{R}^{2 \times 2}$.
> $aY_1 + bY_2 + cY_3 + dY_4 = \begin{pmatrix} a + b & b \\ c + d & d \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 2 & 5 \end{pmatrix}$. Rovnice s jedinou neznámou napřed: $b = 1$, $d = 5$, pak $a = 3 - 1 = 2$, $c = 2 - 5 = -3$.
>
> Souřadnice: **$(2; 1; -3; 5)$**.

---
← [[LAG 05 – Báze a dimenze|7. 10. 2026 Báze a dimenze]] · [[LAG 07 – Lineární zobrazení|14. 10. 2026 Lineární zobrazení]] →

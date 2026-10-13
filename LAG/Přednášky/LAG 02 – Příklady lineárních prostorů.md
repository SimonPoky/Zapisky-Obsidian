---
predmet: LAG
prednaska: 2
datum: 2026-09-25
zdroj: "V poznámkách oddíl 1.2 (1.10–1.24)"
tags: [prednaska, LAG]
---

# LAG 02 – Příklady lineárních prostorů

*Přednáška 2 · pátek 25. 9. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `𝔽ⁿ` · `matice` · `eukleidovské vektory` · `posloupnosti` · `𝔽ᴬ` · `polynomy`

[[lineární prostor|Lineární prostor]] není jen množina šipek. Stačí cokoliv, co umíš sčítat a násobit číslem [[operace po složkách|po složkách]] a co splňuje [[axiomy lineárního prostoru|osm axiomů]] z minula. V celé přednášce je $\mathbb{F}$ pevně zvolené [[číselné těleso|těleso]]; klidně si představuj $\mathbb{F} = \mathbb{R}$.

## §0 Přehled na jedné stránce

| prostor | vektory | sčítání a násobení | nulový vektor | opačný k $\vec{x}$ |
|---|---|---|---|---|
| $\mathbb{F}^n$ | sloupce $(x_1; \dots; x_n)$ | po složkách | $(0; \dots; 0)$ | $(-x_1; \dots; -x_n)$ |
| $\mathbb{F}^{m \times n}$ | matice $m \times n$ | po prvcích $a_{ij}$ | nulová matice $\mathbf{O}$ | $-\mathbf{A}$ |
| eukleidovské | šipky z pevného bodu $O$ | rovnoběžník, škálování délky | „šipka“ nulové délky v $O$ | šipka opačným směrem |
| $\mathbb{F}^{\mathbb{N}}$ | posloupnosti $(a_n)$ | člen po členu | $(0, 0, 0, \dots)$ | $(-a_n)$ |
| $\mathbb{F}^A$ | funkce $f : A \to \mathbb{F}$ | bodově: $(f \oplus g)(t) = f(t) + g(t)$ | nulová funkce | $-f$ |
| $\mathbb{F}[x]$ | polynomy | koeficient po koeficientu | nulový polynom $o(x) = 0$ | $-p$ |

## §1 Sloupcové vektory $\mathbb{F}^n$

> [!definice] Příklad · pozn. 1.10
> $$
> \mathbb{F}^n = \left\{ \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \;\middle|\; x_1, \dots, x_n \in \mathbb{F} \right\},
> \qquad
> \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \oplus \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} = \begin{pmatrix} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{pmatrix},
> \qquad
> \alpha \odot \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} \alpha x_1 \\ \vdots \\ \alpha x_n \end{pmatrix}
> $$

^def-fn

> [!lidsky] Lidsky
> Sloupec čísel je jako skříňka se šuplíky. Sčítání „po složkách“ znamená, že sečteš obsah prvního šuplíku s prvním, druhého s druhým a tak dál. Mezi šuplíky se nic nepřelévá: $(1; 2) \oplus (3; 4) = (4; 6)$.

> [!veta] Tvrzení
> $(\mathbb{F}^n, \mathbb{F}, \oplus, \odot)$ je lineární prostor.
>
> **Důkaz:** je třeba ověřit všech 8 axiomů. Ukázka axiomu 1 (komutativita):
>
> $$
> \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \oplus \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}
> = \begin{pmatrix} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{pmatrix}
> \overset{\text{kom. v } \mathbb{F}}{=} \begin{pmatrix} y_1 + x_1 \\ \vdots \\ y_n + x_n \end{pmatrix}
> = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \oplus \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}
> $$

> [!navic] Princip všech těchto důkazů
> Operace jsou definované po složkách, takže každý axiom se „přenese“ z čísel: komutativita vektorů plyne z komutativity čísel v $\mathbb{F}$, distributivita z distributivity čísel atd. Stejný trik funguje pro matice, posloupnosti i funkce.

**Značení** `pozn. 1.10`: sloupcové vektory se značí tučně, $\mathbf{x}$, nulový vektor $\mathbf{0}$. Složku značíme $x_i$ nebo $[\mathbf{x}]_i$, takže $[\mathbf{x} \oplus \mathbf{y}]_i = x_i + y_i$ a $[\alpha \odot \mathbf{x}]_i = \alpha x_i$. Sloupcové (ne řádkové) vektory mají dobrý důvod, ukáže se u násobení maticí.

## §2 Matice $\mathbb{F}^{m \times n}$

> [!definice] Příklad · pozn. 1.11
> $$
> \mathbb{F}^{m \times n} = \left\{ \begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{pmatrix} \;\middle|\; a_{11}, \dots, a_{mn} \in \mathbb{F} \right\}
> $$
>
> je prostor všech matic rozměru $m \times n$. Prvek $a_{ij}$ leží na pozici $(i, j)$: nejdřív **řádek**, pak **sloupec**. Značí se také $[\mathbf{A}]_{ij} = a_{ij}$. Operace jsou definované stejně jako u sloupcových vektorů, po prvcích:
>
> $$
> [\mathbf{A} \oplus \mathbf{B}]_{ij} = a_{ij} + b_{ij}, \qquad [\alpha \odot \mathbf{A}]_{ij} = \alpha a_{ij}
> $$

^def-matice

Příklad: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \oplus \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 3 & 7 \end{pmatrix}$ ✓

> [!navic] Souvislosti · pozn. 1.11
> $\mathbb{F}^{m \times n}$ je „prakticky totéž“ co $\mathbb{F}^{mn}$: stejná čísla, jen poskládaná do tabulky místo do jednoho sloupce. Pro sčítání na tvaru nezáleží, počítá se políčko po políčku. A naopak $\mathbb{F}^n$ je přesně $\mathbb{F}^{n \times 1}$, matice s jedním sloupcem.

## §3 Eukleidovské vektory

Orientované úsečky s pevně zvoleným počátkem $O$, nad tělesem $\mathbb{R}$. Sčítají se doplněním na rovnoběžník a násobí se změnou délky (záporné číslo navíc otočí směr), přesně jak to znáš z fyziky `pozn. 1.12`. ^def-eukl

> [!obrazek] Rovnoběžník a násobek
> ![[lag02-rovnobeznik.png]]
> *Modrá: x = (3; 1), oranžová: y = (1; 2), zelená: x + y = (4; 3) (doplnění na rovnoběžník), čárkovaná modrá: 2 · x = (6; 2).*

## §4 Posloupnosti $\mathbb{F}^{\mathbb{N}}$

> [!definice] Příklad · pozn. 1.16
> $$
> \mathbb{F}^{\mathbb{N}} = \bigl\{ (a_n)_{n=1}^{\infty} \;\big|\; a_n \in \mathbb{F} \bigr\},
> \qquad
> (a_n) \oplus (b_n) = (a_n + b_n)_{n \in \mathbb{N}},
> \qquad
> \alpha \odot (a_n) = (\alpha a_n)_{n \in \mathbb{N}}
> $$

^def-posl

Konkrétně: $\bigl(1, \tfrac12, \tfrac13, \dots\bigr) \oplus (1, 1, 1, \dots) = \bigl(2, \tfrac32, \tfrac43, \dots\bigr)$ a $2 \odot \bigl(1, \tfrac12, \tfrac13, \dots\bigr) = \bigl(2, 1, \tfrac23, \dots\bigr)$. Posloupnost je vlastně nekonečně dlouhý sloupcový vektor.

## §5 Obecně: funkce $\mathbb{F}^A$

> [!definice] Příklad · pozn. 1.17
> Buď $A$ libovolná množina. Potom
>
> $$
> \mathbb{F}^A = \{ f : A \to \mathbb{F} \}
> $$
>
> je lineární prostor nad $\mathbb{F}$ vzhledem k operacím po složkách (bodově):
>
> $$
> (f \oplus g)(t) = f(t) + g(t), \qquad (\alpha \odot f)(t) = \alpha f(t)
> $$

^def-fa

> [!lidsky] Lidsky
> Vektor $(3; 1; 4)$ je vlastně tabulka „pozice → číslo“: pozici 1 přiřadí 3, pozici 2 přiřadí 1, pozici 3 přiřadí 4. To je funkce z množiny $\{1, 2, 3\}$ do čísel.
>
> Když místo $\{1, 2, 3\}$ vezmeš libovolnou množinu pozic $A$, dostaneš $\mathbb{F}^A$. Posloupnost má pozice $1, 2, 3, \dots$ a funkce $\mathbb{R} \to \mathbb{R}$ má pozici pro každé reálné číslo. Funkce je tedy vektor s „hodně složkami“, jedna složka za každý prvek $A$. Sčítání „bodově“ je pořád totéž co „po složkách“: sčítá se hodnota s hodnotou na stejné pozici.

> [!obrazek] Vektor, posloupnost a funkce jsou totéž
> ![[lag02-vektor-funkce.png]]
> *Nad každou pozicí t leží hodnota f(t). Vektor (3; 1; 4) má 3 pozice, posloupnost 4/n nekonečně mnoho a funkce ℝ → ℝ jednu pozici pro každé reálné číslo.*

Tohle je „mateřský“ příklad, ze kterého vzniknou všechny předchozí volbou množiny $A$:

- $A = \{1, \dots, n\}$: funkce přiřadí indexu $i$ číslo $x_i$, to je vektor z $\mathbb{F}^n$ (hodnoty se čtou po řádcích sloupce),
- $A = \mathbb{N}$: posloupnosti $\mathbb{F}^{\mathbb{N}}$,
- $A = \mathbb{F}$: všechny funkce $\mathbb{F} \to \mathbb{F}$, např. $\sin + \cos$ je vektor v $\mathbb{R}^{\mathbb{R}}$,
- $A = \{1, \dots, m\} \times \{1, \dots, n\}$: dvojici $(i, j)$ přiřadí $a_{ij}$, to jsou [[matice]].

> [!navic] Co když A = ∅?
> Množina $A$ může být zcela libovolná, i prázdná: existuje právě jedna (prázdná) funkce $\emptyset \to \mathbb{F}$, takže $\mathbb{F}^{\emptyset}$ je jednoprvková množina. I ta je lineární prostor (příklad 1.13), jen dost nudný.

## §6 Polynomy $\mathbb{F}[x]$

> [!definice] Definice · pozn. 1.18
> *Polynom* s proměnnou $x$ a koeficienty z tělesa $\mathbb{F}$ je výraz tvaru
>
> $$
> p(x) = \alpha_0 + \alpha_1 x + \dots + \alpha_n x^n, \qquad n \in \mathbb{N}_0,\ \alpha_i \in \mathbb{F}.
> $$
>
> *Stupeň* polynomu je index nejvyššího nenulového koeficientu:
>
> $$
> \deg p(x) = \max\{ i \in \mathbb{N}_0 \mid \alpha_i \neq 0 \}.
> $$
>
> Pro *nulový polynom* $o(x) = 0$ se dohodou klade $\deg o(x) = -\infty$. Množinu všech polynomů s koeficienty z $\mathbb{F}$ značíme $\mathbb{F}[x]$.

^def-poly

> [!lidsky] Lidsky
> Stupeň je nejvyšší mocnina $x$, která v polynomu opravdu je, tedy má před sebou nenulové číslo. $3 + 0x^5$ má stupeň 0, protože $x^5$ tam ve skutečnosti není.

**Příklad:** $p(x) = 2 + 3x - x^2$ má koeficienty $\alpha_0 = 2,\ \alpha_1 = 3,\ \alpha_2 = -1$, stupeň $\deg p(x) = 2$ a jeho nejvyšší nenulový člen je $-x^2$. Tomu členu se běžně říká *vedoucí člen* a číslu $-1$ *vedoucí koeficient*. ^vedouci

> [!navic] Proč jsou polynomy lineární prostor
> Polynom je úplně určený seznamem svých koeficientů. $2 + 3x - x^2$ je vlastně vektor $(2; 3; -1)$ a $1 - x + x^2$ je $(1; -1; 1)$. Sčítání a násobení číslem dělá přesně totéž co u vektorů, po složkách:
>
> $$
> (2 + 3x - x^2) \oplus (1 - x + x^2) = 3 + 2x \quad\longleftrightarrow\quad (2; 3; -1) + (1; -1; 1) = (3; 2; 0)
> $$
>
> Mají-li polynomy různou délku, kratší se doplní nulami. [[nulový vektor|Nulový vektor]] je nulový polynom, [[opačný vektor]] k $p$ je $-p$. Všech 8 axiomů se tak ověří stejně jako u $\mathbb{F}^n$. Rozdíl je jen v tom, že délka seznamu není omezená: polynomy jsou „posloupnosti koeficientů, které jsou od jistého místa nulové“.

> [!obrazek] Polynom = vektor koeficientů
> ![[lag02-polynomy.png]]
> *Modrá: p = 2 + 3x − x², oranžová: q = 1 − x + x², zelená: p + q = 3 + 2x. Koeficienty se sečtou jako vektory (2; 3; −1) + (1; −1; 1) = (3; 2; 0) a stupeň klesne ze 2 na 1.*

> [!navic] Proč je deg o(x) = −∞, a ne 0
> Stupeň 0 už mají nenulové konstanty ($\deg 5 = 0$). Hodnota $-\infty$ zajistí, že pravidla o stupních platí úplně pro všechny polynomy:
>
> - $\deg(p \cdot q) = \deg p + \deg q$: pro $p = o$ vyjde $-\infty = -\infty + \deg q$ ✓, kdežto s nulou by to nesedělo.
> - $\deg(p + q) \le \max(\deg p, \deg q)$: stupeň součtu může klesnout, např. $(x^2 + 1) + (-x^2) = 1$, a pro $q = -p$ klesne až na $-\infty$.

> [!navic] Polynom vs. polynomiální funkce · pozn. 1.19–1.22
> - Polynom je určen **koeficienty**, polynomiální funkce **hodnotami** na definičním oboru. Do polynomu lze dosazovat ledacos, později třeba i matice.
> - Pro číselná tělesa je to ale jen kosmetický rozdíl: koeficienty jsou jednoznačně určené hodnotami v racionálních bodech (věta 1.20), takže polynomy z $\mathbb{F}[x]$ a polynomiální funkce $\mathbb{F} \to \mathbb{F}$ si vzájemně jednoznačně odpovídají.
> - $\mathbb{F}_{\le n}[x]$, polynomy stupně nejvýše $n$, jsou také lineární prostor a jsou „prakticky totéž“ co $\mathbb{F}^{n+1}$. Tady už stačí ověřit, že součet ani násobek nevyvedou z množiny ven (operace jsou *dobře definované*).

^pozn-polyfce

> [!lidsky] Lidsky
> Polynom je recept (seznam koeficientů), polynomiální funkce je hotové jídlo (co vyjde po dosazení čísla). Dva různé recepty by teoreticky mohly dát stejné jídlo: nad tělesem $\mathbb{Z}_2$ dávají $x$ a $x^2$ v bodech 0 a 1 stejné hodnoty. U číselných těles se to stát nemůže, recept a jídlo si odpovídají jedna ku jedné.
>
> „Dobře definovaná“ operace nevyvede z množiny ven. Sečteš dva polynomy stupně nejvýše 2 a vyjde zase polynom stupně nejvýše 2, takže se nemusíš bát, že „vypadneš“ z prostoru.

## §7 Další příklady lineárních prostorů

- **Jednoprvková množina** $\{\vec{0}\}$ je lineární prostor nad jakýmkoliv tělesem (1.13).
- **Těleso samo nad sebou:** $\mathbb{F}$ s obyčejným $+$ a $\cdot$ (1.14).
- **$\mathbb{C}$ nad $\mathbb{R}$:** komplexní čísla sčítáš a násobíš reálnými čísly (1.15).

> [!example]- Na zamyšlení: kladná čísla, kde „sčítání“ je násobení (1.24)
> Vezmi $L = (0, +\infty)$ a definuj $x \oplus y = xy$ a $\alpha \odot x = x^{\alpha}$ pro $\alpha \in \mathbb{R}$. Je to lineární prostor nad $\mathbb{R}$?
>
> > [!question]- Co je tady nulový vektor a co opačný vektor?
> > Nulový vektor je číslo $1$, protože $x \oplus 1 = x \cdot 1 = x$. Opačný vektor k $x$ je $\frac{1}{x}$, protože $x \oplus \frac1x = 1$.
>
> > [!question]- Platí axiom 7?
> > Ano: $(\alpha + \beta) \odot x = x^{\alpha + \beta} = x^{\alpha} \cdot x^{\beta} = (\alpha \odot x) \oplus (\beta \odot x)$. Ostatní axiomy jsou pravidla pro počítání s mocninami.
>
> > [!question]- Je to něco nového, nebo „prakticky“ $\mathbb{R}$?
> > Prakticky $\mathbb{R}$. Logaritmus převádí tento prostor na obyčejná reálná čísla: $\ln(xy) = \ln x + \ln y$ a $\ln(x^{\alpha}) = \alpha \ln x$. Takovému převodu se později bude říkat *izomorfismus* (kap. 7): dva prostory jsou „stejné, jen jinak zapsané“.

^zamysleni

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- Jak se dokazuje, že $\mathbb{F}^n$ je lineární prostor?
> Ověří se všech 8 axiomů. Operace jsou po složkách, takže každý axiom plyne z odpovídající vlastnosti čísel v $\mathbb{F}$ (komutativita vektorů z komutativity sčítání čísel atd.).

> [!karta|04]- Jak souvisí $\mathbb{F}^{m \times n}$ s $\mathbb{F}^{mn}$ a $\mathbb{F}^n$ s maticemi?
> $\mathbb{F}^{m \times n}$ je „prakticky“ $\mathbb{F}^{mn}$: stejná čísla, jen poskládaná do tabulky, sčítá se políčko po políčku. A $\mathbb{F}^n = \mathbb{F}^{n \times 1}$, matice s jedním sloupcem.

> [!karta|05]- Jak z prostoru funkcí $\mathbb{F}^A$ dostaneš $\mathbb{F}^n$, posloupnosti a funkce $\mathbb{R} \to \mathbb{R}$?
> Volbou $A = \{1, \dots, n\}$, $A = \mathbb{N}$ a $A = \mathbb{R}$ (s $\mathbb{F} = \mathbb{R}$). Matice dostaneš pro $A = \{1, \dots, m\} \times \{1, \dots, n\}$.

> [!karta|08]- Proč je $\deg o(x) = -\infty$, a ne $0$?
> Stupeň 0 už mají nenulové konstanty. S $-\infty$ platí $\deg(p \cdot q) = \deg p + \deg q$ i pro nulový polynom.

> [!karta|09]- Co víš o stupni součtu $\deg(p + q)$?
> $\deg(p + q) \le \max(\deg p, \deg q)$. Stupeň může klesnout: $(x^2 + 1) + (-x^2) = 1$, pro $q = -p$ až na $-\infty$.

> [!karta|10]- Proč se polynomy sčítají jako vektory?
> Polynom je určený seznamem koeficientů, $2 + 3x - x^2 \leftrightarrow (2; 3; -1)$. Sčítání i násobení číslem jde koeficient po koeficientu, stejně jako v $\mathbb{F}^n$.

> [!karta|12]- Čemu „odpovídá“ $\mathbb{F}_{\le n}[x]$ a proč je to lineární prostor?
> Polynomy stupně nejvýše $n$ mají $n + 1$ koeficientů, takže jsou „prakticky“ $\mathbb{F}^{n+1}$. Lineární prostor jsou, protože součet ani násobek nezvýší stupeň nad $n$ (operace jsou dobře definované).

> [!karta|13]- Proč nad číselným tělesem odpovídají polynomy a polynomiální funkce jedna ku jedné? Kde to neplatí?
> Koeficienty jsou jednoznačně určené hodnotami v racionálních bodech (nenulový polynom stupně $n$ má nejvýš $n$ kořenů). Neplatí to např. nad $\mathbb{Z}_2$: $x$ a $x^2$ mají v bodech 0 a 1 stejné hodnoty.

### Příklady na procvičení

> [!priklad|01]- Urči nulový vektor v $\mathbb{F}^{2 \times 2}$, v $\mathbb{F}[x]$ a v $\mathbb{F}^{\mathbb{N}}$?
> Nulová matice $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$, nulový polynom $o(x) = 0$, nulová posloupnost $(0, 0, 0, \dots)$.

> [!priklad|06]- Co je $\mathbb{F}^{\emptyset}$ a je to lineární prostor?
> **Jednoprvková množina**: existuje právě jedna (prázdná) funkce $\emptyset \to \mathbb{F}$. Je to lineární prostor, jen triviální $\{\vec{0}\}$ (příklad 1.13).

> [!priklad|07]- Jaký je stupeň polynomů $2 + 3x - x^2$, $5$ a $0$?
> $2$, $0$ a $-\infty$.

> [!priklad|11]- Je množina polynomů stupně *přesně* 2 lineární prostor?
> Není. Neobsahuje nulový polynom a součet z ní vypadne: $x^2 + (-x^2 + x) = x$ má stupeň 1. Polynomy stupně **nejvýše** 2 lineární prostor jsou.

> [!priklad|14]- Je $L = (0, +\infty)$ s $x \oplus y = xy$ a $\alpha \odot x = x^{\alpha}$ lineární prostor nad $\mathbb{R}$? Co je jeho nulový vektor?
> Ano. Nulový vektor je $1$ (protože $x \cdot 1 = x$), opačný k $x$ je $\frac{1}{x}$. Logaritmus ho převádí na obyčejné $\mathbb{R}$, jde o izomorfismus.

> [!priklad|15]- Jsou komplexní čísla $\mathbb{C}$ lineární prostor nad $\mathbb{R}$?
> Ano (1.15): komplexní čísla sčítáš mezi sebou a násobíš reálnými čísly, všech 8 axiomů platí. Stejně je každé těleso lineární prostor samo nad sebou (1.14).

---
← [[LAG 01 – Úvod do lineární algebry|23. 9. 2026 Úvod do lineární algebry]] · [[LAG 03 – Lineární podprostor a lineární obal|30. 9. 2026 Lineární podprostor a lineární obal]] →

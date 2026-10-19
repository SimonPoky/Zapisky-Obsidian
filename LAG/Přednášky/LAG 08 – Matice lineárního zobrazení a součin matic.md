---
predmet: LAG
prednaska: 8
datum: 2026-10-16
zdroj: "V poznámkách kap. 6.1 (pozn. 6.6–6.8) a 6.2 (pozn. 6.9–6.20)"
tags: [prednaska, LAG]
---

# LAG 08 – Matice lineárního zobrazení a součin matic

*Přednáška 8 · pátek 16. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `součin matic` · `matice zobrazení vzhledem k bázím` · `[A]^{X→Y}` · `[Ax]^Y = [A][x]^X` · `matice derivace` · `zadání zobrazení na bázi` · `Lin(V, W) ↔ 𝔽^{n×m}` · `skládání = součin matic` · `matice otočení`

Minule jsme viděli, že lineární zobrazení $\mathbb{F}^m \to \mathbb{F}^n$ je totéž co matice: sloupce jsou obrazy $\vec{e}_1, \dots, \vec{e}_m$. Dnes se to rozšíří na **libovolné prostory konečné dimenze**: zvolíme bázi na vstupu i na výstupu, přejdeme k souřadnicím a zobrazení se zase stane násobením maticí. Nejdřív si ale zavedeme součin dvou matic, protože přesně ten odpovídá skládání zobrazení.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[součin matic]] | $[AB]_{ij} = \sum_{k} a_{ik}b_{kj}$; po sloupcích $A(\vec{b}_1 \cdots \vec{b}_l) = (A\vec{b}_1 \cdots A\vec{b}_l)$ | $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 3 & -2 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 19 & 4 \end{pmatrix}$ |
| [[matice lineárního zobrazení vzhledem k bázím]] | $[A]^{\mathcal{X} \to \mathcal{Y}} = ([A\vec{x}_1]^{\mathcal{Y}} \cdots [A\vec{x}_m]^{\mathcal{Y}})$ | derivace na $\mathbb{R}^{\le 2}[x]$ |
| [[matice lineárního operátoru v bázi]] | $[A]^{\mathcal{X}} = [A]^{\mathcal{X} \to \mathcal{X}}$ | $[D]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$ |
| [[operátor derivace]] | $D(\alpha_0 + \alpha_1 x + \alpha_2 x^2) = \alpha_1 + 2\alpha_2 x$ | $D(3x^2 + 5x + 7) = 6x + 5$ |
| [[věta o souřadnicích obrazu]] | $[A\vec{x}]^{\mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}}[\vec{x}]^{\mathcal{X}}$ | derivace spočítaná maticí |
| [[věta o zadání lineárního zobrazení na bázi]] | obrazy vektorů báze jdou předepsat libovolně a určí zobrazení jednoznačně | |
| [[korespondence lineárních zobrazení a matic]] | $A \mapsto [A]^{\mathcal{X} \to \mathcal{Y}}$ je bijekce $\operatorname{Lin}(V, W) \to \mathbb{F}^{n \times m}$ | |
| [[věta o matici složeného zobrazení]] | $[BA]^{\mathcal{X} \to \mathcal{Z}} = [B]^{\mathcal{Y} \to \mathcal{Z}}[A]^{\mathcal{X} \to \mathcal{Y}}$ | |
| [[matice otočení]] | $R_\alpha = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}$ | $\alpha = 90°$: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ |

## §1 Opakování: zobrazení zadané maticí

Dvě tvrzení z minula, teď v označení, které se bude používat dál: matice $A \in \mathbb{F}^{n \times m}$ (tedy $n$ řádků a $m$ sloupců) dělá zobrazení $\mathbb{F}^m \to \mathbb{F}^n$.

> [!veta] Tvrzení (násobení maticí je lineární) · pozn. 6.6 a 6.8
> ==Buď $A = (\vec{a}_1 \cdots \vec{a}_m) \in \mathbb{F}^{n \times m}$.== Potom je zobrazení $\mathbb{F}^m \to \mathbb{F}^n$, $\vec{x} \mapsto A\vec{x}$ **lineární**. Přitom
>
> $$
> A\vec{x} = x_1\vec{a}_1 + \dots + x_m\vec{a}_m, \qquad [A\vec{x}]_i = \sum_{k=1}^{m} a_{ik}x_k.
> $$

^veta-nasobeni-matici

> [!lidsky] Lidsky
> [[lineární kombinace|Lineární kombinace]] je lineární „funkcí“ svých koeficientů: vektory $\vec{a}_1, \dots, \vec{a}_m$ jsou pevné konstanty a proměnné jsou jen čísla $x_1, \dots, x_m$. Důkaz je [[věta o zobrazení zadaném sloupci]] z minula.

> [!veta] Tvrzení (určení kanonickou bází) · pozn. 6.8
> ==Buď $A \in \operatorname{Lin}(\mathbb{F}^m, \mathbb{F}^n)$ a $\vec{a}_i = A\vec{e}_i$.== Pak **$A\vec{x} = (\vec{a}_1 \cdots \vec{a}_m)\vec{x}$ pro každé $\vec{x} \in \mathbb{F}^m$**, tedy lineární zobrazení je jednoznačně určené tím, kam pošle [[kanonická báze|kanonickou bázi]]:
>
> $$
> A\begin{pmatrix} x_1 \\ \vdots \\ x_m \end{pmatrix} = A(x_1\vec{e}_1 + \dots + x_m\vec{e}_m) = x_1 A\vec{e}_1 + \dots + x_m A\vec{e}_m = x_1\vec{a}_1 + \dots + x_m\vec{a}_m.
> $$

^veta-urceni-kanonickou

> [!lidsky] Lidsky
> Tohle je [[matice zobrazení v kanonické bázi]]. Dohromady obě tvrzení říkají: matice $n \times m$ a lineární zobrazení $\mathbb{F}^m \to \mathbb{F}^n$ jsou „totéž“. Dnes se ukáže, že to platí pro jakékoli dva prostory konečné dimenze, jen se musí zvolit báze.

> [!navic] Stejné písmeno pro zobrazení i matici
> Zobrazení a jeho matice se často značí stejným písmenem, někdy se matice odliší jiným fontem ($A \mapsto \mathbb{A}$). U $\mathbb{F}^m \to \mathbb{F}^n$ to nevadí, protože $A\vec{x}$ je opravdu matice krát vektor. U obecných prostorů (polynomy, matice) je ale potřeba psát $[A]^{\mathcal{X} \to \mathcal{Y}}$ (§3), protože matice tam násobí souřadnice, ne samotný vektor.

## §2 Součin matic

Matici jde násobit nejen vektorem, ale i jinou maticí. Definice je nastavená tak, aby součin odpovídal skládání zobrazení (§6).

> [!definice] Definice ♥ · pozn. 6.9 · součin matic
> Buďte $A \in \mathbb{F}^{n \times m}$ a $B \in \mathbb{F}^{m \times l}$. Jejich *součin* $AB \in \mathbb{F}^{n \times l}$ definujeme předpisem
>
> $$
> [AB]_{ij} = \sum_{k=1}^{m} a_{ik}b_{kj} \qquad (i = 1, \dots, n;\ j = 1, \dots, l),
> $$
>
> kde $a_{ik} = [A]_{ik}$ a $b_{kj} = [B]_{kj}$. Speciálně (volbou $l = 1$) pro $\vec{x} \in \mathbb{F}^m$ dostaneme $A\vec{x} \in \mathbb{F}^n$, $[A\vec{x}]_i = \sum_{k=1}^{m} a_{ik}x_k$, tedy přesně [[součin matice a vektoru]].

^def-soucin-matic

> [!lidsky] Lidsky
> Prvek na místě $(i, j)$ dostaneš jako „**$i$-tý řádek $A$ krát $j$-tý sloupec $B$**“: vynásobíš první s prvním, druhý s druhým… a sečteš. Aby to šlo, musí být řádek $A$ stejně dlouhý jako sloupec $B$: $A$ má tolik sloupců, kolik má $B$ řádků. Výsledek zdědí počet řádků od $A$ a počet sloupců od $B$: $(n \times m) \cdot (m \times l) = n \times l$, „vnitřní“ $m$ zmizí.

> [!example] Příklady
> Jako zobrazení (kombinace sloupců s proměnnými koeficienty):
>
> $$
> \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = x\begin{pmatrix} 1 \\ 4 \end{pmatrix} + y\begin{pmatrix} 2 \\ 5 \end{pmatrix} + z\begin{pmatrix} 3 \\ 6 \end{pmatrix} = \begin{pmatrix} x + 2y + 3z \\ 4x + 5y + 6z \end{pmatrix}.
> $$
>
> Matice $2 \times 3$ tedy dělá zobrazení $\mathbb{R}^3 \to \mathbb{R}^2$. Pro konkrétní vektor a pak pro matici se dvěma sloupci:
>
> $$
> \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix} = \begin{pmatrix} 7 \\ 19 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 3 & -2 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 19 & 4 \end{pmatrix}.
> $$
>
> Druhý sloupec: $1 \cdot (-1) + 2 \cdot (-2) + 3 \cdot 3 = 4$ a $4 \cdot (-1) + 5 \cdot (-2) + 6 \cdot 3 = 4$.

> [!obrazek] Řádek krát sloupec, nebo matice krát sloupce
> ![[lag08-soucin.png]]
> *Modrý řádek $A$ krát oranžový sloupec $B$ dá zelený prvek $[AB]_{21} = 19$. Vpravo druhý pohled: první sloupec součinu je $A$ krát první sloupec $B$.*

Z definice hned plyne pohled **po sloupcích**: $j$-tý sloupec $AB$ má složky $\sum_k a_{ik}b_{kj}$, a to jsou přesně složky $A\vec{b}_j$. Tedy

$$
A(\vec{b}_1 \cdots \vec{b}_l) = (A\vec{b}_1 \cdots A\vec{b}_l).
$$

^sloupce-soucinu

> [!pozor] Pořadí a rozměry
> Součin $AB$ existuje jen pro „počet sloupců $A$ = počet řádků $B$“. Pro $A \in \mathbb{F}^{2 \times 3}$ a $B \in \mathbb{F}^{3 \times 2}$ existují oba součiny, ale $AB$ je $2 \times 2$ a $BA$ je $3 \times 3$, takže si rovné být nemůžou. Ani u čtvercových matic obecně $AB \ne BA$: $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 4 & 2 \end{pmatrix} = \begin{pmatrix} 6 & 0 \\ 12 & 6 \end{pmatrix}$, ale v opačném pořadí vyjde $\begin{pmatrix} 2 & -2 \\ 8 & 10 \end{pmatrix}$. Je to stejné jako u [[složené zobrazení|skládání zobrazení]].

## §3 Matice lineárního zobrazení vzhledem k bázím

U $\mathbb{F}^m \to \mathbb{F}^n$ jsme do sloupců psali přímo obrazy $A\vec{e}_i$. U polynomů nebo matic to nejde: obraz je polynom, ne sloupec čísel. Pomůže [[souřadnicový vektor]]: každý vektor převedeme na sloupec jeho souřadnic v nějaké bázi.

> [!definice] Definice ♥ · pozn. 6.11 · matice lineárního zobrazení vzhledem k bázím
> Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$ konečné dimenze. Nechť $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_m)$ je báze $V$ a $\mathcal{Y} = (\vec{y}_1, \dots, \vec{y}_n)$ je báze $W$. Pro libovolné $A \in \operatorname{Lin}(V, W)$ definujeme jeho *matici v bázích $\mathcal{X}$ a $\mathcal{Y}$* jako
>
> $$
> [A]^{\mathcal{X} \to \mathcal{Y}} = \big([A\vec{x}_1]^{\mathcal{Y}} \cdots [A\vec{x}_m]^{\mathcal{Y}}\big) \in \mathbb{F}^{n \times m}.
> $$
>
> Je-li $V = W$ a $\mathcal{X} = \mathcal{Y}$, značíme $[A]^{\mathcal{X}} = [A]^{\mathcal{X} \to \mathcal{X}}$ (*matice operátoru $A$ v bázi $\mathcal{X}$*).
>
> *Pozor na písmena: tady má $V$ dimenzi $m$ a $W$ dimenzi $n$; v pozn. 6.11 i v [[LAG 07 – Lineární zobrazení|LAG 07]] je to naopak. Platí vždy: řádků je tolik, kolik je $\dim W$ (výstup), sloupců tolik, kolik je $\dim V$ (vstup).*

^def-matice-v-bazich

> [!lidsky] Lidsky
> Recept na matici ve třech krocích: **(1)** vezmi $j$-tý vektor vstupní báze $\vec{x}_j$, **(2)** zobraz ho, **(3)** výsledek $A\vec{x}_j$ rozlož do výstupní báze $\mathcal{Y}$ a koeficienty napiš jako $j$-tý sloupec. Vstupní báze tedy určuje, **které** vektory zobrazuješ (a kolik je sloupců, $m = \dim V$), výstupní báze, **v jakých souřadnicích** zapisuješ výsledek (a kolik je řádků, $n = \dim W$). Jiné báze dají jinou matici téhož zobrazení, stejně jako jiná báze dá jiné souřadnice téhož vektoru.

> [!pozor] Které souřadnice kam
> Ve sloupcích jsou souřadnice **obrazů** $A\vec{x}_j$ vzhledem k bázi **$\mathcal{Y}$**, ne souřadnice $\vec{x}_j$ a ne souřadnice v bázi $\mathcal{X}$. Častá chyba v testu: zobrazit vektor správně, ale zapsat ho do sloupce „tak, jak vypadá“, místo jeho souřadnic ve výstupní bázi.

> [!navic] Značení na cvičení
> Na cvičení a v testech se píše $[A]_{\mathcal{B} \to \mathcal{C}}$ nebo $[A]_{\mathcal{B} \mapsto \mathcal{C}}$ („matice lineárního zobrazení $A$ vůči bázím $\mathcal{B}$ a $\mathcal{C}$“), v těchto poznámkách $[A]^{\mathcal{X} \to \mathcal{Y}}$. Je to totéž; první báze je vždy ta na vstupu.

### Příklad: derivace polynomů

> [!definice] Definice · operátor derivace na $\mathbb{R}^{\le 2}[x]$
> Zobrazení $D : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$,
>
> $$
> D(\alpha_0 + \alpha_1 x + \alpha_2 x^2) = \alpha_1 + 2\alpha_2 x,
> $$
>
> je *derivace* polynomů. Je to [[lineární operátor]]: derivace součtu je součet derivací a konstanta se vytkne (stejně jako $D$ na celém $\mathbb{R}[x]$ v [[LAG 07 – Lineární zobrazení#Derivace a „integrál“ polynomů|minulé přednášce]]). Obecně $D(\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n) = \alpha_1 + 2\alpha_2 x + \dots + n\alpha_n x^{n-1}$ na $\mathbb{R}^{\le n}[x]$.

^def-operator-derivace

> [!lidsky] Lidsky
> Derivaci znáš ze školy jako „sklon funkce“. Lineární algebru ale zajímá jen to, co dělá s koeficienty: $x^k$ přejde na $kx^{k-1}$. Je to dobrý příklad, že lineární zobrazení nemusí mít nic společného se šipkami v rovině.

Bázi zvolíme $\mathcal{E} = (1, x, x^2)$ (kanonickou bázi [[prostor polynomů stupně nejvýše n|$\mathbb{R}^{\le 2}[x]$]]) na vstupu i na výstupu. Zobrazíme vektory báze a výsledky rozložíme zpátky do $\mathcal{E}$:

| $\vec{x}_j$ | $D(\vec{x}_j)$ | rozklad v $\mathcal{E}$ | $[D(\vec{x}_j)]^{\mathcal{E}}$ |
| --- | --- | --- | --- |
| $1$ | $0$ | $0 \cdot 1 + 0 \cdot x + 0 \cdot x^2$ | $(0; 0; 0)$ |
| $x$ | $1$ | $1 \cdot 1 + 0 \cdot x + 0 \cdot x^2$ | $(1; 0; 0)$ |
| $x^2$ | $2x$ | $0 \cdot 1 + 2 \cdot x + 0 \cdot x^2$ | $(0; 2; 0)$ |

$$
[D]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}.
$$

^matice-derivace

K čemu taková matice je, říká hlavní věta:

> [!veta] Věta 6.13 (souřadnice obrazu)
> ==Buďte $V$, $W$ lineární prostory konečné dimenze nad $\mathbb{F}$ a $\mathcal{X}$, $\mathcal{Y}$ jejich báze.== Potom pro libovolné $A \in \operatorname{Lin}(V, W)$ a $\vec{x} \in V$ platí
>
> $$
> \mathbf{[A\vec{x}]^{\mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}} \cdot [\vec{x}]^{\mathcal{X}}.}
> $$
>
> > [!note]- Důkaz
> > Buď $[\vec{x}]^{\mathcal{X}} = (\xi_1; \dots; \xi_m)$, tedy $\vec{x} = \xi_1\vec{x}_1 + \dots + \xi_m\vec{x}_m$. Z [[věta o zachování lineárních kombinací|zachování lineárních kombinací]] je $A\vec{x} = \xi_1 A\vec{x}_1 + \dots + \xi_m A\vec{x}_m$. Souřadnice jsou lineární ([[věta o linearitě souřadnic]]), takže
> >
> > $$
> > [A\vec{x}]^{\mathcal{Y}} = \xi_1[A\vec{x}_1]^{\mathcal{Y}} + \dots + \xi_m[A\vec{x}_m]^{\mathcal{Y}}.
> > $$
> >
> > Vpravo je lineární kombinace sloupců matice $[A]^{\mathcal{X} \to \mathcal{Y}}$ s koeficienty $\xi_1, \dots, \xi_m$, a to je podle definice [[součin matice a vektoru|součinu matice a vektoru]] přesně $[A]^{\mathcal{X} \to \mathcal{Y}}[\vec{x}]^{\mathcal{X}}$.

^veta-souradnice-obrazu

> [!lidsky] Lidsky
> Místo abys zobrazoval samotný vektor (polynom, matici…), převedeš ho na souřadnice, vynásobíš maticí a dostaneš souřadnice výsledku. Matice je „překladač“: počítá to samé co $A$, jen v jazyce sloupců čísel. Na obrázku vedou obě cesty z levého horního rohu do pravého dolního ke stejnému výsledku.

> [!obrazek] Dvě cesty ke stejnému výsledku
> ![[lag08-baze.png]]
> *Modrá: zobrazení $A$ přímo ve $V$ a $W$. Oranžové: převod na souřadnice v bázích $\mathcal{X}$ a $\mathcal{Y}$. Zelená: násobení maticí $[A]^{\mathcal{X} \to \mathcal{Y}}$. Cesta „dolů a doprava“ dá totéž co „doprava a dolů“.*

> [!example] Derivace maticí
> $p(x) = 3x^2 + 5x + 7$, takže $[p]^{\mathcal{E}} = (7; 5; 3)$ (pozor na pořadí: báze začíná jedničkou). Podle věty
>
> $$
> [Dp]^{\mathcal{E}} = [D]^{\mathcal{E}}[p]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} 7 \\ 5 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ 6 \\ 0 \end{pmatrix},
> $$
>
> tedy $Dp = 5 \cdot 1 + 6 \cdot x + 0 \cdot x^2 = 6x + 5$. Přímé derivování dá totéž: $(3x^2 + 5x + 7)' = 6x + 5$.

> [!navic] Matice určuje zobrazení jen jedna
> Z věty plyne i opak definice: je-li $M \in \mathbb{F}^{n \times m}$ matice, pro kterou $M[\vec{x}]^{\mathcal{X}} = [A\vec{x}]^{\mathcal{Y}}$ pro všechna $\vec{x} \in V$, pak $M = [A]^{\mathcal{X} \to \mathcal{Y}}$. Stačí dosadit $\vec{x} = \vec{x}_j$: je $[\vec{x}_j]^{\mathcal{X}} = \vec{e}_j$ a $M\vec{e}_j$ je $j$-tý sloupec $M$, takže $j$-tý sloupec $M$ je $[A\vec{x}_j]^{\mathcal{Y}}$. Toho využijeme v §6.

## §4 Kanonická báze v rovině

V $\mathbb{F}^n$ s [[kanonická báze|kanonickou bází]] $\mathcal{E}$ jsou souřadnice vektoru jeho složky: $[\vec{v}]^{\mathcal{E}} = \vec{v}$. Matice $[A]^{\mathcal{E}}$ je proto přesně [[matice zobrazení v kanonické bázi]] z minula a věta o souřadnicích obrazu říká jen $A\vec{x} = [A]^{\mathcal{E}}\vec{x}$.

> [!example] $A(x; y) = (x - y;\ x + y)$
> $A : \mathbb{R}^2 \to \mathbb{R}^2$, $\mathcal{E} = (\vec{e}_1, \vec{e}_2)$. Obrazy:
>
> $$
> A\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad A\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}, \qquad [A]^{\mathcal{E}} = (A\vec{e}_1\ A\vec{e}_2) = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}.
> $$
>
> Kontrola větou:
>
> $$
> A\begin{pmatrix} x \\ y \end{pmatrix} = \left[A\begin{pmatrix} x \\ y \end{pmatrix}\right]^{\mathcal{E}} = [A]^{\mathcal{E}}\left[\begin{pmatrix} x \\ y \end{pmatrix}\right]^{\mathcal{E}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ x + y \end{pmatrix}.
> $$

> [!obrazek] Co $A$ udělá s mřížkou
> ![[lag08-mrizka.png]]
> *Vlevo kanonická síť, modré $\vec{e}_1$ a oranžové $\vec{e}_2$. Vpravo jejich obrazy, sloupce matice: $(1; 1)$ a $(-1; 1)$. Celá síť se otočí o $45°$ a natáhne $\sqrt{2}$-krát, protože $\lvert(1; 1)\rvert = \sqrt{2} \approx 1{,}41$.*

> [!navic] Vyzkoušej si to
> Na [shad.io/MatVis ↗](https://shad.io/MatVis/) zadáš matici $2 \times 2$ a uvidíš, jak deformuje síť. Zkus $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, zkosení $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ nebo průmět $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Zdarma, v prohlížeči.

## §5 Zadání lineárního zobrazení na bázi

Viděli jsme, že lineární zobrazení je určené obrazy vektorů báze. Platí ale víc: tyto obrazy si můžeme **vymyslet libovolně** a zobrazení vždycky existuje.

> [!veta] Věta 6.15 (zadání lineárního zobrazení na bázi)
> ==Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$. Nechť $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_m)$ je báze $V$ a $\vec{w}_1, \dots, \vec{w}_m \in W$ libovolné vektory.== Potom **existuje právě jedno $A \in \operatorname{Lin}(V, W)$ takové, že $A\vec{x}_i = \vec{w}_i$ pro všechna $i = 1, \dots, m$.**
>
> > [!note]- Důkaz
> > **Existence.** Každé $\vec{v} \in V$ má jediné vyjádření $\vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_m\vec{x}_m$ (souřadnice v bázi). Položme
> >
> > $$
> > A\vec{v} = \alpha_1\vec{w}_1 + \dots + \alpha_m\vec{w}_m.
> > $$
> >
> > Předpis je dobře definovaný, protože koeficienty $\alpha_i$ jsou určené jednoznačně. Je to složení dvou lineárních zobrazení: $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$ ([[věta o linearitě souřadnic|linearita souřadnic]]) a $(\alpha_1; \dots; \alpha_m) \mapsto \alpha_1\vec{w}_1 + \dots + \alpha_m\vec{w}_m$ (lineární stejným výpočtem jako [[věta o zobrazení zadaném sloupci|zobrazení zadané sloupci]]). Složení lineárních je lineární. A protože $[\vec{x}_i]^{\mathcal{X}} = \vec{e}_i$, je $A\vec{x}_i = \vec{w}_i$.
> >
> > **Jednoznačnost.** Splňuje-li to i $B \in \operatorname{Lin}(V, W)$, pak pro každé $\vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_m\vec{x}_m$ je
> >
> > $$
> > B\vec{v} = \alpha_1 B\vec{x}_1 + \dots + \alpha_m B\vec{x}_m = \alpha_1\vec{w}_1 + \dots + \alpha_m\vec{w}_m = A\vec{v},
> > $$
> >
> > podle [[věta o zachování lineárních kombinací|zachování lineárních kombinací]]. Tedy $B = A$.

^veta-zadani-na-bazi

> [!lidsky] Lidsky
> Báze je jako sada „řídicích knoflíků“: kam pošleš každý vektor báze, si vybereš úplně svobodně, a tím je celé zobrazení hotové, protože všechno ostatní je jejich kombinace a linearita kombinace zachovává. Třeba $A : \mathbb{R}^2 \to \mathbb{R}^2$ s $A(1; 1) = (3; 1)$ a $A(1; -1) = (1; -1)$ existuje právě jedno, a vyjde $A(x; y) = (2x + y;\ y)$ (příklad 20).

> [!pozor] Proč to musí být báze
> - Když $\mathcal{X}$ jen generuje, ale je LZ, předepsané hodnoty si můžou odporovat. Pro $\vec{x}_2 = 2\vec{x}_1$ musí platit $A\vec{x}_2 = 2A\vec{x}_1$, takže $\vec{w}_2 \ne 2\vec{w}_1$ nedovolí **žádné** lineární zobrazení. Padá existence.
> - Když je $\mathcal{X}$ LN, ale negeneruje, na vektorech mimo $\operatorname{span}\mathcal{X}$ není nic předepsáno a zobrazení jde dodefinovat mnoha způsoby. Padá jednoznačnost.

> [!veta] Důsledek 6.16 (lineární zobrazení = matice)
> ==Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$ konečné dimenze, $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_m)$ báze $V$ a $\mathcal{Y} = (\vec{y}_1, \dots, \vec{y}_n)$ báze $W$.== Potom je zobrazení $A \mapsto [A]^{\mathcal{X} \to \mathcal{Y}}$ **bijekce**
>
> $$
> \operatorname{Lin}(V, W) \longleftrightarrow \mathbb{F}^{n \times m}.
> $$
>
> > [!note]- Důkaz
> > **Prosté:** mají-li $A$, $B$ stejnou matici, je $[A\vec{x}_j]^{\mathcal{Y}} = [B\vec{x}_j]^{\mathcal{Y}}$ pro všechna $j$. Vektor je svými souřadnicemi určený, takže $A\vec{x}_j = B\vec{x}_j$, a podle jednoznačnosti ve větě výše $A = B$.
> >
> > **Na:** pro $M \in \mathbb{F}^{n \times m}$ polož $\vec{w}_j = m_{1j}\vec{y}_1 + \dots + m_{nj}\vec{y}_n$ (vektor, jehož souřadnice v $\mathcal{Y}$ jsou $j$-tý sloupec $M$). Podle věty existuje $A$ s $A\vec{x}_j = \vec{w}_j$, a ta má $[A]^{\mathcal{X} \to \mathcal{Y}} = M$.

^veta-korespondence

> [!lidsky] Lidsky
> Po zvolení bází je každé lineární zobrazení $V \to W$ zapsatelné jedinou maticí $n \times m$ a každá taková matice nějaké zobrazení popisuje. Lineární algebra „s polynomy, maticemi a funkcemi“ se tak převede na počítání s tabulkami čísel. Pozor jen, že ta korespondence **závisí na volbě bází**.

## §6 Skládání a součin matic

Proč je součin matic definovaný tak divně (řádek krát sloupec)? Protože přesně odpovídá [[složené zobrazení|skládání zobrazení]].

> [!veta] Věta 6.19 (matice složeného zobrazení)
> ==Buďte $U$, $V$, $W$ lineární prostory konečné dimenze s bázemi $\mathcal{X}$, $\mathcal{Y}$, $\mathcal{Z}$ a $A \in \operatorname{Lin}(U, V)$, $B \in \operatorname{Lin}(V, W)$.== Potom
>
> $$
> \mathbf{[BA]^{\mathcal{X} \to \mathcal{Z}} = [B]^{\mathcal{Y} \to \mathcal{Z}} \cdot [A]^{\mathcal{X} \to \mathcal{Y}}.}
> $$
>
> > [!note]- Důkaz
> > Porovnáme $j$-té sloupce. Vlevo je podle definice $[BA\vec{x}_j]^{\mathcal{Z}}$. Podle [[věta o souřadnicích obrazu|věty o souřadnicích obrazu]] (použité na $B$ a vektor $A\vec{x}_j$)
> >
> > $$
> > [B(A\vec{x}_j)]^{\mathcal{Z}} = [B]^{\mathcal{Y} \to \mathcal{Z}}[A\vec{x}_j]^{\mathcal{Y}},
> > $$
> >
> > a $[A\vec{x}_j]^{\mathcal{Y}}$ je $j$-tý sloupec $[A]^{\mathcal{X} \to \mathcal{Y}}$. Podle [[LAG 08 – Matice lineárního zobrazení a součin matic#^sloupce-soucinu|sloupcového pravidla]] je $[B]^{\mathcal{Y} \to \mathcal{Z}}$ krát $j$-tý sloupec $[A]^{\mathcal{X} \to \mathcal{Y}}$ právě $j$-tý sloupec součinu. Sloupce se shodují, matice taky.

^veta-slozeni

> [!lidsky] Lidsky
> „Nejdřív $A$, pak $B$“ v jazyce matic je „vynásob $[B][A]$“. Pořadí se čte stejně jako u zobrazení, **zprava doleva**: matice, která je blíž k vektoru, na něj působí první. Pro $\mathbb{F}^n$ s kanonickými bázemi to znamená prostě: matice složení je součin matic.

> [!example] Složení dvou zobrazení roviny
> $A(\vec{v}) = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}\vec{v}$ a $B(\vec{v}) = \begin{pmatrix} 3 & 0 \\ -1 & 1 \end{pmatrix}\vec{v}$ na $\mathbb{R}^2$, $C = A \circ B$ (nejdřív $B$). Pak
>
> $$
> [C]^{\mathcal{E}} = [A]^{\mathcal{E}}[B]^{\mathcal{E}} = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ -2 & 2 \end{pmatrix}.
> $$
>
> Kontrola na $\vec{e}_1$: $B\vec{e}_1 = (3; -1)$ a $A(3; -1) = (3 - 1;\ -2) = (2; -2)$, první sloupec sedí. Stejný typ úlohy je v ukázce k zápočtovému testu; procvičíš ho v příkladu 21.

## §7 Matice otočení

> [!veta] Příklad 6.17 (matice otočení)
> ==Otočení $R_\alpha : \mathbb{R}^2 \to \mathbb{R}^2$ o úhel $\alpha$ proti směru hodinových ručiček kolem počátku== je lineární a
>
> $$
> \mathbf{[R_\alpha]^{\mathcal{E}} = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}}, \qquad R_\alpha\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x\cos\alpha - y\sin\alpha \\ x\sin\alpha + y\cos\alpha \end{pmatrix}.
> $$
>
> > [!note]- Odvození
> > Linearitu otočení vidíme geometricky: otočí se celý rovnoběžník ze šipek, takže i jeho úhlopříčka ([[LAG 07 – Lineární zobrazení|minule]]), a natažená šipka zůstane natažená. Stačí tedy otočit $\vec{e}_1$ a $\vec{e}_2$ (sloupce matice). Jednotkový vektor $\vec{e}_1$ po otočení o $\alpha$ leží na jednotkové kružnici pod úhlem $\alpha$, tedy $R_\alpha\vec{e}_1 = (\cos\alpha; \sin\alpha)$. Vektor $\vec{e}_2$ je o $90°$ dál a po otočení míří pod úhlem $90° + \alpha$, tedy $R_\alpha\vec{e}_2 = (\cos(90° + \alpha); \sin(90° + \alpha)) = (-\sin\alpha; \cos\alpha)$.

^def-matice-otoceni

> [!lidsky] Lidsky
> Vzorec si nemusíš pamatovat, stačí obrázek: první sloupec je „kam se otočí $(1; 0)$“, druhý „kam se otočí $(0; 1)$“, a ten je o čtvrt otáčky dál, proto má $-\sin$ nahoře. Kontrola na $\alpha = 90°$: vyjde $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, tedy otočení $(x; y) \mapsto (-y; x)$ z minula.

> [!obrazek] Kam se otočí jednotkové vektory
> ![[lag08-otoceni.png]]
> *Světlé šipky jsou $\vec{e}_1$, $\vec{e}_2$, syté jejich obrazy po otočení o $\alpha$ (zelené oblouky). Tečkované čáry ukazují složky: modrý obraz má $(\cos\alpha; \sin\alpha)$, oranžový $(-\sin\alpha; \cos\alpha)$.*

> [!navic] Zpátky k §4
> Pro $\alpha = 45°$ je $\cos\alpha = \sin\alpha = \tfrac{1}{\sqrt{2}}$, takže $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \sqrt{2}\,[R_{45°}]^{\mathcal{E}}$. Zobrazení $A(x; y) = (x - y;\ x + y)$ je proto otočení o $45°$ složené se [[stejnolehlost|stejnolehlostí]] s koeficientem $\sqrt{2}$, přesně jak to ukazuje mřížka.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč musí mít $A$ tolik sloupců, kolik má $B$ řádků, aby šel spočítat součin $AB$? Jaký rozměr má výsledek?
> $[AB]_{ij} = \sum_k a_{ik}b_{kj}$ páruje $k$-tý prvek **řádku $A$** s $k$-tým prvkem **sloupce $B$**, takže musí být stejně dlouhé. Pro $A \in \mathbb{F}^{n \times m}$, $B \in \mathbb{F}^{m \times l}$ je $AB \in \mathbb{F}^{n \times l}$.

> [!karta|02]- Jak souvisí $j$-tý sloupec součinu $AB$ se sloupci matice $B$? Proč?
> Je to **$A\vec{b}_j$**, tedy $A(\vec{b}_1 \cdots \vec{b}_l) = (A\vec{b}_1 \cdots A\vec{b}_l)$. Složky $j$-tého sloupce jsou $\sum_k a_{ik}b_{kj}$, a to jsou přesně složky $A\vec{b}_j$.

> [!karta|03]- Proč součin matic obecně není komutativní? Kdy $BA$ ani nedává stejný rozměr jako $AB$?
> Odpovídá skládání zobrazení a tam **záleží na pořadí**. Pro $A \in \mathbb{F}^{2 \times 3}$, $B \in \mathbb{F}^{3 \times 2}$ je $AB$ typu $2 \times 2$, ale $BA$ typu $3 \times 3$. I u čtvercových: $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 4 & 2 \end{pmatrix} \ne \begin{pmatrix} 1 & -1 \\ 4 & 2 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$.

> [!karta|04]- Proč má matice $[A]^{\mathcal{X} \to \mathcal{Y}}$ pro $\dim V = m$ a $\dim W = n$ rozměr $n \times m$, a ne $m \times n$?
> Sloupců je tolik, kolik je vektorů **vstupní báze** $\mathcal{X}$, tedy $m$. Každý sloupec $[A\vec{x}_j]^{\mathcal{Y}}$ jsou souřadnice ve **výstupní bázi** $\mathcal{Y}$, má tedy $n$ složek.

> [!karta|05]- Jak dokážeš $[A\vec{x}]^{\mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}}[\vec{x}]^{\mathcal{X}}$?
> $\vec{x} = \xi_1\vec{x}_1 + \dots + \xi_m\vec{x}_m$, linearita $A$ dá $A\vec{x} = \sum \xi_j A\vec{x}_j$, **linearita souřadnic** dá $[A\vec{x}]^{\mathcal{Y}} = \sum \xi_j [A\vec{x}_j]^{\mathcal{Y}}$. To je kombinace sloupců matice s koeficienty $\xi_j$, tedy **matice krát $[\vec{x}]^{\mathcal{X}}$**.

> [!karta|06]- Proč je $[A]^{\mathcal{X} \to \mathcal{Y}}$ jediná matice $M$ splňující $M[\vec{x}]^{\mathcal{X}} = [A\vec{x}]^{\mathcal{Y}}$ pro všechna $\vec{x} \in V$?
> Dosaď $\vec{x} = \vec{x}_j$: $[\vec{x}_j]^{\mathcal{X}} = \vec{e}_j$ a **$M\vec{e}_j$ je $j$-tý sloupec $M$**. Ten se tedy musí rovnat $[A\vec{x}_j]^{\mathcal{Y}}$, $j$-tému sloupci $[A]^{\mathcal{X} \to \mathcal{Y}}$.

> [!karta|07]- Proč je pro $A : \mathbb{F}^m \to \mathbb{F}^n$ matice $[A]^{\mathcal{E} \to \mathcal{E}}$ stejná jako matice $(A\vec{e}_1 \cdots A\vec{e}_m)$ z minulé přednášky?
> V kanonické bázi jsou souřadnice vektoru jeho složky: **$[\vec{v}]^{\mathcal{E}} = \vec{v}$**. Sloupce $[A\vec{e}_j]^{\mathcal{E}}$ jsou tedy přímo $A\vec{e}_j$.

> [!karta|08]- Proč má matice derivace $[D]^{\mathcal{E}}$ na $\mathbb{R}^{\le 2}[x]$ v bázi $(1, x, x^2)$ nulový první sloupec a nulový poslední řádek?
> První sloupec je $[D(1)]^{\mathcal{E}}$ a **derivace konstanty je 0**. Poslední řádek je koeficient u $x^2$ ve výsledku a derivace polynomu stupně $\le 2$ má **stupeň $\le 1$**, takže je vždy nulový.

> [!karta|09]- Jak dokážeš existenci ve větě o zadání lineárního zobrazení na bázi?
> Pro $\vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_m\vec{x}_m$ polož $A\vec{v} = \alpha_1\vec{w}_1 + \dots + \alpha_m\vec{w}_m$. **Dobře definované**, protože souřadnice jsou jednoznačné; **lineární** jako složení souřadnic a zobrazení zadaného sloupci; $A\vec{x}_i = \vec{w}_i$, protože $[\vec{x}_i]^{\mathcal{X}} = \vec{e}_i$.

> [!karta|10]- Jak dokážeš jednoznačnost ve větě o zadání lineárního zobrazení na bázi?
> Má-li i $B$ hodnoty $B\vec{x}_i = \vec{w}_i$, pak podle **zachování lineárních kombinací** $B\vec{v} = \sum \alpha_i B\vec{x}_i = \sum \alpha_i\vec{w}_i = A\vec{v}$ pro každé $\vec{v}$. Tedy $B = A$.

> [!karta|11]- Proč musí být ve větě o zadání lineárního zobrazení na bázi $\mathcal{X}$ báze? Co se pokazí, když je jen generující, nebo jen LN?
> **Jen generující (LZ):** hodnoty si můžou odporovat, např. $\vec{x}_2 = 2\vec{x}_1$, ale $\vec{w}_2 \ne 2\vec{w}_1$, a pak zobrazení **neexistuje**. **Jen LN (negeneruje):** mimo $\operatorname{span}\mathcal{X}$ není nic určené, zobrazení **není jednoznačné**.

> [!karta|12]- Proč je $A \mapsto [A]^{\mathcal{X} \to \mathcal{Y}}$ bijekce $\operatorname{Lin}(V, W) \to \mathbb{F}^{n \times m}$?
> **Prosté:** stejná matice ⇒ stejné $[A\vec{x}_j]^{\mathcal{Y}}$ ⇒ stejné $A\vec{x}_j$ ⇒ stejné zobrazení (jednoznačnost zadání na bázi). **Na:** ze sloupců $M$ sestav $\vec{w}_j$ se souřadnicemi $j$-tého sloupce a podle **existence** vezmi $A$ s $A\vec{x}_j = \vec{w}_j$.

> [!karta|13]- Proč je matice složeného zobrazení součin matic? V jakém pořadí se násobí?
> $j$-tý sloupec $[BA]^{\mathcal{X} \to \mathcal{Z}}$ je $[B(A\vec{x}_j)]^{\mathcal{Z}} = [B]^{\mathcal{Y} \to \mathcal{Z}}[A\vec{x}_j]^{\mathcal{Y}}$, tedy $[B]$ krát $j$-tý sloupec $[A]$, a to je $j$-tý sloupec součinu. **$[BA] = [B][A]$**, stejné pořadí jako u zobrazení (nejdřív $A$, čte se zprava).

> [!karta|14]- Jak odvodíš matici otočení roviny o úhel $\alpha$?
> Sloupce jsou obrazy $\vec{e}_1$, $\vec{e}_2$. $\vec{e}_1$ se otočí na **$(\cos\alpha; \sin\alpha)$**, $\vec{e}_2$ (o $90°$ dál) na **$(-\sin\alpha; \cos\alpha)$**. Proto $\begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}$.

### Příklady na procvičení

> [!priklad|15]- Spočítej $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 3 & -2 \\ 0 & 3 \end{pmatrix}$.
> První sloupec: $(1 + 6 + 0;\ 4 + 15 + 0) = (7; 19)$. Druhý: $(-1 - 4 + 9;\ -4 - 10 + 18) = (4; 4)$.
>
> **$\begin{pmatrix} 7 & 4 \\ 19 & 4 \end{pmatrix}$**

> [!priklad|16]- Spočítej $AB$ a $BA$ pro $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 1 & -1 \\ 4 & 2 \end{pmatrix}$.
> $AB = \begin{pmatrix} 2 + 4 & -2 + 2 \\ 0 + 12 & 0 + 6 \end{pmatrix} = $ **$\begin{pmatrix} 6 & 0 \\ 12 & 6 \end{pmatrix}$**, $BA = \begin{pmatrix} 2 + 0 & 1 - 3 \\ 8 + 0 & 4 + 6 \end{pmatrix} = $ **$\begin{pmatrix} 2 & -2 \\ 8 & 10 \end{pmatrix}$**. Liší se.

> [!priklad|17]- Urči $[D]^{\mathcal{E}}$ derivace na $\mathbb{R}^{\le 3}[x]$, $\mathcal{E} = (1, x, x^2, x^3)$, a spočítej s ní $D(2 - x + 4x^3)$.
> $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, $D(x^3) = 3x^2$, takže $[D]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$. $[p]^{\mathcal{E}} = (2; -1; 0; 4)$, součin $(-1; 0; 12; 0)$.
>
> **$D(2 - x + 4x^3) = -1 + 12x^2$**

> [!priklad|18]- Urči $[A]^{\mathcal{E}}$ pro $A(x; y) = (x - y;\ x + y)$ a spočítej s ní $A(3; 1)$.
> $A\vec{e}_1 = (1; 1)$, $A\vec{e}_2 = (-1; 1)$, $[A]^{\mathcal{E}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. $A(3; 1) = 3(1; 1) + 1 \cdot (-1; 1) = $ **$(2; 4)$**.

> [!priklad|19]- Napiš matici otočení o $60°$ a spočítej obraz vektoru $(2; 0)$.
> $\cos 60° = \tfrac{1}{2}$, $\sin 60° = \tfrac{\sqrt{3}}{2}$: $[R_{60°}]^{\mathcal{E}} = \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$. $R_{60°}(2; 0) = 2 \cdot (\tfrac{1}{2}; \tfrac{\sqrt{3}}{2}) = $ **$(1; \sqrt{3}) \approx (1; 1{,}73)$**.

> [!priklad|20]- Lineární $A : \mathbb{R}^2 \to \mathbb{R}^2$ splňuje $A(1; 1) = (3; 1)$ a $A(1; -1) = (1; -1)$. Urči $A(x; y)$ a $[A]^{\mathcal{E}}$.
> $((1; 1), (1; -1))$ je báze $\mathbb{R}^2$ (dva LN vektory v prostoru dimenze 2), takže $A$ existuje a je jediné. $(x; y) = \tfrac{x + y}{2}(1; 1) + \tfrac{x - y}{2}(1; -1)$, tedy $A(x; y) = \tfrac{x + y}{2}(3; 1) + \tfrac{x - y}{2}(1; -1) = $ **$(2x + y;\ y)$**, $[A]^{\mathcal{E}} = $ **$\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$**.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|21]- $A(\vec{v}) = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}\vec{v}$, $B(\vec{v}) = \begin{pmatrix} 2 & 0 \\ 1 & -1 \end{pmatrix}\vec{v}$ na $\mathbb{R}^2$ a $C(\vec{v}) = A(B(\vec{v}))$. Najdi $[C]^{\mathcal{E} \to \mathcal{E}}$ a spočti $C(\vec{u} - 2\vec{w})$ pro $\vec{u} = (1; 2)$, $\vec{w} = (0; 1)$.
> V kanonické bázi je $[A]^{\mathcal{E}}$ a $[B]^{\mathcal{E}}$ přímo zadaná matice ($[\vec{v}]^{\mathcal{E}} = \vec{v}$). Podle věty o matici složeného zobrazení
>
> $$
> [C]^{\mathcal{E}} = [A]^{\mathcal{E}}[B]^{\mathcal{E}} = \begin{pmatrix} 1 \cdot 2 + 2 \cdot 1 & 1 \cdot 0 + 2 \cdot (-1) \\ -1 \cdot 2 + 3 \cdot 1 & -1 \cdot 0 + 3 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 4 & -2 \\ 1 & -3 \end{pmatrix}.
> $$
>
> $\vec{u} - 2\vec{w} = (1; 0)$, takže $C(\vec{u} - 2\vec{w}) = [C]^{\mathcal{E}}(1; 0) = $ **$(4; 1)$** (první sloupec). Kontrola: $B(1; 0) = (2; 1)$, $A(2; 1) = (4; 1)$.
>
> **$[C]^{\mathcal{E}} = \begin{pmatrix} 4 & -2 \\ 1 & -3 \end{pmatrix}$, $C(\vec{u} - 2\vec{w}) = (4; 1)$**

> [!priklad|22]- $A : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $A(ax^2 + bx + c) = (b + c)x^2 + 2ax - c$. Najdi $[A]^{\mathcal{C} \to \mathcal{B}}$ pro $\mathcal{B} = (1, x, x^2)$ a $\mathcal{C} = (x^2 + 1,\ x - 2,\ 3x^2)$.
> $\mathcal{C}$ je báze: $\alpha(x^2 + 1) + \beta(x - 2) + \gamma \cdot 3x^2 = 0$ dá u $x$: $\beta = 0$, u $1$: $\alpha - 2\beta = 0$, tedy $\alpha = 0$, u $x^2$: $\alpha + 3\gamma = 0$, tedy $\gamma = 0$. Tři LN vektory v prostoru dimenze 3 tvoří bázi. Sloupce jsou souřadnice obrazů v $\mathcal{B}$:
>
> - $A(x^2 + 1)$ ($a = 1$, $b = 0$, $c = 1$) $= x^2 + 2x - 1$, souřadnice $(-1; 2; 1)$,
> - $A(x - 2)$ ($a = 0$, $b = 1$, $c = -2$) $= -x^2 + 2$, souřadnice $(2; 0; -1)$,
> - $A(3x^2)$ ($a = 3$, $b = c = 0$) $= 6x$, souřadnice $(0; 6; 0)$.
>
> **$[A]^{\mathcal{C} \to \mathcal{B}} = \begin{pmatrix} -1 & 2 & 0 \\ 2 & 0 & 6 \\ 1 & -1 & 0 \end{pmatrix}$**

> [!priklad|23]- Dokaž, že $\begin{pmatrix} 2 & 3 \\ -1 & -1 \end{pmatrix}$ je $[A]^{\mathcal{E} \to \mathcal{X}}$ pro $A(x; y) = (x + 2y;\ y)$ a $\mathcal{X} = ((1; 1), (1; 2))$.
> $\mathcal{X}$ je báze: dva vektory, které nejsou násobkem jeden druhého, jsou LN, a $\dim\mathbb{R}^2 = 2$. Sloupce mají být $[A\vec{e}_j]^{\mathcal{X}}$:
>
> - $A\vec{e}_1 = (1; 0) = 2(1; 1) - 1 \cdot (1; 2)$, tedy $[A\vec{e}_1]^{\mathcal{X}} = (2; -1)$,
> - $A\vec{e}_2 = (2; 1) = 3(1; 1) - 1 \cdot (1; 2)$, tedy $[A\vec{e}_2]^{\mathcal{X}} = (3; -1)$.
>
> Sloupce se shodují se zadanou maticí, **je to $[A]^{\mathcal{E} \to \mathcal{X}}$**.

> [!priklad|24]- $A : \mathbb{R}^{2 \times 2} \to \mathbb{R}^{2 \times 2}$, $A\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} b & 0 \\ 0 & a + d \end{pmatrix}$. Najdi $[A]^{\mathcal{M} \to \mathcal{X}}$ pro $\mathcal{M} = \left(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}\right)$ a kanonickou bázi $\mathcal{X} = (E_{11}, E_{12}, E_{21}, E_{22})$.
> $\mathcal{M}$ je báze: $\alpha M_1 + \beta M_2 + \gamma M_3 + \delta M_4 = \begin{pmatrix} \alpha & 2\beta \\ \gamma & \gamma - \delta \end{pmatrix} = 0$ dá $\alpha = \beta = \gamma = \delta = 0$, a $\dim\mathbb{R}^{2 \times 2} = 4$. V kanonické bázi jsou souřadnice matice její prvky po řádcích $(a; b; c; d)$:
>
> - $A(M_1) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \to (0; 0; 0; 1)$, $A(M_2) = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \to (2; 0; 0; 0)$,
> - $A(M_3) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \to (0; 0; 0; 1)$, $A(M_4) = \begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix} \to (0; 0; 0; -1)$.
>
> **$[A]^{\mathcal{M} \to \mathcal{X}} = \begin{pmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 1 & -1 \end{pmatrix}$**

> [!priklad|25]- Najdi $[A]^{\mathcal{X}}$ operátoru $A(x; y) = (x - y;\ x + y)$ v bázi $\mathcal{X} = ((1; 0), (1; 1))$.
> $\mathcal{X}$ je báze (dva LN vektory v $\mathbb{R}^2$). Na vstupu i výstupu je $\mathcal{X}$:
>
> - $A(1; 0) = (1; 1) = 0 \cdot (1; 0) + 1 \cdot (1; 1)$, souřadnice $(0; 1)$,
> - $A(1; 1) = (0; 2) = -2 \cdot (1; 0) + 2 \cdot (1; 1)$, souřadnice $(-2; 2)$.
>
> **$[A]^{\mathcal{X}} = \begin{pmatrix} 0 & -2 \\ 1 & 2 \end{pmatrix}$** (v kanonické bázi by vyšlo $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$: jiná báze, jiná matice téhož zobrazení).

---
← [[LAG 07 – Lineární zobrazení|14. 10. 2026 Lineární zobrazení]]

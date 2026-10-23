---
predmet: LAG
prednaska: 9
datum: 2026-10-21
zdroj: "V poznámkách kap. 6.2 (pozn. 6.20–6.24), 6.3 (pozn. 6.25–6.27) a 6.4 (pozn. 6.28–6.31, 6.34)"
tags: [prednaska, LAG]
---

# LAG 09 – Algebra matic a transformace souřadnic

*Přednáška 9 · středa 21. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `asociativita součinu matic` · `otočení + stejnolehlost` · `jednotková a nulová matice` · `Kroneckerovo delta` · `matice přechodu` · `[v]^Y = [id]^{X→Y}[v]^X` · `Lin(V, W) jako lineární prostor` · `[A + B] = [A] + [B]`

Minule jsme zjistili, že skládání lineárních zobrazení odpovídá násobení jejich matic. Dnes z toho vytěžíme pravidla počítání s maticemi: součin je **asociativní** (závorky jsou zbytečné), **jednotková matice** se chová jako jednička a nulová jako nula. Pak použijeme matici identického zobrazení ve dvou různých bázích jako stroj na **přepočet souřadnic** z jedné báze do druhé. Na konec začneme sčítat lineární zobrazení a násobit je číslem: $\operatorname{Lin}(V, W)$ je sám lineární prostor.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[asociativita násobení matic]] | $(AB)C = A(BC)$ | $(AB)\vec{v} = A(B\vec{v}) = (7; 3)$ |
| [[věta o matici složeného zobrazení]] (minule) | $[AB]^{\mathcal{X} \to \mathcal{Z}} = [A]^{\mathcal{Y} \to \mathcal{Z}}[B]^{\mathcal{X} \to \mathcal{Y}}$ | $[R_{45°} \circ S_{\sqrt{2}}]^{\mathcal{E}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ |
| [[jednotková matice]] | $[E_n]_{ij} = \delta_{ij}$, jedničky na diagonále | $[\mathrm{id}]^{\mathcal{X}} = E_n$ pro každou bázi $\mathcal{X}$ |
| [[nulová matice]] | všechny prvky $0$ | $O \in \mathbb{F}^{m \times n}$ |
| [[Kroneckerovo delta]] | $\delta_{ij} = 1$ pro $i = j$, jinak $0$ | $\delta_{22} = 1$, $\delta_{23} = 0$ |
| [[věta o násobení jednotkovou maticí]] | $AE_n = A = E_mA$ pro $A \in \mathbb{F}^{m \times n}$ | |
| [[matice přechodu]] | $[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}} = ([\vec{x}_1]^{\mathcal{Y}} \cdots [\vec{x}_n]^{\mathcal{Y}})$ | $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix}$ |
| [[věta o transformaci souřadnic]] | $[\vec{v}]^{\mathcal{Y}} = [\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}[\vec{v}]^{\mathcal{X}}$ | $[(1; 3)]^{\mathcal{X}} = (2; 1)$ |
| [[součet lineárních zobrazení]] | $(A + B)\vec{x} = A\vec{x} + B\vec{x}$ | |
| [[skalární násobek lineárního zobrazení]] | $(\alpha A)\vec{x} = \alpha(A\vec{x})$ | |
| [[věta o lineárním prostoru lineárních zobrazení]] | $\operatorname{Lin}(V, W)$ s těmito operacemi je lineární prostor | |
| [[věta o matici součtu a násobku zobrazení]] | $[A + B] = [A] + [B]$, $[\alpha A] = \alpha[A]$ | $R_{45°} = \tfrac{\sqrt{2}}{2}A$ |

## §1 Asociativita součinu matic

Skládání zobrazení je asociativní: pro $f : A \to B$, $g : B \to C$, $h : C \to D$ je $(h \circ g) \circ f = h \circ (g \circ f)$, protože obě strany pošlou $x$ na $h(g(f(x)))$ ([[asociativita skládání zobrazení]]). Matice jsou zobrazení a součin matic je matice složení, takže totéž platí i pro matice.

> [!veta] Důsledek (asociativita násobení matic) · pozn. 6.20
> ==Buď $\mathbb{F}$ číselné těleso, $A \in \mathbb{F}^{k \times l}$, $B \in \mathbb{F}^{l \times m}$, $C \in \mathbb{F}^{m \times n}$.== Potom
>
> $$
> \mathbf{(AB)C = A(BC).}
> $$
>
> > [!note]- Důkaz přímo z definice součinu (pozn. 6.10)
> > Porovnáme prvek na místě $(i, j)$:
> >
> > $$
> > [(AB)C]_{ij} = \sum_{x} [AB]_{ix}c_{xj} = \sum_{x}\sum_{y} a_{iy}b_{yx}c_{xj}, \qquad [A(BC)]_{ij} = \sum_{y} a_{iy}[BC]_{yj} = \sum_{y}\sum_{x} a_{iy}b_{yx}c_{xj}.
> > $$
> >
> > Je to tentýž konečný součet, jen sečtený v jiném pořadí.

^veta-asociativita-matic

> [!lidsky] Lidsky
> U součinu tří matic nezáleží na tom, kterou dvojici vynásobíš dřív, takže se závorky nepíšou: $ABC$. **Pořadí** matic ale měnit nesmíš, součin není komutativní. Stejně je to s výrobní linkou: je jedno, jestli první dva stroje spojíš do jednoho, nebo poslední dva, ale stroje nesmíš přeházet.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, $\vec{v} = (2; 1)$. Napřed $AB = \begin{pmatrix} 2 & 3 \\ 1 & 1 \end{pmatrix}$ a $(AB)\vec{v} = (4 + 3;\ 2 + 1) = (7; 3)$. Jinak: $B\vec{v} = (1; 3)$ a $A(B\vec{v}) = (1 + 6;\ 3) = (7; 3)$. Oba postupy dají **$(7; 3)$**.

## §2 Příklad: otočení a zvětšení

> [!example] Příklad 6.21 · $A(x; y) = (x - y;\ x + y)$
> Zobrazení $A$ má v kanonické bázi matici $[A]^{\mathcal{E}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. Z obrázku to vypadá jako otočení o $45°$ spolu se zvětšením $\sqrt{2}$krát. Ověříme to násobením matic: [[matice otočení]] o $45°$ a matice [[stejnolehlost|stejnolehlosti]] $S_k : \vec{x} \mapsto k\vec{x}$ s $k = \sqrt{2}$ jsou
>
> $$
> [R_{45°}]^{\mathcal{E}} = \begin{pmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{pmatrix}, \qquad [S_{\sqrt{2}}]^{\mathcal{E}} = \begin{pmatrix} \sqrt{2} & 0 \\ 0 & \sqrt{2} \end{pmatrix},
> $$
>
> a podle [[věta o matici složeného zobrazení|věty o matici složeného zobrazení]]
>
> $$
> [R_{45°} \circ S_{\sqrt{2}}]^{\mathcal{E}} = \begin{pmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{pmatrix}\begin{pmatrix} \sqrt{2} & 0 \\ 0 & \sqrt{2} \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = [A]^{\mathcal{E}}.
> $$
>
> Matice určuje zobrazení jednoznačně, takže **$A = R_{45°} \circ S_{\sqrt{2}}$**. V opačném pořadí vyjde totéž, $S_{\sqrt{2}} \circ R_{45°} = A$, protože stejnolehlost komutuje se vším (její matice je $\sqrt{2}E$, viz §3).

> [!obrazek] Co $A$ udělá s jednotkovým čtvercem
> ![[lag09-otoceni.png]]
> *Vlevo modrý $\vec{e}_1$ a oranžový $\vec{e}_2$, vpravo jejich obrazy $A\vec{e}_1 = (1; 1)$ a $A\vec{e}_2 = (-1; 1)$ (sloupce $[A]^{\mathcal{E}}$). Zelený čtverec je otočený o $45°$ (červený oblouk) a má stranu $\sqrt{2}$.*

## §3 Identita, jednotková a nulová matice

Skládání má neutrální prvek, [[identické zobrazení]]: $f \circ \mathrm{id}_A = f = \mathrm{id}_B \circ f$ pro každé $f : A \to B$. Jeho maticí v kanonické bázi je $[\mathrm{id}]^{\mathcal{E}} = (\vec{e}_1\ \vec{e}_2 \cdots \vec{e}_n)$, a ta dostala vlastní jméno.

> [!definice] Definice ♥ · pozn. 6.23 · jednotková a nulová matice
> Matici
>
> $$
> E_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \in \mathbb{F}^{n \times n}, \qquad \text{tj. } [E_n]_{ij} = \begin{cases} 1 & \text{pro } i = j, \\ 0 & \text{pro } i \ne j, \end{cases}
> $$
>
> nazýváme *jednotková matice* (rozměrů $n \times n$). Když je rozměr jasný, píšeme jen $E$.
>
> Matici $O_{m,n} \in \mathbb{F}^{m \times n}$, jejíž všechny prvky jsou nulové, nazýváme *nulová matice* (často jen $O$). Je to nulový vektor prostoru $\mathbb{F}^{m \times n}$.

^def-jednotkova-matice

> [!lidsky] Lidsky
> Jednotková matice je **maticová jednička**: jedničky na diagonále, jinde nuly. Jako zobrazení nechá každý vektor na místě, protože je to matice identity, a to v **jakékoli** bázi: $j$-tý vektor báze se v té samé bázi zapíše jako $(0; \dots; 1; \dots; 0)$. Nulová matice je **maticová nula**: přičtená nic nezmění a jako zobrazení pošle všechno do $\vec{0}$.

> [!example] Příklad
> $E_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $E_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ a $E_2\begin{pmatrix} 5 \\ -2 \end{pmatrix} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}$. Nulová matice $O_{2,3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ pošle každé $\vec{x} \in \mathbb{R}^3$ na $(0; 0)$. Nepříklad: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ jednotková není, $(0; 1)$ pošle na $(1; 1)$.

> [!definice] Poznámka · pozn. 6.24 · Kroneckerovo delta
> Symbol *Kroneckerovo delta* je definován podmínkou
>
> $$
> \delta_{ij} = \begin{cases} 1 & \text{jestliže } i = j, \\ 0 & \text{jestliže } i \ne j. \end{cases}
> $$
>
> Je to jen symbol, ne matice nějakého rozměru; $i$ a $j$ jsou většinou indexy. Jednotkovou matici s ním zapíšeme stručně: $[E_n]_{ij} = \delta_{ij}$.

^def-kroneckerovo-delta

> [!lidsky] Lidsky
> Zkratka pro „**1, když se indexy rovnají, jinak 0**“. V součtu funguje jako síto: ze všech členů propustí jediný, ten se shodnými indexy.

> [!example] Příklad
> $\delta_{22} = 1$, $\delta_{23} = 0$, $\delta_{31} = 0$. V součtu $\sum_{k=1}^{3} a_k\delta_{k2} = a_1 \cdot 0 + a_2 \cdot 1 + a_3 \cdot 0 = a_2$. Proto $[AE]_{ij} = \sum_k a_{ik}\delta_{kj} = a_{ij}$, tedy $AE = A$.

> [!veta] Tvrzení (násobení jednotkovou maticí) · pozn. 6.22
> ==Buď $A \in \mathbb{F}^{m \times n}$.== Potom
>
> $$
> \mathbf{AE_n = A = E_mA.}
> $$
>
> Je to maticová obdoba $f \circ \mathrm{id}_A = f = \mathrm{id}_B \circ f$.

^veta-jednotkova-matice

> [!lidsky] Lidsky
> Násobit jednotkovou maticí je jako násobit číslo jedničkou: nic se nezmění. Jen musí mít správný rozměr: **zprava** tolik řádků, kolik má $A$ sloupců ($n$), **zleva** tolik sloupců, kolik má $A$ řádků ($m$).

> [!example] Příklad
> Pro $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \in \mathbb{R}^{2 \times 3}$ je $AE_3 = A$ i $E_2A = A$. Součin $AE_2$ neexistuje: $A$ má 3 sloupce, $E_2$ jen 2 řádky.

## §4 Transformace souřadnic

Hledat souřadnice vektoru v nekanonické bázi znamená řešit soustavu. Pro jeden vektor to jde, pro sto vektorů bychom stokrát řešili skoro tutéž soustavu. Přiřazení souřadnic je ale lineární ([[věta o linearitě souřadnic]]), takže má matici, a s ní je přepočet jen násobení.

> [!example] Příklad 6.25 · souřadnice v bázi $\mathcal{X} = ((1; 1), (-1; 1))$
> Chceme pro $\vec{v} \in \mathbb{R}^2$ zadané kanonickými souřadnicemi najít $[\vec{v}]^{\mathcal{X}}$. Triviálně $\vec{v} = \mathrm{id}\,\vec{v}$, takže podle [[věta o souřadnicích obrazu|věty o souřadnicích obrazu]]
>
> $$
> [\vec{v}]^{\mathcal{X}} = [\mathrm{id}\,\vec{v}]^{\mathcal{X}} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}[\vec{v}]^{\mathcal{E}}.
> $$
>
> Sloupce $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$ jsou vektory kanonické báze vyjádřené v bázi $\mathcal{X}$:
>
> $$
> \vec{e}_1 = \tfrac{1}{2}(\vec{x}_1 - \vec{x}_2) \Rightarrow [\vec{e}_1]^{\mathcal{X}} = \begin{pmatrix} 1/2 \\ -1/2 \end{pmatrix}, \qquad \vec{e}_2 = \tfrac{1}{2}(\vec{x}_1 + \vec{x}_2) \Rightarrow [\vec{e}_2]^{\mathcal{X}} = \begin{pmatrix} 1/2 \\ 1/2 \end{pmatrix},
> $$
>
> tedy $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix}$ a pro každé $\vec{v} = (v_1; v_2)$ je $[\vec{v}]^{\mathcal{X}} = (\tfrac{1}{2}v_1 + \tfrac{1}{2}v_2;\ -\tfrac{1}{2}v_1 + \tfrac{1}{2}v_2)$. Například $[(1; 3)]^{\mathcal{X}} = (2; 1)$; kontrola: $2(1; 1) + 1 \cdot (-1; 1) = (1; 3)$.
>
> Opačný směr je mnohem snazší: $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$ má ve sloupcích $[\vec{x}_j]^{\mathcal{E}} = \vec{x}_j$, tedy prostě vektory báze: $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.

> [!obrazek] Stejný vektor, dvoje souřadnice
> ![[lag09-prechod.png]]
> *Šedá mřížka patří kanonické bázi, zelená bázi $\mathcal{X}$ (modrý $\vec{x}_1$, oranžový $\vec{x}_2$). Červený vektor $\vec{v}$ je v kanonické mřížce $(1; 3)$, v zelené mřížce dva kroky po $\vec{x}_1$ a jeden po $\vec{x}_2$, tedy $[\vec{v}]^{\mathcal{X}} = (2; 1)$.*

> [!definice] Definice ♥ · pozn. 6.26 · matice přechodu
> Buď $V$ lineární prostor nad tělesem $\mathbb{F}$ konečné dimenze a nechť $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ a $\mathcal{Y}$ jsou jeho báze. Matici
>
> $$
> [\mathrm{id}_V]^{\mathcal{X} \to \mathcal{Y}} = \big([\vec{x}_1]^{\mathcal{Y}} \cdots [\vec{x}_n]^{\mathcal{Y}}\big) \in \mathbb{F}^{n \times n}
> $$
>
> nazýváme *matice přechodu* nebo také *matice transformace souřadnic* od báze $\mathcal{X}$ k bázi $\mathcal{Y}$.

^def-matice-prechodu

> [!lidsky] Lidsky
> **Překladová tabulka** mezi dvěma bázemi: do $j$-tého sloupce napíšeš, jak se $j$-tý vektor „staré“ báze $\mathcal{X}$ vyjádří ve vektorech „nové“ báze $\mathcal{Y}$. Vstupní báze dává vektory, výstupní báze jazyk souřadnic. Pak už souřadnice libovolného vektoru přeložíš jedním násobením.

> [!example] Příklad
> V $\mathbb{R}^2$ je $\mathcal{X} = ((2; 1), (1; 1))$. Pak $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ (sloupce jsou vektory báze). Pro opačný směr vyjádříme $\vec{e}_1 = (2; 1) - (1; 1)$ a $\vec{e}_2 = -(2; 1) + 2(1; 1)$, takže $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$. Nepříklad: $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ **není** $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$, i když obsahuje „vektory báze“; směr šipky rozhoduje.

> [!veta] Pozorování (transformace souřadnic) · pozn. 6.27
> ==Buď $V$ lineární prostor nad $\mathbb{F}$ konečné dimenze, $\mathcal{X}$ a $\mathcal{Y}$ jeho báze a $\vec{v} \in V$.== Potom
>
> $$
> \mathbf{[\vec{v}]^{\mathcal{Y}} = [\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}[\vec{v}]^{\mathcal{X}}.}
> $$
>
> > [!note]- Důkaz
> > Je to [[věta o souřadnicích obrazu]] $[A\vec{v}]^{\mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}}[\vec{v}]^{\mathcal{X}}$ pro $A = \mathrm{id}_V$, protože $\mathrm{id}\,\vec{v} = \vec{v}$.

^veta-transformace-souradnic

> [!lidsky] Lidsky
> Znáš souřadnice v jedné bázi a chceš je v jiné? Vynásob je maticí přechodu. Šipka v indexu ukazuje směr překladu a musí navazovat: $[\cdot]^{\mathcal{X} \to \mathcal{Y}}$ bere souřadnice v $\mathcal{X}$ a vrací souřadnice v $\mathcal{Y}$.

> [!example] Příklad
> S bází $\mathcal{X} = ((2; 1), (1; 1))$ z předchozího příkladu: $[(3; 4)]^{\mathcal{X}} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}(3; 4) = (3 - 4;\ -3 + 8) = (-1; 5)$. Kontrola: $-(2; 1) + 5(1; 1) = (3; 4)$.

> [!navic] Značení na cvičení
> Na cvičení se matice přechodu píše $T_{\mathcal{X} \to \mathcal{Y}}$ („matice transformace souřadnic z báze $\mathcal{X}$ do báze $\mathcal{Y}$“) a souřadnice $[\vec{v}]_{\mathcal{X}}$. Vztah z pozorování má pak tvar $[\vec{v}]_{\mathcal{Y}} = T_{\mathcal{X} \to \mathcal{Y}}[\vec{v}]_{\mathcal{X}}$. Je to totéž.

> [!navic] Tam a zpátky
> Matice přechodu tam a zpátky jsou navzájem inverzní: podle [[věta o matici složeného zobrazení|věty o matici složeného zobrazení]] je $[\mathrm{id}]^{\mathcal{Y} \to \mathcal{X}}[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}} = [\mathrm{id} \circ \mathrm{id}]^{\mathcal{X} \to \mathcal{X}} = E$. Na příkladu: $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. Přesně se k inverzním maticím dostaneme v kap. 7.

## §5 Lineární prostor lineárních zobrazení

Matice stejného rozměru umíme sčítat a násobit číslem, tvoří [[lineární prostor]]. Čemu tyto operace odpovídají v řeči zobrazení?

> [!definice] Definice · pozn. 6.28 · součet a skalární násobek zobrazení
> Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$.
>
> 1. Pro zobrazení $A, B : V \to W$ definujeme jejich *součet* $(A + B) : V \to W$ předpisem $(A + B)(\vec{x}) = A\vec{x} + B\vec{x}$ pro všechna $\vec{x} \in V$.
> 2. Pro zobrazení $A : V \to W$ a skalár $\alpha \in \mathbb{F}$ definujeme *skalární násobek* $(\alpha A) : V \to W$ předpisem $(\alpha A)(\vec{x}) = \alpha(A\vec{x})$ pro všechna $\vec{x} \in V$.

^def-soucet-zobrazeni

> [!lidsky] Lidsky
> Zobrazení se sčítají **bod po bodu**, stejně jako funkce ze střední: $(f + g)(t) = f(t) + g(t)$. Do obou dosadíš stejný vektor a výsledky sečteš. Násobek $\alpha A$ znamená „nejdřív zobraz, výsledek vynásob $\alpha$“.

> [!example] Příklad
> $A(x; y) = (x + y;\ 2y)$ a $B(x; y) = (y;\ x - y)$ na $\mathbb{R}^2$. Pak $(A + B)(x; y) = (x + 2y;\ x + y)$, $(3A)(x; y) = (3x + 3y;\ 6y)$ a třeba $(A + B)(1; 2) = (5; 3) = (3; 4) + (2; -1) = A(1; 2) + B(1; 2)$.

> [!veta] Věta 6.29 a 6.30 (Lin(V, W) je lineární prostor)
> ==Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$.== Potom
>
> 1. **pro každé $A, B \in \operatorname{Lin}(V, W)$ je $A + B \in \operatorname{Lin}(V, W)$,**
> 2. **pro každé $\alpha \in \mathbb{F}$ a $A \in \operatorname{Lin}(V, W)$ je $\alpha A \in \operatorname{Lin}(V, W)$,**
>
> a množina $\operatorname{Lin}(V, W)$ s těmito operacemi je **lineární prostor nad $\mathbb{F}$**: $(\operatorname{Lin}(V, W), \mathbb{F}, +, \cdot)$.
>
> > [!note]- Důkaz bodu 1
> > Podle [[kritérium linearity|kritéria linearity]] stačí pro $\vec{x}, \vec{y} \in V$ a $\alpha \in \mathbb{F}$ ověřit jednu rovnost:
> >
> > $$
> > (A + B)(\alpha\vec{x} + \vec{y}) = A(\alpha\vec{x} + \vec{y}) + B(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y} + \alpha B\vec{x} + B\vec{y} = \alpha(A\vec{x} + B\vec{x}) + (A\vec{y} + B\vec{y}) = \alpha(A + B)\vec{x} + (A + B)\vec{y}.
> > $$
> >
> > Bod 2 stejně. Axiomy lineárního prostoru se ověří bod po bodu, protože ve $W$ platí; nulovým vektorem je [[nulové zobrazení]] a opačným k $A$ je $(-1)A$.

^veta-lin-prostor-zobrazeni

> [!lidsky] Lidsky
> Součet dvou lineárních zobrazení je zase lineární a násobek taky, takže z lineárních zobrazení se stává „sbírka vektorů“: zobrazení jsou teď samy vektory. Nulou je nulové zobrazení. Identita tu žádnou zvláštní roli nehraje, je neutrální pro **skládání**, ne pro sčítání.

> [!example] Příklad
> V $\operatorname{Lin}(\mathbb{R}^2, \mathbb{R}^2)$ je otočení $R_{90°}(x; y) = (-y; x)$ i identita. Jejich součet $(R_{90°} + \mathrm{id})(x; y) = (x - y;\ x + y)$ je zase lineární; je to zobrazení $A$ z §2. Opačný vektor k $R_{90°}$ je $(-1)R_{90°}(x; y) = (y; -x)$, otočení o $-90°$.

> [!veta] Věta 6.31 (matice součtu a násobku)
> ==Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$ konečné dimenze, $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ báze $V$ a $\mathcal{Y}$ báze $W$.== Potom
>
> 1. **$[A + B]^{\mathcal{X} \to \mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}} + [B]^{\mathcal{X} \to \mathcal{Y}}$ pro každé $A, B \in \operatorname{Lin}(V, W)$,**
> 2. **$[\alpha A]^{\mathcal{X} \to \mathcal{Y}} = \alpha[A]^{\mathcal{X} \to \mathcal{Y}}$ pro každé $\alpha \in \mathbb{F}$ a $A \in \operatorname{Lin}(V, W)$.**
>
> > [!note]- Důkaz bodu 2
> > Podle definice [[matice lineárního zobrazení vzhledem k bázím|matice zobrazení]] a [[věta o linearitě souřadnic|linearity souřadnic]]:
> >
> > $$
> > [\alpha A]^{\mathcal{X} \to \mathcal{Y}} = \big([\alpha A\vec{x}_1]^{\mathcal{Y}} \cdots [\alpha A\vec{x}_n]^{\mathcal{Y}}\big) = \big(\alpha[A\vec{x}_1]^{\mathcal{Y}} \cdots \alpha[A\vec{x}_n]^{\mathcal{Y}}\big) = \alpha\big([A\vec{x}_1]^{\mathcal{Y}} \cdots [A\vec{x}_n]^{\mathcal{Y}}\big) = \alpha[A]^{\mathcal{X} \to \mathcal{Y}}.
> > $$
> >
> > Bod 1 stejně, s $[(A + B)\vec{x}_j]^{\mathcal{Y}} = [A\vec{x}_j]^{\mathcal{Y}} + [B\vec{x}_j]^{\mathcal{Y}}$.

^veta-matice-souctu

> [!lidsky] Lidsky
> Sčítání zobrazení a sčítání matic je **totéž**, jen v jiném jazyce. Chceš matici součtu? Sečti matice. Chceš matici trojnásobku? Vynásob matici třemi.

> [!example] Příklad 6.34 · vytýkání z matic
> Výpočet z §2 jde zlidštit vytknutím konstant. Matice otočení o $45°$ je
>
> $$
> [R_{45°}]^{\mathcal{E}} = \begin{pmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{pmatrix} = \frac{\sqrt{2}}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \frac{\sqrt{2}}{2}[A]^{\mathcal{E}},
> $$
>
> tedy $R_{45°} = \tfrac{\sqrt{2}}{2}A$, a stejnolehlost je $S_{\sqrt{2}} = \sqrt{2}\,\mathrm{id}$. Proto
>
> $$
> [R_{45°} \circ S_{\sqrt{2}}]^{\mathcal{E}} = \Big(\frac{\sqrt{2}}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\Big)\Big(\sqrt{2}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\Big) = \frac{\sqrt{2}}{2} \cdot \sqrt{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}.
> $$
>
> Že se smí skaláry z obou činitelů vytknout před součin, říká [[vytýkání skaláru ze součinu]] (další přednáška).

> [!navic] Připomenutí: kritérium linearity
> $F : V \to W$ je lineární, právě když $F(\alpha\vec{x} + \vec{y}) = \alpha F\vec{x} + F\vec{y}$ pro všechna $\vec{x}, \vec{y} \in V$ a $\alpha \in \mathbb{F}$ ([[kritérium linearity]]). Tak se dokazuje i bod 1 věty 6.29.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jak dokážeš $(AB)C = A(BC)$ přímo z definice součinu matic?
> Porovnej prvek $(i, j)$: $[(AB)C]_{ij} = \sum_x [AB]_{ix}c_{xj} = \sum_x \sum_y a_{iy}b_{yx}c_{xj}$ a $[A(BC)]_{ij} = \sum_y a_{iy}[BC]_{yj} = \sum_y \sum_x a_{iy}b_{yx}c_{xj}$. Je to **tentýž konečný součet**, jen sečtený v jiném pořadí.

> [!karta|02]- Proč z věty o matici složeného zobrazení plyne asociativita součinu matic, aniž bys počítal sumy?
> Matice jsou lineární zobrazení a **součin matic = matice složení**. Skládání zobrazení je asociativní, $(h \circ g) \circ f = h \circ (g \circ f)$, protože obě strany pošlou $x$ na $h(g(f(x)))$. Proto i $(AB)C = A(BC)$.

> [!karta|03]- Proč u součinu tří matic nemusíš psát závorky, ale nesmíš měnit pořadí?
> Součin je **asociativní**, $(AB)C = A(BC)$, takže závorky výsledek nemění. Není ale **komutativní**: $AB \ne BA$ obecně (odpovídá to pořadí skládání zobrazení).

> [!karta|04]- Proč stejnolehlost $S_k$ komutuje s každým lineárním zobrazením roviny?
> Její matice je $kE$ a $(kE)M = kM = M(kE)$ pro každou matici $M$. Zvětšení a pak otočení dá totéž co otočení a pak zvětšení.

> [!karta|05]- Proč je $[\mathrm{id}]^{\mathcal{X} \to \mathcal{X}}$ jednotková matice pro **každou** bázi $\mathcal{X}$?
> $j$-tý sloupec je $[\vec{x}_j]^{\mathcal{X}}$ a $\vec{x}_j = 0 \cdot \vec{x}_1 + \dots + 1 \cdot \vec{x}_j + \dots + 0 \cdot \vec{x}_n$, tedy **$[\vec{x}_j]^{\mathcal{X}} = \vec{e}_j$**.

> [!karta|06]- Proč $[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}$ pro dvě různé báze obvykle **není** jednotková, i když $\mathrm{id}$ nic nedělá?
> Identita vektor nemění, ale mění se **jazyk souřadnic**: sloupce jsou $[\vec{x}_j]^{\mathcal{Y}}$, tedy vektory $\mathcal{X}$ zapsané v bázi $\mathcal{Y}$, a ty nejsou $\vec{e}_j$, pokud $\mathcal{X} \ne \mathcal{Y}$.

> [!karta|07]- Proč v $AE_n = A = E_mA$ pro $A \in \mathbb{F}^{m \times n}$ stojí na jedné straně $E_n$ a na druhé $E_m$?
> Kvůli rozměrům součinu: **zprava** musí mít $E$ tolik řádků, kolik má $A$ sloupců ($n$), **zleva** tolik sloupců, kolik má $A$ řádků ($m$). U nečtvercové $A$ jsou to různé matice.

> [!karta|08]- Proč je v $\mathbb{F}^n$ matice $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$ snadná, zatímco $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$ dá práci?
> Sloupce $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$ jsou $[\vec{x}_j]^{\mathcal{E}} = \vec{x}_j$: **prostě vektory báze** $\mathcal{X}$. Pro $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$ musíš každé $\vec{e}_j$ **vyjádřit v bázi $\mathcal{X}$**, tj. řešit soustavu.

> [!karta|09]- Ze které věty a jak plyne $[\vec{v}]^{\mathcal{Y}} = [\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}[\vec{v}]^{\mathcal{X}}$?
> Z **věty o souřadnicích obrazu** $[A\vec{v}]^{\mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}}[\vec{v}]^{\mathcal{X}}$ pro $A = \mathrm{id}_V$: $\mathrm{id}\,\vec{v} = \vec{v}$.

> [!karta|10]- Co napíšeš do $j$-tého sloupce matice přechodu od báze $\mathcal{X}$ k bázi $\mathcal{Y}$?
> Souřadnice **$j$-tého vektoru báze $\mathcal{X}$ vzhledem k bázi $\mathcal{Y}$**, tj. $[\vec{x}_j]^{\mathcal{Y}}$. Vstupní báze dává vektory, výstupní báze jazyk souřadnic.

> [!karta|11]- Jak spolu souvisí $[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}$ a $[\mathrm{id}]^{\mathcal{Y} \to \mathcal{X}}$?
> Jejich součin je **jednotková matice**: $[\mathrm{id}]^{\mathcal{Y} \to \mathcal{X}}[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}} = [\mathrm{id} \circ \mathrm{id}]^{\mathcal{X} \to \mathcal{X}} = E$. Jedna překládá tam, druhá zpátky.

> [!karta|12]- Co je nulový vektor a opačný vektor v prostoru $\operatorname{Lin}(V, W)$?
> Nulový vektor je **nulové zobrazení** $\vec{x} \mapsto \vec{0}$ (přičtením se nic nezmění). Opačný k $A$ je **$(-1)A$**, tj. $\vec{x} \mapsto -A\vec{x}$, protože $(A + (-1)A)\vec{x} = \vec{0}$.

> [!karta|13]- Proč nemůže být $\begin{pmatrix} \cos\alpha & \sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}$ matice otočení o úhel $\alpha$?
> Pro $\alpha = 90°$ dá $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, která prohodí souřadnice: to je **zrcadlení podle $y = x$**, ne otočení. Obraz $\vec{e}_2$ je $(-\sin\alpha; \cos\alpha)$, proto **$-\sin\alpha$** v pravém horním rohu.

> [!karta|22]- Jak dokážeš, že součet dvou lineárních zobrazení $A, B : V \to W$ je lineární?
> Podle **kritéria linearity** stačí jedna rovnost: $(A + B)(\alpha\vec{x} + \vec{y}) = A(\alpha\vec{x} + \vec{y}) + B(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y} + \alpha B\vec{x} + B\vec{y} = \alpha(A + B)\vec{x} + (A + B)\vec{y}$. Použije se **definice součtu** a **linearita $A$ a $B$**.

> [!karta|23]- Je identické zobrazení nulovým vektorem prostoru $\operatorname{Lin}(V, V)$? Jakou roli tam hraje?
> **Ne.** Nulovým vektorem je **nulové zobrazení**: $A + O = A$. Pro identitu je $(A + \mathrm{id})\vec{x} = A\vec{x} + \vec{x}$, takže $A + \mathrm{id} \ne A$. Identita je neutrální prvek **skládání** ($A \circ \mathrm{id} = A$), ne sčítání.

> [!karta|24]- Proč je $[A + B]^{\mathcal{X} \to \mathcal{Y}} = [A]^{\mathcal{X} \to \mathcal{Y}} + [B]^{\mathcal{X} \to \mathcal{Y}}$? Co se děje se sloupci?
> $j$-tý sloupec vlevo je $[(A + B)\vec{x}_j]^{\mathcal{Y}} = [A\vec{x}_j + B\vec{x}_j]^{\mathcal{Y}} = [A\vec{x}_j]^{\mathcal{Y}} + [B\vec{x}_j]^{\mathcal{Y}}$ podle **linearity souřadnic**, a to je součet $j$-tých sloupců vpravo. **Sloupec po sloupci** se matice sečtou.

### Příklady na procvičení

> [!priklad|14]- Pro $A = \begin{pmatrix} 2 & 0 & 1 \\ -1 & 3 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 2 \\ 0 & -1 \\ 3 & 1 \end{pmatrix}$ a $\vec{v} = (2; -1)$ spočítej $(AB)\vec{v}$ i $A(B\vec{v})$.
> $AB = \begin{pmatrix} 2 + 0 + 3 & 4 + 0 + 1 \\ -1 + 0 + 0 & -2 - 3 + 0 \end{pmatrix} = \begin{pmatrix} 5 & 5 \\ -1 & -5 \end{pmatrix}$, $(AB)\vec{v} = (10 - 5;\ -2 + 5) = (5; 3)$.
>
> $B\vec{v} = (2 - 2;\ 0 + 1;\ 6 - 1) = (0; 1; 5)$, $A(B\vec{v}) = (0 + 0 + 5;\ 0 + 3 + 0) = (5; 3)$.
>
> **Obojí $(5; 3)$.**

> [!priklad|15]- Ukaž, že $A(x; y) = (x - \sqrt{3}y;\ \sqrt{3}x + y)$ je otočení o $60°$ složené se zvětšením $2\times$.
> $[A]^{\mathcal{E}} = \begin{pmatrix} 1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{pmatrix}$. $[R_{60°}]^{\mathcal{E}} = \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$ a $[S_2]^{\mathcal{E}}[R_{60°}]^{\mathcal{E}} = 2[R_{60°}]^{\mathcal{E}} = \begin{pmatrix} 1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{pmatrix}$.
>
> **$A = S_2 \circ R_{60°}$**, protože matice určuje zobrazení jednoznačně.

> [!priklad|16]- V $\mathbb{R}^2$ je $\mathcal{X} = ((2; 1), (1; 1))$. Najdi $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$, $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$ a souřadnice $(3; 4)$ v bázi $\mathcal{X}$.
> $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ (sloupce jsou vektory báze). Vyjádři $\vec{e}_1 = (2; 1) - (1; 1)$, $\vec{e}_2 = -(2; 1) + 2(1; 1)$, takže $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$. Pak $[(3; 4)]^{\mathcal{X}} = (3 - 4;\ -3 + 8) = (-1; 5)$.
>
> **$(-1; 5)$**; kontrola: $-(2; 1) + 5(1; 1) = (3; 4)$.

> [!priklad|17]- $A(x; y) = (x + y;\ 2y)$, $B(x; y) = (y;\ x - y)$. Najdi $[3A - B]^{\mathcal{E}}$ a $(3A - B)(1; 2)$.
> $[A]^{\mathcal{E}} = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, $[B]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$, takže $[3A - B]^{\mathcal{E}} = \begin{pmatrix} 3 & 2 \\ -1 & 7 \end{pmatrix}$. $(3A - B)(1; 2) = (3 + 4;\ -1 + 14)$.
>
> **$\begin{pmatrix} 3 & 2 \\ -1 & 7 \end{pmatrix}$, $(7; 13)$**; kontrola po složkách: $3A(1; 2) - B(1; 2) = (9; 12) - (2; -1) = (7; 13)$.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|18]- V $\mathbb{R}^{\le 2}[x]$ jsou báze $\mathcal{B} = (1, x, x^2)$ a $\mathcal{C} = (x + 1,\ x^2,\ 2 - x)$. Najdi $T_{\mathcal{C} \to \mathcal{B}}$, $T_{\mathcal{B} \to \mathcal{C}}$ a souřadnice $3x^2 - x + 4$ vzhledem k $\mathcal{C}$.
> **$T_{\mathcal{C} \to \mathcal{B}}$:** sloupce jsou souřadnice vektorů $\mathcal{C}$ v $\mathcal{B}$ (koeficienty u $1, x, x^2$): $x + 1 \to (1; 1; 0)$, $x^2 \to (0; 0; 1)$, $2 - x \to (2; -1; 0)$, tedy $T_{\mathcal{C} \to \mathcal{B}} = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$.
>
> **$T_{\mathcal{B} \to \mathcal{C}}$:** vyjádři $1, x, x^2$ v $\mathcal{C}$. $(x + 1) + (2 - x) = 3$, tedy $1 = \tfrac{1}{3}(x + 1) + \tfrac{1}{3}(2 - x) \to (\tfrac{1}{3}; 0; \tfrac{1}{3})$; $x = \tfrac{2}{3}(x + 1) - \tfrac{1}{3}(2 - x) \to (\tfrac{2}{3}; 0; -\tfrac{1}{3})$; $x^2 \to (0; 1; 0)$. Tedy $T_{\mathcal{B} \to \mathcal{C}} = \begin{pmatrix} 1/3 & 2/3 & 0 \\ 0 & 0 & 1 \\ 1/3 & -1/3 & 0 \end{pmatrix}$.
>
> **Souřadnice:** $[p]^{\mathcal{B}} = (4; -1; 3)$, $[p]^{\mathcal{C}} = T_{\mathcal{B} \to \mathcal{C}}(4; -1; 3) = (\tfrac{4}{3} - \tfrac{2}{3};\ 3;\ \tfrac{4}{3} + \tfrac{1}{3})$ = **$(\tfrac{2}{3}; 3; \tfrac{5}{3})$**. Kontrola: $\tfrac{2}{3}(x + 1) + 3x^2 + \tfrac{5}{3}(2 - x) = 3x^2 - x + 4$.

> [!priklad|19]- V $\mathbb{R}^2$ jsou báze $\mathcal{X} = ((1; 0), (1; 1))$ a $\mathcal{Y} = ((1; 1), (1; -1))$. Najdi $T_{\mathcal{X} \to \mathcal{Y}}$ a s ní $[\vec{v}]^{\mathcal{Y}}$ pro $[\vec{v}]^{\mathcal{X}} = (2; 3)$.
> Sloupce jsou $[\vec{x}_j]^{\mathcal{Y}}$: $(1; 0) = \tfrac{1}{2}(1; 1) + \tfrac{1}{2}(1; -1) \to (\tfrac{1}{2}; \tfrac{1}{2})$, $(1; 1) = 1 \cdot (1; 1) + 0 \cdot (1; -1) \to (1; 0)$. Tedy $T_{\mathcal{X} \to \mathcal{Y}} = \begin{pmatrix} 1/2 & 1 \\ 1/2 & 0 \end{pmatrix}$ a $[\vec{v}]^{\mathcal{Y}} = (1 + 3;\ 1 + 0)$ = **$(4; 1)$**.
>
> Kontrola: $\vec{v} = 2(1; 0) + 3(1; 1) = (5; 3)$ a $4(1; 1) + 1 \cdot (1; -1) = (5; 3)$.

> [!priklad|20]- V $\mathbb{R}^{2 \times 2}$ je $\mathcal{X} = (E_{11}, E_{12}, E_{21}, E_{22})$ kanonická a $\mathcal{Y} = \left(\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 2 & 1 \end{pmatrix}\right)$. Ověř, že $T_{\mathcal{X} \to \mathcal{Y}} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 1 \end{pmatrix}$, a najdi souřadnice $\begin{pmatrix} 3 & 1 \\ 2 & 5 \end{pmatrix}$ vzhledem k $\mathcal{Y}$.
> $j$-tý sloupec mají být souřadnice $j$-tého vektoru $\mathcal{X}$ v $\mathcal{Y}$. Ověř po sloupcích: $E_{11} = Y_1 - Y_2$, $E_{12} = Y_2$, $E_{21} = Y_3$, $E_{22} = -2Y_3 + Y_4$ (protože $-2\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$). Sloupce sedí, **matice je správná**.
>
> V kanonické bázi jsou souřadnice prvky po řádcích $(3; 1; 2; 5)$, takže $[M]^{\mathcal{Y}} = T_{\mathcal{X} \to \mathcal{Y}}(3; 1; 2; 5) = (3;\ -3 + 1;\ 2 - 10;\ 5)$ = **$(3; -2; -8; 5)$**. Kontrola: $3Y_1 - 2Y_2 - 8Y_3 + 5Y_4 = \begin{pmatrix} 3 & 1 \\ 2 & 5 \end{pmatrix}$.

> [!priklad|21]- $A(x; y) = \begin{pmatrix} 1 & 2 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}$, $\mathcal{X} = ((1; 1), (2; 1))$. Najdi $[A]^{\mathcal{X} \to \mathcal{X}}$ pomocí matic přechodu.
> $\mathcal{X}$ je báze: dva vektory, které nejsou násobkem jeden druhého, jsou LN, a $\dim\mathbb{R}^2 = 2$. Podle věty o matici složeného zobrazení pro $A = \mathrm{id} \circ A \circ \mathrm{id}$:
>
> $$
> [A]^{\mathcal{X} \to \mathcal{X}} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}\,[A]^{\mathcal{E} \to \mathcal{E}}\,[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}.
> $$
>
> $[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$; z $\vec{e}_1 = -(1; 1) + (2; 1)$, $\vec{e}_2 = 2(1; 1) - (2; 1)$ je $[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}$. Pak $[A]^{\mathcal{E}}[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = \begin{pmatrix} 3 & 4 \\ -1 & -2 \end{pmatrix}$ a
>
> **$[A]^{\mathcal{X} \to \mathcal{X}} = \begin{pmatrix} -1 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 3 & 4 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} -5 & -8 \\ 4 & 6 \end{pmatrix}$.** Kontrola: $A(1; 1) = (3; -1) = -5(1; 1) + 4(2; 1)$.

---
← [[LAG 08 – Matice lineárního zobrazení a součin matic|16. 10. 2026 Matice lineárního zobrazení a součin matic]] · [[LAG 10 – Obraz a vzor při lineárním zobrazení|23. 10. 2026 Obraz a vzor při lineárním zobrazení]] →

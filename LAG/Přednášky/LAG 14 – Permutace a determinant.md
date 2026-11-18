---
predmet: LAG
prednaska: 14
datum: 2026-11-11
zdroj: "V poznámkách pozn. 10.1 až věta 10.16 (kap. 10.1–10.2), navazuje na pozn. 9.11–9.18"
tags: [prednaska, LAG]
---

# LAG 14 – Permutace a determinant

*Přednáška 14 · středa 11. 11. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `zápisy permutace` · `cyklický zápis` · `sgn jako homomorfismus` · `ax = b a a ≠ 0` · `det 2 × 2 = ad − bc` · `vzorec pro A⁻¹ (2 × 2)` · `singulární matice` · `definice determinantu` · `det Aᵀ = det A` · `Sarrusovo pravidlo` · `algebraický doplněk` · `rozvoj podle řádku a sloupce` · `horní trojúhelníková matice` · `determinant a řádkové úpravy`

Minule jsme zavedli permutace a jejich znaménko. Dnes se ukáže, k čemu jsou: rovnice $ax = b$ má právě jedno řešení, když $a \neq 0$, a *determinant* je číslo, které tuhle roli hraje pro čtvercové matice. Pro matici $2 \times 2$ vyjde z eliminace $ad - bc$, obecně je to součet přes všechny permutace. Prakticky se determinant počítá rozvojem podle řádku či sloupce nebo eliminací na trojúhelníkový tvar.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| cyklický zápis permutace | permutaci zapíšeš jako cykly „kam co jde“ | $1 \mapsto 3 \mapsto 2 \mapsto 1$, $4 \leftrightarrow 5$: $(1\,3\,2)(4\,5)$ |
| věta o znaménku složené permutace | $\operatorname{sgn}(\pi\sigma) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\sigma$ | $\operatorname{sgn} : (S_n, \circ) \to (\{\pm 1\}, \cdot)$ je homomorfismus |
| determinant matice 2 × 2 | $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$ | $\begin{vmatrix} 3 & 1 \\ 1 & 2 \end{vmatrix} = 5$ |
| vzorec pro inverzní matici 2 × 2 | $A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ | |
| singulární matice ♥ | čtvercová matice, která není regulární | $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ |
| determinant ♥ | $\det A = \sum_{\pi \in S_n} \operatorname{sgn}\pi \, a_{1\pi(1)} \cdots a_{n\pi(n)}$ | $n!$ sčítanců |
| determinant transponované matice | $\det A^{\mathsf{T}} = \det A$ | řádky a sloupce jsou rovnocenné |
| Sarrusovo pravidlo | $3 \times 3$: tři „diagonály“ s plusem, tři s minusem | jen pro $n = 3$! |
| algebraický doplněk ♥ | $D_{ij} = (-1)^{i+j}\det A^{(i,j)}$, škrtni řádek $i$ a sloupec $j$ | znaménka jako šachovnice |
| rozvoj determinantu | $\det A = \sum_i a_{ik}D_{ik} = \sum_i a_{ki}D_{ki}$ | rozvíjej podle řádku s nejvíc nulami |
| horní trojúhelníková matice | pod diagonálou nuly | $\begin{pmatrix} 2 & 5 \\ 0 & 3 \end{pmatrix}$ |
| determinant horní trojúhelníkové matice | součin diagonály; regulární $\Leftrightarrow$ $\det \neq 0$ | $2 \cdot 3 = 6$ |
| věta o determinantu a řádkových úpravách | prohození: $-\det$; násobek řádku: $\alpha\det$; přičtení násobku: beze změny | výpočet eliminací |

## §1 Permutace: zápisy a znaménko

Z minula: [[permutace]] je bijekce $\{1, \dots, n\} \to \{1, \dots, n\}$, všechny tvoří grupu $S_n$ s $n!$ prvky, a [[znaménko permutace|znaménko]] $\operatorname{sgn}\pi = (-1)^{\text{počet inverzí}}$ ([[inverze v permutaci]], pozn. 9.14). Permutaci jde zapsat třemi způsoby:

- **dvouřádkově** $\begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 1 & 2 & 5 & 4 \end{pmatrix}$: nahoře vzory, dole obrazy,
- **jednořádkově** $(3\ 1\ 2\ 5\ 4)$: jen spodní řádek,
- **cyklicky** $(1\,3\,2)(4\,5)$: kam co postupně jde.

> [!definice] Definice · cyklický zápis permutace (k pozn. 9.11)
> Pro různá čísla $a_1, \dots, a_k \in \{1, \dots, n\}$ je *cyklus* $(a_1\,a_2\,\dots\,a_k)$ permutace, která posílá
>
> $$
> a_1 \mapsto a_2 \mapsto \dots \mapsto a_k \mapsto a_1
> $$
>
> a ostatní čísla nechává na místě; $k$ je *délka* cyklu. Každou permutaci lze zapsat jako složení cyklů, které nemají společné prvky (*cyklický zápis*); pevné body (cykly délky 1) se nepíšou.

^def-cyklicky-zapis

> [!lidsky] Lidsky
> Vezmi nejmenší číslo a sleduj ho: kam jde, kam jde to, … až se vrátíš na začátek. To je jeden cyklus („kolečko výměn“). Pak vezmi nejmenší dosud nepoužité číslo a opakuj. Cyklus délky 2 je přesně [[transpozice (permutace)|transpozice]].

> [!example] Příklad
> $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 2 & 4 \end{pmatrix}$: $1 \to 3 \to 1$ a $2 \to 5 \to 4 \to 2$, tedy **$\sigma = (1\,3)(2\,5\,4)$**. Na pořadí cyklů nezáleží (nemají společné prvky) a cyklus jde začít kterýmkoli svým prvkem: $(2\,5\,4) = (5\,4\,2) = (4\,2\,5)$. Ale $(2\,4\,5)$ je jiný cyklus, jde opačným směrem.
>
> Nepříklad: $(1\,2)(2\,3)$ není cyklický zápis v tomto smyslu, cykly mají společný prvek $2$.

> [!obrazek] Permutace jako kolečka
> ![[lag14-cykly.png]]
> *Permutace $(3\ 1\ 2\ 5\ 4)$ nakreslená šipkami $i \to \pi(i)$. Modře cyklus $(1\,3\,2)$ délky 3, oranžově cyklus $(4\,5)$ délky 2 (transpozice).*

> [!pozor] Cyklus není jednořádkový zápis
> $(1\,3\,2)$ jako **cyklus** znamená $1 \mapsto 3$, $3 \mapsto 2$, $2 \mapsto 1$, tedy jednořádkově $(3\ 1\ 2)$. Jako **jednořádkový zápis** by $(1\ 3\ 2)$ byla transpozice prohazující 2 a 3. Z kontextu musí být jasné, který zápis používáš; cykly se proto píšou bez mezer mezi čísly, nebo se to řekne.

Z minula také víme ([[věta o znaménku složené permutace]], věty 9.17 a 9.18), že znaménko je [[homomorfismus grup]] $\operatorname{sgn} : (S_n, \circ) \to (\{\pm 1\}, \cdot)$, tedy $\operatorname{sgn}(\pi \circ \sigma) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\sigma$. Z toho se dá znaménko vyčíst přímo z cyklů:

$$
(a_1\,a_2\,\dots\,a_k) = (a_1\,a_k) \circ \dots \circ (a_1\,a_3) \circ (a_1\,a_2),
$$

cyklus délky $k$ je složením $k - 1$ transpozic, každá je lichá (pozorování 9.16), takže **cyklus délky $k$ má znaménko $(-1)^{k-1}$** a znaménko permutace je součin znamének jejích cyklů.

> [!example] Příklad
> $(1\,2\,3) = (1\,3) \circ (1\,2)$: napravo nejdřív $(1\,2)$ pošle $1 \mapsto 2$ a $(1\,3)$ dvojku nechá, takže $1 \mapsto 2$; $2 \mapsto 1 \mapsto 3$; $3 \mapsto 3 \mapsto 1$. Znaménko $(-1)^2 = +1$.
>
> $\sigma = (1\,3)(2\,5\,4)$ z příkladu výše: $\operatorname{sgn}\sigma = (-1) \cdot (+1) = -1$. Kontrola inverzemi v $(3\ 5\ 1\ 2\ 4)$: $(1, 3)$, $(1, 4)$, $(2, 3)$, $(2, 4)$, $(2, 5)$, tedy 5, lichá. ✓

## §2 Motivace: kdy má soustava jediné řešení

Pro čísla platí (věta 10.1): **rovnice $ax = b$ má právě jedno řešení, právě když $a \neq 0$.** Pro soustavu $A\vec{x} = \vec{b}$ se čtvercovou maticí hraje roli „$a \neq 0$“ regularita ([[věta o charakterizaci regulární matice]]). Determinant bude jedno číslo, které o regularitě rozhodne stejně jednoduše jako $a \neq 0$. Připomenutí 10.2: [[regulární matice]] je čtvercová matice $A$, pro kterou je $\vec{x} \mapsto A\vec{x}$ [[bijekce]].

> [!veta] Příklad 10.4 a 10.8 · Determinant matice $2 \times 2$
> ==Buď $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathbb{F}^{2 \times 2}$.== Označme
>
> $$
> \det A = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc.
> $$
>
> Potom **$A$ je regulární, právě když $ad - bc \neq 0$.**
>
> > [!note]- Důkaz
> > **$a \neq 0$:** úprava $r_2 \cdot a - c \cdot r_1$ dá $\begin{pmatrix} a & b \\ 0 & ad - bc \end{pmatrix}$ (násobení řádku číslem $a \ne 0$ je povolená úprava). Matice má dva [[pivot|pivoty]], tedy hodnost 2, právě když $ad - bc \neq 0$.
> >
> > **$a = 0$:** pak $ad - bc = -bc$. Je-li $bc \neq 0$, prohození řádků dá $\begin{pmatrix} c & d \\ 0 & b \end{pmatrix}$ se dvěma pivoty. Je-li $bc = 0$, je $b = 0$ (první řádek nulový) nebo $c = 0$ (první sloupec nulový), a matice regulární není.

^veta-det-2x2

> [!lidsky] Lidsky
> **Hlavní diagonála minus vedlejší.** Číslo $ad - bc$ přesně vypadne z eliminace jako to, co zbude na místě druhého pivotu. Geometricky je $|ad - bc|$ obsah rovnoběžníku, který napnou sloupce $A$: když je nulový, sloupce leží na jedné přímce a $A$ „zplacatí“ rovinu.

> [!example] Příklad
> $\begin{vmatrix} 3 & 1 \\ 1 & 2 \end{vmatrix} = 3 \cdot 2 - 1 \cdot 1 = 5 \neq 0$, regulární. $\begin{vmatrix} 1 & 2 \\ 2 & 4 \end{vmatrix} = 4 - 4 = 0$: sloupce $(1; 2)$ a $(2; 4)$ jsou na jedné přímce, matice regulární není.

> [!obrazek] Determinant $2 \times 2$ jako obsah
> ![[lag14-rovnobeznik.png]]
> *Modrý a oranžový vektor jsou sloupce $(3; 1)$ a $(1; 2)$ matice $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$; zelený rovnoběžník má obsah $3 \cdot 2 - 1 \cdot 1 = 5$. Vpravo sloupce $(1; 2)$ a $(2; 4)$ (červeně) leží na přímce a rovnoběžník má obsah 0.*

> [!veta] Příklad 10.4 · Inverze matice $2 \times 2$
> ==Je-li $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ a $ad - bc \neq 0$==, pak
>
> $$
> \mathbf{A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}}.
> $$
>
> > [!note]- Důkaz
> > Roznásob: $\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = (ad - bc)E$. Vydělením $ad - bc$ vyjde $E$, takže jde o [[inverzní matice|inverzní matici]].

^veta-inverze-2x2

> [!lidsky] Lidsky
> Recept na tři kroky: **prohoď** čísla na hlavní diagonále, **změň znaménka** na vedlejší a **vyděl** determinantem. Nulou dělit nejde, a to je přesně případ, kdy inverze neexistuje.

> [!example] Příklad
> $A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $\det A = 5$: $A^{-1} = \frac{1}{5}\begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}$. Kontrola: $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ 0 & 5 \end{pmatrix}$. ✓ Soustava $A\vec{x} = (4; 3)$ má pak řešení $\vec{x} = \frac{1}{5}(8 - 3;\ -4 + 9) = (1; 1)$.

> [!definice] Definice · pozn. 10.3 ♥
> Matice $A \in \mathbb{F}^{n \times n}$ se nazývá *singulární*, jestliže není regulární.

^def-singularni

> [!lidsky] Lidsky
> Singulární = „pokažená“ čtvercová matice: zobrazení $\vec{x} \mapsto A\vec{x}$ slepí dva různé vektory dohromady, inverze neexistuje a soustava $A\vec{x} = \vec{b}$ nemá jediné řešení (buď žádné, nebo nekonečně mnoho). Poznáš ji podle $\det A = 0$.

> [!example] Příklad
> $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ je singulární: $\det = 0$ a $(2; -1) \mapsto (0; 0)$, stejně jako nulový vektor. Soustava s pravou stranou $(1; 0)$ nemá řešení, s pravou stranou $(1; 2)$ jich má nekonečně mnoho. Nepříklad: $\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$ s $\det = 5$.

> [!pozor] Jen čtvercové matice
> Regulární a singulární jsou jen **čtvercové** matice. O matici $2 \times 3$ nemá smysl říkat, že je singulární, ani počítat její determinant.

## §3 Definice determinantu

Pro $2 \times 2$ jsou ve vzorci $ad - bc$ dva součiny, každý bere z každého řádku i sloupce jeden prvek: $a_{11}a_{22}$ (permutace $\mathrm{id}$, sudá) a $a_{12}a_{21}$ (transpozice, lichá, proto minus). Přesně tak se determinant definuje obecně.

> [!definice] Definice · pozn. 10.5 ♥
> *Determinant* matice $A \in \mathbb{F}^{n \times n}$ je skalár
>
> $$
> \det A = \sum_{\pi \in S_n} \operatorname{sgn}\pi \cdot a_{1\pi(1)}\,a_{2\pi(2)} \cdots a_{n\pi(n)} \in \mathbb{F}.
> $$
>
> Značí se také svislými čarami, $\det A = |A|$ (pozn. 10.7).

^def-determinant

> [!lidsky] Lidsky
> Projdi všechny způsoby, jak do matice postavit $n$ „věží“, které se navzájem neohrožují (v každém řádku i sloupci právě jedna). Každé rozestavění je permutace: v řádku $i$ stojí věž ve sloupci $\pi(i)$. Vynásob čísla pod věžemi, dej znaménko permutace a všechno sečti. Členů je $n!$.

> [!example] Příklad
> $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 4 \end{pmatrix}$, šest permutací $S_3$ (jednořádkově):
>
> | $\pi$ | $\operatorname{sgn}\pi$ | $a_{1\pi(1)}a_{2\pi(2)}a_{3\pi(3)}$ | člen |
> | --- | --- | --- | --- |
> | $(1\ 2\ 3)$ | $+$ | $2 \cdot 3 \cdot 4$ | $24$ |
> | $(1\ 3\ 2)$ | $-$ | $2 \cdot 2 \cdot 1$ | $-4$ |
> | $(2\ 1\ 3)$ | $-$ | $0 \cdot 1 \cdot 4$ | $0$ |
> | $(2\ 3\ 1)$ | $+$ | $0 \cdot 2 \cdot 1$ | $0$ |
> | $(3\ 1\ 2)$ | $+$ | $1 \cdot 1 \cdot 1$ | $1$ |
> | $(3\ 2\ 1)$ | $-$ | $1 \cdot 3 \cdot 1$ | $-3$ |
>
> **$\det A = 24 - 4 + 1 - 3 = 18$.** Pro $n = 1$ je $\det(a) = a$, pro $n = 2$ vyjde $ad - bc$.

> [!pozor] $n!$ roste rychle
> Matice $4 \times 4$ má $24$ členů, $5 \times 5$ už $120$ a $10 \times 10$ přes $3{,}6$ milionu. Z definice se determinant počítá jen pro $n \le 3$; větší matice rozvojem (§4) nebo eliminací (§5).

> [!veta] Pozorování 10.6 · Determinant transponované matice
> ==Pro každou $A \in \mathbb{F}^{n \times n}$== platí
>
> $$
> \mathbf{\det A^{\mathsf{T}} = \det A} = \sum_{\pi \in S_n} \operatorname{sgn}\pi \cdot a_{\pi(1)1}\,a_{\pi(2)2} \cdots a_{\pi(n)n}.
> $$
>
> > [!note]- Důkaz
> > Součin $a_{1\pi(1)} \cdots a_{n\pi(n)}$ obsahuje z každého sloupce $j$ prvek $a_{\pi^{-1}(j)j}$, takže po přerovnání podle sloupců je to $a_{\sigma(1)1} \cdots a_{\sigma(n)n}$ se $\sigma = \pi^{-1}$. Když $\pi$ proběhne celé $S_n$, proběhne ho i $\pi^{-1}$ (inverze je bijekce $S_n \to S_n$), a podle [[věta o znaménku složené permutace|věty 9.18]] je $\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$. Součet je tedy $\sum_\sigma \operatorname{sgn}\sigma \cdot a_{\sigma(1)1} \cdots a_{\sigma(n)n}$, a to je definice $\det A^{\mathsf{T}}$, protože $[A^{\mathsf{T}}]_{i\sigma(i)} = a_{\sigma(i)i}$.

^veta-det-transpozice

> [!lidsky] Lidsky
> [[transponovaná matice|Překlopení podle diagonály]] determinant nezmění: rozestavění věží se jen zrcadlí a znaménko zůstává. Proto **co platí pro řádky, platí i pro sloupce**: rozvoj, úpravy, nulový řádek i nulový sloupec.

> [!example] Příklad
> $\begin{vmatrix} 3 & 1 \\ 4 & 2 \end{vmatrix} = 6 - 4 = 2$ a $\begin{vmatrix} 3 & 4 \\ 1 & 2 \end{vmatrix} = 6 - 4 = 2$. U $A$ z příkladu výše: $\det A^{\mathsf{T}} = \begin{vmatrix} 2 & 1 & 1 \\ 0 & 3 & 1 \\ 1 & 2 & 4 \end{vmatrix} = 24 + 1 + 0 - 3 - 4 - 0 = 18$.

> [!veta] Příklad 10.8 · Sarrusovo pravidlo
> ==Pro matici $3 \times 3$== platí
>
> $$
> \begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = \mathbf{aei + bfg + cdh - ceg - afh - bdi}.
> $$
>
> > [!note]- Důkaz
> > Šest členů definice: sudé permutace $(1\ 2\ 3)$, $(2\ 3\ 1)$, $(3\ 1\ 2)$ dávají $aei$, $bfg$, $cdh$ se znaménkem $+$, liché $(3\ 2\ 1)$, $(1\ 3\ 2)$, $(2\ 1\ 3)$ dávají $ceg$, $afh$, $bdi$ se znaménkem $-$.

^veta-sarrus

> [!lidsky] Lidsky
> Pomůcka, jak těch šest členů nezapomenout: **opiš pod matici první dva řádky**, tři úhlopříčky „dolů doprava“ vezmi s plusem, tři „dolů doleva“ s minusem.

> [!example] Příklad
> $\begin{vmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 4 \end{vmatrix}$: plus $2 \cdot 3 \cdot 4 + 0 \cdot 2 \cdot 1 + 1 \cdot 1 \cdot 1 = 25$, minus $1 \cdot 3 \cdot 1 + 2 \cdot 2 \cdot 1 + 0 \cdot 1 \cdot 4 = 7$. **$\det = 25 - 7 = 18$**, stejně jako z definice.

> [!obrazek] Sarrusovo pravidlo
> ![[lag14-sarrus.png]]
> *Matice $3 \times 3$ s opsanými prvními dvěma řádky (šedě). Modré úhlopříčky jdou dolů doprava a berou se s plusem, červené dolů doleva s minusem.*

> [!pozor] Sarrus jen pro $3 \times 3$
> Pro matici $4 \times 4$ by „úhlopříček“ s opsanými řádky bylo jen 8, ale determinant má $4! = 24$ členů. **Pro $n \ge 4$ Sarrusovo pravidlo neplatí**, použij rozvoj nebo eliminaci.

## §4 Rozvoj determinantu

> [!definice] Definice · pozn. 10.9 ♥
> Buď $A \in \mathbb{F}^{n \times n}$ a $A^{(i,j)} \in \mathbb{F}^{(n-1) \times (n-1)}$ matice, která vznikne z $A$ odstraněním $i$-tého řádku a $j$-tého sloupce. *Algebraický doplněk* pozice $(i, j)$ v matici $A$ je
>
> $$
> D_{ij} = (-1)^{i+j}\det A^{(i,j)}.
> $$

^def-algebraicky-doplnek

> [!lidsky] Lidsky
> Zakryj řádek a sloupec, ve kterém prvek stojí, spočítej determinant toho, co zbylo, a dej mu znaménko podle **šachovnice**: vlevo nahoře $+$ a sousední políčka se střídají. Znaménko patří **pozici**, ne číslu, které tam stojí.

> [!example] Příklad
> $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 4 \end{pmatrix}$: $D_{11} = +\begin{vmatrix} 3 & 2 \\ 1 & 4 \end{vmatrix} = 10$, $D_{12} = -\begin{vmatrix} 1 & 2 \\ 1 & 4 \end{vmatrix} = -2$, $D_{13} = +\begin{vmatrix} 1 & 3 \\ 1 & 1 \end{vmatrix} = -2$. Doplněk $D_{13}$ je záporný, i když má znaménko $+$: záporný je determinant podmatice.

> [!obrazek] Šachovnice znamének
> ![[lag14-sachovnice.png]]
> *Znaménka $(-1)^{i+j}$ pro matici $4 \times 4$: modré $+$, červené $-$. Zeleně orámovaná pozice $(2, 3)$ má znaménko $(-1)^5 = -1$, oranžově orámovaná $(3, 3)$ znaménko $(-1)^6 = +1$.*

> [!veta] Věta 10.10 · Rozvoj determinantu
> ==Buď $A \in \mathbb{F}^{n \times n}$ a $D_{ij}$ algebraické doplňky.== Pro každé $k \in \{1, \dots, n\}$ platí
>
> $$
> \det A = \sum_{i=1}^{n} a_{ik}D_{ik} \quad \text{(rozvoj podle $k$-tého sloupce)}, \qquad \det A = \sum_{i=1}^{n} a_{ki}D_{ki} \quad \text{(podle $k$-tého řádku)}.
> $$
>
> > [!note]- Důkaz\* (náznak)
> > Pro poslední sloupec: rozděl členy definice podle toho, ve kterém řádku $i$ je vybrán prvek posledního sloupce ($\pi(i) = n$), a vytkni $a_{in}$. Zbylé součiny berou po jednom prvku z matice $A^{(i,n)}$ a permutace s $\pi(i) = n$ odpovídají bijektivně permutacím $S_{n-1}$; znaménko se přitom změní o $(-1)^{n-i}$ (tolik inverzí přibude či ubude přesunem). Součet členů s $a_{in}$ je tedy $a_{in}(-1)^{i+n}\det A^{(i,n)} = a_{in}D_{in}$. Pro jiný sloupec se sloupec nejdřív přesune na konec, pro řádky se použije $\det A^{\mathsf{T}} = \det A$.

^veta-rozvoj

> [!lidsky] Lidsky
> Determinant velké matice převedeš na několik determinantů o řád menších: vyber **jeden** řádek nebo sloupec, každý jeho prvek vynásob jeho algebraickým doplňkem a sečti. Vyjde to stejně, ať vybereš kterýkoli, takže vyber ten **s nejvíc nulami**: nulové prvky jejich doplněk vůbec nepotřebují.

> [!example] Příklad
> Rozvoj $\begin{vmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 4 \end{vmatrix}$ podle 1. řádku: $2 \cdot 10 + 0 \cdot (-2) + 1 \cdot (-2) = 18$. ✓
>
> Matice $4 \times 4$ s jediným nenulovým prvkem ve 3. sloupci:
>
> $$
> \begin{vmatrix} 2 & 0 & 0 & 1 \\ 1 & 3 & 0 & 2 \\ 0 & 0 & 4 & 0 \\ 1 & 1 & 0 & 3 \end{vmatrix} = 4 \cdot (-1)^{3+3}\begin{vmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 3 \end{vmatrix} = 4 \cdot \big(2 \cdot 7 - 0 + 1 \cdot (-2)\big) = 4 \cdot 12 = 48.
> $$

> [!pozor] Častá chyba: zapomenuté znaménko
> V rozvoji se násobí $a_{ij}$ **algebraickým doplňkem** $D_{ij}$, ne jen determinantem podmatice. Rozvoj podle 2. řádku matice $3 \times 3$ začíná znaménkem **minus**: $-a_{21}\det A^{(2,1)} + a_{22}\det A^{(2,2)} - a_{23}\det A^{(2,3)}$.

> [!navic] Multilinearita (pozn. 10.11\*, věta 10.12\*)
> Z rozvoje podle $j$-tého sloupce je vidět, že determinant je **lineární v každém sloupci zvlášť** (při pevných ostatních): doplňky $D_{ij}$ na $j$-tém sloupci nezávisí. Takovému zobrazení se říká *multilineární*. Jako zobrazení $\mathbb{F}^{n \times n} \to \mathbb{F}$ ale determinant [[lineární zobrazení|lineární]] **není**: vytknutím z každého z $n$ sloupců dostaneš $\det(\alpha A) = \alpha^n\det A$, třeba $\det(2E_2) = 4 \ne 2 \det E_2$.

## §5 Trojúhelníkové matice a řádkové úpravy

> [!definice] Definice · pozn. 10.14
> Matice $A \in \mathbb{F}^{n \times n}$ je v *horním trojúhelníkovém tvaru*, jestliže $a_{ij} = 0$ pro každé $i > j$.

^def-horni-trojuhelnikova

> [!lidsky] Lidsky
> Pod hlavní diagonálou samé nuly, na ní a nad ní cokoli (i nuly). Čtvercová matice v [[horní stupňovitý tvar|horním stupňovitém tvaru]] je vždy horní trojúhelníková, takže na tenhle tvar ji dostane [[Gaussova eliminace]].

> [!example] Příklad
> $\begin{pmatrix} 2 & 5 & -1 \\ 0 & 3 & 7 \\ 0 & 0 & -4 \end{pmatrix}$ i $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$ jsou horní trojúhelníkové; [[jednotková matice]] taky. Nepříklad: $\begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$, protože $a_{21} = 1$.

> [!veta] Pozorování 10.15
> ==Buď $A \in \mathbb{F}^{n \times n}$ v horním trojúhelníkovém tvaru.== Potom
>
> $$
> \mathbf{\det A = a_{11}a_{22} \cdots a_{nn}}
> $$
>
> a **$A$ je regulární, právě když $a_{ii} \neq 0$ pro všechna $i$, tedy právě když $\det A \neq 0$.**
>
> > [!note]- Důkaz
> > Člen $a_{1\pi(1)} \cdots a_{n\pi(n)}$ může být nenulový, jen když $\pi(i) \ge i$ pro všechna $i$ (pod diagonálou jsou nuly). Pak $\pi(n) = n$, z prostoty $\pi(n-1) = n - 1$ atd., takže $\pi = \mathrm{id}$ a zbude jediný člen $+a_{11} \cdots a_{nn}$. Regularita: jsou-li všechna $a_{ii} \ne 0$, má matice $n$ pivotů a hodnost $n$. Je-li některé $a_{ii} = 0$, má po eliminaci méně než $n$ pivotů.

^veta-det-trojuhelnikove

> [!lidsky] Lidsky
> U trojúhelníkové matice je determinant zadarmo: **vynásob diagonálu**. Jediná nula na diagonále znamená $\det A = 0$ a singulární matici.

> [!example] Příklad
> $\begin{vmatrix} 2 & 5 & -1 \\ 0 & 3 & 7 \\ 0 & 0 & -4 \end{vmatrix} = 2 \cdot 3 \cdot (-4) = -24$, regulární. $\begin{vmatrix} 1 & 2 \\ 0 & 0 \end{vmatrix} = 0$, singulární.

> [!veta] Věta 10.16 · Determinant a elementární úpravy
> ==Buď $A \in \mathbb{F}^{n \times n}$ a $\tilde{A}$ vznikne z $A$ jednou [[elementární řádkové úpravy|elementární řádkovou úpravou]].== Potom
>
> 1. **prohození dvou řádků:** $\det\tilde{A} = -\det A$,
> 2. **vynásobení řádku číslem $\alpha$:** $\det\tilde{A} = \alpha\det A$,
> 3. **přičtení $\alpha$-násobku řádku k jinému řádku:** $\det\tilde{A} = \det A$.
>
> Totéž platí pro sloupcové úpravy (díky $\det A^{\mathsf{T}} = \det A$).
>
> > [!note]- Důkaz\* (náznak)
> > **1.** Nechť $\tau$ je transpozice prohazovaných řádků $k$, $l$. Řádek $i$ matice $\tilde{A}$ je řádek $\tau(i)$ matice $A$, takže člen pro $\pi$ v $\det\tilde{A}$ je $\prod_i a_{\tau(i)\pi(i)} = \prod_j a_{j\,\pi(\tau(j))}$. Substitucí $\sigma = \pi \circ \tau$ (bijekce $S_n \to S_n$) a $\operatorname{sgn}(\pi \circ \tau) = -\operatorname{sgn}\pi$ vyjde $\det\tilde{A} = -\det A$.
> >
> > **2.** Plyne z rozvoje podle upravovaného řádku: každý sčítanec se vynásobí $\alpha$.
> >
> > **3.** Rozvoj podle $l$-tého řádku, ke kterému se přičítá $\alpha$-násobek řádku $k$, rozdělí $\det\tilde{A}$ na $\det A + \alpha\det B$, kde $B$ je $A$ s řádkem $k$ napsaným i na místě řádku $l$. Matice $B$ má **dva stejné řádky**, a ta má determinant 0:
> >
> > > [!note]- Důkaz: dva stejné řádky ⇒ $\det B = 0$
> > > Nechť řádky $k \ne l$ matice $B$ jsou stejné a $\tau$ je transpozice $k \leftrightarrow l$. Permutace $\pi$ a $\pi \circ \tau$ vybírají v řádcích $k$ a $l$ prvky z prohozených sloupců: $b_{k\pi(l)}b_{l\pi(k)}$ místo $b_{k\pi(k)}b_{l\pi(l)}$. Protože jsou řádky stejné, je $b_{k\pi(l)} = b_{l\pi(l)}$ a $b_{l\pi(k)} = b_{k\pi(k)}$, takže oba členy mají **stejný součin**, ale **opačné znaménko** ($\operatorname{sgn}(\pi \circ \tau) = -\operatorname{sgn}\pi$). Zobrazení $\pi \mapsto \pi \circ \tau$ je bijekce mezi sudými a lichými permutacemi, takže
> > >
> > > $$
> > > \det B = \sum_{\pi \text{ sudá}} \big(b_{1\pi(1)} \cdots b_{n\pi(n)} - b_{1(\pi\tau)(1)} \cdots b_{n(\pi\tau)(n)}\big) = 0.
> > > $$

^veta-det-upravy

> [!lidsky] Lidsky
> Eliminace mění determinant předvídatelně: **prohození** otočí znaménko, **vynásobení řádku** $\alpha$ násobí determinant $\alpha$, **přičtení násobku** jiného řádku ho nechá být. Proto stačí matici eliminovat na trojúhelník, vynásobit diagonálu a opravit to o prohození a násobení.

> [!example] Příklad
> $\begin{vmatrix} 1 & 2 & 1 \\ 2 & 5 & 4 \\ -1 & 1 & 3 \end{vmatrix}$: $r_2 - 2r_1$ dá $(0\ 1\ 2)$, $r_3 + r_1$ dá $(0\ 3\ 4)$, $r_3 - 3r_2$ dá $(0\ 0\ {-2})$. Jen přičítání násobků, takže **$\det = 1 \cdot 1 \cdot (-2) = -2$**.
>
> S prohozením: $\begin{vmatrix} 0 & 2 \\ 3 & 1 \end{vmatrix}$ po $r_1 \leftrightarrow r_2$ je $\begin{vmatrix} 3 & 1 \\ 0 & 2 \end{vmatrix} = 6$, tedy původní determinant je $-6$ (a opravdu $0 \cdot 1 - 2 \cdot 3 = -6$).

> [!pozor] Častá chyba: „$r_2 \cdot a - c \cdot r_1$“ mění determinant
> Úprava $r_2 \to a\,r_2 - c\,r_1$ je **vynásobení** řádku $a$ a pak přičtení násobku, takže determinant **vynásobí $a$**. U $\begin{vmatrix} 2 & 1 \\ 3 & 4 \end{vmatrix} = 5$ dá $r_2 \to 2r_2 - 3r_1$ matici $\begin{pmatrix} 2 & 1 \\ 0 & 5 \end{pmatrix}$ s diagonálou $2 \cdot 5 = 10 = 2 \cdot 5$. Pro výpočet determinantu buď přičítej jen násobky ($r_2 - \tfrac{3}{2}r_1$), nebo si každé násobení zapiš a nakonec jím vyděl. Pro regularitu (zda $\det \ne 0$) to nevadí, $a \ne 0$.

> [!pozor] Těleso, kde $1 + 1 = 0$
> Častý krátký důkaz „prohozením dvou stejných řádků se matice nezmění, tedy $\det B = -\det B$ a $\det B = 0$“ potřebuje dělit dvěma. V [[grupa zbytkových tříd|tělese $\mathbb{Z}_2$]] je ale $1 + 1 = 0$, tam je $-x = x$ pro každé $x$ a rovnost $\det B = -\det B$ neříká nic. Nad $\mathbb{R}$, $\mathbb{Q}$, $\mathbb{C}$ (a každým [[číselné těleso|číselným tělesem]]) argument funguje; obecný důkaz páruje permutace $\pi$ a $\pi \circ \tau$ (vnořený důkaz výše).

> [!navic] Co z toho plyne dál
> Kombinací pozorování 10.15 a věty 10.16 vyjde, že **$A$ je regulární, právě když $\det A \ne 0$** (věta 10.18): eliminace na trojúhelníkový tvar nemění regularitu ani to, jestli je determinant nulový. Tím je motivace z §2 splněná. Výpočet eliminací spolu s rozvojem a vlastnost $\det(AB) = \det A \det B$ jsou na pořadu příště.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Kolik sčítanců má determinant matice $n \times n$ a jak vypadá každý z nich?
> **$n!$ sčítanců**, jeden za každou permutaci $\pi \in S_n$. Sčítanec je součin $n$ prvků, z **každého řádku i každého sloupce právě jednoho** ($a_{1\pi(1)} \cdots a_{n\pi(n)}$), se znaménkem **$\operatorname{sgn}\pi$**.

> [!karta|02]- Proč Sarrusovo pravidlo nefunguje pro matice $4 \times 4$?
> Determinant $4 \times 4$ má **$4! = 24$ sčítanců**, ale „úhlopříček“ s opsanými řádky je jen 8 a znaménka by ani neodpovídala znaménkům permutací. Sarrus je jen pomůcka pro **$n = 3$** ($3! = 6$ členů).

> [!karta|03]- Proč je determinant horní trojúhelníkové matice součin prvků na diagonále?
> Člen $a_{1\pi(1)} \cdots a_{n\pi(n)}$ je nenulový jen tehdy, když $\pi(i) \geq i$ pro všechna $i$ (pod diagonálou jsou nuly). To splní **jen identita**: $\pi(n) = n$, pak $\pi(n-1) = n - 1$ atd. Zbude jediný člen $+a_{11}a_{22} \cdots a_{nn}$.

> [!karta|04]- Proč platí $\det A^{\mathsf{T}} = \det A$?
> Součin $a_{1\pi(1)} \cdots a_{n\pi(n)}$ jde přeuspořádat podle sloupců na $a_{\sigma(1)1} \cdots a_{\sigma(n)n}$ se **$\sigma = \pi^{-1}$**. Když $\pi$ proběhne $S_n$, proběhne ho i $\pi^{-1}$, a **$\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$**. Vznikne přesně definice $\det A^{\mathsf{T}}$.

> [!karta|05]- Dokaž, že matice se dvěma stejnými řádky má determinant 0.
> Prohozením těch dvou řádků se matice **nezmění**, ale podle věty o úpravách se determinant **otočí**: $\det B = -\det B$, tedy $2\det B = 0$. Odtud **$\det B = 0$**, ale jen když $1 + 1 \neq 0$ (platí v $\mathbb{R}$, $\mathbb{Q}$, $\mathbb{C}$, ne v $\mathbb{Z}_2$).
>
> Obecně z definice: je-li $\tau$ transpozice prohazující ty dva řádky, mají sčítance pro $\pi$ a $\pi \circ \tau$ **stejný součin a opačné znaménko**, takže se po dvojicích **vyruší**.

> [!karta|06]- Jaká znaménka mají algebraické doplňky $D_{23}$ a $D_{33}$ v rozvoji matice $4 \times 4$ a podle čeho se to určuje?
> Znaménko je **$(-1)^{i+j}$** (šachovnice s $+$ v levém horním rohu): $D_{23}$ má $(-1)^5$, tedy **$-$**, $D_{33}$ má $(-1)^6$, tedy **$+$**. Závisí jen na **pozici** $(i, j)$, ne na hodnotě prvku $a_{ij}$ ani na velikosti matice.

> [!karta|07]- Podle kterého řádku nebo sloupce je nejlepší rozvíjet determinant a proč?
> Podle toho s **nejvíce nulami**: sčítanec $a_{ij}D_{ij}$ s $a_{ij} = 0$ je nulový a jeho doplněk (determinant o řád menší) **není třeba počítat**. Výsledek je podle věty o rozvoji stejný pro každý řádek i sloupec.

> [!karta|08]- Jak spočítáš determinant Gaussovou eliminací a na co si dát pozor?
> Řádkovými úpravami převeď matici na **horní trojúhelníkový tvar**, determinant je pak **součin diagonály**. Pozor: **každé prohození řádků** otočí znaménko a **vynásobení řádku** $\alpha$ násobí determinant $\alpha$; přičtení násobku jiného řádku ho nemění.

> [!karta|09]- Je determinant lineární zobrazení $\mathbb{F}^{n \times n} \to \mathbb{F}$? Zdůvodni.
> **Není** (pro $n \geq 2$): $\det(\alpha A) = \alpha^n\det A$, třeba $\det(2E_2) = 4 \neq 2 = 2\det E_2$. Ani součet nesedí: $\det E_2 + \det E_2 = 2$, ale $\det(2E_2) = 4$. Lineární je jen **v každém řádku (sloupci) zvlášť** = multilineární.

> [!karta|10]- Proč je matice $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ regulární, právě když $ad - bc \neq 0$?
> Pro $a \neq 0$ eliminace $r_2 \cdot a - c \cdot r_1$ dá druhý řádek $(0\ \ ad - bc)$: **druhý pivot existuje, právě když $ad - bc \neq 0$**. Pro $a = 0$ a $ad - bc = 0$ je $bc = 0$, takže první řádek nebo sloupec je nulový. Jinak se ověří vzorec $A \cdot \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = E$.

> [!karta|11]- Jaké znaménko má cyklus délky $k$ a proč?
> **$(-1)^{k-1}$**: cyklus délky $k$ je složením $k - 1$ transpozic, např. $(1\,2\,3) = (1\,3)(1\,2)$. Každá transpozice je lichá a **znaménka se při skládání násobí**. Cyklus délky 3 je tedy sudý, délky 2 a 4 lichý.

> [!karta|12]- Co znamená, že $\operatorname{sgn}$ je homomorfismus z $(S_n, \circ)$ do $(\{\pm 1\}, \cdot)$?
> Zachovává operaci: **$\operatorname{sgn}(\pi \circ \sigma) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\sigma$** (skládání permutací se převede na násobení $\pm 1$). Z toho plyne $\operatorname{sgn}\mathrm{id} = 1$ a $\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$.

> [!karta|13]- Jak se změní $\det A$, když prohodíš dva sloupce, a proč to smíš?
> **Otočí se znaménko**, stejně jako u řádků. Platí to díky **$\det A^{\mathsf{T}} = \det A$**: sloupcová úprava $A$ je řádková úprava $A^{\mathsf{T}}$.

### Příklady na procvičení

> [!priklad|14]- Zapiš $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 1 & 5 & 2 & 3 \end{pmatrix}$ cyklicky a urči její znaménko dvěma způsoby.
> $1 \to 4 \to 2 \to 1$, $3 \to 5 \to 3$: **$\sigma = (1\,4\,2)(3\,5)$**. Z cyklů: $(+1) \cdot (-1) = -1$. Z inverzí: $(1, 2)$, $(1, 4)$, $(3, 4)$, $(3, 5)$, $(1, 5)$ ($4 > 3$), tedy 5 inverzí. **$\operatorname{sgn}\sigma = -1$, lichá.**

> [!priklad|15]- Spočítej $\det A$ a $A^{-1}$ pro $A = \begin{pmatrix} 4 & 3 \\ 2 & 2 \end{pmatrix}$ vzorcem.
> $\det A = 8 - 6 = 2$, **$A^{-1} = \frac{1}{2}\begin{pmatrix} 2 & -3 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 1 & -\frac{3}{2} \\ -1 & 2 \end{pmatrix}$**. Kontrola: $\begin{pmatrix} 4 & 3 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} 1 & -3/2 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. ✓

> [!priklad|16]- Spočítej Sarrusovým pravidlem $\begin{vmatrix} 1 & 2 & 0 \\ 3 & 1 & -1 \\ 0 & 2 & 4 \end{vmatrix}$.
> Plus: $1 \cdot 1 \cdot 4 + 2 \cdot (-1) \cdot 0 + 0 \cdot 3 \cdot 2 = 4$. Minus: $0 \cdot 1 \cdot 0 + 1 \cdot (-1) \cdot 2 + 2 \cdot 3 \cdot 4 = -2 + 24 = 22$. **$\det = 4 - 22 = -18$.**

> [!priklad|17]- Rozvojem spočítej $\begin{vmatrix} 1 & 0 & 2 & 0 \\ 0 & 3 & 0 & 0 \\ 4 & 0 & 5 & 1 \\ 0 & 2 & 0 & 6 \end{vmatrix}$.
> Rozvoj podle 2. řádku (jen $a_{22} = 3$, znaménko $+$): $3\begin{vmatrix} 1 & 2 & 0 \\ 4 & 5 & 1 \\ 0 & 0 & 6 \end{vmatrix}$. Rozvoj podle 3. řádku (jen $6$ na $(3, 3)$, znaménko $+$): $3 \cdot 6 \cdot (5 - 8) =$ **$-54$**.

> [!priklad|18]- Eliminací spočítej $\begin{vmatrix} 0 & 1 & 2 \\ 1 & 1 & 1 \\ 2 & 3 & 1 \end{vmatrix}$.
> Prohoď $r_1 \leftrightarrow r_2$ (znaménko $-$): $\begin{vmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 2 & 3 & 1 \end{vmatrix}$; $r_3 - 2r_1$: $(0\ 1\ {-1})$; $r_3 - r_2$: $(0\ 0\ {-3})$. Diagonála $1 \cdot 1 \cdot (-3) = -3$, s prohozením **$\det = -(-3) = 3$**.

> [!priklad|19]- Rozhodni pomocí determinantu, zda je $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ regulární.
> Sarrus: $45 + 84 + 96 - 105 - 48 - 72 = 0$. Rychleji: $r_3 - r_2$ a $r_2 - r_1$ dají dva stejné řádky $(3\ 3\ 3)$. **$\det = 0$, matice je singulární.**

> [!priklad|20]- Pro $A \in \mathbb{R}^{3 \times 3}$ s $\det A = 2$ spočítej $\det(3A)$ a $\det A^{\mathsf{T}}$.
> Z každého ze tří řádků se vytkne 3: **$\det(3A) = 3^3 \cdot 2 = 54$**. **$\det A^{\mathsf{T}} = \det A = 2$.**

---
← [[LAG 13 – Inverzní matice eliminací, transpozice a grupy|6. 11. 2026 Inverzní matice eliminací, transpozice a grupy]] · [[LAG 15 – Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci|13. 11. 2026 Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci]] →

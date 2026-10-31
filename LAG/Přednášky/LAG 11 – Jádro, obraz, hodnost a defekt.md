---
predmet: LAG
prednaska: 11
datum: 2026-10-30
zdroj: "V poznámkách kap. 7 (pozn. 7.8–7.19) a začátek kap. 8 (text před větou 8.1)"
tags: [prednaska, LAG]
---

# LAG 11 – Jádro, obraz, hodnost a defekt

*Přednáška 11 · pátek 30. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `mono-, epi-, izomorfismus` · `regulární operátor a matice` · `izomorfní prostory` · `A⁻¹ je lineární` · `V ≅ 𝔽ⁿ` · `inverzní matice` · `jádro a obraz` · `im A = span sloupců` · `hodnost a defekt` · `prosté ⟺ ker A = {0}` · `A⁻¹{b} = {xₚ} + ker A` · `dim V = rank A + def A` · `matice soustavy`

Minule jsme si přesně zopakovali prosté, na a bijektivní zobrazení a na matici $\begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$ viděli, že vzor bodu je posunutá přímka. Dnes dostaly tyto pojmy u lineárních zobrazení vlastní jména (mono-, epi-, izomorfismus) a „vzor nuly“ a „obor hodnot“ se staly **jádrem** a **obrazem**. Jejich dimenze, **defekt** a **hodnost**, spolu vždy dají dimenzi definičního oboru. Na konci začala kapitola 8 o soustavách rovnic. Pět z patnácti definic na 1. zápočtový test (č. 11–15) je z této přednášky.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[monomorfismus]] | lineární a prosté | $(a; b) \mapsto a + bx^2$ |
| [[epimorfismus]] | lineární a na | derivace $\mathbb{R}^{\le 3}[x] \to \mathbb{R}^{\le 2}[x]$ |
| [[izomorfismus]] | lineární bijekce | $a + bx \mapsto (a; b)$ |
| [[regulární operátor]], [[regulární matice]] | izomorfismus $V \to V$, resp. $\mathbb{F}^n \to \mathbb{F}^n$ | $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ |
| [[izomorfní prostory]] | existuje mezi nimi izomorfismus, $V \cong W$ | $\mathbb{R}^{\le 2}[x] \cong \mathbb{R}^3$ |
| [[věta o linearitě inverzního zobrazení]] | inverze izomorfismu je lineární | |
| [[souřadnicový izomorfismus]] | $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$, tedy $\dim V = n \Rightarrow V \cong \mathbb{F}^n$ | |
| [[inverzní matice]] | $A^{-1}A = E$ | $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}^{-1} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$ |
| [[obraz lineárního zobrazení]] | $\operatorname{im} A = \{A\vec{x} \mid \vec{x} \in V\} \le W$ | $\operatorname{span}\{(1; 2)\}$ |
| [[jádro]] | $\ker A = \{\vec{x} \in V \mid A\vec{x} = \vec{0}\} \le V$ | $\operatorname{span}\{(1; 0; 0), (0; 1; -2)\}$ |
| [[věta o obrazu lineárního obalu]] | $\operatorname{im}$ matice = obal sloupců | |
| [[hodnost]], [[defekt]] | $\operatorname{rank} A = \dim \operatorname{im} A$, $\operatorname{def} A = \dim \ker A$ | $1$ a $2$ |
| [[věta o prostotě a jádru]] | prosté $\Leftrightarrow \ker A = \{\vec{0}\}$ | |
| [[věta o struktuře vzoru]] | $A^{-1}\{\vec{b}\} = \{\vec{x}_p\} + \ker A$ | |
| [[věta o dimenzi jádra a obrazu]] | $\dim V = \operatorname{rank} A + \operatorname{def} A$ | $3 = 1 + 2$ |
| [[matice soustavy]] | soustava = rovnice $A\vec{x} = \vec{b}$ | |

## §1 Mono-, epi- a izomorfismus

Prosté, na a bijektivní zobrazení známe z minula. Když je zobrazení navíc lineární, mají tyto vlastnosti vlastní jména.

> [!definice] Definice · pozn. 7.8 ♥
> Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$. [[lineární zobrazení|Lineární zobrazení]] $A : V \to W$ nazveme
>
> - *monomorfismus*, jestliže je [[injektivní zobrazení|injektivní]] (prosté),
> - *epimorfismus*, jestliže je [[surjektivní zobrazení|surjektivní]] (na),
> - *izomorfismus*, jestliže je [[bijekce|bijektivní]].
>
> [[lineární operátor|Lineárnímu operátoru]] $A : V \to V$ (nebo čtvercové matici), který je bijektivní, se říká *regulární*. Dva lineární prostory, mezi kterými existuje izomorfismus, se nazývají *izomorfní*; píšeme $V \cong W$.

^def-mono-epi-izo

> [!lidsky] Lidsky
> Nic nového, jen jména: **mono** = prosté, **epi** = na, **izo** = obojí, vždy u lineárního zobrazení. Izomorfismus je „překladač“ mezi dvěma prostory: každému vektoru z $V$ přiřadí právě jeden z $W$ a zachová sčítání i násobení. Izomorfní prostory jsou proto stejné, jen jinak zapsané.

> [!example] Příklad
> - $A : \mathbb{R}^2 \to \mathbb{R}^{\le 2}[x]$, $A(a; b) = a + bx^2$ je **monomorfismus** (různé dvojice dají různé polynomy), ale ne epimorfismus: polynom $x$ nemá vzor.
> - Derivace $D : \mathbb{R}^{\le 3}[x] \to \mathbb{R}^{\le 2}[x]$ je **epimorfismus** (každý $a + bx + cx^2$ je derivací $ax + \tfrac{b}{2}x^2 + \tfrac{c}{3}x^3$), ale ne monomorfismus: $D(1) = D(5) = 0$.
> - $a + bx \mapsto (a; b)$ je **izomorfismus** $\mathbb{R}^{\le 1}[x] \to \mathbb{R}^2$, takže $\mathbb{R}^{\le 1}[x] \cong \mathbb{R}^2$.
> - Otočení roviny o $90°$ je **regulární operátor** na $\mathbb{R}^2$; inverze je otočení o $-90°$.
> - Nepříklad: $f(x) = x + 1$ na $\mathbb{R}$ je bijekce, ale izomorfismus **není**, protože není lineární ($f(0) = 1 \ne 0$).

> [!navic] Značení na cvičení
> Na cvičení se píše *isomorfismus* a obraz často $\operatorname{Im}(f)$ s velkým I. Regulární matici cvičení definuje jako čtvercovou matici, ke které existuje $A^{-1}$ s $AA^{-1} = A^{-1}A = E_n$; nemá-li inverzi, je *singulární*. Je to totéž co bijektivní $\vec{x} \mapsto A\vec{x}$ (viz §2).

## §2 Inverze izomorfismu a izomorfní prostory

> [!veta] Věta 7.10
> ==Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$ izomorfismus.== Potom je **inverzní zobrazení $A^{-1} : W \to V$ lineární**.
>
> > [!note]- Důkaz
> > Vezmeme $\vec{x}, \vec{y} \in W$ a $\alpha \in \mathbb{F}$. Protože $A$ je bijekce, existují (jediné) $\vec{u}, \vec{v} \in V$ s $A\vec{u} = \vec{x}$ a $A\vec{v} = \vec{y}$, tedy $A^{-1}\vec{x} = \vec{u}$ a $A^{-1}\vec{y} = \vec{v}$. Z linearity $A$:
> >
> > $$
> > A(\alpha\vec{u} + \vec{v}) = \alpha A\vec{u} + A\vec{v} = \alpha\vec{x} + \vec{y}.
> > $$
> >
> > Vektor $\alpha\vec{u} + \vec{v}$ je tedy ten jediný vzor vektoru $\alpha\vec{x} + \vec{y}$, a proto
> >
> > $$
> > A^{-1}(\alpha\vec{x} + \vec{y}) = \alpha\vec{u} + \vec{v} = \alpha A^{-1}\vec{x} + A^{-1}\vec{y}.
> > $$
> >
> > To je [[kritérium linearity]].

^veta-inverze-linearni

> [!lidsky] Lidsky
> Když překladač $A$ zachovává sčítání a násobení, zachovává je i překlad zpátky. Trik důkazu: místo počítání s $A^{-1}$ si vektory z $W$ „pojmenuješ“ jejich vzory $\vec{u}$, $\vec{v}$ a počítáš s $A$, o kterém linearitu víš.

> [!example] Příklad
> $A(x; y) = (x + y; y)$ je izomorfismus $\mathbb{R}^2 \to \mathbb{R}^2$ s inverzí $A^{-1}(s; t) = (s - t; t)$. Ta je zase lineární: je to násobení maticí $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$. Kontrola: $A^{-1}(A(2; 3)) = A^{-1}(5; 3) = (2; 3)$.

> [!veta] Pozorování · pozn. 7.9
> Buďte $U$, $V$, $W$ lineární prostory nad $\mathbb{F}$.
>
> - **$V \cong V$** (izomorfismem je identita),
> - **$V \cong W \Rightarrow W \cong V$** (inverze izomorfismu je izomorfismus podle věty 7.10),
> - **$U \cong V$ a $V \cong W \Rightarrow U \cong W$** (složení lineárních zobrazení je lineární a složení bijekcí je bijekce).
>
> ==Je-li $\dim V = n < \infty$ a $\mathcal{X}$ báze $V$==, pak zobrazení $V \to \mathbb{F}^n$, $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$ je izomorfismus, tedy **$V \cong \mathbb{F}^n$**.

^veta-izomorfnost

> [!lidsky] Lidsky
> „Být izomorfní“ se chová jako „být stejný“: každý prostor je stejný sám se sebou, nezáleží na pořadí a stejnost se přenáší. A hlavně: **každý prostor dimenze $n$ je jen převlečené $\mathbb{F}^n$**. Převlek sundáš tak, že vektor nahradíš jeho [[souřadnicový vektor|souřadnicemi]]. Proto stačí umět počítat se sloupci čísel.

> [!example] Příklad
> V bázi $\mathcal{X} = (1, x, x^2)$ je $[3 - 2x + x^2]^{\mathcal{X}} = (3; -2; 1)$, takže $\mathbb{R}^{\le 2}[x] \cong \mathbb{R}^3$. Podobně $\mathbb{R}^{2 \times 2} \cong \mathbb{R}^4$ přes $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \mapsto (a; b; c; d)$. Z tranzitivity pak i $\mathbb{R}^{\le 3}[x] \cong \mathbb{R}^{2 \times 2}$, oba mají dimenzi 4.

Pro matice dostáváme z obecné definice konkrétní pojmy (pozn. 7.11):

> [!definice] Definice · pozn. 7.11 · regulární a inverzní matice
> Čtvercová matice $A \in \mathbb{F}^{n \times n}$ je *regulární*, právě když je zobrazení $\mathbb{F}^n \to \mathbb{F}^n$, $\vec{x} \mapsto A\vec{x}$ izomorfismus.
>
> Je-li $A$ regulární, definujeme *inverzní matici* $A^{-1} \in \mathbb{F}^{n \times n}$ jako tu jednoznačně určenou matici, pro kterou
>
> $$
> A^{-1}A = E \qquad (\text{tj. } A^{-1}A\vec{x} = \vec{x} \text{ pro všechna } \vec{x}).
> $$
>
> Je to matice inverzního zobrazení k $\vec{x} \mapsto A\vec{x}$, proto platí i $AA^{-1} = E$.

^def-regularni-matice

> [!lidsky] Lidsky
> Regulární matice je ta, se kterou jde „dělit“: z $A\vec{x} = \vec{b}$ dostaneš $\vec{x} = A^{-1}\vec{b}$. [[inverzní matice|Inverzní matice]] je maticová obdoba čísla $\tfrac{1}{a}$, jen místo jedničky je [[jednotková matice]] $E$.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ má sloupce LN, je regulární a $A^{-1} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$. Kontrola prvního sloupce $A^{-1}A$: $A^{-1}(1; 3) = (-2 + 3;\ \tfrac{3}{2} - \tfrac{3}{2}) = (1; 0)$. Nepříklad: $\begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$ z minula regulární není, zobrazení není prosté ani na.

> [!navic] Inverze v libovolných bázích (pozn. 7.11, cvičení)
> Pro izomorfismus $A : V \to W$ a báze $\mathcal{X}$, $\mathcal{Y}$ platí $[A^{-1}]^{\mathcal{Y} \to \mathcal{X}} = \big([A]^{\mathcal{X} \to \mathcal{Y}}\big)^{-1}$. Speciálně $\big([\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}\big)^{-1} = [\mathrm{id}]^{\mathcal{Y} \to \mathcal{X}}$: [[matice přechodu]] opačným směrem je inverzní maticí. Na cvičení $T_{X \to Y}^{-1} = T_{Y \to X}$.

## §3 Jádro a obraz

> [!definice] Definice · pozn. 7.12 ♥
> Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$. Definujeme
>
> - *obraz* $A$ jako jeho [[obor hodnot]]: $\operatorname{im} A = A(V) = \{A\vec{x} \mid \vec{x} \in V\} \subseteq W$,
> - *jádro* $A$ jako [[vzor množiny|vzor]] nulového vektoru: $\ker A = A^{-1}\{\vec{0}\} = \{\vec{x} \in V \mid A\vec{x} = \vec{0}\} \subseteq V$.
>
> Pro matici $A \in \mathbb{F}^{m \times n}$ (zobrazení $\mathbb{F}^n \to \mathbb{F}^m$) je $\operatorname{im} A = \{A\vec{x} \mid \vec{x} \in \mathbb{F}^n\}$ a $\ker A = \{\vec{x} \in \mathbb{F}^n \mid A\vec{x} = \vec{0}\}$.

^def-jadro-obraz

> [!lidsky] Lidsky
> **Obraz** je všechno, kam se zobrazení „trefí“. **Jádro** je všechno, co zobrazení „zabije“, tedy pošle na nulu. Jádro žije ve vstupním prostoru $V$, obraz ve výstupním $W$.

> [!example] Příklad z přednášky · $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix} : \mathbb{R}^3 \to \mathbb{R}^2$
> **Obraz.** $A(x; y; z) = x(0; 0) + y(2; 4) + z(1; 2)$, takže
>
> $$
> \operatorname{im} A = \operatorname{span}\Big\{\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \end{pmatrix}\Big\} = \operatorname{span}\Big\{\begin{pmatrix} 1 \\ 2 \end{pmatrix}\Big\},
> $$
>
> protože $(2; 4) = 2(1; 2)$ a nulový vektor obal nemění. Je to přímka $y = 2x$ v $\mathbb{R}^2$.
>
> **Jádro.** $A(x; y; z) = (0; 0)$ znamená
>
> $$
> \begin{aligned} 0x + 2y + 1z &= 0 \\ 0x + 4y + 2z &= 0 \end{aligned}
> $$
>
> Druhá rovnice je dvojnásobek první, zbývá $2y + z = 0$. Volíme $x = t$, $y = s$, pak $z = -2s$:
>
> $$
> \ker A = \Big\{\begin{pmatrix} t \\ s \\ -2s \end{pmatrix} \Bigm\vert t, s \in \mathbb{R}\Big\} = \Big\{t\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + s\begin{pmatrix} 0 \\ 1 \\ -2 \end{pmatrix}\Big\} = \operatorname{span}\Big\{\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -2 \end{pmatrix}\Big\},
> $$
>
> rovina v $\mathbb{R}^3$. Nepříklad: $(0; 1; 0) \notin \ker A$, protože $A(0; 1; 0) = (2; 4) \ne \vec{0}$.

> [!obrazek] Jádro a obraz matice $\begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$
> ![[lag11-priklad.png]]
> *Vlevo $\mathbb{R}^3$: zelená rovina je $\ker A$ se zelenými generátory $(1; 0; 0)$ a $(0; 1; -2)$, modrá rovnoběžná rovina je vzor bodu $(1; 2)$, tedy zelená rovina posunutá o červený bod $(0; 0; 1)$. Vpravo $\mathbb{R}^2$: oranžová přímka je $\operatorname{im} A$, modrý bod $(1; 2)$ v ní leží, červený $(1; 0)$ ne a nemá žádný vzor.*

> [!obrazek] Jádro a obraz obecně
> ![[lag11-jadro-obraz.png]]
> *Modrý prostor $V$ se zobrazí do oranžového $\operatorname{im} A$ uvnitř šedého $W$. Celé zelené jádro skončí v jediném bodě, nulovém vektoru $W$. Body $W$ mimo $\operatorname{im} A$ (červený křížek) nemají vzor.*

> [!veta] Věta 7.13
> ==Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$.== Potom
>
> 1. **$\operatorname{im} A$ je lineární podprostor $W$**,
> 2. **$\ker A$ je lineární podprostor $V$**.
>
> > [!note]- Důkaz
> > Obě množiny obsahují nulový vektor ($A\vec{0} = \vec{0}$), takže jsou neprázdné. Ověříme uzavřenost na lineární kombinace.
> >
> > 1. Buďte $\vec{v}, \vec{w} \in \operatorname{im} A$, $\alpha \in \mathbb{F}$. Pak existují $\vec{x}, \vec{y} \in V$ s $\vec{v} = A\vec{x}$, $\vec{w} = A\vec{y}$ a
> >
> > $$
> > \alpha\vec{v} + \vec{w} = \alpha A\vec{x} + A\vec{y} = A(\alpha\vec{x} + \vec{y}) \in \operatorname{im} A.
> > $$
> >
> > 2. Buďte $\vec{x}, \vec{y} \in \ker A$, tj. $A\vec{x} = \vec{0}$, $A\vec{y} = \vec{0}$, a $\alpha \in \mathbb{F}$. Pak
> >
> > $$
> > A(\alpha\vec{x} + \vec{y}) = \alpha A\vec{x} + A\vec{y} = \alpha\vec{0} + \vec{0} = \vec{0}, \quad\text{tedy } \alpha\vec{x} + \vec{y} \in \ker A.
> > $$

^veta-jadro-obraz-podprostory

> [!lidsky] Lidsky
> Co se „trefí“ a co se „zabije“, jsou vždy podprostory: přímky a roviny procházející nulou, nikdy posunuté. Důkaz je jen „linearita dovnitř a ven“: kombinace obrazů je obraz kombinace, kombinace zabitých vektorů je zabitá.

> [!example] Příklad
> U matice výše je $\operatorname{im} A$ přímka a $\ker A$ rovina, obojí přes počátek. Kdyby se jádro počítalo pro rovnici $2y + z = 1$, vyšla by posunutá rovina bez nuly, a to podprostor není. Proto jádro bere vždy nulu napravo.

> [!veta] Cvičení 7.14 · obraz a vzor podprostoru
> ==Buď $A \in \operatorname{Lin}(V, W)$.== Pak
>
> - **$U \le V \Rightarrow A(U) \le W$**: obraz podprostoru je podprostor,
> - **$U \le W \Rightarrow A^{-1}(U) \le V$**: vzor podprostoru je podprostor.
>
> Věta 7.13 je speciální případ pro $U = V$ a $U = \{\vec{0}\}$.

^veta-obraz-vzor-podprostoru

> [!lidsky] Lidsky
> Lineární zobrazení přenáší „rovné kusy přes nulu“ na „rovné kusy přes nulu“, a to oběma směry: tam obrazem, zpátky vzorem.

> [!example] Příklad
> Pro $A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$ a $U = \operatorname{span}\{(1; 0)\}$ (osa $x$ v $W$) je $A^{-1}(U) = \mathbb{R}^2$, celá rovina, protože všechno padne na osu $x$. Pro $U = \operatorname{span}\{(0; 1)\}$ (osa $y$) je $A^{-1}(U) = \ker A = \operatorname{span}\{(1; 1)\}$: na ose $y$ zasáhne $A$ jen nulu.

> [!veta] Pozorování 7.15
> ==Pro $A \in \operatorname{Lin}(V, W)$ a $\vec{x}_1, \dots, \vec{x}_n \in V$== platí
>
> $$
> \mathbf{A(\operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}) = \operatorname{span}\{A\vec{x}_1, \dots, A\vec{x}_n\}}.
> $$
>
> Generují-li $\vec{x}_1, \dots, \vec{x}_n$ celý $V$, je $\operatorname{im} A = \operatorname{span}\{A\vec{x}_1, \dots, A\vec{x}_n\}$. Pro matici $A = (\vec{a}_1\ \cdots\ \vec{a}_n) \in \mathbb{F}^{m \times n}$ se sloupci $\vec{a}_j$:
>
> $$
> \mathbf{\operatorname{im} A = \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n\} \le \mathbb{F}^m}.
> $$
>
> > [!note]- Proč
> > $A\vec{x} = x_1\vec{a}_1 + \dots + x_n\vec{a}_n$ ([[součin matice a vektoru]]), takže obrazy jsou právě lineární kombinace sloupců. Obecně: $A(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n) = \alpha_1A\vec{x}_1 + \dots + \alpha_nA\vec{x}_n$ ([[věta o zachování lineárních kombinací]]).

^veta-obraz-obalu

> [!lidsky] Lidsky
> Obraz poznáš z obrazů generátorů. U matice je to ještě snazší: **obraz = obal sloupců** (anglicky *column space*), protože sloupce jsou obrazy vektorů [[kanonická báze|kanonické báze]].

> [!example] Příklad
> $\operatorname{im}\begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ 1 & 3 & 0 \end{pmatrix} = \operatorname{span}\{(1; 2; 1), (2; 4; 3), (-1; -2; 0)\} = \operatorname{span}\{(1; 2; 1), (2; 4; 3)\}$, protože třetí sloupec je $-3 \cdot$ první $+$ druhý. U derivace na $\mathbb{R}^{\le 3}[x]$ stačí zderivovat generátory $1, x, x^2, x^3$: $\operatorname{im} D = \operatorname{span}\{0, 1, 2x, 3x^2\} = \mathbb{R}^{\le 2}[x]$.

> [!navic] Obraz abstraktního zobrazení přes jeho matici
> Pro $A \in \operatorname{Lin}(V, W)$ s bázemi $\mathcal{X}$ a $\mathcal{Y}$ platí $\vec{w} \in \operatorname{im} A \Leftrightarrow [\vec{w}]^{\mathcal{Y}} \in \operatorname{im}[A]^{\mathcal{X} \to \mathcal{Y}}$ ([[věta o souřadnicích obrazu]] a souřadnicový izomorfismus). U polynomů nebo matic tedy obraz spočítáš jako obal sloupců matice a výsledek přeložíš zpátky.

## §4 Hodnost, defekt a věta o dimenzi

> [!definice] Definice · pozn. 7.16 ♥
> Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$.
>
> - *Hodnost* lineárního zobrazení $A$ je číslo $\operatorname{rank} A = \dim \operatorname{im} A$.
> - *Defekt* lineárního zobrazení $A$ je číslo $\operatorname{def} A = \dim \ker A$.

^def-hodnost-defekt

> [!lidsky] Lidsky
> **Hodnost** = kolik směrů „přežije“ (dimenze toho, kam se trefíš). **Defekt** = kolik směrů se „ztratí“ (dimenze toho, co se zabije). Matice, která rovinu splácne do přímky, má hodnost 1 a defekt 1.

> [!example] Příklad
> $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$: $\operatorname{im} A = \operatorname{span}\{(1; 2)\}$, tedy **$\operatorname{rank} A = 1$**; $\ker A = \operatorname{span}\{(1; 0; 0), (0; 1; -2)\}$ a ty dva vektory jsou LN, tedy **$\operatorname{def} A = 2$**. Jednotková matice $E_3$: $\operatorname{rank} = 3$, $\operatorname{def} = 0$. Nulové zobrazení $\mathbb{R}^3 \to \mathbb{R}^2$: $\operatorname{rank} = 0$, $\operatorname{def} = 3$.

> [!veta] Věta 7.17
> ==Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$.== Potom
>
> $$
> \mathbf{A \text{ je prosté (monomorfismus)} \iff \ker A = \{\vec{0}\}}, \quad\text{tj. } \operatorname{def} A = 0.
> $$
>
> > [!note]- Důkaz
> > ($\Rightarrow$) $\ker A$ je podprostor, takže obsahuje $\vec{0}$. Prosté zobrazení má u každého bodu nanejvýš jeden vzor, speciálně vzorem nuly může být jen $\vec{0}$.
> >
> > ($\Leftarrow$) Nechť $A\vec{x}_1 = A\vec{x}_2$. Pak $\vec{0} = A\vec{x}_1 - A\vec{x}_2 = A(\vec{x}_1 - \vec{x}_2)$, tedy $\vec{x}_1 - \vec{x}_2 \in \ker A = \{\vec{0}\}$ a $\vec{x}_1 = \vec{x}_2$.

^veta-prostota-jadro

> [!lidsky] Lidsky
> U lineárního zobrazení stačí kontrolovat **jen nulu**: když se na nulu zobrazí jen nula, nesrazí se nikde žádné dva vektory. Dva vektory se srazí právě tehdy, když jejich rozdíl leží v jádře.

> [!example] Příklad
> $A(a; b) = a + bx^2$: $a + bx^2 = 0$ jen pro $a = b = 0$, tedy $\ker A = \{\vec{0}\}$ a $A$ je monomorfismus. Naopak $\begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$ prostá není: $(1; 0; 0) \in \ker A$, takže třeba $(5; 1; 1)$ a $(6; 1; 1)$ mají stejný obraz $(3; 6)$.

> [!pozor] Prostotu u lineárního zobrazení nedokazuj přes dva body
> Na testu se po tobě chce zdůvodnit, zda je zobrazení monomorfismus. Nejrychlejší je spočítat $\ker A$: vyjde-li $\{\vec{0}\}$, je prosté; najdeš-li nenulový $\vec{x}$ s $A\vec{x} = \vec{0}$, prosté není a tenhle $\vec{x}$ je celé zdůvodnění.

> [!veta] Věta 7.18
> ==Buďte $V$ a $W$ lineární prostory nad $\mathbb{F}$, $A \in \operatorname{Lin}(V, W)$, $\vec{b} \in W$ a nechť pro nějaké $\vec{x}_p \in V$ platí $A\vec{x}_p = \vec{b}$.== Potom
>
> $$
> \mathbf{A^{-1}\{\vec{b}\} = \{\vec{x}_p\} + \ker A = \{\vec{x}_p + \vec{x}_0 \mid \vec{x}_0 \in \ker A\}}.
> $$
>
> > [!note]- Důkaz
> > ($\supseteq$) Pro $\vec{x}_0 \in \ker A$ je $A(\vec{x}_p + \vec{x}_0) = A\vec{x}_p + A\vec{x}_0 = \vec{b} + \vec{0} = \vec{b}$.
> >
> > ($\subseteq$) Nechť $A\vec{x} = \vec{b}$. Hledáme $\vec{x}_0 \in \ker A$ s $\vec{x} = \vec{x}_p + \vec{x}_0$, takže položíme $\vec{x}_0 = \vec{x} - \vec{x}_p$. Ten v jádře opravdu je: $A\vec{x}_0 = A\vec{x} - A\vec{x}_p = \vec{b} - \vec{b} = \vec{0}$.

^veta-struktura-vzoru

> [!lidsky] Lidsky
> Všechna řešení $A\vec{x} = \vec{b}$ = **jedno konkrétní řešení** $\vec{x}_p$ („partikulární“) **+ cokoli z jádra**. Vzor bodu je jádro posunuté o $\vec{x}_p$: rovnoběžná kopie jádra, která neprochází nulou (pokud $\vec{b} \ne \vec{0}$).

> [!example] Příklad
> Pro $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$ a $\vec{b} = (1; 2)$ stačí uhodnout $\vec{x}_p = (0; 0; 1)$: $A\vec{x}_p = (1; 2)$. Pak
>
> $$
> A^{-1}\{(1; 2)\} = \{(0; 0; 1)\} + \operatorname{span}\{(1; 0; 0), (0; 1; -2)\},
> $$
>
> modrá rovina na obrázku v §3. Totéž v rovině ukazuje minulý obrázek:
>
> ![[lag10-vzory.png]]

> [!pozor] $A^{-1}\{\vec{b}\}$ není inverzní zobrazení
> Zápis $A^{-1}\{\vec{b}\}$ (se složenými závorkami) je [[vzor množiny]] a existuje pro každé lineární zobrazení. Je to podprostor jen pro $\vec{b} = \vec{0}$; pro $\vec{b} \ne \vec{0}$ nulu neobsahuje. A když $\vec{b} \notin \operatorname{im} A$, je prázdný a věta 7.18 se nepoužije, protože žádné $\vec{x}_p$ neexistuje.

> [!veta] Věta 7.19 (o dimenzi jádra a obrazu)
> ==Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$ a $A : V \to W$ lineární zobrazení.== Potom
>
> $$
> \mathbf{\dim V = \operatorname{rank} A + \operatorname{def} A}.
> $$
>
> > [!note]- Důkaz (pro $\dim V = n < \infty$)
> > Označme $k = \operatorname{def} A$ a vezměme bázi $(\vec{x}_1, \dots, \vec{x}_k)$ jádra. Tu [[věta o doplnění na bázi|doplníme na bázi]] $V$: $(\vec{x}_1, \dots, \vec{x}_k, \vec{y}_1, \dots, \vec{y}_{n-k})$. Ukážeme, že $(A\vec{y}_1, \dots, A\vec{y}_{n-k})$ je báze $\operatorname{im} A$; pak $\operatorname{rank} A = n - k$.
> >
> > **Generuje:** $\operatorname{im} A$ je obal obrazů celé báze (pozorování 7.15) a $A\vec{x}_i = \vec{0}$, takže zbývají $A\vec{y}_1, \dots, A\vec{y}_{n-k}$.
> >
> > **Je LN:** nechť $\alpha_1A\vec{y}_1 + \dots + \alpha_{n-k}A\vec{y}_{n-k} = \vec{0}$. Pak $A(\alpha_1\vec{y}_1 + \dots + \alpha_{n-k}\vec{y}_{n-k}) = \vec{0}$, takže tato kombinace leží v $\ker A$ a dá se zapsat bází jádra:
> >
> > $$
> > \alpha_1\vec{y}_1 + \dots + \alpha_{n-k}\vec{y}_{n-k} = \beta_1\vec{x}_1 + \dots + \beta_k\vec{x}_k.
> > $$
> >
> > Převedením na jednu stranu dostaneme $\alpha_1\vec{y}_1 + \dots + \alpha_{n-k}\vec{y}_{n-k} - \beta_1\vec{x}_1 - \dots - \beta_k\vec{x}_k = \vec{0}$, a protože je to báze $V$ (LN), jsou všechny koeficienty nulové, speciálně $\alpha_1 = \dots = \alpha_{n-k} = 0$.
> >
> > (Pro $\dim V = \infty$ se ukáže, že $\operatorname{rank} A$ nebo $\operatorname{def} A$ je nekonečno; pro lineární algebru to není podstatné.)

^veta-dimenze-jadra-obrazu

> [!lidsky] Lidsky
> **Směry vstupu se nikam neztrácejí bez evidence:** každý buď přežije (hodnost), nebo se zabije (defekt). Matice $\mathbb{R}^3 \to \mathbb{R}^2$ s hodností 1 musí 2 směry zabít. Pozor, počítá se s dimenzí **vstupu** $V$, ne výstupu $W$.

> [!example] Příklad
> $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$: $3 = 1 + 2$. Derivace na $\mathbb{R}^{\le 3}[x]$: jádro jsou konstanty ($\operatorname{def} = 1$), obraz $\mathbb{R}^{\le 2}[x]$ ($\operatorname{rank} = 3$), $4 = 3 + 1$. Rychlé použití: jádro $g(x; y; z) = (x + 2z;\ y - z)$ je $\operatorname{span}\{(-2; 1; 1)\}$, tedy $\operatorname{def} g = 1$ a $\operatorname{rank} g = 3 - 1 = 2 = \dim \mathbb{R}^2$, takže $g$ je na, aniž bys obraz počítal.

> [!obrazek] Hodnost + defekt = dimenze vstupu
> ![[lag11-dimenze.png]]
> *Oranžová část je hodnost (přežije), zelená defekt (zabije se); dohromady vždy dají dimenzi definičního oboru $V$. Otočení nezabije nic, nulové zobrazení všechno.*

> [!navic] Co z věty plyne (pozn. 7.21, 7.22)
> - **$\dim V > \dim W$ ⇒ $A$ není prosté**: $\operatorname{rank} A \le \dim W < \dim V$, takže $\operatorname{def} A > 0$.
> - **$\dim V < \dim W$ ⇒ $A$ není na**: $\operatorname{rank} A \le \dim V < \dim W$.
> - **Operátor na prostoru konečné dimenze** ($A \in \operatorname{Lin}(V)$, $\dim V < \infty$): mono ⟺ epi ⟺ izo, protože $\operatorname{def} A = 0 \Leftrightarrow \operatorname{rank} A = \dim V \Leftrightarrow \operatorname{im} A = V$ ([[věta o dimenzi podprostoru]]). Pro čtvercovou matici: sloupce LN ⟺ generují ⟺ báze ([[věta o bázi z n vektorů]]).
> - V nekonečné dimenzi to neplatí: derivace na $\mathbb{R}[x]$ je epi, ale ne mono; integrování $p \mapsto \int_0^x p$ je mono, ale ne epi.

## §5 Soustavy lineárních rovnic

Kapitola 8 začíná tím, že soustavu lineárních rovnic napíšeme jako jednu maticovou rovnici. Všechno z §3 a §4 se pak dá použít na soustavy.

> [!definice] Definice · text před větou 8.1 · matice soustavy
> Soustava $m$ rovnic o $n$ neznámých nad $\mathbb{F}$
>
> $$
> \begin{aligned} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\ &\ \ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m \end{aligned}
> $$
>
> je ekvivalentní rovnici $A\vec{x} = \vec{b}$, kde $A = (a_{ij}) \in \mathbb{F}^{m \times n}$ je *matice soustavy*, $\vec{x} = (x_1; \dots; x_n) \in \mathbb{F}^n$ *sloupec neznámých* a $\vec{b} = (b_1; \dots; b_m) \in \mathbb{F}^m$ *sloupec pravých stran*. Matice $(A \mid \vec{b}) \in \mathbb{F}^{m \times (n+1)}$ je *[[rozšířená matice soustavy]]*. Soustava je *[[homogenní soustava|homogenní]]* (bez pravé strany), je-li $\vec{b} = \vec{0}$.

^def-matice-soustavy

> [!lidsky] Lidsky
> Celá soustava se vejde do tří objektů: tabulka koeficientů $A$, sloupec neznámých $\vec{x}$ a sloupec pravých stran $\vec{b}$. Vyřešit soustavu = najít [[vzor množiny|vzor]] $\vec{b}$ při zobrazení $\vec{x} \mapsto A\vec{x}$ = zapsat $\vec{b}$ jako lineární kombinaci sloupců $A$.

> [!example] Příklad
> Soustava $x - y + 2z = 3$, $2x + y = 0$ má matici soustavy $\begin{pmatrix} 1 & -1 & 2 \\ 2 & 1 & 0 \end{pmatrix} \in \mathbb{R}^{2 \times 3}$, sloupec pravých stran $(3; 0)$ a rozšířenou matici $\left(\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 2 & 1 & 0 & 0 \end{array}\right)$. Množina řešení homogenní soustavy (s pravou stranou $(0; 0)$) je $\ker A$.

> [!navic] Slovník soustava ↔ zobrazení
> | soustava $A\vec{x} = \vec{b}$ | zobrazení $\vec{x} \mapsto A\vec{x}$ |
> | --- | --- |
> | množina řešení homogenní soustavy | $\ker A$, podprostor dimenze $n - \operatorname{rank} A$ |
> | soustava má řešení | $\vec{b} \in \operatorname{im} A$ |
> | množina všech řešení | $A^{-1}\{\vec{b}\} = \{\vec{x}_p\} + \ker A$ |
> | nejvýš jedno řešení pro každé $\vec{b}$ | $\ker A = \{\vec{0}\}$, monomorfismus |
>
> Přesně to shrne Frobeniova věta (věta 8.1) na příští přednášce.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Dokaž, že inverze izomorfismu $A : V \to W$ je lineární zobrazení.
> Pro $\vec{x}, \vec{y} \in W$ vezmi jejich vzory $\vec{u} = A^{-1}\vec{x}$, $\vec{v} = A^{-1}\vec{y}$. Z **linearity $A$**: $A(\alpha\vec{u} + \vec{v}) = \alpha\vec{x} + \vec{y}$, takže $\alpha\vec{u} + \vec{v}$ je **ten jediný vzor** $\alpha\vec{x} + \vec{y}$ a $A^{-1}(\alpha\vec{x} + \vec{y}) = \alpha A^{-1}\vec{x} + A^{-1}\vec{y}$.

> [!karta|02]- Proč je relace „$V$ je izomorfní s $W$“ symetrická a tranzitivní?
> **Symetrie:** inverze izomorfismu $V \to W$ je bijekce $W \to V$ a podle věty o linearitě inverze je **lineární**. **Tranzitivita:** složení izomorfismů $U \to V \to W$ je lineární (složení lineárních) a bijektivní (složení bijekcí).

> [!karta|03]- Proč jsou každé dva lineární prostory nad $\mathbb{F}$ se stejnou konečnou dimenzí $n$ izomorfní?
> Každý je izomorfní s $\mathbb{F}^n$ přes **souřadnice** $\vec{v} \mapsto [\vec{v}]^{\mathcal{X}}$. Ze $V \cong \mathbb{F}^n$ a $W \cong \mathbb{F}^n$ plyne **symetrií a tranzitivitou** $V \cong W$. Např. $\mathbb{R}^{\le 3}[x] \cong \mathbb{R}^{2 \times 2}$.

> [!karta|04]- Dokaž, že $\ker A$ a $\operatorname{im} A$ jsou podprostory.
> Obě obsahují $\vec{0}$. **Jádro:** $A\vec{x} = A\vec{y} = \vec{0} \Rightarrow A(\alpha\vec{x} + \vec{y}) = \alpha\vec{0} + \vec{0} = \vec{0}$. **Obraz:** $\vec{v} = A\vec{x}$, $\vec{w} = A\vec{y} \Rightarrow \alpha\vec{v} + \vec{w} = A(\alpha\vec{x} + \vec{y}) \in \operatorname{im} A$. V obou krocích jen **linearita**.

> [!karta|05]- Proč je obraz matice $A \in \mathbb{F}^{m \times n}$ roven obalu jejích sloupců?
> $A\vec{x} = x_1\vec{a}_1 + \dots + x_n\vec{a}_n$, takže **každý obraz je lineární kombinace sloupců** a naopak každá kombinace sloupců je obraz vektoru jejích koeficientů. Sloupce jsou obrazy vektorů kanonické báze.

> [!karta|06]- Dokaž, že lineární zobrazení $A$ je prosté, právě když $\ker A = \{\vec{0}\}$.
> ($\Rightarrow$) $\vec{0} \in \ker A$ a prosté zobrazení má u nuly **nejvýš jeden vzor**. ($\Leftarrow$) Z $A\vec{x}_1 = A\vec{x}_2$ plyne $A(\vec{x}_1 - \vec{x}_2) = \vec{0}$, tedy **$\vec{x}_1 - \vec{x}_2 \in \ker A = \{\vec{0}\}$** a $\vec{x}_1 = \vec{x}_2$.

> [!karta|07]- Dokaž, že každé řešení $A\vec{x} = \vec{b}$ má tvar $\vec{x}_p + \vec{x}_0$ s $\vec{x}_0 \in \ker A$, je-li $A\vec{x}_p = \vec{b}$.
> Polož **$\vec{x}_0 = \vec{x} - \vec{x}_p$**. Pak $A\vec{x}_0 = A\vec{x} - A\vec{x}_p = \vec{b} - \vec{b} = \vec{0}$, takže $\vec{x}_0 \in \ker A$ a $\vec{x} = \vec{x}_p + \vec{x}_0$. (Opačná inkluze: $A(\vec{x}_p + \vec{x}_0) = \vec{b} + \vec{0}$.)

> [!karta|08]- Kolik řešení může mít soustava $A\vec{x} = \vec{b}$ nad $\mathbb{R}$ a čím je to dané?
> **Žádné**, když $\vec{b} \notin \operatorname{im} A$. Jinak $\{\vec{x}_p\} + \ker A$: **právě jedno** při $\ker A = \{\vec{0}\}$, **nekonečně mnoho** při $\operatorname{def} A \ge 1$ (jádro obsahuje celou přímku). Dvě nebo pět řešení nastat nemůže.

> [!karta|09]- Jak se v důkazu $\dim V = \operatorname{rank} A + \operatorname{def} A$ získá báze obrazu?
> Bázi jádra $(\vec{x}_1, \dots, \vec{x}_k)$ **doplň na bázi $V$** vektory $\vec{y}_1, \dots, \vec{y}_{n-k}$. Obrazy $A\vec{y}_1, \dots, A\vec{y}_{n-k}$ generují $\operatorname{im} A$ (protože $A\vec{x}_i = \vec{0}$) a jsou LN: kombinace s nulovým obrazem leží v jádře, je tedy kombinací $\vec{x}_i$, a z **LN báze $V$** jsou všechny koeficienty nulové.

> [!karta|10]- Proč lineární zobrazení $A : V \to W$ s $\dim V > \dim W$ nemůže být prosté a s $\dim V < \dim W$ nemůže být na?
> $\operatorname{im} A \le W$ a podle věty o dimenzi $\operatorname{rank} A \le \dim V$. Při $\dim V > \dim W$ je **$\operatorname{def} A = \dim V - \operatorname{rank} A \ge \dim V - \dim W > 0$**. Při $\dim V < \dim W$ je **$\operatorname{rank} A \le \dim V < \dim W$**, takže $\operatorname{im} A \ne W$.

> [!karta|11]- Proč je pro lineární operátor na prostoru konečné dimenze prostota totéž co surjektivita? Platí to i pro $\mathbb{R}[x]$?
> $\operatorname{def} A = 0 \Leftrightarrow \operatorname{rank} A = \dim V \Leftrightarrow \operatorname{im} A = V$ (**věta o dimenzi** a podprostor plné dimenze je celý prostor). Pro $\mathbb{R}[x]$ (**nekonečná dimenze**) ne: derivace je na, ale ne prostá ($D(1) = D(5) = 0$).

> [!karta|12]- Ve kterém prostoru leží jádro a ve kterém obraz lineárního zobrazení $A : V \to W$?
> **$\ker A \le V$** (vstupy, které se zobrazí na nulu), **$\operatorname{im} A \le W$** (výstupy). U matice $m \times n$ je jádro v $\mathbb{F}^n$ (počet sloupců), obraz v $\mathbb{F}^m$ (počet řádků).

> [!karta|13]- Proč je vzor $A^{-1}\{\vec{b}\}$ při lineárním zobrazení podprostor jen pro $\vec{b} = \vec{0}$?
> Podprostor musí obsahovat $\vec{0}$, ale **$A\vec{0} = \vec{0} \ne \vec{b}$**, takže pro $\vec{b} \ne \vec{0}$ nula ve vzoru není. Vzor je pak **posunuté jádro** $\{\vec{x}_p\} + \ker A$, nebo prázdná množina.

> [!karta|14]- Jak poznáš z hodnosti a defektu, že $A : V \to W$ (konečné dimenze) je mono-, epi- nebo izomorfismus?
> **Mono** ⟺ $\operatorname{def} A = 0$. **Epi** ⟺ $\operatorname{rank} A = \dim W$. **Izo** ⟺ obojí, a pak nutně $\dim V = \dim W$.

### Příklady na procvičení

> [!priklad|15]- Pro $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$ urči $\ker A$, $\operatorname{im} A$, hodnost a defekt a ověř větu o dimenzi.
> $\operatorname{im} A = \operatorname{span}\{(0; 0), (2; 4), (1; 2)\} = \operatorname{span}\{(1; 2)\}$, **$\operatorname{rank} A = 1$**. Jádro: $2y + z = 0$, s $x = t$, $y = s$ je $z = -2s$, **$\ker A = \operatorname{span}\{(1; 0; 0), (0; 1; -2)\}$**, vektory nejsou násobky, **$\operatorname{def} A = 2$**. Kontrola: $\dim \mathbb{R}^3 = 3 = 1 + 2$.

> [!priklad|16]- Pro $A = \begin{pmatrix} 0 & 2 & 1 \\ 0 & 4 & 2 \end{pmatrix}$ najdi vzor bodu $(1; 2)$ a vzor bodu $(1; 0)$.
> $(1; 2)$ je třetí sloupec, takže $\vec{x}_p = (0; 0; 1)$. **$A^{-1}\{(1; 2)\} = \{(0; 0; 1)\} + \operatorname{span}\{(1; 0; 0), (0; 1; -2)\}$**. Bod $(1; 0)$ není násobkem $(1; 2)$, leží mimo $\operatorname{im} A$: **vzor je $\emptyset$**.

> [!priklad|17]- Je $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ regulární? Ověř, že $A^{-1} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$.
> Sloupce $(1; 3)$ a $(2; 4)$ nejsou násobky, jsou LN, tedy $\ker A = \{\vec{0}\}$ a $\operatorname{rank} A = 2$: zobrazení je prosté i na, **$A$ je regulární**. $A^{-1}A = \begin{pmatrix} -2 + 3 & -4 + 4 \\ \tfrac{3}{2} - \tfrac{3}{2} & 3 - 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, **takže je to inverze**.

> [!priklad|18]- Urči jádro, obraz, hodnost a defekt derivace $D : \mathbb{R}^{\le 3}[x] \to \mathbb{R}^{\le 3}[x]$. Je to mono-, epi- nebo izomorfismus?
> $D(a + bx + cx^2 + dx^3) = b + 2cx + 3dx^2 = 0 \Leftrightarrow b = c = d = 0$: **$\ker D$ = konstanty $= \operatorname{span}\{1\}$**, $\operatorname{def} D = 1$. $\operatorname{im} D = \operatorname{span}\{D1, Dx, Dx^2, Dx^3\} = \operatorname{span}\{0, 1, 2x, 3x^2\} = \mathbb{R}^{\le 2}[x]$, **$\operatorname{rank} D = 3$**, $4 = 3 + 1$. **Ani mono, ani epi** ($x^3 \notin \operatorname{im} D$).

> [!priklad|19]- Existuje prosté lineární zobrazení $\mathbb{R}^3 \to \mathbb{R}^2$? A lineární zobrazení $\mathbb{R}^2 \to \mathbb{R}^3$, které je na?
> **Ne a ne.** Pro $A : \mathbb{R}^3 \to \mathbb{R}^2$ je $\operatorname{rank} A \le 2$, takže $\operatorname{def} A = 3 - \operatorname{rank} A \ge 1$ a jádro je netriviální. Pro $B : \mathbb{R}^2 \to \mathbb{R}^3$ je $\operatorname{rank} B \le 2 < 3$, takže $\operatorname{im} B \ne \mathbb{R}^3$.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|20]- Rozhodni, zda je lineární zobrazení $f : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $f(ax^2 + bx + c) = (a + b)x^2 + (b + c)x + (a + c)$ izomorfismus.
> **Jádro:** $f(p) = 0$ znamená $a + b = 0$, $b + c = 0$, $a + c = 0$. Z prvních dvou $a = -b = c$, ze třetí $2a = 0$, tedy $a = b = c = 0$ a $\ker f = \{0\}$: $f$ je **monomorfismus**. Podle věty o dimenzi $\operatorname{rank} f = 3 - 0 = 3 = \dim \mathbb{R}^{\le 2}[x]$, takže $\operatorname{im} f = \mathbb{R}^{\le 2}[x]$ a $f$ je i **epimorfismus**.
>
> **Ano, $f$ je izomorfismus.**

> [!priklad|21]- Rozhodni, zda je lineární zobrazení $f : \mathbb{R}^{2 \times 2} \to \mathbb{R}^{2 \times 2}$, $f(X) = X \cdot \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ monomorfismus. Urči hodnost a defekt.
> $\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} a + b & a + b \\ c + d & c + d \end{pmatrix}$. Třeba $X = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} \ne 0$ má $f(X) = 0$, takže $\ker f \ne \{0\}$ a **$f$ není monomorfismus**.
>
> $\ker f = \{b = -a,\ d = -c\} = \operatorname{span}\Big\{\begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & -1 \end{pmatrix}\Big\}$, **$\operatorname{def} f = 2$**, a **$\operatorname{rank} f = 4 - 2 = 2$**.

> [!priklad|22]- Dokaž, že $g : \mathbb{R}^3 \to \mathbb{R}^2$, $g(x; y; z) = (x + 2z;\ y - z)$ je lineární, urči $\operatorname{Im} g$ a $\ker g$. Je $g$ epimorfismus?
> $g(\vec{v}) = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}\vec{v}$ je násobení maticí, tedy **lineární**. $\operatorname{Im} g$ = obal sloupců $(1; 0)$, $(0; 1)$, $(2; -1)$, a první dva už generují $\mathbb{R}^2$: **$\operatorname{Im} g = \mathbb{R}^2$**. Jádro: $x = -2z$, $y = z$, **$\ker g = \operatorname{span}\{(-2; 1; 1)\}$**; kontrola $3 = 2 + 1$.
>
> **Ano, $g$ je epimorfismus** (ale ne monomorfismus).

> [!priklad|23]- Pro $h : \mathbb{R}^2 \to \mathbb{R}^3$, $h(x; y) = (x - y;\ 2x - 2y;\ 0)$ najdi bázi jádra a obrazu, hodnost a defekt. Je $h$ mono-, epi-, nebo izomorfismus?
> Matice $\begin{pmatrix} 1 & -1 \\ 2 & -2 \\ 0 & 0 \end{pmatrix}$, druhý sloupec je $-1 \cdot$ první: **báze $\operatorname{im} h$ je $((1; 2; 0))$, $\operatorname{rank} h = 1$**. $h(x; y) = 0 \Leftrightarrow x = y$: **báze $\ker h$ je $((1; 1))$, $\operatorname{def} h = 1$**. Kontrola $2 = 1 + 1$.
>
> **Není mono** ($\operatorname{def} h = 1$), **není epi** ($\operatorname{rank} h = 1 < 3$), tedy ani izo.

> [!priklad|24]- Najdi bázi jádra a obrazu matice $A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ 1 & 3 & 0 \end{pmatrix}$ a urči $\operatorname{rank} A$, $\operatorname{def} A$.
> Druhý řádek je dvojnásobek prvního, zbývá $x + 2y - z = 0$, $x + 3y = 0$. S $y = t$: $x = -3t$, $z = x + 2y = -t$. **Báze $\ker A$ je $((-3; 1; -1))$, $\operatorname{def} A = 1$.** Kontrola: $A(-3; 1; -1) = (-3 + 2 + 1;\ -6 + 4 + 2;\ -3 + 3 + 0) = \vec{0}$.
>
> Podle věty o dimenzi $\operatorname{rank} A = 3 - 1 = 2$. Sloupce $(1; 2; 1)$ a $(2; 4; 3)$ nejsou násobky, jsou LN a leží v $\operatorname{im} A$: **báze $\operatorname{im} A$ je $((1; 2; 1), (2; 4; 3))$, $\operatorname{rank} A = 2$**.

---
← [[LAG 10 – Obraz a vzor při lineárním zobrazení|23. 10. 2026 Obraz a vzor při lineárním zobrazení]]

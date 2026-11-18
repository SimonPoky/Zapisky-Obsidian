---
predmet: LAG
prednaska: 16
datum: 2026-11-18
zdroj: "pozn. 11.1 až 11.24"
tags: [prednaska, LAG]
---

# LAG 16 – Vlastní čísla, charakteristický polynom a diagonalizace

*Přednáška 16 · středa 18. 11. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `mocniny matice Fibonacciho systému` · `vlastní číslo a vlastní vektor` · `id, nulový operátor, projekce` · `λ = 0 ⟺ singulární` · `(A − λE)x = 0` · `det(A − λE) = 0` · `vlastní podprostor` · `geometrická násobnost` · `kořen a násobnost kořene` · `základní věta algebry` · `charakteristický polynom` · `algebraická násobnost` · `řádkové úpravy mění vlastní čísla` · `podobné matice` · `diagonalizovatelný operátor` · `báze z vlastních vektorů` · `A = TDT⁻¹` · `otočení o 90° nad ℂ`

Minule jsme Fibonacciho čísla spočítali vzorcem a všimli si, že matice rekurence některé vektory jen natáhne. Dnes z toho je obecná teorie: vektorům $\vec{x} \neq \vec{0}$ s $A\vec{x} = \lambda\vec{x}$ říkáme vlastní vektory, čísla $\lambda$ najdeme jako kořeny charakteristického polynomu $\det(A - \lambda E)$. Když vlastní vektory tvoří bázi, je matice operátoru v této bázi diagonální a mocniny, které jinak vyžadují spoustu násobení, se spočítají po prvcích.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| vlastní číslo, vlastní vektor ♥ | $A\vec{x} = \lambda\vec{x}$ pro nějaké $\vec{x} \neq \vec{0}$ | $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ |
| věta o nulovém vlastním čísle | $0$ je vlastní číslo $\Leftrightarrow$ $\ker A \neq \{\vec{0}\}$ $\Leftrightarrow$ $A$ singulární | projekce na osu $x$ |
| věta o vlastních číslech a char. polynomu | $\lambda$ vlastní číslo $\Leftrightarrow$ $\det(A - \lambda E) = 0$ | $(3 - \lambda)(2 - \lambda) = 0$ |
| vlastní podprostor, geometrická násobnost | $\ker(A - \lambda\,\mathrm{id})$ a jeho dimenze | $\lambda = 3$: $\operatorname{span}\{(1; 1)\}$, dimenze $1$ |
| násobnost kořene | $p(x) = (x - \alpha)^k q(x)$, $q(\alpha) \neq 0$ | $(x - 2)^2(x + 1)$: kořen $2$ je dvojnásobný |
| věta o počtu kořenů polynomu | stupeň $n$ $\Rightarrow$ nejvýš $n$ kořenů i s násobnostmi | $x^2 + 1$ nemá v $\mathbb{R}$ žádný |
| základní věta algebry | nad $\mathbb{C}$ se každý polynom rozloží na kořenové činitele | $x^2 + 1 = (x - \mathrm{i})(x + \mathrm{i})$ |
| charakteristický polynom ♥ | $p_A(x) = \det(A - xE)$, stupeň $n$ | $p_A(\lambda) = \lambda^2 - 5\lambda + 6$ |
| algebraická násobnost | násobnost $\lambda$ jako kořene $p_A$ | $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$: $\lambda = 2$ dvojnásobné |
| podobné matice ♥ | $B = T^{-1}AT$ pro regulární $T$ | $B = [A]^{\mathcal{X}}$ je podobná $A = [A]^{\mathcal{E}}$ |
| věta o podobných maticích | podobné $\Rightarrow$ stejný $p_A$, stejná vlastní čísla | obrácení neplatí: $O_2$ a $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ |
| diagonalizovatelný operátor ♥ | v nějaké bázi má diagonální matici | Fibonacci: $[A]^{\mathcal{X}} = \operatorname{diag}(\varphi_+, \varphi_-)$ |
| diagonalizovatelná matice | $A = TDT^{-1}$, $D$ diagonální | $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix} = T\operatorname{diag}(2, 3)T^{-1}$ |
| věta o diagonalizovatelnosti | diagonalizovatelný $\Leftrightarrow$ existuje báze z vlastních vektorů | otočení o $90°$: nad $\mathbb{R}$ ne, nad $\mathbb{C}$ ano |

## §1 Motivace: mocniny matice Fibonacciho systému

Fibonacciho rekurenci $a_{n+2} = a_{n+1} + a_n$ zapíšeme jako dynamický systém: stav je dvojice sousedních členů $(a_n; a_{n+1})$ a jeden krok ho posune o člen dál,

$$
A\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ x + y \end{pmatrix}, \qquad [A]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}.
$$

Od $(0; 1)$ dostaneme $(1; 1)$, $(1; 2)$, $(2; 3)$, $(3; 5)$, … a $n$-té Fibonacciho číslo je první složka $A^n(0; 1)$. Otázka tedy zní: **kolik je $A^n$?**

S [[diagonální matice|diagonální maticí]] by to bylo snadné, mocní se po prvcích: $\operatorname{diag}(a, b)^n = \operatorname{diag}(a^n, b^n)$. Matice $A$ diagonální není, ale dva směry jen natahuje. Pro $\varphi_\pm = \frac{1 \pm \sqrt{5}}{2}$ (kořeny $\lambda^2 = \lambda + 1$, [[zlatý řez]]) platí

$$
A\begin{pmatrix} 1 \\ \varphi_\pm \end{pmatrix} = \begin{pmatrix} \varphi_\pm \\ 1 + \varphi_\pm \end{pmatrix} = \begin{pmatrix} \varphi_\pm \\ \varphi_\pm^2 \end{pmatrix} = \varphi_\pm\begin{pmatrix} 1 \\ \varphi_\pm \end{pmatrix}, \qquad \text{tedy} \quad A^n\begin{pmatrix} 1 \\ \varphi_\pm \end{pmatrix} = \varphi_\pm^n\begin{pmatrix} 1 \\ \varphi_\pm \end{pmatrix}.
$$

Vektory $\vec{x}_\pm = (1; \varphi_\pm)$ jsou [[lineární nezávislost|LN]], takže $\mathcal{X} = (\vec{x}_+, \vec{x}_-)$ je [[báze]] $\mathbb{R}^2$. Každý vektor je jejich kombinace, třeba $(0; 1) = \frac{1}{\sqrt{5}}(\vec{x}_+ - \vec{x}_-)$, a pak

$$
A^n\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{5}}\left(\varphi_+^n\vec{x}_+ - \varphi_-^n\vec{x}_-\right), \qquad a_n = \frac{1}{\sqrt{5}}\left(\varphi_+^n - \varphi_-^n\right),
$$

což je [[Binetův vzorec]]. Maticově: v bázi $\mathcal{X}$ je [[matice lineárního operátoru v bázi|matice operátoru]] diagonální,

$$
[A]^{\mathcal{X}} = \begin{pmatrix} \varphi_+ & 0 \\ 0 & \varphi_- \end{pmatrix}, \qquad [A^n]^{\mathcal{X}} = \left([A]^{\mathcal{X}}\right)^n = \begin{pmatrix} \varphi_+^n & 0 \\ 0 & \varphi_-^n \end{pmatrix},
$$

a s [[matice přechodu|maticí přechodu]] $T = [\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = \begin{pmatrix} 1 & 1 \\ \varphi_+ & \varphi_- \end{pmatrix}$ (ve sloupcích vektory báze) je

$$
A^n = [A^n]^{\mathcal{E}} = [\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}\,[A^n]^{\mathcal{X}}\,[\mathrm{id}]^{\mathcal{E} \to \mathcal{X}} = T\begin{pmatrix} \varphi_+ & 0 \\ 0 & \varphi_- \end{pmatrix}^n T^{-1}.
$$

Totéž bez bází: z $A = TDT^{-1}$ plyne $A^n = TD\underbrace{T^{-1}T}_{E}D\underbrace{T^{-1}T}_{E}D \cdots DT^{-1} = TD^nT^{-1}$.

> [!obrazek] Fibonacciho systém se stáčí k vlastní přímce
> ![[lag16-fibonacci.png]]
> *Modré body jsou stavy $(0; 1)$, $(1; 1)$, $(1; 2)$, $(2; 3)$, $(3; 5)$, $(5; 8)$, šipky jeden krok $A$. Zelená čárkovaná přímka $\operatorname{span}\{(1; \varphi_+)\}$: vektory na ní se jen natáhnou $1{,}618$-krát. Oranžová $\operatorname{span}\{(1; \varphi_-)\}$: vektory na ní se zkrátí a otočí ($\varphi_- \approx -0{,}618$). Složka podél oranžové přímky s každým krokem slábne, proto se stavy přimknou k zelené.*

> [!navic] Stejná matice, jiné pořadí složek
> Minule jsme stav psali jako $(a_{n+1}; a_n)$ s maticí $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ a vlastními vektory $(\varphi_\pm; 1)$. Tady je stav $(a_n; a_{n+1})$, matice $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ a vlastní vektory $(1; \varphi_\pm)$. Jde o tentýž systém, jen s prohozenými souřadnicemi; vlastní čísla $\varphi_\pm$ vyjdou stejná. Indukcí $A^n = \begin{pmatrix} a_{n-1} & a_n \\ a_n & a_{n+1} \end{pmatrix}$, třeba $A^{10} = \begin{pmatrix} 34 & 55 \\ 55 & 89 \end{pmatrix}$.

## §2 Vlastní číslo a vlastní vektor

> [!definice] Definice · pozn. 11.2 ♥
> Buď $L$ lineární prostor nad tělesem $\mathbb{F}$ a $A \in \operatorname{Lin}(L)$ [[lineární operátor]]. Skalár $\lambda \in \mathbb{F}$ se nazývá *vlastní číslo* operátoru $A$, jestliže existuje vektor $\vec{x} \in L$, $\vec{x} \neq \vec{0}$, takový, že
>
> $$
> A\vec{x} = \lambda\vec{x}.
> $$
>
> Tento vektor $\vec{x}$ pak nazýváme *vlastní vektor* příslušný vlastnímu číslu $\lambda$.
>
> Pro matici $A \in \mathbb{F}^{n \times n}$: $\lambda \in \mathbb{F}$ je její vlastní číslo příslušné vlastnímu vektoru $\vec{x} \in \mathbb{F}^n$, $\vec{x} \neq \vec{0}$, jestliže $A\vec{x} = \lambda\vec{x}$.

^def-vlastni-cislo

> [!lidsky] Lidsky
> Vlastní vektor je směr, který operátor **neotočí**, jen ho natáhne, zkrátí, převrátí nebo vynuluje. Vlastní číslo je ten koeficient natažení. Většinu vektorů operátor „stočí“ jinam; vlastní vektory jsou výjimečné směry, ve kterých se chová jako obyčejné násobení číslem.

> [!example] Příklad
> $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$: $A\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 1 \end{pmatrix}$, takže $3$ je vlastní číslo a $(1; 1)$ příslušný vlastní vektor; $(5; 5)$ i $(-2; -2)$ jsou také. Nepříklad: $A\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$ není násobkem $(1; 0)$, takže $(1; 0)$ vlastní vektor není.

> [!pozor] Vektor nenulový, číslo klidně nulové
> Vlastní vektor **musí být nenulový**, jinak by každé $\lambda$ bylo vlastní číslo: $A\vec{0} = \vec{0} = \lambda\vec{0}$ platí vždy. Vlastní **číslo** naopak nulové být smí: $A\vec{x} = 0 \cdot \vec{x}$ s $\vec{x} \neq \vec{0}$ je v pořádku a znamená, že $A$ vektor $\vec{x}$ vynuluje.

### Příklady (pozn. 11.3)

- [[identické zobrazení|Identita]] $\mathrm{id} : V \to V$, $\mathrm{id}(\vec{x}) = \vec{x}$: každé $\vec{x} \neq \vec{0}$ je vlastní vektor příslušný $\lambda = 1$. Jiná vlastní čísla nemá.
- [[nulové zobrazení|Nulový operátor]] $O : V \to V$, $O(\vec{x}) = \vec{0}$: každé $\vec{x} \neq \vec{0}$ je vlastní vektor příslušný $\lambda = 0$. Jiná vlastní čísla nemá.
- Projekce $A : \mathbb{R}^2 \to \mathbb{R}^2$ na osu $x$, $A(x; y) = (x; 0)$: vektory $(x; 0)$, $x \neq 0$, jsou vlastní pro $\lambda = 1$ ($A\vec{v} = \vec{v}$), vektory $(0; y)$, $y \neq 0$, jsou vlastní pro $\lambda = 0$ ($A\vec{w} = \vec{0}$). Jiné vlastní vektory nemá: $(x; y)$ s $x \neq 0 \neq y$ se zobrazí na $(x; 0)$, což není jeho násobek.

> [!obrazek] Vlastní vektory projekce
> ![[lag16-projekce.png]]
> *Modrý $\vec{v}$ na ose $x$ se nezmění ($\lambda = 1$). Oranžový $\vec{w}$ na ose $y$ se zobrazí na nulový vektor ($\lambda = 0$). Červený $\vec{u}$ mimo osy se zobrazí na čárkovaný $A\vec{u}$, který míří jinam, takže vlastní vektor není.*

> [!veta] Pozorování 11.4
> ==Buď $A \in \operatorname{Lin}(L)$.== Vektor $\vec{x} \neq \vec{0}$ je vlastní vektor příslušný $\lambda = 0$, právě když $A\vec{x} = \vec{0}$, tj. $\vec{x} \in \ker A$. Tedy
>
> $$
> \mathbf{0 \text{ je vlastní číslo } A \iff \ker A \neq \{\vec{0}\} \iff A \text{ není prostý.}}
> $$
>
> ==Pro matici $A \in \mathbb{F}^{n \times n}$:== **$0$ je vlastní číslo $A$, právě když $A$ je singulární.**

^veta-nulove-vlastni-cislo

> [!lidsky] Lidsky
> Vlastní vektor k nule je nenulový vektor, který operátor „zabije“. Takový existuje, právě když [[jádro]] není triviální, a to je přesně případ, kdy operátor není [[injektivní zobrazení|prostý]] a matice je [[singulární matice|singulární]] ($\det A = 0$).

> [!example] Příklad
> $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ má $\det = 0$, takže $0$ je její vlastní číslo; vlastní vektor je třeba $(2; -1)$: $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Regulární $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$ vlastní číslo $0$ nemá.

## §3 Jak vlastní čísla a vektory najít

Pro matici $A \in \mathbb{F}^{n \times n}$ řešíme $A\vec{x} = \lambda\vec{x}$. Protože $\lambda\vec{x} = \lambda E\vec{x}$ ([[jednotková matice]]), je to

$$
A\vec{x} = \lambda\vec{x} \iff A\vec{x} - \lambda E\vec{x} = \vec{0} \iff (A - \lambda E)\vec{x} = \vec{0}.
$$

To je [[homogenní soustava]] $n$ rovnic o $n$ neznámých s parametrem $\lambda$. Nenulové řešení má, právě když je její matice $A - \lambda E$ singulární, a podle [[věta o regularitě a determinantu|věty o regularitě a determinantu]]:

$$
\lambda \text{ je vlastní číslo } A \iff A - \lambda E \text{ je singulární} \iff \det(A - \lambda E) = 0.
$$

Postup je tedy dvoukrokový: nejdřív vlastní čísla z rovnice $\det(A - \lambda E) = 0$, pak pro každé z nich vlastní vektory jako nenulová řešení soustavy $(A - \lambda E)\vec{x} = \vec{0}$.

> [!example] Úloha 11.5 · vlastní čísla a vektory $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$
> **Vlastní čísla.**
>
> $$
> A - \lambda E = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix} - \begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix} = \begin{pmatrix} 3 - \lambda & 0 \\ 1 & 2 - \lambda \end{pmatrix}, \qquad 0 = \det(A - \lambda E) = (3 - \lambda)(2 - \lambda) = \lambda^2 - 5\lambda + 6,
> $$
>
> tedy $\lambda = 2$ nebo $\lambda = 3$.
>
> **$\lambda = 2$:** $A - 2E = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, tedy $x_1 = 0$, $x_2$ volné: $\vec{x} \in \operatorname{span}\{(0; 1)\}$. Kontrola: $A(0; 1) = (0; 2) = 2 \cdot (0; 1)$. ✓
>
> **$\lambda = 3$:** $A - 3E = \begin{pmatrix} 0 & 0 \\ 1 & -1 \end{pmatrix} \sim \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$, tedy $x_1 = x_2$: $\vec{x} \in \operatorname{span}\{(1; 1)\}$. Kontrola: $A(1; 1) = (3; 3) = 3 \cdot (1; 1)$. ✓
>
> Vlastní vektory jsou **všechny nenulové** prvky těchto [[lineární obal|obalů]].

> [!obrazek] Co matice dělá s vlastními vektory
> ![[lag16-priklad.png]]
> *Matice $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$. Vlevo: modré vlastní vektory $(0; 1)$ a $(1; 1)$ a jejich oranžové obrazy na týchž zelených přímkách, natažené $2$× a $3$×; červený $(1; 0)$ se zobrazí na čárkovaný $(3; 1)$, který míří jinam. Vpravo: modrá buňka báze $((0; 1), (1; 1))$ a oranžová buňka obrazu: podél $(0; 1)$ se natáhla $2$×, podél $(1; 1)$ $3$×. V této bázi matice jen natahuje osy, tedy je diagonální.*

> [!veta] Věta 11.7
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $A \in \operatorname{Lin}(L)$ a $\lambda \in \mathbb{F}$.== Potom množina
>
> $$
> \{\vec{x} \in L \mid A\vec{x} = \lambda\vec{x}\}
> $$
>
> (vlastní vektory příslušné $\lambda$ doplněné o $\vec{0}$) **je lineární podprostor $L$, a to $\ker(A - \lambda\,\mathrm{id}_L)$.**
>
> > [!note]- Důkaz
> > $(A - \lambda\,\mathrm{id})\vec{x} = A\vec{x} - \lambda\vec{x}$, takže $A\vec{x} = \lambda\vec{x}$ platí, právě když $(A - \lambda\,\mathrm{id})\vec{x} = \vec{0}$. Zobrazení $A - \lambda\,\mathrm{id}$ je lineární (součet lineárních zobrazení) a jádro lineárního zobrazení je podprostor (věta 7.13).

^veta-vlastni-podprostor

> [!lidsky] Lidsky
> Všechny vektory, které $A$ natáhne právě $\lambda$-krát, tvoří spolu s nulou podprostor: součet dvou takových i jejich násobek se natáhne zase $\lambda$-krát. Najdeš ho jako [[jádro]] matice $A - \lambda E$, tedy jako řešení homogenní soustavy.

> [!example] Příklad
> Pro projekci na osu $x$ a $\lambda = 1$ je to celá osa $x$: $\ker\left(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} - E\right) = \ker\begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix} = \operatorname{span}\{(1; 0)\}$. Pro $\lambda = 5$ vyjde $\ker\begin{pmatrix} -4 & 0 \\ 0 & -5 \end{pmatrix} = \{\vec{0}\}$: podprostor existuje vždy, ale jen pro vlastní číslo je netriviální.

> [!definice] Definice · pozn. 11.9
> Buď $L$ lineární prostor nad $\mathbb{F}$, $A \in \operatorname{Lin}(L)$ a $\lambda \in \mathbb{F}$ vlastní číslo $A$. Lineární podprostor
>
> $$
> \{\vec{x} \in L \mid A\vec{x} = \lambda\vec{x}\} = \ker(A - \lambda\,\mathrm{id}_L)
> $$
>
> se nazývá *vlastní podprostor* příslušný vlastnímu číslu $\lambda$. Jeho [[dimenze]] se nazývá *geometrická násobnost* vlastního čísla $\lambda$.

^def-vlastni-podprostor

> [!lidsky] Lidsky
> Vlastní podprostor je „přihrádka“ všech směrů, které $A$ natahuje stejným číslem $\lambda$, i s nulou. Geometrická násobnost říká, kolik nezávislých takových směrů je: $1$ znamená přímku, $2$ rovinu.

> [!example] Příklad
> U $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$ jsou vlastní podprostory $\operatorname{span}\{(0; 1)\}$ pro $\lambda = 2$ a $\operatorname{span}\{(1; 1)\}$ pro $\lambda = 3$, obě geometrické násobnosti jsou $1$. U identity na $\mathbb{R}^2$ je vlastní podprostor pro $\lambda = 1$ celé $\mathbb{R}^2$, geometrická násobnost $2$.

## §4 Kořeny polynomů

Rovnice $\det(A - \lambda E) = 0$ je polynomiální. Připomeňme, co víme o kořenech (pozn. 11.12). [[polynom|Polynom]] $p(x) \in \mathbb{F}[x]$ je výraz; za proměnnou $x$ jde dosadit číslo $\alpha \in \mathbb{F}$ a vyjde číslo $p(\alpha) \in \mathbb{F}$.

> [!definice] Definice · pozn. 11.12
> Buď $p(x) \in \mathbb{F}[x]$. Číslo $\alpha \in \mathbb{F}$ je *kořen* polynomu $p(x)$, jestliže $p(\alpha) = 0$. To nastane, právě když $p(x) = (x - \alpha)q(x)$ pro nějaký polynom $q(x) \in \mathbb{F}[x]$ (polynom jde beze zbytku vydělit kořenovým činitelem $x - \alpha$).
>
> Kořen $\alpha$ má *násobnost* $k \in \mathbb{N}$, jestliže
>
> $$
> p(x) = (x - \alpha)^k q(x), \qquad q(\alpha) \neq 0.
> $$

^def-koren

> [!lidsky] Lidsky
> Kořen je číslo, pro které polynom vyjde nula; graf tam protne (nebo se dotkne) osy $x$. [[násobnost kořene|Násobnost]] říká, kolikrát jde z polynomu „vytknout“ závorku $(x - \alpha)$, než kořen zmizí. Dvojnásobný kořen je místo, kde se graf osy jen dotkne.

> [!example] Příklad
> $p(x) = x^3 - 3x - 2 = (x - 2)(x + 1)^2$: kořen $2$ má násobnost $1$, kořen $-1$ násobnost $2$, protože po vytknutí $(x + 1)^2$ zbude $q(x) = x - 2$ a $q(-1) = -3 \neq 0$. Nepříklad: $3$ kořen není, $p(3) = 27 - 9 - 2 = 16$.

> [!veta] Pozn. 11.12 · Počet kořenů
> ==Buď $p(x) \in \mathbb{F}[x]$ nenulový polynom stupně $n$.== Potom **$p$ má nejvýše $n$ kořenů, i když každý počítáme tolikrát, kolik je jeho násobnost.**
>
> > [!note]- Zdůvodnění
> > Má-li $p$ kořeny $\alpha_1, \dots, \alpha_l$ s násobnostmi $k_1, \dots, k_l$, opakovaným vytýkáním dostaneme $p(x) = (x - \alpha_1)^{k_1} \cdots (x - \alpha_l)^{k_l}q(x)$ s nenulovým $q$. Porovnáním stupňů $n = k_1 + \cdots + k_l + \deg q \ge k_1 + \cdots + k_l$.

^veta-pocet-korenu

> [!lidsky] Lidsky
> Každý kořen „spotřebuje“ aspoň jeden stupeň polynomu, protože z něj musíš vytknout závorku $(x - \alpha)$. Kvadratická rovnice má proto nejvýš dva kořeny, kubická tři. Kořenů může být i méně, nad $\mathbb{R}$ třeba žádný.

> [!example] Příklad
> $x^2 - 5x + 6 = (x - 2)(x - 3)$ má dva kořeny, $(x - 2)^2$ jeden dvojnásobný (počítá se dvakrát), $x^2 + 1$ nad $\mathbb{R}$ žádný.

> [!navic] Základní věta algebry (pozn. 11.12)
> [[základní věta algebry|Základní věta algebry]] (znáš ji z MA1) říká, že každý polynom $p(x) \in \mathbb{C}[x]$ stupně $n \ge 1$ má v $\mathbb{C}$ kořen. Opakovaným vytýkáním se pak rozloží na součin kořenových činitelů
>
> $$
> p(x) = \alpha(x - \alpha_1)(x - \alpha_2) \cdots (x - \alpha_n), \qquad \alpha, \alpha_1, \dots, \alpha_n \in \mathbb{C},
> $$
>
> takže **nad $\mathbb{C}$ má každý polynom stupně $n$ právě $n$ kořenů**, počítáme-li je s násobnostmi. Důkaz se zde neuvádí, potřebuje matematickou analýzu.

> [!example] Příklad
> $x^2 + 1 = (x - \mathrm{i})(x + \mathrm{i})$, kořeny $\pm\mathrm{i}$. $x^3 - 1 = (x - 1)(x^2 + x + 1)$ má jeden reálný kořen $1$ a dva komplexní $-\frac{1}{2} \pm \frac{\sqrt{3}}{2}\mathrm{i}$. V reálných číslech rozklad až do konce nejde, proto u reálných matic může vlastní číslo chybět.

## §5 Charakteristický polynom

> [!veta] Pozorování 11.10
> ==Buď $A \in \mathbb{F}^{n \times n}$.== Potom **$\det(A - \lambda E)$ je polynom v proměnné $\lambda$ s koeficienty v $\mathbb{F}$ stupně $n$**, a **$\lambda \in \mathbb{F}$ je vlastní číslo $A$, právě když je kořenem tohoto polynomu.**
>
> > [!note]- Zdůvodnění
> > Podle definice [[determinant|determinantu]] je $\det(A - \lambda E)$ součet $n!$ součinů, každý z $n$ prvků matice $A - \lambda E$. Prvky na diagonále jsou $a_{ii} - \lambda$, ostatní neobsahují $\lambda$; každý součin je tedy polynom v $\lambda$ stupně nejvýš $n$. Stupně $n$ dosáhne jen součin celé diagonály (identická permutace) $(a_{11} - \lambda) \cdots (a_{nn} - \lambda)$, jehož vedoucí člen $(-1)^n\lambda^n$ se ničím nezruší. Druhá část je odvození z §3.

^veta-vlastni-cisla-koreny

> [!lidsky] Lidsky
> Hledání vlastních čísel se převede na hledání kořenů jednoho polynomu: z matice $A - \lambda E$ spočítáš determinant jako výraz s $\lambda$ a položíš ho rovný nule. Matice $2 \times 2$ dá kvadratickou rovnici, $3 \times 3$ kubickou.

> [!example] Příklad
> $\det\begin{pmatrix} 3 - \lambda & 0 \\ 1 & 2 - \lambda \end{pmatrix} = \lambda^2 - 5\lambda + 6$, kořeny $2$ a $3$ = vlastní čísla. Pro $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$: $(4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 2)(\lambda - 5)$, vlastní čísla $2$ a $5$.

> [!definice] Definice · pozn. 11.11 ♥
> Pro matici $A \in \mathbb{F}^{n \times n}$ nazýváme polynom
>
> $$
> p_A(x) = \det(A - xE) \in \mathbb{F}[x]
> $$
>
> *charakteristický polynom* matice $A$. Je-li $\lambda \in \mathbb{F}$ kořen $p_A$, nazýváme jeho násobnost jakožto kořene $p_A$ *algebraická násobnost* vlastního čísla $\lambda$.

^def-charakteristicky-polynom

> [!lidsky] Lidsky
> Charakteristický polynom je determinant matice, od jejíž diagonály odečteš neznámou. Jeho kořeny jsou přesně vlastní čísla. Algebraická násobnost říká, kolikrát se vlastní číslo v rozkladu polynomu opakuje; geometrická (§3), kolik nezávislých vlastních vektorů k němu je. Ty dvě se nemusí rovnat.

> [!example] Příklad
> $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$: $p_A(x) = (2 - x)^2$, vlastní číslo $2$ má algebraickou násobnost $2$. Vlastní vektory: $A - 2E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, tedy $x_2 = 0$ a vlastní podprostor je jen $\operatorname{span}\{(1; 0)\}$, geometrická násobnost $1$. Naproti tomu $2E_2$ má tentýž $p(x) = (2 - x)^2$ a geometrickou násobnost $2$.

> [!navic] Charakteristický polynom operátoru (pozn. 11.13) a jiné znaménko
> Pro operátor $A \in \operatorname{Lin}(L)$ na prostoru konečné dimenze se definuje $p_A(x) = \det(A - x\,\mathrm{id}) = \det([A]^{\mathcal{X}} - xE)$ v libovolné bázi $\mathcal{X}$; na volbě báze nezáleží, stejně jako u [[determinant lineárního operátoru|determinantu operátoru]] (věta o podobných maticích v §6). Některé učebnice berou $\det(xE - A) = (-1)^n p_A(x)$: liší se nanejvýš znaménkem, kořeny i násobnosti jsou stejné.

> [!navic] Geometrická násobnost nepřeroste algebraickou (věta 11.30\*)
> Pro každé vlastní číslo platí $1 \le$ geometrická násobnost $\le$ algebraická násobnost. Matice $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ ukazuje, že nerovnost může být ostrá.

### Řádkové úpravy vlastní čísla mění

U [[horní trojúhelníková matice|horní trojúhelníkové matice]] je $A - \lambda E$ také trojúhelníková, takže $p_A(\lambda) = (a_{11} - \lambda) \cdots (a_{nn} - \lambda)$ a **vlastní čísla stojí na diagonále** (pozn. 11.19). Nabízí se tedy matici [[Gaussova eliminace|eliminací]] převést na trojúhelníkový tvar a vlastní čísla odečíst. To nejde.

> [!pozor] Eliminace vlastní čísla nezachovává
> $A = \begin{pmatrix} 1 & -3 \\ 4 & -6 \end{pmatrix}$ má $p_A(\lambda) = (1 - \lambda)(-6 - \lambda) + 12 = \lambda^2 + 5\lambda + 6 = (\lambda + 2)(\lambda + 3)$, vlastní čísla $-2$ a $-3$. Po úpravě $r_2 - 4r_1$ vyjde $\begin{pmatrix} 1 & -3 \\ 0 & 6 \end{pmatrix}$ s vlastními čísly $1$ a $6$. Důvod: řádkové úpravy dají $B = TA$ ([[matice elementární řádkové úpravy]]), kdežto vlastní čísla zachovává jen $B = T^{-1}AT$ (§6), tedy každá řádková úprava by musela mít „protiúpravu“ ve sloupcích. Navíc Gaussova–Jordanova eliminace převede každou regulární matici na $E$, a ta má jediné vlastní číslo $1$.

## §6 Podobné matice

> [!definice] Definice · pozn. 11.14 ♥
> Matice $A, B \in \mathbb{F}^{n \times n}$ se nazývají *podobné*, jestliže existuje [[regulární matice]] $T \in \mathbb{F}^{n \times n}$ taková, že
>
> $$
> B = T^{-1}AT.
> $$

^def-podobne-matice

> [!lidsky] Lidsky
> Podobné matice popisují **tentýž operátor, jen v jiné bázi**. $T$ je překladová tabulka mezi bázemi: vektor přeložíš do „staré“ báze ($T$), provedeš $A$ a výsledek přeložíš zpátky ($T^{-1}$).

> [!example] Příklad
> $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$ a $T = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ (ve sloupcích vlastní vektory), $T^{-1} = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}$:
>
> $$
> T^{-1}AT = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix},
> $$
>
> takže $A$ je podobná $\operatorname{diag}(2, 3)$. Nepříklad: $2E_2$ je podobná jen sama sobě, protože $T^{-1}(2E)T = 2T^{-1}T = 2E$.

**Proč „tentýž operátor“ (pozn. 11.15).** Matici $A \in \mathbb{F}^{n \times n}$ odpovídá operátor $A : \mathbb{F}^n \to \mathbb{F}^n$, $A\vec{x} = A\vec{x}$, s maticí $[A]^{\mathcal{E}} = A$ v [[kanonická báze|kanonické bázi]]. Regulární $T = (\vec{x}_1 \cdots \vec{x}_n)$ má LN sloupce, takže $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ je báze $\mathbb{F}^n$ a $T = [\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$, $T^{-1} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$. Podle [[věta o transformaci souřadnic|transformace souřadnic]]

$$
B = T^{-1}AT = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}\,[A]^{\mathcal{E}}\,[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = [A]^{\mathcal{X}}.
$$

> [!veta] Věta 11.16
> ==Buďte $A, B \in \mathbb{F}^{n \times n}$ podobné.== Potom **mají stejný charakteristický polynom, a tedy i stejná vlastní čísla** (se stejnými algebraickými násobnostmi).
>
> > [!note]- Důkaz
> > Je-li $B = T^{-1}AT$, pak díky $E = T^{-1}T = T^{-1}ET$ a [[věta o determinantu součinu|větě o determinantu součinu]]:
> >
> > $$
> > \det(B - \lambda E) = \det(T^{-1}AT - \lambda T^{-1}ET) = \det\big(T^{-1}(A - \lambda E)T\big) = \det T^{-1} \cdot \det(A - \lambda E) \cdot \det T = \det(A - \lambda E),
> > $$
> >
> > protože $\det T^{-1} \cdot \det T = 1$ ([[determinant inverzní matice]]).

^veta-podobne-matice

> [!lidsky] Lidsky
> Vlastní čísla patří operátoru, ne jeho zápisu. Když změníš bázi, matice se změní, ale směry, které operátor natahuje, a koeficienty natažení zůstanou. Je to stejný trik jako u [[determinant lineárního operátoru|determinantu operátoru]]: přechodové matice se vykrátí.

> [!example] Příklad
> $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$ a podobná $\operatorname{diag}(2, 3)$ mají obě $p(\lambda) = (2 - \lambda)(3 - \lambda)$. Kontrolou stopy a determinantu: obě mají součet diagonály $5$ a determinant $6$.

> [!pozor] Obrácení neplatí (pozn. 11.18)
> Stejný charakteristický polynom podobnost nezaručí. $O_2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ a $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ mají obě $p(\lambda) = \lambda^2$, ale podobné nejsou: $T^{-1}O_2T = O_2 \neq N$ pro každé $T$.

## §7 Diagonalizace

Připomenutí: matice je [[diagonální matice|diagonální]], jestliže $a_{ij} = 0$ pro $i \neq j$ (pozn. 11.20). Pro operátor $A : L \to L$ s $[A]^{\mathcal{X}} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ je pak $[A^k]^{\mathcal{X}} = ([A]^{\mathcal{X}})^k = \operatorname{diag}(\lambda_1^k, \dots, \lambda_n^k)$.

> [!definice] Definice · pozn. 11.21 ♥
> Buď $L$ lineární prostor nad $\mathbb{F}$, $\dim L < \infty$. Lineární operátor $A \in \operatorname{Lin}(L)$ je *diagonalizovatelný*, jestliže existuje báze $\mathcal{X}$ prostoru $L$ taková, že $[A]^{\mathcal{X}}$ je diagonální.

^def-diagonalizovatelny

> [!lidsky] Lidsky
> Operátor je diagonalizovatelný, když si umíš zvolit souřadnicové osy tak, aby podél každé jen natahoval svým číslem a nic nemíchal. V takové bázi se s ním počítá stejně snadno jako s násobením čísly.

> [!example] Příklad
> Fibonacciho operátor $A(x; y) = (y; x + y)$ je diagonalizovatelný: v bázi $\mathcal{X} = ((1; \varphi_+), (1; \varphi_-))$ je $[A]^{\mathcal{X}} = \operatorname{diag}(\varphi_+, \varphi_-)$. Nepříklad: [[operátor derivace|derivace]] na $\mathbb{R}^{\le 1}[x]$ (v bázi $(1, x)$ matice $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$) diagonalizovatelná není, má jen vlastní čísla $0$ a vlastní vektory jen konstanty.

> [!definice] Definice · pozn. 11.23
> Matice $A \in \mathbb{F}^{n \times n}$ je *diagonalizovatelná*, jestliže je diagonalizovatelný operátor $A : \mathbb{F}^n \to \mathbb{F}^n$, $A\vec{x} = A\vec{x}$. Ekvivalentně:
>
> $$
> \begin{aligned}
> A \text{ je diagonalizovatelná} &\iff \exists\, \mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n) \text{ báze } \mathbb{F}^n \text{ taková, že } [A]^{\mathcal{X}} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}A\,[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} \text{ je diagonální} \\
> &\iff \exists\, T \in \mathbb{F}^{n \times n} \text{ regulární taková, že } T^{-1}AT \text{ je diagonální} \\
> &\iff A \text{ je podobná diagonální matici.}
> \end{aligned}
> $$
>
> Pak $D = T^{-1}AT$, neboli $A = TDT^{-1}$, kde $T$ má ve sloupcích bázi z vlastních vektorů a $D$ na diagonále příslušná vlastní čísla.

^def-diagonalizovatelna-matice

> [!lidsky] Lidsky
> Diagonalizovat matici znamená rozložit ji na tři kroky: $T^{-1}$ přepočítá vektor do souřadnic vůči vlastním vektorům, $D$ v nich natáhne každou souřadnici svým vlastním číslem a $T$ výsledek přepočítá zpět.

> [!example] Příklad
> $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}$. Nepříklad: $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ diagonalizovatelná není, vlastní vektory tvoří jen přímku $\operatorname{span}\{(1; 0)\}$ a báze $\mathbb{R}^2$ z nich nejde poskládat.

> [!veta] Věta 11.22
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $\dim L < \infty$, $A \in \operatorname{Lin}(L)$.== Potom **$A$ je diagonalizovatelný, právě když v $L$ existuje báze tvořená vlastními vektory $A$.**
>
> > [!note]- Důkaz
> > ($\Leftarrow$) Nechť $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$ je báze s $A\vec{x}_i = \lambda_i\vec{x}_i$. $i$-tý sloupec $[A]^{\mathcal{X}}$ je $[A\vec{x}_i]^{\mathcal{X}} = [\lambda_i\vec{x}_i]^{\mathcal{X}} = \lambda_i\vec{e}_i$, tedy $[A]^{\mathcal{X}} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.
> >
> > ($\Rightarrow$) Nechť $[A]^{\mathcal{X}} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ pro bázi $\mathcal{X} = (\vec{x}_1, \dots, \vec{x}_n)$. Pak $[A\vec{x}_i]^{\mathcal{X}}$ je $i$-tý sloupec, tedy $(0; \dots; \lambda_i; \dots; 0) = \lambda_i\vec{e}_i$, což znamená
> >
> > $$
> > A\vec{x}_i = 0\vec{x}_1 + \cdots + 0\vec{x}_{i-1} + \lambda_i\vec{x}_i + 0\vec{x}_{i+1} + \cdots + 0\vec{x}_n = \lambda_i\vec{x}_i.
> > $$
> >
> > Vektory báze jsou nenulové, takže každý $\vec{x}_i$ je vlastní vektor.

^veta-diagonalizovatelnost

> [!lidsky] Lidsky
> Diagonální matice v bázi $\mathcal{X}$ znamená přesně tohle: $A$ pošle každý bázový vektor na jeho násobek. To je definice vlastního vektoru. Diagonalizovat tedy znamená najít dost (tolik, kolik je dimenze) nezávislých vlastních vektorů.

> [!example] Příklad
> $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ má vlastní čísla $2$ a $5$ s vlastními vektory $(1; -2)$ a $(1; 1)$. Ty jsou LN, tvoří bázi, takže $A = TDT^{-1}$ s $T = \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix}$, $D = \operatorname{diag}(2, 5)$. Pak $A^n = T\operatorname{diag}(2^n, 5^n)T^{-1}$, třeba $A^3 = \begin{pmatrix} 86 & 39 \\ 78 & 47 \end{pmatrix}$.

> [!pozor] Pořadí sloupců $T$ a diagonály $D$ musí sedět
> $i$-tý sloupec $T$ je vlastní vektor k **$i$-tému** číslu na diagonále $D$. Prohodíš-li sloupce $T$, musíš prohodit i čísla v $D$. A $A = TDT^{-1}$, ne $T^{-1}DT$: matice s vlastními vektory ve sloupcích stojí **vlevo** od $D$.

**Mocniny.** Z $A = TDT^{-1}$ plyne $A^k = TD^kT^{-1}$, protože vnitřní $T^{-1}T$ se vykrátí. Pro $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$:

$$
A^k = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 2^k & 0 \\ 0 & 3^k \end{pmatrix}\begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3^k & 0 \\ 3^k - 2^k & 2^k \end{pmatrix},
$$

třeba $A^4 = \begin{pmatrix} 81 & 0 \\ 65 & 16 \end{pmatrix}$.

## §8 Otočení o 90°: vlastní čísla nad $\mathbb{C}$

Naivní plán „$p_A$ má stupeň $n$, tedy $n$ kořenů, ke každému vlastní vektor, a ty dají bázi“ má díry. První: polynom stupně $n$ má $n$ kořenů jen nad $\mathbb{C}$ ([[základní věta algebry]]), nad $\mathbb{R}$ obecně ne.

> [!example] Příklad 11.24 · otočení o $90°$
> $A : \mathbb{R}^2 \to \mathbb{R}^2$, $A(x; y) = (-y; x)$, [[matice otočení|matice]] $[A]^{\mathcal{E}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Žádný nenulový vektor nezůstane na své přímce, tedy čekáme, že vlastní vektory nejsou:
>
> $$
> p_A(\lambda) = \begin{vmatrix} -\lambda & -1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 + 1,
> $$
>
> a to nad $\mathbb{R}$ nemá kořen. **Nad $\mathbb{R}$ nemá $A$ žádné vlastní číslo** a diagonalizovatelná není.
>
> Táž matice ale leží i v $\mathbb{C}^{2 \times 2}$ ($\mathbb{R} \subseteq \mathbb{C}$). Nad $\mathbb{C}$ je $\lambda = \pm\mathrm{i}$ a
>
> $$
> \lambda = \pm\mathrm{i}: \quad A - \lambda E = \begin{pmatrix} \mp\mathrm{i} & -1 \\ 1 & \mp\mathrm{i} \end{pmatrix} \sim \begin{pmatrix} \mp\mathrm{i} & -1 \\ 0 & 0 \end{pmatrix}, \qquad \vec{x} \in \operatorname{span}\left\{\begin{pmatrix} \pm\mathrm{i} \\ 1 \end{pmatrix}\right\}
> $$
>
> (druhý řádek je $\pm\mathrm{i}$-násobek prvního). Kontrola pro $+\mathrm{i}$: $A(\mathrm{i}; 1) = (-1; \mathrm{i}) = \mathrm{i}(\mathrm{i}; 1)$. ✓ Vektory $(\mathrm{i}; 1)$, $(-\mathrm{i}; 1)$ jsou LN, tvoří bázi $\mathbb{C}^2$ a
>
> $$
> A = TDT^{-1}, \qquad T = \begin{pmatrix} \mathrm{i} & -\mathrm{i} \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} \mathrm{i} & 0 \\ 0 & -\mathrm{i} \end{pmatrix}, \quad T^{-1} = \frac{1}{2}\begin{pmatrix} -\mathrm{i} & 1 \\ \mathrm{i} & 1 \end{pmatrix}.
> $$

> [!obrazek] Otočení nemá reálný vlastní vektor
> ![[lag16-otoceni.png]]
> *Tři vektory (modrý, zelený, červený, plné šipky) a jejich obrazy při otočení o $90°$ (čárkované šipky téže barvy). Každý obraz leží kolmo na tečkovanou přímku původního vektoru, žádný na ní nezůstane.*

Výsledek nad $\mathbb{C}$ je prakticky stejně dobrý jako nad $\mathbb{R}$. Třeba $A^{1000}$: protože $\mathrm{i}^{1000} = (\mathrm{i}^4)^{250} = 1$ a $(-\mathrm{i})^{1000} = 1$,

$$
A^{1000} = TD^{1000}T^{-1} = T\begin{pmatrix} \mathrm{i}^{1000} & 0 \\ 0 & (-\mathrm{i})^{1000} \end{pmatrix}T^{-1} = TET^{-1} = E,
$$

což sedí s geometrií: čtyři otočení o $90°$ dají identitu a $1000 = 4 \cdot 250$.

> [!navic] Komplexní kořeny reálných matic chodí v párech (cvičení 11.25)
> Je-li $\alpha = a + b\mathrm{i}$ kořen polynomu s reálnými koeficienty, je kořenem i $\bar{\alpha} = a - b\mathrm{i}$. A je-li $\vec{x}$ vlastní vektor reálné matice k $\lambda$, je $\bar{\vec{x}}$ (komplexně sdružené složky) vlastní vektor k $\bar{\lambda}$. U otočení: $\pm\mathrm{i}$ a $(\pm\mathrm{i}; 1)$.

> [!navic] Druhá díra v naivním plánu
> I když kořenů je dost, nemusí být vlastních vektorů dost na bázi: $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ má dvojnásobné vlastní číslo $2$, ale vlastní vektory jen na jedné přímce. Kdy vlastní vektory bázi dají, řeší další část kapitoly (věta 11.26 a důsledek 11.29: $n$ různých vlastních čísel stačí).

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč musí být vlastní vektor nenulový, když vlastní číslo nulové být smí?
> Pro $\vec{x} = \vec{0}$ platí $A\vec{0} = \vec{0} = \lambda\vec{0}$ pro **každé** $\lambda$, takže by každé číslo bylo vlastní a pojem by nic neříkal. Vlastní číslo $0$ je naopak smysluplné: $A\vec{x} = \vec{0}$ pro $\vec{x} \neq \vec{0}$ znamená, že $A$ **vynuluje nějaký nenulový vektor**.

> [!karta|02]- Kdy má čtvercová matice vlastní číslo $0$? Zdůvodni.
> Právě když je **singulární**. $0$ je vlastní číslo $\Leftrightarrow$ existuje $\vec{x} \neq \vec{0}$ s $A\vec{x} = 0\vec{x} = \vec{0}$ $\Leftrightarrow$ $\ker A \neq \{\vec{0}\}$ $\Leftrightarrow$ $A$ není prostá $\Leftrightarrow$ $\det A = 0$.

> [!karta|03]- Proč je $\lambda$ vlastní číslo matice $A$, právě když $\det(A - \lambda E) = 0$?
> $A\vec{x} = \lambda\vec{x} \Leftrightarrow (A - \lambda E)\vec{x} = \vec{0}$. Tato **homogenní soustava** má nenulové řešení, právě když je $A - \lambda E$ **singulární**, a to je právě když $\det(A - \lambda E) = 0$ (věta o regularitě a determinantu).

> [!karta|04]- Dokaž, že vlastní vektory příslušné $\lambda$ spolu s nulovým vektorem tvoří podprostor.
> $\{\vec{x} \mid A\vec{x} = \lambda\vec{x}\} = \{\vec{x} \mid (A - \lambda\,\mathrm{id})\vec{x} = \vec{0}\} = $ **$\ker(A - \lambda\,\mathrm{id})$**, protože $(A - \lambda\,\mathrm{id})\vec{x} = A\vec{x} - \lambda\vec{x}$. $A - \lambda\,\mathrm{id}$ je lineární a **jádro lineárního zobrazení je podprostor**.

> [!karta|05]- Proč je $\det(A - \lambda E)$ pro $A \in \mathbb{F}^{n \times n}$ polynom v $\lambda$ stupně právě $n$?
> Determinant je součet součinů $n$ prvků, z každého řádku a sloupce jednoho. $\lambda$ je jen na diagonále ($a_{ii} - \lambda$), takže každý součin je polynom stupně $\le n$. Stupeň $n$ má **jen součin celé diagonály** $(a_{11} - \lambda) \cdots (a_{nn} - \lambda)$ s vedoucím členem **$(-1)^n\lambda^n$**, který se ničím nezruší.

> [!karta|06]- Proč má matice $n \times n$ nejvýše $n$ vlastních čísel a kolik jich má nad $\mathbb{C}$?
> Vlastní čísla jsou kořeny $p_A$, polynomu **stupně $n$**, a ten má nejvýše $n$ kořenů i s násobnostmi (každý kořen vytkne závorku $(x - \alpha)$). Nad $\mathbb{C}$ podle **základní věty algebry** právě $n$, počítáno s algebraickými násobnostmi; nad $\mathbb{R}$ může být i žádné.

> [!karta|07]- Proč nejdou vlastní čísla počítat Gaussovou eliminací?
> Řádkové úpravy dají $B = TA$, kdežto vlastní čísla zachovává jen **podobnost** $B = T^{-1}AT$. Protipříklad: $\begin{pmatrix} 1 & -3 \\ 4 & -6 \end{pmatrix}$ má vlastní čísla $-2$, $-3$, po $r_2 - 4r_1$ vyjde $\begin{pmatrix} 1 & -3 \\ 0 & 6 \end{pmatrix}$ s vlastními čísly $1$, $6$. A eliminace převede každou regulární matici na $E$ s jediným vlastním číslem $1$.

> [!karta|08]- Jaká vlastní čísla má horní trojúhelníková matice a proč?
> **Čísla na diagonále.** $A - \lambda E$ je také horní trojúhelníková, její determinant je součin diagonály: $p_A(\lambda) = (a_{11} - \lambda) \cdots (a_{nn} - \lambda)$, a ten má kořeny přesně $a_{11}, \dots, a_{nn}$.

> [!karta|09]- Dokaž, že podobné matice mají stejný charakteristický polynom.
> $B = T^{-1}AT$ a $E = T^{-1}ET$, takže $B - \lambda E = T^{-1}(A - \lambda E)T$. **Determinant součinu**: $\det(B - \lambda E) = \det T^{-1} \cdot \det(A - \lambda E) \cdot \det T = \det(A - \lambda E)$, protože $\det T^{-1}\det T = 1$.

> [!karta|10]- Plyne ze stejného charakteristického polynomu, že jsou dvě matice podobné?
> **Ne.** $O_2$ a $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ mají obě $p(\lambda) = \lambda^2$, ale $T^{-1}O_2T = O_2$ pro každé regulární $T$, takže nulovou matici nikdy nepřevedeš na $N$.

> [!karta|11]- Proč popisují podobné matice $A$ a $B = T^{-1}AT$ tentýž operátor? Co je $T$?
> Sloupce regulární $T$ tvoří bázi $\mathcal{X}$ prostoru $\mathbb{F}^n$ a $T = $ **$[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}}$**, $T^{-1} = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}$. Pak $B = [\mathrm{id}]^{\mathcal{E} \to \mathcal{X}}[A]^{\mathcal{E}}[\mathrm{id}]^{\mathcal{X} \to \mathcal{E}} = $ **$[A]^{\mathcal{X}}$**: matice operátoru $\vec{x} \mapsto A\vec{x}$ v bázi $\mathcal{X}$.

> [!karta|12]- Dokaž, že operátor je diagonalizovatelný, právě když existuje báze z jeho vlastních vektorů.
> $i$-tý sloupec $[A]^{\mathcal{X}}$ je $[A\vec{x}_i]^{\mathcal{X}}$. ($\Leftarrow$) $A\vec{x}_i = \lambda_i\vec{x}_i$ dá sloupec $\lambda_i\vec{e}_i$, matice je **diagonální**. ($\Rightarrow$) Je-li $i$-tý sloupec $\lambda_i\vec{e}_i$, je $A\vec{x}_i = \lambda_i\vec{x}_i$ a $\vec{x}_i \neq \vec{0}$ (vektor báze), tedy **vlastní vektor**.

> [!karta|13]- Co stojí ve sloupcích $T$ a na diagonále $D$ v rozkladu $A = TDT^{-1}$?
> Ve sloupcích $T$ je **báze z vlastních vektorů** $\vec{x}_1, \dots, \vec{x}_n$, na diagonále $D$ **příslušná vlastní čísla ve stejném pořadí**: $i$-tý sloupec $T$ patří k $d_{ii}$. Kontrola: $AT = TD$ říká po sloupcích $A\vec{x}_i = d_{ii}\vec{x}_i$.

> [!karta|14]- Proč platí $A^k = TD^kT^{-1}$ a k čemu to je?
> $A^k = (TDT^{-1})(TDT^{-1}) \cdots (TDT^{-1})$ a **vnitřní $T^{-1}T = E$ se vykrátí**. $D^k$ se počítá **po prvcích**, takže místo $k$ násobení matic stačí umocnit čísla. Tak vyjde třeba vzorec pro Fibonacciho čísla z $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$.

> [!karta|15]- Proč otočení o $90°$ v $\mathbb{R}^2$ nemá vlastní čísla a jak se dá přesto diagonalizovat?
> $p_A(\lambda) = \lambda^2 + 1$ nemá **reálný kořen**; geometricky žádný nenulový vektor nezůstane na své přímce. Nad **$\mathbb{C}$** má kořeny $\pm\mathrm{i}$ s vlastními vektory $(\pm\mathrm{i}; 1)$, které tvoří bázi $\mathbb{C}^2$, takže $A = TDT^{-1}$ s $D = \operatorname{diag}(\mathrm{i}, -\mathrm{i})$ a třeba $A^{1000} = TD^{1000}T^{-1} = E$.

> [!karta|16]- Čím se liší algebraická a geometrická násobnost vlastního čísla? Uveď příklad, kdy se liší.
> **Algebraická** = násobnost $\lambda$ jako kořene $p_A$. **Geometrická** = $\dim\ker(A - \lambda\,\mathrm{id})$, počet nezávislých vlastních vektorů. Pro $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ je $p_N(\lambda) = \lambda^2$ (algebraická $2$), ale $\ker N = \operatorname{span}\{(1; 0)\}$ (geometrická $1$). Vždy platí geometrická $\le$ algebraická.

### Příklady na procvičení

> [!priklad|17]- Najdi vlastní čísla a vlastní vektory matice $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$.
> $p_A(\lambda) = (4 - \lambda)(3 - \lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda - 2)(\lambda - 5)$. **$\lambda = 2$:** $A - 2E = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$, $2x_1 + x_2 = 0$, **$\operatorname{span}\{(1; -2)\}$**. **$\lambda = 5$:** $A - 5E = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$, $x_1 = x_2$, **$\operatorname{span}\{(1; 1)\}$**. Kontrola: $A(1; -2) = (2; -4)$, $A(1; 1) = (5; 5)$.

> [!priklad|18]- Diagonalizuj $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$: najdi regulární $T$ a diagonální $D$ s $A = TDT^{-1}$.
> Vlastní vektory $(1; -2)$ k $2$ a $(1; 1)$ k $5$ jsou LN. **$T = \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix}$, $D = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$**, $\det T = 3$, $T^{-1} = \frac{1}{3}\begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}$. Kontrola: $TD = \begin{pmatrix} 2 & 5 \\ -4 & 5 \end{pmatrix}$ a $TD \cdot T^{-1} = \frac{1}{3}\begin{pmatrix} 12 & 3 \\ 6 & 9 \end{pmatrix} = A$.

> [!priklad|19]- Pomocí diagonalizace spočítej $A^n$ pro $A = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$.
> Vlastní vektory $(0; 1)$ k $2$ a $(1; 1)$ k $3$: $T = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, $D = \operatorname{diag}(2, 3)$, $T^{-1} = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}$. $A^n = TD^nT^{-1} = \begin{pmatrix} 0 & 3^n \\ 2^n & 3^n \end{pmatrix}\begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix} = $ **$\begin{pmatrix} 3^n & 0 \\ 3^n - 2^n & 2^n \end{pmatrix}$**. Kontrola $n = 1$: $\begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$ ✓.

> [!priklad|20]- Najdi vlastní čísla a vlastní vektory zrcadlení $A(x; y) = (y; x)$ podle přímky $y = x$.
> $[A]^{\mathcal{E}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $p_A(\lambda) = \lambda^2 - 1$. **$\lambda = 1$:** $\operatorname{span}\{(1; 1)\}$ (přímka zrcadlení se nehne). **$\lambda = -1$:** $\operatorname{span}\{(1; -1)\}$ (kolmý směr se převrátí). Ty dva vektory tvoří bázi, v ní $[A] = \operatorname{diag}(1, -1)$.

> [!priklad|21]- Najdi vlastní čísla a vlastní vektory matice $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ Fibonacciho systému.
> $p_A(\lambda) = -\lambda(1 - \lambda) - 1 = \lambda^2 - \lambda - 1$, **$\lambda = \varphi_\pm = \frac{1 \pm \sqrt{5}}{2}$**. $A - \varphi E = \begin{pmatrix} -\varphi & 1 \\ 1 & 1 - \varphi \end{pmatrix}$, první řádek dá $y = \varphi x$ (druhý je jeho násobek, protože $\det = 0$). Vlastní vektory **$\operatorname{span}\{(1; \varphi_\pm)\}$**.

> [!priklad|22]- Urči algebraickou a geometrickou násobnost vlastních čísel $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ a rozhodni, zda je diagonalizovatelná.
> $p_A(\lambda) = (2 - \lambda)^2$: jediné vlastní číslo $2$, **algebraická násobnost $2$**. $A - 2E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $x_2 = 0$, vlastní podprostor $\operatorname{span}\{(1; 0)\}$, **geometrická násobnost $1$**. Dva LN vlastní vektory neexistují, takže **diagonalizovatelná není**.

> [!priklad|23]- Jsou podobné matice $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ a $\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}$? A matice $2E_2$ a $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$?
> Obě první mají (trojúhelníkové) vlastní čísla $1$ a $3$, každé s vlastním vektorem, ty dva jsou LN: $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = P\,\operatorname{diag}(1, 3)P^{-1}$ s $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ a $\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix} = Q\,\operatorname{diag}(1, 3)Q^{-1}$ s $Q = \begin{pmatrix} 0 & 2 \\ 1 & 5 \end{pmatrix}$. Obě jsou podobné téže diagonální matici, tedy **jsou podobné**: z $\operatorname{diag}(1, 3) = Q^{-1}\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}Q$ vyjde $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = S^{-1}\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}S$ pro $S = QP^{-1}$. Druhá dvojice **podobná není**: $T^{-1}(2E)T = 2E$ pro každé $T$, přestože polynom $(2 - \lambda)^2$ je stejný.

> [!priklad|24]- Najdi vlastní čísla a vlastní podprostory derivace $D : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $p \mapsto p'$. Je diagonalizovatelná?
> V bázi $(1, x, x^2)$: $[D] = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$, horní trojúhelníková, $p_D(\lambda) = -\lambda^3$. Jediné vlastní číslo **$0$** s algebraickou násobností $3$; vlastní podprostor $\ker D = $ **konstanty** $\operatorname{span}\{1\}$, geometrická násobnost $1$. Báze z vlastních vektorů neexistuje, **diagonalizovatelná není**.

---
← [[LAG 15 – Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci|13. 11. 2026 Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci]]

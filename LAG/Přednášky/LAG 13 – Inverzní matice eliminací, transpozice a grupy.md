---
predmet: LAG
prednaska: 13
datum: 2026-11-06
zdroj: "V poznámkách úloha 8.14 až pozorování 8.25 a kap. 9* (pozn. 9.1–9.18)"
tags: [prednaska, LAG]
---

# LAG 13 – Inverzní matice eliminací, transpozice a grupy

*Přednáška 13 · pátek 6. 11. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `inverze přes (A | E)` · `Gaussova–Jordanova eliminace` · `(A | B) ~ (E | A⁻¹B)` · `ERÚ = násobení regulární maticí` · `B = TA` · `úpravy zachovávají hodnost` · `transponovaná matice` · `(AB)ᵀ = BᵀAᵀ` · `rank A = rank Aᵀ` · `charakterizace regulární matice` · `grupa` · `podgrupa` · `homomorfismus a jádro` · `zbytkové třídy ℤₙ` · `permutace a znaménko`

Minule jsme Gaussovou eliminací řešili soustavy. Dnes stejným postupem počítáme inverzní matici a ukážeme, že každá řádková úprava je jen vynásobení regulární maticí zleva. Z toho plyne, že úpravy zachovávají hodnost a že hodnost řádků je stejná jako hodnost sloupců ($\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}}$). Druhá polovina je krátký výlet do abstraktní algebry: grupy, homomorfismy, počítání „na ciferníku“ v $\mathbb{Z}_n$ a permutace, které budou potřeba u determinantu.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[výpočet inverzní matice eliminací]] | $(A \mid E) \sim \dots \sim (E \mid A^{-1})$, obecně $(A \mid B) \sim (E \mid A^{-1}B)$ | $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}^{-1} = \begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix}$ |
| [[Gaussova–Jordanova eliminace]] | po Gaussově eliminaci vyděl pivoty a vynuluj i nad nimi | redukovaný stupňovitý tvar |
| [[matice elementární řádkové úpravy]] | každá ERÚ = násobení regulární maticí $T$ zleva | $T$ = úprava provedená na $E$ |
| [[věta o řádkových úpravách a regulární matici]] | $A$ jde upravit na $B$ $\Leftrightarrow$ $B = TA$ pro regulární $T$ | $T = T_2T_1 = A^{-1}$ |
| [[zachování hodnosti při řádkových úpravách]] | $\operatorname{rank}(TA) = \operatorname{rank} A$ | |
| [[transponovaná matice]] ♥ | $[A^{\mathsf{T}}]_{ij} = a_{ji}$, řádky ↔ sloupce | $(1\ 2\ 3)^{\mathsf{T}}$ je sloupec |
| [[transpozice součinu matic]] | $(AB)^{\mathsf{T}} = B^{\mathsf{T}}A^{\mathsf{T}}$, pořadí se otočí | |
| [[věta o hodnosti transponované matice]] | $\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}} \le \min\{m, n\}$ | |
| [[věta o charakterizaci regulární matice]] | regulární $\Leftrightarrow$ $\operatorname{rank} A = n$ $\Leftrightarrow$ LN sloupce $\Leftrightarrow$ LN řádky … | |
| [[grupa]], [[abelovská grupa]] | asociativita, neutrální prvek, inverze (+ komutativita) | $(\mathbb{Z}, +)$, $(\mathbb{R} \setminus \{0\}, \cdot)$ |
| [[podgrupa]] | uzavřená na operaci i inverze | sudá čísla v $(\mathbb{Z}, +)$ |
| [[homomorfismus grup]], [[jádro homomorfismu]] | $\varphi(xy) = \varphi(x)\varphi(y)$; $\ker \varphi = \varphi^{-1}\{e\}$ | $x \mapsto e^x$ |
| [[věta o prostotě homomorfismu]] | prostý $\Leftrightarrow$ $\varphi^{-1}\{e\} = \{e\}$ | |
| [[zbytková třída]], [[grupa zbytkových tříd]] | $[i] = \{i + kn \mid k \in \mathbb{Z}\}$, $[i] + [j] = [i + j]$ | hodiny: $[9] + [5] = [2]$ v $\mathbb{Z}_{12}$ |
| [[permutace]] ♥ | bijekce $\{1, \dots, n\} \to \{1, \dots, n\}$; $S_n$ má $n!$ prvků | $\pi = (3\ 1\ 4\ 2)$ |
| [[inverze v permutaci]], [[znaménko permutace]] ♥ | $i < j$, $\pi(i) > \pi(j)$; $\operatorname{sgn} \pi = (-1)^{\text{počet inverzí}}$ | 3 inverze, $\operatorname{sgn} = -1$ |
| [[transpozice (permutace)]] | prohodí dva prvky, je lichá | |
| [[věta o znaménku složené permutace]] | $\operatorname{sgn}(\pi\sigma) = \operatorname{sgn}\pi \operatorname{sgn}\sigma$, $\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$ | |

## §1 Inverzní matice Gaussovou eliminací

### Inverze jako řešení soustav (úloha 8.14)

Regulární matice $A \in \mathbb{F}^{n \times n}$ určuje izomorfismus $\vec{x} \mapsto A\vec{x}$ a [[inverzní matice]] $A^{-1}$ je matice inverzního zobrazení. Jako každá [[matice zobrazení v kanonické bázi|matice zobrazení v kanonické bázi]] má $A^{-1}$ ve sloupcích obrazy vektorů kanonické báze:

$$
A^{-1} = \big(A^{-1}\vec{e}_1 \ \cdots \ A^{-1}\vec{e}_n\big).
$$

Vektor $\vec{x}_j = A^{-1}\vec{e}_j$ je jediné $\vec{x}$, pro které $A\vec{x} = \vec{e}_j$. Hledat $j$-tý sloupec inverze tedy znamená **vyřešit soustavu $A\vec{x} = \vec{e}_j$**. Všech $n$ soustav má tutéž matici $A$, takže je stačí upravovat naráz: za čáru napíšeš všechny pravé strany $\vec{e}_1, \dots, \vec{e}_n$, tedy jednotkovou matici.

> [!example] Příklad (úloha 8.14)
> $A = \begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}$. Upravujeme $(A \mid E)$, dokud vlevo nevznikne $E$:
>
> $$
> \left(\begin{array}{cc|cc} 1 & 3 & 1 & 0 \\ 2 & 5 & 0 & 1 \end{array}\right)
> \sim
> \left(\begin{array}{cc|cc} 1 & 3 & 1 & 0 \\ 0 & -1 & -2 & 1 \end{array}\right)
> \sim
> \left(\begin{array}{cc|cc} 1 & 0 & -5 & 3 \\ 0 & -1 & -2 & 1 \end{array}\right)
> \sim
> \left(\begin{array}{cc|cc} 1 & 0 & -5 & 3 \\ 0 & 1 & 2 & -1 \end{array}\right)
> $$
>
> ($r_2 - 2r_1$; $r_1 + 3r_2$; $r_2 \cdot (-1)$). Vpravo je $A^{-1} = \begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix}$. Kontrola: $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}\begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} -5 + 6 & 3 - 3 \\ -10 + 10 & 6 - 5 \end{pmatrix} = E$. ✓
>
> S inverzí se pak dá vyřešit každá soustava s maticí $A$: $A\vec{x} = (2; 8)$ má řešení $\vec{x} = A^{-1}(2; 8) = (-10 + 24;\ 4 - 8) = (14; -4)$, a opravdu $14 - 12 = 2$, $28 - 20 = 8$.

Že soustavy měly jednoznačné řešení, zároveň dokazuje, že $A$ regulární je. Kdyby nebyla, eliminace vlevo nedojde k $E$: vznikne nulový řádek a některá soustava $A\vec{x} = \vec{e}_j$ řešení mít nebude.

> [!definice] Algoritmus 8.12 · Gaussova–Jordanova eliminace
> Vstup: matice $B \in \mathbb{F}^{m \times n}$. Proveď Gaussovu eliminaci a označ $k_1, \dots, k_r$ hlavní sloupce. Pak pro $i = r, r - 1, \dots, 1$ opakuj:
>
> 1. vyděl $i$-tý řádek pivotem $b_{ik_i}$,
> 2. pro každé $j < i$ odečti od $j$-tého řádku $b_{jk_i}$-násobek $i$-tého.
>
> Výsledný tvar matice se nazývá *redukovaný stupňovitý tvar*: pivoty jsou jedničky a nad i pod nimi jsou nuly.

^def-gauss-jordan

> [!lidsky] Lidsky
> Obyčejná Gaussova eliminace jde **shora dolů** a nuluje pod pivoty. Gaussova–Jordanova pak jde **zdola nahoru**: z každého pivotu udělá jedničku a vynuluje i čísla nad ním. Na konci vidíš výsledek rovnou, bez dosazování; výpočetně je to totéž co [[zpětná substituce]].

> [!example] Příklad
> $\left(\begin{array}{cc|c} 2 & 4 & 6 \\ 0 & 3 & 3 \end{array}\right)$ je stupňovitý, ale ne redukovaný. Vyděl $r_2$ třemi: $(0\ 1 \mid 1)$; odečti $4r_2$ od $r_1$: $(2\ 0 \mid 2)$; vyděl $r_1$ dvěma: $(1\ 0 \mid 1)$. Redukovaný tvar $\left(\begin{array}{cc|c} 1 & 0 & 1 \\ 0 & 1 & 1 \end{array}\right)$ říká rovnou $x = 1$, $y = 1$.
>
> Nepříklad: $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ redukovaná není, nad pivotem ve 2. sloupci zůstala dvojka.

> [!veta] Pozn. 8.19 · Inverze a $A^{-1}B$ eliminací
> ==Buď $A \in \mathbb{F}^{n \times n}$ regulární a $B \in \mathbb{F}^{n \times p}$.== Gaussova–Jordanova eliminace převede
>
> $$
> \mathbf{(A \mid B) \sim \dots \sim (E \mid A^{-1}B)},
> $$
>
> speciálně pro $B = E$ je **$(A \mid E) \sim \dots \sim (E \mid A^{-1})$**. Tak se dá řešit i maticová rovnice $AX = B$: $X = A^{-1}B$.
>
> > [!note]- Důkaz
> > Každá řádková úprava je násobení regulární maticí zleva (lemma 8.15 v §2), a ta působí na obě části matice stejně: $T(A \mid B) = (TA \mid TB)$. Když úpravy převedou levou část na $E$, je $TA = E$, tedy $T = A^{-1}$, a pravá část je $TB = A^{-1}B$.

^veta-inverze-eliminaci

> [!lidsky] Lidsky
> Upravuješ levou část, dokud z ní není jednička. Pravá část dostane „zadarmo“ tytéž úpravy, a protože úpravy dohromady odpovídají násobení $A^{-1}$, objeví se vpravo $A^{-1}B$. Pro $B = E$ je to přímo inverze.

> [!pozor] Kdy se postup zastaví
> Když při eliminaci vlevo vznikne **nulový řádek**, $A$ není regulární a inverzi nemá; dál nepočítej. Nepomůže ani prohazování sloupců, to není řádková úprava. A úpravy dělej s **celým řádkem** včetně části za čarou, jinak ztratíš vztah $T(A \mid B) = (TA \mid TB)$.

> [!navic] K čemu je to v testu
> Matici transformace souřadnic $T_{\mathcal{X} \to \mathcal{Y}}$ v $\mathbb{F}^n$ najdeš jako $Y^{-1}X$, kde $X$, $Y$ mají ve sloupcích vektory bází. Eliminace $(Y \mid X) \sim (E \mid Y^{-1}X)$ ji dá bez počítání inverze zvlášť. Stejně $[A]^{\mathcal{X} \to \mathcal{X}} = X^{-1}AX$ dostaneš z $(X \mid AX) \sim (E \mid X^{-1}AX)$. Viz typové příklady na konci.

## §2 Řádkové úpravy jako násobení maticí

> [!veta] Lemma 8.15\*
> ==Buď $B \in \mathbb{F}^{m \times n}$.== **Každou elementární řádkovou úpravu matice $B$ lze realizovat vynásobením $B$ zleva regulární maticí $T \in \mathbb{F}^{m \times m}$**, $T = (\vec{t}_1 \cdots \vec{t}_m)$, kde
>
> 1. pro prohození $k$-tého a $l$-tého řádku je $\vec{t}_i = \vec{e}_i$ pro $i \ne k, l$, $\vec{t}_k = \vec{e}_l$, $\vec{t}_l = \vec{e}_k$,
> 2. pro vynásobení $k$-tého řádku číslem $\alpha \ne 0$ je $\vec{t}_i = \vec{e}_i$ pro $i \ne k$, $\vec{t}_k = \alpha\vec{e}_k$,
> 3. pro přičtení $\alpha$-násobku $k$-tého řádku k $l$-tému je $\vec{t}_i = \vec{e}_i$ pro $i \ne k$, $\vec{t}_k = \vec{e}_k + \alpha\vec{e}_l$.
>
> > [!note]- Důkaz
> > Pro sloupec $\vec{b} = \sum_i b_i\vec{e}_i$ a matici z bodu 3 je $T\vec{b} = \sum_i b_i\vec{t}_i = \sum_{i \ne k} b_i\vec{e}_i + b_k(\vec{e}_k + \alpha\vec{e}_l) = \vec{b} + \alpha b_k\vec{e}_l$: k $l$-té složce se přičte $\alpha$-násobek $k$-té, ostatní se nemění. Body 1 a 2 se ověří stejně. Násobení zleva působí po sloupcích, $TB = (T\vec{b}_1 \cdots T\vec{b}_n)$, takže se úprava provede v každém sloupci, tedy s celými řádky. Každá úprava jde vrátit jinou úpravou (prohodit znovu, vynásobit $\alpha^{-1}$, přičíst $-\alpha$-násobek), takže příslušné zobrazení má inverzi a $T$ je regulární.

^veta-matice-uprav

> [!lidsky] Lidsky
> Matici úpravy nemusíš skládat podle vzorců: **udělej tu úpravu s jednotkovou maticí** $E_m$. Co vyjde, je $T$. Pak $TB$ je přesně $B$ po té úpravě. Proto je každá eliminace jen násobení maticí, a to dává do ruky nástroje z algebry matic.

> [!obrazek] Tři typy matic elementárních úprav
> ![[lag13-elementarni.png]]
> *Matice pro $m = 4$. Modré jedničky jsou zbytek jednotkové matice, oranžově jsou pozice, které úprava změnila: prohozené řádky, číslo $\alpha$ na diagonále, číslo $\alpha$ na pozici (řádek 3, sloupec 1).*

> [!example] Příklad
> Pro $X = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$ a úpravu „ke 3. řádku přičti dvojnásobek 1.“ je $T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{pmatrix}$ a $TX = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 7 & 10 \end{pmatrix}$: třetí řádek $(5\ 6) + 2(1\ 2) = (7\ 10)$.
>
> V úloze 8.14 výše odpovídal první krok ($r_2 - 2r_1$) matici $T_1 = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}$ a zbylé dva kroky ($r_1 + 3r_2$, pak $r_2 \cdot (-1)$) dohromady matici $T_2 = \begin{pmatrix} 1 & 3 \\ 0 & -1 \end{pmatrix}$. Celá eliminace je
>
> $$
> T = T_2T_1 = \begin{pmatrix} 1 & 3 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix} = A^{-1}.
> $$

> [!pozor] Pořadí v součinu
> Úprava provedená **později** stojí v součinu **vlevo**: $B = T_l \cdots T_2T_1A$. Matice se násobí zprava doleva stejně jako u [[složené zobrazení|skládání zobrazení]], a $T_1T_2 \ne T_2T_1$.

> [!veta] Věta 8.16
> ==Buď $A, B \in \mathbb{F}^{m \times n}$.== **Matici $A$ lze převést sledem elementárních řádkových úprav na $B$, právě když existuje regulární matice $T \in \mathbb{F}^{m \times m}$ taková, že $B = TA$.**
>
> > [!note]- Důkaz\*
> > **($\Rightarrow$)** Podle lemmatu 8.15 dává sled úprav regulární matice $T_1, \dots, T_l$ s $B = T_l \cdots T_1A$; součin regulárních matic je regulární, takže $T = T_l \cdots T_1$.
> >
> > **($\Leftarrow$)** Je-li $T$ regulární, je regulární i $T^{-1}$ a Gaussova–Jordanova eliminace ji převede na $E$. Tím dostaneme úpravy s maticemi $T_1, \dots, T_l$ a $E = T_l \cdots T_1T^{-1}$, tedy $T = T_l \cdots T_1$. Tytéž úpravy proto vedou od $A$ k $TA = B$.

^veta-upravy-regularni

> [!lidsky] Lidsky
> „Dá se upravit na“ a „vznikne vynásobením regulární maticí zleva“ je totéž. Sloupce $B$ jsou jen obrazy sloupců $A$ při izomorfismu $\vec{x} \mapsto T\vec{x}$, takže mezi sloupci zůstávají **tytéž lineární vztahy**: co bylo kombinací ostatních, je kombinací se stejnými koeficienty, LN zůstane LN.

> [!veta] Důsledek 8.17
> ==Vznikne-li $B$ z $A$ sledem elementárních řádkových úprav==, pak **$\operatorname{rank} B = \operatorname{rank} A$**.
>
> > [!note]- Důkaz
> > $B = TA$ s regulární $T$. Zobrazení $\vec{y} \mapsto T\vec{y}$ je izomorfismus, tedy prosté, a zůstane prosté i zúžené na $\operatorname{im} A$. Jeho obraz je $T(\operatorname{im} A) = \operatorname{im}(TA)$. Prosté lineární zobrazení má nulový defekt, takže podle [[věta o dimenzi jádra a obrazu|věty o dimenzi jádra a obrazu]] je $\dim \operatorname{im} A = \dim \operatorname{im}(TA)$, tedy $\operatorname{rank} A = \operatorname{rank} B$.

^dusledek-hodnost-uprav

> [!lidsky] Lidsky
> Násobení regulární maticí je „otočení a natažení“ prostoru, které nic nezmáčkne do menšího rozměru. Obal sloupců se sice změní, ale **dimenzi si zachová**. Proto smíš hodnost počítat po eliminaci.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \sim \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} = B$ ($r_2 - 2r_1$). Obraz se změnil: $\operatorname{im} A = \operatorname{span}\{(1; 2)\}$, $\operatorname{im} B = \operatorname{span}\{(1; 0)\}$. Obě jsou ale přímky, $\operatorname{rank} A = \operatorname{rank} B = 1$.

## §3 Transponovaná matice a hodnost řádků

> [!definice] Definice · pozn. 8.21 ♥
> Pro matici $A \in \mathbb{F}^{m \times n}$ definujeme *matici transponovanou* $A^{\mathsf{T}} \in \mathbb{F}^{n \times m}$ s prvky
>
> $$
> [A^{\mathsf{T}}]_{ij} = a_{ji}.
> $$
>
> Pro sloupec $\vec{x} \in \mathbb{F}^n$ (matici s jedním sloupcem) je $\vec{x}^{\mathsf{T}}$ řádkový vektor, matice s jedním řádkem a $n$ sloupci.

^def-transponovana

> [!lidsky] Lidsky
> **Řádky se stanou sloupci** a naopak: $i$-tý řádek $A$ je $i$-tý sloupec $A^{\mathsf{T}}$. Geometricky překlopíš tabulku podle hlavní diagonály (té, která začíná vlevo nahoře). Rozměr $m \times n$ se změní na $n \times m$.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$, $A^{\mathsf{T}} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$; třeba $[A^{\mathsf{T}}]_{31} = a_{13} = 3$. Sloupec $\begin{pmatrix} 1 \\ 2 \end{pmatrix}^{\mathsf{T}} = (1\ 2)$. U symetrické matice $\begin{pmatrix} 1 & 7 \\ 7 & 2 \end{pmatrix}$ transpozice nic nezmění, u $\begin{pmatrix} 1 & 7 \\ 0 & 2 \end{pmatrix}$ ano: vznikne $\begin{pmatrix} 1 & 0 \\ 7 & 2 \end{pmatrix}$.

> [!obrazek] Transpozice jako překlopení podle diagonály
> ![[lag13-transpozice.png]]
> *Každý sloupec $A$ má svou barvu (modrý, zelený, oranžový) a v $A^{\mathsf{T}}$ se z něj stane řádek stejné barvy. Červená čárkovaná je hlavní diagonála; čísla na ní ($1$ a $5$) zůstávají na místě.*

> [!veta] Cvičení · Transpozice součinu
> ==Buď $A \in \mathbb{F}^{m \times n}$ a $B \in \mathbb{F}^{n \times p}$.== Potom **$(AB)^{\mathsf{T}} = B^{\mathsf{T}}A^{\mathsf{T}}$**.
>
> > [!note]- Důkaz
> > Obě strany mají rozměr $p \times m$. Pro prvek na pozici $(i, j)$:
> >
> > $$
> > [(AB)^{\mathsf{T}}]_{ij} = [AB]_{ji} = \sum_{k=1}^{n} a_{jk}b_{ki} = \sum_{k=1}^{n} [B^{\mathsf{T}}]_{ik}[A^{\mathsf{T}}]_{kj} = [B^{\mathsf{T}}A^{\mathsf{T}}]_{ij}.
> > $$

^veta-transpozice-soucinu

> [!lidsky] Lidsky
> Jako svlékání: co si oblékneš poslední, sundáváš první. Transpozice součinu **otočí pořadí** činitelů. Jinak by to ani nešlo: $A^{\mathsf{T}}B^{\mathsf{T}}$ je $(n \times m)(p \times n)$ a pro $m \ne p$ vůbec nedává smysl.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$: $AB = \begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}$, $(AB)^{\mathsf{T}} = \begin{pmatrix} 7 & 3 \\ 2 & 1 \end{pmatrix} = B^{\mathsf{T}}A^{\mathsf{T}}$. Naopak $A^{\mathsf{T}}B^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix}$, tedy jiná matice.

> [!veta] Věta 8.22 a důsledek 8.23
> ==Buď $A \in \mathbb{F}^{m \times n}$.== Potom **$\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}}$** a tedy **$\operatorname{rank} A \le \min\{m, n\}$**.
>
> > [!note]- Důkaz
> > **Rovnost.** Je-li $A$ v [[horní stupňovitý tvar|horním stupňovitém tvaru]] s $r$ pivoty, je LN sloupců $r$ (hlavní sloupce, věta 8.6) a LN řádků také $r$: nenulové řádky jsou LN, protože ve sloupci prvního pivotu má nenulové číslo jen první řádek, takže v nulové kombinaci řádků musí mít první řádek koeficient $0$; pak totéž platí pro druhý řádek atd. Každou matici lze řádkovými úpravami převést na stupňovitý tvar, takže stačí, že úpravy nemění dimenzi obalu sloupců (důsledek 8.17) ani obalu řádků. Pro řádky je to snadné: každý nový řádek je kombinací starých a díky vratnosti úprav i naopak, takže **obal řádků se nezmění vůbec**. Dimenze obalu řádků $A$ je přitom $\operatorname{rank} A^{\mathsf{T}}$.
> >
> > **Odhad.** $\operatorname{im} A \le \mathbb{F}^m$, takže $\operatorname{rank} A \le m$. Stejně $\operatorname{im} A^{\mathsf{T}} \le \mathbb{F}^n$, takže $\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}} \le n$.

^veta-hodnost-transpozice

> [!lidsky] Lidsky
> Hodnost můžeš počítat **po řádcích i po sloupcích**, vyjde totéž: počet nezávislých řádků = počet nezávislých sloupců. Proto matice $3 \times 100$ nemá nikdy hodnost víc než 3, i když má 100 sloupců: sloupce žijí v $\mathbb{F}^3$.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$: druhý řádek je dvojnásobek prvního, takže LN řádek je jen jeden, a sloupce $(1; 2)$, $(2; 4)$, $(3; 6)$ jsou všechny násobky $(1; 2)$. **$\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}} = 1 \le \min\{2, 3\}$.**

> [!pozor] Řádkové úpravy mění obal sloupců, ne obal řádků
> Po eliminaci smíš vzít **nenulové řádky upravené matice** jako bázi obalu řádků, protože ten se nezměnil. Bázi obalu **sloupců** (obrazu) ale musíš vzít z **původní** matice na pozicích hlavních sloupců.

> [!veta] Pozorování 8.25
> ==Buď $A \in \mathbb{F}^{n \times n}$ a $\vec{b} \in \mathbb{F}^n$.== Následující výroky jsou **ekvivalentní**:
>
> 1. $A\vec{x} = \vec{0}$ má právě jedno řešení,
> 2. $A\vec{x} = \vec{b}$ má právě jedno řešení,
> 3. $A$ je [[regulární matice|regulární]],
> 4. $\operatorname{rank} A = n$,
> 5. $A$ má lineárně nezávislé sloupce,
> 6. $A$ má lineárně nezávislé řádky.
>
> > [!note]- Důkaz
> > Body 1–5 plynou z dřívějších vět: pro čtvercovou matici je $\vec{x} \mapsto A\vec{x}$ prosté $\Leftrightarrow$ $\ker A = \{\vec{0}\}$ $\Leftrightarrow$ $\operatorname{def} A = 0$ $\Leftrightarrow$ $\operatorname{rank} A = n$ $\Leftrightarrow$ na, takže prosté $\Leftrightarrow$ bijekce; hodnost $n$ znamená $n$ LN sloupců z $n$; podle Frobeniovy věty je řešení jediné, právě když $\dim S_0 = n - \operatorname{rank} A = 0$. Bod 6 plyne z $\operatorname{rank} A^{\mathsf{T}} = \operatorname{rank} A = n$.

^veta-charakterizace-regularni

> [!lidsky] Lidsky
> U čtvercové matice je „všechno nebo nic“: buď je regulární a pak soustava s ní má vždy právě jedno řešení, sloupce i řádky jsou LN a hodnost je plná, nebo neplatí ani jedno z toho. Stačí ověřit **kteroukoli** podmínku, nejčastěji eliminací hodnost.

> [!example] Příklad
> $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$: řádky jsou LZ ($r_2 = 2r_1$), takže **nic** z 1–6 neplatí; třeba $A\vec{x} = \vec{0}$ má kromě nuly i řešení $(2; -1)$. Naopak $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}$ má hodnost 2, je regulární a $A\vec{x} = (2; 8)$ má jediné řešení $(14; -4)$.

> [!pozor] Jen pro čtvercové matice
> Pro obdélníkovou matici ekvivalence neplatí: $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$ má LN řádky, ale sloupce LZ (tři vektory v $\mathbb{R}^2$), a regulární být nemůže, protože regularita je definovaná jen pro čtvercové matice.

## §4 Grupy

> [!navic] Kapitola 9 je s hvězdičkou
> Celá kapitola 9 („jemný náhled do světa abstraktní algebry“) není nutná ke zkoušce, **kromě permutace** (§6), ze které se v příští kapitole postaví determinant. Grupy ale ukazují, co mají lineární prostory, zbytky po dělení a permutace společného, a pojmy jako jádro a izomorfismus tu potkáš znovu.

> [!definice] Definice · pozn. 9.1
> Dvojice $(G, \cdot)$ neprázdné množiny $G$ a operace $\cdot : G \times G \to G$ splňující následující tři axiomy se nazývá *grupa*:
>
> 1. *asociativní zákon:* $\forall x, y, z \in G:\ (x \cdot y) \cdot z = x \cdot (y \cdot z)$,
> 2. *existence neutrálního prvku:* $\exists e \in G\ \forall x \in G:\ x \cdot e = x = e \cdot x$,
> 3. *existence inverzí:* $\forall x \in G\ \exists y \in G:\ x \cdot y = e = y \cdot x$.
>
> Grupa se nazývá *abelovská*, jestliže navíc platí
>
> 4. *komutativní zákon:* $\forall x, y \in G:\ x \cdot y = y \cdot x$.

^def-grupa

> [!lidsky] Lidsky
> Grupa je množina s jedinou operací, se kterou se dá počítat „jako se sčítáním“: nezáleží na uzávorkování, existuje prvek, který nic nemění (jako $0$ u sčítání nebo $1$ u násobení), a každý krok jde vrátit (k $x$ existuje $x^{-1}$). Na pořadí obecně záležet smí; když nezáleží, je grupa abelovská.

> [!example] Příklad (pozn. 9.8)
> - $(\mathbb{Z}, +)$: neutrální prvek $0$, inverze k $5$ je $-5$; abelovská grupa. Stejně $(\mathbb{R}, +)$, $(\mathbb{F}, +)$ a $(L, +)$ pro každý lineární prostor $L$.
> - $(\mathbb{R} \setminus \{0\}, \cdot)$: neutrální prvek $1$, inverze k $4$ je $\tfrac{1}{4}$; abelovská grupa.
> - **Nejsou grupy:** $(\mathbb{Z}, \cdot)$, protože $2$ nemá inverzi ($\tfrac{1}{2} \notin \mathbb{Z}$); $(\mathbb{N}, +)$, protože k $1$ chybí opačný prvek; $(\mathbb{Z}, -)$, protože odčítání není asociativní: $(1 - 2) - 3 = -4$, ale $1 - (2 - 3) = 2$.
> - **Neabelovská grupa:** regulární matice $n \times n$ s násobením (pro $n \ge 2$): $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, ale v opačném pořadí $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.

> [!navic] Pologrupa, monoid a značení (pozn. 9.2–9.4)
> - Jen asociativita = *pologrupa*; asociativita a neutrální prvek = *monoid*. Třeba $(\mathbb{N}, \cdot)$ je monoid, ale ne grupa.
> - V každé grupě je neutrální prvek **jediný** a každý prvek má **jedinou** inverzi; dokazuje se to stejně jako jednoznačnost nulového a opačného vektoru ([[věta o vlastnostech lineárního prostoru]]).
> - Operace se značí $\cdot$ (často se vynechává, $xy$), neutrální prvek $e$ a inverze $x^{-1}$. U abelovských grup se často píše $+$, neutrální prvek $0$, opačný prvek $-x$ a $x - y$ místo $x + (-y)$.
> - Regulární matice $n \times n$ nad $\mathbb{F}$ tvoří grupu $GL(n, \mathbb{F})$ (obecná lineární grupa, pozn. 9.10): součin regulárních matic je regulární, $E$ je neutrální prvek a inverzní matice je inverze.

> [!definice] Definice · podgrupa
> Nechť $(G, \cdot)$ je grupa. Neprázdná podmnožina $K \subseteq G$ se nazývá *podgrupa* grupy $G$, jestliže pro každé $x, y \in K$ platí $xy \in K$ a $x^{-1} \in K$.

^def-podgrupa

> [!lidsky] Lidsky
> Kousek grupy, ze kterého operace ani inverze nevyvedou ven, takže je to sám o sobě grupa se stejnou operací. Obdoba [[lineární podprostor|lineárního podprostoru]]: tam se ověřuje uzavřenost na sčítání a násobení číslem, tady na operaci a inverzi.

> [!example] Příklad
> Sudá čísla $2\mathbb{Z} = \{\dots, -2, 0, 2, 4, \dots\}$ jsou podgrupa $(\mathbb{Z}, +)$: součet sudých je sudé a opačné k sudému je sudé. **Lichá čísla ne:** $1 + 3 = 4$ není liché. $\mathbb{N}$ v $(\mathbb{Z}, +)$ také ne: $-1 \notin \mathbb{N}$.

> [!pozor] Proč „neprázdná“
> Podmínky „$xy \in K$ a $x^{-1} \in K$ pro všechna $x, y \in K$“ splní i prázdná množina, protože v ní žádné $x$ není. Až s neprázdností plyne, že podgrupa obsahuje neutrální prvek: vezmi $x \in K$, pak $x^{-1} \in K$ a $e = xx^{-1} \in K$.

> [!definice] Definice · pozn. 9.5
> Buďte $(G, \cdot)$ a $(H, \cdot)$ grupy. Zobrazení $\varphi : G \to H$ se nazývá *homomorfismus*, jestliže pro každé $x, y \in G$ platí
>
> $$
> \varphi(x \cdot y) = \varphi(x) \cdot \varphi(y).
> $$
>
> Je-li homomorfismus bijekcí, nazýváme jej *izomorfismus*. (Prostý homomorfismus je *monomorfismus*, homomorfismus na je *epimorfismus*.)

^def-homomorfismus

> [!lidsky] Lidsky
> Zobrazení, kterému je jedno, jestli nejdřív spočítáš v $G$ a pak převedeš, nebo nejdřív převedeš a pak spočítáš v $H$. Přesně to jsme chtěli po [[lineární zobrazení|lineárních zobrazeních]]; lineární zobrazení je homomorfismus grup $(V, +) \to (W, +)$, které navíc zachovává násobení číslem.

> [!example] Příklad
> $\varphi(x) = e^x$ je homomorfismus $(\mathbb{R}, +) \to (\mathbb{R} \setminus \{0\}, \cdot)$, protože $e^{x + y} = e^x e^y$: součet se převede na součin. Je prostý, ale ne na (záporná čísla nenabývá), takže je to monomorfismus.
>
> $(\{1, -1\}, \cdot)$ a $(\mathbb{Z}_2, +)$ (§5) jsou izomorfní přes $1 \mapsto [0]$, $-1 \mapsto [1]$: „mínus krát mínus je plus“ je totéž co „liché plus liché je sudé“.
>
> Nepříklad: $\varphi(x) = x + 1$ na $(\mathbb{Z}, +)$ homomorfismus není: $\varphi(1 + 1) = 3$, ale $\varphi(1) + \varphi(1) = 4$.

> [!definice] Definice · jádro homomorfismu (cvičení 9.7)
> Buď $\varphi : G \to H$ homomorfismus grup a $e$ neutrální prvek $H$. *Jádro homomorfismu* $\varphi$ je vzor neutrálního prvku:
>
> $$
> \ker \varphi = \varphi^{-1}\{e\} = \{x \in G \mid \varphi(x) = e\} \subseteq G.
> $$
>
> Jádro je vždy podgrupa grupy $G$.

^def-jadro-homomorfismu

> [!lidsky] Lidsky
> Všechno, co $\varphi$ „zabije“, tedy pošle na neutrální prvek. U lineárního zobrazení je neutrální prvek nulový vektor a jádro je to známé [[jádro]] $\ker A = A^{-1}\{\vec{0}\}$.

> [!example] Příklad
> Pro $\varphi : (\mathbb{Z}, +) \to (\mathbb{Z}_{12}, +)$, $k \mapsto [k]$ (čtení hodin) je $\ker \varphi = \{\dots, -12, 0, 12, 24, \dots\} = 12\mathbb{Z}$: přesně posuny o celé násobky 12 hodin nezmění, kolik ukazují hodiny. Pro $x \mapsto e^x$ je jádro $\{0\}$, protože $e^x = 1$ jen pro $x = 0$.

> [!veta] Věta 9.6
> ==Buďte $G$ a $H$ grupy a $\varphi : G \to H$ homomorfismus.== Potom **$\varphi$ je prostý, právě když $\varphi^{-1}\{e\} = \{e\}$.**
>
> > [!note]- Důkaz
> > **($\Rightarrow$)** Homomorfismus pošle $e$ na $e$ ($\varphi(e) = \varphi(ee) = \varphi(e)\varphi(e)$, vynásob zleva $\varphi(e)^{-1}$). Prostý homomorfismus už nic jiného na $e$ poslat nemůže.
> >
> > **($\Leftarrow$)** Nechť $\varphi(x_1) = \varphi(x_2)$. Pak $\varphi(x_1x_2^{-1}) = \varphi(x_1)\varphi(x_2^{-1}) = \varphi(x_1)\varphi(x_2)^{-1} = \varphi(x_1)\varphi(x_1)^{-1} = e$, kde jsme použili $\varphi(g^{-1}) = \varphi(g)^{-1}$ (plyne z $\varphi(g)\varphi(g^{-1}) = \varphi(gg^{-1}) = \varphi(e) = e$). Protože na $e$ jde jen $e$, je $x_1x_2^{-1} = e$, tedy $x_1 = x_2$.

^veta-prostota-homomorfismu

> [!lidsky] Lidsky
> Stejný trik jako u lineárních zobrazení ([[věta o prostotě a jádru]]): stačí zkontrolovat, že se na neutrální prvek nezobrazí nic navíc. Kdyby dva různé prvky šly na stejné místo, jejich „rozdíl“ $x_1x_2^{-1} \ne e$ by šel na $e$.

> [!example] Příklad
> $k \mapsto [k]$ z $\mathbb{Z}$ do $\mathbb{Z}_{12}$ prostý není, protože jádro je $12\mathbb{Z} \ne \{0\}$; opravdu $0$ i $12$ jdou na $[0]$. $x \mapsto e^x$ prostý je, jádro je $\{0\}$.

## §5 Zbytkové třídy $\mathbb{Z}_n$

> [!definice] Definice · pozn. 9.9
> Zafixujme $n \in \mathbb{N}$. Pro $i \in \mathbb{Z}$ je *zbytková třída*
>
> $$
> [i] = \{i + kn \mid k \in \mathbb{Z}\} = \{\dots, i - n, i, i + n, i + 2n, \dots\}.
> $$
>
> Různých tříd je právě $n$, a to $\mathbb{Z}_n = \{[0], [1], \dots, [n - 1]\}$; třída $[j]$ obsahuje všechna celá čísla se zbytkem $j$ po dělení $n$. Pro množiny $A, B \subseteq \mathbb{Z}$ je $A + B = \{a + b \mid a \in A, b \in B\}$ a platí
>
> $$
> [i] + [j] = [i + j].
> $$
>
> S tímto sčítáním je $(\mathbb{Z}_n, +)$ abelovská grupa: neutrální prvek je $[0] = n\mathbb{Z}$ a opačný prvek k $[i]$ je $-[i] = [-i]$.

^def-zbytkove-tridy

> [!lidsky] Lidsky
> Čísla se stejným zbytkem po dělení $n$ hodíš do jednoho pytle a dál počítáš s pytli. Sečíst dva pytle znamená vzít z každého libovolné číslo, sečíst je a podívat se, do kterého pytle výsledek patří; vyjde vždy stejný pytel. Takhle počítají **hodiny** ($n = 12$): 9 hodin plus 5 hodin je 2 hodiny.

> [!example] Příklad
> - V $\mathbb{Z}_{12}$: $[9] + [5] = [14] = [2]$, $-[5] = [-5] = [7]$ (protože $[5] + [7] = [12] = [0]$), $[25] = [1]$.
> - V $\mathbb{Z}_2$ jsou jen dvě třídy, sudá čísla $[0]$ a lichá $[1]$; $[1] + [1] = [0]$ je pravidlo „liché plus liché je sudé“.
> - V $\mathbb{Z}_5$: $[3] + [4] = [7] = [2]$.

> [!obrazek] Grupa $(\mathbb{Z}_{12}, +)$ jako ciferník
> ![[lag13-hodiny.png]]
> *Dvanáct tříd na kružnici. Oranžový oblouk je přičtení $[5]$ k $[9]$: pět kroků po směru ručiček skončí na zeleném $[2]$. Vpravo: zelená třída $[2]$ jako množina čísel, modře neutrální prvek $[0] = 12\mathbb{Z}$ a opačný prvek k $[5]$.*

> [!pozor] $[i]$ je množina, ne číslo
> $[2] = [14] = [-10]$ je **jedna a táž** třída zapsaná různými zástupci. Proto se musí ověřit, že $[i] + [j] = [i + j]$ nezávisí na volbě zástupců; množinová definice $A + B$ to zaručí sama.

> [!navic] Násobení a tělesa $\mathbb{Z}_p$
> Třídy jde i násobit, $[i][j] = [ij]$. $(\mathbb{Z}_n, \cdot)$ ale grupa není ($[0]$ nemá inverzi) a $(\mathbb{Z}_n \setminus \{[0]\}, \cdot)$ je grupa, právě když $n$ je prvočíslo: v $\mathbb{Z}_6$ je $[2][3] = [0]$, takže $[2]$ inverzi nemá. Pro prvočíslo $p$ je $(\mathbb{Z}_p, +, \cdot)$ **těleso** (pozn. 9.19–9.21); lineární algebra nad ním funguje stejně jako nad [[číselné těleso|číselnými tělesy]], jen některé intuice selžou (prostor $\mathbb{Z}_2^n$ má jen $2^n$ vektorů).

## §6 Permutace

> [!definice] Definice · pozn. 9.11 ♥
> Buď $M$ konečná množina. Bijekci $\pi : M \to M$ nazýváme *permutace* množiny $M$. Množinu všech permutací množiny $M = \{1, \dots, n\}$ značíme $S_n$ a nazýváme *symetrická grupa*.

^def-permutace

> [!lidsky] Lidsky
> Permutace je **přeházení pořadí**: každý prvek dostane nové místo a žádná dvě místa nejsou stejná. $S_n$ je grupa vzhledem ke [[složené zobrazení|skládání]]: složením dvou přeházení je přeházení, „nic nepřehazuj“ ($\mathrm{id}$) je neutrální prvek a přeházení jde vrátit (inverzní [[bijekce]]). Prvků má $n! = n(n - 1) \cdots 2 \cdot 1$.

> [!example] Příklad
> Zápis $\pi = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 1 & 4 & 2 \end{pmatrix}$, zkráceně $(3\ 1\ 4\ 2)$, znamená $\pi(1) = 3$, $\pi(2) = 1$, $\pi(3) = 4$, $\pi(4) = 2$. Inverzní permutace čte zápis zdola nahoru: $\pi^{-1} = (2\ 4\ 1\ 3)$. $S_3$ má $3! = 6$ prvků: $(1\,2\,3)$, $(1\,3\,2)$, $(2\,1\,3)$, $(2\,3\,1)$, $(3\,1\,2)$, $(3\,2\,1)$. Nepříklad: $f(1) = 2$, $f(2) = 2$, $f(3) = 1$ permutace není, není prostá.

> [!definice] Definice · pozn. 9.14 ♥
> Buď $\pi \in S_n$. *Inverze v permutaci* $\pi$ je dvojice čísel $(i, j)$ taková, že $1 \le i < j \le n$ a $\pi(i) > \pi(j)$. *Znaménko permutace* $\pi$ je
>
> $$
> \operatorname{sgn} \pi = (-1)^{\text{počet inverzí } \pi}.
> $$
>
> Permutace je *sudá*, má-li sudý počet inverzí ($\operatorname{sgn} \pi = 1$), a *lichá*, má-li lichý počet inverzí ($\operatorname{sgn} \pi = -1$).

^def-znamenko

> [!lidsky] Lidsky
> Inverze je **dvojice, která se přeházením „předběhla“**: menší číslo jde na větší místo než větší číslo. Spočítáš všechny takové dvojice a podle sudosti dostaneš znaménko $+1$, nebo $-1$. V obrázku se šipkami $i \to \pi(i)$ je inverze každé **křížení** dvou šipek.

> [!example] Příklad
> $\pi = (3\ 1\ 4\ 2)$: dvojice $(1, 2)$ ($3 > 1$), $(1, 4)$ ($3 > 2$) a $(3, 4)$ ($4 > 2$) jsou inverze, ostatní tři dvojice ne. **3 inverze, $\operatorname{sgn} \pi = -1$, lichá.** Permutace $(2\ 3\ 1)$ má inverze $(1, 3)$ a $(2, 3)$, je sudá; identita nemá žádnou inverzi, $\operatorname{sgn} \mathrm{id} = 1$.

> [!obrazek] Inverze jako křížení šipek
> ![[lag13-permutace.png]]
> *Zelené šipky vedou z $i$ (nahoře) na $\pi(i)$ (dole) pro $\pi = (3\ 1\ 4\ 2)$. Každé červeně zakroužkované křížení je jedna inverze $(i, j)$: šipky z $i < j$ se překříží právě tehdy, když $\pi(i) > \pi(j)$.*

> [!pozor] Inverze v permutaci ≠ inverzní permutace
> *Inverze v permutaci* je dvojice pozic, které se „předběhly“, a počítá se jich víc. *Inverzní permutace* $\pi^{-1}$ je jedna permutace, která přeházení vrátí. Jméno je stejné náhodou.

> [!definice] Definice · pozn. 9.15
> Permutace, která prohazuje dva prvky a žádné jiné nemění, se nazývá *transpozice*.

^def-transpozice-permutace

> [!lidsky] Lidsky
> Nejjednodušší možné přeházení: dva prvky si vymění místa, zbytek stojí. Každá transpozice je **lichá** permutace (pozorování 9.16).

> [!example] Příklad
> V $S_4$ je $(1\ 3\ 2\ 4)$ transpozice prohazující 2 a 3: jediná inverze $(2, 3)$, lichá. $(3\ 2\ 1)$ v $S_3$ prohazuje 1 a 3 a má inverze $(1, 2)$, $(1, 3)$, $(2, 3)$, tedy 3: také lichá. Nepříklad: $(2\ 3\ 1)$ mění všechny tři prvky, transpozice není.

> [!veta] Věta 9.17 a věta 9.18
> ==Pro $\pi, \sigma \in S_n$== platí **$\operatorname{sgn}(\pi\sigma) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\sigma$** a **$\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$**.
>
> > [!note]- Důkaz
> > První tvrzení se zde nedokazuje. Druhé z něj plyne: $1 = \operatorname{sgn}\mathrm{id} = \operatorname{sgn}(\pi\pi^{-1}) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\pi^{-1}$, takže $\operatorname{sgn}\pi^{-1} = (\operatorname{sgn}\pi)^{-1} = \operatorname{sgn}\pi$, protože $\pm 1$ je samo sobě převrácenou hodnotou. (Jinak: $(i, j)$ je inverze v $\pi$, právě když $(\pi(j), \pi(i))$ je inverze v $\pi^{-1}$, takže mají stejný počet inverzí.)

^veta-znamenko-slozeni

> [!lidsky] Lidsky
> Znaménka se při skládání **násobí** jako $\pm 1$: sudá ∘ sudá a lichá ∘ lichá je sudá, sudá ∘ lichá je lichá. Jinými slovy $\operatorname{sgn} : S_n \to (\{\pm 1\}, \cdot)$ je homomorfismus grup. Speciálně složení s transpozicí **otočí znaménko**.

> [!example] Příklad
> $\pi = (2\ 3\ 1)$ (sudá) a transpozice $\sigma = (2\ 1\ 3)$ (lichá): $(\pi\sigma)(i) = \pi(\sigma(i))$ dá $\pi\sigma = (3\ 2\ 1)$ se 3 inverzemi, tedy lichá, a opravdu $(+1)(-1) = -1$. $\pi = (3\ 1\ 4\ 2)$ i $\pi^{-1} = (2\ 4\ 1\ 3)$ mají po 3 inverzích.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč po úpravách $(A \mid E) \sim \dots \sim (E \mid X)$ je $X = A^{-1}$?
> Každý sloupec za čarou je řešení soustavy $A\vec{x} = \vec{e}_j$, tedy **$A^{-1}\vec{e}_j$ = $j$-tý sloupec $A^{-1}$**. Maticově: úpravy jsou násobení $T$ zleva, $T(A \mid E) = (TA \mid T)$, a z $TA = E$ plyne **$T = A^{-1}$**.

> [!karta|02]- Jak při výpočtu $(A \mid E) \sim \dots$ poznáš, že $A$ inverzi nemá?
> Vlevo vznikne **nulový řádek** (méně než $n$ pivotů), takže $\operatorname{rank} A < n$ a $A$ není regulární. Některá soustava $A\vec{x} = \vec{e}_j$ pak nemá řešení: řádek $(0 \cdots 0 \mid \ast)$ má vpravo aspoň jedno nenulové číslo.

> [!karta|03]- Dokaž, že pro regulární $A$ převede eliminace $(A \mid B)$ na $(E \mid A^{-1}B)$.
> Úpravy jsou násobení regulární maticí $T$ zleva a působí na obě části stejně: **$T(A \mid B) = (TA \mid TB)$**. Vlevo vznikne $E$, takže $TA = E$, tedy $T = A^{-1}$, a vpravo je **$TB = A^{-1}B$**.

> [!karta|04]- Dokaž, že elementární řádkové úpravy zachovávají hodnost matice.
> Upravená matice je $B = TA$ s **regulární $T$**. Zobrazení $\vec{y} \mapsto T\vec{y}$ je prosté, i zúžené na $\operatorname{im} A$, a jeho obraz je $\operatorname{im}(TA)$. Prosté zobrazení má nulový defekt, takže podle **věty o dimenzi** $\dim \operatorname{im} A = \dim \operatorname{im}(TA)$.

> [!karta|05]- Dokaž, že $(AB)^{\mathsf{T}} = B^{\mathsf{T}}A^{\mathsf{T}}$.
> Porovnej prvky: $[(AB)^{\mathsf{T}}]_{ij} = [AB]_{ji} = \sum_k a_{jk}b_{ki} = \sum_k [B^{\mathsf{T}}]_{ik}[A^{\mathsf{T}}]_{kj} = [B^{\mathsf{T}}A^{\mathsf{T}}]_{ij}$. Rozměry obou stran jsou $p \times m$.

> [!karta|06]- Proč obecně neplatí $(AB)^{\mathsf{T}} = A^{\mathsf{T}}B^{\mathsf{T}}$?
> **Rozměry:** pro $A \in \mathbb{F}^{m \times n}$, $B \in \mathbb{F}^{n \times p}$ je $A^{\mathsf{T}}B^{\mathsf{T}}$ součin $(n \times m)(p \times n)$, definovaný jen pro $m = p$. I u čtvercových matic to obecně neplatí, protože **násobení matic není komutativní**: $(AB)^{\mathsf{T}} = B^{\mathsf{T}}A^{\mathsf{T}}$ a $B^{\mathsf{T}}A^{\mathsf{T}} \ne A^{\mathsf{T}}B^{\mathsf{T}}$.

> [!karta|07]- Dokaž, že $\operatorname{rank} A \le \min\{m, n\}$ pro $A \in \mathbb{F}^{m \times n}$.
> $\operatorname{im} A \le \mathbb{F}^m$, takže **$\operatorname{rank} A \le m$**. Podle věty o hodnosti transponované matice je $\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}}$ a $\operatorname{im} A^{\mathsf{T}} \le \mathbb{F}^n$, takže **$\operatorname{rank} A \le n$**. (Bez transpozice: $\operatorname{rank} A = n - \operatorname{def} A \le n$.)

> [!karta|08]- Uveď čtyři podmínky ekvivalentní s tím, že čtvercová matice $A \in \mathbb{F}^{n \times n}$ je regulární.
> - $A\vec{x} = \vec{b}$ má **právě jedno řešení** (pro dané $\vec{b}$; ekvivalentně $A\vec{x} = \vec{0}$ jen nulové),
> - **$\operatorname{rank} A = n$**,
> - **sloupce** $A$ jsou LN,
> - **řádky** $A$ jsou LN.

> [!karta|09]- Proč má čtvercová matice lineárně nezávislé řádky, právě když má lineárně nezávislé sloupce?
> $n$ řádků je LN $\Leftrightarrow$ $\operatorname{rank} A^{\mathsf{T}} = n$ a $n$ sloupců je LN $\Leftrightarrow$ $\operatorname{rank} A = n$. Obojí je totéž, protože **$\operatorname{rank} A = \operatorname{rank} A^{\mathsf{T}}$**. Pro obdélníkovou matici to neplatí.

> [!karta|10]- Uveď příklad grupy, která není abelovská, a zdůvodni to.
> **Regulární matice $2 \times 2$ s násobením** ($GL(2, \mathbb{R})$): je to grupa (součin regulárních je regulární, $E$ neutrální, inverzní matice), ale $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \ne \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ = součin v opačném pořadí. Jiný příklad: permutace $S_3$ se skládáním.

> [!karta|11]- Dokaž, že homomorfismus grup $\varphi : G \to H$ zobrazí neutrální prvek na neutrální prvek.
> $\varphi(e) = \varphi(e \cdot e) = \varphi(e)\varphi(e)$. Vynásob obě strany zleva **$\varphi(e)^{-1}$** (v $H$ existuje): $e_H = \varphi(e)$.

> [!karta|12]- Jaký je rozdíl mezi inverzí v permutaci a inverzní permutací?
> **Inverze v permutaci** $\pi$ je dvojice $(i, j)$ s $i < j$ a $\pi(i) > \pi(j)$; počítá se jich počet kvůli znaménku. **Inverzní permutace** $\pi^{-1}$ je permutace, která $\pi$ vrátí ($\pi^{-1}\pi = \mathrm{id}$). Společné mají jen jméno.

> [!karta|13]- Proč má permutace $\pi$ stejné znaménko jako $\pi^{-1}$?
> $1 = \operatorname{sgn}\mathrm{id} = \operatorname{sgn}(\pi\pi^{-1}) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\pi^{-1}$ (**znaménka se při skládání násobí**). Znaménko je $\pm 1$ a to je samo sobě převrácenou hodnotou, takže $\operatorname{sgn}\pi^{-1} = \operatorname{sgn}\pi$.

### Příklady na procvičení

> [!priklad|14]- Eliminací $(A \mid E)$ najdi inverzi $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.
> $\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right) \sim \left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & -2 & 1 \end{array}\right) \sim \left(\begin{array}{cc|cc} 1 & 1 & -2 & 1 \\ 2 & 1 & 1 & 0 \end{array}\right) \sim \left(\begin{array}{cc|cc} 1 & 1 & -2 & 1 \\ 0 & -1 & 5 & -2 \end{array}\right) \sim \left(\begin{array}{cc|cc} 1 & 0 & 3 & -1 \\ 0 & 1 & -5 & 2 \end{array}\right)$
>
> ($r_2 - 2r_1$, prohodit, $r_2 - 2r_1$, pak $r_2 \cdot (-1)$ a $r_1 - r_2$). **$A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$**; kontrola $AA^{-1} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = E$.

> [!priklad|15]- Najdi inverzi $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$.
> $(A \mid E)$: $r_3 - r_1$ dá $(0\ 1\ 0 \mid -1\ 0\ 1)$, $r_3 - r_2$ dá $(0\ 0\ {-1} \mid -1\ {-1}\ 1)$, $r_3 \cdot (-1)$ dá $(0\ 0\ 1 \mid 1\ 1\ {-1})$. Nahoru: $r_2 - r_3$ dá $(0\ 1\ 0 \mid -1\ 0\ 1)$, $r_1 - r_3$ dá $(1\ 0\ 0 \mid 0\ {-1}\ 1)$.
>
> **$A^{-1} = \begin{pmatrix} 0 & -1 & 1 \\ -1 & 0 & 1 \\ 1 & 1 & -1 \end{pmatrix}$.**

> [!priklad|16]- Napiš matici $T \in \mathbb{R}^{3 \times 3}$, která prohodí 2. a 3. řádek, a spočítej $TX$ pro $X = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$.
> Prohoď 2. a 3. řádek jednotkové matice: **$T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$**, **$TX = \begin{pmatrix} 1 & 2 \\ 5 & 6 \\ 3 & 4 \end{pmatrix}$**. Platí $T^2 = E$, takže $T^{-1} = T$: druhé prohození vše vrátí.

> [!priklad|17]- Rozhodni, které z $(\mathbb{Z}, \cdot)$, $(\mathbb{Q} \setminus \{0\}, \cdot)$, $(\mathbb{Z}, -)$ a $(2\mathbb{Z}, +)$ jsou grupy.
> - $(\mathbb{Z}, \cdot)$ **ne**: $2$ nemá inverzi, $\tfrac{1}{2} \notin \mathbb{Z}$.
> - $(\mathbb{Q} \setminus \{0\}, \cdot)$ **ano**, abelovská: neutrální $1$, inverze k $\tfrac{p}{q}$ je $\tfrac{q}{p}$.
> - $(\mathbb{Z}, -)$ **ne**: není asociativní, $(1 - 2) - 3 = -4 \ne 2 = 1 - (2 - 3)$.
> - $(2\mathbb{Z}, +)$ **ano**, abelovská (podgrupa $(\mathbb{Z}, +)$): neutrální $0$, opačné k sudému je sudé.

> [!priklad|18]- Spočítej v $\mathbb{Z}_{12}$: $[9] + [5]$, $-[5]$ a $[7] + [8] + [10]$.
> $[9] + [5] = [14] = $ **$[2]$**; $-[5] = [-5] = $ **$[7]$** (kontrola $[5] + [7] = [0]$); $[7] + [8] + [10] = [25] = $ **$[1]$** ($25 = 2 \cdot 12 + 1$).

> [!priklad|19]- Urči všechny inverze a znaménko permutace $\pi = (4\ 1\ 3\ 2)$ a znaménko $\pi^{-1}$.
> Dvojice $(i, j)$ s $\pi(i) > \pi(j)$: $(1, 2)$ ($4 > 1$), $(1, 3)$ ($4 > 3$), $(1, 4)$ ($4 > 2$), $(3, 4)$ ($3 > 2$). **4 inverze, $\operatorname{sgn}\pi = 1$, sudá.** $\pi^{-1} = (2\ 4\ 3\ 1)$ má inverze $(1, 4)$, $(2, 3)$, $(2, 4)$, $(3, 4)$, také **4, $\operatorname{sgn}\pi^{-1} = 1$**.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|20]- V $\mathbb{R}^{\le 2}[x]$ jsou báze $\mathcal{B} = (1, x, x^2)$ a $\mathcal{C} = (1 + x,\ x,\ x^2 + 2x + 1)$. Najdi $T_{\mathcal{C} \to \mathcal{B}}$, $T_{\mathcal{B} \to \mathcal{C}}$ a souřadnice $3 + 5x + 2x^2$ vůči $\mathcal{C}$.
> **$T_{\mathcal{C} \to \mathcal{B}}$** má ve sloupcích souřadnice vektorů $\mathcal{C}$ v bázi $\mathcal{B}$: $\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$. **$T_{\mathcal{B} \to \mathcal{C}} = T_{\mathcal{C} \to \mathcal{B}}^{-1}$**: v $(T \mid E)$ udělej $r_2 - r_1$, $r_1 - r_3$, $r_2 - r_3$, vyjde $\begin{pmatrix} 1 & 0 & -1 \\ -1 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}$.
>
> Souřadnice: $T_{\mathcal{B} \to \mathcal{C}}(3; 5; 2) = (3 - 2;\ -3 + 5 - 2;\ 2) =$ **$(1; 0; 2)$**. Kontrola: $1 \cdot (1 + x) + 2(x^2 + 2x + 1) = 3 + 5x + 2x^2$. ✓

> [!priklad|21]- Pro $A : \mathbb{R}^2 \to \mathbb{R}^2$, $A\vec{x} = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}\vec{x}$, a bázi $\mathcal{X} = \big((1; 1), (1; 2)\big)$ najdi $[A]^{\mathcal{X} \to \mathcal{X}}$.
> $[A]^{\mathcal{X} \to \mathcal{X}} = X^{-1}AX$, kde $X = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ má ve sloupcích bázi. $AX = \begin{pmatrix} 3 & 5 \\ 3 & 6 \end{pmatrix}$ a eliminace $(X \mid AX)$: $r_2 - r_1$ dá $(0\ 1 \mid 0\ 1)$, $r_1 - r_2$ dá $(1\ 0 \mid 3\ 4)$.
>
> **$[A]^{\mathcal{X} \to \mathcal{X}} = \begin{pmatrix} 3 & 4 \\ 0 & 1 \end{pmatrix}$.** Kontrola: $A(1; 1) = (3; 3) = 3(1; 1) + 0(1; 2)$, $A(1; 2) = (5; 6) = 4(1; 1) + 1(1; 2)$. ✓

> [!priklad|22]- Ověř jakýmkoli způsobem, že pro báze $\mathcal{X} = \big((1; 2), (1; 3)\big)$ a $\mathcal{Y} = \big((1; 0), (1; 1)\big)$ prostoru $\mathbb{R}^2$ je $T_{\mathcal{X} \to \mathcal{Y}} = \begin{pmatrix} -1 & -2 \\ 2 & 3 \end{pmatrix}$.
> Sloupce $T_{\mathcal{X} \to \mathcal{Y}}$ mají být souřadnice vektorů $\mathcal{X}$ v bázi $\mathcal{Y}$, tedy musí platit $Y \cdot T = X$ (matice s bázemi ve sloupcích): $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} -1 & -2 \\ 2 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix} = X$. ✓ Po sloupcích: $-1 \cdot (1; 0) + 2(1; 1) = (1; 2)$ a $-2(1; 0) + 3(1; 1) = (1; 3)$.
>
> **Ano, daná matice je $T_{\mathcal{X} \to \mathcal{Y}}$.**

---
← [[LAG 12 – Frobeniova věta a Gaussova eliminace|4. 11. 2026 Frobeniova věta a Gaussova eliminace]]

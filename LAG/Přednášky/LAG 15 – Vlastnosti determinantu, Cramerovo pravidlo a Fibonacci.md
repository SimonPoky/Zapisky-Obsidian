---
predmet: LAG
prednaska: 15
datum: 2026-11-13
zdroj: "pozn. 10.11 až 10.27, pozn. 11.1 a 11.20; příklad 8.33*"
tags: [prednaska, LAG]
---

# LAG 15 – Vlastnosti determinantu, Cramerovo pravidlo a Fibonacci

*Přednáška 15 · pátek 13. 11. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `det není lineární, ale multilineární` · `det(αA) = αⁿ det A` · `regulární ⟺ det A ≠ 0` · `výpočet determinantu 4 × 4` · `det(AB) = det A · det B` · `det A⁻¹ = (det A)⁻¹` · `geometrický význam determinantu` · `determinant operátoru` · `adjungovaná matice` · `Cramerovo pravidlo` · `Fibonacciho rekurence` · `zlatý řez` · `diagonální matice` · `motivace vlastních čísel`

Minule jsme determinant definovali a naučili se ho počítat rozvojem a eliminací. Dnes jsme zjistili, které vlastnosti má: v každém sloupci zvlášť je lineární, pozná regularitu a „slučuje se“ s násobením matic. Geometricky říká, kolikrát zobrazení zvětší obsah či objem. Z rozvoje vyšel vzorec pro inverzní matici a Cramerovo pravidlo pro soustavy. Na konci jsme lineární algebrou spočítali vzorec pro Fibonacciho čísla a ukázali, proč nás budou zajímat vektory, které matice jen natáhne: vlastní vektory.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| multilineární zobrazení | lineární v každém argumentu zvlášť | $f(x, y) = xy$ |
| multilinearita determinantu | $\det$ je lineární v každém sloupci (i řádku) zvlášť | $\det(\alpha A) = \alpha^n \det A$ |
| věta o regularitě a determinantu | $A$ regulární $\Leftrightarrow$ $\det A \neq 0$ | $\det\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 0$ |
| věta o determinantu součinu | $\det(AB) = \det A \det B$ | $\det(A^3) = (\det A)^3$ |
| determinant inverzní matice | $\det A^{-1} = (\det A)^{-1}$ | $\det A = 2 \Rightarrow \det A^{-1} = \frac{1}{2}$ |
| geometrický význam determinantu | $\lvert\det A\rvert$ = kolikrát se zvětší obsah, znaménko = orientace | čtverec $\to$ rovnoběžník o obsahu $5$ |
| determinant lineárního operátoru | $\det A = \det [A]^{\mathcal{X}}$, nezávisí na bázi | posun $p(x) \mapsto p(x + 1)$: $\det = 1$ |
| adjungovaná matice ♥ | na pozici $(i, j)$ je doplněk pozice $(j, i)$ | $\operatorname{adj}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ |
| inverzní matice pomocí adjungované matice | $A^{-1} = \frac{1}{\det A}\operatorname{adj} A$ | |
| Cramerovo pravidlo | $x_i = \det A^{(i)} / \det A$ | $2x + y = 5$, $x + 3y = 10$: $x = 1$, $y = 3$ |
| lineární rekurentní rovnice | $a_{n+2} = a_{n+1} + a_n$; řešení tvoří podprostor dimenze 2 | Fibonacci $0, 1, 1, 2, 3, 5, \dots$ |
| zlatý řez | kořeny $\lambda^2 - \lambda - 1 = 0$: $\varphi_\pm = \frac{1 \pm \sqrt{5}}{2}$ | $\varphi_+ \approx 1{,}618$ |
| Binetův vzorec | $a_n = \frac{1}{\sqrt{5}}(\varphi_+^n - \varphi_-^n)$ | $a_{10} = 55$ |
| diagonální matice | mimo diagonálu nuly; součin a mocniny po prvcích | $\operatorname{diag}(2, 3)^n = \operatorname{diag}(2^n, 3^n)$ |

## §1 Determinant není lineární, ale multilineární

Minule se ukázalo, že [[determinant]] jako zobrazení $\mathbb{F}^{n \times n} \to \mathbb{F}$ lineární není: $\det(2E_2) = 4$, ne $2$. Přesto se s ním dá počítat „lineárně“, jen opatrněji: po jednom sloupci.

> [!definice] Definice · pozn. 10.11\*
> Buďte $V$, $W$ lineární prostory nad $\mathbb{F}$. Zobrazení $f : V \times \cdots \times V \to W$ ($n$ argumentů) se nazývá *multilineární*, jestliže pro každé $i = 1, \dots, n$ a každou volbu $\vec{a}_1, \dots, \vec{a}_{i-1}, \vec{a}_{i+1}, \dots, \vec{a}_n \in V$ je zobrazení
>
> $$
> \vec{x} \mapsto f(\vec{a}_1, \dots, \vec{a}_{i-1}, \vec{x}, \vec{a}_{i+1}, \dots, \vec{a}_n)
> $$
>
> [[lineární zobrazení|lineární]]. Pro $n = 2$ jde o [[bilineární zobrazení]].

^def-multilinearni-zobrazeni

> [!lidsky] Lidsky
> Všechny proměnné kromě jedné „zmrazíš“ a v té jedné musí být zobrazení lineární: součet se rozdělí, násobek se vytkne. Lineární ve všech proměnných **naráz** být nemusí, a obvykle není.

> [!example] Příklad
> $f(x, y) = xy$ na $\mathbb{R} \times \mathbb{R}$: pro pevné $y = 3$ je $x \mapsto 3x$ lineární, stejně pro pevné $x$. Je tedy multilineární, ale ne lineární: $f(2 \cdot (1, 1)) = f(2, 2) = 4$, kdežto $2f(1, 1) = 2$.
>
> Nepříklad: $g(x, y) = x + y$ multilineární není, protože pro $y = 3$ je $x \mapsto x + 3$ posunutí, které nulu nepošle na nulu.

> [!veta] Věta 10.12\*
> ==Buď $n \in \mathbb{N}$.== Zobrazení $(\vec{a}_1, \dots, \vec{a}_n) \mapsto \det(\vec{a}_1 \cdots \vec{a}_n)$, které $n$ sloupcům z $\mathbb{F}^n$ přiřadí determinant matice z nich složené, **je multilineární**:
>
> $$
> \det(\vec{a}_1 \cdots \vec{a}_i + \alpha\vec{a}_i' \cdots \vec{a}_n) = \det(\vec{a}_1 \cdots \vec{a}_i \cdots \vec{a}_n) + \alpha\det(\vec{a}_1 \cdots \vec{a}_i' \cdots \vec{a}_n).
> $$
>
> Protože $\det A^{\mathsf{T}} = \det A$, platí totéž pro řádky. Důsledek: **$\det(\alpha A) = \alpha^n \det A$** pro $A \in \mathbb{F}^{n \times n}$.
>
> > [!note]- Důkaz
> > Rozviň determinant podle $i$-tého sloupce ([[rozvoj determinantu]], věta 10.10): $\det(\vec{a}_1 \cdots \vec{x} \cdots \vec{a}_n) = \sum_{k=1}^{n} x_k D_{ki}$. [[algebraický doplněk|Algebraické doplňky]] $D_{ki}$ $i$-tý sloupec vůbec nepoužívají, takže pro zmrazené ostatní sloupce jsou to konstanty. Zobrazení $\vec{x} \mapsto \sum_k D_{ki}x_k$ je součin řádku $(D_{1i} \cdots D_{ni})$ se sloupcem $\vec{x}$, tedy lineární (pozn. 6.6). Pro $\alpha A$ vytkneš $\alpha$ z každého z $n$ sloupců zvlášť.

^veta-multilinearita

> [!lidsky] Lidsky
> Determinant se chová lineárně **v jednom sloupci**, když ostatní stojí. Obsah rovnoběžníku se stejnou základnou $\vec{a}$ je základna krát výška, a výšky se sčítají: $\det(\vec{a}, \vec{b} + \vec{b}') = \det(\vec{a}, \vec{b}) + \det(\vec{a}, \vec{b}')$. Když ale vynásobíš celou matici, vytkne se číslo z **každého** sloupce, proto $\alpha^n$.

> [!example] Příklad
> Rozdělení druhého sloupce: $\det\begin{pmatrix} 1 & 2 + 3 \\ 4 & 1 + 0 \end{pmatrix} = \det\begin{pmatrix} 1 & 2 \\ 4 & 1 \end{pmatrix} + \det\begin{pmatrix} 1 & 3 \\ 4 & 0 \end{pmatrix} = -7 - 12 = -19$, a přímo $1 \cdot 1 - 5 \cdot 4 = -19$. ✓
>
> Násobek celé matice: pro $A \in \mathbb{R}^{3 \times 3}$ s $\det A = 5$ je $\det(-2A) = (-2)^3 \cdot 5 = -40$, ne $-10$.

> [!obrazek] Multilinearita jako sčítání výšek
> ![[lag15-multilinearita.png]]
> *Všechny tři rovnoběžníky mají společnou základnu $\vec{a} = (3; 0)$. Modrý ($\vec{a}$, $\vec{b}$) má výšku $1$, zelený ($\vec{a}$, $\vec{b}'$) výšku $1{,}5$, oranžový čárkovaný ($\vec{a}$, $\vec{b} + \vec{b}'$) výšku $2{,}5$: jeho obsah $7{,}5$ je součet modrého a zeleného.*

### Přičtení násobku sloupce determinant nezmění

Z multilinearity jde znovu odvodit třetí bod [[věta o determinantu a řádkových úpravách|věty o determinantu a řádkových úpravách]] (věta 10.16). Přičteme-li k $l$-tému sloupci $\alpha$-násobek $k$-tého ($k \neq l$), je podle multilinearity v $l$-tém sloupci

$$
\det(\cdots \vec{a}_l + \alpha\vec{a}_k \cdots) = \det A + \alpha\det(\cdots \vec{a}_k \cdots \vec{a}_k \cdots),
$$

kde druhá matice má na místech $k$ i $l$ tentýž sloupec $\vec{a}_k$. Stačí tedy vědět, že **matice se dvěma stejnými sloupci má determinant $0$**.

> [!note]- Důkaz: dva stejné sloupce dávají determinant 0
> Buď $B$ matice, jejíž $k$-tý a $l$-tý sloupec jsou stejné, a $\tau$ [[transpozice (permutace)|transpozice]] prohazující $k$ a $l$. Podle pozn. 10.6 ($\det B = \det B^{\mathsf{T}}$) je
>
> $$
> \det B = \sum_{\pi \in S_n} \operatorname{sgn}\pi \cdot b_{\pi(1)1}b_{\pi(2)2} \cdots b_{\pi(n)n}.
> $$
>
> Spárujeme permutace $\pi$ a $\pi \circ \tau$. Sčítanec pro $\pi \circ \tau$ se od sčítance pro $\pi$ liší jen ve sloupcích $k$ a $l$: místo $b_{\pi(k)k}b_{\pi(l)l}$ obsahuje $b_{\pi(l)k}b_{\pi(k)l}$. Protože sloupce $k$ a $l$ jsou stejné, je $b_{\pi(l)k} = b_{\pi(l)l}$ a $b_{\pi(k)l} = b_{\pi(k)k}$, takže **součiny jsou stejné**. Znaménka jsou opačná: $\operatorname{sgn}(\pi \circ \tau) = \operatorname{sgn}\pi \cdot \operatorname{sgn}\tau = -\operatorname{sgn}\pi$ ([[věta o znaménku složené permutace]]). Zobrazení $\pi \mapsto \pi \circ \tau$ je bijekce $S_n \to S_n$, která je sama sobě inverzí a nemá pevný bod ($\pi \circ \tau \neq \pi$), takže rozdělí $S_n$ na dvojice $\{\pi, \pi \circ \tau\}$. V každé dvojici se sčítance odečtou, a proto **$\det B = 0$**, nad každým tělesem.

> [!pozor] Argument „prohodím stejné sloupce“ nestačí všude
> Rychlá úvaha zní: prohození dvou sloupců otočí znaménko, ale prohození dvou **stejných** sloupců matici nezmění, takže $\det B = -\det B$, tedy $2\det B = 0$. Z toho plyne $\det B = 0$ jen tehdy, když smíš dělit dvěma, tj. když $1 + 1 \neq 0$. To platí v každém [[číselné těleso|číselném tělese]], ale ne v tělese $\mathbb{Z}_2$ ([[grupa zbytkových tříd|zbytkové třídy]] mod 2), kde $1 + 1 = 0$ a $-1 = 1$: tam prohození sloupců determinant nemění vůbec a rovnost $\det B = -\det B$ neříká nic. Párování $\pi \leftrightarrow \pi \circ \tau$ výše funguje i tam, protože sčítance se ruší ve dvojicích.

## §2 Regularita a výpočet determinantu

> [!veta] Věta 10.18
> ==Buď $A \in \mathbb{F}^{n \times n}$.== Potom **$A$ je [[regulární matice|regulární]], právě když $\det A \neq 0$.**
>
> > [!note]- Důkaz
> > [[Gaussova eliminace|Gaussovou eliminací]] převeď $A$ na [[horní trojúhelníková matice|horní trojúhelníkovou]] matici $B$. Řádkové úpravy zachovávají regularitu ($B = TA$ s regulární $T$) a determinant mění jen **nenulovým násobkem**: prohození řádků ho vynásobí $-1$, vynásobení řádku číslem $\alpha \neq 0$ ho vynásobí $\alpha$, přičtení násobku jiného řádku ho nezmění (věta 10.16). Tedy $\det A \neq 0 \Leftrightarrow \det B \neq 0$. Pro trojúhelníkovou $B$ je $\det B$ součin diagonály (pozorování 10.15) a $B$ je regulární, právě když na diagonále nejsou nuly. Obojí je tedy totéž.

^veta-regularita

> [!lidsky] Lidsky
> Jedno číslo rozhodne o všem, co [[věta o charakterizaci regulární matice]] dává do ekvivalence: nenulový determinant znamená LN sloupce, plnou hodnost, jediné řešení každé soustavy a existenci inverze. Nulový determinant znamená, že zobrazení $\vec{x} \mapsto A\vec{x}$ „zplacatí“ prostor do menší dimenze.

> [!example] Příklad
> $\det\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix} = 6 - 1 = 5 \neq 0$, matice je regulární. $\det\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = 0$, matice je [[singulární matice|singulární]]: třetí sloupec je $2 \cdot$ druhý $-$ první.

### Výpočet determinantu $4 \times 4$ (cvičení 10.13 a 10.17)

U větší matice se vyplatí kombinovat obě metody: **rozvíjet podle řádku nebo sloupce s nejvíce nulami**, a když žádný takový není, nuly si nejdřív **vyrobit řádkovými úpravami**.

> [!example] Příklad: rozvoj podle řídkého sloupce
> $$
> X = \begin{pmatrix} 2 & 0 & 1 & 3 \\ 1 & 0 & 0 & 2 \\ 0 & 4 & 1 & 1 \\ 3 & 0 & 2 & 1 \end{pmatrix}.
> $$
>
> Ve 2. sloupci je jediné nenulové číslo $4$ na pozici $(3, 2)$ se znaménkem $(-1)^{3+2} = -1$. Vynecháním 3. řádku a 2. sloupce zbude matice $3 \times 3$, kterou rozvineme podle 1. řádku:
>
> $$
> \det X = -4 \begin{vmatrix} 2 & 1 & 3 \\ 1 & 0 & 2 \\ 3 & 2 & 1 \end{vmatrix} = -4\big(2(0 - 4) - 1(1 - 6) + 3(2 - 0)\big) = -4 \cdot 3 = -12.
> $$

> [!example] Příklad: eliminace
> $$
> Y = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 5 & 1 & 3 \\ 0 & 1 & 3 & 2 \\ 1 & 3 & 2 & 4 \end{pmatrix}
> \sim
> \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 3 & 2 \\ 0 & 1 & 2 & 3 \end{pmatrix}
> \sim
> \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 1 & 2 \end{pmatrix}
> \sim
> \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & \tfrac{3}{2} \end{pmatrix}
> $$
>
> ($r_2 - 2r_1$, $r_4 - r_1$; $r_3 - r_2$, $r_4 - r_2$; $r_4 - \tfrac{1}{2}r_3$). Jen přičítání násobků, determinant se nezměnil: $\det Y = 1 \cdot 1 \cdot 2 \cdot \tfrac{3}{2} = 3$.

> [!pozor] Úpravy, které determinant mění
> Prohození řádků otočí znaménko a vynásobení řádku číslem $\alpha$ násobí determinant $\alpha$. Častá chyba: „$r_2 \to 2r_2 - r_1$“ je ve skutečnosti dvě úpravy, a determinant se tím **zdvojnásobí**. Kdo chce mít klid, přičítá jen násobky jiných řádků k řádku, který se nemění násobkem.

## §3 Determinant součinu a inverzní matice

> [!veta] Věta 10.19
> ==Buďte $A, B \in \mathbb{F}^{n \times n}$.== Potom **$\det(AB) = \det A \cdot \det B$**.
>
> > [!note]- Důkaz\*
> > Pro [[matice elementární řádkové úpravy|matici elementární úpravy]] $T$ je $TB$ matice $B$ po té úpravě, takže $\det(TB) = \det T \cdot \det B$, kde $\det T$ je $-1$ (prohození), $\alpha$ (násobení) nebo $1$ (přičtení): stačí úpravu provést s $E$. Je-li $A$ regulární, je součinem matic elementárních úprav, $A = T_1 \cdots T_l$ (Gaussova–Jordanova eliminace $A^{-1}$ na $E$), a opakováním dostaneme $\det(AB) = \det T_1 \cdots \det T_l \cdot \det B = \det A \cdot \det B$. Je-li $A$ singulární, je singulární i $AB$ (jinak by $A = (AB)B^{-1}$ nebo $\operatorname{im}(AB) \subseteq \operatorname{im} A \neq \mathbb{F}^n$), takže obě strany jsou $0$.

^veta-det-soucinu

> [!lidsky] Lidsky
> Determinant je „koeficient zvětšení“. Když nejdřív zvětšíš obsahy dvakrát a pak třikrát, zvětšil jsi je šestkrát. Proto se při skládání zobrazení (násobení matic) determinanty násobí. Řečeno algebraicky: $\det$ je [[homomorfismus grup]] z regulárních matic s násobením do $(\mathbb{F} \setminus \{0\}, \cdot)$, stejně jako [[znaménko permutace]] je homomorfismus $S_n \to \{\pm 1\}$ (pozn. 10.21\*).

> [!example] Příklad
> $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 3 & 3 \end{pmatrix}$ a $\det = 12 - 6 = 6 = 3 \cdot 2$. ✓ Mocniny: $\det(A^3) = (\det A)^3$. A protože součin čísel je nenulový, jen když jsou nenulové oba činitele, je $AB$ regulární, právě když jsou regulární $A$ i $B$.

> [!pozor] Se sčítáním se determinant neslučuje
> $\det(A + B) \neq \det A + \det B$ obecně. Pro $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ jsou oba determinanty $0$, ale $A + B = E_2$ má determinant $1$. Rozdělit se smí jen **jeden sloupec**, když ostatní zůstanou stejné (§1).

> [!veta] Věta 10.20
> ==Buď $A \in \mathbb{F}^{n \times n}$ regulární.== Potom **$\det A^{-1} = (\det A)^{-1}$**.
>
> > [!note]- Důkaz
> > $1 = \det E = \det(AA^{-1}) = \det A \cdot \det A^{-1}$ podle věty 10.19. Protože $A$ je regulární, je $\det A \neq 0$ a smíme jím dělit.

^veta-det-inverze

> [!lidsky] Lidsky
> [[inverzní matice|Inverze]] vrací zobrazení zpět, takže co původní zobrazení zvětšilo $k$-krát, inverze zmenší $k$-krát. Je to stejný trik jako u znaménka: $\operatorname{sgn}\pi^{-1} = (\operatorname{sgn}\pi)^{-1}$.

> [!example] Příklad
> $A = \begin{pmatrix} 4 & 3 \\ 2 & 2 \end{pmatrix}$, $\det A = 2$; $A^{-1} = \begin{pmatrix} 1 & -\tfrac{3}{2} \\ -1 & 2 \end{pmatrix}$ má $\det A^{-1} = 2 - \tfrac{3}{2} = \tfrac{1}{2}$. ✓

## §4 Geometrický význam determinantu

> [!veta] Pozn. 10.22 · Obsah a orientace
> ==Buď $A \in \mathbb{R}^{2 \times 2}$ (resp. $\mathbb{R}^{3 \times 3}$).== Potom **$\lvert\det A\rvert$ je obsah rovnoběžníku (objem rovnoběžnostěnu) určeného sloupci $A$**. Znaménko určuje orientaci: **$\det A > 0$**, právě když zobrazení $\vec{x} \mapsto A\vec{x}$ orientaci zachovává, **$\det A < 0$**, právě když ji převrací.
>
> > [!note]- Zdůvodnění
> > Pro horní trojúhelníkovou $A = \begin{pmatrix} a & b \\ 0 & c \end{pmatrix}$ (s $a, c > 0$) je rovnoběžník ze sloupců $(a; 0)$ a $(b; c)$ se základnou $a$ na ose $x$ a výškou $c$, obsah je $ac = \det A$. Obecnou matici převedeme sloupcovými úpravami „přičti násobek“ na trojúhelníkovou; takové úpravy posouvají vrchol rovnoběžníku rovnoběžně se základnou, takže obsah nemění, a determinant také ne. Prohození sloupců obrátí orientaci i znaménko.

^veta-geometricky-vyznam

> [!lidsky] Lidsky
> [[matice zobrazení v kanonické bázi|Sloupce matice]] jsou obrazy $\vec{e}_1$ a $\vec{e}_2$, takže jednotkový čtverec se zobrazí na rovnoběžník ze sloupců. Lineární zobrazení zvětší **každý** útvar stejným poměrem (útvar si poskládej z malých čtverečků), takže $\lvert\det A\rvert$ říká, kolikrát se zvětší libovolný obsah. Záporné znaménko je zrcadlo, nula je zplacatění do přímky.

> [!example] Příklad
> $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, $\det A = 5$: čtverec o obsahu $1$ přejde na rovnoběžník o obsahu $5$, kruh o obsahu $\pi$ na elipsu o obsahu $5\pi$. Zrcadlení $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ má determinant $-1$: obsah nemění, orientaci otočí. Zkosení $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ má determinant $1$, tvar mění, obsah ne.

> [!obrazek] Determinant jako zvětšení obsahu
> ![[lag15-obsah.png]]
> *Vlevo: modrý jednotkový čtverec a oranžový rovnoběžník ze sloupců $(2; 1)$, $(1; 3)$ o obsahu $5$. Uprostřed: modrý jednotkový kruh a jeho oranžový obraz, elipsa o obsahu $5\pi$. Vpravo: zelená kladně orientovaná dvojice $\vec{e}_1, \vec{e}_2$ (otočení doleva), červený obraz při zrcadlení, kde se od $A\vec{e}_1$ k $A\vec{e}_2$ otáčí doprava: $\det = -1$.*

> [!navic] Trojúhelník a objem
> Trojúhelník s vrcholy $\vec{0}$, $\vec{u}$, $\vec{v}$ je polovina rovnoběžníku, má obsah $\tfrac{1}{2}\lvert\det(\vec{u}\ \vec{v})\rvert$: pro $(3; 1)$, $(1; 2)$ je to $\tfrac{5}{2}$. V $\mathbb{R}^3$ dává $\lvert\det(\vec{u}\ \vec{v}\ \vec{w})\rvert$ objem rovnoběžnostěnu a $\tfrac{1}{6}$ z toho objem čtyřstěnu.

## §5 Determinant lineárního operátoru

> [!definice] Definice · pozn. 10.23
> Buď $L$ lineární prostor konečné [[dimenze]], $\mathcal{X}$ jeho [[báze]] a $A \in \operatorname{Lin}(L)$ [[lineární operátor]]. *Determinant operátoru* $A$ je
>
> $$
> \det A = \det [A]^{\mathcal{X}}.
> $$
>
> Tato hodnota **nezávisí na volbě báze** $\mathcal{X}$.
>
> > [!note]- Důkaz nezávislosti
> > Pro jinou bázi $\mathcal{Y}$ a [[matice přechodu|matici přechodu]] $T = [\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}$ je $[A]^{\mathcal{Y}} = T[A]^{\mathcal{X}}T^{-1}$. Podle vět 10.19 a 10.20:
> >
> > $$
> > \det[A]^{\mathcal{Y}} = \det T \cdot \det[A]^{\mathcal{X}} \cdot (\det T)^{-1} = \det[A]^{\mathcal{X}}.
> > $$

^def-det-operatoru

> [!lidsky] Lidsky
> Operátor na abstraktním prostoru (polynomy, funkce) žádnou matici nemá, dokud nezvolíš bázi. V různých bázích vyjdou různé [[matice lineárního operátoru v bázi|matice]], ale jejich determinant je pořád stejný: přechodové matice se vykrátí. Determinant je tedy vlastnost **zobrazení**, ne zápisu.

> [!example] Příklad
> Posun $P : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $p(x) \mapsto p(x + 1)$: v bázi $(1, x, x^2)$ je $P(1) = 1$, $P(x) = 1 + x$, $P(x^2) = 1 + 2x + x^2$, tedy
>
> $$
> [P] = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det P = 1.
> $$
>
> [[operátor derivace|Derivace]] $p \mapsto p'$ na témže prostoru má matici s nulovým prvním sloupcem ($1' = 0$), tedy $\det = 0$: derivace není regulární, konstanty pošle na nulu.

> [!pozor] Jen pro operátor
> Determinant má smysl pro zobrazení $L \to L$ s **jednou** bází na obou stranách. Pro $A : L \to W$ nebo pro matici $[A]^{\mathcal{X} \to \mathcal{Y}}$ se dvěma různými bázemi by výsledek na volbě bází záležel: třeba $[\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}$ je libovolná matice přechodu, ne $E$.

## §6 Adjungovaná matice a Cramerovo pravidlo

> [!definice] Definice · pozn. 10.24 ♥
> Buď $A \in \mathbb{F}^{n \times n}$ a $D_{ij} = (-1)^{i+j}\det A^{(i,j)}$ [[algebraický doplněk]] pozice $(i, j)$. *Adjungovaná matice* k $A$ je matice $\operatorname{adj} A \in \mathbb{F}^{n \times n}$, která má na pozici $(i, j)$ algebraický doplněk pozice $(j, i)$:
>
> $$
> [\operatorname{adj} A]_{ij} = D_{ji}.
> $$

^def-adjungovana

> [!lidsky] Lidsky
> Spočítáš všechny algebraické doplňky, zapíšeš je do matice na „jejich“ místa a celou matici [[transponovaná matice|transponuješ]]. Transpozice není rozmar: díky ní vyjde v součinu $\operatorname{adj}(A) \cdot A$ na diagonále rozvoj determinantu.

> [!example] Příklad
> Pro $2 \times 2$: $\operatorname{adj}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ (doplňky jsou $D_{11} = d$, $D_{12} = -c$, $D_{21} = -b$, $D_{22} = a$). Třeba $\operatorname{adj}\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}$.
>
> Pro $C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ vyjdou doplňky $D_{11} = 1$, $D_{12} = 1$, $D_{13} = -1$, $D_{21} = -2$, $D_{22} = 1$, $D_{23} = 2$, $D_{31} = 2$, $D_{32} = -1$, $D_{33} = 1$ a po transpozici
>
> $$
> \operatorname{adj} C = \begin{pmatrix} 1 & -2 & 2 \\ 1 & 1 & -1 \\ -1 & 2 & 1 \end{pmatrix}.
> $$

Lemma 10.25 je jen jinak zapsaný [[rozvoj determinantu]]: nahradíme-li $i$-tý sloupec $A$ vektorem $\vec{b}$, je determinant nové matice $\sum_k D_{ki}b_k$, protože doplňky $D_{ki}$ na $i$-tém sloupci nezávisí. Z toho jsou obě následující věty.

> [!veta] Věta 10.26
> ==Buď $A \in \mathbb{F}^{n \times n}$ regulární.== Potom
>
> $$
> \mathbf{A^{-1} = \frac{1}{\det A}\operatorname{adj} A}.
> $$
>
> > [!note]- Důkaz
> > Ukážeme $\operatorname{adj}(A) \cdot A = (\det A)E$. Prvek na pozici $(i, j)$ je $\sum_k [\operatorname{adj} A]_{ik}a_{kj} = \sum_k D_{ki}a_{kj}$, podle lemmatu 10.25 determinant matice, která vznikne z $A$ nahrazením $i$-tého sloupce $j$-tým sloupcem $\vec{a}_j$. Pro $i = j$ je to $A$ sama, prvek je $\det A$. Pro $i \neq j$ má ta matice **dva stejné sloupce** (na místech $i$ a $j$), prvek je $0$ (§1). Protože $\det A \neq 0$, je $\frac{1}{\det A}\operatorname{adj} A$ levá inverze, a u čtvercové matice tedy inverze.

^veta-inverze-adj

> [!lidsky] Lidsky
> Inverze má vzorec: adjungovaná matice vydělená determinantem. Pro $2 \times 2$ je to známé „prohoď diagonálu, změň znaménka mimo ni, vyděl $ad - bc$“ ([[vzorec pro inverzní matici 2 × 2]]). Pro větší matice je [[výpočet inverzní matice eliminací|eliminace]] rychlejší; vzorec je cenný v teorii a u matic s parametrem.

> [!example] Příklad
> Pro $C$ výše: rozvoj podle 1. řádku dá $\det C = 1 \cdot 1 + 2 \cdot 1 + 0 \cdot (-1) = 3$, takže
>
> $$
> C^{-1} = \frac{1}{3}\begin{pmatrix} 1 & -2 & 2 \\ 1 & 1 & -1 \\ -1 & 2 & 1 \end{pmatrix}.
> $$
>
> Kontrola prvního sloupce: $C \cdot \tfrac{1}{3}(1; 1; -1) = \tfrac{1}{3}(1 + 2;\ 1 - 1;\ 1 - 1) = (1; 0; 0)$. ✓

> [!veta] Věta 10.27 · Cramerovo pravidlo
> ==Buď $A \in \mathbb{F}^{n \times n}$ regulární a $\vec{b} \in \mathbb{F}^n$. Označme $A^{(i)}$ matici, která vznikne z $A$ nahrazením $i$-tého sloupce vektorem $\vec{b}$.== Potom jediné řešení soustavy $A\vec{x} = \vec{b}$ má složky
>
> $$
> \mathbf{x_i = \frac{\det A^{(i)}}{\det A}}, \qquad i = 1, \dots, n.
> $$
>
> > [!note]- Důkaz
> > $\vec{x} = A^{-1}\vec{b} = \frac{1}{\det A}\operatorname{adj}(A)\vec{b}$, takže $x_i = \frac{1}{\det A}\sum_k D_{ki}b_k$, a součet je podle lemmatu 10.25 přesně $\det A^{(i)}$.

^veta-cramer

> [!lidsky] Lidsky
> Každá neznámá je podíl dvou determinantů. Ve jmenovateli je vždy determinant [[matice soustavy]], v čitateli tatáž matice, jen sloupec „té“ neznámé vyměníš za pravou stranu.

> [!example] Příklad
> $2x + y = 5$, $x + 3y = 10$: $\det A = \begin{vmatrix} 2 & 1 \\ 1 & 3 \end{vmatrix} = 5$,
>
> $$
> x = \frac{1}{5}\begin{vmatrix} 5 & 1 \\ 10 & 3 \end{vmatrix} = \frac{5}{5} = 1, \qquad y = \frac{1}{5}\begin{vmatrix} 2 & 5 \\ 1 & 10 \end{vmatrix} = \frac{15}{5} = 3.
> $$
>
> Kontrola: $2 + 3 = 5$, $1 + 9 = 10$. ✓

> [!navic] Kdy Cramer a kdy eliminace (pozn. 10.28, cvičení 10.29)
> Determinant z definice má $n!$ sčítanců, eliminace potřebuje řádově $n^3$ operací, a Cramer chce $n + 1$ determinantů. Pro konkrétní čísla je tedy eliminace rychlejší. Cramer se hodí pro **soustavy s parametrem** a když chceš **jen jednu neznámou**. Třeba $\lambda x + y = 1$, $x + \lambda y = 1$: $\det A = \lambda^2 - 1 = (\lambda - 1)(\lambda + 1)$, pro $\lambda \neq \pm 1$ je
>
> $$
> x = \frac{1}{\lambda^2 - 1}\begin{vmatrix} 1 & 1 \\ 1 & \lambda \end{vmatrix} = \frac{\lambda - 1}{(\lambda - 1)(\lambda + 1)} = \frac{1}{\lambda + 1}
> $$
>
> a ze symetrie $y = \frac{1}{\lambda + 1}$. Pro $\lambda = 1$ jsou obě rovnice stejné (nekonečně mnoho řešení), pro $\lambda = -1$ si odporují ($-x + y = 1$ a $x - y = 1$).

> [!pozor] Jen pro čtvercové regulární soustavy
> Při $\det A = 0$ Cramerovo pravidlo **nic neříká**: soustava může mít nekonečně mnoho řešení i žádné. Pak rozhodne [[Frobeniova věta]] a eliminace.

## §7 Lineární rekurence: Fibonacciho čísla

Fibonacciho čísla (příklad 8.33\*, „rozmnožování králíků“) začínají $0, 1, 1, 2, 3, 5, 8, 13, \dots$ a každé další je součtem dvou předchozích. Spočítat $a_{100}$ krok za krokem jde, ale lineární algebra dá vzorec.

> [!definice] Definice · příklad 8.33\*
> Rovnost $a_{n+2} = a_{n+1} + a_n$ pro všechna $n \in \mathbb{N}_0$ chápeme jako nekonečnou soustavu lineárních rovnic pro neznámé $a_0, a_1, a_2, \dots$. Pro lineární zobrazení
>
> $$
> F : \mathbb{R}^{\mathbb{N}_0} \to \mathbb{R}^{\mathbb{N}_0}, \qquad (a_n) \mapsto (a_{n+2} - a_{n+1} - a_n)
> $$
>
> je to rovnice $F(a_n) = 0$, takže množina řešení je [[jádro]] $\ker F$, [[lineární podprostor]] prostoru [[posloupnosti|posloupností]]. Taková rovnice se nazývá *lineární rekurentní rovnice* (zde druhého řádu); její prostor řešení má **dimenzi 2**.
>
> > [!note]- Důkaz, že $\dim \ker F = 2$
> > **$\le 2$:** Řešení je jednoznačně určené dvojicí $(a_0, a_1)$, zbytek dopočítá rekurence. Vezmi tři řešení; jejich počáteční dvojice jsou tři vektory v $\mathbb{R}^2$, tedy [[lineární závislost|LZ]], a nějaká netriviální kombinace dá dvojici $(0, 0)$. Tatáž kombinace posloupností je (jádro je podprostor) zase řešení, a to s počátkem $0, 0$, tedy celá nulová. Tři řešení jsou vždy LZ.
> >
> > **$\ge 2$:** $(0, 1, 1, 2, 3, \dots)$ a $(1, 0, 1, 1, 2, \dots)$ jsou řešení s LN počátečními dvojicemi, tedy [[lineární nezávislost|LN]].

^def-linearni-rekurence

> [!lidsky] Lidsky
> Recept, který další člen spočítá jako lineární kombinaci předchozích. Součet dvou řešení i násobek řešení je zase řešení, takže řešení tvoří podprostor, a protože každé je určené prvními dvěma členy, má ten podprostor dimenzi 2. Stačí tedy najít **dvě** nezávislá řešení a všechna ostatní jsou jejich kombinace.

> [!example] Příklad
> $a_0 = 0$, $a_1 = 1$ dá Fibonacciho čísla $0, 1, 1, 2, 3, 5, 8, \dots$; $a_0 = 2$, $a_1 = 1$ dá Lucasova čísla $2, 1, 3, 4, 7, 11, \dots$, také řešení. Konstantní posloupnost $(1, 1, 1, \dots)$ řešením není: $1 - 1 - 1 = -1 \neq 0$.

**Hledání báze.** Rekurence prvního řádu $a_{n+1} = \lambda a_n$ má řešení $a_n = \lambda^n a_0$, zkusíme tedy $a_n = \lambda^n$ i tady. Dosazením $\lambda^{n+2} = \lambda^{n+1} + \lambda^n$ a vydělením $\lambda^n$ dostaneme

$$
\lambda^2 - \lambda - 1 = 0, \qquad \lambda = \varphi_\pm = \frac{1 \pm \sqrt{5}}{2}.
$$

> [!definice] Definice · příklad 8.33\*
> Kořeny rovnice $\lambda^2 - \lambda - 1 = 0$ jsou
>
> $$
> \varphi_+ = \frac{1 + \sqrt{5}}{2} \approx 1{,}618, \qquad \varphi_- = \frac{1 - \sqrt{5}}{2} \approx -0{,}618.
> $$
>
> Číslo $\varphi_+$ se nazývá *zlatý řez*. Platí $\varphi_\pm^2 = \varphi_\pm + 1$.

^def-zlaty-rez

> [!lidsky] Lidsky
> Zlatý řez je jediné kladné číslo, jehož druhá mocnina je o jedna větší než ono samo. Je to také číslo, ke kterému se blíží podíly sousedních Fibonacciho čísel: rekurence se „chová jako“ násobení $\varphi_+$.

> [!example] Příklad
> $\varphi_+^2 = \frac{1 + 2\sqrt{5} + 5}{4} = \frac{3 + \sqrt{5}}{2} \approx 2{,}618 = \varphi_+ + 1$. ✓ Podíly $\frac{13}{8} = 1{,}625$, $\frac{89}{55} \approx 1{,}6182$ se blíží $\varphi_+$. Součin kořenů je $\varphi_+\varphi_- = -1$ a součet $1$ (Vièteovy vztahy).

Posloupnosti $(\varphi_+^n)$ a $(\varphi_-^n)$ jsou dvě LN řešení, tedy báze prostoru řešení, a každé řešení je $a_n = \alpha\varphi_+^n + \beta\varphi_-^n$.

> [!veta] Příklad 8.33\* · Binetův vzorec
> ==Pro $a_0 = 0$, $a_1 = 1$, $a_{n+2} = a_{n+1} + a_n$== platí
>
> $$
> \mathbf{a_n = \frac{1}{\sqrt{5}}\big(\varphi_+^n - \varphi_-^n\big)} = \left[\frac{\varphi_+^n}{\sqrt{5}}\right],
> $$
>
> kde $[\,\cdot\,]$ je zaokrouhlení na nejbližší celé číslo.
>
> > [!note]- Odvození
> > Z $a_n = \alpha\varphi_+^n + \beta\varphi_-^n$: $a_0 = \alpha + \beta = 0$ a $a_1 = \alpha\varphi_+ + \beta\varphi_- = \alpha(\varphi_+ - \varphi_-) = \alpha\sqrt{5} = 1$, tedy $\alpha = \frac{1}{\sqrt{5}}$, $\beta = -\frac{1}{\sqrt{5}}$. Zaokrouhlení: $\lvert\varphi_-\rvert < 1$ a $\frac{1}{\sqrt{5}} < \frac{1}{2}$, takže $\left\lvert\frac{\varphi_-^n}{\sqrt{5}}\right\rvert < \frac{1}{2}$, a celé číslo $a_n$ je od $\frac{\varphi_+^n}{\sqrt{5}}$ vzdálené méně než $\frac{1}{2}$.

^veta-binet

> [!lidsky] Lidsky
> $n$-té Fibonacciho číslo dostaneš bez počítání předchozích: umocni zlatý řez, vyděl $\sqrt{5}$ a zaokrouhli. Druhý člen se zápornou bází je tak malý, že jen „dorovnává“ výsledek na celé číslo.

> [!example] Příklad
> $\frac{\varphi_+^{10}}{\sqrt{5}} \approx 55{,}004$, tedy $a_{10} = 55$; $\frac{\varphi_+^5}{\sqrt{5}} \approx 4{,}960$, tedy $a_5 = 5$.

> [!obrazek] Fibonacciho čísla a zlatý řez
> ![[lag15-fibonacci.png]]
> *Vlevo: modré body jsou $a_n$, oranžová křivka $\varphi_+^n/\sqrt{5}$; body na ní prakticky leží. Vpravo: zelené podíly $a_{n+1}/a_n$ střídavě přestřelují a podstřelují červenou hladinu $\varphi_+ \approx 1{,}618$ a rychle se k ní blíží.*

> [!navic] Obecně
> Stejně se řeší každá rekurence $a_{n+2} = pa_{n+1} + qa_n$: kořeny $\lambda_1 \neq \lambda_2$ rovnice $\lambda^2 = p\lambda + q$ dají řešení $a_n = \alpha\lambda_1^n + \beta\lambda_2^n$ a $\alpha$, $\beta$ se dopočítají z $a_0$, $a_1$. Třeba $a_{n+2} = a_{n+1} + 2a_n$ má kořeny $2$ a $-1$.

## §8 Motivace: diagonální matice a vlastní vektory

Fibonacciho rekurenci jde zapsat maticově: pro $\vec{v}_n = (a_{n+1}; a_n)$ je

$$
\vec{v}_{n+1} = \begin{pmatrix} a_{n+2} \\ a_{n+1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix} = F\vec{v}_n, \qquad \text{tedy} \quad \vec{v}_n = F^n\vec{v}_0.
$$

Potřebujeme tedy umět rychle mocnit matici. S obecnou maticí je to pracné, s diagonální snadné.

> [!definice] Definice · pozn. 11.20
> Matice $A \in \mathbb{F}^{n \times n}$ se nazývá *diagonální*, jestliže $a_{ij} = 0$ pro všechna $i \neq j$. Značíme $A = \operatorname{diag}(a_{11}, \dots, a_{nn})$.

^def-diagonalni

> [!lidsky] Lidsky
> Mimo hlavní diagonálu samé nuly. Taková matice jen **natahuje osy**, každou svým číslem, a nic nemíchá. Proto se s ní počítá po prvcích: $\operatorname{diag}(a_i) \cdot \operatorname{diag}(b_i) = \operatorname{diag}(a_ib_i)$, $\operatorname{diag}(a_i)^k = \operatorname{diag}(a_i^k)$, a determinant je součin diagonály. Je to speciální [[horní trojúhelníková matice]]; [[jednotková matice]] je $\operatorname{diag}(1, \dots, 1)$.

> [!example] Příklad
> $A = \operatorname{diag}(2, -1, 3)$: $A^2 = \operatorname{diag}(4, 1, 9)$, $A^{10} = \operatorname{diag}(1024, 1, 59\,049)$, $A^{-1} = \operatorname{diag}(\tfrac{1}{2}, -1, \tfrac{1}{3})$, $\det A = -6$. Nepříklad: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ diagonální není, je jen trojúhelníková.

**Vlastní vektory.** Matice $F$ diagonální není, ale některé vektory jen natáhne. Pro $\vec{x}_\pm = (\varphi_\pm; 1)$ je

$$
F\vec{x}_\pm = \begin{pmatrix} \varphi_\pm + 1 \\ \varphi_\pm \end{pmatrix} = \begin{pmatrix} \varphi_\pm^2 \\ \varphi_\pm \end{pmatrix} = \varphi_\pm\vec{x}_\pm,
$$

protože $\varphi_\pm^2 = \varphi_\pm + 1$. Vektory s vlastností $A\vec{x} = \lambda\vec{x}$, $\vec{x} \neq \vec{0}$, se nazývají *vlastní vektory* a čísla $\lambda$ *vlastní čísla*; budou tématem příští kapitoly. V bázi $\mathcal{X} = (\vec{x}_+, \vec{x}_-)$ je [[matice lineárního operátoru v bázi|matice operátoru]] $[F]^{\mathcal{X}} = \operatorname{diag}(\varphi_+, \varphi_-)$, takže $[F^n]^{\mathcal{X}} = \operatorname{diag}(\varphi_+^n, \varphi_-^n)$, a odtud znovu vyjde Binetův vzorec.

> [!obrazek] Obecný vektor se otočí, vlastní vektor se jen natáhne
> ![[lag15-vlastni-vektory.png]]
> *Matice $F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. Vlevo: modré $\vec{e}_1$, $\vec{e}_2$ a jejich oranžové obrazy, které míří jinam. Vpravo: modré vlastní vektory $\vec{x}_\pm$ a oranžové obrazy na týchž zelených přímkách: $\vec{x}_+$ se natáhne $1{,}618$-krát, $\vec{x}_-$ se zkrátí a otočí ($\varphi_- \approx -0{,}618$).*

> [!navic] Kontrola: $F^n$ obsahuje Fibonacciho čísla
> Indukcí $F^n = \begin{pmatrix} a_{n+1} & a_n \\ a_n & a_{n-1} \end{pmatrix}$, třeba $F^{10} = \begin{pmatrix} 89 & 55 \\ 55 & 34 \end{pmatrix}$. Z věty o determinantu součinu navíc $\det F^n = (\det F)^n = (-1)^n$, tedy $a_{n+1}a_{n-1} - a_n^2 = (-1)^n$ (Cassiniho identita): $89 \cdot 34 - 55^2 = 3026 - 3025 = 1$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč platí $\det(\alpha A) = \alpha^n \det A$ pro $A \in \mathbb{F}^{n \times n}$?
> Matice $\alpha A$ má **každý z $n$ sloupců** vynásobený $\alpha$. Podle **multilinearity** jde $\alpha$ vytknout z každého sloupce zvlášť, celkem $n$-krát: $\alpha \cdot \alpha \cdots \alpha = \alpha^n$.

> [!karta|02]- Dokaž z multilinearity, že přičtení $\alpha$-násobku $k$-tého sloupce k $l$-tému determinant nezmění.
> Multilinearita v $l$-tém sloupci: $\det(\cdots \vec{a}_l + \alpha\vec{a}_k \cdots) = \det A + \alpha\det(\cdots \vec{a}_k \cdots \vec{a}_k \cdots)$. Druhá matice má **dva stejné sloupce**, takže její determinant je **$0$**: je-li $\tau$ transpozice prohazující ty dva sloupce, mají sčítance pro $\pi$ a $\pi \circ \tau$ stejný součin a opačné znaménko a vyruší se.
>
> (Úvaha „prohození matici nezmění, ale otočí znaménko, tedy $\det = -\det$“ stačí jen pro $1 + 1 \neq 0$, nad $\mathbb{Z}_2$ ne.)

> [!karta|03]- Jak se dokáže, že $A$ je regulární, právě když $\det A \neq 0$?
> Eliminací převeď $A$ na **trojúhelníkový tvar** $B$. Úpravy zachovávají regularitu a determinant mění jen **nenulovým násobkem** ($-1$, $\alpha \neq 0$, $1$). Pro trojúhelníkovou $B$ platí: regulární $\Leftrightarrow$ diagonála bez nul $\Leftrightarrow$ $\det B = $ součin diagonály $\neq 0$.

> [!karta|04]- Dokaž, že $\det A^{-1} = (\det A)^{-1}$ pro regulární $A$.
> $1 = \det E = \det(AA^{-1}) = \det A \cdot \det A^{-1}$ (**determinant součinu**). Protože $A$ je regulární, $\det A \neq 0$ a můžeme dělit.

> [!karta|05]- Proč je součin $AB$ čtvercových matic regulární, právě když jsou regulární obě matice $A$ i $B$?
> $\det(AB) = \det A \cdot \det B$ a součin čísel je **nenulový, právě když jsou nenulové oba činitele**. Podle věty o regularitě: $AB$ regulární $\Leftrightarrow$ $\det A \neq 0$ a $\det B \neq 0$ $\Leftrightarrow$ $A$ i $B$ regulární.

> [!karta|06]- Platí $\det(A + B) = \det A + \det B$? Zdůvodni.
> **Obecně ne**: pro $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ a $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ je $\det A = \det B = 0$, ale $\det(A + B) = \det E_2 = 1$. Determinant je lineární jen **v jednom sloupci (řádku)**, když ostatní zůstanou stejné; s násobením se slučuje ($\det(AB) = \det A \det B$), se sčítáním ne.

> [!karta|07]- Proč nezávisí determinant operátoru $\det A = \det[A]^{\mathcal{X}}$ na volbě báze $\mathcal{X}$?
> Pro jinou bázi $\mathcal{Y}$ je $[A]^{\mathcal{Y}} = T[A]^{\mathcal{X}}T^{-1}$ s $T = [\mathrm{id}]^{\mathcal{X} \to \mathcal{Y}}$. Podle **věty o součinu** a **o inverzi** je $\det[A]^{\mathcal{Y}} = \det T \cdot \det[A]^{\mathcal{X}} \cdot (\det T)^{-1} = \det[A]^{\mathcal{X}}$: determinanty přechodových matic se vykrátí.

> [!karta|08]- Co geometricky znamená, že $\det A < 0$ pro $A \in \mathbb{R}^{2 \times 2}$?
> Zobrazení $\vec{x} \mapsto A\vec{x}$ **převrací orientaci** (jako zrcadlení): od 1. ke 2. sloupci $A$ vede nejkratší cesta otočením **doprava**, ačkoli od $\vec{e}_1$ k $\vec{e}_2$ doleva. Obsah se přitom zvětší $\lvert\det A\rvert$-krát.

> [!karta|09]- Kolikrát se zvětší obsah útvaru při zobrazení $\vec{x} \mapsto A\vec{x}$ a proč stačí ověřit to na jednotkovém čtverci?
> **$\lvert\det A\rvert$-krát.** Jednotkový čtverec se zobrazí na rovnoběžník ze sloupců $A$ o obsahu $\lvert\det A\rvert$. Útvar se dá poskládat (přibližně) z malých čtverců a lineární zobrazení zvětší každý **stejným poměrem**.

> [!karta|10]- Proč je na pozici $(i, j)$ adjungované matice doplněk pozice $(j, i)$, a ne $(i, j)$?
> Aby v součinu $\operatorname{adj}(A) \cdot A$ vyšel na diagonále **rozvoj $\det A$ podle sloupce**: $\sum_k [\operatorname{adj} A]_{ik}a_{ki} = \sum_k D_{ki}a_{ki}$. S netransponovanými doplňky by se násobily doplňky jednoho řádku se sloupcem a vzorec $A^{-1} = \frac{1}{\det A}\operatorname{adj} A$ by neplatil.

> [!karta|11]- Dokaž, že $\operatorname{adj}(A) \cdot A = (\det A)E$.
> Prvek $(i, j)$ je $\sum_k D_{ki}a_{kj}$ = rozvoj podle $i$-tého sloupce matice, která vznikne z $A$ **nahrazením $i$-tého sloupce $j$-tým**. Pro $i = j$ je to $A$ sama, tedy **$\det A$**. Pro $i \neq j$ má ta matice **dva stejné sloupce**, tedy determinant **$0$**.

> [!karta|12]- Jaké předpoklady má Cramerovo pravidlo a kdy se oproti eliminaci vyplatí?
> Matice soustavy musí být **čtvercová a regulární** ($\det A \neq 0$). Na každou neznámou stojí **dva determinanty**, takže pro konkrétní čísla je eliminace rychlejší. Vyplatí se pro **soustavy s parametrem**, když chceš **jen jednu neznámou**, a jako obecný vzorec v teorii.

> [!karta|13]- Proč tvoří řešení rekurence $a_{n+2} = a_{n+1} + a_n$ podprostor dimenze právě 2?
> Řešení jsou **jádro** lineárního zobrazení $F(a_n) = (a_{n+2} - a_{n+1} - a_n)$, tedy podprostor. Každé řešení je **určené dvojicí $(a_0, a_1)$**: tři řešení mají LZ počáteční dvojice v $\mathbb{R}^2$, tatáž kombinace posloupností začíná $0, 0$, a tak je nulová. Proto $\dim \le 2$, a $(0, 1, 1, 2, \dots)$, $(1, 0, 1, 1, \dots)$ jsou dvě LN řešení.

> [!karta|14]- Proč se řešení rekurence $a_{n+2} = a_{n+1} + a_n$ hledá ve tvaru $a_n = \lambda^n$ a jaká rovnice z toho vyjde?
> Rekurence prvního řádu $a_{n+1} = \lambda a_n$ má řešení **$\lambda^n a_0$**, tak zkusíme totéž. Dosazením $\lambda^{n+2} - \lambda^{n+1} - \lambda^n = 0$ a vydělením $\lambda^n$ vyjde **$\lambda^2 - \lambda - 1 = 0$**, tedy $\lambda = \frac{1 \pm \sqrt{5}}{2}$. Dvě různá $\lambda$ dají dvě LN řešení = bázi.

> [!karta|15]- Proč stačí $n$-té Fibonacciho číslo spočítat jako zaokrouhlené $\varphi_+^n / \sqrt{5}$?
> Přesně je $a_n = \frac{1}{\sqrt{5}}(\varphi_+^n - \varphi_-^n)$. Protože $\lvert\varphi_-\rvert \approx 0{,}618 < 1$ a $\frac{1}{\sqrt{5}} < \frac{1}{2}$, je **$\lvert\varphi_-^n / \sqrt{5}\rvert < \frac{1}{2}$**; $a_n$ je celé číslo vzdálené od $\varphi_+^n / \sqrt{5}$ méně než $\frac{1}{2}$, tedy jeho **zaokrouhlení**.

> [!karta|16]- Proč by se nám hodila báze, ve které je matice operátoru diagonální?
> S diagonální maticí se počítá **po prvcích**: $\operatorname{diag}(a, b)^n = \operatorname{diag}(a^n, b^n)$, inverze i polynomy taky. Báze z vektorů s $A\vec{x} = \lambda\vec{x}$ (**vlastních vektorů**) dá diagonální $[A]^{\mathcal{X}}$; u Fibonacciho čísel $[A]^{\mathcal{X}} = \operatorname{diag}(\varphi_+, \varphi_-)$, takže $A^n$ a tím $a_n$ spočítáš hned.

### Příklady na procvičení

> [!priklad|17]- Pro $A \in \mathbb{R}^{4 \times 4}$ s $\det A = -3$ spočítej $\det A^{-1}$, $\det(A^2)$ a $\det(2A^{\mathsf{T}}A^{-1})$.
> $\det A^{-1} = -\frac{1}{3}$, $\det(A^2) = (-3)^2 = 9$. $\det(2A^{\mathsf{T}}A^{-1}) = 2^4 \cdot (-3) \cdot \left(-\frac{1}{3}\right) = $ **$16$** (vytknutí $2$ ze čtyř sloupců, determinant součinu, $\det A^{\mathsf{T}} = \det A$). Výsledky: **$-\frac{1}{3}$, $9$, $16$**.

> [!priklad|18]- Cramerovým pravidlem vyřeš $2x + y = 5$, $x + 3y = 10$.
> $\det A = \det\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = 5$. $x = \frac{1}{5}\det\begin{pmatrix} 5 & 1 \\ 10 & 3 \end{pmatrix} = \frac{5}{5} = 1$, $y = \frac{1}{5}\det\begin{pmatrix} 2 & 5 \\ 1 & 10 \end{pmatrix} = \frac{15}{5} = 3$. **$(x; y) = (1; 3)$**, kontrola $2 + 3 = 5$, $1 + 9 = 10$.

> [!priklad|19]- Najdi $\operatorname{adj} C$ a $C^{-1}$ pro $C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$.
> Doplňky: $D_{11} = 1$, $D_{12} = -(0 - 1) = 1$, $D_{13} = -1$; $D_{21} = -2$, $D_{22} = 1$, $D_{23} = -(0 - 2) = 2$; $D_{31} = 2$, $D_{32} = -1$, $D_{33} = 1$. Transponovat: **$\operatorname{adj} C = \begin{pmatrix} 1 & -2 & 2 \\ 1 & 1 & -1 \\ -1 & 2 & 1 \end{pmatrix}$**. Rozvoj podle 1. řádku: $\det C = 1 \cdot 1 + 2 \cdot 1 + 0 = 3$, tedy **$C^{-1} = \frac{1}{3}\operatorname{adj} C$**.

> [!priklad|20]- Pro $C = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ a $\vec{b} = (5; 3; 2)$ spočítej Cramerovým pravidlem jen $x_2$.
> $\det C = 3$. $C^{(2)} = \begin{pmatrix} 1 & 5 & 0 \\ 0 & 3 & 1 \\ 1 & 2 & 1 \end{pmatrix}$, rozvoj podle 1. řádku: $1 \cdot (3 - 2) - 5 \cdot (0 - 1) + 0 = 6$. **$x_2 = \frac{6}{3} = 2$** (celé řešení je $(1; 2; 1)$, kontrola $C(1; 2; 1) = (5; 3; 2)$).

> [!priklad|21]- Jaký obsah má obraz kruhu o poloměru $1$ při zobrazení $\vec{x} \mapsto A\vec{x}$, $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$? A jaký obsah má trojúhelník s vrcholy $(0; 0)$, $(3; 1)$, $(1; 2)$?
> $\det A = 6 - 1 = 5$, obraz kruhu (elipsa) má obsah **$5\pi$**. Trojúhelník je polovina rovnoběžníku ze sloupců $(3; 1)$, $(1; 2)$ s $\lvert\det\rvert = \lvert 6 - 1\rvert = 5$, obsah **$\frac{5}{2}$**.

> [!priklad|22]- Najdi vzorec pro $a_n$, je-li $a_0 = 0$, $a_1 = 3$ a $a_{n+2} = a_{n+1} + 2a_n$.
> $a_n = \lambda^n$: $\lambda^2 - \lambda - 2 = 0$, $\lambda \in \{2, -1\}$, takže $a_n = \alpha 2^n + \beta(-1)^n$. $a_0 = \alpha + \beta = 0$, $a_1 = 2\alpha - \beta = 3$ dá $\alpha = 1$, $\beta = -1$. **$a_n = 2^n - (-1)^n$**; kontrola $a_2 = 3 + 0 = 3 = 4 - 1$, $a_3 = 3 + 6 = 9 = 8 + 1$.

> [!priklad|23]- Je $\det(\vec{a}_1\ \vec{a}_2\ \vec{a}_3) = 4$. Spočítej $\det(2\vec{a}_1\ \ \vec{a}_1 + \vec{a}_2\ \ {-\vec{a}_3})$.
> Vytkni $2$ z 1. a $-1$ ze 3. sloupce: $-2\det(\vec{a}_1\ \ \vec{a}_1 + \vec{a}_2\ \ \vec{a}_3)$. Podle multilinearity ve 2. sloupci $= -2\big(\det(\vec{a}_1\ \vec{a}_1\ \vec{a}_3) + \det(\vec{a}_1\ \vec{a}_2\ \vec{a}_3)\big) = -2(0 + 4) = $ **$-8$**.

> [!priklad|24]- Spočítej determinant operátoru $P : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^{\le 2}[x]$, $p(x) \mapsto p(x + 1)$.
> V bázi $(1, x, x^2)$: $P(1) = 1$, $P(x) = 1 + x$, $P(x^2) = 1 + 2x + x^2$, tedy $[P] = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$, horní trojúhelníková s jedničkami na diagonále: **$\det P = 1$** (v každé bázi stejně).

---
← [[LAG 14 – Permutace a determinant|11. 11. 2026 Permutace a determinant]] · [[LAG 16 – Vlastní čísla, charakteristický polynom a diagonalizace|18. 11. 2026 Vlastní čísla, charakteristický polynom a diagonalizace]] →

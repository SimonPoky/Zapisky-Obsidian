---
predmet: LAG
prednaska: 12
datum: 2026-11-04
zdroj: "V poznámkách kap. 8.1 a začátek 8.2 (věta 8.1 až úloha 8.11)"
tags: [prednaska, LAG]
---

# LAG 12 – Frobeniova věta a Gaussova eliminace

*Přednáška 12 · středa 4. 11. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `soustava jako Ax = b` · `Frobeniova věta` · `rank A = rank(A | b)` · `S = xₚ + S₀` · `parametrický tvar` · `zpětná substituce` · `horní stupňovitý tvar` · `hlavní a vedlejší sloupce, pivoty` · `hlavní sloupce = báze im A` · `elementární řádkové úpravy` · `Gaussova eliminace`

Minule jsme soustavu lineárních rovnic zapsali jako $A\vec{x} = \vec{b}$ a viděli, že řešení jsou vzor $\vec{b}$, tedy posunuté jádro. Dnes to shrnula Frobeniova věta: kdy řešení existuje (porovnáním dvou hodností) a jak velká je množina řešení. Věta ale neříká, jak řešení najít. Proto přišel horní stupňovitý tvar, ve kterém se soustava vyřeší zpětnou substitucí, a Gaussova eliminace, která na tento tvar převede každou matici, aniž by změnila množinu řešení.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[matice soustavy]] | soustava = $A\vec{x} = \vec{b}$ = $\vec{b}$ jako kombinace sloupců $A$ | $x - y + 2z = 3$: $A = (1\ {-1}\ 2)$ |
| [[Frobeniova věta]] | $\dim S_0 = n - \operatorname{rank} A$; řešení existuje $\Leftrightarrow \operatorname{rank} A = \operatorname{rank}(A \mid \vec{b})$; $S = \vec{x}_p + S_0$ | $\dim S_0 = 3 - 1 = 2$ |
| [[parametrický tvar řešení]] | každá neznámá jako výraz v parametrech | $x = 3 + t - 2s$, $y = t$, $z = s$ |
| [[zpětná substituce]] | dopočítávání neznámých od poslední rovnice nahoru | $z = 1$, $y = 0$, $x = 1$ |
| [[horní stupňovitý tvar]] | nenulové řádky nahoře, každý začíná víc vpravo než předchozí | schod $2, 4, 5$ |
| [[hlavní sloupec]], [[vedlejší sloupec]], [[pivot]] | sloupce s prvním nenulovým číslem řádku / ostatní / ta čísla | |
| [[věta o hlavních sloupcích]] | hlavní sloupce tvoří bázi $\operatorname{im} A$, $\operatorname{rank} A$ = počet nenulových řádků | $\operatorname{rank} = 3$ |
| [[elementární řádkové úpravy]] | prohození řádků, násobení řádku $\alpha \ne 0$, přičtení násobku jiného řádku | |
| [[věta o elementárních řádkových úpravách]] | nemění množinu řešení soustavy | |
| [[věta o převodu na horní stupňovitý tvar]] | každou matici jde úpravami 1. a 3. převést na stupňovitý tvar | |
| [[Gaussova eliminace]] | algoritmus, který to udělá sloupec po sloupci | řešení $(1; 0; 2; 1)$ |

## §1 Soustava jako jedna maticová rovnice

Soustava $m$ rovnic o $n$ neznámých nad tělesem $\mathbb{F}$ je jedna rovnice $A\vec{x} = \vec{b}$ s [[matice soustavy|maticí soustavy]] $A \in \mathbb{F}^{m \times n}$, sloupcem neznámých $\vec{x} \in \mathbb{F}^n$ a sloupcem pravých stran $\vec{b} \in \mathbb{F}^m$. Když sloupce $A$ označíme $\vec{a}_1, \dots, \vec{a}_n$, tedy $A = (\vec{a}_1 \cdots \vec{a}_n)$, je podle definice [[součin matice a vektoru|součinu matice a vektoru]]

$$
A\vec{x} = x_1\vec{a}_1 + x_2\vec{a}_2 + \dots + x_n\vec{a}_n = \vec{b}.
$$

Vyřešit soustavu tedy znamená tři rovnocenné věci: najít [[vzor množiny|vzor]] $\vec{b}$ při zobrazení $\vec{x} \mapsto A\vec{x}$, zapsat $\vec{b}$ jako [[lineární kombinace|lineární kombinaci]] sloupců $A$, a najít všechna $\vec{x}$ s $A\vec{x} = \vec{b}$. Pro $\vec{b} = \vec{0}$ je soustava [[homogenní soustava|homogenní]] a její množina řešení je [[jádro]] $\ker A$.

> [!example] Příklad
> Soustava $x + 2y = 5$, $3x - y = 1$ je $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$, neboli $x\begin{pmatrix} 1 \\ 3 \end{pmatrix} + y\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$. Řešení $x = 1$, $y = 2$ říká, že $(5; 1) = 1 \cdot (1; 3) + 2 \cdot (2; -1)$.

## §2 Frobeniova věta

> [!veta] Věta 8.1 (Frobeniova)
> ==Buď $\mathbb{F}$ těleso a $A\vec{x} = \vec{b}$ soustava lineárních rovnic s $n$ neznámými, $A \in \mathbb{F}^{m \times n}$, $\vec{b} \in \mathbb{F}^m$.== Potom:
>
> 1. **Množina řešení $S_0$ homogenní soustavy $A\vec{x} = \vec{0}$ je lineární podprostor $\mathbb{F}^n$ dimenze $n - \operatorname{rank} A$.**
> 2. **Soustava $A\vec{x} = \vec{b}$ má řešení, právě když $\operatorname{rank} A = \operatorname{rank}(A \mid \vec{b})$.**
> 3. ==Je-li $\vec{x}_p$ nějaké řešení soustavy $A\vec{x} = \vec{b}$==, pak její množina řešení je
>
> $$
> \mathbf{S = \vec{x}_p + S_0 = \{\vec{x}_p + \vec{x}_0 \mid \vec{x}_0 \in S_0\}}.
> $$
>
> > [!note]- Důkaz
> > **1.** $S_0 = \ker A$ je podprostor ([[věta o jádru a obrazu]]) a podle [[věta o dimenzi jádra a obrazu|věty o dimenzi]] je $\dim \ker A = \operatorname{def} A = \dim \mathbb{F}^n - \operatorname{rank} A = n - \operatorname{rank} A$.
> >
> > **2.** Soustava má řešení $\Leftrightarrow$ $\vec{b}$ je kombinací sloupců $\Leftrightarrow$ $\vec{b} \in \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n\}$. To je totéž jako $\operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n\} = \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n, \vec{b}\}$ (pozn. 2.15). Rovné podprostory mají stejnou dimenzi; naopak levý obal leží vždy v pravém, a stejná konečná dimenze proto dává rovnost ([[věta o dimenzi podprostoru]]). Levý obal je $\operatorname{im} A$ s dimenzí $\operatorname{rank} A$, pravý je $\operatorname{im}(A \mid \vec{b})$ s dimenzí $\operatorname{rank}(A \mid \vec{b})$.
> >
> > **3.** $S$ je vzor $\vec{b}$ při zobrazení $\vec{x} \mapsto A\vec{x}$ a $S_0 = \ker A$, takže jde přesně o [[věta o struktuře vzoru|větu o struktuře vzoru]] (věta 7.18).

^veta-frobenius

> [!lidsky] Lidsky
> Frobeniova věta je návod ve třech krocích. **(2) Má to vůbec řešení?** Přidej k matici sloupec pravých stran. Když tím hodnost nevyskočí, je $\vec{b}$ složitelné ze sloupců a řešení existuje. **(1) Kolik volnosti mají řešení?** Tolik parametrů, kolik je neznámých minus hodnost. **(3) Jak vypadají všechna řešení?** Jedno konkrétní řešení plus cokoli z řešení homogenní soustavy.

> [!example] Příklad
> $x + 2y = 3$, $2x + 4y = 5$: $\operatorname{rank}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 1$, ale $\operatorname{rank}\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 5 \end{array}\right) = 2$, protože $(3; 5)$ není násobkem $(1; 2)$: **řešení neexistuje** (dvě rovnoběžné přímky). Se stejnou levou stranou a $\vec{b} = (3; 6)$ je $\operatorname{rank}(A \mid \vec{b}) = 1$, řešení existují a tvoří přímku, $\dim S_0 = 2 - 1 = 1$.

> [!pozor] $n$ je počet neznámých, ne rovnic
> V bodě 1 se odečítá hodnost od **počtu sloupců** matice soustavy (neznámých), ne od počtu řádků. Jedna rovnice o třech neznámých má $\dim S_0 = 3 - 1 = 2$, ne $1 - 1 = 0$.

> [!navic] Co Frobeniova věta neumí
> Řekne, **jestli** řešení existuje a **jak velká** je množina řešení, ale žádné řešení nenajde: pořád potřebuješ znát hodnosti a jedno $\vec{x}_p$. Hodnost umíme zatím spočítat jen u matic ve speciálním tvaru (§4) a obecnou matici na něj převede Gaussova eliminace (§5). Jméno „Frobeniova věta“ se používá jen v Česku a na Slovensku; jinde se jí říká Rouchéova–Capelliho nebo Kroneckerova–Capelliho věta.

## §3 Řešení podle Frobeniovy věty

### Jedna rovnice o třech neznámých (úloha 8.2)

Řešme nad $\mathbb{R}$ rovnici $x - y + 2z = 3$. Rozšířená matice je $(1\ \ {-1}\ \ 2 \mid 3)$, matice soustavy $A = (1\ \ {-1}\ \ 2)$.

1. **Existence:** $\operatorname{rank} A = 1 = \operatorname{rank}(A \mid \vec{b})$ (jeden nenulový řádek), takže řešení existuje.
2. **Homogenní soustava** $x - y + 2z = 0$: $S_0 = \{(x; y; z) \in \mathbb{R}^3 \mid x - y + 2z = 0\} \le \mathbb{R}^3$ má dimenzi $3 - \operatorname{rank} A = 3 - 1 = 2$. Stačí tedy najít **dvě LN řešení**, ta už $S_0$ generují ([[věta o bázi z n vektorů]]). Volíme $y = 1, z = 0$, dopočítáme $x = 1$; volíme $y = 0, z = 1$, dopočítáme $x = -2$. Vektory $(1; 1; 0)$ a $(-2; 0; 1)$ jsou LN, protože na pozicích $y, z$ mají $(1; 0)$ a $(0; 1)$. Tedy $S_0 = \operatorname{span}\{(1; 1; 0), (-2; 0; 1)\}$.
3. **Jedno řešení** původní rovnice: zvolíme nejjednodušší $y = z = 0$, pak $x = 3$, tedy $\vec{x}_p = (3; 0; 0)$.

$$
S = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} + \operatorname{span}\left\{\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -2 \\ 0 \\ 1 \end{pmatrix}\right\} = \left\{\begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} + t\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + s\begin{pmatrix} -2 \\ 0 \\ 1 \end{pmatrix} \;\middle|\; t, s \in \mathbb{R}\right\}.
$$

Rozepsáno po složkách je to **parametrický tvar řešení**: $x = 3 + t - 2s$, $y = t$, $z = s$, kde $t, s \in \mathbb{R}$ jsou parametry. Každá volba parametrů dává jedno řešení a každé řešení odpovídá jediné volbě; parametrů je $\dim S_0 = n - \operatorname{rank} A$. ^parametricky-tvar

> [!obrazek] Řešení homogenní a nehomogenní rovnice
> ![[lag12-frobenius.png]]
> *Zelená rovina je $S_0 = \ker A$ (řešení $x - y + 2z = 0$) se zelenými generátory $(1; 1; 0)$ a $(-2; 0; 1)$. Modrá rovina je $S$ (řešení $x - y + 2z = 3$): zelená rovina posunutá o červené $\vec{x}_p = (3; 0; 0)$. Roviny jsou rovnoběžné a modrá neprochází počátkem.*

> [!example] Příklad
> Kontrola dosazením: $t = 1$, $s = 1$ dá $(3 + 1 - 2;\ 1;\ 1) = (2; 1; 1)$ a $2 - 1 + 2 \cdot 1 = 3$. ✓ Partikulární řešení není jediné: $(1; 0; 1)$ také splňuje $1 - 0 + 2 = 3$, a $\{(1; 0; 1)\} + S_0$ je tatáž množina $S$, protože $(1; 0; 1) - (3; 0; 0) = (-2; 0; 1) \in S_0$.

> [!pozor] Volba neznámých musí zaručit LN
> Volba „jedna volná neznámá $= 1$, ostatní volné $= 0$“ dává automaticky LN vektory. Kdybys volil nahodile, třeba $(y; z) = (1; 1)$ a $(2; 2)$, dostaneš vektory $(-1; 1; 1)$ a $(-2; 2; 2)$, které jsou násobky a rovinu $S_0$ negenerují.

### Trojúhelníková soustava (úloha 8.3)

Soustava s rozšířenou maticí

$$
\left(\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 0 & 3 & -1 & -1 \\ 0 & 0 & 2 & 2 \end{array}\right)
$$

znamená $x - y + 2z = 3$, $3y - z = -1$, $2z = 2$. Z poslední rovnice $z = 1$, dosazením do druhé $3y - 1 = -1$, tedy $y = 0$, a dosazením do první $x - 0 + 2 = 3$, tedy $x = 1$. Tomuto postupu, kdy se z poslední rovnice spočítá poslední neznámá a výsledky se postupně dosazují do rovnic nad ní, se říká **zpětná substituce**. Funguje vždy, když je matice soustavy v horním stupňovitém tvaru (§4). ^zpetna-substituce

Frobeniova věta výsledek potvrdí: žádný sloupec $A$ není kombinací předchozích, takže $\operatorname{rank} A = 3$. Hodnost $(A \mid \vec{b})$ nemůže být víc než 3, protože matice má jen 3 řádky, takže $\operatorname{rank}(A \mid \vec{b}) = 3$ a řešení existuje. Navíc $\dim S_0 = 3 - 3 = 0$, $S_0 = \{\vec{0}\}$, a řešení je **právě jedno**: $S = \{(1; 0; 1)\}$.

> [!lidsky] Lidsky
> Zpětná substituce je jako rozplétání uzlu od konce: poslední rovnice obsahuje jedinou neznámou, tu spočítáš hned; o řádek výš pak zbude zase jen jedna nová neznámá. Proto chceme matici dostat do „schodovitého“ tvaru.

## §4 Horní stupňovitý tvar

> [!definice] Definice · pozn. 8.4
> Buď $\mathbb{F}$ těleso. Matice $A \in \mathbb{F}^{m \times n}$ je v *horním stupňovitém tvaru*, jestliže existuje $0 \le r \le m$ takové, že
>
> - $a_{ij} = 0$ pro všechna $i > r$ a $j = 1, \dots, n$ (řádky pod $r$-tým jsou nulové), a
> - existují čísla $0 < k_1 < k_2 < \dots < k_r \le n$ taková, že pro každé $i = 1, \dots, r$ je $a_{ik_i} \ne 0$ a $a_{ij} = 0$ pro všechna $j < k_i$.
>
> Sloupce s indexy $k_1, \dots, k_r$ se nazývají *hlavní*, ostatní sloupce *vedlejší*. Pozicím $(i, k_i)$ (a číslům $a_{ik_i}$ na nich) se říká *pivoty*.

^def-stupnovity-tvar

> [!lidsky] Lidsky
> Každý nenulový řádek začíná nulami a jeho **první nenulové číslo (pivot)** je víc vpravo než pivot řádku nad ním. Pod pivoty tak vznikne „schodiště“ ze samých nul a nulové řádky jsou úplně dole. Sloupec s pivotem je hlavní, sloupec bez pivotu vedlejší. Neznámé u vedlejších sloupců jsou ty, které si při řešení volíš (parametry).

> [!example] Příklad
> $\begin{pmatrix} 0 & 3 & 1 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ **je** v horním stupňovitém tvaru: $r = 2$, $k_1 = 2$, $k_2 = 4$, pivoty $3$ a $2$, hlavní sloupce 2 a 4, vedlejší 1 a 3.
>
> $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ **není**: první nenulové číslo třetího řádku je ve 2. sloupci, tedy vlevo od pivotu druhého řádku (3. sloupec), a $k_3 > k_2$ neplatí. Jednotková matice $E_n$ v tvaru je, všechny její sloupce jsou hlavní.

> [!obrazek] Schodiště, pivoty a hlavní sloupce
> ![[lag12-stupnovity.png]]
> *Rozšířená matice z úlohy 8.5. Modrá čára je schod, pod ním a vlevo od něj jsou jen nuly (červeně). Oranžové kroužky jsou pivoty, oranžově podbarvené sloupce hlavní (neznámé $x_2, x_4, x_5$), šedé vedlejší ($x_1, x_3, x_6, x_7$, ty jsou parametry).*

> [!pozor] Pivot nemusí být na diagonále
> Stupňovitý tvar není totéž co horní trojúhelníková matice. Schod může být „dlouhý“ (mezi pivoty vedlejší sloupce) a první sloupec může být celý nulový. Podstatné je jen, že pivoty jdou **striktně doprava** a nulové řádky jsou dole.

### Soustava ve stupňovitém tvaru (úloha 8.5)

Řešme soustavu 3 rovnic o 7 neznámých s rozšířenou maticí z obrázku:

$$
\left(\begin{array}{ccccccc|c} 0 & 1 & 0 & 2 & 5 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 & 3 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 2 & 1 \end{array}\right)
$$

- **Hodnosti:** hlavní sloupce jsou 2, 4, 5, takže $\operatorname{rank} A = 3$; sloupec pravých stran je vedlejší, takže i $\operatorname{rank}(A \mid \vec{b}) = 3$ a řešení existuje.
- **Homogenní soustava:** $\dim S_0 = 7 - 3 = 4$. Volné neznámé jsou u vedlejších sloupců: $x_1, x_3, x_6, x_7$. Postupně zvolíme jednu z nich $= 1$ a ostatní $= 0$ a zbytek dopočítáme zpětnou substitucí z rovnic $x_5 + x_6 + 2x_7 = 0$, $2x_4 + 3x_5 + x_6 = 0$, $x_2 + 2x_4 + 5x_5 + x_7 = 0$:
  - $x_1 = 1$: $x_5 = x_4 = x_2 = 0$, vektor $(1; 0; 0; 0; 0; 0; 0)$;
  - $x_3 = 1$: vektor $(0; 0; 1; 0; 0; 0; 0)$;
  - $x_6 = 1$: $x_5 = -1$, $2x_4 = 3 - 1$, $x_4 = 1$, $x_2 = -2 + 5 = 3$, vektor $(0; 3; 0; 1; -1; 1; 0)$;
  - $x_7 = 1$: $x_5 = -2$, $2x_4 = 6$, $x_4 = 3$, $x_2 = -6 + 10 - 1 = 3$, vektor $(0; 3; 0; 3; -2; 0; 1)$.
- **Partikulární řešení:** všechny volné neznámé $= 0$; pak $x_5 = 1$, $2x_4 = 1 - 3$, $x_4 = -1$, $x_2 = 1 + 2 - 5 = -2$, tedy $\vec{x}_p = (0; -2; 0; -1; 1; 0; 0)$.

$$
S = \begin{pmatrix} 0 \\ -2 \\ 0 \\ -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} + \operatorname{span}\left\{\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 3 \\ 0 \\ 1 \\ -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 3 \\ 0 \\ 3 \\ -2 \\ 0 \\ 1 \end{pmatrix}\right\}.
$$

Čtyři vektory jsou LN, protože na pozicích volných neznámých $(x_1, x_3, x_6, x_7)$ mají $(1;0;0;0)$, $(0;1;0;0)$, $(0;0;1;0)$, $(0;0;0;1)$. První dva generátory jen říkají, že $x_1$ a $x_3$ mohou být cokoli; v soustavě se vůbec nevyskytují.

> [!veta] Věta 8.6
> ==Nechť $A$ je matice v horním stupňovitém tvaru.== Potom **hlavní sloupce $A$ tvoří bázi $\operatorname{im} A$**. Jejich počet $r$, a tedy i počet nenulových řádků $A$, je roven **$\operatorname{rank} A$**.
>
> > [!note]- Důkaz
> > **LN:** $i$-tý hlavní sloupec (na pozici $k_i$) má v $i$-tém řádku pivot $a_{ik_i} \ne 0$, zatímco všechny předchozí sloupce tam mají $0$. Proto není kombinací předchozích a podle [[alternativní definice lineární závislosti|alternativní definice LZ]] jsou hlavní sloupce LN.
> >
> > **Generují:** každý sloupec má nuly v řádcích $r + 1, \dots, m$, takže $\operatorname{im} A$ (obal sloupců) leží v podprostoru vektorů, které mají nenulová čísla jen na prvních $r$ pozicích. Ten má dimenzi $r$, tedy $\dim \operatorname{im} A \le r$. Našli jsme $r$ LN vektorů v $\operatorname{im} A$, takže tvoří bázi ([[věta o bázi z n vektorů]]).

^veta-hlavni-sloupce

> [!lidsky] Lidsky
> Ve stupňovitém tvaru se hodnost **čte okem**: spočítej schody (pivoty, nenulové řádky). Hlavní sloupce jsou nezávislé, protože každý „otevírá“ nový řádek, kde předchozí mají nulu. Vedlejší sloupec nic nového nepřinese: je kombinací hlavních sloupců vlevo od něj.

> [!example] Příklad
> V úloze 8.5 je $\operatorname{rank} A = 3$ a báze $\operatorname{im} A$ je $\big((1; 0; 0), (2; 2; 0), (5; 3; 1)\big)$, tedy sloupce 2, 4, 5. Vedlejší sloupec 6, $(0; 1; 1)$, je jejich kombinace: $(0; 1; 1) = -3 \cdot (1; 0; 0) - 1 \cdot (2; 2; 0) + 1 \cdot (5; 3; 1)$. Tyto koeficienty jsou (s opačným znaménkem) složky třetího vektoru jádra $(0; 3; 0; 1; -1; 1; 0)$, protože $3\vec{a}_2 + \vec{a}_4 - \vec{a}_5 + \vec{a}_6 = \vec{0}$.

## §5 Elementární řádkové úpravy a Gaussova eliminace

> [!definice] Definice · pozn. 8.7
> *Elementární řádkové úpravy* (ERÚ) matice jsou:
>
> 1. prohození dvou řádků,
> 2. vynásobení řádku nenulovým skalárem $\alpha \in \mathbb{F}$,
> 3. přičtení libovolného skalárního násobku jednoho řádku k jinému řádku.

^def-elementarni-upravy

> [!lidsky] Lidsky
> Přesně to, co děláš se soustavou rovnic od střední školy: přehodíš pořadí rovnic, vynásobíš rovnici nenulovým číslem, k rovnici přičteš násobek jiné. Všechny tři kroky jdou **vrátit zpět** (prohodit znovu, vynásobit $\alpha^{-1}$, odečíst ten násobek), a proto se nic neztratí ani nepřibude.

> [!example] Příklad
> Z $\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & -1 & 1 \end{array}\right)$ dostaneš úpravou 3 (druhý řádek minus trojnásobek prvního) $\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -7 & -14 \end{array}\right)$ a úpravou 2 (druhý řádek krát $-\tfrac{1}{7}$) $\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 2 \end{array}\right)$. Odtud $y = 2$, $x = 5 - 4 = 1$. Naopak „vynásob řádek nulou“ ERÚ **není**: z $(3\ {-1} \mid 1)$ by se stalo $(0\ 0 \mid 0)$ a rovnice by zmizela.

> [!veta] Věta 8.8
> ==Buď $\mathbb{F}$ těleso, $A \in \mathbb{F}^{m \times n}$, $\vec{b} \in \mathbb{F}^m$.== **Elementární řádkové úpravy rozšířené matice $(A \mid \vec{b})$ nemění množinu řešení $\{\vec{x} \in \mathbb{F}^n \mid A\vec{x} = \vec{b}\}$.**
>
> > [!note]- Důkaz
> > **Prohození** řádků mění jen pořadí rovnic. **Násobení** $k$-tého řádku $\gamma \ne 0$: rovnice $a_{k1}x_1 + \dots + a_{kn}x_n = b_k$ a $\gamma a_{k1}x_1 + \dots + \gamma a_{kn}x_n = \gamma b_k$ jsou ekvivalentní (zleva doprava násobíme $\gamma$, zprava doleva $\gamma^{-1}$, které existuje díky $\gamma \ne 0$). **Přičtení** $\alpha$-násobku $l$-tého řádku ke $k$-tému: když $\vec{x}$ splňuje obě rovnice, splňuje i jejich součet $(\text{řádek}_k + \alpha\,\text{řádek}_l)$; naopak z nové $k$-té rovnice a nezměněné $l$-té dostaneš původní $k$-tou odečtením $\alpha$-násobku $l$-té. Ostatní rovnice se nemění.

^veta-upravy-nemeni-reseni

> [!lidsky] Lidsky
> Upravená soustava je jen **jinak zapsaná táž soustava**: každé řešení staré je řešením nové a naopak. Proto smíš soustavu upravovat, dokud není ve tvaru, kde řešení vidíš.

> [!pozor] ERÚ mění obraz matice
> Řádkové úpravy nemění množinu řešení, tedy ani $\ker A$, a tím ani $\operatorname{rank} A = n - \operatorname{def} A$. **Mění ale sloupce, a tím i $\operatorname{im} A$:** $\begin{pmatrix} 1 \\ 1 \end{pmatrix} \sim \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ (druhý řádek minus první) a $\operatorname{span}\{(1; 1)\} \ne \operatorname{span}\{(1; 0)\}$. Bázi $\operatorname{im} A$ proto ber ze sloupců **původní** matice, na pozicích, kde jsou po eliminaci hlavní sloupce. Vztahy mezi sloupci se úpravami nemění, protože jsou to řešení homogenní soustavy.

> [!veta] Věta 8.9
> **Každou matici lze sledem elementárních řádkových úprav 1. a 3. převést na horní stupňovitý tvar.**
>
> > [!note]- Důkaz
> > Stačí ukázat, že k cíli vždy dojde algoritmus 8.10 níže: v každém kroku buď posune sloupec doprava, nebo vyrobí pivot a pod ním nuly a posune řádek i sloupec. Po nejvýš $m + n$ krocích skončí a vzniklá matice je stupňovitá. Násobení řádku (úprava 2) není potřeba.

^veta-prevod-na-stupnovity

> [!lidsky] Lidsky
> Žádná matice není „neupravitelná“. Když v aktuálním sloupci nenajdeš nic nenulového, posuneš se doprava; když najdeš, přesuneš to nahoru a vynuluješ všechno pod tím.

> [!definice] Algoritmus 8.10 · Gaussova eliminační metoda
> Vstup: matice $B \in \mathbb{F}^{m \times n}$. Polož $l = 1$ (řádek) a $j = 1$ (sloupec). Dokud $j \le n$ a $l \le m$, opakuj:
>
> 1. Je-li $b_{ij} = 0$ pro všechna $i \ge l$, polož $j = j + 1$ a opakuj krok 1.
> 2. Je-li $b_{lj} = 0$, najdi $k > l$ s $b_{kj} \ne 0$ a prohoď řádky $k$ a $l$.
> 3. Pro každé $i > l$ odečti od $i$-tého řádku $\dfrac{b_{ij}}{b_{lj}}$-násobek $l$-tého. Polož $l = l + 1$, $j = j + 1$ a vrať se ke kroku 1.
>
> Výsledná matice je v horním stupňovitém tvaru a pivoty jsou čísla $b_{lj}$ z kroku 3.

^def-gaussova-eliminace

> [!lidsky] Lidsky
> Jdi sloupec po sloupci zleva. V aktuálním sloupci si vyber nenulové číslo (pivot), přesuň jeho řádek nahoru do „pracovní pozice“ a odečítáním jeho násobků vynuluj všechno pod ním. Pak ten řádek i sloupec „zamkni“ a pokračuj v menší matici vpravo dole.

> [!example] Příklad (úloha 8.11)
> Soustava s rozšířenou maticí
>
> $$
> \left(\begin{array}{cccc|c} 1 & 2 & -1 & 3 & 2 \\ 2 & 4 & 0 & 1 & 3 \\ 0 & -1 & 2 & -1 & 3 \\ 1 & 0 & 1 & -2 & 1 \end{array}\right)
> \sim
> \left(\begin{array}{cccc|c} 1 & 2 & -1 & 3 & 2 \\ 0 & 0 & 2 & -5 & -1 \\ 0 & -1 & 2 & -1 & 3 \\ 0 & -2 & 2 & -5 & -1 \end{array}\right)
> $$
>
> ($r_2 - 2r_1$, $r_4 - r_1$). Ve 2. sloupci je na pracovní pozici nula, proto **prohodíme** $r_2$ a $r_3$ (krok 2) a pak $r_4 - 2r_2$; nakonec ve 3. sloupci $r_4 + r_3$:
>
> $$
> \sim
> \left(\begin{array}{cccc|c} 1 & 2 & -1 & 3 & 2 \\ 0 & -1 & 2 & -1 & 3 \\ 0 & 0 & 2 & -5 & -1 \\ 0 & 0 & -2 & -3 & -7 \end{array}\right)
> \sim
> \left(\begin{array}{cccc|c} 1 & 2 & -1 & 3 & 2 \\ 0 & -1 & 2 & -1 & 3 \\ 0 & 0 & 2 & -5 & -1 \\ 0 & 0 & 0 & -8 & -8 \end{array}\right).
> $$
>
> Všechny 4 sloupce $A$ jsou hlavní: $\operatorname{rank} A = \operatorname{rank}(A \mid \vec{b}) = 4$, $\dim S_0 = 0$, řešení je právě jedno. Zpětná substituce: $-8x_4 = -8$, $x_4 = 1$; $2x_3 - 5 = -1$, $x_3 = 2$; $-x_2 + 4 - 1 = 3$, $x_2 = 0$; $x_1 + 0 - 2 + 3 = 2$, $x_1 = 1$. **$S = \{(1; 0; 2; 1)\}$**; dosazení do původních čtyř rovnic: $1 - 2 + 3 = 2$, $2 + 1 = 3$, $4 - 1 = 3$, $1 + 2 - 2 = 1$. ✓

> [!navic] Místo zpětné substituce: úpravy až do konce
> Úpravy se dají dotáhnout i nahoru: vydělit poslední řádek $-8$, odečíst jeho násobky od řádků nad ním, pak totéž s třetím řádkem atd. Skončíš u
>
> $$
> \left(\begin{array}{cccc|c} 1 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 1 \end{array}\right)
> $$
>
> a řešení $(1; 0; 2; 1)$ přečteš za čarou. Tento postup (Gaussova–Jordanova eliminace, redukovaný stupňovitý tvar) je v poznámkách jako algoritmus 8.12; výpočetně dělá totéž co zpětná substituce.

> [!navic] Celý postup řešení soustavy $A\vec{x} = \vec{b}$
> 1. Gaussovou eliminací převeď $(A \mid \vec{b})$ na stupňovitý tvar.
> 2. Je-li pivot ve sloupci pravých stran (řádek $(0 \cdots 0 \mid c)$ s $c \ne 0$), je $\operatorname{rank}(A \mid \vec{b}) > \operatorname{rank} A$: **řešení neexistuje**.
> 3. Jinak: neznámé u vedlejších sloupců jsou parametry. Volbou „jeden parametr $= 1$, ostatní $= 0$“ s nulovou pravou stranou získáš bázi $S_0$, volbou „všechny parametry $= 0$“ partikulární řešení $\vec{x}_p$.
> 4. Výsledek: $S = \vec{x}_p + S_0$, případně v parametrickém tvaru.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Dokaž bod 2 Frobeniovy věty: $A\vec{x} = \vec{b}$ má řešení, právě když $\operatorname{rank} A = \operatorname{rank}(A \mid \vec{b})$.
> Řešení existuje $\Leftrightarrow$ $\vec{b} \in \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n\}$ $\Leftrightarrow$ **$\operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n\} = \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n, \vec{b}\}$**. Levý obal leží v pravém, takže rovnost nastane, právě když mají **stejnou dimenzi**; ty jsou $\operatorname{rank} A$ a $\operatorname{rank}(A \mid \vec{b})$.

> [!karta|02]- Jak z hodností $\operatorname{rank} A$, $\operatorname{rank}(A \mid \vec{b})$ a počtu neznámých $n$ poznáš, kolik řešení má soustava $A\vec{x} = \vec{b}$?
> $\operatorname{rank}(A \mid \vec{b}) > \operatorname{rank} A$: **žádné**. Jinak $S = \vec{x}_p + S_0$ s $\dim S_0 = n - \operatorname{rank} A$: při $\operatorname{rank} A = n$ **právě jedno**, při $\operatorname{rank} A < n$ tolik jako prvků $S_0$, nad $\mathbb{R}$ **nekonečně mnoho** s $n - \operatorname{rank} A$ parametry.

> [!karta|03]- Proč je $\operatorname{rank}(A \mid \vec{b})$ vždy buď $\operatorname{rank} A$, nebo $\operatorname{rank} A + 1$?
> $\operatorname{im}(A \mid \vec{b}) = \operatorname{span}\{\vec{a}_1, \dots, \vec{a}_n, \vec{b}\}$ obsahuje $\operatorname{im} A$ a vznikne **přidáním jediného vektoru**. Báze $\operatorname{im} A$ se tím buď nezmění ($\vec{b} \in \operatorname{im} A$), nebo se **prodlouží právě o $\vec{b}$** (přidání vektoru mimo obal k LN posloupnosti zachová LN).

> [!karta|04]- Dokaž, že hlavní sloupce matice v horním stupňovitém tvaru tvoří bázi jejího obrazu.
> **LN:** $i$-tý hlavní sloupec má v $i$-tém řádku pivot $\ne 0$, všechny předchozí sloupce tam mají $0$, takže **není kombinací předchozích**. **Generují:** všechny sloupce mají nuly pod $r$-tým řádkem, takže $\dim \operatorname{im} A \le r$; $r$ LN vektorů v prostoru dimenze $\le r$ je báze.

> [!karta|05]- Dokaž, že přičtení $\alpha$-násobku $l$-tého řádku ke $k$-tému nemění množinu řešení soustavy.
> Splňuje-li $\vec{x}$ obě rovnice, splňuje i **jejich kombinaci** $r_k + \alpha r_l$. Naopak z nové $k$-té a **nezměněné $l$-té** rovnice dostaneš původní $k$-tou odečtením $\alpha$-násobku $l$-té. Úprava je **vratná**, takže obě soustavy mají stejná řešení.

> [!karta|06]- Proč elementární řádková úprava „vynásob řádek skalárem“ vyžaduje nenulový skalár?
> Násobení nulou je **nevratné**: rovnice se změní na $0 = 0$ a zmizí, množina řešení se může **zvětšit** (např. z bodu na přímku). Pro $\alpha \ne 0$ jde krok vrátit násobením $\alpha^{-1}$.

> [!karta|07]- Které z $\ker A$, $\operatorname{im} A$, $\operatorname{rank} A$ se mění elementárními řádkovými úpravami?
> **$\ker A$ ne** (množina řešení $A\vec{x} = \vec{0}$ se nemění), tedy **ani $\operatorname{rank} A = n - \operatorname{def} A$**. **$\operatorname{im} A$ ano**: $\begin{pmatrix} 1 \\ 1 \end{pmatrix} \sim \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ mění obal sloupců.

> [!karta|08]- Jak z horního stupňovitého tvaru rozšířené matice $(A \mid \vec{b})$ poznáš, že soustava nemá řešení?
> **Pivot leží ve sloupci pravých stran**, tj. vznikl řádek $(0 \cdots 0 \mid c)$ s $c \ne 0$ (rovnice $0 = c$). Pak je $\operatorname{rank}(A \mid \vec{b}) = \operatorname{rank} A + 1$.

> [!karta|09]- Jak najdeš bázi $S_0$ ze stupňovitého tvaru a proč jsou nalezené vektory LN?
> Neznámé u **vedlejších sloupců** jsou volné. Pro každou z nich polož ji $= 1$, ostatní volné $= 0$, a zbytek dopočítej zpětnou substitucí. Vektory jsou LN, protože na pozicích volných neznámých tvoří **kanonickou bázi**; je jich $n - r = \dim S_0$, takže generují.

> [!karta|10]- Proč je dimenze množiny řešení homogenní soustavy rovna počtu vedlejších sloupců stupňovitého tvaru matice soustavy?
> Úpravy nemění $S_0$. Ve stupňovitém tvaru je **$\operatorname{rank} A$ = počet hlavních sloupců** (věta 8.6), takže podle Frobeniovy věty $\dim S_0 = n - \operatorname{rank} A$ = **počet vedlejších sloupců**.

> [!karta|11]- Má homogenní soustava s víc neznámými než rovnicemi vždy nenulové řešení? A nehomogenní vždy nějaké řešení?
> **Homogenní ano:** $\operatorname{rank} A \le m < n$, tedy $\dim S_0 = n - \operatorname{rank} A \ge 1$. **Nehomogenní ne:** $x + y = 1$, $x + y = 2$ má $\operatorname{rank} A = 1 < 2 = \operatorname{rank}(A \mid \vec{b})$, žádné řešení.

> [!karta|12]- Jak Gaussovou eliminací najdeš bázi $\operatorname{im} A$ a proč nestačí vzít hlavní sloupce upravené matice?
> Eliminací urči, které sloupce jsou hlavní ($k_1, \dots, k_r$), a vezmi **sloupce původní matice $A$ na těchto pozicích**. Řádkové úpravy **mění $\operatorname{im} A$**, ale zachovávají lineární vztahy mezi sloupci (řešení $A\vec{x} = \vec{0}$), takže LN i počet sedí jen pro tytéž indexy.

### Příklady na procvičení

> [!priklad|13]- Vyřeš podle Frobeniovy věty rovnici $2x + y - z = 4$ nad $\mathbb{R}$.
> $\operatorname{rank} A = \operatorname{rank}(A \mid \vec{b}) = 1$, řešení existuje, $\dim S_0 = 3 - 1 = 2$. Volné $x, z$ (z rovnice $y = -2x + z$): $(x; z) = (1; 0) \Rightarrow (1; -2; 0)$, $(0; 1) \Rightarrow (0; 1; 1)$. Partikulární $x = z = 0$, $y = 4$.
>
> **$S = (0; 4; 0) + \operatorname{span}\{(1; -2; 0), (0; 1; 1)\}$**, parametricky $x = t$, $y = 4 - 2t + s$, $z = s$.

> [!priklad|14]- Je $\begin{pmatrix} 0 & 3 & 1 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ v horním stupňovitém tvaru? Urči hlavní a vedlejší sloupce, pivoty a hodnost.
> **Ano:** $r = 2$, $k_1 = 2 < k_2 = 4$, nulový řádek je dole. **Hlavní sloupce 2 a 4, vedlejší 1 a 3, pivoty $3$ na $(1, 2)$ a $2$ na $(2, 4)$, $\operatorname{rank} = 2$.**

> [!priklad|15]- Je $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ v horním stupňovitém tvaru?
> **Ne.** První nenulové číslo řádků je ve sloupcích $1, 3, 2$, ale musí jít **striktně doprava** ($k_3 = 2 < k_2 = 3$). Prohozením 2. a 3. řádku tvar získáš, hodnost je 3.

> [!priklad|16]- Gaussovou eliminací vyřeš soustavu $x + y + z = 6$, $2x + 3y + z = 11$, $x + 2y + 3z = 14$.
> $\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & 3 & 1 & 11 \\ 1 & 2 & 3 & 14 \end{array}\right) \sim \left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -1 & -1 \\ 0 & 1 & 2 & 8 \end{array}\right) \sim \left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 3 & 9 \end{array}\right)$ ($r_2 - 2r_1$, $r_3 - r_1$, pak $r_3 - r_2$). Zpětně $z = 3$, $y = -1 + 3 = 2$, $x = 6 - 2 - 3 = 1$.
>
> **$S = \{(1; 2; 3)\}$**, rank 3, právě jedno řešení.

> [!priklad|17]- Rozhodni podle Frobeniovy věty, zda má soustava $x + 2y = 3$, $2x + 4y = 5$ řešení.
> $\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 5 \end{array}\right) \sim \left(\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & -1 \end{array}\right)$: pivot ve sloupci pravých stran, $\operatorname{rank} A = 1 < 2 = \operatorname{rank}(A \mid \vec{b})$. **Řešení neexistuje** (rovnoběžné přímky).

> [!priklad|18]- Vyřeš soustavu $x_1 + 2x_2 - x_3 + x_4 = 1$, $2x_1 + 4x_2 - x_3 + 3x_4 = 4$.
> $r_2 - 2r_1$: $\left(\begin{array}{cccc|c} 1 & 2 & -1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 2 \end{array}\right)$. Hlavní sloupce 1, 3, volné $x_2, x_4$; rank 2, $\dim S_0 = 4 - 2 = 2$. Z rovnic $x_3 = -x_4$ (homogenní) a $x_1 = -2x_2 + x_3 - x_4$: $x_2 = 1 \Rightarrow (-2; 1; 0; 0)$, $x_4 = 1 \Rightarrow x_3 = -1$, $x_1 = -2$, tedy $(-2; 0; -1; 1)$. Partikulární $x_2 = x_4 = 0$: $x_3 = 2$, $x_1 = 1 + 2 = 3$.
>
> **$S = (3; 0; 2; 0) + \operatorname{span}\{(-2; 1; 0; 0), (-2; 0; -1; 1)\}$.**

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|19]- Gaussovou eliminací urči hodnost, defekt, bázi jádra a obrazu $f : \mathbb{R}^3 \to \mathbb{R}^3$, $f(\vec{x}) = A\vec{x}$, $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 3 \\ 1 & 3 & 2 \end{pmatrix}$. Je $f$ mono- nebo epimorfismus?
> $r_2 - 2r_1$, $r_3 - r_1$, pak $r_3 - r_2$: $\begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$. Hlavní sloupce 1, 2, **$\operatorname{rank} f = 2$**, báze $\operatorname{im} f$ = sloupce **původní** matice: $\big((1; 2; 1), (2; 5; 3)\big)$. Jádro: $z = t$, $y = -t$, $x = -2y - z = t$, báze $\ker f$ je $\big((1; -1; 1)\big)$, **$\operatorname{def} f = 1$**; kontrola $3 = 2 + 1$.
>
> **Není mono** ($\ker f \ne \{\vec{0}\}$) **ani epi** ($\operatorname{rank} f = 2 < 3$).

> [!priklad|20]- Rozhodni, zda je $f : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^3$, $f(p) = (p(0); p(1); p(2))$ izomorfismus.
> Pro $p = a + bx + cx^2$ je $f(p) = (a;\ a + b + c;\ a + 2b + 4c)$, tedy $[f]$ v bázích $(1, x, x^2)$ a kanonické je $\begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 2 & 4 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$. Tři pivoty: $\operatorname{rank} f = 3 = \dim \mathbb{R}^3$ (epi) a $\operatorname{def} f = 3 - 3 = 0$ (mono).
>
> **Ano, $f$ je izomorfismus.**

> [!priklad|21]- Najdi bázi a dimenzi $L = \operatorname{span}\{(1; 2; 0; 1), (2; 4; 1; 3), (0; 0; 1; 1), (1; 2; 1; 2)\} \le \mathbb{R}^4$.
> Vektory dej do sloupců a eliminuj: $\begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 0 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 3 & 1 & 2 \end{pmatrix} \sim \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ ($r_2 - 2r_1$, $r_4 - r_1$, prohodit, $r_4 - r_2$). Hlavní sloupce 1, 2.
>
> **$\dim L = 2$, báze $\big((1; 2; 0; 1), (2; 4; 1; 3)\big)$.** Kontrola: $(0; 0; 1; 1) = (2; 4; 1; 3) - 2(1; 2; 0; 1)$ a $(1; 2; 1; 2) = (1; 2; 0; 1) + (0; 0; 1; 1)$.

> [!priklad|22]- Je $(1 + x,\ x + x^2,\ 1 + 2x + x^2)$ báze $\mathbb{R}^{\le 2}[x]$?
> Souřadnice v bázi $(1, x, x^2)$ dej do sloupců: $\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 0 & 1 & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix} \sim \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$: hodnost 2 < 3, třetí sloupec je vedlejší.
>
> **Není**, polynomy jsou LZ: $1 + 2x + x^2 = (1 + x) + (x + x^2)$.

---
← [[LAG 11 – Jádro, obraz, hodnost a defekt|30. 10. 2026 Jádro, obraz, hodnost a defekt]]

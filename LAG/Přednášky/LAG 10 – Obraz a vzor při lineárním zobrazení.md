---
predmet: LAG
prednaska: 10
datum: 2026-10-23
zdroj: "V poznámkách kap. 6.4 (pozn. 6.32–6.35) a 7 (pozn. 7.1–7.5)"
tags: [prednaska, LAG]
---

# LAG 10 – Obraz a vzor při lineárním zobrazení

*Přednáška 10 · pátek 23. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `distributivita` · `(αA)B = α(AB) = A(αB)` · `bilinearita součinu` · `vzor vektoru = řešení soustavy` · `im A` · `soustava, kombinace, vzor` · `definiční obor a cílová množina` · `obraz a vzor množiny` · `prosté, na, bijekce` · `inverzní zobrazení`

Minule se z $\operatorname{Lin}(V, W)$ stal lineární prostor: zobrazení umíme sčítat a násobit číslem. Dnes nejdřív dořešíme, jak se sčítání a násobení číslem snáší se skládáním (distributivita, bilinearita). Pak začne kapitola 7: na matici, která rovinu „splácne“ do přímky, uvidíme, že **hledat vzor vektoru je totéž co řešit soustavu**, a srovnáme tři pohledy na jednu úlohu. Nakonec si zopakujeme obecné pojmy o zobrazeních (cílová množina, obraz a vzor množiny, prosté, na, bijekce, inverze), tentokrát přesně.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| [[distributivita skládání a sčítání]] | $(A + B)C = AC + BC$, $A(C + D) = AC + AD$ | |
| [[vytýkání skaláru ze součinu]] | $(\alpha A)B = \alpha(AB) = A(\alpha B)$ | $(\tfrac{\sqrt{2}}{2}A)(\sqrt{2}E) = A$ |
| [[bilineární zobrazení]] | lineární v každém argumentu zvlášť | $(X, Y) \mapsto XY$ |
| vzor vektoru = řešení soustavy | $A\vec{x} = \vec{b}$ | $A^{-1}\{(-3; 0)\} = \{(-3; 0)\} + \operatorname{span}\{(1; 1)\}$ |
| [[zobrazení]] | $f \subseteq A \times B$, ke každému $x$ právě jedno $y$ | |
| [[cílová množina]] | kam $f$ zobrazuje, nemusí být celá zasažena | $x^2 : \mathbb{R} \to \mathbb{R}$ |
| [[obor hodnot]] | $f(A) = \{f(x) \mid x \in A\}$ | $\operatorname{im}\begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} = \operatorname{span}\{(1; 0)\}$ |
| [[obraz množiny]] | $f(M) = \{f(x) \mid x \in M\}$ | $f([-1; 2]) = [0; 4]$ pro $x^2$ |
| [[vzor množiny]] | $f^{-1}(N) = \{x \in A \mid f(x) \in N\}$ | $f^{-1}([1; 4]) = [-2; -1] \cup [1; 2]$ |
| [[injektivní zobrazení]] | $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$ | $2x + 1$ ano, $x^2$ ne |
| [[surjektivní zobrazení]] | $f(A) = B$ | $x^2 : \mathbb{R} \to [0; +\infty)$ |
| [[bijekce]] | prosté a na | $2x + 1 : \mathbb{R} \to \mathbb{R}$ |
| [[inverzní zobrazení]] | $f^{-1}(y) = x$, kde $f(x) = y$ | $f^{-1}(y) = \tfrac{y - 1}{2}$ |

## §1 Distributivita a bilinearita

Sčítání a násobení číslem máme pro zobrazení i matice, skládání (součin) taky. Jak spolu tyto operace počítají?

> [!veta] Věta 6.32 (distributivita)
> ==Buďte $U$, $V$, $W$ lineární prostory nad $\mathbb{F}$.== Potom pro libovolná $A, B \in \operatorname{Lin}(V, W)$ a $C, D \in \operatorname{Lin}(U, V)$ platí
>
> $$
> \mathbf{(A + B)C = AC + BC, \qquad A(C + D) = AC + AD.}
> $$
>
> V důsledku pro matice $A, B \in \mathbb{F}^{l \times m}$, $C, D \in \mathbb{F}^{m \times n}$ platí **$(A + B)C = AC + BC$** a **$A(C + D) = AC + AD$**.
>
> > [!note]- Důkaz
> > Vezmeme libovolné $\vec{x} \in U$. První zákon plyne jen z definice [[součet lineárních zobrazení|součtu zobrazení]]:
> >
> > $$
> > \big((A + B)C\big)\vec{x} = (A + B)(C\vec{x}) = AC\vec{x} + BC\vec{x} = (AC + BC)\vec{x}.
> > $$
> >
> > Druhý zákon potřebuje navíc **linearitu $A$**:
> >
> > $$
> > \big(A(C + D)\big)\vec{x} = A(C\vec{x} + D\vec{x}) = AC\vec{x} + AD\vec{x} = (AC + AD)\vec{x}.
> > $$
> >
> > Maticová verze plyne ze zobrazení, protože součet matic odpovídá součtu zobrazení a součin matic složení ([[věta o matici součtu a násobku zobrazení]], [[věta o matici složeného zobrazení]]).

^veta-distributivita

> [!lidsky] Lidsky
> Závorky jde „roznásobit“ jako u čísel: $(a + b)c = ac + bc$. Jen **pořadí** činitelů musí zůstat: $C(A + B) = CA + CB$ platí taky, ale $CA$ se nesmí přepsat na $AC$.

> [!example] Příklad
> $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $C = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$. Napřed $A + B = \begin{pmatrix} 1 & 3 \\ 1 & 1 \end{pmatrix}$ a $(A + B)C = \begin{pmatrix} 5 & 10 \\ 3 & 4 \end{pmatrix}$. Jinak: $AC = \begin{pmatrix} 4 & 7 \\ 1 & 3 \end{pmatrix}$, $BC = \begin{pmatrix} 1 & 3 \\ 2 & 1 \end{pmatrix}$ a $AC + BC = \begin{pmatrix} 5 & 10 \\ 3 & 4 \end{pmatrix}$. Vyšlo totéž.

> [!pozor] Proč u druhého zákona záleží na linearitě
> Pro nelineární zobrazení první zákon platí pořád (je to jen definice součtu), druhý ne. Pro $f(t) = t^2$ na $\mathbb{R}$ a $C = D = \mathrm{id}$ je $f \circ (C + D) : t \mapsto (2t)^2 = 4t^2$, ale $f \circ C + f \circ D : t \mapsto 2t^2$.

> [!veta] Věta 6.33 (skalár a skládání)
> ==Buďte $U$, $V$, $W$ lineární prostory nad $\mathbb{F}$.== Potom pro libovolná $A \in \operatorname{Lin}(V, W)$, $B \in \operatorname{Lin}(U, V)$ a $\alpha \in \mathbb{F}$ platí
>
> $$
> \mathbf{(\alpha A)B = \alpha(AB) = A(\alpha B).}
> $$
>
> V důsledku totéž platí pro matice $A \in \mathbb{F}^{l \times m}$, $B \in \mathbb{F}^{m \times n}$ a $\alpha \in \mathbb{F}$.
>
> > [!note]- Důkaz
> > Pro $\vec{x} \in U$: $((\alpha A)B)\vec{x} = \alpha(A(B\vec{x})) = (\alpha(AB))\vec{x}$ z definice násobku, a $(A(\alpha B))\vec{x} = A(\alpha B\vec{x}) = \alpha A(B\vec{x})$ z linearity $A$.

^veta-skalar-skladani

> [!lidsky] Lidsky
> Číslo smíš ze součinu **vytknout** dopředu, ať stojí u kteréhokoli činitele. U matic to ušetří práci se zlomky a odmocninami.

> [!example] Příklad
> Z minula: $\big(\tfrac{\sqrt{2}}{2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\big)\big(\sqrt{2}E\big) = \tfrac{\sqrt{2}}{2} \cdot \sqrt{2} \cdot \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}E = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, tedy $R_{45°} \circ S_{\sqrt{2}} = A$ bez násobení odmocnin po prvcích.

> [!navic] Slovník matice ↔ zobrazení
> | matice | zobrazení |
> | --- | --- |
> | součin $AB$ | složení $A \circ B$ |
> | součet $A + B$ | součet $A + B$ |
> | násobek $\alpha A$ | násobek $\alpha A$ |
>
> Každé pravidlo pro jedno platí i pro druhé, třeba $\gamma(A + B) = \gamma A + \gamma B$ nebo $C(A + B) = CA + CB$.

> [!definice] Poznámka · pozn. 6.35 · bilineární zobrazení
> Zobrazení dvou vektorových proměnných $f : V_1 \times V_2 \to W$ se nazývá *bilineární*, je-li lineární v každém argumentu zvlášť:
>
> $$
> f(\vec{a}, \alpha\vec{x} + \vec{y}) = \alpha f(\vec{a}, \vec{x}) + f(\vec{a}, \vec{y}), \qquad f(\alpha\vec{x} + \vec{y}, \vec{b}) = \alpha f(\vec{x}, \vec{b}) + f(\vec{y}, \vec{b})
> $$
>
> pro všechna $\vec{a}, \vec{x}, \vec{y}$, $\vec{b}$ z příslušných prostorů a $\alpha \in \mathbb{F}$. Věty 6.32 a 6.33 říkají, že **násobení matic $\mathbb{F}^{l \times m} \times \mathbb{F}^{m \times n} \to \mathbb{F}^{l \times n}$, $(X, Y) \mapsto XY$, je bilineární**: pro pevné $A$ je $X \mapsto AX$ lineární a pro pevné $B$ je $X \mapsto XB$ lineární.

^def-bilinearni

> [!lidsky] Lidsky
> Zafixuješ jeden argument a ve druhém se zobrazení chová lineárně. Obě proměnné **najednou** ale lineární být nemusí: $2A \cdot 2B = 4AB$, ne $2AB$.

> [!example] Příklad
> Součin čísel $f(a, b) = ab$ na $\mathbb{R} \times \mathbb{R}$ je bilineární: pro pevné $a = 3$ je $b \mapsto 3b$ lineární. Ale není lineární jako zobrazení $\mathbb{R}^2 \to \mathbb{R}$: $f(2, 2) = 4 \ne 2f(1, 1) = 2$. Nepříklad: $g(a, b) = a + b$ bilineární není, pro pevné $a = 1$ je $b \mapsto 1 + b$ posunutí a nepošle $0$ na $0$.

## §2 Obraz a vzor: příklad

Hledat **vzor** vektoru $\vec{b}$ při zobrazení daném maticí $A$, tj. všechna $\vec{x}$ s $A\vec{x} = \vec{b}$, znamená řešit soustavu (pozn. 7.1):

$$
\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix} \quad\Longleftrightarrow\quad \begin{aligned} \alpha x + \beta y &= a \\ \gamma x + \delta y &= b \end{aligned}
$$

> [!example] Příklad 7.2 · $A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix} : \mathbb{R}^2 \to \mathbb{R}^2$
> **Obraz.** $A\begin{pmatrix} x \\ y \end{pmatrix} = x\begin{pmatrix} 1 \\ 0 \end{pmatrix} + y\begin{pmatrix} -1 \\ 0 \end{pmatrix}$, takže oba sloupce leží na ose $x$ a celá rovina se „splácne“ do osy $x$:
>
> $$
> \operatorname{im} A = \operatorname{span}\Big\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \end{pmatrix}\Big\} = \operatorname{span}\Big\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}\Big\} \le \mathbb{R}^2.
> $$
>
> **Vzor bodu $(-3; 0)$.** Řešíme $A\vec{x} = (-3; 0)$:
>
> $$
> \begin{aligned} 1 \cdot x - 1 \cdot y &= -3 \\ 0 \cdot x + 0 \cdot y &= 0 \end{aligned}
> $$
>
> Druhá rovnice nic neříká, zbývá $x - y = -3$. S parametrem $y = t$ je $x = t - 3$, tedy
>
> $$
> A^{-1}\Big\{\begin{pmatrix} -3 \\ 0 \end{pmatrix}\Big\} = \Big\{\begin{pmatrix} t - 3 \\ t \end{pmatrix} \Bigm\vert t \in \mathbb{R}\Big\} = \Big\{\begin{pmatrix} -3 \\ 0 \end{pmatrix} + t\begin{pmatrix} 1 \\ 1 \end{pmatrix} \Bigm\vert t \in \mathbb{R}\Big\} = \Big\{\begin{pmatrix} -3 \\ 0 \end{pmatrix}\Big\} + \operatorname{span}\Big\{\begin{pmatrix} 1 \\ 1 \end{pmatrix}\Big\}.
> $$
>
> **Obecně** pro bod $(a; 0)$ z obrazu: $A^{-1}\{(a; 0)\} = \{(a; 0)\} + \operatorname{span}\{(1; 1)\}$, přímka $x - y = a$. Bod mimo osu $x$, třeba $(0; 1)$, nemá vzor žádný: druhá rovnice by byla $0 = 1$.

> [!obrazek] Kam se co zobrazí
> ![[lag10-vzory.png]]
> *Vlevo vzory: červená přímka $x - y = -3$ se celá zobrazí do červeného bodu $(-3; 0)$ (třeba $(-1; 2) \mapsto (-3; 0)$), zelená přímka $x - y = 0$ do nuly, modrá $x - y = 2$ do $(2; 0)$. Vpravo obraz: celá rovina skončí na oranžové ose $x$. Zobrazení tedy promítá rovinu na osu $x$ pod úhlem $45°$.*

> [!lidsky] Lidsky
> $A$ si z vektoru pamatuje jen rozdíl $x - y$. Všechny body se stejným rozdílem (jedna přímka se směrem $(1; 1)$) proto skončí v tomtéž bodě. Vzor bodu je celá přímka, ne jeden bod, a bod mimo osu $x$ nemá vzor vůbec.

Zápis $\{\vec{x}_p\} + \operatorname{span}\{\dots\}$ je [[součet podprostorů|součet množin]] $M + N = \{\vec{a} + \vec{b} \mid \vec{a} \in M, \vec{b} \in N\}$: každý bod $\vec{x}_p$ plus cokoli z obalu.

> [!navic] Co z příkladu platí obecně (přesně v kap. 7)
> - **Vzor nulového vektoru je vždy podprostor.** Je to množina řešení [[homogenní soustava|homogenní soustavy]] (zde přímka $x - y = 0$).
> - **Vzor každého jiného bodu je jen posunutý vzor nuly.** Je-li $A\vec{x}_0 = \vec{0}$ a $A\vec{x}_p = \vec{b}$, pak $A(\vec{x}_p + \vec{x}_0) = \vec{b} + \vec{0} = \vec{b}$. V příkladu: sečtením $x_0 - y_0 = 0$ a $x_p - y_p = a$ dostaneme $(x_0 + x_p) - (y_0 + y_p) = a$.

## §3 Tři pohledy na jednu úlohu

Tutéž úlohu jde zapsat třikrát: jako soustavu, jako hledání lineární kombinace sloupců a jako hledání vzoru (tabulka 7.1, cvičení 7.3).

| soustava $\begin{aligned} \alpha x + \beta y &= a \\ \gamma x + \delta y &= b \end{aligned}$ | lineární kombinace $x\begin{pmatrix} \alpha \\ \gamma \end{pmatrix} + y\begin{pmatrix} \beta \\ \delta \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix}$ | vzor $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix}$ |
| --- | --- | --- |
| má aspoň 1 řešení | $(a; b) \in \operatorname{span}\{(\alpha; \gamma), (\beta; \delta)\}$ | $(a; b) \in \operatorname{im} A$ |
| má aspoň 1 řešení pro každé $a, b$ | $(\alpha; \gamma)$, $(\beta; \delta)$ [[generující posloupnost\|generují]] $\mathbb{R}^2$ | $\operatorname{im} A = \mathbb{R}^2$ ($A$ je na) |
| má nejvýš 1 řešení pro každé $a, b$ | $(\alpha; \gamma)$, $(\beta; \delta)$ jsou [[lineární nezávislost\|LN]] | $A$ je prosté |
| má právě 1 řešení pro každé $a, b$ | $(\alpha; \gamma)$, $(\beta; \delta)$ tvoří [[báze\|bázi]] $\mathbb{R}^2$ | $A$ je bijekce $\mathbb{R}^2 \to \mathbb{R}^2$ |

> [!lidsky] Lidsky
> Řádek tabulky čti napříč: tři různé věty říkají totéž. Kapitoly o LN, bázích a dimenzi byly o prostředním sloupci, kapitola 7 je o pravém. Spoustu vět proto už vlastně známe, jen v jiném jazyce.

> [!example] Příklad
> Pro $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ jsou sloupce $(1; 3)$, $(2; 4)$ LN (nejsou násobkem jeden druhého), tedy báze $\mathbb{R}^2$. Soustava má proto pro každou pravou stranu právě jedno řešení, třeba pro $(5; 6)$ je to $(x; y) = (-4; \tfrac{9}{2})$, a zobrazení je bijekce. Pro $A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$ z §2 sloupce LN nejsou ani negenerují $\mathbb{R}^2$: soustava má buď nekonečně mnoho řešení, nebo žádné.

## §4 Zobrazení obecně

> [!definice] Připomenutí · pozn. 7.4 · zobrazení, definiční obor, cílová množina
> Zápis $f : A \to B$ znamená, že $f$ je *zobrazení*, $A$ je jeho *definiční obor* a $B$ jeho *cílová množina*, tj. $f(x) \in B$ pro každé $x \in A$. Formálně je zobrazení množina dvojic $f \subseteq A \times B$ taková, že
>
> $$
> \forall x \in A\ \exists!\, y \in B : (x, y) \in f,
> $$
>
> a místo $(x, y) \in f$ píšeme $f(x) = y$. Definiční obor je nedílnou součástí zadání zobrazení. Cílová množina se nemusí shodovat s oborem hodnot: může existovat $y \in B$, na které se nic nezobrazí.

^def-zobrazeni

> [!lidsky] Lidsky
> Zobrazení je **tabulka dvojic „vstup → výstup“**, ve které má každý vstup z $A$ přesně jeden výstup. Cílová množina $B$ je „terč“, do kterého se střílí; nemusí být zasažena celá.

> [!example] Příklad
> $f = \{(1, a), (2, a), (3, c)\}$ je zobrazení $\{1, 2, 3\} \to \{a, b, c\}$: každý vstup má jeden výstup, $b$ nezasáhne nic. Nepříklad: $\{(1, a), (1, b), (2, c), (3, c)\}$ zobrazení není, $1$ má dva výstupy; $\{(1, a), (2, c)\}$ taky ne, $3$ nemá žádný.

> [!definice] Definice · pozn. 7.4 · obraz a vzor množiny, obor hodnot
> Buď $f : A \to B$ zobrazení.
>
> - Pro $M \subseteq A$ definujeme *obraz množiny* $M$ jako $f(M) = \{f(x) \mid x \in M\}$.
> - Speciálně pro $M = A$ dostáváme *obor hodnot* $f(A) = \{f(x) \mid x \in A\}$.
> - Pro $N \subseteq B$ definujeme *vzor množiny* $N$ jako $f^{-1}(N) = \{x \in A \mid f(x) \in N\}$.

^def-obraz-vzor-mnoziny

> [!lidsky] Lidsky
> **Obraz** je „kam se dostanou body z $M$“, **vzor** je „odkud se dá dostat do $N$“. Obor hodnot jsou všechna místa terče, která jsou opravdu zasažená.

> [!example] Příklad
> Pro $f(x) = x^2$ na $\mathbb{R}$: $f([-1; 2]) = [0; 4]$, $f^{-1}([1; 4]) = [-2; -1] \cup [1; 2]$, $f^{-1}(\{-1\}) = \emptyset$ a obor hodnot je $f(\mathbb{R}) = [0; +\infty)$. U matice z §2 je obor hodnot osa $x$ a vzor bodu $(-3; 0)$ přímka $x - y = -3$.

> [!pozor] $f^{-1}(N)$ existuje vždy
> Vzor množiny je definovaný pro **každé** zobrazení, i když inverzní zobrazení neexistuje. $f^{-1}(\{4\}) = \{-2, 2\}$ pro $x^2$ je v pořádku; zápis $f^{-1}(4)$ (číslo místo množiny) by smysl neměl.

> [!definice] Definice · pozn. 7.4 · prosté, na, bijektivní
> Zobrazení $f : A \to B$ nazýváme
>
> - *prosté* neboli *injektivní*, jestliže $\forall x_1, x_2 \in A : x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$, ekvivalentně $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$; ekvivalentně je pro každé $y \in B$ vzor $f^{-1}(\{y\})$ nanejvýš jednoprvkový,
> - *na* neboli *surjektivní*, jestliže $f(A) = B$, tj. $\forall y \in B\ \exists x \in A : f(x) = y$,
> - *bijektivní*, jestliže platí obojí, tj. $\forall y \in B\ \exists!\, x \in A : f(x) = y$.

^def-prosta-na-bijekce

> [!lidsky] Lidsky
> **Prosté**: žádné dva vstupy nemají stejný výstup, každý zásah terče je od nejvýš jednoho střelce. **Na**: zasažený je celý terč. **Bijekce**: obojí, takže prvky $A$ a $B$ jsou spárované jedna ku jedné.

> [!example] Příklady
> - $f : \mathbb{R} \to \mathbb{R}$, $f(x) = 2x + 1$ je bijekce: $2x_1 + 1 = 2x_2 + 1 \Rightarrow x_1 = x_2$ a k $y$ je $x = \tfrac{y - 1}{2}$.
> - $g : \mathbb{Z} \to \mathbb{Z}$, $g(n) = 2n$ je prosté, ale ne na: liché číslo $3$ nemá vzor.
> - $h : \mathbb{R} \to [0; +\infty)$, $h(x) = x^2$ je na, ale ne prosté: $h(-2) = h(2) = 4$.
> - $x^2 : \mathbb{R} \to \mathbb{R}$ není ani prosté, ani na ($-1$ nemá vzor). Stejný předpis, jiná cílová množina, jiná odpověď na „je na?“.

> [!obrazek] Čtyři možnosti
> ![[lag10-prosta-na.png]]
> *Modré body jsou definiční obor $A$, oranžové cílová množina $B$, zelené šipky zobrazení. Červený bod v $B$ nemá vzor (zobrazení není na); dvě šipky do jednoho bodu znamenají, že zobrazení není prosté.*

> [!definice] Definice · pozn. 7.4 · inverzní zobrazení
> Je-li $f : A \to B$ bijekce (a jen tehdy), definujeme *inverzní zobrazení* $f^{-1} : B \to A$ předpisem
>
> $$
> f^{-1}(y) = x, \quad \text{kde } x \in A \text{ je to jediné s } f(x) = y.
> $$
>
> Pak platí $f^{-1}(f(x)) = x$ pro $x \in A$ a $f(f^{-1}(y)) = y$ pro $y \in B$, tedy **$f^{-1} \circ f = \mathrm{id}_A$ a $f \circ f^{-1} = \mathrm{id}_B$**.

^def-inverzni-zobrazeni

> [!lidsky] Lidsky
> Zobrazení „puštěné pozpátku“: z výstupu vrátí vstup. Aby to šlo, musí mít každý $y \in B$ vstup (na) a jen jeden (prosté), jinak by $f^{-1}(y)$ nebylo definované nebo by nebylo jednoznačné.

> [!example] Příklad
> Pro $f(x) = 2x + 1$ na $\mathbb{R}$ je $f^{-1}(y) = \tfrac{y - 1}{2}$; kontrola $f^{-1}(f(3)) = f^{-1}(7) = 3$. Pro $A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$ z §2 inverzní zobrazení neexistuje, $A$ není prosté ani na. Proto tam $A^{-1}\{(-3; 0)\}$ znamená vzor množiny, ne inverzi.

> [!navic] Střední škola versus tady (pozn. 7.5)
> Na střední se cílová množina neřešila (všechno šlo do $\mathbb{R}$) a definiční obor byl „všechno, co jde dosadit“. Pro inverzi proto stačila prostota: inverze pak měla definiční obor jen obor hodnot. Tady je cílová množina součástí zadání, takže pro inverzi $B \to A$ je potřeba prostota **i** surjektivita. Viz [[prostá funkce]] a [[inverzní funkce]] v MA1, kde se inverze bere na $f(D)$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč z distributivity pro lineární zobrazení plyne distributivita pro matice, $(A + B)C = AC + BC$?
> Matice jsou zobrazení a operace si odpovídají: **součet matic = matice součtu zobrazení**, **součin matic = matice složení**. Rovnost zobrazení $(A + B)C = AC + BC$ se proto přenese na jejich matice.

> [!karta|02]- Proč při důkazu $A(C + D) = AC + AD$ potřebuješ linearitu $A$, ale u $(A + B)C = AC + BC$ ne?
> $(A + B)(C\vec{x}) = AC\vec{x} + BC\vec{x}$ je jen **definice součtu zobrazení**. Naopak $A(C\vec{x} + D\vec{x}) = AC\vec{x} + AD\vec{x}$ znamená, že $A$ **zachovává součet**, a to je linearita. Pro $f(t) = t^2$ a $C = D = \mathrm{id}$ druhý zákon neplatí: $4t^2 \ne 2t^2$.

> [!karta|03]- Proč je pro pevnou matici $A \in \mathbb{F}^{l \times m}$ zobrazení $X \mapsto AX$ na $\mathbb{F}^{m \times n}$ lineární?
> Z **distributivity** $A(X + Y) = AX + AY$ a z **vytýkání skaláru** $A(\alpha X) = \alpha(AX)$. Totéž pro $X \mapsto XB$. Proto je součin matic **bilineární**.

> [!karta|04]- Proč je vzor nulového vektoru při lineárním zobrazení $A : V \to W$ vždy podprostor $V$?
> Je to množina řešení **homogenní soustavy** $A\vec{x} = \vec{0}$. Obsahuje $\vec{0}$ a pro $A\vec{x} = A\vec{y} = \vec{0}$ je $A(\alpha\vec{x} + \vec{y}) = \alpha\vec{0} + \vec{0} = \vec{0}$ (**linearita**).

> [!karta|05]- Proč je vzor bodu $\vec{b}$ při lineárním zobrazení jen posunutý vzor nuly?
> Je-li $A\vec{x}_p = \vec{b}$ a $A\vec{x}_0 = \vec{0}$, pak $A(\vec{x}_p + \vec{x}_0) = \vec{b}$, tedy $\vec{x}_p + \vec{x}_0$ je taky vzor. Vzor je **$\{\vec{x}_p\} + A^{-1}\{\vec{0}\}$**: jedno konkrétní řešení plus všechna řešení homogenní soustavy.

> [!karta|06]- Jak souvisí to, že soustava $A\vec{x} = \vec{b}$ má řešení, se sloupci matice $A$ a s $\operatorname{im} A$?
> Má řešení, právě když je $\vec{b}$ **lineární kombinací sloupců** $A$, tj. $\vec{b} \in \operatorname{span}\{\text{sloupce}\}$, a to je právě když **$\vec{b} \in \operatorname{im} A$**. Obraz matice je obal jejích sloupců.

> [!karta|07]- Čemu v tabulce „soustava – kombinace – vzor“ odpovídá, že soustava má pro každou pravou stranu nejvýš jedno řešení?
> Sloupce matice jsou **lineárně nezávislé** a zobrazení je **prosté**. Nejvýš jedno řešení = nejvýš jeden způsob, jak $\vec{b}$ složit ze sloupců.

> [!karta|08]- Proč se u zobrazení rozlišuje cílová množina a obor hodnot? Na čem závisí, jestli je $f$ na?
> Cílová množina je **součást zadání** $f : A \to B$, obor hodnot $f(A)$ je to, **co se opravdu zasáhne**. „Na“ znamená $f(A) = B$, takže závisí na zvolené cílové množině: $x^2 : \mathbb{R} \to [0; +\infty)$ je na, $x^2 : \mathbb{R} \to \mathbb{R}$ ne.

> [!karta|09]- Proč jsou podmínky „$x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$“ a „$f(x_1) = f(x_2) \Rightarrow x_1 = x_2$“ ekvivalentní?
> Druhá je [[obměněná implikace|obměněná implikace]] první: $p \Rightarrow q$ je totéž co $\neg q \Rightarrow \neg p$. V důkazech se víc hodí druhá, začneš rovností a odvodíš rovnost.

> [!karta|10]- Proč pro existenci inverzního zobrazení $f^{-1} : B \to A$ nestačí, aby bylo $f$ prosté?
> $f^{-1}$ musí být definované na **celém** $B$. Když $f$ není na, nějaké $y \in B$ nemá vzor a $f^{-1}(y)$ nemá co vrátit. Je potřeba **prosté i na**, tedy bijekce. (Na střední se inverze brala jen na oboru hodnot, proto stačila prostota.)

> [!karta|11]- Jaký je rozdíl mezi $f^{-1}(N)$ pro množinu $N$ a inverzním zobrazením $f^{-1}$?
> **Vzor množiny** $f^{-1}(N) = \{x \mid f(x) \in N\}$ existuje pro **každé** zobrazení a je to množina (i prázdná). **Inverzní zobrazení** existuje jen pro bijekci a vrací jeden prvek. Pro $x^2$ je $f^{-1}(\{4\}) = \{-2, 2\}$, ale inverze na $\mathbb{R}$ neexistuje.

> [!karta|12]- Co znamenají rovnosti $f^{-1} \circ f = \mathrm{id}_A$ a $f \circ f^{-1} = \mathrm{id}_B$ pro bijekci $f : A \to B$?
> **$f^{-1}(f(x)) = x$**: když zobrazíš a vrátíš se, jsi tam, kde jsi začal. **$f(f^{-1}(y)) = y$**: když najdeš vzor a zobrazíš ho, dostaneš zpět $y$. Pozor na indexy: první identita je na $A$, druhá na $B$.

### Příklady na procvičení

> [!priklad|13]- Ověř distributivitu $(A + B)C = AC + BC$ pro $A = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$.
> $A + B = \begin{pmatrix} 3 & -1 \\ 1 & 3 \end{pmatrix}$, $(A + B)C = \begin{pmatrix} 0 & 6 \\ 10 & 2 \end{pmatrix}$.
>
> $AC = \begin{pmatrix} 2 & 4 \\ 4 & 2 \end{pmatrix}$, $BC = \begin{pmatrix} -2 & 2 \\ 6 & 0 \end{pmatrix}$, $AC + BC = \begin{pmatrix} 0 & 6 \\ 10 & 2 \end{pmatrix}$.
>
> **Obě strany jsou $\begin{pmatrix} 0 & 6 \\ 10 & 2 \end{pmatrix}$.**

> [!priklad|14]- Rozhodni, zda je $g : \mathbb{Z} \to \mathbb{Z}$, $g(n) = 2n$ prosté, na, bijekce.
> Prosté: $2n_1 = 2n_2 \Rightarrow n_1 = n_2$. Na není: $3 \in \mathbb{Z}$ nemá vzor, $2n = 3$ nemá celočíselné řešení.
>
> **Prosté, ne na, tedy ne bijekce.** (Jako $g : \mathbb{R} \to \mathbb{R}$ by to bijekce byla.)

> [!priklad|15]- Pro $f(x) = x^2$ na $\mathbb{R}$ urči $f([-1; 2])$, $f^{-1}([1; 4])$ a $f^{-1}(\{-1\})$.
> Na $[-1; 2]$ nabývá $x^2$ všech hodnot od $0$ (v $x = 0$) do $4$ (v $x = 2$): **$f([-1; 2]) = [0; 4]$**. $1 \le x^2 \le 4 \Leftrightarrow 1 \le |x| \le 2$: **$f^{-1}([1; 4]) = [-2; -1] \cup [1; 2]$**. $x^2 = -1$ nemá řešení: **$f^{-1}(\{-1\}) = \emptyset$**.

> [!priklad|16]- Najdi inverzní zobrazení k $f : \mathbb{R} \to \mathbb{R}$, $f(x) = 3x - 6$, a ověř $f^{-1}(f(x)) = x$.
> $f$ je bijekce (lineární funkce se sklonem $3 \ne 0$). Z $y = 3x - 6$ je $x = \tfrac{y + 6}{3}$, tedy **$f^{-1}(y) = \tfrac{y}{3} + 2$**. Kontrola: $f^{-1}(3x - 6) = \tfrac{3x - 6 + 6}{3} = x$.

> [!priklad|17]- Pro $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ urči $\operatorname{im} A$, vzor bodu $(3; 6)$ a vzor bodu $(1; 0)$.
> Sloupce jsou $(1; 2)$ a $(2; 4) = 2(1; 2)$, tedy **$\operatorname{im} A = \operatorname{span}\{(1; 2)\}$**. $A\vec{x} = (3; 6)$: obě rovnice jsou $x + 2y = 3$, s $y = t$ je $x = 3 - 2t$, takže **$A^{-1}\{(3; 6)\} = \{(3; 0)\} + \operatorname{span}\{(-2; 1)\}$**. Bod $(1; 0)$ v $\operatorname{im} A$ není (není násobkem $(1; 2)$): **vzor je $\emptyset$**.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|18]- $A : \mathbb{R}^2 \to \mathbb{R}^2$, $A(x; y) = (x + 2y;\ 2x + 4y)$. Urči $\operatorname{Im} A$ a rozhodni, zda je $A$ prosté a zda je na.
> $A(x; y) = x(1; 2) + y(2; 4)$, takže $\operatorname{Im} A = \operatorname{span}\{(1; 2), (2; 4)\} = \operatorname{span}\{(1; 2)\}$, protože $(2; 4) = 2(1; 2)$.
>
> **Není prosté:** $A(2; -1) = (0; 0) = A(0; 0)$, ale $(2; -1) \ne (0; 0)$. **Není na:** $(1; 0) \notin \operatorname{Im} A$, protože není násobkem $(1; 2)$.
>
> **$\operatorname{Im} A = \operatorname{span}\{(1; 2)\}$, $A$ není prosté ani na.**

> [!priklad|19]- $A : \mathbb{R}^{\le 2}[x] \to \mathbb{R}^2$, $A(p) = (p(0);\ p(1))$. Je $A$ na? Je prosté? Urči $\operatorname{Im} A$.
> **Na:** pro libovolné $(a; b) \in \mathbb{R}^2$ stačí $p(x) = a + (b - a)x$, protože $p(0) = a$ a $p(1) = b$. Tedy $\operatorname{Im} A = \mathbb{R}^2$.
>
> **Není prosté:** $p(x) = x^2 - x$ má $p(0) = 0$ a $p(1) = 0$, takže $A(x^2 - x) = (0; 0) = A(0)$, ačkoli $x^2 - x \ne 0$.
>
> **$\operatorname{Im} A = \mathbb{R}^2$, $A$ je na, ale není prosté.**

> [!priklad|20]- $A : \mathbb{R}^2 \to \mathbb{R}^{\le 2}[x]$, $A(a; b) = a + bx^2$. Urči $\operatorname{Im} A$ a rozhodni, zda je $A$ prosté a zda je na.
> $\operatorname{Im} A = \{a + bx^2 \mid a, b \in \mathbb{R}\} = \operatorname{span}\{1, x^2\}$.
>
> **Prosté:** $a_1 + b_1x^2 = a_2 + b_2x^2$ znamená rovnost koeficientů polynomů, tedy $a_1 = a_2$ a $b_1 = b_2$. **Není na:** $x \notin \operatorname{Im} A$, polynom $a + bx^2$ má u $x$ vždy koeficient $0$.
>
> **$\operatorname{Im} A = \operatorname{span}\{1, x^2\}$, prosté, ne na.**

> [!priklad|21]- Pro $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ najdi vzor $A^{-1}\{(2; 3)\}$ ve tvaru $\{\vec{x}_p\} + \operatorname{span}\{\dots\}$.
> Soustava $x_1 + x_2 = 2$, $x_2 + x_3 = 3$. S parametrem $x_3 = t$: $x_2 = 3 - t$, $x_1 = 2 - x_2 = t - 1$. Tedy $\vec{x} = (-1; 3; 0) + t(1; -1; 1)$.
>
> **$A^{-1}\{(2; 3)\} = \{(-1; 3; 0)\} + \operatorname{span}\{(1; -1; 1)\}$.** Kontrola: $A(-1; 3; 0) = (2; 3)$ a $A(1; -1; 1) = (0; 0)$.

---
← [[LAG 09 – Algebra matic a transformace souřadnic|21. 10. 2026 Algebra matic a transformace souřadnic]]

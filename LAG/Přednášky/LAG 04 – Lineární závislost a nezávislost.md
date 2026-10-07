---
predmet: LAG
prednaska: 4
datum: 2026-10-02
zdroj: "V poznámkách věta 2.13 a kapitola 3 (3.1–3.6)"
tags: [prednaska, LAG]
---

# LAG 04 – Lineární závislost a nezávislost

*Přednáška 4 · pátek 2. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `důkaz věty 2.13` · `geometrie obalu` · `lineární závislost` · `lineární nezávislost` · `věta 3.3` · `věta 3.6`

Minule jsme zavedli [[lineární obal]] a bez důkazu řekli, že je to vždy [[lineární podprostor]]. Dnes ten důkaz a pak otázka, která z obalu přirozeně vyplyne: kdy je některý vektor v seznamu zbytečný, protože se dá namíchat z ostatních? Přesně to měří lineární závislost. Nezávislé vektory nemají nic navíc a obal z nich je „co největší“.

## §0 Přehled na jedné stránce

| pojem / věta                  | co říká                                                       | příklad v $\mathbb{R}^2$                    |
| ----------------------------- | ------------------------------------------------------------- | ------------------------------------------- |
| věta 2.13                     | $\operatorname{span} M \le L$ pro každé $M \subseteq L$       | $\operatorname{span}\{(1; 0)\}$ je osa $x$  |
| [[lineární závislost]] (LZ)   | $\vec{0}$ jde zapsat jako **netriviální** kombinaci           | $2 \cdot (1; 2) - 1 \cdot (2; 4) = \vec{0}$ |
| [[lineární nezávislost]] (LN) | $\vec{0}$ jde zapsat **jen** triviálně                        | $((1; 0), (0; 1))$                          |
| pozorování 3.2                | s $\vec{0}$ nebo s opakováním vždy LZ, $()$ je LN             | $((1; 1), (0; 0))$ je LZ                    |
| věta 3.3                      | ubráním z LN zůstane LN, přidáním k LZ zůstane LZ             |                                             |
| věta 3.6                      | LZ $\iff$ některý vektor je kombinací ostatních (předchozích) | $(2; 4) = 2 \cdot (1; 2)$                   |

## §1 Obal je podprostor

> [!veta] Věta 2.13
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $M \subseteq L$.== Potom **$\operatorname{span} M$ je lineární podprostor $L$.**
>
> > [!note]- Důkaz
> > Ověříme tři části definice podprostoru.
> >
> > **Neprázdnost:** $\vec{0} \in \operatorname{span} M$, protože je to prázdná lineární kombinace ($k = 0$). Funguje to i pro $M = \emptyset$.
> >
> > **Součet:** buďte $\vec{x}, \vec{y} \in \operatorname{span} M$. Pak existují $k \in \mathbb{N}_0$, $\vec{x}_1, \dots, \vec{x}_k \in M$, $\alpha_1, \dots, \alpha_k \in \mathbb{F}$ a $l \in \mathbb{N}_0$, $\vec{y}_1, \dots, \vec{y}_l \in M$, $\beta_1, \dots, \beta_l \in \mathbb{F}$ takové, že
> >
> > $$
> > \vec{x} = \alpha_1\vec{x}_1 + \dots + \alpha_k\vec{x}_k, \qquad \vec{y} = \beta_1\vec{y}_1 + \dots + \beta_l\vec{y}_l.
> > $$
> >
> > Potom $\vec{x} + \vec{y} = \alpha_1\vec{x}_1 + \dots + \alpha_k\vec{x}_k + \beta_1\vec{y}_1 + \dots + \beta_l\vec{y}_l$ je lineární kombinace $k + l$ prvků z $M$, tedy leží ve $\operatorname{span} M$.
> >
> > **Násobek:** pro libovolné $\gamma \in \mathbb{F}$ je
> >
> > $$
> > \gamma\vec{x} = \gamma(\alpha_1\vec{x}_1 + \dots + \alpha_k\vec{x}_k) = (\gamma\alpha_1)\vec{x}_1 + \dots + (\gamma\alpha_k)\vec{x}_k \in \operatorname{span} M.
> > $$

^veta-213-dukaz

> [!lidsky] Lidsky
> Smícháš-li dva recepty z ingrediencí $M$, dostaneš zase recept z ingrediencí $M$ (jen delší). Zdvojnásobíš-li recept, je to pořád recept z $M$. A „nic nevařit“ je taky recept, ten dá nulu. Víc podprostor potřebovat nemusí.

> [!pozor] Dva vektory z obalu mají vlastní kombinace
> Častá chyba je psát $\vec{x}$ i $\vec{y}$ pomocí stejných vektorů $\vec{x}_1, \dots, \vec{x}_k$ se stejným $k$. Obecně je každý z nich kombinací **jiných** prvků $M$, proto různá písmena ($\vec{y}_j$, $\beta_j$, $l$). Součet pak prostě spojí oba seznamy.

Příklad použití: polynomy stupně nejvýše $n$ jsou přesně všechny kombinace mocnin $x$, takže

$$
\mathbb{R}^{\le n}[x] = \{\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n \mid \alpha_0, \dots, \alpha_n \in \mathbb{R}\} = \operatorname{span}\{1, x, x^2, \dots, x^n\} \le \mathbb{R}[x].
$$

Podprostor $\mathbb{R}[x]$ to je hned z věty 2.13, bez ověřování uzavřenosti jako v [[LAG 03 – Lineární podprostor a lineární obal#§1 Polynomy stupně nejvýše n|přednášce 3]].

## §2 Jak obaly vypadají

V $\mathbb{R}^3$:

- $\operatorname{span}\{\vec{x}\}$ pro $\vec{x} \neq \vec{0}$ je **přímka** přes počátek.
- $\operatorname{span}\{\vec{x}, \vec{y}\}$ je **rovina** přes počátek, pokud $\vec{y}$ není násobkem $\vec{x}$ (a $\vec{x} \neq \vec{0}$). Jinak vyjde zase jen přímka (nebo $\{\vec{0}\}$).
- $\operatorname{span}\{\vec{x}, \vec{y}, \vec{z}\}$ je **celé** $\mathbb{R}^3$, pokud žádný z vektorů není lineární kombinací ostatních. Jinak rovina, přímka, nebo $\{\vec{0}\}$.

> [!obrazek] Obal jednoho, dvou a tří vektorů v $\mathbb{R}^3$
> ![[lag04-obaly.png]]
> *Modrá čárkovaná: přímka span{x}. Zelená rovina: span{x, y}, když y (oranžová) neleží na přímce x. Vpravo: z (červená) vyčnívá z roviny x, y, a obal je proto celý prostor (zelená krychle naznačuje, že vyplní všechno).*

Otázka „je některý vektor kombinací ostatních?“ je přesně to, čemu se říká lineární závislost.

## §3 Lineární závislost a nezávislost

> [!definice] Definice ♥ · pozn. 3.1
> Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$. Posloupnost vektorů $(\vec{x}_1, \dots, \vec{x}_n)$ se nazývá *lineárně závislá* (LZ), jestliže lze nulový vektor $\vec{0}$ zapsat jako netriviální lineární kombinaci vektorů z této posloupnosti:
>
> $$
> (\vec{x}_1, \dots, \vec{x}_n) \text{ je LZ} \iff (\exists \alpha_1, \dots, \alpha_n \in \mathbb{F})\big((\exists i \in \{1, \dots, n\})(\alpha_i \neq 0) \wedge \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \vec{0}\big).
> $$
>
> V opačném případě se posloupnost nazývá *lineárně nezávislá* (LN), tj. jediná lineární kombinace, která dává nulový vektor, je ta triviální:
>
> $$
> (\vec{x}_1, \dots, \vec{x}_n) \text{ je LN} \iff (\forall \alpha_1, \dots, \alpha_n \in \mathbb{F})\big(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \vec{0} \Rightarrow \alpha_1 = \dots = \alpha_n = 0\big).
> $$

^def-lz

> [!lidsky] Lidsky
> [[triviální lineární kombinace|Triviálně]] dá nulu každá sada vektorů: od všeho nula dávek. Závislá sada umí nulu „namíchat“ i jinak, s aspoň jednou nenulovou dávkou. To znamená, že se vektory navzájem ruší, takže aspoň jeden z nich jde poskládat z ostatních a je v sadě navíc.
>
> Příklad: $2 \cdot (1; 2) - 1 \cdot (2; 4) = (0; 0)$, takže $((1; 2), (2; 4))$ je LZ. Druhý vektor je jen dvojnásobek prvního.

> [!pozor] Netriviální = aspoň jeden koeficient nenulový
> Častá chyba je chtít, aby byly nenulové **všechny** koeficienty. Stačí jeden: $((1; 0), (0; 0))$ je LZ díky $0 \cdot (1; 0) + 1 \cdot (0; 0) = \vec{0}$. A naopak u LN nestačí najít jednu kombinaci s nenulovými koeficienty, která nulu nedá; musí se ukázat, že **každá** kombinace dávající nulu je triviální.

> [!navic] Proč posloupnost, a ne množina
> V množině $\{\vec{x}_1, \dots, \vec{x}_n\}$ nezáleží na pořadí a opakování splyne: $\{\vec{x}, \vec{x}\} = \{\vec{x}\}$. V uspořádané $n$-tici $(\vec{x}_1, \dots, \vec{x}_n)$ se opakování počítá, a to je pro závislost podstatné: $(\vec{x}, \vec{x})$ je LZ, i když $(\vec{x})$ pro $\vec{x} \neq \vec{0}$ je LN.

## §4 Pozorování 3.2

1. LZ a LN **nezávisí na pořadí** vektorů v posloupnosti. Sčítání je komutativní, koeficienty se přehází spolu s vektory.
2. Vyskytuje-li se v posloupnosti některý vektor **vícekrát**, je LZ: $1 \cdot \vec{x} + (-1) \cdot \vec{x} = \vec{0}$ (ostatním koeficient $0$).
3. **Prázdná posloupnost** $()$ je LN. Jediná kombinace nula vektorů je prázdná, a ta je triviální.
4. Obsahuje-li posloupnost **nulový vektor**, je LZ: $1 \cdot \vec{0} = \vec{0}$ je netriviální kombinace.
5. $(\vec{x})$ je LN $\iff \vec{x} \neq \vec{0}$. Z $\alpha\vec{x} = \vec{0}$ a $\alpha \neq 0$ plyne $\vec{x} = \alpha^{-1}\vec{0} = \vec{0}$.
6. $(\vec{x}, \vec{y})$ je LZ $\iff$ jeden je násobkem druhého ($\vec{y} = \alpha\vec{x}$ nebo $\vec{x} = \alpha\vec{y}$).

^poz-32

> [!question]- Proč v bodě 6 nestačí „$\vec{y} = \alpha\vec{x}$“?
> Pro $\vec{x} = \vec{0}$ a $\vec{y} \neq \vec{0}$ je $(\vec{0}, \vec{y})$ LZ (obsahuje nulu), ale $\vec{y}$ není násobkem nulového vektoru. Funguje opačně: $\vec{x} = 0 \cdot \vec{y}$. Proto „jeden je násobkem druhého“.

## §5 Jak závislost rozhodnout výpočtem

> [!example] Úloha 3.5
> Jsou vektory $\vec{x}_1 = (1; 1; 0)^T$, $\vec{x}_2 = (0; 1; 1)^T$, $\vec{x}_3 = (1; 2; 1)^T$ v $\mathbb{R}^3$ lineárně nezávislé?
>
> Hledáme všechna $\alpha, \beta, \gamma \in \mathbb{R}$ s $\alpha\vec{x}_1 + \beta\vec{x}_2 + \gamma\vec{x}_3 = \vec{0}$:
>
> $$
> \alpha\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + \beta\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \gamma\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha + \gamma \\ \alpha + \beta + 2\gamma \\ \beta + \gamma \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
> $$
>
> Z první rovnice $\alpha = -\gamma$, ze třetí $\beta = -\gamma$; druhá pak dá $-\gamma - \gamma + 2\gamma = 0$, platí vždy. Soustava je tedy ekvivalentní s $\alpha + \gamma = 0$, $\beta + \gamma = 0$ a $\gamma$ je libovolné.
>
> Volbou $\gamma = 1$ vyjde $\alpha = \beta = -1$:
>
> $$
> -\vec{x}_1 - \vec{x}_2 + \vec{x}_3 = \vec{0}, \qquad \text{tj. } \vec{x}_3 = \vec{x}_1 + \vec{x}_2.
> $$
>
> Našli jsme netriviální kombinaci, posloupnost je **lineárně závislá**.

> [!obrazek] Tři závislé vektory leží v jedné rovině
> ![[lag04-uloha35.png]]
> *Modrá x₁ a oranžová x₂ určují zelenou rovinu span{x₁, x₂}. Červená x₃ = x₁ + x₂ je úhlopříčka rovnoběžníku (tečkovaně), leží ve stejné rovině a nic nového nepřidá.*

> [!pozor] Po výpočtu dosaď zpět
> Častá chyba je splést znaménko při volbě volné proměnné. Kontrola je okamžitá: $-(1; 1; 0) - (0; 1; 1) + (1; 2; 1) = (0; 0; 0)$. Volba $\alpha = \beta = \gamma = -1$ by dala $-(2; 4; 2) \neq \vec{0}$.

> [!lidsky] Lidsky
> Rozhodnout LZ/LN znamená vyřešit homogenní soustavu, kde neznámé jsou koeficienty. Má-li jen nulové řešení, je posloupnost LN. Má-li i jiné (nějaká proměnná vyjde volná), je LZ, a každé nenulové řešení rovnou ukáže, který vektor se dá vyjádřit z ostatních.

## §6 Ubírání a přidávání vektorů

> [!veta] Věta 3.3
> ==Buď $L$ lineární prostor nad $\mathbb{F}$.==
>
> 1. **Odebráním libovolného počtu vektorů z LN posloupnosti vznikne LN posloupnost.**
> 2. **Přidáním libovolného počtu vektorů k LZ posloupnosti vznikne LZ posloupnost.**
>
> > [!note]- Důkaz (přímo, cvičení 3.4)
> > **1.** Buď $(\vec{x}_1, \dots, \vec{x}_n)$ LN. Na pořadí nezáleží (pozorování 3.2), takže stačí ukázat, že pro každé $k \le n$ je LN posloupnost $(\vec{x}_1, \dots, \vec{x}_k)$.
> >
> > Předpokládáme: $(\forall \alpha_1, \dots, \alpha_n \in \mathbb{F})(\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \vec{0} \Rightarrow \alpha_1 = \dots = \alpha_n = 0)$.
> >
> > Chceme: $(\forall \beta_1, \dots, \beta_k \in \mathbb{F})(\beta_1\vec{x}_1 + \dots + \beta_k\vec{x}_k = \vec{0} \Rightarrow \beta_1 = \dots = \beta_k = 0)$.
> >
> > Nechť tedy $\beta_1\vec{x}_1 + \dots + \beta_k\vec{x}_k = \vec{0}$. Položíme $\alpha_1 = \beta_1, \dots, \alpha_k = \beta_k$ a $\alpha_{k+1} = \dots = \alpha_n = 0$. Pak $\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \vec{0}$, takže z předpokladu jsou všechna $\alpha_i = 0$, speciálně $\beta_1 = \dots = \beta_k = 0$.
> >
> > **2.** Je to obměna bodu 1. Kdyby přidáním vznikla LN posloupnost, pak by podle bodu 1 bylo LN i to, co z ní odebráním přidaných vektorů zbude, tedy původní posloupnost. To je spor s tím, že byla LZ.

^veta-33

> [!lidsky] Lidsky
> Netriviální kombinace dávající nulu se přidáním vektorů neztratí: nové vektory dostanou koeficient $0$. A když nezávislá sada nemá žádné „zbytečné“ vektory, tak je nemá ani žádný její kousek.

> [!navic] Obráceně to neplatí
> Přidáním vektoru k LN posloupnosti může vzniknout LZ (k $(\vec{x}_1, \vec{x}_2)$ z úlohy 3.5 přidáme $\vec{x}_3$) a odebráním z LZ může vzniknout LN (z $(\vec{x}_1, \vec{x}_2, \vec{x}_3)$ odebereme $\vec{x}_3$). Kdy přidání LN zachová, říká věta 3.7: když nový vektor neleží v obalu těch předchozích.

## §7 Alternativní definice závislosti

> [!veta] Věta 3.6 (alternativní definice LZ)
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$.== Potom jsou **ekvivalentní**:
>
> 1. $(\vec{x}_1, \dots, \vec{x}_n)$ je LZ,
> 2. existuje $i$ takové, že $\vec{x}_i$ je lineární kombinací ostatních: $\vec{x}_i \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}, \vec{x}_{i+1}, \dots, \vec{x}_n\}$,
> 3. existuje $i$ takové, že $\vec{x}_i$ je lineární kombinací předchozích: $\vec{x}_i \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}\}$.
>
> > [!note]- Důkaz (3) ⇒ (2) ⇒ (1) ⇒ (3)
> > **(3) ⇒ (2):** kombinace předchozích je i kombinací ostatních, zbylé vektory dostanou koeficient $0$.
> >
> > **(2) ⇒ (1):** je-li $\vec{x}_i = \sum_{j \neq i} \alpha_j\vec{x}_j$, pak
> >
> > $$
> > \alpha_1\vec{x}_1 + \dots + \alpha_{i-1}\vec{x}_{i-1} + (-1)\vec{x}_i + \alpha_{i+1}\vec{x}_{i+1} + \dots + \alpha_n\vec{x}_n = \vec{0}
> > $$
> >
> > a koeficient u $\vec{x}_i$ je $-1 \neq 0$, takže kombinace je netriviální.
> >
> > **(1) ⇒ (3):** buď $\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \vec{0}$ netriviální. Vezmeme největší $i$, pro které $\alpha_i \neq 0$; pak $\alpha_{i+1} = \dots = \alpha_n = 0$ a $\alpha_1\vec{x}_1 + \dots + \alpha_i\vec{x}_i = \vec{0}$. Protože $\alpha_i \neq 0$, můžeme jím dělit:
> >
> > $$
> > \vec{x}_i = -\frac{\alpha_1}{\alpha_i}\vec{x}_1 - \dots - \frac{\alpha_{i-1}}{\alpha_i}\vec{x}_{i-1} \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}\}.
> > $$

^veta-36

> [!lidsky] Lidsky
> Závislá sada = sada, ve které je aspoň jeden vektor zbytečný, protože ho poskládáš z ostatních. Bod 3 jde ještě dál: projdeš-li vektory zleva doprava, narazíš na první, který už jde poskládat jen z těch před ním. V úloze 3.5 je to $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$.

> [!pozor] „Kombinace předchozích“ pro první vektor
> Pro $i = 1$ nejsou žádné předchozí vektory a $\operatorname{span}\emptyset = \{\vec{0}\}$. Bod 3 pro $i = 1$ tedy znamená $\vec{x}_1 = \vec{0}$, což souhlasí s pozorováním 3.2: posloupnost s nulovým vektorem je LZ. A pozor, bod 2 neříká, že **každý** vektor je kombinací ostatních: v $((1; 0), (2; 0), (0; 1))$ je $(0; 1)$ z ostatních nesložitelný, a posloupnost je přesto LZ.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jak dokážeš větu 2.13, že $\operatorname{span} M \le L$?
> **Neprázdnost:** $\vec{0}$ je prázdná kombinace. **Součet:** $\sum \alpha_i\vec{x}_i + \sum \beta_j\vec{y}_j$ je kombinace prvků $M$ (spojené seznamy). **Násobek:** $\gamma\sum \alpha_i\vec{x}_i = \sum (\gamma\alpha_i)\vec{x}_i$.

> [!karta|02]- Proč platí $\mathbb{R}^{\le n}[x] = \operatorname{span}\{1, x, \dots, x^n\}$ a co z toho plyne?
> Polynom stupně $\le n$ je přesně kombinace $\alpha_0 \cdot 1 + \alpha_1 x + \dots + \alpha_n x^n$. Podle věty 2.13 je to tedy **podprostor** $\mathbb{R}[x]$ bez dalšího ověřování.

> [!karta|03]- Jak geometricky vypadá $\operatorname{span}\{\vec{x}, \vec{y}, \vec{z}\}$ v $\mathbb{R}^3$?
> **Celé $\mathbb{R}^3$**, když žádný z vektorů není kombinací ostatních. Jinak rovina, přímka nebo $\{\vec{0}\}$ přes počátek.

> [!karta|04]- Co znamená, že je lineární kombinace netriviální?
> **Aspoň jeden** koeficient je nenulový (ne nutně všechny).

> [!karta|05]- Proč lineární závislost nezávisí na pořadí vektorů?
> Sčítání vektorů je **komutativní**: když vektory přeházíš, přeházíš s nimi i koeficienty a kombinace dává totéž.

> [!karta|06]- Proč je posloupnost, ve které se vektor opakuje, lineárně závislá?
> $1 \cdot \vec{x} + (-1) \cdot \vec{x} = \vec{0}$ (ostatní koeficienty $0$) je **netriviální** kombinace dávající nulu.

> [!karta|07]- Proč je posloupnost obsahující $\vec{0}$ lineárně závislá?
> $1 \cdot \vec{0} = \vec{0}$ (ostatní koeficienty $0$) je netriviální kombinace s výsledkem $\vec{0}$.

> [!karta|08]- Je prázdná posloupnost $()$ LZ, nebo LN? Proč?
> **LN.** Jediná kombinace nula vektorů je prázdná, ta je triviální; netriviální kombinace neexistuje.

> [!karta|09]- Kdy je jednoprvková posloupnost $(\vec{x})$ LN?
> Právě když $\vec{x} \neq \vec{0}$. Z $\alpha\vec{x} = \vec{0}$ s $\alpha \neq 0$ plyne $\vec{x} = \alpha^{-1}\vec{0} = \vec{0}$.

> [!karta|10]- Kdy je dvojice $(\vec{x}, \vec{y})$ lineárně závislá?
> Právě když je **jeden násobkem druhého** ($\vec{y} = \alpha\vec{x}$ nebo $\vec{x} = \alpha\vec{y}$). Pro $\vec{x} = \vec{0}$ funguje jen druhá varianta.

> [!karta|11]- Proč se lineární závislost definuje pro posloupnost, a ne pro množinu vektorů?
> V množině **opakování splyne** ($\{\vec{x}, \vec{x}\} = \{\vec{x}\}$), ale $(\vec{x}, \vec{x})$ je LZ, zatímco $(\vec{x})$ pro $\vec{x} \neq \vec{0}$ je LN.

> [!karta|12]- Co říká věta 3.3?
> 1. **Odebráním** vektorů z LN posloupnosti vznikne LN posloupnost.
> 2. **Přidáním** vektorů k LZ posloupnosti vznikne LZ posloupnost.

> [!karta|13]- Jak dokážeš, že odebráním vektorů z LN posloupnosti zůstane LN (věta 3.3.1)?
> Je-li $\beta_1\vec{x}_1 + \dots + \beta_k\vec{x}_k = \vec{0}$, doplň odebrané vektory s koeficientem **0**. Vznikne kombinace celé LN posloupnosti dávající $\vec{0}$, takže všechna $\beta_i = 0$.

> [!karta|14]- Proč bod 2 věty 3.3 (přidání k LZ) plyne z bodu 1?
> Je to **obměna**: kdyby přidáním vznikla LN posloupnost, byla by podle bodu 1 LN i původní (vznikne odebráním přidaných), spor.

> [!karta|15]- Jaké tři ekvivalentní podmínky dává věta 3.6 (alternativní definice LZ)?
> 1. posloupnost je **LZ**,
> 2. některý $\vec{x}_i$ je kombinací **ostatních**,
> 3. některý $\vec{x}_i$ je kombinací **předchozích** $\vec{x}_1, \dots, \vec{x}_{i-1}$.

> [!karta|16]- Proč z „$\vec{x}_i$ je kombinací ostatních“ plyne lineární závislost (věta 3.6, (2) ⇒ (1))?
> Převedeš $\vec{x}_i$ na druhou stranu: $\sum_{j \neq i} \alpha_j\vec{x}_j + (-1)\vec{x}_i = \vec{0}$. Koeficient **$-1 \neq 0$**, kombinace je netriviální.

> [!karta|17]- Jak z netriviální kombinace $\sum \alpha_j\vec{x}_j = \vec{0}$ najdeš vektor, který je kombinací předchozích (věta 3.6, (1) ⇒ (3))?
> Vezmi **největší $i$ s $\alpha_i \neq 0$** a vyděl: $\vec{x}_i = -\frac{\alpha_1}{\alpha_i}\vec{x}_1 - \dots - \frac{\alpha_{i-1}}{\alpha_i}\vec{x}_{i-1}$.

> [!karta|18]- Co znamená podmínka „$\vec{x}_1$ je kombinací předchozích“ z věty 3.6?
> Předchozí nejsou, $\operatorname{span}\emptyset = \{\vec{0}\}$, takže to znamená **$\vec{x}_1 = \vec{0}$**.

### Příklady na procvičení

> [!priklad|19]- Jsou $\vec{x}_1 = (1; 1; 0)$, $\vec{x}_2 = (0; 1; 1)$, $\vec{x}_3 = (1; 2; 1)$ lineárně nezávislé (úloha 3.5)?
> Soustava $\alpha + \gamma = 0$, $\alpha + \beta + 2\gamma = 0$, $\beta + \gamma = 0$ má volné $\gamma$. Pro $\gamma = 1$: $-\vec{x}_1 - \vec{x}_2 + \vec{x}_3 = \vec{0}$, tedy **LZ**, $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$.

> [!priklad|20]- Je $((1; 2), (2; 4))$ v $\mathbb{R}^2$ LZ, nebo LN?
> **LZ**: $2 \cdot (1; 2) - 1 \cdot (2; 4) = (0; 0)$. Druhý vektor je dvojnásobek prvního.

> [!priklad|21]- Je $((1; 0), (0; 1))$ v $\mathbb{R}^2$ LZ, nebo LN?
> $\alpha(1; 0) + \beta(0; 1) = (\alpha; \beta) = (0; 0)$ dává $\alpha = \beta = 0$, tedy **LN**.

> [!priklad|22]- Je $((1; 2), (3; 4), (5; 6))$ v $\mathbb{R}^2$ LZ? Najdi kombinaci.
> **LZ**: z $\alpha + 3\beta + 5\gamma = 0$, $2\alpha + 4\beta + 6\gamma = 0$ vyjde $\beta = -2\gamma$, $\alpha = \gamma$; pro $\gamma = 1$: $(1; 2) - 2(3; 4) + (5; 6) = (0; 0)$.

> [!priklad|23]- Je $(1, x, x^2)$ v $\mathbb{R}[x]$ lineárně nezávislá?
> **Ano.** $\alpha_0 + \alpha_1 x + \alpha_2 x^2$ je nulový polynom, jen když jsou všechny koeficienty nulové, tedy $\alpha_0 = \alpha_1 = \alpha_2 = 0$.

> [!priklad|24]- Je $((1; 1), (0; 0))$ LZ? Uveď netriviální kombinaci.
> **LZ** (obsahuje $\vec{0}$): $0 \cdot (1; 1) + 1 \cdot (0; 0) = (0; 0)$.

---
← [[LAG 03 – Lineární podprostor a lineární obal|30. 9. 2026 Lineární podprostor a lineární obal]] · [[LAG 05 – Báze a dimenze|7. 10. 2026 Báze a dimenze]] →

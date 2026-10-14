---
predmet: LAG
prednaska: 3
datum: 2026-09-30
zdroj: "V poznámkách kapitola 2 (2.1–2.14)"
tags: [prednaska, LAG]
---

# LAG 03 – Lineární podprostor a lineární obal

*Přednáška 3 · středa 30. 9. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `𝔽≤ⁿ[x]` · `lineární podprostor` · `homogenní soustava` · `lineární kombinace` · `lineární obal`

Minule bylo vidět, že [[lineární prostor|lineárních prostorů]] je spousta. Dnes jde o dvě otázky. Jak poznat, že kousek lineárního prostoru je sám lineární prostor, aniž bys znovu ověřoval všech 8 [[axiomy lineárního prostoru|axiomů]]? Stačí dvě podmínky. A jak z pár vektorů takový kousek vyrobit? Vezmeš všechny jejich [[lineární kombinace]].

## §0 Přehled na jedné stránce

| pojem | co to je | příklad v $\mathbb{R}^2$ |
|---|---|---|
| [[lineární podprostor]] $V \le L$ | neprázdná podmnožina uzavřená na $+$ a na násobení skalárem | přímka přes počátek |
| [[lineární kombinace]] | $\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$ | $2\vec{x} - \vec{y}$ |
| [[triviální lineární kombinace]] | všechny koeficienty jsou $0$ | $0\vec{x} + 0\vec{y} = \vec{0}$ |
| [[lineární obal]] $\operatorname{span} M$ | všechny lineární kombinace prvků $M$ | $\operatorname{span}\{\vec{x}\}$ je přímka |

## §1 Polynomy stupně nejvýše n

> [!veta] Tvrzení
> Množina
>
> $$
> \mathbb{F}^{\le n}[x] = \{\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n \mid \alpha_0, \dots, \alpha_n \in \mathbb{F}\} = \{p(x) \in \mathbb{F}[x] \mid \deg p(x) \le n\}
> $$
>
> je lineární prostor nad $\mathbb{F}$ vzhledem ke stejným operacím jako v $\mathbb{F}[x]$.

^veta-poly-n

Ověřit se dá všech 8 axiomů, hlavní je ale, že sčítání z množiny nevyvede ven, je [[dobře definovaná operace|dobře definované]]:

$$
(\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n) + (\beta_0 + \beta_1 x + \dots + \beta_n x^n) = (\alpha_0 + \beta_0) + (\alpha_1 + \beta_1)x + \dots + (\alpha_n + \beta_n)x^n \in \mathbb{F}^{\le n}[x]
$$

Stejně $\gamma \cdot (\alpha_0 + \dots + \alpha_n x^n) = \gamma\alpha_0 + \dots + \gamma\alpha_n x^n$ má stupeň nejvýše $n$.

> [!navic] Tohle ověřování si za chvíli ušetříš
> $\mathbb{F}^{\le n}[x]$ je podmnožina $\mathbb{F}[x]$ a axiomy 1, 2, 5–8 v $\mathbb{F}[x]$ už platí. Věta 2.2 níže říká, že v takové situaci stačí ověřit dvě podmínky uzavřenosti, tedy přesně výpočet výše. Proto $\mathbb{F}^{\le n}[x] \le \mathbb{F}[x]$.

## §2 Lineární podprostor

> [!definice] Definice ♥ · pozn. 2.1
> Buď $L$ lineární prostor nad tělesem $\mathbb{F}$. Řekneme, že ==neprázdná== podmnožina $V \subseteq L$ je *lineární podprostor* $L$, a píšeme $V \le L$, jestliže je
>
> 1. **uzavřená na sčítání:** $(\forall \vec{x}, \vec{y} \in V)(\vec{x} + \vec{y} \in V)$,
> 2. **uzavřená na násobení skalárem:** $(\forall \alpha \in \mathbb{F})(\forall \vec{x} \in V)(\alpha\vec{x} \in V)$.

^def-podprostor

> [!lidsky] Lidsky
> Podprostor je místnost uvnitř prostoru, ze které se sčítáním a natahováním nedá utéct. Sečteš dva vektory z místnosti a jsi pořád v ní; vynásobíš číslem a jsi pořád v ní. V $\mathbb{R}^2$ existují jen tři typy: samotný počátek $\{\vec{0}\}$, přímky přes počátek a celá rovina.
>
> Proč to chceme: podprostor je sám lineární prostor (věta 2.2), jen menší. Množina řešení homogenní soustavy nebo spojité funkce jsou podprostory, takže pro ně automaticky platí všechno, co se dokáže o lineárních prostorech.

> [!obrazek] Co je a co není podprostor $\mathbb{R}^2$
> ![[lag03-podprostory.png]]
> *Zelená: přímka přes počátek je podprostor, s x obsahuje všechny násobky. Červená uprostřed: přímka y = x/2 + 1 neobsahuje nulový vektor (prázdné kolečko) a součet a + b (oranžová) z ní vypadne. Červená vpravo: první kvadrant je uzavřený na sčítání, ale (−1)·x (oranžová) už v něm není.*

## §3 Podprostor je sám lineární prostor

> [!veta] Věta 2.2
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $V \le L$ jeho lineární podprostor.== Potom **$V$ je lineární prostor nad $\mathbb{F}$ vzhledem k operacím z $L$ zúženým na $V$.** Speciálně $\vec{0} \in V$ a pro každé $\vec{x} \in V$ je $-\vec{x} \in V$.
>
> > [!note]- Důkaz
> > **Operace.** V $L$ máme $+ : L \times L \to L$ a $\cdot : \mathbb{F} \times L \to L$. Díky uzavřenosti je můžeme zúžit na $V$: $+ : V \times V \to V$ a $\cdot : \mathbb{F} \times V \to V$ (výsledek z $V$ nevypadne).
> >
> > **Axiomy 1, 2, 5–8** jsou tvaru „pro všechna …“. Platí pro všechny vektory z $L$, tedy i pro ty z $V$.
> >
> > **Axiomy 3 a 4** říkají, že něco *existuje*, a to se samo zdědit nemusí: nula z $L$ by mohla ležet mimo $V$. Protože $V \neq \emptyset$, existuje nějaké $\vec{x} \in V$, a z uzavřenosti na násobení (věta 1.8, body 3 a 4):
> >
> > $$
> > \vec{0} = 0 \cdot \vec{x} \in V, \qquad -\vec{x} = (-1) \cdot \vec{x} \in V.
> > $$

^veta-22

> [!lidsky] Lidsky
> Místo osmi axiomů ověřuješ dvě podmínky. Pravidla typu $\vec{x} + \vec{y} = \vec{y} + \vec{x}$ platí v celém $L$, takže platí i v každém jeho kousku. Jediné, co by kousku mohlo chybět, je nula a opačné vektory, a ty si podprostor vyrobí sám: vynásobí libovolný svůj vektor nulou a mínus jedničkou.

> [!navic] Rychlý test: obsahuje V nulu?
> Z věty plyne nutná podmínka: když $\vec{0} \notin V$, podprostor to není a dál nic ověřovat nemusíš (přímka $y = x/2 + 1$ na obrázku). Obráceně to neplatí: první kvadrant nulu obsahuje, a podprostor přesto není.

## §4 Příklady podprostorů

- $\{\vec{0}\} \le L$ pro libovolné $L$: nejmenší podprostor, tzv. *triviální* `pozn. 2.3`. ^triv-podprostor
- $L \le L$ pro libovolné $L$: největší podprostor.
- $\emptyset \not\le L$: podle definice musí být podprostor neprázdný.
- $\mathbb{R}^{\le n}[x] \le \mathbb{R}[x]$: polynomy stupně nejvýše $n$ (§1).
- $C(\mathbb{R}) \le \mathbb{R}^{\mathbb{R}}$: spojité funkce mezi všemi funkcemi $\mathbb{R} \to \mathbb{R}$. Součet spojitých funkcí i násobek spojité funkce je spojitý, nulová funkce je spojitá.

> [!question]- Proč definice chce neprázdnou množinu? Podmínky uzavřenosti ∅ přece splňuje.
> Splňuje, a to prázdně: v $\emptyset$ nejsou žádné vektory, které by šly sečíst. Jenže lineární prostor musí mít nulový vektor (axiom 3) a $\emptyset$ žádný nemá. Podmínka $V \neq \emptyset$ je přesně to, co v důkazu věty 2.2 zaručí $\vec{0} \in V$.

### Řešení homogenní soustavy

Soustavě, která má všechny pravé strany nulové, se říká *homogenní*. ^def-homogenni

> [!veta] Tvrzení · obecně pozn. 2.6
> Pro libovolná $\alpha, \beta, \gamma, \delta \in \mathbb{R}$ je množina řešení
>
> $$
> S = \left\{ \begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2 \;\middle|\; \begin{aligned} \alpha x + \beta y &= 0 \\ \gamma x + \delta y &= 0 \end{aligned} \right\}
> $$
>
> lineární podprostor $\mathbb{R}^2$.
>
> > [!note]- Důkaz
> > **Neprázdnost:** $(0; 0) \in S$.
> >
> > **Součet:** buďte $(x_1; y_1), (x_2; y_2) \in S$. Chceme $(x_1 + x_2; y_1 + y_2) \in S$:
> >
> > $$
> > \alpha(x_1 + x_2) + \beta(y_1 + y_2) = \underbrace{(\alpha x_1 + \beta y_1)}_{0} + \underbrace{(\alpha x_2 + \beta y_2)}_{0} = 0
> > $$
> >
> > a stejně pro druhou rovnici s $\gamma, \delta$.
> >
> > **Násobek:** pro $r \in \mathbb{R}$ je $\alpha(r x_1) + \beta(r y_1) = r(\alpha x_1 + \beta y_1) = r \cdot 0 = 0$, stejně druhá rovnice.

> [!pozor] Důkaz podprostoru má tři části
> Častá chyba je ověřit jen součet. Úplný důkaz, že $S \le L$, potřebuje **neprázdnost** (nejjednodušeji $\vec{0} \in S$), **uzavřenost na součet** a **uzavřenost na násobek**. U zkoušky (část B2) se bez kterékoliv z nich důkaz nepočítá jako úplný.

> [!obrazek] Jak může vypadat řešení homogenní soustavy v $\mathbb{R}^2$
> ![[lag03-homogenni.png]]
> *Vlevo: dvě různoběžné přímky přes počátek (modrá, oranžová), řešením je jen bod (0; 0). Uprostřed: obě rovnice popisují tutéž přímku, řešením je celá přímka. Vpravo: rovnice 0 = 0 splní každý bod, řešením je celá rovina. Pokaždé podprostor, nikdy třeba posunutá přímka.*

> [!lidsky] Lidsky
> Homogenní znamená „napravo samé nuly“. Dvě řešení sečtená dají zase řešení, protože $0 + 0 = 0$, a řešení vynásobené číslem taky, protože $r \cdot 0 = 0$. Kdyby napravo bylo $5$, součet dvou řešení by dal $10$, ne $5$. Nehomogenní soustava proto podprostor nikdy netvoří: neobsahuje ani $(0; 0)$.

> [!example] Matice se stopou 0 · pozn. 2.7
> *Stopa* čtvercové matice je součet prvků na diagonále: $\operatorname{tr}\mathbf{A} = a_{11} + a_{22} + \dots + a_{nn}$. Matice se stopou $0$ tvoří podprostor $\mathbb{F}^{n \times n}$, protože $\operatorname{tr}(\mathbf{A} + \mathbf{B}) = \operatorname{tr}\mathbf{A} + \operatorname{tr}\mathbf{B}$ a $\operatorname{tr}(\alpha\mathbf{A}) = \alpha \operatorname{tr}\mathbf{A}$. Např. $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$ má stopu $1 + (-1) = 0$.

^def-stopa

## §5 Jak podprostory vyrábět

Hledáme nejmenší podprostor, který obsahuje daný vektor $\vec{x} \neq \vec{0}$.

> [!veta] Tvrzení · pozn. 2.4
> Pro každé $\vec{x} \in L$ je $\{\alpha\vec{x} \mid \alpha \in \mathbb{F}\} \le L$.
>
> > [!note]- Důkaz
> > Množina je neprázdná, obsahuje $\vec{x} = 1 \cdot \vec{x}$. Součet dvou násobků je násobek: $\alpha\vec{x} + \beta\vec{x} = (\alpha + \beta)\vec{x}$ (axiom 7). Násobek násobku je násobek: $\gamma(\alpha\vec{x}) = (\gamma\alpha)\vec{x}$ (axiom 5).

> [!pozor] Skalár se píše zleva
> V lineárním prostoru je jen násobení $\mathbb{F} \times L \to L$, tedy skalár zleva: $\gamma \cdot (\alpha\vec{x}) = (\gamma\alpha)\vec{x}$. Zápis $\vec{x} \cdot \gamma$ není definovaný, i když by „vyšel“ stejně.

Proč je to ten **nejmenší** podprostor obsahující $\vec{x}$: každý podprostor, ve kterém leží $\vec{x}$, musí kvůli uzavřenosti na násobení obsahovat i všechna $\alpha\vec{x}$. Geometricky je to přímka přes počátek ve směru $\vec{x}$.

Stejně je $\{\alpha\vec{x} + \beta\vec{y} \mid \alpha, \beta \in \mathbb{F}\}$ nejmenší podprostor, který obsahuje $\vec{x}$ i $\vec{y}$. Výraz $\alpha\vec{x} + \beta\vec{y}$ je lineární kombinace a z toho vznikne obecná definice v §6.

> [!obrazek] Přímka a rovina v $\mathbb{R}^3$
> ![[lag03-obal.png]]
> *Modrá čárkovaná: všechny násobky x, tedy přímka span{x}. Zelená rovina: všechny kombinace αx + βy, tedy span{x, y}. Zelená šipka x + y leží v rovině také. Obě prochází nulou.*

## §6 Lineární kombinace

> [!definice] Definice ♥ · pozn. 2.8
> Buď $L$ lineární prostor nad $\mathbb{F}$. Buďte $\vec{x}_1, \dots, \vec{x}_n \in L$, $\alpha_1, \dots, \alpha_n \in \mathbb{F}$, $n \in \mathbb{N}_0$. Vektor
>
> $$
> \alpha_1\vec{x}_1 + \alpha_2\vec{x}_2 + \dots + \alpha_n\vec{x}_n = \sum_{i=1}^{n} \alpha_i\vec{x}_i \in L
> $$
>
> nazveme *lineární kombinací* vektorů $\vec{x}_1, \dots, \vec{x}_n$. Skaláry $\alpha_1, \dots, \alpha_n$ nazýváme *koeficienty* této lineární kombinace. Lineární kombinace se nazývá *triviální*, jestliže $\alpha_1 = \dots = \alpha_n = 0$.

^def-lk

> [!lidsky] Lidsky
> Lineární kombinace je recept: vezmi $\alpha_1$ dávek první ingredience, $\alpha_2$ dávek druhé… a všechno smíchej. Triviální kombinace je „od všeho nula dávek“ a dá vždy $\vec{0}$.
>
> Nulu ale umí dát i netriviální kombinace, např. $1 \cdot \vec{x} + (-1) \cdot \vec{x} = \vec{0}$ nebo $2 \cdot (1; 1) - 1 \cdot (2; 2) = (0; 0)$. Kdy se to stát může, je téma příští přednášky (lineární závislost, 2. 10.).

> [!example] Cukrárna, vlastní čísla (v duchu příkladu 2.9)
> Suroviny zapíšeme jako vektor (mouka v kg; vejce v ks; cukr v kg). Bábovka potřebuje $\vec{b} = (0{,}4;\ 4;\ 0{,}2)$, koláč $\vec{k} = (0{,}3;\ 2;\ 0{,}15)$. Objednávka 3 bábovek a 5 koláčů je lineární kombinace:
>
> $$
> 3\vec{b} + 5\vec{k} = (1{,}2 + 1{,}5;\ 12 + 10;\ 0{,}6 + 0{,}75) = (2{,}7;\ 22;\ 1{,}35)
> $$
>
> Při cenách 20 Kč/kg mouky, 5 Kč/vejce a 25 Kč/kg cukru stojí suroviny $2{,}7 \cdot 20 + 22 \cdot 5 + 1{,}35 \cdot 25 = 54 + 110 + 33{,}75 = 197{,}75$ Kč. I cena je lineární kombinace, tentokrát cen s koeficienty $2{,}7$, $22$ a $1{,}35$.

## §7 Lineární obal

> [!definice] Definice ♥ · pozn. 2.11
> Buď $L$ lineární prostor nad $\mathbb{F}$. Pro množinu vektorů $M \subseteq L$ definujeme její *lineární obal* $\operatorname{span} M$ jako množinu všech lineárních kombinací prvků z $M$, tedy
>
> $$
> \operatorname{span} M = \{\alpha_1\vec{x}_1 + \dots + \alpha_k\vec{x}_k \mid k \in \mathbb{N}_0,\ \vec{x}_1, \dots, \vec{x}_k \in M,\ \alpha_1, \dots, \alpha_k \in \mathbb{F}\}.
> $$

^def-span

> [!pozor] Nezapomeň, odkud jsou koeficienty
> V množině musí být i podmínka $\alpha_1, \dots, \alpha_k \in \mathbb{F}$. Bez ní není řečeno, čím se vektory násobí, a u ♥ definice ve zkoušce (část B1) se to počítá jako chyba.

> [!lidsky] Lidsky
> Lineární obal je všechno, co se dá z vektorů v $M$ namíchat. Z jednoho nenulového vektoru přímka, ze dvou různoběžných rovina. $M$ smí být i nekonečná, ale každá jednotlivá kombinace bere jen konečně mnoho vektorů ($k$ je přirozené číslo).

Příklady:

$$
\{\alpha\vec{x} \mid \alpha \in \mathbb{F}\} = \operatorname{span}\{\vec{x}\}, \qquad \{\alpha\vec{x} + \beta\vec{y} \mid \alpha, \beta \in \mathbb{F}\} = \operatorname{span}\{\vec{x}, \vec{y}\}
$$

Poznámky:

- $\operatorname{span}\emptyset = \{\vec{0}\}$. Z prázdné množiny jde vzít jen $k = 0$ vektorů a prázdný součet je podle konvence nulový vektor `pozn. 2.10`.
- $\operatorname{span} L = L$ a $\operatorname{span} V = V$ pro libovolné $V \le L$. Podprostor je uzavřený na lineární kombinace, takže nic nového nevznikne.
- $\operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\} = \{\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n \mid \alpha_1, \dots, \alpha_n \in \mathbb{F}\}$. U konečné množiny stačí brát vždy všechny vektory, nepoužitý dostane koeficient $0$.

> [!veta] Obal je nejmenší podprostor · věta 2.13 a cvičení 2.14
> - **Věta 2.13:** ==Buď $L$ lineární prostor a $M \subseteq L$.== Potom **$\operatorname{span} M$ je lineární podprostor $L$.**
> - **Cvičení 2.14:** $\operatorname{span} M = \bigcap \{V \mid M \subseteq V \le L\}$, tedy průnik všech podprostorů, které obsahují $M$. Je to nejmenší podprostor obsahující $M$.

^veta-213

> [!lidsky] Lidsky
> „Obal“ doslova: nejtěsnější podprostor, do kterého se $M$ vejde. Každý podprostor obsahující $M$ musí kvůli uzavřenosti obsahovat i všechny kombinace prvků $M$, a víc než ty kombinace už potřeba není.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč definice lineárního podprostoru vyžaduje $V \neq \emptyset$?
> $\emptyset$ splňuje obě podmínky uzavřenosti prázdně, ale nemá nulový vektor. Z $V \neq \emptyset$ plyne existence $\vec{x} \in V$, a tedy $\vec{0} = 0 \cdot \vec{x} \in V$.

> [!karta|02]- Proč každý podprostor $V \le L$ obsahuje $\vec{0}$ a s každým $\vec{x}$ i $-\vec{x}$?
> $V$ je neprázdný, takže obsahuje nějaké $\vec{x}$. Z uzavřenosti na násobení: $\vec{0} = 0 \cdot \vec{x} \in V$ a $-\vec{x} = (-1) \cdot \vec{x} \in V$.

> [!karta|03]- Které axiomy je u podprostoru potřeba zvlášť zdůvodnit a proč ostatní ne?
> Jen **existence nulového a opačného vektoru**. Ostatní jsou tvaru „pro všechna“, platí v $L$, a tedy i ve $V \subseteq L$.

> [!karta|07]- Kdy je množina řešení soustavy lineárních rovnic podprostor $\mathbb{F}^n$?
> Když je soustava **homogenní** (pravé strany nulové). Nehomogenní soustava podprostor netvoří, protože nulový vektor ji nesplňuje.

> [!karta|09]- Který podprostor je nejmenší a který největší v každém lineárním prostoru $L$?
> Nejmenší $\{\vec{0}\}$ (triviální), největší $L$ sám.

> [!karta|13]- Čemu se rovná $\operatorname{span}\emptyset$ a proč?
> $\{\vec{0}\}$. Z $\emptyset$ lze vzít jen $k = 0$ vektorů a **prázdný součet je nulový vektor** (konvence 2.10).

> [!karta|14]- Čemu se rovná $\operatorname{span} V$ pro podprostor $V \le L$?
> Samotnému $V$. Podprostor je uzavřený na lineární kombinace, takže nic nového nevznikne. Speciálně $\operatorname{span} L = L$.

> [!karta|16]- Jak geometricky vypadá $\operatorname{span}\{\vec{x}, \vec{y}\}$ v $\mathbb{R}^3$?
> Pro $\vec{x}, \vec{y}$, které nejsou násobky jednoho vektoru: **rovina přes počátek**. Jsou-li to násobky téhož nenulového vektoru, jen přímka; pro $\vec{x} = \vec{y} = \vec{0}$ jen $\{\vec{0}\}$.

> [!karta|22]- Jak nejrychleji ukázat, že množina **není** lineární podprostor?
> 1. Zkontroluj **nulový vektor**: podmínka s nenulovou pravou stranou ($a + b = 1$) ho vylučuje, a tím je hotovo.
> 2. Jinak najdi **konkrétní protipříklad**: dva prvky, jejichž součet z množiny vypadne, nebo prvek a číslo (často $-1$ nebo $2$), jehož násobek vypadne. Podezřelé jsou nelineární výrazy ($x^2$, $|x|$, $xy$).
> 3. Na „ne“ stačí konkrétní čísla, na „ano“ je potřeba obecný důkaz obou uzavřeností.

### Příklady na procvičení

> [!priklad|04]- Je přímka $y = x + 1$ lineární podprostor $\mathbb{R}^2$?
> **Není**: neobsahuje nulový vektor $(0; 0)$. Podprostory $\mathbb{R}^2$ jsou jen $\{\vec{0}\}$, přímky **přes počátek** a celé $\mathbb{R}^2$.

> [!priklad|05]- Je první kvadrant $\{(x; y) \mid x, y \ge 0\}$ podprostor $\mathbb{R}^2$?
> **Není.** Na sčítání uzavřený je, na násobení skalárem ne: $(-1) \cdot (1; 1) = (-1; -1)$ vypadne.

> [!priklad|06]- Je $\{\vec{0}, \vec{x}\}$ pro $\vec{x} \neq \vec{0}$ podprostor $L$ (nad číselným tělesem)?
> **Není**: $\vec{x} + \vec{x} = 2\vec{x}$ není ani $\vec{0}$, ani $\vec{x}$. Podprostor s nenulovým vektorem obsahuje všechny jeho násobky, tedy nekonečně mnoho vektorů.

> [!priklad|08]- Dokaž: množina řešení $S$ soustavy $\alpha x + \beta y = 0$, $\gamma x + \delta y = 0$ je podprostor $\mathbb{R}^2$.
> $(0; 0) \in S$. Součet: $\alpha(x_1 + x_2) + \beta(y_1 + y_2) = (\alpha x_1 + \beta y_1) + (\alpha x_2 + \beta y_2) = 0 + 0$. Násobek: $\alpha(rx_1) + \beta(ry_1) = r \cdot 0 = 0$. Stejně druhá rovnice.

> [!priklad|10]- Dokaž, že $\{\alpha\vec{x} \mid \alpha \in \mathbb{F}\} \le L$.
> Neprázdná: obsahuje $1 \cdot \vec{x}$. Součet: $\alpha\vec{x} + \beta\vec{x} = (\alpha + \beta)\vec{x}$. Násobek: $\gamma(\alpha\vec{x}) = (\gamma\alpha)\vec{x}$.

> [!priklad|11]- Proč jsou spojité funkce $C(\mathbb{R})$ podprostor $\mathbb{R}^{\mathbb{R}}$?
> Nulová funkce je spojitá, součet dvou spojitých funkcí je spojitý a násobek spojité funkce číslem je spojitý.

> [!priklad|12]- Tvoří matice $2 \times 2$ se stopou $0$ podprostor $\mathbb{F}^{2 \times 2}$?
> **Ano**: $\operatorname{tr}(\mathbf{A} + \mathbf{B}) = \operatorname{tr}\mathbf{A} + \operatorname{tr}\mathbf{B} = 0$ a $\operatorname{tr}(\alpha\mathbf{A}) = \alpha \operatorname{tr}\mathbf{A} = 0$; nulová matice má stopu 0.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|17]- Je $M = \{(x; y) \in \mathbb{R}^2 \mid x^2 = 4y^2\}$ lineární podprostor $\mathbb{R}^2$?
> **Ne.** $(2; 1) \in M$ i $(2; -1) \in M$ (v obou případech $4 = 4$), ale jejich součet $(4; 0)$ do $M$ nepatří: $16 \ne 0$. $M$ není uzavřená na sčítání. Geometricky jsou to dvě přímky $y = \pm x/2$ a sjednocení dvou přímek podprostor není.

> [!priklad|18]- Je $\{ax^2 + bx + c \in \mathbb{R}^{\le 2}[x] \mid a - 2b + c = 0\}$ lineární podprostor $\mathbb{R}^{\le 2}[x]$?
> **Ano.**
> - Neprázdná: nulový polynom ($a = b = c = 0$) podmínku splňuje.
> - Součet: z $a_1 - 2b_1 + c_1 = 0$ a $a_2 - 2b_2 + c_2 = 0$ plyne $(a_1 + a_2) - 2(b_1 + b_2) + (c_1 + c_2) = 0 + 0 = 0$.
> - Násobek: $\alpha a - 2\alpha b + \alpha c = \alpha(a - 2b + c) = \alpha \cdot 0 = 0$.
>
> Obecně: množina popsaná **homogenními lineárními** rovnicemi v koeficientech je vždy podprostor.

> [!priklad|19]- Je $\{ax^2 + bx + c \in \mathbb{R}^{\le 2}[x] \mid b^2 + c = 0\}$ lineární podprostor $\mathbb{R}^{\le 2}[x]$?
> **Ne.** $p = x - 1$ ($b = 1$, $c = -1$: $1 - 1 = 0$) do množiny patří, ale $2p = 2x - 2$ ne: $b^2 + c = 4 - 2 = 2 \ne 0$. Kvůli $b^2$ není množina uzavřená na násobení číslem.

> [!priklad|20]- Je $\{ax^2 + bx + c \in \mathbb{R}^{\le 2}[x] \mid a + b = 1\}$ lineární podprostor $\mathbb{R}^{\le 2}[x]$?
> **Ne.** Nulový polynom má $a + b = 0 \ne 1$, takže v množině není, ale každý podprostor nulový vektor obsahuje. Nenulová pravá strana znamená rovnou „ne“.

> [!priklad|21]- Je $\left\{\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathbb{R}^{2 \times 2} \mid ad = 0\right\}$ lineární podprostor $\mathbb{R}^{2 \times 2}$?
> **Ne.** $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ i $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ mají $ad = 0$, ale jejich součet je jednotková matice s $ad = 1 \ne 0$. Množina není uzavřená na sčítání.

---
← [[LAG 02 – Příklady lineárních prostorů|25. 9. 2026 Příklady lineárních prostorů]] · [[LAG 04 – Lineární závislost a nezávislost|2. 10. 2026 Lineární závislost a nezávislost]] →

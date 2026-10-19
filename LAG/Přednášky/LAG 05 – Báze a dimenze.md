---
predmet: LAG
prednaska: 5
datum: 2026-10-07
zdroj: "V poznámkách věta 3.7 a kapitola 4 (4.1–4.16)"
tags: [prednaska, LAG]
---

# LAG 05 – Báze a dimenze

*Přednáška 5 · středa 7. 10. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `věta 3.7` · `generující posloupnost` · `jednoznačnost vyjádření` · `báze` · `kanonická báze` · `věta 4.5` · `dimenze` · `výběr báze` · `doplnění na bázi` · `dimenze podprostoru`

Minule jsme poznali [[lineární nezávislost]]: v nezávislé posloupnosti není žádný vektor navíc. Dnes to spojíme s [[lineární obal|obalem]]. Posloupnost, která generuje celý prostor a přitom nemá nic navíc, je [[báze]]: každý vektor se z ní dá poskládat, a to jediným způsobem. Všechny báze daného prostoru mají stejně prvků a tomu číslu se říká [[dimenze]]. Na konci uvidíme, že bázi jde vždycky vybrat z generátorů nebo doplnit z nezávislých vektorů.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| věta 3.7 | k LN posloupnosti přidám $\vec{v}$ a zůstane LN $\iff \vec{v} \notin \operatorname{span}$ | $((1; 0), (0; 1))$ je LN, protože $(0; 1) \notin \operatorname{span}\{(1; 0)\}$ |
| [[generující posloupnost]] (4.1 ♥) | $L = \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}$: každý vektor jde poskládat | $((1; 0), (0; 1), (1; 1))$ generuje $\mathbb{R}^2$ |
| věta 4.2 | LN $\iff$ každý vektor jde poskládat **nejvýše jedním** způsobem | |
| [[báze]] (4.3 ♥) | LN + generuje: každý vektor jde poskládat **právě jedním** způsobem | $((1; 0), (1; 1))$ je báze $\mathbb{R}^2$ |
| [[kanonická báze]] (4.4 ♥) | $\mathcal{E} = (\vec{e}_1, \dots, \vec{e}_n)$, jednička na $i$-tém místě | $(x; y) = x\vec{e}_1 + y\vec{e}_2$ |
| věta 4.5 | báze = minimální generující = maximální LN posloupnost | |
| věta 4.7 | všechny báze mají stejně prvků | |
| [[dimenze]] (4.8 ♥) | $\dim L$ = počet prvků báze, případně $\infty$ | $\dim\mathbb{F}^n = n$, $\dim\mathbb{F}[x] = \infty$ |
| věta 4.11 | z konečné generující množiny jde vybrat bázi | $\operatorname{span}\{\vec{x}_1, \vec{x}_2, \vec{x}_1 + \vec{x}_2\}$ má bázi $(\vec{x}_1, \vec{x}_2)$, je-li $(\vec{x}_1, \vec{x}_2)$ LN |
| doplnění na bázi | LN posloupnost jde doplnit na bázi ($\dim L < \infty$) | |
| důsledek | pro $n = \dim L$ vektorů: báze $\iff$ LN $\iff$ generuje | |
| dimenze podprostoru | $V \le L \Rightarrow \dim V \le \dim L$; pro $\dim L < \infty$ je $V = L \iff \dim V = \dim L$ | |

## §1 Přidání vektoru k nezávislé posloupnosti

Nejdřív drobnost, kterou budeme pořád používat: odebráním vektoru se obal nezmění právě tehdy, když byl ten vektor zbytečný.

> [!navic] Pozorování: kdy se obal odebráním nezmění
> $$
> \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\} = \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{n-1}\} \iff \vec{x}_n \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{n-1}\}.
> $$
>
> Zleva doprava: $\vec{x}_n$ leží v levém obalu, tedy i v pravém. Zprava doleva: v každé kombinaci $\alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$ nahradíš $\vec{x}_n$ jeho vyjádřením z ostatních a dostaneš kombinaci jen $\vec{x}_1, \dots, \vec{x}_{n-1}$. Na pořadí nezáleží, takže totéž platí pro odebrání libovolného $\vec{x}_i$.

^poz-obal

Z [[LAG 04 – Lineární závislost a nezávislost#^veta-36|věty 3.6]] (LZ $\iff$ některý vektor je kombinací předchozích) plyne obrácením obou stran popis nezávislosti, který se hodí do důkazů:

$$
(\vec{x}_1, \dots, \vec{x}_n) \text{ je LN} \iff (\forall i \in \{1, \dots, n\})\big(\vec{x}_i \notin \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}\}\big).
$$

^ln-predchozi

> [!lidsky] Lidsky
> Projdi vektory zleva doprava. Posloupnost je nezávislá, právě když každý další vektor přinese nový směr, který z těch předchozích poskládat nejde. První vektor tedy nesmí být nulový ($\operatorname{span}\emptyset = \{\vec{0}\}$).

> [!veta] Věta 3.7
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $\vec{x}_1, \dots, \vec{x}_n \in L$ a předpokládejme, že $(\vec{x}_1, \dots, \vec{x}_n)$ je LN.== Potom pro $\vec{v} \in L$ platí
>
> $$
> (\vec{x}_1, \dots, \vec{x}_n, \vec{v}) \text{ je LN} \iff \vec{v} \notin \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}.
> $$
>
> > [!note]- Důkaz
> > Z předpokladu a popisu LN výše platí $\vec{x}_i \notin \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}\}$ pro všechna $i \in \{1, \dots, n\}$. Podle téhož popisu je prodloužená posloupnost $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ LN, právě když navíc platí podmínka pro poslední vektor, tedy $\vec{v} \notin \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}$.

^veta-37

> [!lidsky] Lidsky
> Nezávislou sadu smíš rozšířit o nový vektor bez ztráty nezávislosti, právě když ukazuje „ven“ z toho, co už sada umí namíchat. V $\mathbb{R}^3$: ke dvěma nezávislým vektorům přidáš třetí, který nevede po jejich rovině.

> [!obrazek] Věta 3.7 v $\mathbb{R}^3$
> ![[lag05-veta37.png]]
> *Modré $\vec{x}_1, \vec{x}_2$ jsou LN a jejich obal je zelená rovina. Oranžový $\vec{v}$ z roviny vyčnívá, takže $(\vec{x}_1, \vec{x}_2, \vec{v})$ je LN. Červený $\vec{w}$ leží v rovině, takže $(\vec{x}_1, \vec{x}_2, \vec{w})$ je LZ.*

> [!pozor] Předpoklad LN je potřeba
> Bez něj tvrzení neplatí: $((1; 0), (2; 0))$ je LZ, a přidáním $(0; 1) \notin \operatorname{span}\{(1; 0), (2; 0)\}$ nezávislá posloupnost nevznikne (přidáním k LZ zůstane LZ, [[LAG 04 – Lineární závislost a nezávislost#^veta-33|věta 3.3]]).

## §2 Existence: generující posloupnost

Na začátku kapitoly je obrázek, který známe od přednášky 1: k bodu $(3; 2)$ v rovině dojdeš třemi kroky doprava a dvěma nahoru. Otázka „lze dojít ke každému bodu?“ je otázka existence, a tu řeší následující definice.

> [!navic] Co chceme od „souřadnic“
> Souřadný systém pro **body** potřebuje i počátek: posuneš-li počátek, změní se souřadnice všech bodů. My pracujeme s **vektory**, a tam je počátek daný, je to nulový vektor. Nežádáme ani to, co bývá ve škole, totiž aby základní vektory byly na sebe kolmé a měly délku 1. Stačí dva požadavky:
>
> 1. **existence:** ke každému vektoru se z vybraných vektorů dá dojít (generují, §2),
> 2. **jednoznačnost:** dá se k němu dojít jediným způsobem (jsou LN, §3).
>
> Dvojice „existence a jednoznačnost“ se v matematice objevuje často a obvykle se řeší každá zvlášť. Splňuje-li posloupnost obojí, neříká se jí souřadný systém (to slovo zůstává pro body s počátkem), ale [[báze]].

> [!definice] Definice ♥ · pozn. 4.1
> Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$. Řekneme, že posloupnost $(\vec{x}_1, \dots, \vec{x}_n)$ *generuje* $L$, jestliže
>
> $$
> L = \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}.
> $$

^def-generuje

> [!lidsky] Lidsky
> Vektory generují prostor, když se z nich dá poskládat úplně každý jeho vektor. Prakticky: pro libovolné $\vec{v} \in L$ má úloha „najdi $\alpha_1, \dots, \alpha_n \in \mathbb{F}$ taková, že $\vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n$“ **aspoň jedno řešení**. V $\mathbb{R}^n$ je to soustava rovnic s neznámými $\alpha_i$.

> [!example] Příklad: $\mathbb{R}^2$
> Posloupnost $((1; 0), (0; 1))$ generuje $\mathbb{R}^2$, protože
>
> $$
> \begin{pmatrix} x \\ y \end{pmatrix} = x\begin{pmatrix} 1 \\ 0 \end{pmatrix} + y\begin{pmatrix} 0 \\ 1 \end{pmatrix}.
> $$
>
> Generuje ho i $((1; 0), (0; 1), (1; 1))$, jen tam už je jeden vektor navíc, a $(3; 2)$ pak jde zapsat třeba jako $3(1; 0) + 2(0; 1) + 0(1; 1)$ i jako $1(1; 0) + 0(0; 1) + 2(1; 1)$.

## §3 Jednoznačnost

Generování zaručí, že vyjádření existuje. Kdy je jediné, říká nezávislost.

> [!veta] Věta 4.2
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$.== Posloupnost $(\vec{x}_1, \dots, \vec{x}_n)$ je LN, **právě když každý vektor $\vec{v} \in L$ lze vyjádřit jako lineární kombinaci $\vec{x}_1, \dots, \vec{x}_n$ nejvýše jedním způsobem.**
>
> > [!note]- Důkaz
> > **⇐:** Nulový vektor jde vyjádřit triviálně, $\vec{0} = 0\vec{x}_1 + \dots + 0\vec{x}_n$. Je-li každé vyjádření nejvýše jedno, žádné jiné neexistuje, a to je přesně definice LN.
> >
> > **⇒:** Nechť $\vec{v} \in L$ má dvě vyjádření:
> >
> > $$
> > \vec{v} = \alpha_1\vec{x}_1 + \dots + \alpha_n\vec{x}_n = \beta_1\vec{x}_1 + \dots + \beta_n\vec{x}_n.
> > $$
> >
> > Odečtením dostaneme
> >
> > $$
> > (\alpha_1 - \beta_1)\vec{x}_1 + \dots + (\alpha_n - \beta_n)\vec{x}_n = \vec{0}.
> > $$
> >
> > Z LN jsou všechny koeficienty nulové: $\alpha_1 - \beta_1 = 0, \dots, \alpha_n - \beta_n = 0$, tedy $\alpha_1 = \beta_1, \dots, \alpha_n = \beta_n$. Obě vyjádření jsou stejná.

^veta-42

> [!lidsky] Lidsky
> Kdyby šlo k jednomu bodu dojít dvěma různými recepty, jejich rozdíl by byl netriviální recept na nulu, a to nezávislé vektory nedovolí. Nezávislost tedy znamená „žádné dva recepty na totéž“.

> [!pozor] Nejvýše jedním, ne právě jedním
> LN samotná nezaručí, že vyjádření **existuje**. $((1; 0))$ je LN v $\mathbb{R}^2$, ale $(0; 1)$ z ní poskládat nejde. Právě jedním způsobem jde vyjádřit každý vektor až u posloupnosti, která je LN **a** generuje.

## §4 Báze

> [!definice] Definice ♥ · pozn. 4.3
> Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$. Posloupnost $(\vec{x}_1, \dots, \vec{x}_n)$ se nazývá *báze* $L$, jestliže je LN a generuje $L$.

^def-baze

> [!lidsky] Lidsky
> Báze je souřadnicový systém prostoru: sada směrů, ze kterých poskládáš každý vektor (generuje), a to jediným receptem (LN, věta 4.2). Nic nechybí a nic není navíc. Čísla v tom jediném receptu budou příště *souřadnice* vektoru v dané bázi.

> [!definice] Definice ♥ · pozn. 4.4
> V $\mathbb{F}^n$ nad $\mathbb{F}$ definujeme posloupnost
>
> $$
> \mathcal{E} = (\vec{e}_1, \vec{e}_2, \dots, \vec{e}_n) = \left(\begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \dots, \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{pmatrix}\right), \qquad \text{tj. } [\vec{e}_i]_j = \begin{cases} 0, & j \neq i, \\ 1, & j = i. \end{cases}
> $$
>
> Nazýváme ji *kanonická báze*.

^def-kanonicka

> [!lidsky] Lidsky
> [[kanonická báze|Kanonická báze]] jsou „jednotkové kroky“ podél os: v $\mathbb{R}^3$ krok doprava $(1; 0; 0)$, dopředu $(0; 1; 0)$ a nahoru $(0; 0; 1)$. Vektor $(4; -2; 7)$ je pak prostě 4 kroky prvním směrem, $-2$ druhým a 7 třetím, takže souřadnice v kanonické bázi jsou přímo složky vektoru.

Zápis $[\vec{e}_i]_j$ znamená „$j$-tá složka vektoru $\vec{e}_i$“. Báze se značí psacími velkými písmeny ($\mathcal{E}$, $\mathcal{B}$), aby se nepletly s množinami a prostory; místo „kanonická“ se někdy říká *standardní* báze. Že je $\mathcal{E}$ opravdu báze, je vidět rovnou:

- **LN:** každé $\vec{e}_i$ má jedničku na místě, kde mají všechny ostatní nulu, takže ho z ostatních (ani z předchozích) poskládat nejde.
- **Generuje:** $(x_1; \dots; x_n) = x_1\vec{e}_1 + \dots + x_n\vec{e}_n$, koeficienty jsou přímo složky vektoru.

> [!obrazek] Stejný vektor ve dvou bázích $\mathbb{R}^2$
> ![[lag05-souradnice.png]]
> *Vlevo kanonická báze: zelený $\vec{v} = (3; 2)$ je 3 modré kroky $\vec{e}_1$ a 2 oranžové kroky $\vec{e}_2$. Vpravo báze $\vec{b}_1 = (1; 0)$, $\vec{b}_2 = (1; 1)$: tentýž vektor je 1 modrý krok a 2 oranžové, $(3; 2) = 1 \cdot (1; 0) + 2 \cdot (1; 1)$.*

> [!pozor] Báze je posloupnost, ne množina
> Záleží na pořadí: $((1; 0), (0; 1))$ a $((0; 1), (1; 0))$ jsou dvě různé báze $\mathbb{R}^2$ a vektor $(3; 2)$ v nich má čísla $(3; 2)$ a $(2; 3)$. Proto se píše do kulatých závorek. A prostor má bází nekonečně mnoho, kanonická je jen ta nejpohodlnější.

## §5 Tři pohledy na bázi

> [!veta] Věta 4.5
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a $\vec{x}_1, \dots, \vec{x}_n \in L$.== Následující výroky jsou **ekvivalentní**:
>
> 1. $(\vec{x}_1, \dots, \vec{x}_n)$ je báze $L$ (je LN a generuje $L$).
> 2. $(\vec{x}_1, \dots, \vec{x}_n)$ je **minimální** (vzhledem k inkluzi) generující posloupnost: generuje $L$, ale žádná její vlastní podposloupnost už $L$ negeneruje.
> 3. $(\vec{x}_1, \dots, \vec{x}_n)$ je **maximální** (vzhledem k inkluzi) LN posloupnost: je LN a každá delší $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ s $\vec{v} \in L$ je LZ.
>
> > [!note]- Důkaz
> > **(1) ⇔ (2):** Obě strany požadují, aby posloupnost generovala $L$; zbývá porovnat zbytek. Podle [[#^poz-obal|pozorování v §1]] se obal po odebrání $\vec{x}_i$ nezmění, právě když je $\vec{x}_i$ kombinací ostatních. Tedy:
> >
> > $(\vec{x}_1, \dots, \vec{x}_n)$ je LN $\iff$ žádný $\vec{x}_i$ není kombinací ostatních (věta 3.6) $\iff$ žádný $\vec{x}_i$ nejde z generátorů vyjmout, aby zbytek pořád generoval.
> >
> > Když nejde vyjmout žádný jednotlivý vektor, nejde vyjmout ani víc najednou (obal menší podposloupnosti je podmnožinou obalu větší).
> >
> > **(1) ⇒ (3):** Báze je LN. Pro libovolné $\vec{v} \in L$ je $\vec{v} \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\} = L$, takže podle věty 3.7 je $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ LZ.
> >
> > **(3) ⇒ (1):** Posloupnost je LN, zbývá generování. Pro libovolné $\vec{v} \in L$ je $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ LZ, takže podle věty 3.7 je $\vec{v} \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}$. Každý vektor $L$ tedy leží v obalu.

^veta-45

> [!lidsky] Lidsky
> Báze je přesně na hraně. Uber z ní cokoli a přestane generovat. Přidej k ní cokoli a přestane být nezávislá. Je to nejmenší sada, která ještě všechno poskládá, a zároveň největší sada, ve které ještě nic není navíc.

> [!pozor] Minimální vzhledem k inkluzi ≠ nejkratší
> „Minimální“ tu znamená, že z posloupnosti **nejde nic vyhodit** (inkluze = být podposloupností), ne že je nejkratší ze všech generujících. Kdyby se počítal jen počet prvků, nebylo by to zatím dokázané: a priori by mohl mít prostor dvě báze různé délky, obě minimální, protože kratší nemusí být podposloupností delší. Že to nenastane, říká až věta 4.7 v §6, a teprve pak má smysl definovat dimenzi.

## §6 Dimenze

Aby šlo mluvit o „počtu směrů“ prostoru, musí mít všechny báze stejně prvků. To zaručí následující lemma.

> [!veta] Lemma 4.6 (Steinitzova věta o výměně) \*
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $(\vec{x}_1, \dots, \vec{x}_k)$ LN posloupnost a $(\vec{y}_1, \dots, \vec{y}_l)$ posloupnost, která generuje $L$.== Potom **$k \le l$**.
>
> V poznámkách je lemma formulované pro konečnou generující *množinu* $G$ s $l = |G|$; pro posloupnost je to totéž (opakované prvky jen zvětší $l$).

^lemma-46

Lemma se zde nedokazuje a ke zkouškové písemce není nutné (v poznámkách je označené \*); důkaz je matematickou indukcí a dá se tam dohledat. Plné znění navíc říká, že $l - k$ vhodných vektorů $\vec{y}_j$ spolu s $\vec{x}_1, \dots, \vec{x}_k$ pořád generuje $L$: $k$ generátorů jde **vyměnit** za $k$ nezávislých vektorů a posloupnost generuje dál. Odtud název.

> [!navic] V čem je důkaz těžký
> Kdybys věděl, že všechny báze mají $n$ prvků, lemma by šlo odvodit snadno: LN posloupnost jde doplnit na bázi (má tedy nejvýš $n$ prvků) a z generující jde bázi vybrat (má tedy aspoň $n$ prvků). Jenže to je kruh, protože věta 4.7 o stejné velikosti bází se dokazuje právě z lemmatu. Důkaz lemmatu se tedy musí obejít bez ní.

> [!lidsky] Lidsky
> Nezávislých vektorů nemůže být víc než generátorů. Když v rovině umíš všechno poskládat ze dvou vektorů, tři nezávislé vektory tam nenajdeš.

> [!veta] Věta 4.7
> ==Buď $L$ lineární prostor nad $\mathbb{F}$.== **Každá báze $L$ (pokud existuje) má stejný počet prvků.**
>
> > [!note]- Důkaz
> > Buďte $(\vec{x}_1, \dots, \vec{x}_k)$ a $(\vec{y}_1, \dots, \vec{y}_l)$ dvě báze. První je LN a druhá generuje, takže podle lemmatu $k \le l$. Role jde prohodit: druhá je LN a první generuje, tedy $l \le k$. Dohromady $k = l$.

^veta-47

> [!lidsky] Lidsky
> Báze jsou různé „sady základních směrů“, ale všechny stejně velké: v rovině vždy dva vektory, v prostoru tři. Důvod je lemma o výměně: nezávislých vektorů nemůže být víc než generátorů, a báze je obojí najednou, takže dvě báze se navzájem „uhlídají“ ($k \le l$ i $l \le k$).

> [!definice] Definice ♥ · pozn. 4.8
> Buď $L$ lineární prostor nad $\mathbb{F}$. Definujeme jeho *dimenzi* jako počet prvků jeho báze. Pokud pro žádné $n \in \mathbb{N}_0$ nemá $n$-prvkovou bázi, řekneme, že má dimenzi nekonečno. Dimenzi $L$ značíme $\dim L$.

^def-dimenze

> [!lidsky] Lidsky
> Dimenze je počet nezávislých směrů, kterými se dá v prostoru pohybovat: přímka 1, rovina 2, prostor kolem nás 3. Díky větě 4.7 nezáleží na tom, kterou bázi spočítáš, číslo vyjde vždycky stejné.

### Příklady 4.9

- $\dim\{\vec{0}\} = 0$: bází je prázdná posloupnost $()$. Je LN a $\operatorname{span}\emptyset = \{\vec{0}\}$.
- $\dim\operatorname{span}\{\vec{x}\} = 1$ pro $\vec{x} \neq \vec{0}$: bází je $(\vec{x})$. Dále $\dim\operatorname{span}\{\vec{x}, \vec{y}\} = 2$, právě když je $(\vec{x}, \vec{y})$ LN.
- $\dim\mathbb{F}^n = n$: kanonická báze má $n$ prvků.
- $\dim\mathbb{F}^{\le n}[x] = n + 1$: bází je $(1, x, x^2, \dots, x^n)$. Pozor na $+1$ za konstantu.
- $\dim\mathbb{F}[x] = \infty$: posloupnost $(1, x, x^2, \dots, x^n)$ je LN pro každé $n$, protože $\alpha_0 + \alpha_1 x + \dots + \alpha_n x^n$ je [[nulový polynom]] jen pro $\alpha_0 = \dots = \alpha_n = 0$.

^pr-49

> [!navic] Proč z „LN pro každé $n$“ plyne nekonečná dimenze
> Kdyby $\mathbb{F}[x]$ měl konečnou bázi s $m$ prvky, ta by generovala, a LN posloupnost $(1, x, \dots, x^m)$ má $m + 1$ prvků. Lemma 4.6 by dalo $m + 1 \le m$, spor. Stejně je nekonečná dimenze prostoru [[posloupnosti|posloupností]] $\mathbb{R}^{\mathbb{N}}$: posloupnosti $(1, 0, 0, \dots)$, $(0, 1, 0, \dots)$, … jsou LN pro libovolný počet.

> [!navic] Nekonečné báze (pozn. 4.10 \*)
> Nezávislost a bázi jde zavést i pro nekonečné množiny vektorů: LN znamená, že každá konečná část je LN. Takové bázi se říká Hamelova. Pro polynomy funguje dobře: $(1, x, x^2, \dots)$ je báze $\mathbb{F}[x]$, protože každý polynom má jen konečně mnoho členů.
>
> Pozor, $((1, 0, 0, \dots), (0, 1, 0, \dots), \dots)$ **není** Hamelova báze $\mathbb{R}^{\mathbb{N}}$: lineární kombinace je vždy konečná, takže z nich poskládáš jen posloupnosti, které jsou od jistého místa nulové, třeba $(1, 1, 1, \dots)$ ne. Hamelova báze $\mathbb{R}^{\mathbb{N}}$ sice existuje (každý lineární prostor nějakou má, důkaz ale potřebuje axiom výběru, pozn. 4.10), ale nikdo ji nikdy nevypsal a spočetná být nemůže, a k počítání je proto k ničemu. Užitečná báze nekonečně rozměrných prostorů potřebuje nekonečné kombinace, tedy řady. Ke zkoušce to není potřeba.

## §7 Výběr báze z generátorů

> [!veta] Věta 4.11 (výběr báze z generující posloupnosti)
> ==Buď $L$ lineární prostor nad $\mathbb{F}$ a nechť $G$ je konečná generující množina $L$.== Potom **existují $\vec{x}_1, \dots, \vec{x}_n \in G$ takové, že $(\vec{x}_1, \dots, \vec{x}_n)$ je báze $L$.**
>
> > [!note]- Důkaz
> > Mohou nastat dvě situace.
> >
> > **a)** V $G$ není žádný vektor lineární kombinací ostatních. Pak jsou prvky $G$ LN (věta 3.6) a generují, takže stačí je seřadit do posloupnosti a máme bázi.
> >
> > **b)** Existuje $\vec{v} \in G$ takový, že $\vec{v} \in \operatorname{span}(G \setminus \{\vec{v}\})$. Pak $\operatorname{span}(G \setminus \{\vec{v}\}) = \operatorname{span} G = L$ ([[#^poz-obal|pozorování v §1]]), takže $G \setminus \{\vec{v}\}$ je také generující, a postup opakujeme s ní.
> >
> > Protože je $G$ konečná, může nastat b) jen konečněkrát, a nakonec nastane a).

^veta-411

> [!lidsky] Lidsky
> Máš-li konečnou sadu, ze které jde všechno poskládat, vyhazuj z ní zbytečné vektory (ty, které jdou poskládat ze zbytku), dokud nějaký zbytečný je. Co zbude, je báze. Důsledek: každý prostor generovaný konečně mnoha vektory má konečnou dimenzi.

> [!example] Příklad: báze a dimenze obalu
> $$
> V = \operatorname{span}\left\{\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}\right\} = \operatorname{span}\{\vec{x}_1, \vec{x}_2, \vec{x}_3\}.
> $$
>
> Z [[LAG 04 – Lineární závislost a nezávislost#§5 Jak závislost rozhodnout výpočtem|úlohy 3.5]] víme, že $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$, takže ho jde vyhodit: $V = \operatorname{span}\{\vec{x}_1, \vec{x}_2\}$. Dvojice $(\vec{x}_1, \vec{x}_2)$ je LN (žádný není násobkem druhého), dál už vyhazovat nejde.
>
> Proto **$(\vec{x}_1, \vec{x}_2)$ je báze $V$ a $\dim V = 2$**: $V$ je rovina v $\mathbb{R}^3$.

> [!obrazek] Výběr báze z generátorů
> ![[lag05-priklad.png]]
> *Modrý $\vec{x}_1$ a oranžový $\vec{x}_2$ tvoří bázi zelené roviny $V$ (tmavší rovnoběžník je jejich kombinace s koeficienty mezi 0 a 1). Červený čárkovaný $\vec{x}_3 = \vec{x}_1 + \vec{x}_2$ je úhlopříčka, leží ve stejné rovině a nic nového nepřidá.*

> [!pozor] Vybírá se z $G$, ne libovolně
> Věta říká, že bázi jde poskládat **přímo z generátorů**. Která to bude, záleží na pořadí vyhazování: tady by bází byla i $(\vec{x}_1, \vec{x}_3)$ nebo $(\vec{x}_2, \vec{x}_3)$. Počet prvků je ale vždy stejný, $\dim V = 2$.

## §8 Doplnění na bázi a dimenze podprostoru

Opačný směr k výběru: začneš s nezávislými vektory a přidáváš.

> [!veta] Věta 4.13 (doplnění LN posloupnosti na bázi)
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $\dim L = n < \infty$. Nechť $\vec{x}_1, \dots, \vec{x}_k \in L$ a nechť $(\vec{x}_1, \dots, \vec{x}_k)$ je LN.== Potom **existují $\vec{x}_{k+1}, \dots, \vec{x}_n \in L$ takové, že $(\vec{x}_1, \dots, \vec{x}_n)$ je báze $L$.**
>
> > [!note]- Důkaz
> > Pokud $(\vec{x}_1, \dots, \vec{x}_k)$ generuje $L$, je to báze. Jinak existuje $\vec{v} \in L$ mimo $\operatorname{span}\{\vec{x}_1, \dots, \vec{x}_k\}$ a podle věty 3.7 je $(\vec{x}_1, \dots, \vec{x}_k, \vec{v})$ zase LN. Tak pokračujeme.
> >
> > Každá LN posloupnost v $L$ má nejvýš $n$ prvků (lemma 4.6, báze s $n$ prvky generuje), takže se přidávání po konečně krocích zastaví. Zastaví se jen u posloupnosti, která generuje, tedy u báze, a ta má podle věty 4.7 přesně $n$ prvků.

^veta-doplneni

> [!lidsky] Lidsky
> Nezávislou sadu doplňuj vektory, které ukazují „ven“ z toho, co už sada umí. Dřív nebo později pokryješ všechno; v prostoru dimenze $n$ to bude přesně po $n$ vektorech.

> [!obrazek] Kolik vektorů mají LN a generující posloupnosti
> ![[lag05-pocty.png]]
> *Prostor dimenze 3. Modře: nezávislá posloupnost má nejvýš 3 vektory a doplňováním dojde k bázi. Oranžově: generující posloupnost má aspoň 3 vektory a výběrem (věta 4.11) dojde k bázi. Zelená čára: báze má přesně 3 vektory.*

> [!veta] Důsledek 4.15
> ==Buď $L$ lineární prostor nad $\mathbb{F}$, $\dim L = n < \infty$, a $\vec{x}_1, \dots, \vec{x}_n \in L$ (přesně $n$ vektorů).== Potom jsou následující výroky **ekvivalentní**:
>
> 1. $(\vec{x}_1, \dots, \vec{x}_n)$ je báze $L$,
> 2. $(\vec{x}_1, \dots, \vec{x}_n)$ je LN,
> 3. $(\vec{x}_1, \dots, \vec{x}_n)$ generuje $L$.
>
> > [!note]- Důkaz
> > (1) ⇒ (2) a (1) ⇒ (3) jsou z definice báze.
> >
> > **(2) ⇒ (1):** LN posloupnost doplníme na bázi. Ta má $n$ prvků, takže se nic nepřidalo a posloupnost sama je báze.
> >
> > **(3) ⇒ (1):** Z množiny $\{\vec{x}_1, \dots, \vec{x}_n\}$ (má nejvýš $n$ prvků) vybereme podle věty 4.11 bázi. Ta má $n$ prvků, takže se musely vybrat všechny a byly navzájem různé. Posloupnost sama je tedy báze.

^dusledek-n

> [!lidsky] Lidsky
> Když víš dimenzi a máš přesně tolik vektorů, stačí ověřit jen polovinu definice báze. V $\mathbb{R}^3$ jsou tři vektory bází, jakmile jsou nezávislé; generování už ověřovat nemusíš.
>
> Ověřuje se prakticky vždy LN, protože je to méně práce. LN znamená vyřešit **jednu** homogenní soustavu (pravá strana nulová). Generování znamená ukázat, že soustava má řešení pro **každou** pravou stranu $\vec{v}$. Na cvičení se tenhle důsledek používá velmi často.

> [!pozor] Počet musí sedět přesně
> Důsledek platí jen pro **přesně $n$** vektorů. Dva nezávislé vektory v $\mathbb{R}^3$ nejsou báze (negenerují) a čtyři generující vektory v $\mathbb{R}^3$ nejsou báze (jsou LZ).

> [!veta] Věta 4.16 (dimenze podprostoru)
> ==Nechť $L$ je lineární prostor a $V \le L$.== Potom **$\dim V \le \dim L$**. Navíc, je-li ==$\dim L < \infty$==, platí **$V = L \iff \dim V = \dim L$**.
>
> > [!note]- Důkaz
> > Pro $\dim L = \infty$ není co dokazovat. Nechť $\dim L = n < \infty$. Každá LN posloupnost ve $V$ je LN i v $L$, takže má nejvýš $n$ prvků (lemma 4.6). Vezmeme ve $V$ LN posloupnost s co nejvíce prvky. Ta je maximální LN posloupnost ve $V$, tedy podle věty 4.5 báze $V$, a $\dim V \le n$.
> >
> > Je-li $V = L$, jsou dimenze stejné. Naopak, je-li $\dim V = n$, je báze $V$ posloupnost $n$ nezávislých vektorů v $L$, podle důsledku tedy báze $L$, a $L = \operatorname{span}(\text{báze}) = V$.

^veta-dim-podprostoru

> [!lidsky] Lidsky
> Podprostor nemůže mít víc směrů než celý prostor. A má-li jich stejně, je to celý prostor: rovina uvnitř $\mathbb{R}^2$ je celé $\mathbb{R}^2$. Rovina uvnitř $\mathbb{R}^3$ má dimenzi $2 < 3$, a proto to celé $\mathbb{R}^3$ není.

> [!pozor] Druhá část potřebuje konečnou dimenzi
> Častá chyba je vynechat předpoklad $\dim L < \infty$. Polynomy bez absolutního členu $V = \operatorname{span}\{x, x^2, x^3, \dots\}$ tvoří podprostor $\mathbb{F}[x]$ s $\dim V = \infty = \dim\mathbb{F}[x]$, a přitom $V \neq \mathbb{F}[x]$, protože $1 \notin V$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- Jak jde popsat lineární nezávislost pomocí „předchozích“ vektorů?
> $(\vec{x}_1, \dots, \vec{x}_n)$ je LN, právě když **pro každé $i$ je $\vec{x}_i \notin \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{i-1}\}$** (obrácení [[alternativní definice lineární závislosti]]).

> [!karta|03]- Kdy se obal nezmění, když z $\vec{x}_1, \dots, \vec{x}_n$ odebereš $\vec{x}_n$?
> Právě když $\vec{x}_n \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_{n-1}\}$, tedy když je odebraný vektor **kombinací ostatních**.

> [!karta|05]- Jak dokážeš, že u LN posloupnosti je vyjádření vektoru jednoznačné?
> Ze dvou vyjádření $\sum \alpha_i\vec{x}_i = \sum \beta_i\vec{x}_i$ odečtením $\sum(\alpha_i - \beta_i)\vec{x}_i = \vec{0}$. Z **LN** jsou všechna $\alpha_i - \beta_i = 0$, tedy $\alpha_i = \beta_i$.

> [!karta|06]- Proč LN posloupnost sama nezaručí, že jde vektor vyjádřit?
> LN dává jen **nejvýše jedno** vyjádření; existenci zaručí až **generování**. Např. $((1; 0))$ je LN, ale $(0; 1)$ z ní nesložíš.

> [!karta|26]- Co znamená, že je báze „minimální vzhledem k inkluzi“, a proč to ještě neznamená „nejkratší“?
> Nejde z ní nic **vyhodit** (žádná vlastní podposloupnost negeneruje). Bez [[věta o počtu prvků báze|věty o počtu prvků báze]] by mohly existovat dvě báze různé délky, protože kratší nemusí být **podposloupností** delší.

> [!karta|08]- Jak dokážeš, že báze je maximální LN posloupnost?
> Báze je LN a pro každé $\vec{v} \in L$ je $\vec{v} \in \operatorname{span} = L$, takže $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ je podle [[věta o přidání vektoru k LN posloupnosti|věty o přidání vektoru k LN posloupnosti]] LZ.

> [!karta|09]- Jak dokážeš, že maximální LN posloupnost generuje $L$?
> Pro libovolné $\vec{v} \in L$ je $(\vec{x}_1, \dots, \vec{x}_n, \vec{v})$ LZ, takže podle [[věta o přidání vektoru k LN posloupnosti|věty o přidání vektoru k LN posloupnosti]] je $\vec{v} \in \operatorname{span}\{\vec{x}_1, \dots, \vec{x}_n\}$.

> [!karta|11]- Proč mají všechny báze prostoru stejně prvků?
> Pro báze s $k$ a $l$ prvky: první je LN a druhá generuje, takže $k \le l$ ([[Steinitzova věta]]); po prohození rolí $l \le k$. Tedy $k = l$.

> [!karta|12]- Proč $\dim\mathbb{F}[x] = \infty$?
> $(1, x, \dots, x^m)$ je LN pro každé $m$. Kdyby existovala báze s $m$ prvky, [[Steinitzova věta]] by dala **$m + 1 \le m$**, spor.

> [!karta|13]- Jak dokážeš, že z konečné množiny generátorů prostoru jde vybrat bázi?
> Dokud je v $G$ vektor, který je kombinací ostatních, **vyhodíme ho** (zbytek pořád generuje). $G$ je konečná, takže skončíme u LN generující množiny, tedy báze.

> [!karta|15]- Jak se LN posloupnost doplní na bázi a proč doplňování skončí?
> Dokud negeneruje, přidej $\vec{v} \notin \operatorname{span}$; podle [[věta o přidání vektoru k LN posloupnosti|věty o přidání vektoru k LN posloupnosti]] zůstane LN. LN posloupnost má nejvýš $n = \dim L$ prvků ([[Steinitzova věta]]), takže to skončí u báze.

> [!karta|16]- Co plyne pro posloupnost přesně $n = \dim L$ vektorů?
> Je **báze $\iff$ je LN $\iff$ generuje $L$**. Stačí ověřit jednu polovinu definice báze.

> [!karta|25]- Proč se u posloupnosti $n = \dim L$ vektorů ověřuje LN, a ne generování?
> Podle důsledku stačí jedno. LN = vyřešit **jednu homogenní soustavu**, generování = soustavu pro **každou** pravou stranu.

> [!karta|18]- Proč je ve větě $V = L \iff \dim V = \dim L$ potřeba předpoklad $\dim L < \infty$?
> Protipříklad: $V = \operatorname{span}\{x, x^2, \dots\} \le \mathbb{F}[x]$ má **$\dim V = \infty = \dim\mathbb{F}[x]$**, ale $1 \notin V$, takže $V \neq \mathbb{F}[x]$.

### Příklady na procvičení

> [!priklad|19]- Najdi bázi a dimenzi $V = \operatorname{span}\{(1; 1; 0), (0; 1; 1), (1; 2; 1)\}$.
> $(1; 2; 1) = (1; 1; 0) + (0; 1; 1)$, takže ho vyhodíme. $((1; 1; 0), (0; 1; 1))$ je LN, tedy **báze $V$ a $\dim V = 2$** (rovina).

> [!priklad|20]- Je $((1; 0), (1; 1))$ báze $\mathbb{R}^2$? Vyjádři v ní $(3; 2)$.
> **Ano**: 2 vektory, LN (nejsou násobky), a $\dim\mathbb{R}^2 = 2$, takže podle důsledku je to báze. $(3; 2) = \alpha(1; 0) + \beta(1; 1)$ dává $\beta = 2$, $\alpha = 1$: **$(3; 2) = 1 \cdot (1; 0) + 2 \cdot (1; 1)$**.

> [!priklad|21]- Je $((1; 0), (0; 1), (1; 1))$ báze $\mathbb{R}^2$?
> **Ne.** Generuje, ale je LZ: $(1; 1) = (1; 0) + (0; 1)$. Tři vektory v prostoru dimenze 2 nemůžou být LN ([[Steinitzova věta]]).

> [!priklad|22]- Kolik je $\dim\mathbb{R}^{\le 3}[x]$? Uveď bázi.
> **4**, báze $(1, x, x^2, x^3)$. Pozor na konstantu: stupeň $\le n$ dává $n + 1$.

> [!priklad|23]- Doplň LN posloupnost $((1; 1; 0))$ na bázi $\mathbb{R}^3$.
> Např. přidej $\vec{e}_1 = (1; 0; 0) \notin \operatorname{span}\{(1; 1; 0)\}$ a pak $\vec{e}_3 = (0; 0; 1)$, které neleží v rovině $z = 0$. **$((1; 1; 0), (1; 0; 0), (0; 0; 1))$** je LN se 3 prvky, tedy báze.

> [!priklad|24]- Jaké jsou $\dim\{\vec{0}\}$ a $\dim\operatorname{span}\{(2; 4), (1; 2)\}$?
> $\dim\{\vec{0}\} = $ **0** (báze je $()$). $(2; 4) = 2(1; 2)$, takže obal je přímka s bází $((1; 2))$ a dimenze je **1**.

### Typové příklady na zápočtový test

*Stejný typ úloh jako v ukázce k 1. zápočtovému testu (cvičení J. Rondoš). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|27]- Dokaž, že $\mathcal{C} = (1 + x,\ x + x^2,\ 1 + x^2)$ je báze $\mathbb{R}^{\le 2}[x]$ (lze využít $\dim \mathbb{R}^{\le 2}[x] = 3$).
> Protože $\dim \mathbb{R}^{\le 2}[x] = 3$ a vektory jsou **3**, stačí ověřit **LN**. Z $\alpha(1 + x) + \beta(x + x^2) + \gamma(1 + x^2) = 0$ porovnáním koeficientů:
> - u $1$: $\alpha + \gamma = 0$
> - u $x$: $\alpha + \beta = 0$
> - u $x^2$: $\beta + \gamma = 0$
>
> Sečtením $2(\alpha + \beta + \gamma) = 0$, tedy $\alpha + \beta + \gamma = 0$, a odečtením jednotlivých rovnic $\beta = \gamma = \alpha = 0$. Posloupnost je LN, a proto **je to báze**.

> [!priklad|28]- Je $\left(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}\right)$ báze $\mathbb{R}^{2 \times 2}$?
> $aM_1 + bM_2 + cM_3 + dM_4 = \begin{pmatrix} a + b & b + c \\ c + d & a + d \end{pmatrix} = \mathbf{0}$ dává $a = -b$, $c = -b$, $d = -c = b$ a poslední rovnice $a + d = -b + b = 0$ platí vždy. Pro $b = 1$: $-M_1 + M_2 - M_3 + M_4 = \mathbf{0}$, netriviální kombinace. Posloupnost je **LZ**, takže **není báze** (4 vektory v prostoru dimenze 4 tvoří bázi, právě když jsou LN).

---
← [[LAG 04 – Lineární závislost a nezávislost|2. 10. 2026 Lineární závislost a nezávislost]] · [[LAG 06 – Souřadnice, součet a průnik podprostorů|9. 10. 2026 Souřadnice, součet a průnik podprostorů]] →

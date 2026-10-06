---
predmet: LAG
prednaska: 1
datum: 2026-09-23
zdroj: "V poznámkách oddíl 1.1 (1.1–1.9)"
tags: [prednaska, LAG]
---

# LAG 01 – Úvod do lineární algebry

*Přednáška 1 · středa 23. 9. 2026* · [[LAG – Lineární algebra|LAG]] · [Poznámky k přednáškám (PDF) ↗](https://math.fel.cvut.cz/cz/lide/gromadan/LA26/notes.pdf)

Témata: `číselné těleso` · `soustavy 2 × 2` · `axiomy` · `lineární prostor`

Úvod do celého předmětu: od jedné lineární rovnice přes soustavu dvou rovnic až k abstraktní definici [[lineární prostor|lineárního prostoru]]. V oficiálních poznámkách tomu odpovídá oddíl 1.1.

## §0 Přehled na jedné stránce

| pojem | jednou větou |
|---|---|
| [[lineární rovnice]] $ax = b$ | pro $a \neq 0$ právě jedno řešení $x = b/a$ |
| [[číselné těleso]] $\mathbb{F}$ | čísla, která jde sčítat, odčítat, násobit i dělit (ne nulou) bez vypadnutí ven; $\mathbb{Q} \subseteq \mathbb{F} \subseteq \mathbb{C}$ |
| soustava $2 \times 2$ | tři pohledy: průsečík přímek, [[lineární kombinace]] sloupců, matice jako zobrazení |
| [[lineární prostor]] | množina s $\oplus$ a $\odot$, která splňuje 8 [[axiomy lineárního prostoru|axiomů]] |
| věta 1.8 | nulový i opačný vektor jsou jediné, $\alpha \odot \vec{x} = \vec{0} \iff \alpha = 0$ nebo $\vec{x} = \vec{0}$, $-\vec{x} = (-1) \odot \vec{x}$ |

## §1 Lineární rovnice

> [!definice] Definice
> Nechť $a, b \in \mathbb{R}$. *Lineární rovnice* je úloha nalézt $x \in \mathbb{R}$ takové, že $ax = b$.

^def-rovnice

> [!veta] Věta
> ==Nechť $a, b \in \mathbb{R}$ a $a \neq 0$.== **Potom má rovnice $ax = b$ právě jedno řešení, a to $x = \frac{b}{a}$.**
>
> *==předpoklad== = co musí platit, aby věta fungovala · **tvrzení** = co věta slibuje*

> [!navic] Co když a = 0?
> Pak předpoklad neplatí a věta nic neříká. Rovnice má tvar $0 \cdot x = b$: pro $b \neq 0$ nemá žádné řešení, pro $b = 0$ je řešením každé $x \in \mathbb{R}$. Stejné tři možnosti (žádné, právě jedno, nekonečně mnoho řešení) uvidíš u soustav rovnic, kde je popisuje Frobeniova věta (kap. 8).

## §2 Číselné těleso

> [!definice] Definice · pozn. 1.1
> Podmnožina $\mathbb{F} \subseteq \mathbb{C}$ obsahující aspoň dva prvky se nazývá *číselné těleso*, jestliže platí:
>
> $$
> \begin{aligned}
> &1.\quad (\forall \alpha, \beta \in \mathbb{F})\,(\alpha + \beta \in \mathbb{F})\\
> &2.\quad (\forall \alpha \in \mathbb{F})\,(-\alpha \in \mathbb{F})\\
> &3.\quad (\forall \alpha, \beta \in \mathbb{F})\,(\alpha \beta \in \mathbb{F})\\
> &4.\quad (\forall \alpha \in \mathbb{F},\ \alpha \neq 0)\,\bigl(\tfrac{1}{\alpha} \in \mathbb{F}\bigr)
> \end{aligned}
> $$
>
> Komplexní čísla $\mathbb{C}$ jsou „univerzum“, ve kterém všechna číselná tělesa leží.

^def-teleso

> [!lidsky] Lidsky
> Těleso je „bezpečná zóna“ pro počítání. Vezmi z ní libovolná dvě čísla, sečti, odečti, vynásob nebo vyděl (ne nulou) a výsledek z ní nevypadne. $\mathbb{Z}$ touhle zkouškou neprojde: $1 : 2 = 0{,}5$ a jsi venku.
>
> Proč to potřebujeme: čísla z tělesa budou [[skalár|skaláry]], kterými se násobí vektory. Aby šly řešit rovnice, musí jít dělit. V $\mathbb{Z}$ nemá řešení ani obyčejná rovnice $2x = 1$.

**Příklady:** $\mathbb{Q}, \mathbb{R}, \mathbb{C}$ jsou číselná tělesa. $\mathbb{N}, \mathbb{N}_0, \mathbb{Z}$ nejsou: $\mathbb{N}$ a $\mathbb{N}_0$ nemají opačné prvky ($-1 \notin \mathbb{N}$), $\mathbb{Z}$ nemá inverzní prvky ($\tfrac{1}{2} \notin \mathbb{Z}$).

> [!veta] Co z definice plyne · pozn. 1.4
> - Každé číselné těleso obsahuje **nulu**: vezmu libovolné $x \in \mathbb{F}$, pak i $-x$ a jejich součet $x + (-x) = 0$.
> - Každé obsahuje **jedničku**: díky „aspoň dvěma prvkům“ existuje nenulové $x$, s ním i $x^{-1}$ a součin $x x^{-1} = 1$.
> - Každé obsahuje **celé $\mathbb{Q}$**: sčítáním jedniček dostanu kladná celá čísla, opačné prvky dají záporná a dělením zlomky. Platí tedy $\mathbb{Q} \subseteq \mathbb{F} \subseteq \mathbb{C}$ a $\mathbb{Q}$ je nejmenší číselné těleso.
>
> Pozn. 1.5: dál se píše jen „těleso“. Obecný pojem tělesa (nejen uvnitř $\mathbb{C}$) přijde později a všechno z přednášek bude platit i pro něj.

> [!tip] Je to číselné těleso?
> Nejdřív tipni, pak rozklikni.

> [!priklad|01]- Je ℕ = {1, 2, 3, …} číselné těleso?
> **Není.** Chybí opačné prvky: 1 ∈ ℕ, ale −1 ∉ ℕ (podmínka 2).

> [!priklad|02]- Je ℤ (celá čísla) číselné těleso?
> **Není.** Chybí inverze: 2 ∈ ℤ, ale 1/2 ∉ ℤ (podmínka 4).

> [!question]- ℚ (racionální čísla)
> **Je číselné těleso.** Je to dokonce nejmenší číselné těleso, každé jiné ho obsahuje.

> [!priklad|03]- Je {0} číselné těleso?
> **Není.** Definice vyžaduje aspoň dva prvky.

> [!priklad|04]- Je {0, 1} číselné těleso?
> **Není.** 1 + 1 = 2 ∉ {0, 1}. (S jiným sčítáním, kde 1 + 1 = 0, by to bylo obecné těleso ℤ₂, ale ne číselné.)

> [!question]- sudá celá čísla 2ℤ
> **Není číselné těleso.** Nejsou tam ani 1, ani inverze: 2 ∈ 2ℤ, ale 1/2 ∉ 2ℤ.

> [!priklad|05]- Jsou iracionální čísla ℝ ∖ ℚ číselné těleso?
> **Nejsou.** √2 + (−√2) = 0 a √2 · √2 = 2 jsou racionální, takže výsledek z množiny vypadne.

> [!priklad|06]- Je ℚ[√2] = {a + b√2 | a, b ∈ ℚ} číselné těleso?
> **Je.** Součty a součiny zůstanou tvaru a + b√2. Inverze: 1/(a + b√2) = (a − b√2)/(a² − 2b²), jmenovatel je nenulový, protože √2 je iracionální (cvičení 1.3).

> [!question]- ℂ (komplexní čísla)
> **Je číselné těleso.** Největší číselné těleso, podle definice všechna leží v ℂ.

## §3 Soustava lineárních rovnic ze tří pohledů

$$
\begin{aligned}
2x + y &= 5\\
x - y &= -2
\end{aligned}
$$

### Algebraicky a maticově

Sečtením obou rovnic zmizí $y$: $3x = 3$, tedy $x = 1$ a z první rovnice $y = 3$. Totéž v řeči *rozšířené matice* soustavy, tedy tabulky koeficientů s pravými stranami za svislou čarou:

$$
\left(\begin{array}{cc|c} 2 & 1 & 5\\ 1 & -1 & -2 \end{array}\right)
\sim
\left(\begin{array}{cc|c} 2 & 1 & 5\\ 3 & 0 & 3 \end{array}\right)
\qquad R_2 \to R_2 + R_1
$$

Druhý řádek říká $3x = 3$, první pak $2 \cdot 1 + y = 5$. Řešení je $x = 1,\ y = 3$.

### Řádkový pohled: průsečík přímek

Každá rovnice popisuje přímku v rovině: $y = 5 - 2x$ a $y = x + 2$. Řešení soustavy je jejich průsečík $[1; 3]$.

> [!obrazek] Dvě rovnice, dvě přímky
> ![[lag01-primky.png]]
> *Modrá: 2x + y = 5, oranžová: x − y = −2. Průsečík [1; 3] je řešení soustavy.*

### Sloupcový pohled: lineární kombinace

Stejnou soustavu lze zapsat vektorově:

$$
x \begin{pmatrix} 2 \\ 1 \end{pmatrix} + y \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}
$$

Hledáme, kolikrát vzít první a kolikrát druhý sloupec, aby se složily na pravou stranu. Takovému součtu se říká *lineární kombinace* a je to nejdůležitější pojem celého předmětu (definice 2.8).

> [!lidsky] Lidsky
> Máš dvě ingredience: sloupec $(2; 1)$ a sloupec $(1; -1)$. Úkol zní: kolik dávek které ingredience smíchat, aby vyšel cíl $(5; -2)$? Odpověď je 1 dávka první a 3 dávky druhé. Stejně se v poznámkách (příklad 2.9) počítají náklady cukrárny: množství surovin krát jejich ceny, všechno sečteno.

> [!obrazek] Slož pravou stranu ze sloupců
> ![[lag01-sloupce.png]]
> *Modrá: 1 · (2; 1), oranžová: 3 · (1; −1), zelená čárkovaná: výsledek (5; −2). Zelená šikmá mřížka je nový souřadnicový systém, ve kterém má cíl souřadnice [1; 3].*

### Změna souřadnicového systému

Ve vektorovém zápisu se prostě $x$ nahradí vektorem $(2; 1)$ a $y$ vektorem $(1; -1)$. Tyto dva vektory vytvoří novou, šikmou mřížku. Řešení $(1; 3)$ jsou souřadnice bodu $(5; -2)$ právě v této nové mřížce. Na obrázku výše je nová mřížka zelená a bod b v ní leží na jejím průsečíku 1 krok v prvním a 3 kroky ve druhém směru.

> [!lidsky] Lidsky
> Souřadnice jsou jen návod „kolik kroků kterým směrem“. V běžné mřížce zní návod k bodu b: 5 kroků doprava, 2 dolů. V šikmé mřížce jsou kroky jiné, takže i návod je jiný: 1 krok po $(2; 1)$ a 3 kroky po $(1; -1)$. Bod je pořád tentýž, změnil se jen popis cesty.

> [!navic] Kam to vede
> Tohle je náhled na *souřadnice vektoru v bázi* (kap. 4.2). Dvojice $\bigl((2; 1), (1; -1)\bigr)$ je báze roviny a $[1; 3]$ jsou souřadnice vektoru $(5; -2)$ v ní.

### Matice jako transformace

Matice $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ zkosí čtvercovou síť: čtvereček se změní na rovnoběžník.

> [!navic] Jak to přečíst z matice
> Sloupce matice říkají, kam se zobrazí jednotkové vektory $\mathbf{e}_1 = (1; 0)$ a $\mathbf{e}_2 = (0; 1)$. Matice soustavy $\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$ pošle $\mathbf{e}_1$ na $(2; 1)$ a $\mathbf{e}_2$ na $(1; -1)$. Vyřešit soustavu tedy znamená najít vektor, který tato matice zobrazí na $(5; -2)$. Průsečík přímek, [[lineární kombinace]] i hledání vzoru jsou tři pohledy na tutéž úlohu (tabulka 7.3 v poznámkách).

> [!obrazek] Co matice udělá se sítí
> ![[lag01-zkoseni.png]]
> *Matice (1 1; 0 1): modrá šipka je obraz e₁ = (1; 0), oranžová obraz e₂ = (1; 1). Čtvereček se zkosí na rovnoběžník se stejným obsahem.*

## §4 Co je vektor

- **Fyzikální vektor:** velikost + směr, kreslí se jako šipka.
- **Vektor v analytické geometrii:** uspořádaná dvojice (trojice…) čísel, např. $(3; 1)$.

Oba druhy se chovají stejně při operacích: dají se sčítat a násobit číslem a platí pro to stejná pravidla. Lineární algebra proto neřeší, co vektor „je“, ale jen jak se s ním počítá. Tato pravidla shrnuje [[axiomy lineárního prostoru|osm axiomů]].

## §5 Lineární prostor

> [!definice] Definice · pozn. 1.6
> Buď $\mathbb{F}$ [[číselné těleso|těleso]]. *Lineární (vektorový) prostor* nad $\mathbb{F}$ je čtveřice $(L, \mathbb{F}, \oplus, \odot)$, kde $L$ je neprázdná množina a
>
> $$
> \oplus : L \times L \to L, \qquad \odot : \mathbb{F} \times L \to L
> $$
>
> jsou operace splňující osm axiomů níže. Prvkům $L$ říkáme *vektory*, prvkům $\mathbb{F}$ *skaláry*.

^def-lp

> [!lidsky] Lidsky
> Lineární prostor je jakákoli sbírka věcí, se kterými umíš dvě operace: sečíst dvě z nich a vynásobit jednu číslem. Výsledek musí zůstat ve sbírce a musí platit obvyklá pravidla počítání (8 axiomů níže). Co ty věci jsou, jestli šipky, tabulky čísel, polynomy nebo funkce, je úplně jedno.
>
> Zápis $\odot : \mathbb{F} \times L \to L$ čti jako „vezmi číslo a vektor, dostaneš vektor“. Podobně $\oplus : L \times L \to L$ je „vezmi dva vektory, dostaneš vektor“.
>
> Proč tak abstraktně: co dokážeš jednou pro obecný lineární prostor, platí automaticky pro všechny příklady najednou. Jedna věta místo stovky.

| č. | axiom | lidsky | název |
|---|---|---|---|
|  | **sčítání vektorů** |  |  |
| 1 | $\vec{x} \oplus \vec{y} = \vec{y} \oplus \vec{x}$ | Nezáleží na pořadí sčítání. | komutativita |
| 2 | $(\vec{x} \oplus \vec{y}) \oplus \vec{z} = \vec{x} \oplus (\vec{y} \oplus \vec{z})$ | Nezáleží na závorkách, takže je můžeš vynechat. | asociativita |
| 3 | existuje $\vec{0} \in L$ tak, že $\vec{x} \oplus \vec{0} = \vec{x}$ pro každé $\vec{x}$ | Existuje „nula“, jejíž přičtení nic nezmění. | nulový vektor |
| 4 | ke každému $\vec{x}$ existuje $-\vec{x} \in L$ tak, že $\vec{x} \oplus (-\vec{x}) = \vec{0}$ | Každé přičtení jde vrátit zpět. | opačný vektor |
|  | **násobení skalárem** |  |  |
| 5 | $\alpha \odot (\beta \odot \vec{x}) = (\alpha \beta) \odot \vec{x}$ | Natáhnout 3× a pak 2× je totéž jako rovnou 6×. | asociativita násobení |
| 6 | $1 \odot \vec{x} = \vec{x}$ | Násobení jedničkou nic nezmění. | jednička je neutrální |
|  | **propojení obou operací** |  |  |
| 7 | $(\alpha + \beta) \odot \vec{x} = (\alpha \odot \vec{x}) \oplus (\beta \odot \vec{x})$ | 2 jablka + 3 jablka = 5 jablek. | distributivita (skaláry) |
| 8 | $\alpha \odot (\vec{x} \oplus \vec{y}) = (\alpha \odot \vec{x}) \oplus (\alpha \odot \vec{y})$ | Zvětšit součet je totéž jako sečíst zvětšené. | distributivita (vektory) |

^axiomy

> [!pozor] Axiomy 3 a 4 jsou o existenci
> Nestačí je psát jako rovnosti $\vec{x} + \vec{0} = \vec{x}$ a $\vec{x} + (-\vec{x}) = \vec{0}$. V definici jde o to, že takový vektor *existuje*. Že je [[nulový vektor|nulový]] a [[opačný vektor]] jen jeden, axiomy neříkají, to se musí dokázat (věta 1.8 níže). Právě tento typ jemnosti se hodí u zkouškové části B.

> [!pozor] Dvě věci, které se pletou
> - Lineární prostor nemá násobení dvou vektorů. Jediné násobení je $\odot$: skalár krát vektor.
> - Kroužky $\oplus, \odot$ připomínají, že nejde o obyčejné sčítání a násobení čísel. S čísly mají společnou jen značku a osm axiomů (pozn. 1.9). Od kapitoly 2 se píše jen $+$ a $\cdot$.

> [!veta] Věta 1.8 · vlastnosti lineárních prostorů
> Buď $L$ lineární prostor nad $\mathbb{F}$. Potom:
>
> 1. V $L$ existuje právě jeden nulový vektor.
> 2. Ke každému $\vec{x}$ existuje právě jeden opačný vektor.
> 3. $\alpha \odot \vec{x} = \vec{0}$ platí právě tehdy, když $\alpha = 0$ nebo $\vec{x} = \vec{0}$.
> 4. $-\vec{x} = (-1) \odot \vec{x}$.
>
> > [!note]- Důkaz bodů 1 a 4 (ukázka, jak takový důkaz vypadá)
> > **1.** Nechť $\vec{o}_1$ i $\vec{o}_2$ splňují axiom 3. Pak $\vec{o}_1 = \vec{o}_1 \oplus \vec{o}_2 = \vec{o}_2 \oplus \vec{o}_1 = \vec{o}_2$. První rovnost používá, že $\vec{o}_2$ je nulový, druhá komutativitu, třetí že $\vec{o}_1$ je nulový.
> >
> > **4.** Stačí ověřit, že $(-1) \odot \vec{x}$ splňuje axiom 4: $\vec{x} \oplus ((-1) \odot \vec{x}) = (1 \odot \vec{x}) \oplus ((-1) \odot \vec{x}) = (1 - 1) \odot \vec{x} = 0 \odot \vec{x} = \vec{0}$. Použité axiomy: 6, 7 a bod 3 věty.

^veta-18

> [!lidsky] Lidsky
> Nula i „opak“ jsou v každém prostoru jen jedny a vynásobit cokoliv nulou dá vždy nulový vektor. Zní to samozřejmě, ale z axiomů to přímo nevyplývá, a proto se to dokazuje. Matematika si tu nic „nemyslí“, věří jen tomu, co z pravidel opravdu plyne.

> [!navic] Ke zkoušce · úvod poznámek
> Oddíl 1.1 je v poznámkách označen hvězdičkou **\***, tedy není nutný ke zkouškové písemce. Definice, které musíš umět sám zformulovat (část B1), jsou označené srdíčkem **♥** a první z nich je lineární podprostor v kapitole 2. Důkazy se nazpaměť učit nemusíš, ale pomáhají pochopit, proč věci platí.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|07]- Proč každé číselné těleso obsahuje 0 a 1?
> $0 = x + (-x)$ pro libovolné $x \in \mathbb{F}$. $1 = x \cdot x^{-1}$ pro nenulové $x$, které existuje díky podmínce „aspoň dva prvky“.

> [!karta|08]- Které číselné těleso je nejmenší a proč ho obsahuje každé jiné?
> $\mathbb{Q}$. Každé těleso obsahuje $1$; sčítáním jedniček dostaneš kladná celá čísla, opačnými prvky záporná a dělením všechny zlomky. Proto $\mathbb{Q} \subseteq \mathbb{F} \subseteq \mathbb{C}$.

> [!karta|09]- Kolik řešení má rovnice $ax = b$, když $a = 0$?
> Pro $b \neq 0$ žádné, pro $b = 0$ nekonečně mnoho (každé $x$). Věta o jediném řešení $x = \frac{b}{a}$ předpokládá $a \neq 0$.

> [!karta|10]- Jaké tři pohledy na soustavu dvou rovnic o dvou neznámých znáš?
> 1. **Řádky:** průsečík dvou přímek.
> 2. **Sloupce:** složit pravou stranu jako lineární kombinaci sloupců.
> 3. **Transformace:** najít vektor, který matice soustavy zobrazí na pravou stranu.

> [!karta|12]- Kam matice zobrazí $\mathbf{e}_1$ a $\mathbf{e}_2$ a jak to z ní přečteš?
> Na své sloupce: první sloupec je obraz $\mathbf{e}_1 = (1; 0)$, druhý sloupec obraz $\mathbf{e}_2 = (0; 1)$.

> [!karta|14]- Axiomy lineárního prostoru 1–4: co říkají o sčítání vektorů?
> 1. komutativita: $\vec{x} \oplus \vec{y} = \vec{y} \oplus \vec{x}$
> 2. asociativita: $(\vec{x} \oplus \vec{y}) \oplus \vec{z} = \vec{x} \oplus (\vec{y} \oplus \vec{z})$
> 3. **existuje** nulový vektor $\vec{0}$: $\vec{x} \oplus \vec{0} = \vec{x}$
> 4. ke každému $\vec{x}$ **existuje** opačný $-\vec{x}$: $\vec{x} \oplus (-\vec{x}) = \vec{0}$

> [!karta|15]- Axiomy lineárního prostoru 5–8: co říkají o násobení skalárem?
> 5. $\alpha \odot (\beta \odot \vec{x}) = (\alpha \beta) \odot \vec{x}$
> 6. $1 \odot \vec{x} = \vec{x}$
> 7. $(\alpha + \beta) \odot \vec{x} = (\alpha \odot \vec{x}) \oplus (\beta \odot \vec{x})$
> 8. $\alpha \odot (\vec{x} \oplus \vec{y}) = (\alpha \odot \vec{x}) \oplus (\alpha \odot \vec{y})$

> [!karta|16]- Které axiomy lineárního prostoru jsou existenční a co z nich přímo neplyne?
> Axiomy 3 a 4. Neplyne z nich, že nulový a opačný vektor jsou **jediné**; to se dokazuje ve větě 1.8.

> [!karta|17]- Dokaž, že lineární prostor má jen jeden nulový vektor.
> Nechť $\vec{o}_1$ i $\vec{o}_2$ splňují axiom 3. Pak $\vec{o}_1 = \vec{o}_1 \oplus \vec{o}_2 = \vec{o}_2 \oplus \vec{o}_1 = \vec{o}_2$. Použito: nulovost $\vec{o}_2$, komutativita, nulovost $\vec{o}_1$.

> [!karta|18]- Kdy platí $\alpha \odot \vec{x} = \vec{0}$?
> Právě tehdy, když $\alpha = 0$ nebo $\vec{x} = \vec{0}$ (věta 1.8, bod 3).

> [!karta|19]- Jak vyjádříš opačný vektor $-\vec{x}$ pomocí násobení skalárem a proč to platí?
> $-\vec{x} = (-1) \odot \vec{x}$. Splňuje axiom 4: $\vec{x} \oplus ((-1) \odot \vec{x}) = (1 + (-1)) \odot \vec{x} = 0 \odot \vec{x} = \vec{0}$ (axiomy 6, 7 a bod 3 věty 1.8).

> [!karta|20]- Umí lineární prostor násobit dva vektory mezi sebou?
> Ne. Jediné násobení je $\odot$: skalár krát vektor.

### Příklady na procvičení

> [!priklad|11]- Zapiš soustavu $2x + y = 5$, $x - y = -2$ ve sloupcovém tvaru. Jaké je řešení?
> $$
> x \begin{pmatrix} 2 \\ 1 \end{pmatrix} + y \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}
> $$
>
> Řešení $x = 1$, $y = 3$: jedna dávka prvního sloupce a tři dávky druhého.

> [!priklad|13]- Co udělá matice $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ se čtvercovou sítí?
> $\mathbf{e}_1 \mapsto (1; 0)$ zůstane, $\mathbf{e}_2 \mapsto (1; 1)$. Čtverec se zkosí na rovnoběžník se stejným obsahem.

---
[[LAG 02 – Příklady lineárních prostorů|25. 9. 2026 Příklady lineárních prostorů]] →

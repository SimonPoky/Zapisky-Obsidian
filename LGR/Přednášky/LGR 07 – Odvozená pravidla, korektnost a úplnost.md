---
predmet: LGR
prednaska: 7
datum: 2026-10-22
zdroj: "handout 4, slajdy 11–16; handout 4D"
tags: [prednaska, LGR]
---

# LGR 07 – Odvozená pravidla, korektnost a úplnost

*Přednáška 7 · čtvrtek 22. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 4 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_4.pdf) · [handout 4D ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_4D.pdf)

Témata: `odvozená pravidla` `¬¬i, MT, RAA, TND` `logická ekvivalence ⊣⊢` `věty o kompaktnosti` `syntaktická věta o dedukci` `slabá, silná a strukturální indukce` `věta o korektnosti` `věta o úplnosti` `literály řádku` `lemma o literálech řádku`

Minule se zavedla [[přirozená dedukce]] se základními pravidly. Dnes se z nich odvodí čtyři zkratky (¬¬i, MT, RAA, TND), které dokazování hodně zkrátí, a s jejich pomocí se dokončí ekvivalence $a \Rightarrow b \dashv\vdash \neg a \vee b$. Druhá polovina odpovídá na hlavní otázku kapitoly: přirozená dedukce je **korektní** (dokáže jen pravdu) a **úplná** (dokáže každou pravdu). Důkaz úplnosti se převede na tautologie a jejich odvození se poskládá z řádků pravdivostní tabulky.

## §0 Přehled na jedné stránce

| pojem | zápis | význam |
|---|---|---|
| ¬¬i | $\varphi \;/\; \neg\neg\varphi$ | dvojitou negaci smíš přidat |
| MT | $\varphi \Rightarrow \psi,\ \neg\psi \;/\; \neg\varphi$ | když neplatí důsledek, neplatí předpoklad |
| RAA | box $\neg\varphi \dots \bot \;/\; \varphi$ | důkaz sporem: z $\neg\varphi$ vyjde spor, tedy $\varphi$ |
| TND | $\;/\; \varphi \vee \neg\varphi$ | zákon vyloučeného třetího, platí bez předpokladů |
| logická ekvivalence | $\varphi \dashv\vdash \psi$ | $\varphi \vdash \psi$ a $\psi \vdash \varphi$ |
| syntaktická kompaktnost | $S \vdash \varphi \iff S' \vdash \varphi$ | stačí konečná $S' \subseteq S$ |
| syntaktická věta o dedukci | $S \cup \{\varphi\} \vdash \psi \iff S \vdash \varphi \Rightarrow \psi$ | předpoklad se přesune do implikace |
| věta o korektnosti | $S \vdash \varphi \Rightarrow S \models \varphi$ | co jde odvodit, je pravda |
| věta o úplnosti | $S \vdash \varphi \iff S \models \varphi$ | odvoditelné = pravdivé |
| slabá věta o úplnosti | $\vdash \varphi \iff \models \varphi$ | věty výrokové logiky jsou právě tautologie |
| literály řádku | $L_u = \{\tilde x_1, \dots, \tilde x_n\}$ | $x_i$, nebo $\neg x_i$ podle $u(x_i)$ |
| lemma o literálech řádku | $L_u \vdash \varphi$, nebo $L_u \vdash \neg\varphi$ | každý řádek tabulky jde odvodit |

## §1 Odvozená pravidla

### Základní pravidla pro ¬ a ∨

V odvozeních níž se pořád používají tři základní pravidla ze slajdů 7–8, která stojí za to mít před očima.

> [!definice] Definice · handout 4, slajdy 7–8
> - **zavedení disjunkce** ($\vee$i): z $\varphi$ odvoď $\varphi \vee \psi$ ($\vee$i₁), z $\psi$ odvoď $\varphi \vee \psi$ ($\vee$i₂);
> - **zavedení negace** ($\neg$i): když z pomocného předpokladu $\varphi$ (box) vyjde spor $\bot$, odvoď $\neg\varphi$;
> - **eliminace dvojité negace** ($\neg\neg$e): z $\neg\neg\varphi$ odvoď $\varphi$.

^def-zakladni-pravidla-negace

> [!lidsky] Lidsky
> $\vee$i: když víš, že prší, víš i „prší nebo sněží“. $\neg$i: „kdyby $\varphi$ platila, vyšel by nesmysl, takže $\varphi$ neplatí“. $\neg\neg$e: „není pravda, že neprší“ znamená „prší“.

### Co je odvozené pravidlo

> [!definice] Definice · handout 4, slajd 11
> **Odvozené pravidlo** je pravidlo, jehož závěr jde z jeho předpokladů odvodit jen základními pravidly přirozené dedukce. Smí se používat jako zkratka: každé jeho použití jde nahradit tím odvozením.

^def-odvozene-pravidlo

> [!lidsky] Lidsky
> Jako funkce v programu: jednou ji napíšeš ze základních příkazů a pak už ji jen voláš. Nové pravidlo nic nového nedokáže, jen šetří řádky. Proto systém zůstane [[korektní důkazový systém|korektní]].

### Zavedení dvojité negace (¬¬i)

> [!definice] Definice · handout 4, slajd 11
> $$
> \frac{\varphi}{\neg\neg\varphi}\ \neg\neg\text{i}
> $$

^def-zavedeni-dvojite-negace

> [!lidsky] Lidsky
> Když platí $\varphi$, nemůže platit $\neg\varphi$: to by byl spor. Tedy platí „ne-ne-$\varphi$“.

Odvození $\varphi \vdash \neg\neg\varphi$ jen ze základních pravidel: předpokládej opak $\neg\varphi$ a narazíš na spor s $\varphi$ ([[eliminace negace|¬e]]), takže [[zavedení negace|¬i]] dá $\neg\neg\varphi$.

$$
\begin{array}{rll}\text{1.} & \varphi & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & \neg\varphi & \text{P} \\ \text{3.} & \bot & {\neg}\text{e}\ 1, 2 \\ \hline\end{array} &  \\ \text{4.} & \neg\neg\varphi & {\neg}\text{i}\ 2\text{–}3\end{array}
$$

### Modus tollens (MT)

> [!definice] Definice · handout 4, slajd 11
> $$
> \frac{\varphi \Rightarrow \psi \qquad \neg\psi}{\neg\varphi}\ \text{MT}
> $$

^def-modus-tollens

> [!lidsky] Lidsky
> „Když prší, je mokro. Mokro není. Takže nepršelo.“ Je to [[modus ponens]] pozpátku přes [[obměněná implikace|obměnu]]: $\varphi \Rightarrow \psi$ je totéž co $\neg\psi \Rightarrow \neg\varphi$.

Odvození: předpokládej $\varphi$, modus ponens dá $\psi$ a to je spor s $\neg\psi$.

$$
\begin{array}{rll}\text{1.} & \varphi\Rightarrow\psi & \text{P} \\ \text{2.} & \neg\psi & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & \varphi & \text{P} \\ \text{4.} & \psi & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \bot & {\neg}\text{e}\ 4, 2 \\ \hline\end{array} &  \\ \text{6.} & \neg\varphi & {\neg}\text{i}\ 3\text{–}5\end{array}
$$

> [!pozor] Častá chyba: obrácený MT
> Z $\varphi \Rightarrow \psi$ a $\neg\varphi$ **neplyne** $\neg\psi$. Protipříklad: $u(\varphi) = 0$, $u(\psi) = 1$, předpoklady jsou pravdivé, závěr ne. Podle [[věta o korektnosti|věty o korektnosti]] takové pravidlo nejde odvodit.

### Reductio ad absurdum (RAA)

> [!definice] Definice · handout 4, slajd 11
> Když z pomocného předpokladu $\neg\varphi$ (box) vyjde spor $\bot$, odvoď $\varphi$.
> $$
> \frac{\boxed{\neg\varphi \ \cdots\ \bot}}{\varphi}\ \text{RAA}
> $$

^def-reductio-ad-absurdum

> [!lidsky] Lidsky
> Klasický důkaz sporem: „předpokládejme, že $\varphi$ neplatí… a to je spor, tedy $\varphi$ platí“. Tak se dokazuje třeba iracionalita $\sqrt 2$.

RAA je [[zavedení negace|¬i]] a hned za ním [[eliminace dvojité negace|¬¬e]]: box s $\neg\varphi$ končící sporem dá nejdřív $\neg\neg\varphi$, z toho $\varphi$.

$$
\begin{array}{rll} & \begin{array}{|rll|}\hline \text{1.} & \neg\varphi & \text{P} \\  & \vdots &  \\ \text{k.} & \bot &  \\ \hline\end{array} &  \\ \text{k{+}1.} & \neg\neg\varphi & {\neg}\text{i}\ 1\text{–}k \\ \text{k{+}2.} & \varphi & {\neg\neg}\text{e}\ k{+}1\end{array}
$$

> [!pozor] RAA není ¬i
> $\neg$i: box **$\varphi$** … $\bot$ dá **$\neg\varphi$**. RAA: box **$\neg\varphi$** … $\bot$ dá **$\varphi$**. Rozdíl je jen v tom, kde je negace, ale RAA potřebuje navíc $\neg\neg$e.

### Zákon vyloučeného třetího (TND)

> [!definice] Definice · handout 4, slajd 11
> **Tertium non datur** (zákon vyloučeného třetího): formuli $\varphi \vee \neg\varphi$ smíš napsat kdykoli, bez předpokladů.
> $$
> \frac{}{\varphi \vee \neg\varphi}\ \text{TND}
> $$

^def-tnd

> [!lidsky] Lidsky
> Každé tvrzení buď platí, nebo neplatí, třetí možnost není. Hodí se k rozboru případů: napíšeš $a \vee \neg a$ a pak [[eliminace disjunkce|∨e]] vyřeší zvlášť případ $a$ a případ $\neg a$.

Odvození $\vdash \varphi \vee \neg\varphi$ jde přes spor: předpokládej $\neg(\varphi \vee \neg\varphi)$. Z $\varphi$ by šlo $\vee$i₁ udělat $\varphi \vee \neg\varphi$, to je spor, takže $\neg\varphi$; z $\neg\varphi$ pak $\vee$i₂ dá znovu $\varphi \vee \neg\varphi$ a znovu spor.

$$
\begin{array}{rll} & \begin{array}{|rll|}\hline \text{1.} & \neg(\varphi\vee\neg\varphi) & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & \varphi & \text{P} \\ \text{3.} & \varphi\vee\neg\varphi & {\vee}\text{i}_1\ 2 \\ \text{4.} & \bot & {\neg}\text{e}\ 3, 1 \\ \hline\end{array} &  \\ \text{5.} & \neg\varphi & {\neg}\text{i}\ 2\text{–}4 \\ \text{6.} & \varphi\vee\neg\varphi & {\vee}\text{i}_2\ 5 \\ \text{7.} & \bot & {\neg}\text{e}\ 6, 1 \\ \hline\end{array} &  \\ \text{8.} & \neg\neg(\varphi\vee\neg\varphi) & {\neg}\text{i}\ 1\text{–}7 \\ \text{9.} & \varphi\vee\neg\varphi & {\neg\neg}\text{e}\ 8\end{array}
$$

> [!navic] Proč ne rovnou ∨i
> Přímo $\vee$i nejde: musel bys napřed dokázat $\varphi$ nebo $\neg\varphi$ samotnou. Pro proměnnou $a$ ale nejde ani $\vdash a$, ani $\vdash \neg a$ (ani jedna není [[tautologie]], a podle [[věta o korektnosti|věty o korektnosti]] by tautologií byla). Proto oklika přes $\neg\neg(\varphi \vee \neg\varphi)$ a $\neg\neg$e.

> [!navic] Klasická a neklasická logika
> Pravidla $\neg\neg$e, RAA a TND patří ke **klasické** logice. **Neklasické** logiky (třeba intuicionistická, kde se pravdivost bere jako „umím to dokázat“) je nepřijímají: že $\neg\varphi$ není pravda, ještě neznamená, že máš důkaz $\varphi$. Taková logika má víc možností než jen 1 a 0, a proto v ní TND neplatí.

## §2 Logická ekvivalence

> [!definice] Definice · handout 4, slajd 12
> Formule $\varphi$ a $\psi$ jsou **logicky ekvivalentní**, když $\varphi \vdash \psi$ a zároveň $\psi \vdash \varphi$. Značí se $\varphi \dashv\vdash \psi$.

^def-logicka-ekvivalence

> [!lidsky] Lidsky
> Syntaktické dvojče [[tautologická ekvivalence|tautologické ekvivalence]] $\mathrel{\vert\!=\!\vert}$: místo „mají stejnou tabulku“ říká „jedna jde odvodit z druhé a naopak“. Podle [[věta o úplnosti|věty o úplnosti]] jsou obě ekvivalence totéž.

### Příklad: $a \Rightarrow b \dashv\vdash \neg a \vee b$

Směr $\neg a \vee b \vdash a \Rightarrow b$ je v [[LGR 06 – Rezoluční tabulka a přirozená dedukce|LGR 06]]. Opačný směr $a \Rightarrow b \vdash \neg a \vee b$ potřebuje TND: rozbor případů $a$ / $\neg a$.

$$
\begin{array}{rll}\text{1.} & a\Rightarrow b & \text{P} \\ \text{2.} & a\vee\neg a & \text{TND} \\  & \begin{array}{|rll|}\hline \text{3.} & a & \text{P} \\ \text{4.} & b & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \neg a\vee b & {\vee}\text{i}_2\ 4 \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{6.} & \neg a & \text{P} \\ \text{7.} & \neg a\vee b & {\vee}\text{i}_1\ 6 \\ \hline\end{array} &  \\ \text{8.} & \neg a\vee b & {\vee}\text{e}\ 2, 3\text{–}5, 6\text{–}7\end{array}
$$

V boxu $a$ dá [[modus ponens]] $b$ a z něj $\vee$i₂ cíl; v boxu $\neg a$ stačí $\vee$i₁. [[Eliminace disjunkce|∨e]] uzavře oba boxy.

### Příklad: $\neg b \Rightarrow \neg a \vdash a \Rightarrow b$

Obměnu implikace jde vrátit zpět pomocí RAA: v boxu $a$ předpokládej $\neg b$, dostaneš $\neg a$ a spor.

$$
\begin{array}{rll}\text{1.} & \neg b\Rightarrow\neg a & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & a & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & \neg b & \text{P} \\ \text{4.} & \neg a & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \bot & {\neg}\text{e}\ 2, 4 \\ \hline\end{array} &  \\ \text{6.} & b & \text{RAA}\ 3\text{–}5 \\ \hline\end{array} &  \\ \text{7.} & a\Rightarrow b & {\Rightarrow}\text{i}\ 2\text{–}6\end{array}
$$

## §3 Věty o kompaktnosti a o dedukci

> [!veta] Věta (syntaktická o kompaktnosti) · handout 4, slajd 13
> Pro ==libovolnou množinu formulí $S$ a formuli $\varphi$== platí: **$S \vdash \varphi$, právě když existuje konečná $S' \subseteq S$ taková, že $S' \vdash \varphi$.**

^veta-synt-kompaktnost

> [!lidsky] Lidsky
> Důkaz je konečný text, takže použije jen konečně mnoho předpokladů. Ty tvoří $S'$. Opačný směr: co jde dokázat z menší množiny, jde dokázat i z větší.

> [!veta] Věta (sémantická o kompaktnosti) · handout 4D, slajd 9
> Pro ==libovolnou množinu formulí $S$ a formuli $\varphi$== platí: **$S \models \varphi$, právě když existuje konečná $S' \subseteq S$ taková, že $S' \models \varphi$.** Ekvivalentně: $S$ je nesplnitelná, právě když je nesplnitelná některá její konečná podmnožina.

^veta-sem-kompaktnost

> [!lidsky] Lidsky
> Totéž pro pravdivost, ale tady to zadarmo není: $\models$ mluví o všech ohodnoceních nekonečně mnoha proměnných, žádný konečný důkaz v pozadí není. Je to nejtěžší část důkazu [[věta o úplnosti|věty o úplnosti]]; důkaz se zde neuvádí.

> [!veta] Věta (syntaktická o dedukci) · handout 4, slajd 13
> Pro ==libovolnou množinu formulí $S$ a formule $\varphi$, $\psi$== platí: **$S \cup \{\varphi\} \vdash \psi$, právě když $S \vdash \varphi \Rightarrow \psi$.**
>
> > [!note]- Důkaz
> > **„⇒“:** máme odvození $\psi$ z $S \cup \{\varphi\}$. Předpoklady z $S$ (zde $\alpha$, $\beta$) dáme nahoru, předpoklad $\varphi$ změníme na pomocný předpoklad, který otevře box až do konce odvození, a box uzavřeme pravidlem $\Rightarrow$i.
> >
> > $$
> > \begin{array}{rll}\text{1.} & \alpha & \text{P} \\ \text{2.} & \beta & \text{P} \\  & \vdots &  \\ \text{k.} & \varphi & \text{P} \\  & \vdots &  \\ \text{n.} & \psi & \end{array}
> > $$
> > $\leadsto$
> > $$
> > \begin{array}{rll}\text{1.} & \alpha & \text{P} \\ \text{2.} & \beta & \text{P} \\  & \vdots &  \\  & \begin{array}{|rll|}\hline \text{k.} & \varphi & \text{P} \\  & \vdots &  \\ \text{n.} & \psi &  \\ \hline\end{array} &  \\ \text{n{+}1.} & \varphi\Rightarrow\psi & {\Rightarrow}\text{i}\ k\text{–}n\end{array}
> > $$
> >
> > **„⇐“:** k odvození $\varphi \Rightarrow \psi$ z $S$ připíšeme předpoklad $\varphi$ (teď je v $S \cup \{\varphi\}$) a modus ponens.
> >
> > $$
> > \begin{array}{rll}\text{1.} & \alpha & \text{P} \\  & \vdots &  \\ \text{m.} & \varphi\Rightarrow\psi &  \\ \text{m{+}1.} & \varphi & \text{P} \\ \text{m{+}2.} & \psi & {\Rightarrow}\text{e}\ m{+}1, m\end{array}
> > $$

^veta-synt-dedukce

> [!lidsky] Lidsky
> Je to přesně to, co děláš v matematice: „chci dokázat $\varphi \Rightarrow \psi$, tak předpokládám $\varphi$ a dokážu $\psi$“. Sémantická [[věta o dedukci]] říká totéž pro $\models$.

## §4 Matematická indukce

Důkazy korektnosti a úplnosti jsou indukcí, ale ne vždy tou ze střední školy. Tři varianty:

> [!veta] Princip slabé indukce · handout 4D, slajd 4
> Nechť $V$ je vlastnost přirozených čísel $n \ge n_0$. ==Když (1) $n_0$ má $V$ a (2) pro každé $n \ge n_0$ z toho, že $n$ má $V$, plyne, že $n + 1$ má $V$,== pak **každé $n \ge n_0$ má $V$**.

^veta-slaba-indukce

> [!veta] Princip silné indukce · handout 4D, slajd 5
> Nechť $V$ je vlastnost přirozených čísel $n \ge n_0$. ==Když (1) $n_0$ má $V$ a (2) pro každé $n \ge n_0$ z toho, že **všechna** $k$ s $n_0 \le k \le n$ mají $V$, plyne, že $n + 1$ má $V$,== pak **každé $n \ge n_0$ má $V$**.

^veta-silna-indukce

> [!lidsky] Lidsky
> Slabá indukce jsou domino kostky: každá shodí tu další. Silná indukce smí v kroku použít **všechny** předchozí kostky, nejen tu poslední. To se hodí, když $n + 1$ nestojí na $n$, ale na nějakém dřívějším čísle, které předem neznáš.

> [!veta] Princip strukturální indukce · handout 4D, slajd 7
> Nechť $M$ je induktivně definovaná množina (např. formule) a $V$ vlastnost jejích prvků. ==Když (1) všechny prvky ze základních pravidel mají $V$ a (2) u každého tvořícího pravidla platí: mají-li $V$ jeho předpoklady, má $V$ i výsledek,== pak **každý prvek $M$ má $V$**.

^veta-strukturalni-indukce

> [!lidsky] Lidsky
> [[formule|Formule]] se staví z proměnných spojkami: když $\alpha$, $\beta$ jsou formule, jsou jimi i $\neg\alpha$, $(\alpha \wedge \beta)$, $(\alpha \vee \beta)$, …. Strukturální indukce ověří vlastnost pro proměnné (listy [[syntaktický strom|syntaktického stromu]]) a pak ukáže, že ji každá spojka zachová. Vlastnost se tak „prolije“ od listů ke kořeni.

> [!obrazek] Slabá, silná a strukturální indukce
> ![[lgr07-indukce.png]]
> *Zeleně základ, oranžově krok. Slabá: z $n$ na $n + 1$. Silná: ze všech $0, \dots, n$ na $n + 1$. Strukturální: v syntaktickém stromu formule od listů (proměnné) ke kořeni.*

> [!navic] Jsou to různé principy?
> Na přirozených číslech jsou slabá indukce, silná indukce a **princip dobrého uspořádání** (každá neprázdná podmnožina $\mathbb{N}$ má nejmenší prvek) navzájem ekvivalentní (handout 4D, slajd 6). Silná indukce tedy nedokáže víc, jen se pohodlněji používá.

## §5 Věta o korektnosti

> [!veta] Věta o korektnosti · handout 4, slajd 14
> Pro ==každou množinu formulí $S$ a formuli $\varphi$== platí: **když $S \vdash \varphi$, pak $S \models \varphi$.**
>
> > [!note]- Důkaz (myšlenka, handout 4D, slajd 10)
> > Silnou indukcí podle délky odvození $k \ge 1$ se dokáže vlastnost $V(k)$: „pro každé $S$ a $\varphi$, jejichž odvození z $S$ má délku $k$, platí $S \models \varphi$“.
> >
> > Poslední řádek $\varphi$ je buď předpoklad z $S$ (pak $S \models \varphi$ zjevně), nebo vznikl pravidlem z dřívějších řádků. Pro ty už vlastnost platí (jsou to kratší odvození), a stačí ověřit, že každé pravidlo **respektuje pravdivost**. Například $\vee$i: řádek $n + 1$ je $\alpha \vee \beta$ z řádku $k$ s formulí $\alpha$. Podle indukčního předpokladu $S \models \alpha$, a protože $\alpha \models \alpha \vee \beta$, je **$S \models \alpha \vee \beta$**.
> >
> > U pravidel s boxem ($\Rightarrow$i, $\neg$i, $\vee$e) se indukční předpoklad použije na $S$ rozšířenou o pomocný předpoklad boxu a pak [[věta o dedukci|sémantická věta o dedukci]], jako u $\Rightarrow$i v [[LGR 06 – Rezoluční tabulka a přirozená dedukce|LGR 06]].

^veta-korektnost

> [!lidsky] Lidsky
> Přirozená dedukce nikdy „nedokáže“ nepravdu: každé pravidlo z pravdivých předpokladů vyrobí pravdivý závěr, takže pravdivost se nese celým důkazem.

> [!navic] Proč silná indukce
> Pravidlo na řádku $n + 1$ může brát předpoklady z **libovolných** dřívějších řádků (řádek $k$ výš), ne jen z řádku $n$. Indukční předpoklad proto musí platit pro všechna kratší odvození, a to je silná indukce.

## §6 Věta o úplnosti

> [!veta] Věta o úplnosti · handout 4, slajd 14
> Pro ==každou množinu formulí $S$ a formuli $\varphi$== platí: **$S \vdash \varphi$, právě když $S \models \varphi$.**
>
> > [!note]- Důkaz (myšlenka, handout 4D, slajd 11)
> > „⇒“ je [[věta o korektnosti]]. „⇐“: je-li $S \models \varphi$, dá [[sémantická věta o kompaktnosti]] konečnou $S' = \{\alpha, \beta\} \subseteq S$ s $S' \models \varphi$. Sémantická [[věta o dedukci]] (dvakrát) z toho udělá $\models \alpha \Rightarrow (\beta \Rightarrow \varphi)$, tedy tautologii. [[slabá věta o úplnosti|Slabá věta o úplnosti]] dá $\vdash \alpha \Rightarrow (\beta \Rightarrow \varphi)$, [[syntaktická věta o dedukci]] (dvakrát) $\{\alpha, \beta\} \vdash \varphi$ a [[syntaktická věta o kompaktnosti|syntaktická kompaktnost]] $S \vdash \varphi$.

^veta-uplnost

> [!lidsky] Lidsky
> Přirozená dedukce je [[úplný důkazový systém]]: dokáže přesně ty formule, které z $S$ pravdivostně plynou, ani víc, ani míň. „Pravda“ a „dokazatelné“ tu splývají.

> [!obrazek] Řetěz důkazu věty o úplnosti
> ![[lgr07-retez-uplnosti.png]]
> *Vlevo modře sémantika ($\models$), vpravo oranžově syntax ($\vdash$). Červeně dokazovaná věta, zeleně slabá věta o úplnosti, přes kterou se celý důkaz převede na tautologie.*

> [!definice] Definice · handout 4, slajd 15
> Formule $\varphi$, pro kterou platí $\vdash \varphi$, se nazývá **věta výrokové logiky**.

^def-veta-vyrokove-logiky

> [!lidsky] Lidsky
> Věta výrokové logiky je formule dokazatelná úplně bez předpokladů, třeba $\varphi \vee \neg\varphi$ nebo $a \Rightarrow (b \Rightarrow a)$.

> [!veta] Slabá věta o úplnosti · handout 4, slajd 15
> Větami výrokové logiky jsou právě tautologie: pro ==každou formuli $\varphi$== platí **$\vdash \varphi$, právě když $\models \varphi$.**

^veta-slaba-uplnost

> [!lidsky] Lidsky
> Je to věta o úplnosti pro $S = \emptyset$. Směr „⇒“ je korektnost, směr „⇐“ se dokazuje v §7.

> [!navic] Dvě úlohy, které se doplňují
> Podle věty o úplnosti je $S \vdash \varphi$ totéž co $S \models \varphi$ a $S \nvdash \varphi$ totéž co $S \not\models \varphi$. Vždy je jedna strana lehčí, když najdeš svědka:
> - pro $S \vdash \varphi$ stačí **jedno odvození**, kdežto $S \models \varphi$ chce tabulku o $2^n$ řádcích;
> - pro $S \not\models \varphi$ stačí **jedno ohodnocení** $u$ s $u(S) = 1$ a $u(\varphi) = 0$, kdežto $S \nvdash \varphi$ by znamenalo ukázat, že žádné odvození neexistuje.

## §7 Důkaz slabé věty o úplnosti

Úkol: je-li $\varphi$ [[tautologie]], najít její odvození bez předpokladů. Víme jen, že v tabulce má $\varphi$ ve všech řádcích 1. Plán: každý řádek tabulky se převede na odvození a ta se pak slepí přes TND.

### Literály řádku

> [!definice] Definice · handout 4D, slajd 13
> Nechť $x_1, \dots, x_n$ jsou všechny proměnné formule $\varphi$ a $u$ je [[pravdivostní ohodnocení]]. Pro každou proměnnou označ [[literál]]
> $$
> \tilde x_i = x_i \ \text{ pro } u(x_i) = 1, \qquad \tilde x_i = \neg x_i \ \text{ pro } u(x_i) = 0.
> $$
> **Literály řádku** $u$ jsou $L_u = \{\tilde x_1, \dots, \tilde x_n\}$.

^def-literaly-radku

> [!lidsky] Lidsky
> $L_u$ je řádek tabulky zapsaný jako formule: pro $u$: $x \mapsto 1$, $y \mapsto 0$, $z \mapsto 0$ je $L_u = \{x, \neg y, \neg z\}$. Množina $L_u$ je pravdivá **jen** v ohodnocení $u$, stejně jako [[minterm]] $x \wedge \neg y \wedge \neg z$.

### Lemma o literálech řádku

> [!veta] Lemma · handout 4D, slajd 13
> Nechť ==$\varphi$ je libovolná formule, $u$ libovolné ohodnocení a $L_u$ literály řádku $u$==. Pak **je-li $u(\varphi) = 1$, platí $L_u \vdash \varphi$; je-li $u(\varphi) = 0$, platí $L_u \vdash \neg\varphi$.**
>
> > [!note]- Důkaz strukturální indukcí podle $\varphi$
> > Sémanticky je to jasné: $L_u$ je pravdivá jen v $u$, takže $L_u \models \varphi$, nebo $L_u \models \neg\varphi$. Lemma tvrdí totéž pro $\vdash$, a to se musí odvodit.
> >
> > **1) $\varphi$ je proměnná.** Pak je $\varphi$ nebo $\neg\varphi$ přímo v $L_u$ a stačí ho zopakovat. Pro $L_u = \{x, \neg y, \neg z\}$ a $\varphi = y$ ($u(y) = 0$) chceme $\neg y$:
> >
> > $$
> > \begin{array}{rll}\text{1.} & x & \text{P} \\ \text{2.} & \neg y & \text{P} \\ \text{3.} & \neg z & \text{P} \\ \text{4.} & \neg y & \text{it}\ 2\end{array}
> > $$
> >
> > **2) $\varphi = \neg\alpha$**, kde $\alpha$ splňuje lemma (indukční předpoklad).
> > - $u(\varphi) = 1$: pak $u(\alpha) = 0$, podle indukčního předpokladu $L_u \vdash \neg\alpha$, a $\neg\alpha$ **je** $\varphi$. Hotovo.
> > - $u(\varphi) = 0$: pak $u(\alpha) = 1$, podle indukčního předpokladu $L_u \vdash \alpha$. Odvození prodloužíme o jeden řádek $\neg\neg$i a máme $\neg\neg\alpha = \neg\varphi$:
> >
> > $$
> > \begin{array}{rll}\text{1.} & \tilde x_1 & \text{P} \\  & \vdots &  \\ \text{n.} & \tilde x_n & \text{P} \\  & \vdots &  \\ \text{k.} & \alpha & \text{(ind. předp.)} \\ \text{k{+}1.} & \neg\neg\alpha & {\neg\neg}\text{i}\ k\end{array}
> > $$
> >
> > **3) $\varphi = \alpha \wedge \beta$, $\alpha \vee \beta$, $\alpha \Rightarrow \beta$** se dělají stejně: podle $u(\alpha)$, $u(\beta)$ se z odvození $\alpha$ nebo $\neg\alpha$ a $\beta$ nebo $\neg\beta$ (indukční předpoklad) složí odvození $\varphi$ nebo $\neg\varphi$. Případ $\alpha \Rightarrow \beta$ rozebírá další přednáška.

^veta-lemma-literaly

> [!lidsky] Lidsky
> Pravdivostní tabulka jde „přepsat do důkazů“: každý řádek, ve kterém je $\varphi$ pravdivá, dá odvození $\varphi$ z literálů toho řádku. Pro tautologii je to **každý** řádek: $L_u \vdash \varphi$ pro všechna $u$, nikdy $\neg\varphi$.

> [!example] Příklad
> $\varphi = a \wedge \neg b$, $u$: $a \mapsto 0$, $b \mapsto 0$. Pak $u(\varphi) = 0$, $L_u = \{\neg a, \neg b\}$ a lemma slibuje $L_u \vdash \neg(a \wedge \neg b)$:
>
> $$
> \begin{array}{rll}\text{1.} & \neg a & \text{P} \\ \text{2.} & \neg b & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & a\wedge\neg b & \text{P} \\ \text{4.} & a & {\wedge}\text{e}_1\ 3 \\ \text{5.} & \bot & {\neg}\text{e}\ 4, 1 \\ \hline\end{array} &  \\ \text{6.} & \neg(a\wedge\neg b) & {\neg}\text{i}\ 3\text{–}5\end{array}
> $$

### Slepení řádků přes TND

Pro tautologii $\varphi$ s proměnnými $x, y, z$ dá lemma osm odvození $L_1 \vdash \varphi, \dots, L_8 \vdash \varphi$. Každé ale ještě má předpoklady (literály). Ty se odstraní po jedné proměnné: napíšeš $z \vee \neg z$ (TND), do boxu $z$ vložíš odvození z řádku s $z$, do boxu $\neg z$ odvození z řádku s $\neg z$, a $\vee$e dá $\varphi$ už bez předpokladu o $z$. Totéž pak pro $y$ a nakonec pro $x$.

> [!obrazek] Skládání odvození tautologie
> ![[lgr07-skladani-tnd.png]]
> *Listy (modře) jsou odvození z lemmatu pro osm řádků tabulky. Každý oranžový uzel je jedno TND s rozborem případů ∨e, který zahodí předpoklad jedné proměnné. Kořen je odvození $\vdash \varphi$ bez předpokladů.*

Pro dvě proměnné $x, y$ vypadá celé odvození takto (svislé tečky jsou odvození z lemmatu; jeho předpoklady jsou tu otevřené pomocné předpoklady boxů, takže se místo „P“ píšou jako [[iterace]]):

$$
\begin{array}{rll}\text{1.} & x\vee\neg x & \text{TND} \\  & \begin{array}{|rll|}\hline \text{2.} & x & \text{P} \\ \text{3.} & y\vee\neg y & \text{TND} \\  & \begin{array}{|rll|}\hline \text{4.} & y & \text{P} \\  & \vdots &  \\ \text{5.} & \varphi & \text{lemma, } L_u = \{x, y\} \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{6.} & \neg y & \text{P} \\  & \vdots &  \\ \text{7.} & \varphi & \text{lemma, } L_u = \{x, \neg y\} \\ \hline\end{array} &  \\ \text{8.} & \varphi & {\vee}\text{e}\ 3, 4\text{–}5, 6\text{–}7 \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{9.} & \neg x & \text{P} \\ \text{10.} & y\vee\neg y & \text{TND} \\  & \begin{array}{|rll|}\hline \text{11.} & y & \text{P} \\  & \vdots &  \\ \text{12.} & \varphi & \text{lemma, } L_u = \{\neg x, y\} \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{13.} & \neg y & \text{P} \\  & \vdots &  \\ \text{14.} & \varphi & \text{lemma, } L_u = \{\neg x, \neg y\} \\ \hline\end{array} &  \\ \text{15.} & \varphi & {\vee}\text{e}\ 10, 11\text{–}12, 13\text{–}14 \\ \hline\end{array} &  \\ \text{16.} & \varphi & {\vee}\text{e}\ 1, 2\text{–}8, 9\text{–}15\end{array}
$$

> [!lidsky] Lidsky
> Rozbor všech případů jako v matematice: „buď $x$ platí, nebo ne; v obou případech buď $y$ platí, nebo ne; …“. V každém z $2^n$ koncových případů je $\varphi$ dokázaná lemmatem, takže je dokázaná vždy. TND se přitom použije $1 + 2 + \dots + 2^{n-1} = 2^n - 1$ krát.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč smíš používat ¬¬i, MT, RAA a TND, i když nejsou mezi základními pravidly přirozené dedukce?
> Jsou to **odvozená pravidla**: každé jde odvodit ze základních pravidel, takže jeho použití jde nahradit tím odvozením. Odvoditelné formule se nezmění a systém zůstane korektní.

> [!karta|02]- Čím se liší RAA od pravidla ¬i?
> $\neg$i: box **$\varphi$** … $\bot$ dá **$\neg\varphi$**. RAA: box **$\neg\varphi$** … $\bot$ dá **$\varphi$**. RAA = $\neg$i (dá $\neg\neg\varphi$) + **$\neg\neg$e**.

> [!karta|03]- Proč se $\vdash \varphi \vee \neg\varphi$ nedá odvodit jedním $\vee$i, ale musí přes spor?
> $\vee$i potřebuje mít dokázanou $\varphi$ nebo $\neg\varphi$. Pro proměnnou $a$ ale **nejde ani $\vdash a$, ani $\vdash \neg a$** (nejsou to tautologie, korektnost). Proto se předpokládá $\neg(\varphi \vee \neg\varphi)$, odvodí spor a použije $\neg\neg$e.

> [!karta|04]- Proč neklasické (např. intuicionistické) logiky nepřijímají TND, ¬¬e a RAA?
> $\neg\neg\varphi$ říká jen, že **$\neg\varphi$ není pravda**; to ještě neznamená, že je pravda $\varphi$ (že pro ni máš důkaz). Tyto logiky mají víc možností než 1 a 0, takže „třetí možnost“ existuje.

> [!karta|05]- Jaký je rozdíl mezi $\varphi \dashv\vdash \psi$ a $\varphi \mathrel{\vert\!=\!\vert} \psi$, a proč na něm v přirozené dedukci nezáleží?
> $\dashv\vdash$ je **syntaktická** (jedna jde odvodit z druhé a naopak), $\mathrel{\vert\!=\!\vert}$ **sémantická** (stejné hodnoty ve všech ohodnoceních). Podle **věty o úplnosti** jsou to tytéž dvojice formulí.

> [!karta|06]- Dokaž směr „⇒“ syntaktické věty o dedukci: z $S \cup \{\varphi\} \vdash \psi$ plyne $S \vdash \varphi \Rightarrow \psi$.
> Vezmi odvození $\psi$ z $S \cup \{\varphi\}$. Předpoklady z $S$ dej nahoru, z $\varphi$ udělej **pomocný předpoklad, který otevře box** až po řádek $\psi$, a box uzavři pravidlem **$\Rightarrow$i**: dostaneš $\varphi \Rightarrow \psi$ jen z $S$.

> [!karta|07]- Dokaž směr „⇐“ syntaktické věty o dedukci: z $S \vdash \varphi \Rightarrow \psi$ plyne $S \cup \{\varphi\} \vdash \psi$.
> K odvození $\varphi \Rightarrow \psi$ z $S$ připiš řádek **$\varphi$ (předpoklad)**, teď z $S \cup \{\varphi\}$, a pak **modus ponens** ($\Rightarrow$e) dá $\psi$.

> [!karta|08]- Proč je syntaktická věta o kompaktnosti skoro zadarmo, kdežto sémantická je nejtěžší část důkazu věty o úplnosti?
> Odvození je **konečná posloupnost**, použije jen konečně mnoho předpokladů z $S$, a ty tvoří $S'$. U $\models$ žádný konečný objekt v pozadí není: mluví o **všech ohodnoceních** (i nekonečně mnoha proměnných), a konečnost se musí teprve dokázat.

> [!karta|09]- Proč se věta o korektnosti dokazuje silnou, a ne slabou indukcí podle délky odvození?
> Pravidlo na posledním řádku bere předpoklady z **libovolných dřívějších řádků**, ne jen z předposledního. Indukční předpoklad proto musí platit pro **všechna kratší odvození**, a to dává silná indukce.

> [!karta|10]- Ukaž indukční krok důkazu korektnosti pro pravidlo $\vee$i (řádek $n + 1$: $\alpha \vee \beta$ z řádku $k$: $\alpha$).
> Odvození $\alpha$ (řádky $1, \dots, k$) je kratší, podle indukčního předpokladu **$S \models \alpha$**. Zároveň **$\alpha \models \alpha \vee \beta$**. Tranzitivitou **$S \models \alpha \vee \beta$**.

> [!karta|11]- Jak dokážeš, že $S \nvdash \varphi$ (že odvození neexistuje)?
> Najdi **ohodnocení $u$ s $u(S) = 1$ a $u(\varphi) = 0$**. Pak $S \not\models \varphi$ a podle **věty o korektnosti** (obměnou) $S \nvdash \varphi$. Hledat „všechna odvození“ není potřeba.

> [!karta|12]- Jak se dokáže směr „⇐“ věty o úplnosti ($S \models \varphi \Rightarrow S \vdash \varphi$)? Popiš řetěz vět.
> **Sémantická kompaktnost**: $S' = \{\alpha, \beta\} \models \varphi$. **Sémantická věta o dedukci**: $\models \alpha \Rightarrow (\beta \Rightarrow \varphi)$. **Slabá věta o úplnosti**: $\vdash \alpha \Rightarrow (\beta \Rightarrow \varphi)$. **Syntaktická věta o dedukci**: $\{\alpha, \beta\} \vdash \varphi$. **Syntaktická kompaktnost**: $S \vdash \varphi$.

> [!karta|13]- Co říká lemma o literálech řádku pro tautologii $\varphi$?
> $u(\varphi) = 1$ pro každé $u$, takže **$L_u \vdash \varphi$ pro všech $2^n$ řádků** (nikdy $L_u \vdash \neg\varphi$). Každý řádek tabulky dá jedno odvození $\varphi$ z literálů toho řádku.

> [!karta|14]- Dokaž základ indukce v lemmatu o literálech řádku ($\varphi$ je proměnná $x$).
> Je-li $u(x) = 1$, je **$x \in L_u$**; je-li $u(x) = 0$, je **$\neg x \in L_u$**. V obou případech stačí v odvození vypsat předpoklady $L_u$ a požadovanou formuli zopakovat (**it**).

> [!karta|15]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \neg\alpha$.
> $u(\varphi) = 1$: $u(\alpha) = 0$, podle indukčního předpokladu $L_u \vdash \neg\alpha$, a to **je** $\varphi$. $u(\varphi) = 0$: $u(\alpha) = 1$, tedy $L_u \vdash \alpha$, a jeden řádek **$\neg\neg$i** dá $\neg\neg\alpha = \neg\varphi$.

> [!karta|16]- Jakou roli hraje TND v důkazu slabé věty o úplnosti?
> Lemma dá odvození $\varphi$ jen **z literálů řádku**. TND $x \vee \neg x$ s **$\vee$e** spojí odvození z řádků s $x$ a s $\neg x$ do jednoho, které už předpoklad o $x$ nepotřebuje. Po všech proměnných zbude $\vdash \varphi$.

> [!karta|17]- Jak se z odvození $L_u \vdash \varphi$ pro dvě proměnné $x, y$ složí odvození $\vdash \varphi$?
> $x \vee \neg x$ (TND); v boxu $x$: $y \vee \neg y$ (TND), box $y$ s odvozením z $\{x, y\}$, box $\neg y$ s odvozením z $\{x, \neg y\}$, **$\vee$e** dá $\varphi$. Stejně v boxu $\neg x$. Nakonec **$\vee$e** přes $x \vee \neg x$ dá $\varphi$ bez předpokladů.

> [!karta|18]- Kolikrát se při skládání odvození tautologie s $n$ proměnnými použije TND?
> Každý vnitřní uzel stromu rozboru případů je jedno TND: $1 + 2 + \dots + 2^{n-1} = $ **$2^n - 1$** (pro $n = 3$ sedm).

### Příklady na procvičení

> [!priklad|19]- Odvoď ze základních pravidel $\varphi \vdash \neg\neg\varphi$ (pravidlo ¬¬i).
> $$
> \begin{array}{rll}\text{1.} & \varphi & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & \neg\varphi & \text{P} \\ \text{3.} & \bot & {\neg}\text{e}\ 1, 2 \\ \hline\end{array} &  \\ \text{4.} & \neg\neg\varphi & {\neg}\text{i}\ 2\text{–}3\end{array}
> $$

> [!priklad|20]- Odvoď ze základních pravidel $\varphi \Rightarrow \psi,\ \neg\psi \vdash \neg\varphi$ (pravidlo MT).
> $$
> \begin{array}{rll}\text{1.} & \varphi\Rightarrow\psi & \text{P} \\ \text{2.} & \neg\psi & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & \varphi & \text{P} \\ \text{4.} & \psi & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \bot & {\neg}\text{e}\ 4, 2 \\ \hline\end{array} &  \\ \text{6.} & \neg\varphi & {\neg}\text{i}\ 3\text{–}5\end{array}
> $$

> [!priklad|21]- Odvoď $\vdash \varphi \vee \neg\varphi$ (TND) bez použití TND.
> $$
> \begin{array}{rll} & \begin{array}{|rll|}\hline \text{1.} & \neg(\varphi\vee\neg\varphi) & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & \varphi & \text{P} \\ \text{3.} & \varphi\vee\neg\varphi & {\vee}\text{i}_1\ 2 \\ \text{4.} & \bot & {\neg}\text{e}\ 3, 1 \\ \hline\end{array} &  \\ \text{5.} & \neg\varphi & {\neg}\text{i}\ 2\text{–}4 \\ \text{6.} & \varphi\vee\neg\varphi & {\vee}\text{i}_2\ 5 \\ \text{7.} & \bot & {\neg}\text{e}\ 6, 1 \\ \hline\end{array} &  \\ \text{8.} & \neg\neg(\varphi\vee\neg\varphi) & {\neg}\text{i}\ 1\text{–}7 \\ \text{9.} & \varphi\vee\neg\varphi & {\neg\neg}\text{e}\ 8\end{array}
> $$

> [!priklad|22]- Odvoď $a \Rightarrow b \vdash \neg a \vee b$.
> $$
> \begin{array}{rll}\text{1.} & a\Rightarrow b & \text{P} \\ \text{2.} & a\vee\neg a & \text{TND} \\  & \begin{array}{|rll|}\hline \text{3.} & a & \text{P} \\ \text{4.} & b & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \neg a\vee b & {\vee}\text{i}_2\ 4 \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{6.} & \neg a & \text{P} \\ \text{7.} & \neg a\vee b & {\vee}\text{i}_1\ 6 \\ \hline\end{array} &  \\ \text{8.} & \neg a\vee b & {\vee}\text{e}\ 2, 3\text{–}5, 6\text{–}7\end{array}
> $$

> [!priklad|23]- Odvoď $\neg b \Rightarrow \neg a \vdash a \Rightarrow b$.
> $$
> \begin{array}{rll}\text{1.} & \neg b\Rightarrow\neg a & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & a & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & \neg b & \text{P} \\ \text{4.} & \neg a & {\Rightarrow}\text{e}\ 3, 1 \\ \text{5.} & \bot & {\neg}\text{e}\ 2, 4 \\ \hline\end{array} &  \\ \text{6.} & b & \text{RAA}\ 3\text{–}5 \\ \hline\end{array} &  \\ \text{7.} & a\Rightarrow b & {\Rightarrow}\text{i}\ 2\text{–}6\end{array}
> $$

> [!priklad|24]- Odvoď $\neg(a \vee b) \vdash \neg a \wedge \neg b$.
> $$
> \begin{array}{rll}\text{1.} & \neg(a\vee b) & \text{P} \\  & \begin{array}{|rll|}\hline \text{2.} & a & \text{P} \\ \text{3.} & a\vee b & {\vee}\text{i}_1\ 2 \\ \text{4.} & \bot & {\neg}\text{e}\ 3, 1 \\ \hline\end{array} &  \\ \text{5.} & \neg a & {\neg}\text{i}\ 2\text{–}4 \\  & \begin{array}{|rll|}\hline \text{6.} & b & \text{P} \\ \text{7.} & a\vee b & {\vee}\text{i}_2\ 6 \\ \text{8.} & \bot & {\neg}\text{e}\ 7, 1 \\ \hline\end{array} &  \\ \text{9.} & \neg b & {\neg}\text{i}\ 6\text{–}8 \\ \text{10.} & \neg a\wedge\neg b & {\wedge}\text{i}\ 5, 9\end{array}
> $$
> Bez TND i RAA: dvakrát $\neg$i, v každém boxu $\vee$i a spor s řádkem 1.

> [!priklad|25]- Odvoď $\neg a \Rightarrow b,\ \neg b \vdash a$ pomocí odvozených pravidel.
> $$
> \begin{array}{rll}\text{1.} & \neg a\Rightarrow b & \text{P} \\ \text{2.} & \neg b & \text{P} \\ \text{3.} & \neg\neg a & \text{MT}\ 1, 2 \\ \text{4.} & a & {\neg\neg}\text{e}\ 3\end{array}
> $$
> **MT** dá $\neg\neg a$, **$\neg\neg$e** pak $a$.

> [!priklad|26]- Pro $u$: $a \mapsto 0$, $b \mapsto 0$ urči $L_u$ a odvoď z něj $\varphi = a \wedge \neg b$, nebo $\neg\varphi$ podle lemmatu o literálech řádku.
> $u(\varphi) = 0$, $L_u = \{\neg a, \neg b\}$, cíl **$L_u \vdash \neg(a \wedge \neg b)$**:
> $$
> \begin{array}{rll}\text{1.} & \neg a & \text{P} \\ \text{2.} & \neg b & \text{P} \\  & \begin{array}{|rll|}\hline \text{3.} & a\wedge\neg b & \text{P} \\ \text{4.} & a & {\wedge}\text{e}_1\ 3 \\ \text{5.} & \bot & {\neg}\text{e}\ 4, 1 \\ \hline\end{array} &  \\ \text{6.} & \neg(a\wedge\neg b) & {\neg}\text{i}\ 3\text{–}5\end{array}
> $$

---
← [[LGR 06 – Rezoluční tabulka a přirozená dedukce|15. 10. 2026 Rezoluční tabulka a přirozená dedukce]]

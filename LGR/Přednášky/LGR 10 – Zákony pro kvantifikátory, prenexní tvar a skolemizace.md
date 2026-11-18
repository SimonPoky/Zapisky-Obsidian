---
predmet: LGR
prednaska: 10
datum: 2026-11-05
zdroj: "handout 6, slajdy 8–27; handout 7, slajdy 5–11"
tags: [prednaska, LGR]
---

# LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace

*Přednáška 10 · čtvrtek 5. 11. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 6 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_6.pdf) · [handout 7 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_7.pdf)

Témata: `sémantický důsledek sentencí` · `tautologická ekvivalence sentencí` · `obecný uzávěr` · `negování kvantifikátorů` · `pořadí kvantifikátorů` · `vytýkání kvantifikátorů` · `prenexní tvar` · `klauzule v predikátové logice` · `ekvisplnitelnost` · `skolemizace`

Minule se definovalo, kdy je sentence pravdivá v interpretaci, co je model, splnitelná sentence a tautologie. Dnes se z výrokové logiky přenášejí **sémantický důsledek** a **tautologická ekvivalence** a hlavně se zjišťuje, jak s formulemi s kvantifikátory „počítat“: jak negovat $\forall$ a $\exists$, kdy smějí kvantifikátory přehodit pořadí a kdy je smíme vytknout před $\wedge$ a $\vee$. Výsledkem je **prenexní tvar** (všechny kvantifikátory vpředu). Na konci začíná rezoluce v predikátové logice: existenční kvantifikátory se odstraní **skolemizací**, která ale zachová jen splnitelnost, ne význam.

## §0 Přehled na jedné stránce

| zákon / pojem | zápis | platí? | proč, lidsky |
|---|---|---|---|
| negace $\forall$ | $\neg\forall x\,\alpha$ $\models\mid$ $\exists x\,\neg\alpha$ | ⇔ | „ne všichni“ = „někdo ne“ |
| negace $\exists$ | $\neg\exists x\,\alpha$ $\models\mid$ $\forall x\,\neg\alpha$ | ⇔ | „nikdo“ = „všichni ne“ |
| stejné kvantifikátory | $\forall x\,\forall y\,R$ $\models\mid$ $\forall y\,\forall x\,R$ | ⇔ | pořadí v řadě „pro každé“ je jedno |
| různé kvantifikátory | $\exists x\,\forall y\,R \models \forall y\,\exists x\,R$ | jen ⇒ | jeden pro všechny ⇒ každý má někoho, ne naopak |
| $\forall$ před $\wedge$, $\exists$ před $\vee$ | $\forall x\,P \wedge \forall x\,Q$ $\models\mid$ $\forall x\,(P \wedge Q)$ | ⇔ | $\forall$ je velká konjunkce |
| $\forall$ před $\vee$, $\exists$ před $\wedge$ | $\forall x\,P \vee \forall x\,Q \models \forall x\,(P \vee Q)$ | jen ⇒ | „všichni P nebo všichni Q“ je silnější |
| jiná jména proměnných | $\forall x\,P(x) \vee \forall y\,Q(y)$ $\models\mid$ $\forall x\,\forall y\,(P(x) \vee Q(y))$ | ⇔ | podformule spolu nesdílejí proměnnou |
| vytýkání z předpokladu $\Rightarrow$ | $(\forall x\,\alpha) \Rightarrow \beta$ $\models\mid$ $\exists x\,(\alpha \Rightarrow \beta)$ | ⇔ | kvantifikátor se otočí |
| prenexní tvar | $\nabla_1 x_1 \dots \nabla_n x_n\,\psi$, $\psi$ otevřená | vždy existuje | kvantifikátory vpředu, za nimi „obyčejná“ formule |
| skolemizace | $\forall x\,\exists y\,R(x,y) \approx \forall x\,R(x,f(x))$ | jen splnitelnost | svědka pojmenuje nový symbol |

## §1 Sémantický důsledek a tautologická ekvivalence sentencí

Ve výrokové logice se porovnávala pravdivostní ohodnocení, tady se porovnávají **interpretace**. Z [[LGR 09 – Pravdivost formulí, model a tautologie|minula]] víme, co je [[model sentence]], [[splnitelná sentence]] a [[tautologie predikátové logiky]]. Pro celé množiny sentencí to funguje stejně.

> [!definice] Definice · splnitelná množina sentencí · handout 6, slajd 8
> Množina sentencí $S$ je *splnitelná*, existuje-li interpretace, ve které jsou pravdivé **všechny** sentence z $S$ (*model* množiny $S$). Jinak je *nesplnitelná*. Prázdná množina je splnitelná, jejím modelem je každá interpretace.

^def-splnitelna-mnozina-sentenci

> [!lidsky] Lidsky
> Seznam pravidel o světě, která jdou splnit všechna naráz. Nestačí, že každé zvlášť jde splnit: musí to jít v **jedné** interpretaci.

> [!example] Příklad
> - $\{\forall x\,P(x),\ \exists x\,\neg P(x)\}$ je nesplnitelná: první sentence chce $[\![P]\!] = U$, druhá prvek mimo $[\![P]\!]$. Každá zvlášť přitom splnitelná je.
> - $\{\forall x\,\exists y\,R(x,y),\ \forall x\,\neg R(x,x)\}$ je splnitelná: $U = \{0, 1\}$, $[\![R]\!] = \{(0, 1), (1, 0)\}$.

> [!definice] Definice · sémantický důsledek · handout 6, slajd 9
> Sentence $\varphi$ je *sémantickým důsledkem* množiny sentencí $S$, píšeme $S \models \varphi$, jestliže **každý model** množiny $S$ je i modelem $\varphi$. Zápis $\models \varphi$ (důsledek prázdné množiny) znamená, že $\varphi$ je tautologie.

^def-semanticky-dusledek-pl

> [!lidsky] Lidsky
> V žádném světě, kde platí všechny předpoklady, nesmí závěr selhat. **Vyvrátit** důsledek stačí jednou interpretací (model $S$, který není modelem $\varphi$). **Dokázat** ho vyžaduje úvahu o libovolném modelu, konečně mnoho příkladů nestačí.

> [!example] Příklad
> - $\forall x\,P(x) \models \exists x\,P(x)$: universum je vždy neprázdné, takže nějaký prvek leží v $[\![P]\!] = U$.
> - $\exists x\,P(x) \not\models \forall x\,P(x)$: $U = \mathbb{N}$, $[\![P]\!] =$ sudá čísla je model první sentence, ne druhé.

> [!definice] Definice · tautologická ekvivalence · handout 6, slajd 13
> Sentence $\varphi, \psi$ jsou *tautologicky ekvivalentní*, $\varphi \models\mid \psi$, mají-li **stejné modely**. Ekvivalentně: $\varphi \models \psi$ a $\psi \models \varphi$, nebo také: $\varphi \Leftrightarrow \psi$ je tautologie.

^def-tautologicka-ekvivalence-pl

> [!lidsky] Lidsky
> Dvě sentence říkají totéž jinými slovy: neexistuje svět, kde by jedna platila a druhá ne. Porovnávají se množiny modelů, ne zápis.

> [!example] Příklad
> $\forall x\,(P(x) \wedge Q(x)) \models\mid \forall x\,P(x) \wedge \forall x\,Q(x)$: obě chtějí $[\![P]\!] \cap [\![Q]\!] = U$. Naopak $\exists x\,P(x)$ a $\forall x\,P(x)$ ekvivalentní nejsou, rozliší je $[\![P]\!] =$ sudá čísla v $\mathbb{N}$.

> [!veta] Převod na nesplnitelnost · handout 6, slajd 10
> Pro sentence platí stejné převody jako ve výrokové logice:
> - $\varphi$ je tautologie ⟺ **$\neg\varphi$ je nesplnitelná**,
> - $S \models \varphi$ ⟺ **$S \cup \{\neg\varphi\}$ je nesplnitelná**,
> - $S \cup \{\varphi\} \models \psi$ ⟺ $S \models \varphi \Rightarrow \psi$ (věta o dedukci).

^veta-prevod-na-nesplnitelnost

> [!lidsky] Lidsky
> Všechny otázky („platí vždy?“, „plyne to?“, „říkají totéž?“) se dají přeložit na jedinou: „dá se to splnit?“. Proto stačí jedna metoda na nesplnitelnost, a tou bude rezoluce (§7 a příště).

## §2 Formule s volnými proměnnými a obecný uzávěr

Zákony v tabulce §0 se píší s formulemi jako $\alpha$, $\beta$, které volné proměnné mít smějí. Aby $\models\mid$ dávalo smysl i pro ně, přejde se k sentencím.

> [!definice] Definice · obecný uzávěr · handout 6, slajd 24
> Má-li formule $\alpha$ volné proměnné $x_1, \dots, x_n$, je její *obecný uzávěr* sentence $\forall x_1 \dots \forall x_n\,\alpha$. Pro formule s volnými proměnnými se definuje $\alpha \models\mid \beta$, právě když mají jejich obecné uzávěry stejné modely.

^def-obecny-uzaver

> [!lidsky] Lidsky
> Volná proměnná se čte „ať dosadíš cokoliv“. Uzávěr to napíše výslovně: před formuli se přidá $\forall$ pro každou volnou proměnnou.

> [!example] Příklad
> Obecný uzávěr $R(x, y) \Rightarrow P(x)$ je $\forall x\,\forall y\,(R(x, y) \Rightarrow P(x))$. Zákon $\neg(P(x) \vee Q(x)) \models\mid \neg P(x) \wedge \neg Q(x)$ tedy znamená, že $\forall x\,\neg(P(x) \vee Q(x))$ a $\forall x\,(\neg P(x) \wedge \neg Q(x))$ mají stejné modely.

> [!navic] Zákony výrokové logiky platí dál
> Když ve výrokové tautologické ekvivalenci (De Morgan, distributivita, $\alpha \Rightarrow \beta \models\mid \neg\alpha \vee \beta$ …) nahradíš výrokové proměnné formulemi predikátové logiky, dostaneš platnou ekvivalenci. Nové jsou jen zákony pro kvantifikátory v §3–§5.

## §3 Negování kvantifikátorů

> [!veta] Negování kvantifikátorů · handout 6, slajdy 14 a 21
> Pro libovolnou formuli $\alpha$:
>
> $$
> \neg\forall x\,\alpha \models\mid \exists x\,\neg\alpha, \qquad \neg\exists x\,\alpha \models\mid \forall x\,\neg\alpha.
> $$

^veta-negovani-kvantifikatoru

> [!lidsky] Lidsky
> Negace projde kvantifikátorem a otočí ho. „Ne všichni prošli“ = „někdo neprošel“, „nikdo neprošel“ = „všichni neprošli“. Jsou to De Morganovy zákony: $\forall$ je velká konjunkce přes všechny prvky universa, $\exists$ velká disjunkce.

> [!example] Příklad
> Pro $\alpha = P(x)$: modely $\neg\forall x\,P(x)$ mají $[\![P]\!] \neq U$, modely $\exists x\,\neg P(x)$ mají $U \setminus [\![P]\!] \neq \emptyset$, a to je totéž. Víc kvantifikátorů se neguje postupně zvenku: $\neg\exists x\,\forall y\,R(x, y) \models\mid \forall x\,\exists y\,\neg R(x, y)$.

> [!pozor] Častá chyba
> $\forall x\,P(x) \vee \forall x\,\neg P(x)$ **není** tautologie (v $U = \{0, 1\}$, $[\![P]\!] = \{0\}$ neplatí ani jedna část). Negace sentence $\forall x\,P(x)$ je $\exists x\,\neg P(x)$, ne $\forall x\,\neg P(x)$.

## §4 Pořadí kvantifikátorů

> [!veta] Přehazování kvantifikátorů · handout 6, slajdy 16–17
> - Stejné kvantifikátory pořadí prohodit smějí: $\forall x\,\forall y\,\alpha \models\mid \forall y\,\forall x\,\alpha$ a $\exists x\,\exists y\,\alpha \models\mid \exists y\,\exists x\,\alpha$.
> - Různé ne: $\exists x\,\forall y\,R(x,y) \models \forall y\,\exists x\,R(x,y)$, ale **opačný důsledek neplatí**.

^veta-prehazovani-kvantifikatoru

> [!lidsky] Lidsky
> „Existuje jeden, kdo zná všechny“ je silnější než „každého někdo zná“. Ve druhém případě smí být pro každé $y$ jiný svědek $x$, v prvním musí být jeden společný. U stejných kvantifikátorů se nic takového neděje, je to jen přeskládání velké konjunkce (disjunkce).

> [!obrazek] Pořadí kvantifikátorů na šipkách
> ![[lgr10-poradi.png]]
> *Šipka z $x$ do $y$ znamená $(x, y) \in [\![R]\!]$. Vlevo (zelená) z vrcholu 0 vede šipka do všech, takže platí $\exists x\,\forall y\,R(x,y)$, a proto i $\forall y\,\exists x\,R(x,y)$. Vpravo (oranžová) do každého vrcholu nějaká šipka vede, ale žádný vrchol nemá šipku do všech: $\forall y\,\exists x$ platí, $\exists x\,\forall y$ ne.*

> [!example] Příklad
> $U = \{0, 1\}$, $[\![R]\!] = \{(0, 1), (1, 0)\}$: $\forall y\,\exists x\,R(x, y)$ platí (do 0 vede šipka z 1, do 1 z 0), $\exists x\,\forall y\,R(x, y)$ ne (žádný prvek nemá šipku sám do sebe, tedy ani do všech).

## §5 Vytýkání kvantifikátorů před $\wedge$ a $\vee$

> [!veta] Vytýkání kvantifikátorů · handout 6, slajdy 18–23
> 1. $\forall x\,\alpha \wedge \forall x\,\beta \models\mid \forall x\,(\alpha \wedge \beta)$ a $\exists x\,\alpha \vee \exists x\,\beta \models\mid \exists x\,(\alpha \vee \beta)$.
> 2. Jen jedním směrem: $\forall x\,\alpha \vee \forall x\,\beta \models \forall x\,(\alpha \vee \beta)$ a $\exists x\,(\alpha \wedge \beta) \models \exists x\,\alpha \wedge \exists x\,\beta$.
> 3. ==Neobsahuje-li $\beta$ volnou proměnnou $x$==, vytknout jde **cokoliv před cokoliv**: $(\nabla x\,\alpha) \mathbin{\Diamond} \beta \models\mid \nabla x\,(\alpha \mathbin{\Diamond} \beta)$ pro $\nabla \in \{\forall, \exists\}$, $\Diamond \in \{\wedge, \vee\}$.
> 4. U implikace (opět $x$ není volná v $\beta$): $(\forall x\,\alpha) \Rightarrow \beta \models\mid \exists x\,(\alpha \Rightarrow \beta)$, $(\exists x\,\alpha) \Rightarrow \beta \models\mid \forall x\,(\alpha \Rightarrow \beta)$, ze závěru $\beta \Rightarrow \nabla x\,\alpha \models\mid \nabla x\,(\beta \Rightarrow \alpha)$.

^veta-vytykani-kvantifikatoru

> [!lidsky] Lidsky
> $\forall$ je velká konjunkce, takže se snese s $\wedge$; $\exists$ je velká disjunkce, snese se s $\vee$. Když druhá část na $x$ vůbec nezávisí, chová se při všech dosazeních za $x$ jako konstanta a vytknout jde cokoliv. Z předpokladu implikace se kvantifikátor otočí, protože $\alpha \Rightarrow \beta \models\mid \neg\alpha \vee \beta$ a negace kvantifikátor otáčí.

> [!obrazek] Kde vytýkání selže
> ![[lgr10-vytykani.png]]
> *Universum $\{0, 1, 2, 3\}$, modré pruhy jsou $[\![P]\!]$, oranžové $[\![Q]\!]$. Nahoře pokrývá každý prvek $P$ nebo $Q$, takže $\forall x\,(P \vee Q)$ platí, ale ani $P$, ani $Q$ nepokrývá vše. Dole má $P$ i $Q$ svého svědka, ale žádný prvek není v obou.*

> [!example] Příklad
> $\forall x\,P(x) \vee \forall x\,Q(x)$ chce $[\![P]\!] = U$ nebo $[\![Q]\!] = U$, kdežto $\forall x\,(P(x) \vee Q(x))$ jen $[\![P]\!] \cup [\![Q]\!] = U$. Protipříklad k opačnému směru: $U = \{0, 1, 2\}$, $[\![P]\!] = \{0, 1\}$, $[\![Q]\!] = \{1, 2\}$. S jinými jmény proměnných ekvivalence platí: $\forall x\,P(x) \vee \forall y\,Q(y) \models\mid \forall x\,\forall y\,(P(x) \vee Q(y))$, protože $Q(y)$ neobsahuje $x$.

> > [!note]- Důkaz $\forall x\,\forall y\,(P(x) \vee Q(y)) \models \forall x\,P(x) \vee \forall y\,Q(y)$
> > Buď $(U, [\![-]\!])$ model levé strany. Je-li $[\![P]\!] = U$, platí $\forall x\,P(x)$. Jinak existuje $u \notin [\![P]\!]$. Při kontextu $x \mapsto u$ a libovolném $y \mapsto v$ je $P(x) \vee Q(y)$ pravdivá a $P(x)$ ne, takže $v \in [\![Q]\!]$. Protože $v$ bylo libovolné, $[\![Q]\!] = U$ a platí $\forall y\,Q(y)$.

## §6 Prenexní tvar

> [!definice] Definice · prenexní tvar · handout 6, slajdy 25–27
> Formule je v *prenexním tvaru*, má-li tvar $\nabla_1 x_1 \dots \nabla_n x_n\,\psi$, kde $\nabla_i \in \{\forall, \exists\}$, $x_1, \dots, x_n$ jsou všechny vázané proměnné a $\psi$ je otevřená formule (bez kvantifikátorů, *jádro*).
>
> **Věta:** ke každé sentenci $\varphi$ existuje sentence $\varphi_p$ v prenexním tvaru, $\varphi \models\mid \varphi_p$.

^def-prenexni-tvar

> [!lidsky] Lidsky
> Všechny kvantifikátory vpředu jako hlavička, za nimi „obyčejná“ formule jako ve výrokové logice. Postup: (1) přejmenovat vázané proměnné, aby každý kvantifikátor měl vlastní, (2) nechat jen $\neg, \wedge, \vee$, (3) protlačit negace k atomům, (4) vytknout kvantifikátory.

> [!obrazek] Převod do prenexního tvaru krok za krokem
> ![[lgr10-prenex.png]]
> *Modré rámečky jsou mezikroky, každý zachovává $\models\mid$; zelený je výsledek s otevřeným jádrem $\neg P(x) \vee R(z, y)$. Krok 1 (přejmenování) je nutný, jinak by vytknutí z §5 nebylo bezpečné.*

> [!example] Příklad
> $\forall x\,P(x) \Rightarrow \forall x\,\exists y\,R(x, y) \models\mid \exists x\,\neg P(x) \vee \forall z\,\exists y\,R(z, y) \models\mid \exists x\,\forall z\,\exists y\,(\neg P(x) \vee R(z, y))$. Jiný, stejně dobrý výsledek je $\forall z\,\exists y\,\exists x\,(\dots)$: prenexní tvar není jednoznačný.

> [!pozor] Co se při vytýkání nesmí
> Z levé a pravé podformule se smí vytýkat v libovolném pořadí, ale kvantifikátory **ze stejné podformule** si pořadí vyměnit nesmějí ($\exists$ a $\forall$ spolu nekomutují, §4).

## §7 Začátek rezoluce v predikátové logice: klauzule a skolemizace

Rezoluce bude dokazovat nesplnitelnost (§1). Potřebuje množinu **klauzulí**, tedy jen obecné kvantifikátory. Existenční se odstraní skolemizací.

> [!definice] Definice · klauzule · handout 7, slajd 5
> *Literál* je atomická formule nebo její negace. *Klauzule* je sentence tvaru $\forall x_1 \dots \forall x_n\,(L_1 \vee \dots \vee L_k)$, kde $L_i$ jsou literály; prázdná klauzule je $\mathrm{ff}$.

^def-klauzule-pl

> [!lidsky] Lidsky
> Pravidlo tvaru „pro všechna $x, y, \dots$ platí aspoň jeden z literálů“: jen obecné kvantifikátory, všechny vpředu, za nimi disjunkce literálů. Je to klauzule z výrokové logiky, jen s $\forall$ před ní.

> [!example] Příklad
> Klauzule jsou $\forall x\,\forall y\,(P(x) \vee \neg R(a, y))$, $Q(a)$ i $\mathrm{ff}$. Klauzule nejsou $\exists x\,P(x)$ (existenční kvantifikátor), $\forall x\,(P(x) \wedge Q(x))$ (konjunkce uvnitř) ani $\forall x\,P(x) \vee Q(a)$ (kvantifikátor uvnitř); druhá se rozdělí na klauzule $\forall x\,P(x)$ a $\forall x\,Q(x)$.

> [!definice] Definice · skolemizace · handout 7, slajdy 8–11
> Buď $y$ volná proměnná v $\alpha$. Pak
>
> $$
> \exists y\,\alpha \approx \alpha[y := c], \qquad \forall x_1 \dots \forall x_n\,\exists y\,\alpha \approx \forall x_1 \dots \forall x_n\,\alpha[y := f(x_1, \dots, x_n)],
> $$
>
> kde $c$ je **nový** konstantní symbol a $f$ **nový** funkční symbol arity $n$ (*skolemizační symboly*); $\approx$ znamená ekvisplnitelnost. Skolemizovaná sentence $\models$ původní, opačně obecně ne. Skolemizuje se postupně zleva od prvního $\exists$.

^def-skolemizace

> [!lidsky] Lidsky
> Svědka, o kterém $\exists$ říká „nějaký existuje“, pojmenuješ novým jménem. Když svědek závisí na proměnných z $\forall$ před ním, pojmenuješ ho funkcí těchto proměnných: „pro každé $x$ ten jeho $f(x)$“. Symbol musí být nový, aby ho interpretace směla vyložit libovolně, tedy právě jako svědka; jazyk se tím obohacuje.

> [!example] Příklad
> $\exists x\,P(x) \to P(c)$; $\forall x\,\exists y\,R(x, y) \to \forall x\,R(x, f(x))$; $\exists x\,\forall y\,\exists z\,(R(x,y) \wedge R(y,z)) \to \forall y\,(R(c, y) \wedge R(y, f(y)))$ ($x$ nemá před sebou žádné $\forall$, takže konstanta; $z$ má před sebou $\forall y$, takže funkce arity 1).

> [!pozor] Proč nový symbol
> Nahradit $\exists x\,P(x)$ starou konstantou $a$ nejde: $\{\exists x\,P(x), \neg P(a)\}$ je splnitelná ($U = \{0, 1\}$, $[\![P]\!] = \{0\}$, $[\![a]\!] = 1$), ale $\{P(a), \neg P(a)\}$ ne. S novým $c$ stačí dát $[\![c]\!] = 0$.

> [!navic] Ekvisplnitelnost, ne ekvivalence
> $P(c) \models \exists x\,P(x)$, ale ne naopak ($U = \{0, 1\}$, $[\![P]\!] = \{0\}$, $[\![c]\!] = 1$). Každý model původní sentence se ale dá **přeinterpretováním nového symbolu** předělat na model skolemizované, a to pro rezoluci stačí: hledá se jen nesplnitelnost. Celý převod na klauzule (prenexní tvar, skolemizace, rozdělení podle $\wedge$) pokračuje v [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice|další přednášce]].

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč platí $\neg\forall x\,P(x) \models\mid \exists x\,\neg P(x)$? Vysvětli přes modely.
> Modely levé strany mají $[\![P]\!] \neq U$, modely pravé mají $U \setminus [\![P]\!] \neq \emptyset$. Pro $[\![P]\!] \subseteq U$ je to **totéž**, takže sentence mají **stejné modely**. Intuice: $\forall$ je velká $\wedge$, negace z ní udělá velkou $\vee$ negací (De Morgan).

> [!karta|02]- Proč lze přehodit $\forall x\,\forall y$, ale ne $\exists x\,\forall y$ na $\forall y\,\exists x$?
> Řada stejných kvantifikátorů je jedna velká $\wedge$ (nebo $\vee$) a tu lze přeskládat. U různých se mění, **na čem svědek závisí**: v $\forall y\,\exists x$ smí být pro každé $y$ jiný svědek $x$, v $\exists x\,\forall y$ musí být jeden společný.

> [!karta|03]- Který sémantický důsledek platí mezi $\exists x\,\forall y\,R(x,y)$ a $\forall y\,\exists x\,R(x,y)$ a proč?
> Platí jen **$\exists x\,\forall y\,R(x,y) \models \forall y\,\exists x\,R(x,y)$**: prvek $u_x$, ze kterého vede šipka do všech, je svědkem pro každé $y$. Opačně ne: každý prvek může mít šipku od jiného odesílatele, např. $U = \{0, 1\}$, $[\![R]\!] = \{(0, 1), (1, 0)\}$.

> [!karta|04]- Před kterou spojku lze se zachováním $\models\mid$ vytknout $\forall x$ a před kterou $\exists x$, je-li $x$ v obou podformulích? Proč?
> **$\forall x$ před $\wedge$, $\exists x$ před $\vee$.** $\forall$ je zobecněná konjunkce, takže komutuje jen s $\wedge$; $\exists$ je zobecněná disjunkce, komutuje jen s $\vee$.

> [!karta|05]- Jaký vztah je mezi $\forall x\,P(x) \vee \forall x\,Q(x)$ a $\forall x\,(P(x) \vee Q(x))$?
> Jen **$\forall x\,P(x) \vee \forall x\,Q(x) \models \forall x\,(P(x) \vee Q(x))$**. Levá chce $[\![P]\!] = U$ nebo $[\![Q]\!] = U$, pravá jen $[\![P]\!] \cup [\![Q]\!] = U$. Protipříklad k opačnému směru: $U = \{0, 1, 2\}$, $[\![P]\!] = \{0, 1\}$, $[\![Q]\!] = \{1, 2\}$.

> [!karta|06]- Jaký vztah je mezi $\exists x\,(P(x) \wedge Q(x))$ a $\exists x\,P(x) \wedge \exists x\,Q(x)$?
> Jen **$\exists x\,(P(x) \wedge Q(x)) \models \exists x\,P(x) \wedge \exists x\,Q(x)$** (společný svědek poslouží pro obě části). Opačně ne: svědci pro $P$ a pro $Q$ mohou být různí, např. $[\![P]\!] = \{0\}$, $[\![Q]\!] = \{1\}$.

> [!karta|07]- Jak se dokáže, že $\forall x\,\forall y\,(P(x) \vee Q(y)) \models \forall x\,P(x) \vee \forall y\,Q(y)$?
> Buď model levé strany. Je-li $[\![P]\!] = U$, platí $\forall x\,P(x)$. Jinak existuje $u \notin [\![P]\!]$; při kontextu $x \mapsto u$ a **libovolném** $y \mapsto v$ je $P(x) \vee Q(y)$ pravdivá, $P(x)$ ne, takže $v \in [\![Q]\!]$. Tedy **$[\![Q]\!] = U$** a platí $\forall y\,Q(y)$.

> [!karta|08]- Proč lze $\forall x$ i $\exists x$ vytknout před $\wedge$ i $\vee$, když druhá podformule $\beta$ neobsahuje volné $x$?
> Pravdivost $\beta$ na hodnotě $x$ **nezávisí**, takže se při všech updatech $x$ chová jako konstanta: $(\forall x\,\alpha) \vee \beta$ a $\forall x\,(\alpha \vee \beta)$ obě platí, když platí $\beta$, a jinak obě znamenají $\forall x\,\alpha$.

> [!karta|09]- Co se stane s kvantifikátorem, když ho vytkneme z předpokladu implikace a co ze závěru? Proč?
> Z předpokladu se **otočí**: $(\forall x\,\alpha) \Rightarrow \beta \models\mid \exists x\,(\alpha \Rightarrow \beta)$; ze závěru zůstane: $\beta \Rightarrow \forall x\,\alpha \models\mid \forall x\,(\beta \Rightarrow \alpha)$ ($x$ není volná v $\beta$). Důvod: $\alpha \Rightarrow \beta \models\mid \neg\alpha \vee \beta$ a negace kvantifikátor otočí.

> [!karta|10]- Proč se při převodu do prenexního tvaru nejdřív přejmenují vázané proměnné?
> Aby každý kvantifikátor vázal **jinou proměnnou**. Pak druhá podformule nikdy neobsahuje vytýkanou proměnnou a vytknout jde **cokoliv před $\wedge$ i $\vee$** se zachováním $\models\mid$. Bez přejmenování by se např. z $\forall x\,P(x) \vee \forall x\,Q(x)$ stalo neekvivalentní $\forall x\,(P(x) \vee Q(x))$.

> [!karta|11]- Proč prenexní tvar není jednoznačný a co se při vytýkání nesmí?
> Z levé a pravé podformule lze vytýkat v **libovolném pořadí**, takže vzniknou různé (ekvivalentní) prenexní tvary. **Nesmí se přehodit pořadí kvantifikátorů ze stejné podformule**, protože $\exists$ a $\forall$ spolu nekomutují.

> [!karta|12]- Jak se tautologie, sémantický důsledek a tautologická ekvivalence v predikátové logice převedou na nesplnitelnost?
> - $\varphi$ tautologie ⟺ **$\neg\varphi$ nesplnitelná**
> - $S \models \varphi$ ⟺ **$S \cup \{\neg\varphi\}$ nesplnitelná**
> - $\varphi \models\mid \psi$ ⟺ $\{\varphi, \neg\psi\}$ i $\{\psi, \neg\varphi\}$ nesplnitelné
>
> Proto stačí jedna metoda na nesplnitelnost: rezoluce.

> [!karta|13]- Proč skolemizace zachová jen ekvisplnitelnost, a ne tautologickou ekvivalenci?
> Skolemizovaná sentence říká víc: **konkrétní symbol** je svědek. $P(c) \models \exists x\,P(x)$, ale ne naopak: v $U = \{0, 1\}$, $[\![P]\!] = \{0\}$, $[\![c]\!] = 1$ platí jen $\exists x\,P(x)$. Model původní sentence ale jde vždy **přeinterpretováním nového symbolu** předělat na model skolemizované, takže splnitelnost se zachová.

> [!karta|14]- Proč musí být skolemizační konstanta nový (fresh) symbol?
> Nový symbol smí interpretace vyložit **libovolně**, tedy jako svědka. Starý symbol už význam má a svědkem být nemusí: $\{\exists x\,P(x), \neg P(a)\}$ je splnitelná, ale po nahrazení $x := a$ vznikne nesplnitelná $\{P(a), \neg P(a)\}$.

> [!karta|15]- Proč se $\forall x\,\exists y\,R(x,y)$ skolemizuje funkcí $f(x)$, a ne konstantou?
> Svědek $y$ **závisí na $x$** (pro každé $x$ může být jiný). Konstanta by tvrdila $\forall x\,R(x, c)$, tedy jeden společný svědek, což je silnější $\exists y\,\forall x\,R(x,y)$ a splnitelnost by se mohla ztratit. Arita $f$ = počet $\forall$ před $\exists$.

### Příklady na procvičení

> [!priklad|16]- Je sentence $\forall x\,P(x) \vee \forall x\,\neg P(x)$ tautologie?
> Neplatí: $U = \{0, 1\}$, $[\![P]\!] = \{0\}$. $\forall x\,P(x)$ neplatí (svědek 1), $\forall x\,\neg P(x)$ neplatí (svědek 0). **Není tautologie.** (Tautologie je $\forall x\,P(x) \vee \exists x\,\neg P(x)$.)

> [!priklad|17]- Najdi model sentence $\forall y\,\exists x\,R(x,y)$, který není modelem $\exists x\,\forall y\,R(x,y)$, na tříprvkovém universu.
> $U = \{0, 1, 2\}$, $[\![R]\!] = \{(0, 0), (1, 1), (2, 2)\}$ (rovnost). Do každého $y$ vede šipka sama ze sebe, takže první sentence platí. Žádný prvek ale nemá šipku do všech tří (z 0 nevede do 1, z 1 do 0, z 2 do 0), takže druhá **neplatí**.

> [!priklad|18]- Rozhodni, zda $\exists x\,(P(x) \vee Q(x)) \models\mid \exists x\,P(x) \vee \exists x\,Q(x)$.
> **Platí.** Model levé strany má prvek $u \in [\![P]\!] \cup [\![Q]\!]$, tj. $[\![P]\!] \cup [\![Q]\!] \neq \emptyset$. Model pravé strany má $[\![P]\!] \neq \emptyset$ nebo $[\![Q]\!] \neq \emptyset$, což je totéž. Stejné modely ($\exists$ lze vytknout před $\vee$).

> [!priklad|19]- Zneguj a dostaň negaci k atomům: $\neg\exists x\,\forall y\,(R(x,y) \Rightarrow P(y))$.
> $\forall x\,\neg\forall y\,(R(x,y) \Rightarrow P(y)) \models\mid \forall x\,\exists y\,\neg(\neg R(x,y) \vee P(y)) \models\mid$ **$\forall x\,\exists y\,(R(x,y) \wedge \neg P(y))$**.

> [!priklad|20]- Skolemizuj $\exists x\,\forall y\,\exists z\,(R(x,y) \wedge R(y,z))$.
> Postupně zleva: $x := c$ (nový konstantní symbol, žádné $\forall$ před ním), $z := f(y)$ (nový funkční symbol arity 1). Výsledek **$\forall y\,(R(c,y) \wedge R(y, f(y)))$**, ekvisplnitelný s původní sentencí.

> [!priklad|21]- Je $\forall x\,(P(x) \wedge Q(a))$ klauzule? Pokud ne, rozděl ji na klauzule.
> **Není** (uvnitř je $\wedge$). $\forall x\,(P(x) \wedge Q(a)) \models\mid \forall x\,P(x) \wedge Q(a)$ ($\forall$ se distribuuje pod $\wedge$ jen k podformuli s $x$), klauzule jsou **$\forall x\,P(x)$ a $Q(a)$**.

### Typové příklady na semestrální test

*Stejný typ úloh jako ve starých písemkách k 1. semestrálnímu testu (A. Gollová, 27. 11. 2026, handouty 1–3, 5 a 6). Každé tvrzení zdůvodni; vyvrácení = konkrétní interpretace.*

> [!priklad|22]- Rozhodni, zda platí $\forall x\,(P(x) \Rightarrow Q(x)) \models \forall x\,P(x) \Rightarrow \forall x\,Q(x)$, a zda platí opačný důsledek.
> **Ano.** Buď $(U, [\![-]\!])$ model levé strany: $[\![P]\!] \subseteq [\![Q]\!]$. Pokud $\forall x\,P(x)$ neplatí, implikace vpravo platí. Pokud platí, je $[\![P]\!] = U$, tedy $U \subseteq [\![Q]\!]$ a platí i $\forall x\,Q(x)$.
> **Opačně ne:** $U = \{0, 1\}$, $[\![P]\!] = \{0\}$, $[\![Q]\!] = \emptyset$. Pravá strana platí (předpoklad $\forall x\,P(x)$ je nepravdivý), levá ne ($P(0)$ platí, $Q(0)$ ne).

> [!priklad|23]- Je sentence $\exists x\,(P(x) \Rightarrow \forall y\,P(y))$ tautologie?
> **Ano.** Buď $(U, [\![-]\!])$ libovolná interpretace. Je-li $[\![P]\!] = U$, platí závěr $\forall y\,P(y)$ a svědkem je libovolné $x \in U$ ($U \neq \emptyset$). Je-li $[\![P]\!] \neq U$, zvol svědka $x \mapsto u \notin [\![P]\!]$: předpoklad $P(x)$ je nepravdivý, implikace pravdivá.

> [!priklad|24]- Převeď do prenexního tvaru $\forall x\,P(x) \wedge \neg\forall x\,\exists y\,R(x,y)$.
> 1. Přejmenování: $\forall x\,P(x) \wedge \neg\forall z\,\exists y\,R(z,y)$.
> 2. Negace: $\forall x\,P(x) \wedge \exists z\,\forall y\,\neg R(z,y)$.
> 3. Vytknutí (proměnné se jmenují jinak): **$\forall x\,\exists z\,\forall y\,(P(x) \wedge \neg R(z,y))$**, ekvivalentně např. $\exists z\,\forall y\,\forall x\,(\dots)$; $\exists z$ musí zůstat před $\forall y$.

> [!priklad|25]- Rozhodni, zda je množina $\{\forall x\,\exists y\,R(x,y),\ \forall x\,\neg R(x,x),\ \forall x\,\forall y\,(R(x,y) \Rightarrow \neg R(y,x))\}$ splnitelná.
> **Je.** Model: $U = \{0, 1, 2\}$, $[\![R]\!] = \{(0, 1), (1, 2), (2, 0)\}$ (šipky dokola). Z každého prvku vede šipka, takže platí první sentence; žádná smyčka $(x, x)$, takže platí druhá; k žádné šipce není opačná ($(1, 0)$, $(2, 1)$, $(0, 2) \notin [\![R]\!]$), takže platí i třetí. (Na jedno- ani dvouprvkovém universu model není.)

> [!priklad|26]- Rozhodni, zda $\exists x\,P(x) \wedge \exists x\,Q(x) \models \exists x\,(P(x) \wedge Q(x))$.
> **Neplatí.** $U = \mathbb{N}$, $[\![P]\!] =$ sudá čísla, $[\![Q]\!] =$ lichá čísla. Levá strana platí (svědci 0 a 1), pravá ne, protože žádné číslo není sudé i liché.

---
← [[LGR 09 – Pravdivost formulí, model a tautologie|29. 10. 2026 Pravdivost formulí, model a tautologie]] · [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice|6. 11. 2026 Klauzální tvar a rezolventy v predikátové logice]] →

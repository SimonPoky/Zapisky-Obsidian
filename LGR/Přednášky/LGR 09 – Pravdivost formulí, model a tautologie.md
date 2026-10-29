---
predmet: LGR
prednaska: 9
datum: 2026-10-29
zdroj: "handout 5, slajdy 23–33; handout 6, slajdy 3–7"
tags: [prednaska, LGR]
---

# LGR 09 – Pravdivost formulí, model a tautologie

*Přednáška 9 · čtvrtek 29. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 5 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_5.pdf) · [handout 6 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_6.pdf)

Témata: `jazyk teorie čísel` · `kontext proměnných` · `update kontextu` · `hodnota termu` · `pravdivost formule při kontextu` · `∃ a ∀ přes updaty` · `pravdivost sentence` · `model` · `splnitelná sentence` · `tautologie` · `nemodel`

Minule vznikl jazyk predikátové logiky (termy, formule, volné a vázané proměnné) a [[interpretace]], která symbolům dá význam. Dnes se z toho stane **výpočet pravdivosti**: aby šlo o formuli s volnými proměnnými říct, jestli platí, musí se nejdřív říct, co za ně dosadit (kontext). Kvantifikátory se pak vyhodnocují tak, že se zkouší přepsat hodnotu jedné proměnné (update). Na konci se tím definuje model sentence a, stejně jako ve výrokové logice, splnitelnost a tautologie. Celou dobu běží jeden příklad: čísla s $<$, $0$, $1$, $+$ a $\cdot$.

## §0 Přehled na jedné stránce

| pojem | zápis | co to je | příklad (U = ℕ, ρ: x ↦ 7, y ↦ 15, z ↦ 3) |
|---|---|---|---|
| kontext proměnných | $\rho : \mathrm{Var} \to U$ | co je zrovna dosazeno za každou proměnnou | $\rho(x) = 7$ |
| update | $\rho[x:=d]$ | stejný kontext, jen $x$ přepsáno na $d$ | $\rho[x:=0]$: $x \mapsto 0, y \mapsto 15, z \mapsto 3$ |
| hodnota termu | $[\![t]\!]_\rho \in U$ | který objekt term popisuje | $[\![x + 1]\!]_\rho = 8$ |
| atomická formule | $([\![t_1]\!]_\rho, [\![t_2]\!]_\rho) \in [\![<]\!]$ | dosaď hodnoty, podívej se do relace | $x < 0$: $7 < 0$, nepravdivá |
| $\exists x\,\varphi$ | aspoň jeden update $\rho[x:=d]$ | najdi **svědka** | $\exists y\,(y < x)$: svědek $y := 1$ |
| $\forall x\,\varphi$ | všechny updaty $\rho[x:=d]$ | vyzkoušej **každé** $d \in U$ | $\forall x\,(0 \cdot x = 0)$: $0 \cdot n = 0$ vždy |
| sentence | nezávisí na $\rho$ | stačí interpretace | $\exists x\,(0 < x \wedge x < 1)$ je v ℕ nepravdivá při každém $\rho$ |
| model | $I$, ve které je sentence pravdivá | „svět, kde to platí“ | ℕ je model $\forall x\,(0 \cdot x = 0)$ |
| splnitelná / tautologie | má model / každá $I$ je model | | $\beta$ splnitelná (ℚ), není tautologie (ℕ) |

## §1 Jazyk teorie čísel

Celá přednáška pracuje s jedním [[jazyk predikátové logiky|jazykem]] pro počítání s čísly:

- proměnné $\mathrm{Var} = \{x, y, z\}$ (obecně $x_1, x_2, x_3, \dots$),
- [[predikátový symbol|predikátové symboly]] $\mathrm{Pred} = \{<\}$ (arita 2),
- [[konstantní symbol|konstantní symboly]] $\mathrm{Kons} = \{0, 1\}$,
- [[funkční symbol|funkční symboly]] $\mathrm{Func} = \{+, \cdot\}$ (arita 2, píšou se mezi argumenty: $x + 1$ místo $+(x, 1)$),
- a navíc **logický** predikátový symbol $=$, který je v každém jazyce.

| | příklady |
|---|---|
| [[term|termy]] | $x$, $0$, $x + 1$, $x \cdot (x + 1)$ |
| [[formule predikátové logiky|formule]] | $x < 0$, $x < x + 1$, $x = 0$, $y < x$, $\exists y\,(y < x)$ |
| [[sentence]] | $\exists x\,\big((0 < x) \wedge (x < 1)\big)$, $\forall x\,(0 \cdot x = 0)$ |

$\exists y\,(y < x)$ sentence není: $x$ v ní je [[volná proměnná|volné]].

> [!pozor] Symbol není číslo
> V jazyce jsou $0$, $1$, $+$, $<$ jen **značky**, zatím nic neznamenají. To, že $0$ znamená číslo nula a $+$ sčítání, je až volba interpretace. Jiná interpretace smí $0$ přiřadit číslo 5 nebo prvek $a$ (viz §7). Pevný význam má jen rovnítko.

> [!definice] Logický symbol rovnosti · handout 5, slajdy 26 a 33
> Symbol $=$ (arita 2) je **logický**, ne speciální predikátový symbol. Proto se v každé interpretaci interpretuje stejně, jako skutečná rovnost: formule $t_1 = t_2$ je pravdivá právě tehdy, když $[\![t_1]\!]_\rho = [\![t_2]\!]_\rho$, tedy oba termy označují **tentýž** prvek universa.

^def-rovnost

> [!lidsky] Lidsky
> Všechny ostatní značky si interpretace smí vyložit po svém, rovnítko ne. „Je to totéž“ znamená vždycky totéž.

> [!example] Příklad
> Vezmi klasické ℕ, jen s $[\![0]\!] = 5$. Formule $0 \cdot 1 = 0$ znamená $5 \cdot 1 = 5$ a je pravdivá. Formule $0 + 0 = 0$ znamená $5 + 5 = 5$, tedy $10 = 5$, a je nepravdivá. Kdyby šlo $=$ vyložit třeba jako „$\ge$“, byla by najednou pravdivá ($10 \ge 5$); to definice zakazuje.

## §2 Interpretace jazyka teorie čísel

Připomenutí: [[interpretace]] je dvojice $I = (U, [\![-]\!])$, [[universum]] $U$ a význam každého speciálního symbolu. „Klasická“ interpretace našeho jazyka:

$$
U = \mathbb{N}, \qquad [\![<]\!] = \{(m, n) \in \mathbb{N}^2 : m < n\}, \qquad [\![0]\!] = 0, \qquad [\![1]\!] = 1,
$$

$$
[\![+]\!] : \mathbb{N}^2 \to \mathbb{N} : (m, n) \mapsto m + n, \qquad [\![\cdot]\!] : \mathbb{N}^2 \to \mathbb{N} : (m, n) \mapsto m \cdot n.
$$

Čti: $<$ znamená „být menší“, $+$ sčítání, $\cdot$ násobení. Relace $[\![<]\!]$ je **množina dvojic**, které ve vztahu jsou, např. $(3, 5) \in [\![<]\!]$, $(5, 3) \notin [\![<]\!]$. Přirozená čísla se tu berou včetně nuly.

## §3 Kontext proměnných a update

Interpretace neřekne, kolik je $x$. Formule $x < 0$ proto zatím nemá pravdivostní hodnotu, stejně jako věta „on je vysoký“, dokud nevíš, o kom je řeč.

> [!definice] Kontext proměnných a jeho update · handout 5, slajd 23
> Buď $(U, [\![-]\!])$ interpretace. *[[kontext proměnných|Kontext proměnných]]* je zobrazení $\rho : \mathrm{Var} \to U$, které každé proměnné přiřadí prvek universa.
>
> Je-li $\rho$ kontext, $x \in \mathrm{Var}$ a $d \in U$, pak *[[update kontextu|update]]* $\rho[x:=d] : \mathrm{Var} \to U$ je kontext, který přiřadí proměnné $x$ prvek $d$ a na všech ostatních proměnných se shoduje s $\rho$.

^def-kontext

> [!lidsky] Lidsky
> Kontext je **tabulka dosazení**: u každé proměnné je napsané, za jaké číslo právě stojí. Update je oprava jednoho řádku tabulky, zbytek zůstane. Zápis $\rho[x:=0]$ je stejný jako přiřazení `x = 0` v programu: ostatní proměnné se nezmění.

> [!example] Příklad
> $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$. Pak $\rho' = \rho[x:=0]$ je $x \mapsto 0$, $y \mapsto 15$, $z \mapsto 3$, a $\rho[y:=1]$ je $x \mapsto 7$, $y \mapsto 1$, $z \mapsto 3$. Původní $\rho$ se updatem nemění, update je **nový** kontext.

> [!obrazek] Kontext a jeho update
> ![[lgr09-kontext.png]]
> *Modře kontext $\rho$ (každá proměnná dostane číslo z ℕ), oranžově jediná změna v updatu $\rho[x:=0]$; tečkované šipky ukazují hodnoty, které se převzaly beze změny.*

## §4 Hodnota termu při kontextu

> [!definice] Interpretace termu při kontextu · handout 5, slajd 24
> Pro interpretaci $(U, [\![-]\!])$ a kontext $\rho$ je *[[hodnota termu]]* $t$ prvek $[\![t]\!]_\rho \in U$ určený takto:
>
> - je-li $t$ proměnná $x$: $[\![x]\!]_\rho = \rho(x)$,
> - je-li $t$ konstantní symbol $a$: $[\![a]\!]_\rho = [\![a]\!]$,
> - je-li $t = f(t_1, \dots, t_n)$: $[\![f(t_1, \dots, t_n)]\!]_\rho = [\![f]\!]\big([\![t_1]\!]_\rho, \dots, [\![t_n]\!]_\rho\big)$.

^def-hodnota-termu

> [!lidsky] Lidsky
> Dosaď a spočítej. Proměnnou vezmi z tabulky $\rho$, konstantu ze „slovníku“ interpretace, a funkční symbol nahraď skutečnou operací. Výsledek je **objekt** (číslo), ne pravda či nepravda.

> [!example] Příklad
> V klasické interpretaci na ℕ při $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$:
>
> - $[\![x]\!]_\rho = \rho(x) = 7$,
> - $[\![0]\!]_\rho = [\![0]\!] = 0$ (konstanta na kontextu nezávisí),
> - $[\![x + 1]\!]_\rho = [\![+]\!](7, 1) = 7 + 1 = 8$,
> - $[\![x \cdot (x + 1)]\!]_\rho = 7 \cdot 8 = 56$.

## §5 Pravdivost formule v interpretaci při kontextu

> [!definice] Pravdivost formule v $I$ při $\rho$ · handout 5, slajdy 26–28
> Formule je *pravdivá v interpretaci $I = (U, [\![-]\!])$ při kontextu $\rho$* podle stavby formule:
>
> 1. **Atomická formule.** $P(t_1, \dots, t_n)$ je pravdivá, pokud $([\![t_1]\!]_\rho, \dots, [\![t_n]\!]_\rho) \in [\![P]\!]$; $P$ arity 0 je pravdivá, pokud $[\![P]\!] = 1$; $t_1 = t_2$ je pravdivá, pokud $[\![t_1]\!]_\rho = [\![t_2]\!]_\rho$.
> 2. **Spojky** jako ve výrokové logice: $\neg\varphi$ je pravdivá, právě když $\varphi$ není; $\varphi \wedge \psi$, právě když obě; $\varphi \vee \psi$ je nepravdivá, právě když obě nepravdivé; $\varphi \Rightarrow \psi$ je nepravdivá, právě když $\varphi$ pravdivá a $\psi$ nepravdivá; $\varphi \Leftrightarrow \psi$, právě když mají stejnou hodnotu.
> 3. **Kvantifikátory.** $\forall x\,\varphi$ je pravdivá při $\rho$, pokud je $\varphi$ pravdivá při **každém** updatu $\rho[x:=d]$, $d \in U$. $\exists x\,\varphi$ je pravdivá při $\rho$, pokud je $\varphi$ pravdivá při **aspoň jednom** updatu $\rho[x:=d]$, $d \in U$.

^def-pravdivost-formule

> [!lidsky] Lidsky
> Formule se vyhodnocuje odspodu stromu nahoru, jako ve výrokové logice. Nové jsou jen kvantifikátory: $\exists x$ znamená „**zkus najít** číslo, které za $x$ dosadíš, aby to vyšlo“; $\forall x$ znamená „**ať za $x$ dosadíš cokoli**, musí to vyjít“. Dosazení je právě update: přepíšeš řádek $x$ v tabulce a podformuli vyhodnotíš znovu.

> [!example] Příklad: atomické formule při $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$
> | formule | význam | pravdivost v $I$ při $\rho$ |
> |---|---|---|
> | $x < 0$ | $7 < 0$, neboli $(7, 0) \in [\![<]\!]$? | nepravdivá |
> | $x < x + 1$ | $7 < 8$ | pravdivá |
> | $y < x$ | $15 < 7$ | nepravdivá |
> | $x = 0$ | $7 = 0$ | nepravdivá |
>
> Při kontextu $\rho' = \rho[x:=0]$ by $x = 0$ pravdivá byla: pravdivost formule s volnou proměnnou **závisí na kontextu**.

### §5.1 Existenční kvantifikátor: hledání svědka

Formule $\alpha = \exists y\,\varphi$, kde $\varphi = (y < x)$, při $\rho$: $x \mapsto 7, y \mapsto 15, z \mapsto 3$.

1. Hledá se vhodný update pro $y$: $\rho'' = \rho[y:=\_\,]$, aby $\_ < 7$.
2. Vyhovuje třeba $\rho'' = \rho[y:=1]$: podformule $\varphi$ pak říká $1 < 7 = \rho(x)$, a to platí. Tedy $\varphi$ je pravdivá v $I$ při $\rho''$.
3. Proto je $\alpha$ pravdivá v $I$ při (původním) $\rho$.

Prvek, který se při tom našel (tady $1$), je *[[svědek pravdivosti]]* pro $\alpha$: konkrétní hodnota, která dokazuje, že „existuje“ platí. ^svedek-pravdivosti

> [!navic] Proč nepotřebujeme $\rho(y) = 15$
> $y$ je ve formuli $\alpha$ [[vázaná proměnná|vázaná]]: kvantifikátor $\exists y$ si její hodnotu stejně přepíše updatem, takže původních 15 nehraje roli. Naopak $x$ je volná a $\rho(x) = 7$ potřebujeme: při $\rho(x) = 0$ by svědek neexistoval (žádné přirozené číslo není menší než 0) a $\alpha$ by byla nepravdivá.

### §5.2 Když svědek neexistuje

Sentence $\beta = \exists x\,(0 < x \wedge x < 1)$ v klasické interpretaci na ℕ, podformule $\varphi = (0 < x \wedge x < 1)$.

| zkusený update | $0 < x$ | $\wedge$ | $x < 1$ |
|---|---|---|---|
| $x \mapsto 7$ | $0 < 7$ ano | **ne** | $7 < 1$ ne |

$\varphi$ je nepravdivá v $I$ při $\rho[x:=7]$. To samo o sobě nic nerozhoduje: u $\exists$ jeden nevhodný pokus nestačí. Rozhodne až to, že **vhodný update nejde najít vůbec**: přirozené číslo $n$ s $0 < n < 1$ neexistuje. Proto je $\beta$ nepravdivá v $I$ při $\rho$.

> [!pozor] Jeden neúspěšný pokus nevyvrací „existuje“
> Pro $\exists x\,\varphi$ musíš ukázat, že **žádné** $d \in U$ nevyhovuje (obecným argumentem, ne vyzkoušením pár čísel). Naopak k vyvrácení $\forall x\,\varphi$ stačí jedno $d$, pro které $\varphi$ neplatí.

> [!obrazek] Kvantifikátory jako zkoušení updatů
> ![[lgr09-updaty.png]]
> *Každá buňka je jeden update proměnné na hodnotu $d \in \mathbb{N}$: zeleně podformule platí, červeně ne. Pro $\exists$ stačí jedna zelená buňka (u $\alpha$ např. $d = 1$), pro $\forall$ musí být zelené všechny. U $\beta$ i $\gamma$ jde o nekonečně mnoho buněk, proto se o nich rozhoduje úvahou („pro každé $n$ je $0 \cdot n = 0$“), ne vyzkoušením.*

### §5.3 Obecný kvantifikátor: všechny updaty

Sentence $\gamma = \forall x\,(0 \cdot x = 0)$, podformule $\varphi = (0 \cdot x = 0)$. Musí se vyzkoušet všechny updaty $x \mapsto n \in \mathbb{N}$. Při updatu $\rho[x:=n]$ říká $\varphi$, že $0 \cdot n = 0$, a to je pravda pro každé $n$. Takže $\varphi$ je pravdivá při libovolném updatu $\rho[x:=n]$ a **$\gamma$ je pravdivá v $I$**.

## §6 Pravdivost sentence a model

> [!veta] Pravdivost sentence nezávisí na kontextu · handout 5, slajd 30
> ==Je-li $\varphi$ formule a $I$ interpretace==, pak **pravdivost $\varphi$ v $I$ při $\rho$ závisí jen na hodnotách $\rho$ na volných proměnných $\varphi$.** Speciálně ==je-li $\varphi$ sentence==, je v $I$ **buď pravdivá při každém kontextu, nebo při žádném**: je-li pravdivá při jednom kontextu $\rho$, je pravdivá při každém.

^veta-nezavislost

> [!lidsky] Lidsky
> Kvantifikátor si hodnotu své proměnné vždycky přepíše sám (updatem), takže co v tabulce $\rho$ stálo předtím, je mu jedno. Sentence má všechny proměnné vázané, tedy si přepíše **všechno**, co potřebuje. Výsledek pak určuje jen interpretace, ne tabulka dosazení.

> [!example] Příklad
> $\beta = \exists x\,(0 < x \wedge x < 1)$ je sentence. V ℕ je nepravdivá při $\rho$: $x \mapsto 7$, ale i při $\rho$: $x \mapsto 0$ nebo $x \mapsto 1000$; počáteční hodnotu $x$ kvantifikátor přepíše. Naproti tomu $y < x$ (volné $x$, $y$) je při $x \mapsto 7, y \mapsto 15$ nepravdivá a při $x \mapsto 7, y \mapsto 1$ pravdivá.

> [!definice] Pravdivost sentence v interpretaci a model · handout 5, slajd 31
> Sentence $\varphi$ je *[[pravdivost sentence|pravdivá v interpretaci]]* $I = (U, [\![-]\!])$, jestliže je pravdivá v $I$ při každém kontextu proměnných $\rho$ (podle věty výše stačí ekvivalentně: při aspoň jednom).
>
> Interpretace, ve které je sentence $\varphi$ pravdivá, se nazývá *[[model sentence|model]]* sentence $\varphi$.

^def-model

> [!lidsky] Lidsky
> Model je **svět, ve kterém tvrzení platí**. Stejná sentence může v jednom světě platit a v jiném ne: „mezi 0 a 1 něco leží“ platí v racionálních číslech, ne v přirozených. Interpretace, ve které sentence neplatí, je její „nemodel“ (protipříklad).

> [!example] Příklad
> - Klasické ℕ je model $\gamma = \forall x\,(0 \cdot x = 0)$ (§5.3).
> - Klasické ℕ **není** model $\beta = \exists x\,(0 < x \wedge x < 1)$ (§5.2).
> - $I_2$: $U = \mathbb{Q}$, symboly vyložené stejně (menší, nula, jedna, sčítání, násobení). Pak $\beta$ **je** pravdivá v $I_2$, protože $\varphi$ platí při updatu $x := \tfrac{1}{2}$: $0 < \tfrac{1}{2} < 1$. $I_2$ je model $\beta$.

> [!obrazek] Táž sentence v ℕ a v ℚ
> ![[lgr09-n-vs-q.png]]
> *Oranžový pruh je místo, kde by musel ležet svědek pro $\beta = \exists x\,(0 < x \wedge x < 1)$. V ℕ (nahoře) v něm žádný prvek universa neleží, v ℚ (dole) ano, např. zelené $\tfrac{1}{2}$.*

## §7 Splnitelná sentence, tautologie a nemodel

> [!definice] Splnitelná sentence, tautologie, kontradikce · handout 6, slajd 4
> Sentence je
>
> - *[[splnitelná sentence|splnitelná]]*, jestliže je pravdivá v alespoň jedné interpretaci (má model),
> - *[[tautologie predikátové logiky|tautologie]]*, jestliže je pravdivá v každé interpretaci (každá interpretace je její model),
> - *[[kontradikce predikátové logiky|kontradikce]]*, jestliže je nepravdivá v každé interpretaci (nemá model).

^def-splnitelna-sentence

> [!lidsky] Lidsky
> Stejné tři pojmy jako u [[splnitelná formule|výrokové logiky]], jen místo „řádek pravdivostní tabulky“ (ohodnocení) je „interpretace“. Háček: interpretací je nekonečně mnoho a nejdou vypsat do tabulky, proto se tautologie dokazuje úvahou a „není tautologie“ jedním protipříkladem.

> [!example] Příklad
> $\beta = \exists x\,(0 < x \wedge x < 1)$ je **splnitelná** (model $I_2$ na ℚ), ale **není tautologie**: v klasickém ℕ je nepravdivá. Kontradikce to taky není, protože model má.

### Je $\gamma = \forall x\,(0 \cdot x = 0)$ tautologie?

Klasické ℕ i $I_2$ (ℚ) jsou modely $\gamma$. To ale nestačí: tautologie musí platit v **každé** interpretaci. Stačí tedy vyrobit jeden malý „nemodel“.

$I'$: $U = \{a, b\}$ a

$$
[\![0]\!] = a, \qquad [\![1]\!] = b, \qquad [\![<]\!] = \{(a, b)\}, \qquad [\![+]\!] = \triangle, \qquad [\![\cdot]\!] = *,
$$

kde operace $\triangle, * : U^2 \to U$ jsou dány tabulkami (řádek = levý argument, sloupec = pravý):

| $\triangle$ | $a$ | $b$ |
|---|---|---|
| $a$ | $a$ | $b$ |
| $b$ | $a$ | $b$ |

| $*$ | $a$ | $b$ |
|---|---|---|
| $a$ | $a$ | $b$ |
| $b$ | $b$ | $a$ |

Zkusí se všechny updaty proměnné $x$ (jsou jen dva) a pokaždé se spočítá $\varphi = (0 \cdot x = 0)$, tj. $a * x = a$:

| update | $\varphi$ znamená | výsledek |
|---|---|---|
| $\rho[x:=a]$ | $a * a = a$ | pravda |
| $\rho[x:=b]$ | $a * b = a$, ale $a * b = b$ | **nepravda** |

$\varphi$ neplatí při updatu $x := b$, takže $\gamma$ je nepravdivá v $I'$. **$I'$ není model $\gamma$, a proto $\gamma$ není tautologie.**

> [!navic] Nemodel nemusí být exotický
> Stačí změnit jediný symbol klasické interpretace. $I''$: $U = \mathbb{N}$, všechno klasicky, jen $[\![0]\!] = 5$. Pak $\gamma$ říká „$5 \cdot n = 5$ pro každé $n$“, a to neplatí třeba pro $n = 0$ ($5 \cdot 0 = 0 \ne 5$). $I''$ je taky nemodel $\gamma$. Interpretace smí být „divná“ (5 jako nula, $\max$ jako sčítání); definice předepisuje jen to, aby $[\![+]\!]$ byla všude definovaná s hodnotami v $U$ a aby se $=$ četlo jako rovnost.

> [!lidsky] Proč je „není tautologie“ snazší než „je tautologie“
> Na „není“ stačí **jedna** interpretace, kde sentence neplatí (jako $I'$). Na „je“ musíš obecnou úvahou pokrýt **všechny** interpretace, a těch je nekonečně mnoho. Stejně je snazší ukázat, že sentence je splnitelná (stačí jeden model), než že je kontradikce.

> [!navic] Výhled: kvantifikátory a spojky (handout 6, slajd 18)
> Protože $\forall$ je „konjunkce přes všechny prvky“ a $\exists$ „disjunkce přes všechny prvky“, platí $\forall x\,P(x) \wedge \forall x\,Q(x) \mathrel{\vert\!=\!\vert} \forall x\,(P(x) \wedge Q(x))$ a $\exists x\,P(x) \vee \exists x\,Q(x) \mathrel{\vert\!=\!\vert} \exists x\,(P(x) \vee Q(x))$, kdežto opačné kombinace platí jen jedním směrem, např. $\forall x\,P(x) \vee \forall x\,Q(x) \models \forall x\,(P(x) \vee Q(x))$. Podrobně příště.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Co v predikátové logice hraje roli ohodnocení z výrokové logiky a proč nestačí samotná interpretace?
> **Interpretace + kontext.** Interpretace řekne, co znamenají symboly, ale ne, za co stojí volné proměnné; to doplní kontext $\rho$. U sentencí stačí interpretace sama.

> [!karta|02]- Jak se liší postup ověření $\exists x\,\varphi$ a $\forall x\,\varphi$ v interpretaci $I$ při $\rho$?
> $\exists$: stačí najít **jeden** update $\rho[x:=d]$, při kterém $\varphi$ platí (svědek). $\forall$: $\varphi$ musí platit při **každém** updatu $\rho[x:=d]$, $d \in U$.

> [!karta|03]- Co stačí k vyvrácení $\forall x\,\varphi$ a co je potřeba k vyvrácení $\exists x\,\varphi$?
> $\forall$: **jedno** $d$, pro které $\varphi$ neplatí. $\exists$: ukázat, že $\varphi$ neplatí pro **žádné** $d \in U$; jeden nevhodný pokus (např. $x \mapsto 7$ u $\exists x\,(0 < x \wedge x < 1)$) nestačí.

> [!karta|04]- Proč ve formuli $\exists y\,(y < x)$ nehraje roli $\rho(y)$, ale $\rho(x)$ ano?
> $y$ je **vázaná**: kvantifikátor její hodnotu přepíše updatem. $x$ je **volná**: její hodnota zůstává, při $\rho(x) = 7$ je formule v ℕ pravdivá, při $\rho(x) = 0$ ne.

> [!karta|05]- Proč pravdivost sentence nezávisí na kontextu (myšlenka)?
> Každá proměnná sentence je **vázaná**, takže si ji kvantifikátor při vyhodnocení přepíše updatem. Původní hodnoty v $\rho$ se nikdy nepoužijí; výsledek určuje jen **interpretace**.

> [!karta|06]- Proč je jedno, jestli definujeme „sentence je pravdivá v $I$“ jako „při každém kontextu“, nebo „při aspoň jednom kontextu“?
> Sentence je v dané interpretaci **buď pravdivá při všech kontextech, nebo při žádném** (nezávisí na kontextu). Obě definice proto dají tentýž pojem.

> [!karta|07]- Proč se splnitelnost, tautologie a model definují jen pro sentence?
> Pravdivost formule s **volnou proměnnou** závisí i na kontextu, ne jen na interpretaci (např. $x = 0$). U sentence určuje pravdivost interpretace sama, takže má smysl ptát se, ve kterých interpretacích platí.

> [!karta|08]- Může být táž sentence v jedné interpretaci pravdivá a v jiné nepravdivá? Příklad.
> **Ano**, pravdivost je vždy „pravdivá **v** $I$“. $\exists x\,(0 < x \wedge x < 1)$ je nepravdivá v klasickém ℕ a pravdivá v ℚ (svědek $\tfrac{1}{2}$).

> [!karta|09]- Proč je snazší dokázat, že sentence **není** tautologie, než že **je**?
> Na „není“ stačí **jedna** interpretace, kde neplatí (nemodel). Na „je“ musíš obecnou úvahou pokrýt **všechny** interpretace, a těch je nekonečně mnoho.

> [!karta|10]- Proč smí interpretace vyložit $0$ jako 5 nebo $+$ jako $\max$, ale $=$ musí být vždy rovnost?
> $0$ a $+$ jsou **speciální** symboly, jejich význam volí interpretace (stačí, aby $[\![+]\!]$ byla všude definovaná a mířila do $U$). $=$ je **logický** symbol s pevným významem „tentýž prvek universa“.

> [!karta|11]- Jaký je vztah mezi tautologií, splnitelnou sentencí a kontradikcí?
> Každá **tautologie je splnitelná** (interpretace existují). $\varphi$ je tautologie, právě když $\neg\varphi$ je **kontradikce** ($\neg\varphi$ je nepravdivá přesně tam, kde je $\varphi$ pravdivá).

### Příklady na procvičení

> [!priklad|12]- V klasické interpretaci na ℕ při $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$ spočítej $[\![x \cdot (x + 1)]\!]_\rho$ a $[\![(y + 1) \cdot z]\!]_\rho$.
> $[\![x \cdot (x + 1)]\!]_\rho = 7 \cdot (7 + 1) = $ **56**, $[\![(y + 1) \cdot z]\!]_\rho = (15 + 1) \cdot 3 = $ **48**.

> [!priklad|13]- V klasické interpretaci na ℕ při $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$ rozhodni pravdivost: $z \cdot z < x + 1$, $\;x + z \cdot z = y + 1$.
> $z \cdot z < x + 1$ znamená $9 < 8$: **nepravdivá**. $x + z \cdot z = y + 1$ znamená $7 + 9 = 16$: **pravdivá** (rovnítko: oba termy dávají tentýž prvek 16).

> [!priklad|14]- Je $\exists y\,(y < x)$ pravdivá v klasickém ℕ při kontextu $\rho' = \rho[x:=0]$?
> Hledá se $d \in \mathbb{N}$ s $d < 0$. Takové přirozené číslo neexistuje, svědek není. Formule je **nepravdivá** (při $\rho(x) = 7$ byla pravdivá: závisí na volném $x$).

> [!priklad|15]- Je $\exists z\,(x < z \wedge z < y)$ pravdivá v klasickém ℕ při $\rho$: $x \mapsto 7$, $y \mapsto 15$, $z \mapsto 3$?
> Update $\rho[z:=8]$: $7 < 8$ a $8 < 15$, obojí platí. Svědek $z = 8$, formule je **pravdivá**. Původní $\rho(z) = 3$ nehraje roli ($z$ je vázaná).

> [!priklad|16]- Je klasické ℕ modelem sentence $\forall x\,\exists y\,(x < y)$? A sentence $\exists y\,\forall x\,(x < y)$?
> První: pro každé $n$ je svědek $y := n + 1$, takže **ano, model**. Druhá: pro každé $m$ selže update $x := m$ ($m < m$ neplatí), takže **není model**. Pořadí kvantifikátorů mění význam.

> [!priklad|17]- Interpretace: $U = \{0, 1\}$, $[\![<]\!] = \{(0, 1)\}$, $[\![1]\!] = 1$, $[\![+]\!](m, n) = \max(m, n)$. Je modelem sentence $\forall x\,(x < x + 1)$?
> Update $x := 1$: $[\![x + 1]\!] = \max(1, 1) = 1$ a formule říká $(1, 1) \in [\![<]\!]$, což **neplatí**. Jeden neúspěšný update vyvrací $\forall$: **není model**.

### Typové příklady na semestrální test

*Stejný typ úloh jako ve starších písemkách z LGR: rozhodnout o splnitelnosti nebo tautologii a doložit to modelem (universum + interpretace každého symbolu), nebo protipříkladem. Každé tvrzení je potřeba zdůvodnit.*

> [!priklad|18]- Rozhodni, zda je sentence $\forall x\,\exists y\,(x < y)$ splnitelná a zda je tautologie.
> **Splnitelná:** model $U = \mathbb{N}$, $[\![<]\!]$ = „menší“, svědek pro $x := n$ je $y := n + 1$. **Není tautologie:** v interpretaci $U = \{a\}$, $[\![<]\!] = \emptyset$ selže update $x := a$, protože jediný kandidát $y := a$ dá $(a, a) \notin [\![<]\!]$. Ostatní symboly jazyka ($0$, $1$, $+$, $\cdot$) se tam interpretují jako $a$, resp. $(a, a) \mapsto a$.

> [!priklad|19]- Je sentence $\forall x\,(x \cdot 1 = x)$ v jazyce teorie čísel tautologie?
> **Není.** Model je klasické ℕ ($n \cdot 1 = n$). Nemodel: $U = \mathbb{N}$, vše klasicky, jen $[\![\cdot]\!]$ = sčítání. Update $x := 0$: $0 + 1 = 1 \ne 0$, formule $x \cdot 1 = x$ neplatí, tedy sentence je **nepravdivá** v této interpretaci.

> [!priklad|20]- Je sentence $\exists x\,(x < 0)$ v jazyce teorie čísel splnitelná?
> V klasickém ℕ nepravdivá (žádné $n < 0$), ale to nic nerozhoduje. Model: $U = \mathbb{Z}$, symboly vyložené klasicky (menší, nula, jedna, sčítání, násobení, všechny operace vrací celé číslo); svědek $x := -1$, $-1 < 0$. Sentence je **splnitelná**.

> [!priklad|21]- Je sentence $\forall x\,(x = x)$ tautologie?
> **Ano.** V libovolné interpretaci $(U, [\![-]\!])$ a při libovolném updatu $x := d$ říká formule $x = x$, že $d = d$. Rovnítko je logický symbol a znamená vždy skutečnou rovnost, takže to platí pro každé $d \in U$ v každé interpretaci.

---
← [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky|23. 10. 2026 Dokončení úplnosti a syntaxe predikátové logiky]]

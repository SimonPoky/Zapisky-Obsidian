---
predmet: MA1
prednaska: 10
datum: 2026-10-22
zdroj: "Handout 4B (Derivace, monotonie a extrémy), slajdy 11–19"
tags: [prednaska, MA1]
---

# MA1 10 – Druhá derivace, konvexita a inflexe

*Přednáška 10 · čtvrtek 22. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 4B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout04b.pdf)

Témata: `znaménko f′ v praxi` · `extrém ze změny monotonie` · `x³ − 6x² + 10` · `extrémy pomocí f″` · `f″(p) = 0: cokoli` · `konvexní a konkávní funkce` · `konvexita pomocí f′ a f″` · `inflexní bod` · `f″(p) = 0 v inflexi` · `Weierstrassova funkce`

Minule se ukázalo, že znaménko $f'$ na otevřeném intervalu určuje monotonii. Dnes se to použije v praxi: z tabulky znamének $f'$ se přečtou intervaly monotonie i lokální extrémy. Pak přijde ke slovu druhá derivace: ve stacionárním bodě rozhodne o minimu a maximu, popíše, jestli je graf prohnutý nahoru (konvexní) nebo dolů (konkávní), a najde inflexní body, kde se prohnutí mění.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| monotonie v praxi | $I$ otevřený, $f'$ na $I$ | $f' > 0$ ⇒ rostoucí, $f' < 0$ ⇒ klesající ($\ge$, $\le$ ⇒ neklesající, nerostoucí) |
| extrém ze změny monotonie | $f$ nerostoucí vlevo od $p$, neklesající vpravo | lokální minimum v $p$ (obráceně maximum) |
| extrém pomocí $f''$ | $f'(p) = 0$, $f''(p)$ existuje | $f''(p) > 0$ ⇒ ostré minimum, $f''(p) < 0$ ⇒ ostré maximum, $f''(p) = 0$ ⇒ cokoli |
| konvexní na $I$ | | $f(ax_1 + (1 - a)x_2) \le af(x_1) + (1 - a)f(x_2)$: tětiva nad grafem |
| konvexita a $f'$ | $f'$ na otevřeném $I$ | konvexní $\iff f'$ neklesající; ryze konvexní $\iff f'$ rostoucí |
| konvexita a $f''$ | $f''$ na otevřeném $I$ | $f'' \ge 0$ ⇒ konvexní, $f'' > 0$ ⇒ ryze konvexní (jen jedním směrem) |
| inflexní bod | $f'$ na otevřeném $I$ | $f'$ má v $p$ ostrý lokální extrém; tam se mění ryzí konvexita v ryzí konkávnost |
| nutná podmínka inflexe | $f''$ na $I$, inflexe v $p$ | $f''(p) = 0$ (obráceně neplatí: $x^4$) |

## §1 Monotonie a extrémy v praxi

Z [[věta o znaménku derivace a monotonii|věty o znaménku derivace a monotonii]] (handout 4B, slajd 10) plyne jednoduchý recept. Ať $I$ je otevřený interval a $f$ má derivaci na $I$:

- $f' \ge 0$ na $I$ ⇒ $f$ je na $I$ [[neklesající funkce|neklesající]]; $f' > 0$ na $I$ ⇒ $f$ je na $I$ **rostoucí**;
- $f' \le 0$ na $I$ ⇒ $f$ je na $I$ nerostoucí; $f' < 0$ na $I$ ⇒ $f$ je na $I$ **klesající**.

> [!veta] Lokální extrém ze změny monotonie · handout 4B, slajd 11
> Ať ==$f$ je definována na okolí bodu $p$==.
>
> 1. Je-li $f$ **nerostoucí na levém** a **neklesající na pravém** okolí $p$, má $f$ v $p$ **lokální minimum**.
> 2. Je-li $f$ **neklesající na levém** a **nerostoucí na pravém** okolí $p$, má $f$ v $p$ **lokální maximum**.
>
> Pro ostré extrémy platí totéž s klesající/rostoucí místo nerostoucí/neklesající.

^veta-extrem-zmena-monotonie

> [!lidsky] Lidsky
> Když jdeš z kopce a pak do kopce, v místě obratu jsi na dně. V praxi: [[stacionární bod]], kde $f'$ mění znaménko z $-$ na $+$, je minimum, z $+$ na $-$ maximum. Když se znaménko nemění (jako u $x^3$ v nule), extrém tam není.

### Příklad: $f(x) = x^3 - 6x^2 + 10$ · handout 4B, slajd 12

> [!example] Intervaly monotonie a lokální extrémy
> $f'(x) = 3x^2 - 12x = 3x(x - 4)$. Součin dvou činitelů je kladný, když mají stejné znaménko:
> $$
> f'(x) > 0 \iff (x > 0 \ \&\ x - 4 > 0) \ \text{nebo}\ (x < 0 \ \&\ x - 4 < 0) \iff x \in (-\infty; 0) \cup (4; +\infty).
> $$
> - Na každém z intervalů $(-\infty; 0)$ a $(4; +\infty)$ je $f$ **rostoucí**.
> - $f'(x) < 0 \iff x \in (0; 4)$, takže na $(0; 4)$ je $f$ **klesající**.
> - $f'(x) = 0 \iff x \in \{0, 4\}$. V $0$ se rostoucí mění v klesající: **ostré lokální maximum** $f(0) = 10$. Ve $4$ naopak: **ostré lokální minimum** $f(4) = 64 - 96 + 10 = -22$.

> [!obrazek] Graf $x^3 - 6x^2 + 10$ a znaménko derivace
> ![[ma110-monotonie-priklad.png]]
> *Nahoře graf: zeleně úseky, kde f roste, červeně kde klesá, modře lokální extrémy. Dole f′(x) = 3x(x − 4): zelená plocha f′ > 0, červená f′ < 0.*

> [!pozor] Rostoucí na sjednocení
> Správně je „$f$ roste na $(-\infty; 0)$ a na $(4; +\infty)$“, ne „$f$ roste na $(-\infty; 0) \cup (4; +\infty)$“. Věta mluví o intervalu, a tady by to navíc bylo špatně: $f(-1) = 3 > -22 = f(4)$.

## §2 Lokální extrémy pomocí druhé derivace

> [!veta] Lokální extrémy pomocí druhé derivace · handout 4B, slajd 13
> Ať ==$p$ je [[stacionární bod]] funkce $f$ ležící uvnitř intervalu $I$ a ať $f''(p)$ existuje==. Potom:
>
> 1. je-li $f''(p) > 0$, má $f$ v $p$ **ostré lokální minimum**;
> 2. je-li $f''(p) < 0$, má $f$ v $p$ **ostré lokální maximum**.
>
> Pokud $f''(p) = 0$, může se stát cokoli.
>
> > [!note]- Důkaz (1)
> > Chceme $\delta > 0$ tak, aby $f(p) < f(x)$ pro všechna $x \in (p - \delta; p) \cup (p; p + \delta)$.
> >
> > Protože $f'(p) = 0$, je
> > $$
> > f''(p) = \lim_{x \to p} \frac{f'(x) - f'(p)}{x - p} = \lim_{x \to p} \frac{f'(x)}{x - p} > 0.
> > $$
> > Podle [[věta o znaménku limity|věty o znaménku limity]] existuje $\delta > 0$ takové, že $\frac{f'(t)}{t - p} > 0$ pro všechna $t \neq p$ z $(p - \delta; p + \delta)$. Tedy **$f'(t) < 0$ pro $t < p$** a **$f'(t) > 0$ pro $t > p$** (zmenšením $\delta$ navíc $f'$ existuje na celém okolí, protože $f''(p)$ existuje).
> >
> > Vezmi $x \in (p; p + \delta)$. Podle [[Lagrangeova věta|Lagrangeovy věty]] je $\frac{f(x) - f(p)}{x - p} = f'(t)$ pro nějaké $t$ mezi $p$ a $x$, tedy $t > p$ a $f'(t) > 0$. Protože $x - p > 0$, je **$f(x) - f(p) > 0$**. Pro $x \in (p - \delta; p)$ je $t < p$, $f'(t) < 0$ a $x - p < 0$, takže zase $f(x) - f(p) > 0$. Obojí dohromady: $f(p) < f(x)$, ostré lokální minimum.
> >
> > (2) plyne z (1) pro $-f$.

^veta-extrem-druha-derivace

> [!lidsky] Lidsky
> Ve stacionárním bodě je tečna vodorovná a $f''(p) > 0$ říká, že sklon $f'$ v tom místě **roste**: vlevo graf klesá, vpravo stoupá, jsi na dně. $f''(p) < 0$ je opak, vrchol kopce. Je to rychlejší test než tabulka znamének $f'$, ale ne vždy rozhodne.

> [!obrazek] Test druhou derivací
> ![[ma110-druha-derivace.png]]
> *Vlevo: oranžová f′ prochází nulou v p rostoucím směrem (f″(p) > 0), takže modrá f vlevo klesá a vpravo roste: minimum. Vpravo: všechny tři funkce mají v 0 nulovou první i druhou derivaci; zelená x⁴ má minimum, červená −x⁴ maximum, modrá x³ žádný extrém.*

> [!pozor] $f''(p) = 0$ nic neříká
> Test ve stacionárním bodě s $f''(p) = 0$ **mlčí**: $x^4$ má v $0$ minimum, $-x^4$ maximum a $x^3$ žádný extrém, a všechny tři mají $f'(0) = f''(0) = 0$. Pak se musí rozhodnout jinak, třeba znaménkem $f'$ kolem $p$ (§1).

## §3 Konvexní a konkávní funkce

> [!definice] Konvexní a ryze konvexní funkce · handout 4B, slajd 14
> Ať $f$ je definována na otevřeném intervalu $I$. Funkce $f$ je **konvexní** na $I$, pokud pro všechna $x_1, x_2 \in I$ a všechna $a \in [0; 1]$ platí
> $$
> f\bigl(a x_1 + (1 - a) x_2\bigr) \le a f(x_1) + (1 - a) f(x_2).
> $$
> Funkce $f$ je **ryze konvexní** na $I$, pokud platí ostrá nerovnost $<$ pro všechna $x_1 \neq x_2$ z $I$ a všechna $a \in (0; 1)$.

^def-konvexni

> [!lidsky] Lidsky
> [[konvexní funkce|Konvexní]] graf je prohnutý nahoru jako miska: tětiva mezi libovolnými dvěma body grafu leží **nad grafem** (nebo na něm). Bod $a x_1 + (1 - a) x_2$ projede pro $a$ od $1$ do $0$ celý úsek od $x_1$ do $x_2$ ($a = \frac{1}{2}$ je střed) a $a f(x_1) + (1 - a) f(x_2)$ je výška tětivy nad ním. [[ryze konvexní funkce|Ryze konvexní]] graf nemá žádný rovný kus, tětiva je přísně nad ním.

> [!definice] Konkávní a ryze konkávní funkce · handout 4B, slajd 15
> Otočením nerovností dostaneme pojmy **konkávní** ($\ge$) a **ryze konkávní** ($>$ pro $x_1 \neq x_2$, $a \in (0; 1)$). Šetření práce: $f$ je (ryze) konvexní na $I$, právě když $-f$ je (ryze) konkávní na $I$.

^def-konkavni

> [!lidsky] Lidsky
> [[konkávní funkce|Konkávní]] graf je prohnutý dolů jako kopec, tětiva je pod ním. [[ryze konkávní funkce|Ryze konkávní]] je kopec bez rovných úseků. Přímka je konvexní i konkávní zároveň, ale ani ryze konvexní, ani ryze konkávní.

> [!obrazek] Tětiva nad grafem
> ![[ma110-konvexita.png]]
> *Nahoře: oranžová tětiva mezi body x₁ a x₂ leží nad modrým grafem; v bodě ax₁ + (1 − a)x₂ je výška tětivy (oranžový bod) aspoň f v tom bodě (modrý bod). Dole: zeleně ryze konvexní a konvexní funkce (ta má rovný úsek), červeně ryze konkávní a konkávní.*

> [!pozor] Ostrá nerovnost jen pro $x_1 \neq x_2$ a $a \in (0; 1)$
> Pro $a = 0$, $a = 1$ nebo $x_1 = x_2$ jsou obě strany definice **stejné** (obě rovné $f(x_1)$ nebo $f(x_2)$). Ostrá nerovnost proto nemůže platit „pro všechna $a \in [0; 1]$“; v definici ryzí konvexity se tyto triviální případy vynechávají.

## §4 Konvexita pomocí derivací

> [!veta] Konvexita pomocí monotonie první derivace · handout 4B, slajd 16
> Ať ==$f$ má první derivaci na otevřeném intervalu $I$==. Potom
>
> 1. **$f$ je konvexní na $I$, právě když $f'$ je neklesající na $I$**;
> 2. **$f$ je ryze konvexní na $I$, právě když $f'$ je rostoucí na $I$**.
>
> Analogicky: konkávní $\iff f'$ nerostoucí, ryze konkávní $\iff f'$ klesající. Důkaz se zde neuvádí.

^veta-konvexita-prvni-derivace

> [!lidsky] Lidsky
> Na misce se sklon tečny zleva doprava jen zvětšuje: vlevo klesá prudce, na dně je vodorovná, vpravo stoupá čím dál víc. Konvexita je tedy „monotonie směrnice tečny“.

> [!veta] Konvexita pomocí druhé derivace · handout 4B, slajd 16 (důsledek)
> Ať ==$f$ má druhou derivaci na otevřeném intervalu $I$==. Potom
>
> 1. **je-li $f'' \ge 0$ na $I$, je $f$ konvexní na $I$**;
> 2. **je-li $f'' > 0$ na $I$, je $f$ ryze konvexní na $I$**.
>
> Analogicky $f'' \le 0$ ⇒ konkávní, $f'' < 0$ ⇒ ryze konkávní.
>
> > [!note]- Důkaz
> > $f''$ je derivace $f'$. Podle [[věta o znaménku derivace a monotonii|věty o znaménku derivace a monotonii]] (pro funkci $f'$) z $f'' \ge 0$ plyne, že $f'$ je neklesající, a z $f'' > 0$, že $f'$ je rostoucí. Zbytek je předchozí tvrzení.

^veta-konvexita-druha-derivace

> [!lidsky] Lidsky
> V praxi se konvexita skoro vždy ověřuje takhle: spočítáš $f''$ a podíváš se na její znaménko. $f(x) = x^2$: $f'' = 2 > 0$, ryze konvexní všude.

> [!pozor] Jen jedním směrem
> $f'' > 0$ je **postačující**, ne nutná podmínka ryzí konvexity. $f(x) = x^4$ je ryze konvexní na $\mathbb{R}$ ($f'(x) = 4x^3$ je rostoucí), ale $f''(0) = 0$.

## §5 Inflexní bod

> [!definice] Inflexní bod · handout 4B, slajd 17
> Ať $I$ je otevřený interval a $f$ má první derivaci na $I$. Bod $p \in I$ je **inflexní bod** funkce $f$, pokud má $f'$ v bodě $p$ [[ostrý lokální extrém]].

^def-inflexni-bod

> [!lidsky] Lidsky
> [[inflexní bod|Inflexní bod]] je místo, kde se graf „přehne“: ryzí konkávnost se mění v ryzí konvexitu nebo naopak. Silnice, která zatáčí doleva a v jednom bodě začne zatáčet doprava. Definice to říká přes $f'$: sklon tečny tam přestane růst a začne klesat (nebo obráceně), takže $f'$ má v $p$ extrém.

> [!obrazek] Inflexní bod
> ![[ma110-inflexe.png]]
> *Nahoře graf f: červeně ryze konkávní část, zeleně ryze konvexní, modře inflexní bod p. Dole oranžově f′: v inflexním bodě má ostré lokální minimum (vlevo) nebo maximum (vpravo).*

> [!veta] Nutná podmínka inflexe · handout 4B, slajd 18
> Ať ==$I$ je otevřený interval a $f$ má druhou derivaci na $I$==. Má-li $f$ inflexi v bodě $p \in I$, je **$f''(p) = 0$**, tedy $p$ je stacionární bod funkce $f'$.
>
> > [!note]- Důkaz
> > Inflexe v $p$ znamená, že $f'$ má v $p$ ostrý lokální extrém. Funkce $f'$ má v $p$ derivaci $f''(p)$, takže podle [[nutná podmínka lokálního extrému|nutné podmínky lokálního extrému]] (použité na $f'$) je $(f')'(p) = f''(p) = 0$.

^veta-nutna-podminka-inflexe

> [!lidsky] Lidsky
> Kandidáti na inflexi jsou nulové body $f''$, stejně jako kandidáti na extrém jsou nulové body $f'$. A stejně jako tam je každého kandidáta potřeba ověřit.

> [!pozor] Obráceně neplatí
> $f(x) = x^4$: $f''(0) = 0$, ale **$0$ není inflexní bod**. $f'(x) = 4x^3$ je rostoucí, takže v $0$ nemá extrém, a $f$ je ryze konvexní na celém $\mathbb{R}$. Ověř změnu znaménka $f''$ kolem kandidáta.

## §6 Patologie: Weierstrassova funkce

> [!navic] Spojitá, ale nikde monotónní · handout 4B, slajd 19
> Funkce $f(x) = \sum_{n=0}^{+\infty} b^n \cos(a^n \pi x)$, kde $a$ je liché číslo, $b \in (0; 1)$ a $ab > 1 + \frac{3}{2}\pi$, je **spojitá v každém bodě**, ale **nemá derivaci v žádném bodě** a **není rostoucí ani klesající na žádném intervalu**. Celá teorie z této přednášky ji tedy vůbec nezachytí: věty o derivacích fungují jen pro funkce, které derivaci mají. Mimo zkouškovou látku.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jak ze znaménka $f'$ kolem stacionárního bodu $p$ poznáš, jestli je v $p$ lokální extrém?
> Změna z **$-$ na $+$**: $f$ vlevo klesá a vpravo roste, **minimum**. Z **$+$ na $-$**: **maximum**. Bez změny znaménka (třeba $x^3$ v $0$) **extrém není**.

> [!karta|02]- Co se dá říct o stacionárním bodě $p$, ve kterém $f''(p) = 0$? Uveď příklady.
> **Nic**, test druhou derivací mlčí. $x^4$ má v $0$ **minimum**, $-x^4$ **maximum**, $x^3$ **žádný extrém**; všechny mají $f'(0) = f''(0) = 0$.

> [!karta|03]- Dokaž: je-li $f'(p) = 0$ a $f''(p) > 0$, má $f$ v $p$ ostré lokální minimum.
> $f''(p) = \lim_{x \to p} \frac{f'(x)}{x - p} > 0$, takže podle **věty o znaménku limity** je **$f' < 0$ vlevo a $f' > 0$ vpravo** od $p$ na nějakém okolí. **Lagrange**: $f(x) - f(p) = f'(t)(x - p)$ s $t$ mezi $p$ a $x$; vpravo $f'(t) > 0$ a $x - p > 0$, vlevo oba záporné. Vždy $f(x) > f(p)$.

> [!karta|04]- Proč stačí dokázat jen případ $f''(p) > 0$ (minimum)?
> **Šetření práce**: $f$ má v $p$ ostré lokální maximum, právě když **$-f$ má ostré lokální minimum**, a $(-f)''(p) = -f''(p) > 0$, když $f''(p) < 0$.

> [!karta|05]- V důkazu testu druhou derivací se používá Lagrangeova věta na okolí $p$. Proč tam $f'$ existuje, když předpoklad mluví jen o $f''(p)$?
> $f''(p)$ je limita podílů $\frac{f'(x) - f'(p)}{x - p}$, takže **$f'$ musí být definována na okolí $p$**. Z existence $f'$ na okolí plyne i spojitost $f$ tam, takže Lagrange jde použít.

> [!karta|06]- Co geometricky znamená nerovnost $f(ax_1 + (1 - a)x_2) \le af(x_1) + (1 - a)f(x_2)$?
> Bod $ax_1 + (1 - a)x_2$ projíždí pro $a \in [0; 1]$ úsek od $x_2$ do $x_1$; pravá strana je výška **tětivy** spojující $(x_1; f(x_1))$ a $(x_2; f(x_2))$ nad tímto bodem. Nerovnost říká, že **tětiva leží nad grafem**.

> [!karta|07]- Proč se v definici ryzí konvexity požaduje $x_1 \neq x_2$ a $a \in (0; 1)$, a ne všechna $a \in [0; 1]$?
> Pro **$a = 0$, $a = 1$ nebo $x_1 = x_2$** jsou obě strany **stejné**, takže ostrá nerovnost tam nikdy neplatí. Bez vynechání těchto případů by žádná funkce ryze konvexní nebyla.

> [!karta|08]- Plyne z ryzí konvexity $f$ na $I$, že $f'' > 0$ na $I$? Protipříklad.
> **Neplyne.** $f(x) = x^4$ je ryze konvexní na $\mathbb{R}$ ($f' = 4x^3$ je rostoucí), ale **$f''(0) = 0$**. Podmínka $f'' > 0$ je jen postačující.

> [!karta|09]- Proč z $f'' \ge 0$ na otevřeném intervalu $I$ plyne, že $f$ je konvexní na $I$?
> $f''$ je derivace $f'$, takže podle **věty o znaménku derivace a monotonii** je **$f'$ neklesající**. A $f$ s neklesající $f'$ je podle **tvrzení o konvexitě pomocí první derivace** konvexní.

> [!karta|10]- Dokaž: má-li $f$ (s druhou derivací na $I$) inflexi v $p$, je $f''(p) = 0$.
> Inflexe znamená, že **$f'$ má v $p$ ostrý lokální extrém**. $f'$ má v $p$ derivaci $f''(p)$, takže podle **nutné podmínky lokálního extrému** pro funkci $f'$ je $f''(p) = 0$.

> [!karta|11]- Plyne z $f''(p) = 0$, že $p$ je inflexní bod? Protipříklad.
> **Neplyne.** $f(x) = x^4$: $f''(0) = 0$, ale $f'(x) = 4x^3$ je rostoucí, takže **$f'$ nemá v $0$ extrém** a $0$ není inflexní bod ($f$ je ryze konvexní všude).

> [!karta|12]- Jak souvisí inflexní bod se změnou konvexity a konkávnosti?
> V typickém případě, kdy má $f'$ v $p$ ostré minimum, $f'$ vlevo od $p$ klesá a vpravo roste, takže $f$ je vlevo **ryze konkávní** a vpravo **ryze konvexní**. V inflexi se prohnutí grafu **mění** (konkávní ↔ konvexní).

> [!karta|13]- Jaký je postup, jak najít intervaly monotonie a lokální extrémy funkce s derivací na $\mathbb{R}$?
> 1. Spočítej $f'$ a **rozlož ji na součin**. 2. Najdi **nulové body** $f'$ (stacionární body). 3. Urči **znaménko $f'$** na intervalech mezi nimi: $f' > 0$ rostoucí, $f' < 0$ klesající. 4. Kde se znaménko **mění**, je extrém (nebo použij $f''$).

### Příklady na procvičení

> [!priklad|14]- Urči intervaly monotonie a lokální extrémy funkce $f(x) = x^3 - 6x^2 + 10$ na $\mathbb{R}$.
> $f'(x) = 3x(x - 4)$: $f' > 0$ na $(-\infty; 0)$ a $(4; +\infty)$, kde $f$ **roste**; $f' < 0$ na $(0; 4)$, kde $f$ **klesá**. **Ostré lokální maximum** $f(0) = 10$, **ostré lokální minimum** $f(4) = -22$.

> [!priklad|15]- Rozhodni testem druhou derivací o stacionárních bodech funkce $f(x) = x^3 - 6x^2 + 10$.
> Stacionární body $0$ a $4$, $f''(x) = 6x - 12$. $f''(0) = -12 < 0$: **ostré lokální maximum** v $0$. $f''(4) = 12 > 0$: **ostré lokální minimum** ve $4$.

> [!priklad|16]- Urči intervaly konvexity a konkávnosti a inflexní body funkce $f(x) = x^3 - 6x^2 + 10$.
> $f''(x) = 6x - 12$. $f'' < 0$ na $(-\infty; 2)$: **ryze konkávní**; $f'' > 0$ na $(2; +\infty)$: **ryze konvexní**. $f' = 3x^2 - 12x$ je parabola s vrcholem (ostrým minimem) ve $2$, takže **$2$ je inflexní bod**, $f(2) = -6$.

> [!priklad|17]- Je funkce $f(x) = 2x + 1$ konvexní na $\mathbb{R}$? Ryze konvexní? Konkávní?
> $f(ax_1 + (1 - a)x_2) = 2ax_1 + 2(1 - a)x_2 + 1 = af(x_1) + (1 - a)f(x_2)$, v definici platí **rovnost**. Je tedy **konvexní i konkávní**, ale **ani ryze konvexní, ani ryze konkávní** (ostrá nerovnost nikdy neplatí).

> [!priklad|18]- Dokaž přímo z definice, že $f(x) = x^2$ je ryze konvexní na $\mathbb{R}$.
> Pro $x_1 \neq x_2$ a $a \in (0; 1)$:
> $$
> a x_1^2 + (1 - a) x_2^2 - \bigl(a x_1 + (1 - a) x_2\bigr)^2 = a(1 - a)(x_1 - x_2)^2 > 0,
> $$
> protože $a > 0$, $1 - a > 0$ a $x_1 - x_2 \neq 0$. Tedy **$f(ax_1 + (1 - a)x_2) < af(x_1) + (1 - a)f(x_2)$**, $f$ je ryze konvexní.

> [!priklad|19]- Pro $f(x) = x^4 - 6x^2$ najdi lokální extrémy, intervaly konvexity a konkávnosti a inflexní body.
> $f'(x) = 4x(x^2 - 3)$, stacionární body $0$, $\pm\sqrt{3}$. $f''(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$: $f''(0) = -12 < 0$ dá **ostré lokální maximum** $f(0) = 0$, $f''(\pm\sqrt{3}) = 24 > 0$ dá **ostrá lokální minima** $f(\pm\sqrt{3}) = -9$. $f'' > 0$ na $(-\infty; -1)$ a $(1; +\infty)$: **ryze konvexní**; $f'' < 0$ na $(-1; 1)$: **ryze konkávní**. $f''$ mění znaménko v $\pm 1$, takže $f'$ tam má ostrý extrém: **inflexní body $\pm 1$**, $f(\pm 1) = -5$.

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 1. semestrálnímu testu (J. Velebil, 9.–13. 11. 2026). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|20]- Definujte pojem: funkce $f$ je ryze konkávní na intervalu $(1; 5)$. (Přesně, se všemi předpoklady, českými větami.)
> Ať je funkce $f$ definována na intervalu $(1; 5)$. Funkce $f$ je na $(1; 5)$ ryze konkávní, jestliže **pro všechna $x_1, x_2 \in (1; 5)$, $x_1 \neq x_2$, a pro všechna $a \in (0; 1)$ platí $f\bigl(ax_1 + (1 - a)x_2\bigr) > af(x_1) + (1 - a)f(x_2)$**.

> [!priklad|21]- Dokažte nebo vyvraťte: Jestliže $f$ má druhou derivaci na $\mathbb{R}$, $f'(0) = 0$ a $f''(0) = 0$, potom $f$ nemá v bodě $0$ lokální extrém.
> **Neplatí.** Protipříklad $f(x) = x^4$: $f'(x) = 4x^3$, $f''(x) = 12x^2$ existují na $\mathbb{R}$ a $f'(0) = f''(0) = 0$. Přitom $f(x) = x^4 > 0 = f(0)$ pro všechna $x \neq 0$, takže $f$ má v $0$ **ostré lokální minimum**. **Tvrzení je vyvráceno.**

> [!priklad|22]- Dokažte nebo vyvraťte: Jestliže $f''(x) > 0$ pro všechna $x \in (0; 2)$, potom má $f$ na $(0; 2)$ nejvýše jeden stacionární bod.
> **Platí.** $f''$ je derivace $f'$ a $f'' > 0$ na otevřeném intervalu $(0; 2)$, takže podle věty o znaménku derivace a monotonii je **$f'$ na $(0; 2)$ rostoucí**. Rostoucí funkce je prostá: kdyby $f'(x_1) = f'(x_2) = 0$ pro $x_1 < x_2$, bylo by $f'(x_1) < f'(x_2)$, spor. Proto **$f' = 0$ nejvýše v jednom bodě**.

> [!priklad|23]- Najděte intervaly monotonie a lokální extrémy funkce $f(x) = x^4 - 4x^3$ na $\mathbb{R}$.
> $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$. Protože $x^2 \ge 0$, je $f' < 0$ na $(-\infty; 0)$ a $(0; 3)$, $f'(0) = 0$ a $f' > 0$ na $(3; +\infty)$. Na $(-\infty; 3)$ je $f' \le 0$ a nulová jen v bodě $0$, takže každý podinterval obsahuje bod s $f' < 0$ a $f$ je na **$(-\infty; 3)$ klesající**; na **$(3; +\infty)$ rostoucí**. Ve $3$ se klesání mění v růst: **ostré lokální minimum $f(3) = -27$**. V **$0$ extrém není** (vlevo i vpravo $f$ klesá), i když $0$ je stacionární bod.

---
← [[MA1 09 – Taylorův polynom, extrémy a monotonie|21. 10. 2026 Taylorův polynom, extrémy a monotonie]]

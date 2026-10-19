---
predmet: LGR
prednaska: 1
datum: 2026-09-24
zdroj: "Prezentace 1 (Výroková logika), slajdy 3–14"
tags: [prednaska, LGR]
---

# LGR 01 – Syntax a sémantika výrokové logiky

*Přednáška 1 · čtvrtek 24. 9. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 1 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1.pdf) · [Verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1a.pdf) · [Algoritmus na rozpoznávání formulí ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/fle.pdf)

Témata: `výrok` · `formule` · `syntaktický strom` · `hloubka` · `ohodnocení` · `pravdivostní tabulka` · `tautologie`

Prezentace a videa přednášející (A. Gollová) jsou na [math.fel.cvut.cz ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr-prednaska.html). Výroková logika studuje **logické spojky**: jak pravdivost složeného výroku závisí na pravdivosti jednoduchých výroků, ze kterých je složený.

## §0 Přehled na jedné stránce

|             | syntax (zápis)                                                         | sémantika (význam)                  |
| ----------- | ---------------------------------------------------------------------- | ----------------------------------- |
| základ      | logické proměnné $a, b, c \in A$                                       | ohodnocení $u : A \to \{0, 1\}$     |
| složené     | formule z $\neg, \wedge, \vee, \Rightarrow, \Leftrightarrow$ a závorek | pravdivostní tabulka spojek         |
| struktura   | syntaktický strom, hloubka                                             | výpočet hodnoty zdola nahoru        |
| klasifikace | $\alpha = \beta$ (stejný řetězec)                                      | splnitelná, tautologie, kontradikce |

## §1 Výrok, proměnná, formule

- [[výrok|Výrok]] je oznamovací věta, u které se dá rozhodnout o pravdivosti. „Prší.“ je výrok, „Zavři okno!“ ne. ^def-vyrok
- Jednoduché výroky označujeme jako [[logická proměnná|logické proměnné]], typicky $A = \{a, b, c\}$.
- [[formule|Formule]] je formálně zapsaný výrok, např. $a$ nebo $\neg a \vee b$. Množina všech formulí nad $A$ se značí $\mathrm{Fle}(A)$.

> [!lidsky] Rozdíl mezi a a α
> $a, b, c$ jsou konkrétní logické proměnné, písmenka jazyka. Řecká písmena $\alpha, \beta, \varphi$ jsou **zástupná jména pro libovolnou formuli**: $\alpha$ může znamenat $a$, ale i $(\neg b \Rightarrow a) \vee c$. Pravidlo „je-li $\alpha$ formule, je i $\neg\alpha$“ tak platí najednou pro všechny formule, podobně jako $x$ ve vzorci $(x + 1)^2$ zastupuje libovolné číslo.

## §2 Syntax: definice formule

> [!definice] Formule výrokové logiky · slajd 5
> Buď $A$ neprázdná množina logických proměnných. *Formule* je definována induktivně:
>
> 1. Každá logická proměnná $a \in A$ je formule (tzv. *atomická formule*).
> 2. Jsou-li $\alpha, \beta$ formule, pak také $(\neg\alpha)$, $(\alpha \wedge \beta)$, $(\alpha \vee \beta)$, $(\alpha \Rightarrow \beta)$ a $(\alpha \Leftrightarrow \beta)$ jsou formule.
> 3. Každá formule vznikne konečným počtem použití pravidel 1 a 2.

^def-formule

> [!pozor] Bod 3 se často zapomíná
> Bod 3 říká, že **nic jiného** formulí není: bez něj by definice nevylučovala třeba nekonečný řetězec $\neg\neg\neg\dots$ nebo cokoliv dalšího. Tahle „uzavírací“ podmínka patří ke každé [[rekurzivní definice|rekurzivní definici]] množiny, tady množiny $\mathrm{Fle}(A)$.

Správně se závorkuje vždy, ale my `slajd 6`:

1. nepíšeme vnější závorky,
2. nepíšeme závorky kolem $\neg$ (negace váže silněji než ostatní spojky).

$$
\text{správně: } \varphi = (((\neg b) \Rightarrow a) \vee c), \qquad \text{my píšeme: } \varphi = (\neg b \Rightarrow a) \vee c.
$$

> [!lidsky] Lidsky
> Stejně jako v aritmetice nepíšeš $((2 \cdot 3) + 4)$, ale $2 \cdot 3 + 4$. Počítač umí z odlehčeného zápisu úplné závorky jednoznačně vrátit; algoritmus je v souboru [fle.pdf ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/fle.pdf).

## §3 Syntaktický strom

> [!definice] Syntaktický strom · slajd 7
> Každé formuli odpovídá kořenový strom:
>
> - atomická formule $a$ je jediný vrchol označený $a$,
> - $\neg\alpha$ má kořen $\neg$ s jediným synem, kořenem stromu $\alpha$,
> - $\alpha \circ \beta$ (pro binární spojku $\circ$) má kořen $\circ$, levého syna kořen stromu $\alpha$ a pravého syna kořen stromu $\beta$.

^def-strom

> [!lidsky] Lidsky
> Strom ukazuje, jak se formule skládala: nahoře poslední spojka, pod ní ty, které se použily dřív, dole proměnné. Je to jako rozbor věty ve škole, kde se hledá, co je podmět a co přísudek, jen tady se hledá, která spojka „drží“ celou formuli.

[[syntaktický strom|Strom]] se v podstatě píše **odspodu**: listy jsou proměnné, nad nimi spojky, kořen je poslední použitá spojka. Každý vrchol i se vším pod sebou je *podformule* `slajd 8`.

> [!obrazek] Strom formule $(\neg b \Rightarrow a) \vee c$
> ![[lgr01-strom.png]]
> *Modře spojky, oranžově proměnné (listy). Zelené číslo u vrcholu je hloubka podformule, která v něm začíná; celá formule má hloubku 3.*

## §4 Hloubka formule

> [!definice] Hloubka formule · rekurzivně
> $\mathrm{hl} : \mathrm{Fle}(A) \to \mathbb{N}$:
>
> 1. $\varphi = a \in A$ (logická proměnná) $\Rightarrow$ $\mathrm{hl}(\varphi) = 0$,
> 2. $\varphi = \neg\alpha$ $\Rightarrow$ $\mathrm{hl}(\varphi) = 1 + \mathrm{hl}(\alpha)$,
> 3. $\varphi = \alpha \circ \beta$ $\Rightarrow$ $\mathrm{hl}(\varphi) = 1 + \max\{\mathrm{hl}(\alpha), \mathrm{hl}(\beta)\}$.

^def-hloubka

> [!pozor] Nezapomeň na binární spojky
> Bez bodu 3 by hloubka nebyla definovaná pro $\alpha \wedge \beta$, $\alpha \Rightarrow \beta$ atd. Hloubka je délka nejdelší cesty od kořene k listu, proto se bere **maximum** z obou větví.

Výpočet pro $\varphi = (\neg b \Rightarrow a) \vee c$:

$$
\mathrm{hl}(\neg b) = 1 + 0 = 1, \quad \mathrm{hl}(\neg b \Rightarrow a) = 1 + \max\{1, 0\} = 2, \quad \mathrm{hl}(\varphi) = 1 + \max\{2, 0\} = 3.
$$

> [!lidsky] Lidsky
> Hloubka je počet pater stromu nad nejnižším listem, tedy kolik spojek je „vnořeno do sebe“ na nejdelší cestě. Proměnná má hloubku 0, každá spojka přidá jedno patro.

## §5 Rovnost formulí

> [!definice] Rovnost formulí · slajd 9
> Dvě formule jsou si **rovny**, pokud tvoří stejný řetězec (v neodlehčeném tvaru), neboli mají stejný syntaktický strom.

^def-rovnost-formuli

Proto $\alpha \neq \neg\neg\alpha$ a $a \vee b \neq b \vee a$.

> [!lidsky] Rovnost je zápisová, ne významová
> Rovnost formulí je čistě **zápisová**: porovnávají se znaky, ne význam. $a \vee b$ a $b \vee a$ znamenají totéž, ale jsou to dvě různé formule. Shodu významu měří až *tautologická ekvivalence* $\mathrel{\vert\!=\!\vert}$ (příští přednáška). Důsledek: formulí je nekonečně mnoho i nad jedinou proměnnou: $a, \neg a, \neg\neg a, \dots$ jsou navzájem různé.

## §6 Sémantika: pravdivostní ohodnocení

Pravda je $1$, nepravda $0$. Pravdivost logických proměnných určí vnější svět, matematicky [[pravdivostní ohodnocení|ohodnocení]] $u : A \to \{0, 1\}$. Pravdivost složených formulí se pak spočítá z tabulky spojek:

| $\alpha$ | $\beta$ | $\alpha \wedge \beta$ | $\alpha \vee \beta$ | $\alpha \Rightarrow \beta$  | $\alpha \Leftrightarrow \beta$ |
| -------- | ------- | --------------------- | ------------------- | --------------------------- | ------------------------------ |
| 0        | 0       | 0                     | 0                   | 1                           | 1                              |
| 0        | 1       | 0                     | 1                   | 1                           | 0                              |
| 1        | 0       | 0                     | 1                   | 0                           | 0                              |
| 1        | 1       | 1                     | 1                   | 1                           | 1                              |
| *čti*    |         | „a“                   | „nebo“              | „jestliže…, pak“, „slibuji“ | „právě tehdy, když“            |

a $\neg$: $0 \mapsto 1$, $1 \mapsto 0$.

^tabulka

> [!lidsky] Implikace je slib
> „Když zítra nebude pršet, půjdu na výlet.“ Slib porušíš jen jedním způsobem: nepršelo (předpoklad pravdivý) a na výlet jsi nešel (závěr nepravdivý). Když pršelo, slib nic neříká, takže je splněn ať jdeš, nebo ne. Proto [[implikace]] $\alpha \Rightarrow \beta$ je $0$ jen v řádku $1, 0$.

Totéž přes čísla, kde $u(\alpha) \in \{0, 1\}$:

$$
\begin{aligned}
u(\neg\alpha) &= 1 - u(\alpha), \\
u(\alpha \wedge \beta) &= \min\{u(\alpha), u(\beta)\}, \\
u(\alpha \vee \beta) &= \max\{u(\alpha), u(\beta)\}, \\
u(\alpha \Rightarrow \beta) = 1 &\iff u(\alpha) \le u(\beta), \\
u(\alpha \Leftrightarrow \beta) = 1 &\iff u(\alpha) = u(\beta).
\end{aligned}
$$

(*iff* = *if and only if* = právě když.) Např. $u(\neg\alpha) = 1$ právě tehdy, když $u(\alpha) = 0$.

> [!definice] Pravdivostní ohodnocení · slajd 12
> *Pravdivostní ohodnocení* je zobrazení $u : \mathrm{Fle}(A) \to \{0, 1\}$, které respektuje tabulku spojek: $u(\neg\alpha) = 1$ iff $u(\alpha) = 0$; $u(\alpha \wedge \beta) = 1$ iff $u(\alpha) = u(\beta) = 1$; $u(\alpha \vee \beta) = 0$ iff $u(\alpha) = u(\beta) = 0$; $u(\alpha \Rightarrow \beta) = 0$ iff $u(\alpha) = 1$ a $u(\beta) = 0$; $u(\alpha \Leftrightarrow \beta) = 1$ iff $u(\alpha) = u(\beta)$.

^def-ohodnoceni

> [!veta] Tvrzení · slajd 13
> **Každé pravdivostní ohodnocení $u : \mathrm{Fle}(A) \to \{0, 1\}$ je jednoznačně určeno svými hodnotami na atomických formulích $a \in A$.**
>
> Důsledek: pro $n$ proměnných existuje $2^n$ různých ohodnocení, a proto má pravdivostní tabulka $2^n$ řádků (pro $a, b$ čtyři: $00, 01, 10, 11$).

^veta-ohodnoceni

> [!lidsky] Lidsky
> Stačí říct, které proměnné jsou pravdivé, a hodnota každé formule se dopočítá stromem odspodu nahoru. Jeden řádek tabulky = jedno ohodnocení $\bar{u}$. Každá proměnná má 2 možnosti, takže pro 3 proměnné je $2 \cdot 2 \cdot 2 = 8$ řádků, pro 10 proměnných už $1024$.

## §7 Splnitelná formule, tautologie, kontradikce

> [!definice] Definice · slajd 14
> Formule je
>
> - *[[splnitelná formule|splnitelná]]*, je-li pravdivá v alespoň jednom ohodnocení,
> - *[[tautologie]]*, je-li pravdivá ve všech ohodnoceních,
> - *[[kontradikce]]*, není-li pravdivá v žádném ohodnocení.

^def-tautologie

> [!lidsky] Lidsky
> Podívej se na sloupec formule v tabulce: aspoň jedna jednička znamená splnitelná, samé jedničky tautologie („pravda vždycky, ať je svět jakýkoli“), samé nuly kontradikce („nikdy to nemůže platit“).

> [!example] $\varphi = (\neg b \Rightarrow a) \vee c$ celou tabulkou
> | $a$ | $b$ | $c$ | $\neg b$ | $\neg b \Rightarrow a$ | $\varphi$ |
> |---|---|---|---|---|---|
> | 0 | 0 | 0 | 1 | 0 | **0** |
> | 0 | 0 | 1 | 1 | 0 | 1 |
> | 0 | 1 | 0 | 0 | 1 | 1 |
> | 0 | 1 | 1 | 0 | 1 | 1 |
> | 1 | 0 | 0 | 1 | 1 | 1 |
> | 1 | 0 | 1 | 1 | 1 | 1 |
> | 1 | 1 | 0 | 0 | 1 | 1 |
> | 1 | 1 | 1 | 0 | 1 | 1 |
>
> $\varphi$ je pravdivá v 7 z 8 ohodnocení (87,5 %): je **splnitelná**, ale **není tautologie** (protipříklad $a = b = c = 0$). Ve skutečnosti $\varphi$ znamená totéž co $a \vee b \vee c$.

> [!navic] Vztahy mezi třemi pojmy
> - Každá tautologie je splnitelná, obráceně ne.
> - $\varphi$ je tautologie právě tehdy, když $\neg\varphi$ je kontradikce.
> - Nejjednodušší příklady: $a \vee \neg a$ je tautologie, $a \wedge \neg a$ kontradikce, $a$ je splnitelná, ale ani jedno z toho.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jaký je rozdíl mezi $a$ a $\alpha$ v zápisu výrokové logiky?
> $a$ je konkrétní **logická proměnná** z $A$. $\alpha$ je **zástupné jméno pro libovolnou formuli** (třeba $\neg b \Rightarrow a$).

> [!karta|03]- K čemu je v definici formule podmínka, že každá formule vznikne z proměnných konečným počtem použití spojek?
> Říká, že **nic jiného** formulí není (např. nekonečný řetězec $\neg\neg\neg\dots$). Bez něj by rekurzivní definice množinu neurčovala jednoznačně.

> [!karta|05]- Proč je v hloubce formule $\alpha \circ \beta$ maximum, a ne součet hloubek $\alpha$ a $\beta$?
> Hloubka je **výška syntaktického stromu**: nejdelší cesta od kořene k listu. Pod kořenem $\circ$ visí oba podstromy vedle sebe, takže rozhoduje ten vyšší: $\mathrm{hl}(\alpha \circ \beta) = 1 + \max\{\mathrm{hl}(\alpha), \mathrm{hl}(\beta)\}$.

> [!karta|06]- Jsou formule $a \vee b$ a $b \vee a$ rovny?
> **Ne**, rovnost formulí je stejný řetězec / stejný strom. Jsou ale tautologicky ekvivalentní (stejný význam).

> [!karta|07]- Proč je formulí nekonečně mnoho i nad $A = \{a\}$?
> $a, \neg a, \neg\neg a, \neg\neg\neg a, \dots$ jsou navzájem různé řetězce, tedy různé formule.

> [!karta|08]- Proč je implikace $\alpha \Rightarrow \beta$ pravdivá, když $\alpha$ neplatí?
> Implikace je **slib „když $\alpha$, pak $\beta$“**. Když $\alpha$ neplatí, slib se nedá porušit, takže je splněný. Porušit ho jde jen v řádku $u(\alpha) = 1$, $u(\beta) = 0$.

> [!karta|09]- Vyjádři $u(\alpha \wedge \beta)$, $u(\alpha \vee \beta)$ a $u(\alpha \Rightarrow \beta)$ pomocí čísel 0 a 1.
> $u(\alpha \wedge \beta) = \min$, $u(\alpha \vee \beta) = \max$, $u(\alpha \Rightarrow \beta) = 1 \iff u(\alpha) \le u(\beta)$.

> [!karta|10]- Kolik různých pravdivostních ohodnocení existuje pro 3 proměnné a proč?
> $2^3 = 8$. Ohodnocení je jednoznačně určeno hodnotami na proměnných a každá má 2 možnosti.

> [!karta|12]- Jak souvisí tautologie a kontradikce přes negaci?
> $\varphi$ je tautologie právě tehdy, když $\neg\varphi$ je kontradikce.

### Příklady na procvičení

> [!priklad|02]- Zapiš $(\neg b \Rightarrow a) \vee c$ s úplným uzávorkováním podle definice.
> $(((\neg b) \Rightarrow a) \vee c)$

> [!priklad|04]- Spočti hloubku formule $(\neg b \Rightarrow a) \vee c$.
> $\mathrm{hl}(\neg b) = 1$, $\mathrm{hl}(\neg b \Rightarrow a) = 1 + \max\{1, 0\} = 2$, celá: $1 + \max\{2, 0\} = 3$.

> [!priklad|11]- Je $(\neg b \Rightarrow a) \vee c$ splnitelná? Tautologie?
> Splnitelná ano (pravdivá v 7 z 8 řádků), tautologie **ne**: pro $a = b = c = 0$ je $\neg b \Rightarrow a = 1 \Rightarrow 0 = 0$ a $0 \vee 0 = 0$.

> [!priklad|13]- „Když zítra nebude pršet, půjdu na výlet.“ Pršelo a na výlet jsem šel. Byl slib porušen?
> **Ne.** Předpoklad neplatí ($0$), takže implikace je pravdivá bez ohledu na závěr.

---
[[LGR 02 – Tautologická ekvivalence a úplné systémy spojek|25. 9. 2026 Tautologická ekvivalence a úplné systémy spojek]] →

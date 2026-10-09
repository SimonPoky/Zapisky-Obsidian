---
predmet: LGR
prednaska: 4
datum: 2026-10-08
zdroj: "Prezentace 3 (Sémantika, rezoluční metoda), slajdy 3–14"
tags: [prednaska, LGR]
---

# LGR 04 – Sémantický důsledek a klauzální tvar

*Přednáška 4 · čtvrtek 8. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 3 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_3.pdf) · [Verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_3a.pdf)

Témata: `splnitelnost množiny formulí` · `prázdná množina` · `sémantický důsledek` · `důkaz sporem` · `převod na nesplnitelnost` · `klauzální tvar` · `rezolventa`

Dosud se pravdivost řešila u jedné [[formule]]. Dnes se rozšíří na celé množiny formulí („všechny předpoklady platí naráz“) a z toho vznikne nejdůležitější pojem výrokové logiky: [[sémantický důsledek]], tedy kdy z předpokladů plyne závěr. Na konci se ukáže, proč se skoro každá otázka dá převést na otázku „je tahle množina [[konjunktivní normální forma|CNF]] klauzulí nesplnitelná?“, na kterou odpovídá rezoluční metoda.

## §0 Přehled na jedné stránce

| pojem | zápis | význam |
|---|---|---|
| pravdivost množiny | $u(S) = 1$ | v ohodnocení $u$ jsou pravdivé **všechny** formule z $S$ |
| [[splnitelná množina formulí\|splnitelná množina]] | $\exists u : u(S) = 1$ | aspoň jedno ohodnocení, kde platí vše naráz (svědek) |
| prázdná množina | $u(\emptyset) = 1$ pro každé $u$ | $\emptyset$ je splnitelná, $\emptyset \models \varphi$ iff $\varphi$ je tautologie |
| [[sémantický důsledek]] | $S \models \varphi$ | $\forall u : u(S) \le u(\varphi)$ |
| důkaz sporem | $S \models \varphi$ iff $S \cup \{\neg\varphi\}$ nesplnitelná | důsledek se převede na nesplnitelnost |
| [[klauzální tvar]] | $\mathrm{Kl}(S)$ | všechny klauzule z CNF formulí v $S$; splnitelná iff $S$ splnitelná |
| [[rezolventa]] | $\{\alpha \vee x, \beta \vee \neg x\} \models \alpha \vee \beta$ | když vznikne $\mathrm{ff}$, množina je nesplnitelná |

## §1 Splnitelnost množiny formulí

> [!definice] Pravdivost a splnitelnost množiny · slajdy 3–4
> Nechť $S$ je množina formulí a $u$ [[pravdivostní ohodnocení]]. Pak $u(S) = 1$, právě když $u(\varphi) = 1$ pro **všechny** $\varphi \in S$; jinak $u(S) = 0$.
> - $S$ je *splnitelná*, existuje-li ohodnocení $u$ s $u(S) = 1$. Takové $u$ je *svědek splnitelnosti*.
> - $S$ je *nesplnitelná*, je-li $u(S) = 0$ v každém ohodnocení, tj. v každém $u$ je některá formule z $S$ nepravdivá.

^def-splnitelnost-mnoziny

> [!lidsky] Lidsky
> Množina formulí je seznam pravidel, která mají platit **současně**. Splnitelná znamená, že existuje aspoň jeden „svět“ (řádek tabulky), kde se žádné pravidlo neporuší. Tři kamarádi: „přijdu, jestli přijde Eva“, „Eva nepřijde“, „někdo z nás dvou přijde“. Každá věta zvlášť jde splnit, ale všechny tři naráz ne.

Pro **konečnou** množinu $S = \{\varphi_1, \dots, \varphi_n\}$ je $u(S) = u(\varphi_1 \wedge \dots \wedge \varphi_n)$: „všechny jsou pravdivé“ je přesně konjunkce. Definice přes „všechny prvky“ je potřeba kvůli **nekonečným** množinám. Už z jedné proměnné $a$ vznikne nekonečně mnoho formulí ($a$, $\neg a$, $\neg\neg a$, $a \vee \neg a$, …), takže množina formulí může být nekonečná a nekonečnou konjunkci zapsat nejde.

> [!pozor] Pro množiny se neříká tautologie ani kontradikce
> U množin formulí se mluví jen o **splnitelné** a **nesplnitelné** množině. Slova [[tautologie]] a [[kontradikce]] patří jedné formuli.

> [!example] Tři malé množiny
> | $a$ | $b$ | $a \Rightarrow b$ | $\neg b$ | $a \vee b$ |
> |---|---|---|---|---|
> | 0 | 0 | 1 | 1 | 0 |
> | 0 | 1 | 1 | 0 | 1 |
> | 1 | 0 | 0 | 1 | 1 |
> | 1 | 1 | 1 | 0 | 1 |
>
> - $S = \{a \Rightarrow b, \neg b\}$ je **splnitelná**: svědek je první řádek $u(a) = u(b) = 0$ (implikace s nepravdivým předpokladem je pravdivá).
> - $T = \{a \Rightarrow b, \neg b, a \vee b\}$ je **nesplnitelná**: v žádném ze 4 řádků nejsou všechny tři sloupce $1$. V 1. řádku pokazí $a \vee b$, ve 2. a 4. $\neg b$, ve 3. implikace.

## §2 Prázdná množina formulí

Otázka: platí $u(\emptyset) = 1$? Podle definice to znamená „každá formule z $\emptyset$ je pravdivá v $u$“, přesněji

$$
\forall \varphi \, \big(\varphi \in \emptyset \Rightarrow u(\varphi) = 1\big).
$$

Zvol libovolnou formuli $\varphi$. Předpoklad $\varphi \in \emptyset$ je nepravdivý, takže celá [[implikace]] je pravdivá, ať je $u(\varphi)$ jakékoli. To platí pro každé $\varphi$, takže **$u(\emptyset) = 1$, a to v každém ohodnocení $u$**. Prázdná množina je tedy splnitelná a svědkem je libovolné ohodnocení. ^prazdna-mnozina

> [!lidsky] Lidsky
> „Všechna jablka v prázdném košíku jsou červená“ je pravda, protože neexistuje jablko, které by to vyvrátilo. Prázdný seznam pravidel nejde porušit.

> [!pozor] Past: „každá formule z $\emptyset$ je nepravdivá“ je taky pravda
> Stejnou úvahou platí i $\forall \varphi \, (\varphi \in \emptyset \Rightarrow u(\varphi) = 0)$. Z toho ale **neplyne** $u(\emptyset) = 0$. Nepravdivost množiny znamená, že **existuje** svědek, který ji pokazí:
>
> $$
> u(\emptyset) = 0 \iff \exists \varphi \, \big(\varphi \in \emptyset \wedge u(\varphi) = 0\big),
> $$
>
> a takové $\varphi$ neexistuje (žádná formule v $\emptyset$ není). Proto $u(\emptyset) = 0$ **neplatí**. Pro prvky prázdné množiny platí jakákoli vlastnost, ale k nepravdivosti množiny je potřeba konkrétní pokažená formule.

## §3 Sémantický důsledek

> [!definice] Sémantický důsledek · slajd 5
> Formule $\varphi$ je *sémantickým důsledkem* množiny formulí $S$, píšeme $S \models \varphi$, když $\varphi$ je pravdivá v každém ohodnocení, ve kterém jsou pravdivé všechny formule z $S$:
>
> $$
> S \models \varphi \iff \forall u : \big(u(S) = 1 \Rightarrow u(\varphi) = 1\big).
> $$
>
> Když to neplatí, píšeme $S \not\models \varphi$.

^def-dusledek

> [!lidsky] Lidsky
> „Ze předpokladů $S$ plyne $\varphi$“: kdykoli jsou splněné všechny předpoklady, je splněný i závěr. Řádky, kde nějaký předpoklad neplatí, nás **nezajímají**. Je to přesně to, co dělá dobrý matematický důkaz.

> [!example] $\{a, a \Rightarrow b\} \models b$
> Obojí je pravdivé jen v řádku $a = 1, b = 1$ a tam je $b = 1$. Tohle je *modus ponens*: když platí $a$ a „z $a$ plyne $b$“, platí $b$.

^modus-ponens

> [!obrazek] Je $a$ nebo $b$ důsledkem $\{a \Rightarrow b, a \vee b\}$?
> ![[lgr04-dusledek.png]]
> *Zeleně řádky, kde je celá množina $S$ pravdivá; jen ty se kontrolují. Oranžově vstupní proměnné, modře formule. Vpravo kontrola závěru: červeně řádek, který ho vyvrací.*

V řádku $a = 0, b = 1$ jsou obě formule pravdivé, ale $a$ ne, takže $\{a \Rightarrow b, a \vee b\} \not\models a$ a tento řádek je *protipříklad*. Naopak $b$ vyjde $1$ v obou zelených řádcích, takže $\{a \Rightarrow b, a \vee b\} \models b$. Bez tabulky: kdyby $b = 0$, musela by kvůli $a \vee b$ platit $a = 1$, a pak by implikace $1 \Rightarrow 0$ byla nepravdivá. Spor, tedy $b = 1$. ^priklad-dusledek

> [!veta] Tvrzení · slajd 6
> **$S \models \varphi$, právě když $u(S) \le u(\varphi)$ pro každé ohodnocení $u$.**

^veta-le

> [!lidsky] Lidsky
> V tabulce je zakázaná jen jediná kombinace: $u(S) = 1$ a $u(\varphi) = 0$. Přesně tehdy by neplatilo $u(S) \le u(\varphi)$. Kde $u(S) = 0$, může být $u(\varphi)$ cokoli; kde $u(S) = 1$, musí být $u(\varphi) = 1$. Stejně jako u implikace: $u(\alpha \Rightarrow \beta) = 1$ iff $u(\alpha) \le u(\beta)$.

> [!obrazek] Důsledek jako vnoření množin
> ![[lgr04-mnoziny.png]]
> *Vlevo: zeleně ohodnocení, kde platí celé $S$, modře ohodnocení, kde platí $\varphi$. $S \models \varphi$ znamená, že zelená leží celá v modré. Vpravo: červeně ohodnocení, kde platí $\neg\varphi$. Zelená a červená se nepotkají, takže $S \cup \{\neg\varphi\}$ nemá žádné ohodnocení: je nesplnitelná (§4).*

Pro jednoprvkovou množinu $S = \{\alpha\}$ dostaneš vztah mezi dvěma formulemi:

$$
\alpha \models \varphi \iff \forall u : u(\alpha) \le u(\varphi) \iff \forall u : u(\alpha \Rightarrow \varphi) = 1 \iff (\alpha \Rightarrow \varphi) \text{ je tautologie}.
$$

Vztah mezi dvěma formulemi se tak převede na vlastnost jedné formule, stejně jako [[tautologická ekvivalence]]: $\alpha \mathrel{\vert\!=\!\vert} \beta$ iff $\alpha \Leftrightarrow \beta$ je tautologie. ^veta-implikace

> [!navic] Dva krajní případy · slajd 6
> - Je-li $S$ **nesplnitelná**, pak $S \models \varphi$ pro **každou** $\varphi$: žádný řádek s $u(S) = 1$ není, takže není co pokazit. („Z nepravdy plyne cokoli.“)
> - $\emptyset \models \varphi$ (píše se zkráceně $\models \varphi$), právě když $\varphi$ je tautologie: $u(\emptyset) = 1$ ve všech řádcích, takže $\varphi$ musí být pravdivá všude.

## §4 Věta o sémantickém důkazu sporem

> [!veta] Věta o sémantickém důkazu sporem · slajd 7
> ==Pro množinu formulí $S$ a formuli $\varphi$== platí: **$S \models \varphi$, právě když $S' = S \cup \{\neg\varphi\}$ je nesplnitelná.**
>
> > [!note]- Důkaz
> > **„⇒“:** Nechť $S \models \varphi$, tedy $u(S) \le u(\varphi)$ pro každé $u$. Vezmi libovolné $u$. Jsou dvě možnosti:
> > - $u(S) = 1$: pak $u(\varphi) = 1$, tedy $u(\neg\varphi) = 0$, a proto $u(S') = 0$ (formule $\neg\varphi \in S'$ je nepravdivá).
> > - $u(S) = 0$: pak už některá formule z $S$ je v $u$ nepravdivá, a protože $S \subseteq S'$, je i $u(S') = 0$.
> >
> > Tedy $u(S') = 0$ pro všechna $u$, $S'$ je nesplnitelná.
> >
> > **„⇐“:** Nechť $S'$ je nesplnitelná a $u(S) = 1$. Kdyby $u(\varphi) = 0$, bylo by $u(\neg\varphi) = 1$ a spolu s $u(S) = 1$ by vyšlo $u(S') = 1$, spor. Tedy $u(\varphi) = 1$, a proto $S \models \varphi$.

^veta-spor

> [!lidsky] Lidsky
> Chceš ukázat, že z předpokladů plyne závěr? Přidej k předpokladům opak závěru a ukaž, že to nejde splnit naráz. Na obrázku výše: když zelená leží v modré, nemá zelená s červenou (opakem $\varphi$) nic společného. Důkaz sporem ze střední školy, jen pro množiny formulí.

Díky větě se všechny dosavadní otázky převedou na jednu, o (ne)splnitelnosti (slajd 9):

| otázka | převod |
|---|---|
| je $\varphi$ [[splnitelná formule\|splnitelná]]? | je $\{\varphi\}$ splnitelná? |
| je $\varphi$ [[kontradikce]]? | je $\{\varphi\}$ nesplnitelná? |
| je $\varphi$ [[tautologie]]? | je $\{\neg\varphi\}$ nesplnitelná? |
| platí $S \models \varphi$? | je $S \cup \{\neg\varphi\}$ nesplnitelná? |
| platí $\varphi \mathrel{\vert\!=\!\vert} \psi$? | jsou $\{\varphi, \neg\psi\}$ **i** $\{\psi, \neg\varphi\}$ nesplnitelné? |

^prevod

Poslední řádek: $\varphi \mathrel{\vert\!=\!\vert} \psi$ iff $\varphi \models \psi$ a $\psi \models \varphi$, a každý z obou důsledků se převede zvlášť.

> [!pozor] Častá chyba: tautologie se testuje přes negaci
> Otázka „je $\varphi$ splnitelná?“ s odpovědí *ano* neříká, že $\varphi$ je tautologie: stačí jedna jednička ve sloupci. Pro tautologii se ptej, jestli je **$\neg\varphi$ nesplnitelná** (sloupec $\neg\varphi$ má samé nuly, tedy $\varphi$ samé jedničky).

## §5 Klauzální tvar

Tabulka pro $n$ proměnných má $2^n$ řádků (pro 5 proměnných 32, pro 30 už přes miliardu), takže je potřeba metoda, která se tabulce vyhne. *Rezoluční metoda* umí jen jedno: zjistit, zda je **množina klauzulí** nesplnitelná. Podle §4 to ale stačí na všechno, zbývá převést formule na klauzule.

Klauzule je jiné jméno pro [[maxterm]]: disjunkce [[literál|literálů]], jeden literál, nebo $\mathrm{ff}$ (slajd 10). Každá formule má [[konjunktivní normální forma|CNF]] $\varphi \mathrel{\vert\!=\!\vert} c_1 \wedge c_2 \wedge \dots \wedge c_n$, kde $c_i$ jsou klauzule. Konjunkce je pravdivá, právě když jsou pravdivé všechny členy, takže

$$
u(\varphi) = 1 \iff u(c_1 \wedge \dots \wedge c_n) = 1 \iff u(c_1) = \dots = u(c_n) = 1 \iff u(\{c_1, \dots, c_n\}) = 1.
$$

Formule a množina jejích klauzulí jsou pravdivé **ve stejných ohodnoceních**, mají dokonce stejné svědky splnitelnosti. Otázka o splnitelnosti formule je tedy otázka o splnitelnosti množiny klauzulí.

> [!definice] Klauzální tvar · slajdy 11–12
> *Klauzální tvar* množiny formulí $S$, značený $\mathrm{Kl}(S)$, je množina klauzulí, která vznikne takto:
> 1. každou formuli z $S$ převeď na CNF a rozlož ji na jednotlivé klauzule,
> 2. v každé klauzuli nech každý literál nejvýš jednou ($a \vee a \vee b \mathrel{\vert\!=\!\vert} a \vee b$),
> 3. klauzule, která obsahuje proměnnou pozitivně i negativně, je tautologie ($a \vee \neg a \vee b \mathrel{\vert\!=\!\vert} \mathrm{tt}$) a vypustí se.
>
> Množiny $S$ a $\mathrm{Kl}(S)$ jsou pravdivé ve stejných ohodnoceních, takže **$S$ je splnitelná, právě když $\mathrm{Kl}(S)$ je splnitelná.** $\mathrm{Kl}(S)$ není určená jednoznačně (CNF není jednoznačná).

^def-klauzalni

> [!lidsky] Lidsky
> Rozsekáš všechna pravidla na co nejmenší „aspoň jedno z …“ požadavky. Tautologii smíš vyhodit, protože ji nejde porušit: $u(S \cup \{\mathrm{tt}\}) = u(S)$. Je to jako vyškrtnout ze seznamu povinností „buď prší, nebo neprší“.

> [!navic] Když $S$ obsahuje jen tautologie
> Pak se všechny klauzule vypustí a $\mathrm{Kl}(S) = \emptyset$. To sedí s §2: prázdná množina je splnitelná, stejně jako množina tautologií.

## §6 Příklad: kdo pojede na výlet

> [!example] Zadání (typ písemkové úlohy, 10 b.)
> Zformalizuj věty v jazyce výrokové logiky s $At = \{p, q, r, s, t\}$ a rezoluční metodou ověř, zda věta pod čarou je sémantickým důsledkem vět nad čarou.
> - Na výlet pojede Petr nebo Quido.
> - Jestliže pojede Quido, pojede Simona a nepojede Renata.
> - Jestliže pojede Tomáš, pojede i Renata.
> - Jestliže pojede Simona, pojede Tomáš.
> - ― ― ―
> - Petr pojede na výlet.

**Formalizace** ($p$ … pojede Petr, $q$ … Quido, $r$ … Renata, $s$ … Simona, $t$ … Tomáš):

$$
S = \{\, p \vee q,\ \ q \Rightarrow (s \wedge \neg r),\ \ t \Rightarrow r,\ \ s \Rightarrow t \,\}, \qquad \text{otázka: } S \models p\,?
$$

**Krok 1, převod na nesplnitelnost:** podle §4 platí $S \models p$, právě když $S' = S \cup \{\neg p\}$ je nesplnitelná.

**Krok 2, klauzální tvar $S'$** přes CNF. Jen druhá formule potřebuje distributivní zákon:

$$
q \Rightarrow (s \wedge \neg r) \mathrel{\vert\!=\!\vert} \neg q \vee (s \wedge \neg r) \mathrel{\vert\!=\!\vert} (\neg q \vee s) \wedge (\neg q \vee \neg r).
$$

Implikace $t \Rightarrow r$ a $s \Rightarrow t$ jsou rovnou klauzule $\neg t \vee r$ a $\neg s \vee t$. Celkem

$$
M = \mathrm{Kl}(S') = \{\, p \vee q,\ \neg q \vee s,\ \neg q \vee \neg r,\ \neg t \vee r,\ \neg s \vee t,\ \neg p \,\}.
$$

^priklad-vylet

**Krok 3, hledání sporu.** Předpokládej, že existuje $u$ s $u(M) = 1$, a odvozuj, co dalšího by v něm muselo platit (sémantické důsledky):

- $\{\neg p, p \vee q\} \models q$: Petr nejede, a přitom jede Petr nebo Quido, takže jede Quido.
- $\{\neg q \vee s, \neg s \vee t\} \models \neg q \vee t$: buď Simona jede, pak kvůli $\neg s \vee t$ jede Tomáš; nebo nejede, pak kvůli $\neg q \vee s$ nejede Quido. V každém případě platí $t$ nebo $\neg q$. Pravdivost obou klauzulí nejde zařídit jen přes $s$, protože $s$ je v jedné pozitivně a ve druhé negativně, takže musí být pravdivý jeden ze zbylých „konců“.

Takhle vzniká [[rezolventa]]: ze dvou klauzulí, kde je jedna proměnná jednou pozitivně a jednou negativně, se tato proměnná škrtne a zbytky se spojí $\vee$. Obecně $\{\alpha \vee x, \beta \vee \neg x\} \models \alpha \vee \beta$ (slajd 14 značí $\mathrm{res}_x$). ^def-rezolventa

> [!obrazek] Rezoluční odvození pro výlet
> ![[lgr04-rezoluce.png]]
> *Oranžově klauzule z $S$, červeně $\neg p$ (negovaný závěr), modře rezolventy, šedě proměnná, podle které se rezolvuje. Dole $\mathrm{ff}$: spor.*

Pokračování: $\neg q \vee t$ s $\neg t \vee r$ dá $\neg q \vee r$, to s $\neg q \vee \neg r$ dá $\neg q$, a nakonec $q$ s $\neg q$ dá **$\mathrm{ff}$**. Kdyby existovalo $u$ s $u(M) = 1$, muselo by v něm platit i $\mathrm{ff}$, tedy $u(\mathrm{ff}) = 1$, což nejde. **Spor: $M$ je nesplnitelná, tedy $S'$ je nesplnitelná a $S \models p$. Petr na výlet pojede.**

> [!lidsky] Lidsky
> Rezoluce je řetěz „když je tohle i tohle, pak musí být i tohle“. Každá nová klauzule platí všude, kde platily ty staré, takže ji smíš přidat bez změny odpovědi. Když se dojde k nemožnému ($\mathrm{ff}$, „$q$ a zároveň ne $q$“), původní množina nešla splnit. Tabulka by měla $2^5 = 32$ řádků; tady stačilo 5 kroků.

> [!question]- Kontrola: v kolika ohodnoceních je pravdivá množina $S$ (bez $\neg p$)?
> Ve **4** z 32: $(p, q, r, s, t) \in \{(1,0,0,0,0), (1,0,1,0,0), (1,0,1,0,1), (1,0,1,1,1)\}$. Ve všech je $p = 1$ (a $q = 0$), což souhlasí s $S \models p$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- Jak u konečné množiny $\{\varphi_1, \dots, \varphi_n\}$ nahradíš $u(S)$ jednou formulí, a proč to u nekonečné nejde?
> $u(S) = u(\varphi_1 \wedge \dots \wedge \varphi_n)$, tedy **konjunkce**. Množina formulí může být nekonečná a nekonečnou konjunkci zapsat nejde.

> [!karta|03]- Proč je prázdná množina formulí pravdivá v každém ohodnocení?
> $u(\emptyset) = 1$ znamená $\forall \varphi\, (\varphi \in \emptyset \Rightarrow u(\varphi) = 1)$. Předpoklad $\varphi \in \emptyset$ je vždy nepravdivý, takže implikace je **vždy pravdivá**.

> [!karta|04]- Platí i „každá formule z $\emptyset$ je nepravdivá v $u$“? Plyne z toho $u(\emptyset) = 0$?
> Platí (stejný důvod), ale $u(\emptyset) = 0$ **neplyne**: to by vyžadovalo $\exists \varphi\, (\varphi \in \emptyset \wedge u(\varphi) = 0)$ a takový svědek neexistuje.

> [!karta|05]- Jak je definován sémantický důsledek $S \models \varphi$ a jak ho zapíšeš přes nerovnost?
> $\varphi$ je pravdivá v každém ohodnocení, kde je pravdivé celé $S$. Ekvivalentně **$u(S) \le u(\varphi)$ pro všechna $u$**.

> [!karta|06]- Jak souvisí $\alpha \models \varphi$ s implikací?
> $\alpha \models \varphi$, právě když **$\alpha \Rightarrow \varphi$ je tautologie** (protože $u(\alpha \Rightarrow \varphi) = 1$ iff $u(\alpha) \le u(\varphi)$).

> [!karta|07]- Co je sémantickým důsledkem nesplnitelné množiny $S$ a proč?
> **Každá formule**: neexistuje ohodnocení s $u(S) = 1$, takže podmínku důsledku nejde porušit.

> [!karta|08]- Co znamená $\models \varphi$ (důsledek prázdné množiny)?
> $\varphi$ je **tautologie**, protože $u(\emptyset) = 1$ v každém ohodnocení.

> [!karta|10]- Dokaž směr „⇒“ věty o sémantickém důkazu sporem.
> Nechť $S \models \varphi$ a $u$ libovolné. Je-li $u(S) = 1$, pak $u(\varphi) = 1$, tedy $u(\neg\varphi) = 0$ a $u(S') = 0$. Je-li $u(S) = 0$, pak $u(S') = 0$, protože $S \subseteq S'$. Tedy $S'$ je **nesplnitelná**.

> [!karta|11]- Jak převedeš otázky „je $\varphi$ tautologie?“ a „je $\varphi$ kontradikce?“ na (ne)splnitelnost?
> Tautologie: je **$\{\neg\varphi\}$ nesplnitelná**? Kontradikce: je **$\{\varphi\}$ nesplnitelná**?

> [!karta|12]- Jak převedeš $\varphi \mathrel{\vert\!=\!\vert} \psi$ na nesplnitelnost?
> $\varphi \models \psi$ a $\psi \models \varphi$, tedy **obě** množiny $\{\varphi, \neg\psi\}$ a $\{\psi, \neg\varphi\}$ musí být nesplnitelné.

> [!karta|13]- Proč je formule v CNF $c_1 \wedge \dots \wedge c_n$ splnitelná, právě když je splnitelná množina $\{c_1, \dots, c_n\}$?
> Konjunkce je pravdivá, právě když jsou pravdivé všechny členy, takže obě jsou pravdivé **ve stejných ohodnoceních** (mají stejné svědky).

> [!karta|14]- Proč smíš z množiny klauzulí vypustit tautologii, např. $a \vee \neg a \vee b$?
> Tautologie je pravdivá v každém $u$, takže **$u(S \cup \{\mathrm{tt}\}) = u(S)$**: odpověď na splnitelnost se nezmění.

> [!karta|15]- Proč platí $\{\alpha \vee x, \beta \vee \neg x\} \models \alpha \vee \beta$?
> Je-li $u(x) = 1$, je $\neg x$ nepravdivé, takže platí $\beta$. Je-li $u(x) = 0$, platí $\alpha$. V obou případech **$\alpha \vee \beta$**. Proměnná $x$ sama nezařídí pravdivost obou klauzulí.

> [!karta|16]- Co znamená, když při rezoluci vznikne $\mathrm{ff}$?
> Každá rezolventa je důsledkem, takže by platila v každém $u$ s $u(M) = 1$; $\mathrm{ff}$ ale nikde neplatí. Tedy **$M$ je nesplnitelná**.

### Příklady na procvičení

> [!priklad|17]- Je $\{a \Rightarrow b, \neg b\}$ splnitelná?
> **Ano**, svědek $u(a) = u(b) = 0$: $0 \Rightarrow 0$ je $1$ a $\neg 0 = 1$.

> [!priklad|18]- Je $\{a \Rightarrow b, \neg b, a \vee b\}$ splnitelná?
> **Ne.** $\neg b$ vynutí $b = 0$, pak $a \vee b$ vynutí $a = 1$ a implikace $1 \Rightarrow 0$ je nepravdivá.

> [!priklad|19]- Platí $\{a \Rightarrow b, a \vee b\} \models a$? A $\models b$?
> $\not\models a$: protipříklad $a = 0, b = 1$. **$\models b$**: kdyby $b = 0$, pak $a = 1$ a implikace je nepravdivá.

> [!priklad|20]- Ověř, že $\{a, a \Rightarrow b\} \models b$.
> Obě formule jsou pravdivé jen pro $a = b = 1$ a tam je **$b = 1$** (modus ponens).

> [!priklad|21]- Uprav klauzule $a \vee a \vee b$ a $a \vee \neg a \vee b$ pro klauzální tvar.
> $a \vee a \vee b \mathrel{\vert\!=\!\vert} a \vee b$, zůstane **$a \vee b$**; $a \vee \neg a \vee b \mathrel{\vert\!=\!\vert} \mathrm{tt}$, **vypustí se**.

> [!priklad|22]- Převeď $q \Rightarrow (s \wedge \neg r)$ na klauzule.
> $\neg q \vee (s \wedge \neg r) \mathrel{\vert\!=\!\vert} (\neg q \vee s) \wedge (\neg q \vee \neg r)$, klauzule **$\neg q \vee s$, $\neg q \vee \neg r$**.

> [!priklad|23]- Zformalizuj: „Jestliže pojede Quido, pojede Simona a nepojede Renata.“ a „Jestliže pojede Tomáš, pojede i Renata.“
> **$q \Rightarrow (s \wedge \neg r)$** a **$t \Rightarrow r$**.

> [!priklad|24]- Rozhodni rezolucí, zda $\{p \vee q, q \Rightarrow (s \wedge \neg r), t \Rightarrow r, s \Rightarrow t\} \models p$.
> $\mathrm{Kl}(S \cup \{\neg p\}) = \{p \vee q, \neg q \vee s, \neg q \vee \neg r, \neg t \vee r, \neg s \vee t, \neg p\}$. Rezolventy: $q$; $\neg q \vee t$; $\neg q \vee r$; $\neg q$; $\mathrm{ff}$. Nesplnitelná, tedy **$S \models p$**.

---
← [[LGR 03 – Disjunktivní a konjunktivní normální forma|1. 10. 2026 Disjunktivní a konjunktivní normální forma]] · [[LGR 05 – Rezoluční princip|9. 10. 2026 Rezoluční princip]] →

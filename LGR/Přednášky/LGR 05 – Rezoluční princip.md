---
predmet: LGR
prednaska: 5
datum: 2026-10-09
zdroj: "Prezentace 3 (Sémantika, rezoluční metoda), slajdy 13–26"
tags: [prednaska, LGR]
---

# LGR 05 – Rezoluční princip

*Přednáška 5 · pátek 9. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 3 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_3.pdf) · [Verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_3a.pdf)

Témata: `komplementární literály` · `prázdná klauzule` · `populace rezolvent R*(S)` · `zamítací strom` · `rezoluční princip` · `počet klauzulí 3ⁿ` · `ekvisplnitelnost` · `eliminace proměnné` · `rezoluční tabulka`

Minule se na příkladu s výletem ukázalo, že z množiny klauzulí jde odvozovat [[rezolventa|rezolventy]], a když vznikne $\mathrm{ff}$, množina je nesplnitelná. Dnes se to zformalizuje: rezolventa přesně, systematické vyrábění všech rezolvent $R^*(S)$ a hlavní věta, *rezoluční princip*: konečná množina klauzulí je nesplnitelná, **právě když** se z ní dá vyrobit $\mathrm{ff}$. Snadný směr se dokáže hned; pro těžký směr se dokáže klíčové tvrzení o eliminaci jedné proměnné, na kterém stojí rezoluční tabulka.

## §0 Přehled na jedné stránce

| pojem | zápis | význam |
|---|---|---|
| [[rezolventa]] | $\mathrm{res}_x(\gamma \vee x, \delta \vee \neg x) = \gamma \vee \delta$ | škrtne se **jedna** dvojice komplementárních literálů |
| [[prázdná klauzule]] | $\mathrm{res}_x(x, \neg x) = \mathrm{ff}$ | disjunkce bez členů, nepravdivá v každém ohodnocení |
| [[populace rezolvent]] | $R^0(S) = S$, $R^{i+1}(S) = R(R^i(S))$, $R^*(S) = \bigcup_i R^i(S)$ | všechny klauzule, které jdou z $S$ vyrobit |
| [[rezoluční princip]] | $S$ splnitelná iff $\mathrm{ff} \notin R^*(S)$ | věta, na které stojí rezoluční metoda |
| počet klauzulí | $3^n$ nad $n$ proměnnými (v základním tvaru) | proto se výroba rezolvent zastaví |
| [[věta o eliminaci proměnné\|eliminace proměnné]] | $S$ splnitelná iff $S_0 \cup R_x$ splnitelná | proměnnou $x$ jde z množiny „vyrezolvovat“ |
| [[rezoluční tabulka]] | postupně $x_1, \dots, x_n$ | na konci $\{\mathrm{ff}\}$ (nesplnitelná) nebo $\emptyset$ (splnitelná) |

## §1 Rezolventa přesně

> [!definice] Komplementární literály a rezolventa · slajd 14
> Literály $x$ a $\neg x$ (stejná proměnná, jednou pozitivně, jednou negativně) jsou *komplementární*. Nechť $\alpha = \gamma \vee x$ a $\beta = \delta \vee \neg x$ jsou klauzule. *Rezolventa* $\alpha$ a $\beta$ přes $x$ je
>
> $$
> \mathrm{res}_x(\alpha, \beta) = \gamma \vee \delta,
> $$
>
> tedy [[maxterm|klauzule]] ze všech [[literál|literálů]] $\alpha$ a $\beta$ (každý jen jednou) kromě dvojice $x$, $\neg x$.

^def-komplementarni

> [!lidsky] Lidsky
> „Jede Simona, nebo nejede Quido“ a „nejede Simona, nebo jede Tomáš“. Simona nemůže jet i nejet, takže jedna z klauzulí musí platit díky svému „druhému konci“: nejede Quido, nebo jede Tomáš. Proměnnou, ve které se klauzule hádají, škrtneš a zbytky spojíš „nebo“.

> [!example] Výpočet · slajd 14
> $\mathrm{res}_x(x \vee y \vee z, \ \neg x \vee y \vee w) = y \vee z \vee w$ ($y$ je v obou, napíše se jednou).

### Prázdná klauzule

Když z obou klauzulí zbude jen dvojice $x$, $\neg x$, nezbyde nic:

$$
\mathrm{res}_x(x, \neg x) = \bigvee_{i=1}^{0} \alpha_i = \mathrm{ff}.
$$

> [!definice] Prázdná klauzule
> Disjunkce bez jediného členu se nazývá *prázdná klauzule* a ztotožňuje se s $\mathrm{ff}$: je **nepravdivá v každém ohodnocení**. Disjunkce je pravdivá, když je pravdivý aspoň jeden člen, a prázdná disjunkce žádný člen nemá.

^def-prazdna-klauzule

> [!lidsky] Lidsky
> Klauzule je seznam „stačí splnit aspoň jedno z …“. Prázdný seznam nejde splnit nikdy, protože není z čeho vybírat. Je to opak [[LGR 04 – Sémantický důsledek a klauzální tvar#^prazdna-mnozina|prázdné množiny formulí]], která je naopak pravdivá vždy.

Stejný výsledek dá i úvaha bez prázdné disjunkce: $\neg x \mathrel{\vert\!=\!\vert} \neg x \vee \mathrm{ff}$, takže $\mathrm{res}_x(x, \neg x) = \mathrm{res}_x(x, \neg x \vee \mathrm{ff}) = \mathrm{ff}$. ^prazdna-alt

### Rezolvuje se vždy jen přes jednu proměnnou

> [!pozor] Častá chyba: škrtnout dvě dvojice naráz
> Klauzule $\alpha = x \vee y$ a $\beta = \neg x \vee \neg y \vee z$ mají komplementární dvojice dvě. Škrtnout obě a napsat „rezolventa je $z$“ je **chyba**: $\mathrm{res}(\alpha, \beta) \ne z$.
> - Přes $x$: $\mathrm{res}_x(\alpha, \beta) = y \vee \neg y \vee z \mathrel{\vert\!=\!\vert} \mathrm{tt}$, tautologie, nic se nedozvíš.
> - Přes $y$ stejně: $x \vee \neg x \vee z \mathrel{\vert\!=\!\vert} \mathrm{tt}$.
>
> Proč $z$ neplyne: pravdivost obou klauzulí jde zařídit přes $x$ a $y$, třeba $u(x) = 1$, $u(y) = 0$. Pak $u(\alpha) = 1$, $u(\beta) = 1$ a $z$ může být $0$ i $1$. Máš dva svědky splnitelnosti, v jednom je $z$ nepravdivé.

^dve-dvojice

> [!veta] Tvrzení · slajd 15
> **$\{\alpha, \beta\} \models \mathrm{res}_x(\alpha, \beta)$.** Proto přidání rezolventy k množině $S$ nezmění, ve kterých ohodnoceních je $S$ pravdivá.
>
> > [!note]- Důkaz
> > Pravdivost $\alpha = \gamma \vee x$ a $\beta = \delta \vee \neg x$ nejde zařídit jen přes $x$: $x$ je v jedné klauzuli pozitivně a ve druhé negativně, takže jednu z nich vždy pokazí. Je-li $u(x) = 1$, je $u(\neg x) = 0$ a musí platit $u(\delta) = 1$. Je-li $u(x) = 0$, musí platit $u(\gamma) = 1$. V obou případech je pravdivý aspoň jeden z „konců“, tedy $u(\gamma \vee \delta) = 1$.

^res-dusledek

> [!lidsky] Lidsky
> Rezolventa je „bezpečný závěr“: nic nového nevymýšlí, jen zapíše, co z obou klauzulí naráz plyne. Proto ji smíš do množiny přidat, aniž by se změnilo, kdy je množina pravdivá.

## §2 Populace všech rezolvent

> [!definice] $R(S)$, $R^i(S)$, $R^*(S)$ · slajd 16
> Pro množinu klauzulí $S$:
> - $R(S) = S \cup \{\text{všechny rezolventy dvojic klauzulí z } S\}$,
> - $R^0(S) = S$, $\ R^1(S) = R(S)$, $\ R^{i+1}(S) = R(R^i(S))$,
> - $R^*(S) = \bigcup_{i \ge 0} R^i(S)$, *populace všech rezolvent* množiny $S$.

^def-populace

> [!lidsky] Lidsky
> Rodokmen: $R^1(S)$ jsou původní klauzule a jejich „děti“, $R^2(S)$ k tomu přidá „vnoučata“ (rezolventy, kde aspoň jeden rodič je z první generace) atd. Každá generace obsahuje všechny předchozí. $R^*(S)$ je celý rodokmen, všechno, co z $S$ rezolucí kdy vznikne.

Každá rezolventa je [[sémantický důsledek|důsledkem]] svých rodičů (§1), takže **$S$ a $R^*(S)$ jsou pravdivé ve stejných ohodnoceních**. Kdyby se v $R^*(S)$ objevilo $\mathrm{ff}$, muselo by platit všude, kde platí $S$, a to nejde. ^stejna-ohodnoceni

> [!example] První generace pro výlet
> Klauzální tvar z [[LGR 04 – Sémantický důsledek a klauzální tvar#^priklad-vylet|minulé přednášky]]: $M = \{p \vee q,\ \neg q \vee s,\ \neg q \vee \neg r,\ \neg t \vee r,\ \neg s \vee t,\ \neg p\}$. Systematicky se zkouší každá dvojice s komplementárními literály:
>
> | dvojice | přes | rezolventa |
> |---|---|---|
> | $p \vee q$, $\neg p$ | $p$ | $q$ |
> | $p \vee q$, $\neg q \vee s$ | $q$ | $p \vee s$ |
> | $p \vee q$, $\neg q \vee \neg r$ | $q$ | $p \vee \neg r$ |
> | $\neg q \vee s$, $\neg s \vee t$ | $s$ | $\neg q \vee t$ |
> | $\neg q \vee \neg r$, $\neg t \vee r$ | $r$ | $\neg q \vee \neg t$ |
> | $\neg t \vee r$, $\neg s \vee t$ | $t$ | $r \vee \neg s$ |
>
> $R^1(M)$ má tedy $6 + 6 = 12$ klauzulí. Dál rostou počty $|R^2(M)| = 23$ a $|R^3(M)| = 28$ a $\mathrm{ff}$ se poprvé objeví v $R^3(M)$.

^priklad-r1

> [!definice] Zamítací strom · slajd 18
> Strom, jehož listy jsou klauzule z $S$, každý vnitřní vrchol je rezolventa svých dvou potomků a kořen je $\mathrm{ff}$, se nazývá *zamítací strom*. Když ho najdeš, máš důkaz, že $\mathrm{ff} \in R^*(S)$, tedy že $S$ je nesplnitelná.

^def-zamitaci-strom

> [!lidsky] Lidsky
> Zamítací strom je „rodokmen“ prázdné klauzule: dole předpoklady, každé patro výš je rezolventa dvou klauzulí pod ní a nahoře spor $\mathrm{ff}$. Kdo ukáže takový rodokmen, dokázal, že pravidla nejdou splnit naráz.

> [!example] Zamítací strom ze slajdu 18
> $M = \{z \Rightarrow (x \vee y),\ x \Leftrightarrow y,\ \neg x \wedge (y \vee z)\}$ má klauzální tvar $S = \{\neg z \vee x \vee y,\ \neg x \vee y,\ \neg y \vee x,\ \neg x,\ y \vee z\}$. Strom: $\mathrm{res}_x(\neg z \vee x \vee y, \neg x) = \neg z \vee y$, $\mathrm{res}_x(\neg y \vee x, \neg x) = \neg y$, $\mathrm{res}_z(\neg z \vee y, y \vee z) = y$ a $\mathrm{res}_y(\neg y, y) = \mathrm{ff}$. Množina $S$, a tedy i $M$, je **nesplnitelná**.

> [!obrazek] Zamítací strom ze slajdu 18
> ![[lgr05-zamitaci-strom.png]]
> *Oranžově klauzule z $S$ (list $\neg x$ se smí použít dvakrát), modře rezolventy, červeně kořen $\mathrm{ff}$, šedě proměnná, přes kterou se rezolvuje.*

> [!obrazek] Zamítací strom pro výlet a generace rezolvent
> ![[lgr05-populace.png]]
> *Oranžově klauzule z $S$, červeně $\neg p$ (negovaný závěr), modře rezolventy, šedě proměnná, přes kterou se rezolvuje. Pruhy jsou generace: rezolventa leží v $R^{i+1}$, když je její mladší rodič v $R^i$. Vlevo počet klauzulí v celé generaci.*

Tady bylo štěstí: [[zamítací strom]] se našel rychle. Kdyby se nenašel, musí se zkoušet dál a dál, a hlavně:

> [!pozor] Splnitelnost se nedokáže tím, že ff zatím nevzniklo
> Když je $S$ splnitelná, musíš vyrobit **celou** $R^*(S)$, abys měl jistotu, že v ní $\mathrm{ff}$ není. Nenalezený zamítací strom nic nedokazuje, dokud nejsou vyzkoušené všechny dvojice ve všech generacích. Rezolventy přitom rostou rychle (u výletu $6 \to 12 \to 23 \to 28$), proto se dál zavede úspornější [[rezoluční tabulka]].

## §3 Rezoluční princip

> [!veta] Rezoluční princip · slajd 17
> ==Nechť $S$ je konečná množina klauzulí.== Pak **$S$ je splnitelná, právě když $R^*(S)$ neobsahuje $\mathrm{ff}$.** ($R^*(S)$ je [[populace rezolvent]].)
>
> > [!note]- Důkaz směru „⇒“
> > Dokazuje se *[[obměněná implikace|obměnou]]*: místo „$S$ splnitelná $\Rightarrow$ $\mathrm{ff} \notin R^*(S)$“ se dokáže „$\mathrm{ff} \in R^*(S)$ $\Rightarrow$ $S$ nesplnitelná“.
> >
> > Nechť $\mathrm{ff} \in R^*(S)$. Každá klauzule z $R^*(S)$ je sémantickým důsledkem $S$, takže $S \models \mathrm{ff}$. Kdyby $u(S) = 1$ pro nějaké $u$, bylo by i $u(\mathrm{ff}) = 1$. Takové $u$ neexistuje, tedy **$S$ je nesplnitelná**.
> >
> > **Jinak:** podle [[LGR 04 – Sémantický důsledek a klauzální tvar#^veta-le|tvrzení z minula]] je $S \models \mathrm{ff}$, právě když pro každé $u$ platí $u(S) \le u(\mathrm{ff}) = 0$. Tedy $u(S) = 0$ pro všechna $u$ a $S$ je nesplnitelná.
>
> > [!note]- Směr „⇐“ (dokončí se přes rezoluční tabulku, §5)
> > Je třeba ukázat: když $\mathrm{ff} \notin R^*(S)$, je $S$ splnitelná. Tady už nestačí, že rezolventy jsou důsledky; je potřeba **najít svědka**. K tomu slouží [[věta o eliminaci proměnné]] (§4) a rezoluční tabulka (§5).

^veta-rezolucni-princip

> [!lidsky] Lidsky
> Rezoluce je úplný detektor sporu. Jeden směr je jednoduchý: když z pravidel odvodíš nesmysl, pravidla nejdou splnit. Druhý směr je překvapivý: když ani po vyzkoušení všeho nesmysl nevznikne, pravidla **určitě** splnit jdou, rezoluce nic „nepřehlédne“.

> [!definice] Obměněná implikace
> $\varphi \Rightarrow \psi \mathrel{\vert\!=\!\vert} \neg\psi \Rightarrow \neg\varphi$. Místo „z $\varphi$ plyne $\psi$“ jde ekvivalentně dokázat „když neplatí $\psi$, neplatí ani $\varphi$“.

^def-obmena

> [!lidsky] Lidsky
> „Když prší, je mokro“ znamená totéž co „když není mokro, neprší“. Důkaz obměnou se hodí, když je jednodušší vyjít z negace závěru.

> [!pozor] Obměna není obrácená implikace
> $\psi \Rightarrow \varphi$ („když je mokro, prší“) s $\varphi \Rightarrow \psi$ ekvivalentní **není**; mokro může být od kropení. Ekvivalentní je jen obměna s oběma negacemi.

### Proč se výroba rezolvent zastaví

Nechť $A = \{x_1, \dots, x_n\}$ je konečná množina proměnných. V klauzuli (bez opakování a bez komplementárních dvojic) je každá proměnná v jednom ze tří stavů:

| stav $x_i$ v klauzuli | kód |
|---|---|
| je tam pozitivně ($x_i$) | $1$ |
| je tam negativně ($\neg x_i$) | $-1$ |
| není tam | $0$ |

Klauzule tedy odpovídají $n$-ticím z $\{1, -1, 0\}$ a těch je **$3^n$** (včetně $(0, \dots, 0)$, což je $\mathrm{ff}$). Třeba $x_1 \vee \neg x_2$ nad $\{x_1, x_2, x_3\}$ je $(1, -1, 0)$. Generace $R^0(S) \subseteq R^1(S) \subseteq \dots$ jsou podmnožiny této konečné množiny, takže od nějakého $m$ už nic nového nepřibude: $R^*(S) = R^m(S)$. ^pocet-klauzuli

> [!navic] A co tautologické rezolventy?
> Rezolventa může vyjít tautologie (§1, $y \vee \neg y \vee z$). Ty se z množiny klauzulí smějí vypustit (minule: $u(S \cup \{\mathrm{tt}\}) = u(S)$). Kdyby se nechávaly, je možností pro každou proměnnou čtyři (i oba literály naráz) a klauzulí $4^n$, pořád konečně mnoho, takže zastavení platí tak jako tak.

## §4 Eliminace jedné proměnné

> [!definice] Ekvisplnitelné množiny · slajd 19
> Množiny formulí $S$ a $T$ jsou *ekvisplnitelné*, když $S$ je [[splnitelná množina formulí|splnitelná]], právě když $T$ je splnitelná.

^def-ekvisplnitelne

> [!lidsky] Lidsky
> Obě jdou splnit, nebo obě ne. Nemusí mít stejné svědky, dokonce ani stejné proměnné. Na otázku „jde to splnit?“ ale dají stejnou odpověď, takže smíš řešit tu jednodušší.

> [!definice] Základní tvar klauzulí · slajd 20
> Množina klauzulí je v *základním tvaru*, když žádná klauzule neobsahuje stejnou proměnnou dvakrát, tedy ani dvakrát týž literál, ani komplementární dvojici (taková klauzule je tautologie a vypustí se).

^def-zakladni-tvar

> [!lidsky] Lidsky
> Uklizené klauzule: v každé je každá proměnná nejvýš jednou. [[klauzální tvar|Klauzální tvar]] z minula je přesně takový.

Pro množinu $S$ v [[základní tvar klauzulí|základním tvaru]] a proměnnou $x$ se $S$ rozdělí na tři části:

- $S_x$: klauzule, které obsahují $x$ pozitivně,
- $S_{\neg x}$: klauzule, které obsahují $\neg x$,
- $S_0$: klauzule, ve kterých $x$ není.

Díky základnímu tvaru jsou tyto části **navzájem disjunktní** (žádná klauzule nemá $x$ i $\neg x$). Dál $R_x$ je množina všech rezolvent přes $x$ dvojic z $S_x \times S_{\neg x}$, kromě tautologií. ^rozklad

> [!obrazek] Rozklad S a eliminace proměnné x
> ![[lgr05-rozklad.png]]
> *Modře $S_x$, červeně $S_{\neg x}$, oranžově $S_0$. Vpravo zeleně nová množina $S_0 \cup R_x$: proměnná $x$ v ní už není.*

> [!veta] Věta o eliminaci proměnné · slajdy 21–22
> ==Nechť $A$ je konečná množina proměnných, $S$ (tedy konečná) množina klauzulí nad $A$ v základním tvaru a $x \in A$.== Pak **$S$ je splnitelná, právě když $S_0 \cup R_x$ je splnitelná**, tj. $S$ a $S_0 \cup R_x$ jsou ekvisplnitelné.
>
> > [!note]- Důkaz
> > **„⇒“** (to už víme): je-li $u(S) = 1$, pak $u(S_0) = 1$, protože $S_0 \subseteq S$, a $u(R_x) = 1$, protože rezolventy jsou důsledky klauzulí z $S$ (§1). Svědek pro $S$ je svědkem i pro $S_0 \cup R_x$.
> >
> > **„⇐“:** Ukáže se, že svědka pro $S_0 \cup R_x$ (kde $x$ není) jde šikovnou volbou $u(x)$ předělat na svědka pro $S$.
> >
> > Předpokládej, že $S_0 \cup R_x$ je splnitelná, a zvol svědka $u$: $u(S_0 \cup R_x) = 1$. Protože v $S_0 \cup R_x$ není $x$, jsou to ve skutečnosti **dva svědci**, kteří se liší jen hodnotou $x$:
> > - $u_0$: $x \mapsto 0$, jinde jako $u$,
> > - $u_1$: $x \mapsto 1$, jinde jako $u$.
> >
> > Oba splňují $S_0$ i $R_x$. Je aspoň jeden z nich svědkem pro $S$?
> >
> > 1. $u_0(S_{\neg x}) = 1$ díky $\neg x$. Pokud náhodou (díky ostatním proměnným) i $u_0(S_x) = 1$, je $u_0(S) = 1$ a **svědkem je $u_0$**.
> > 2. Jinak $u_0(S_x) = 0$: existuje klauzule $x \vee \gamma \in S_x$ s $u_0(x \vee \gamma) = 0$. Pak $u_0(\gamma) = 0$, a protože $\gamma$ neobsahuje $x$, i $u_1(\gamma) = 0$.
> > 3. $u_1(S_x) = 1$ díky $x$. Pokud náhodou i $u_1(S_{\neg x}) = 1$, je $u_1(S) = 1$ a **svědkem je $u_1$**.
> > 4. Jinak $u_1(S_{\neg x}) = 0$: existuje $\neg x \vee \delta \in S_{\neg x}$ s $u_1(\neg x \vee \delta) = 0$. Pak $u_1(\delta) = 0$ a, protože $\delta$ neobsahuje $x$, i $u_0(\delta) = 0$.
> >
> > **Situace 4 (po 2) nemůže nastat.** Rezolventa $\mathrm{res}_x(x \vee \gamma, \neg x \vee \delta) = \gamma \vee \delta$ patří do $R_x$ (nebo je tautologie), takže $u_0(\gamma \vee \delta) = u_1(\gamma \vee \delta) = 1$. V situaci 4 je ale $\gamma$ i $\delta$ nepravdivé v $u_0$ i $u_1$, tedy $u_0(\gamma \vee \delta) = 0$. **Spor.** Proto nastane 1 nebo 3 a jeden z $u_0$, $u_1$ je svědkem splnitelnosti $S$.

^veta-eliminace

> [!obrazek] Proč nemůžou selhat oba svědci
> ![[lgr05-svedci.png]]
> *Situace 4 z důkazu: $u_0$ pokazí klauzuli $x \vee \gamma$, $u_1$ pokazí $\neg x \vee \delta$ (červeně). Pak jsou $\gamma$ i $\delta$ nepravdivé v obou, jenže jejich rezolventa $\gamma \vee \delta$ leží v $R_x$ a musí být pravdivá (zeleně).*

> [!lidsky] Lidsky
> Rezolventy přes $x$ „si pamatují“ všechno, co klauzule s $x$ požadovaly od ostatních proměnných. Jakmile je máš, $x$ sám už nic nepřidá a klauzule s $x$ můžeš zahodit. Na konci se $x$ dodá zpátky: zkusíš $x = 0$, a když to nevyjde, $x = 1$ vyjde určitě.

> [!example] Malý příklad
> $S = \{x \vee y,\ x \vee z \vee t,\ \neg x,\ y \vee z\}$. Pak $S_x = \{x \vee y, x \vee z \vee t\}$, $S_{\neg x} = \{\neg x\}$, $S_0 = \{y \vee z\}$ a $R_x = \{y,\ z \vee t\}$. Množina $S_0 \cup R_x = \{y \vee z, y, z \vee t\}$ má svědka $u(y) = u(z) = 1$, $u(t) = 0$. Zkus $u_0$ ($x = 0$): $\neg x$ platí, $x \vee y$ díky $y$, $x \vee z \vee t$ díky $z$. Svědkem pro $S$ je $u_0$.

> [!pozor] Kde se použil základní tvar
> Že $\gamma$ a $\delta$ neobsahují $x$ (takže $u_0$ a $u_1$ na nich dávají stejnou hodnotu), plyne ze základního tvaru: v $x \vee \gamma$ je $x$ jen jednou a $\neg x$ tam není. Bez toho by $S_x$ a $S_{\neg x}$ nemusely být disjunktní a důkaz by nefungoval.

## §5 Rezoluční tabulka

Po přidání všech rezolvent přes $x$ smíš klauzule s $x$ „umrtvit“ (vyhodit): podle [[věta o eliminaci proměnné|věty o eliminaci]] se splnitelnost nezmění. Některé rezolventy, které by s nimi ještě vznikly, tím zapomeneš, ale k rozhodnutí nejsou potřeba.

> [!definice] Rezoluční tabulka · slajdy 23–24
> Vstup: konečná množina klauzulí $S$ v základním tvaru nad $A = \{x_1, \dots, x_n\}$.
> 1. Pro $i = 1, \dots, n$: rozděl $S$ na $S_0$, $S_{x_i}$, $S_{\neg x_i}$, spočítej $R_{x_i}$ a polož $S := S_0 \cup R_{x_i}$.
> 2. Na konci v $S$ není žádná proměnná, takže $S = \{\mathrm{ff}\}$, nebo $S = \emptyset$.
> 3. Je-li $S = \{\mathrm{ff}\}$, původní množina je **nesplnitelná**; je-li $S = \emptyset$, je **splnitelná**.

^def-rezolucni-tabulka

> [!lidsky] Lidsky
> Místo rodokmenu všech rezolvent se proměnné „vyrezolvují“ jedna po druhé. Po každém kroku zmizí jedna proměnná a odpověď na splnitelnost zůstane stejná. Po $n$ krocích zbyde buď spor, nebo nic.

> [!obrazek] Co vyrobí tabulka oproti R*(S)
> ![[lgr05-mnoziny.png]]
> *Šedě všech $3^n$ klauzulí nad $A$, modře $R^*(S)$, zeleně $T$: klauzule z $S$ a rezolventy, které vyrobí rezoluční tabulka, oranžově $S$. Tabulka vyrobí jen část rezolvent, ale $\mathrm{ff}$ najde právě tehdy, když je v $R^*(S)$ (červeně).*

> [!navic] Jak tabulka dokončí důkaz rezolučního principu
> Platí $T \subseteq R^*(S)$ (rezolventy rezolvent jsou v rodokmenu). Je-li $\mathrm{ff} \notin R^*(S)$, pak $\mathrm{ff} \notin T$, tabulka skončí s $\emptyset$, která je splnitelná, a podle věty o eliminaci je splnitelná každá předchozí množina až po $S$. To je směr „⇐“. Svědka dostaneš pozpátku (slajd 25): začni libovolným ohodnocením, postupně pro $x_n, \dots, x_1$ zkus $x_i = 0$, a když to klauzule z daného kroku pokazí, dej $x_i = 1$.

> [!example] Výlet tabulkou (pořadí $p, q, r, s, t$)
> | krok | $S_x$ | $S_{\neg x}$ | $R_x$ | nová $S = S_0 \cup R_x$ |
> |---|---|---|---|---|
> | $p$ | $p \vee q$ | $\neg p$ | $q$ | $q,\ \neg q \vee s,\ \neg q \vee \neg r,\ \neg t \vee r,\ \neg s \vee t$ |
> | $q$ | $q$ | $\neg q \vee s$, $\neg q \vee \neg r$ | $s$, $\neg r$ | $s,\ \neg r,\ \neg t \vee r,\ \neg s \vee t$ |
> | $r$ | $\neg t \vee r$ | $\neg r$ | $\neg t$ | $s,\ \neg t,\ \neg s \vee t$ |
> | $s$ | $s$ | $\neg s \vee t$ | $t$ | $\neg t,\ t$ |
> | $t$ | $t$ | $\neg t$ | $\mathrm{ff}$ | $\mathrm{ff}$ |
>
> Konec $\{\mathrm{ff}\}$: nesplnitelná, stejně jako zamítacím stromem. Celkem 6 rezolvent místo 22 v $R^3$.

^priklad-tabulka

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč se rezolvuje vždy jen přes jednu dvojici komplementárních literálů?
> Škrtnutí dvou dvojic naráz **není důsledek**: z $x \vee y$ a $\neg x \vee \neg y \vee z$ by vyšlo $z$, ale $u(x) = 1$, $u(y) = 0$, $u(z) = 0$ splní obě klauzule a $z$ ne. Rezoluce přes jednu proměnnou tu dá jen tautologie.

> [!karta|02]- Proč je $\mathrm{res}_x(x, \neg x) = \mathrm{ff}$?
> Zbyde **prázdná disjunkce**, ta nemá pravdivý člen, je tedy nepravdivá všude. Jinak: $\neg x \mathrel{\vert\!=\!\vert} \neg x \vee \mathrm{ff}$ a $\mathrm{res}_x(x, \neg x \vee \mathrm{ff}) = \mathrm{ff}$.

> [!karta|03]- Proč jsou $S$ a $R^*(S)$ pravdivé ve stejných ohodnoceních?
> $S \subseteq R^*(S)$ a každá rezolventa je **sémantickým důsledkem** svých rodičů, takže platí všude, kde platí $S$.

> [!karta|04]- Dokaž: je-li $S$ splnitelná, pak $\mathrm{ff} \notin R^*(S)$.
> Obměnou: $\mathrm{ff} \in R^*(S)$ ⇒ $S \models \mathrm{ff}$. Kdyby $u(S) = 1$, bylo by $u(\mathrm{ff}) = 1$, nemožné. Tedy **$S$ nesplnitelná**. (Nebo: $u(S) \le u(\mathrm{ff}) = 0$ pro všechna $u$.)

> [!karta|05]- Proč je nad $n$ proměnnými právě $3^n$ klauzulí (v základním tvaru)?
> Každá proměnná je v klauzuli **pozitivně, negativně, nebo vůbec** ($1, -1, 0$), klauzule odpovídá $n$-tici z $\{1, -1, 0\}$. $(0, \dots, 0)$ je $\mathrm{ff}$.

> [!karta|06]- Proč se výroba rezolvent nad konečnou $A$ zastaví?
> Generace $R^0 \subseteq R^1 \subseteq \dots$ jsou podmnožiny **konečné** množiny všech klauzulí ($3^n$), takže od nějakého $m$ nic nepřibude: $R^*(S) = R^m(S)$.

> [!karta|07]- Proč nestačí na důkaz splnitelnosti, že se zamítací strom zatím nenašel?
> Rezoluční princip mluví o **celé** $R^*(S)$: splnitelnost plyne až z toho, že $\mathrm{ff}$ nevznikne v žádné generaci, tedy po vyrobení všech rezolvent.

> [!karta|08]- Co jsou $S_0$, $S_x$, $S_{\neg x}$, $R_x$ a proč jsou $S_0$, $S_x$, $S_{\neg x}$ disjunktní?
> Klauzule bez $x$, s $x$, s $\neg x$; $R_x$ = rezolventy přes $x$ dvojic z $S_x \times S_{\neg x}$ bez tautologií. Disjunktní díky **základnímu tvaru**: žádná klauzule nemá $x$ i $\neg x$.

> [!karta|09]- Dokaž: je-li $S$ splnitelná, je splnitelná i $S_0 \cup R_x$.
> Svědek $u$ pro $S$ splňuje $S_0 \subseteq S$ a i $R_x$, protože rezolventy jsou **důsledky** klauzulí z $S$.

> [!karta|10]- Jak začíná důkaz „⇐“ věty o eliminaci proměnné (S₀ ∪ Rₓ splnitelná ⇒ S splnitelná)?
> Vezmi svědka $u$ pro $S_0 \cup R_x$; $x$ tam není, takže svědky jsou **$u_0$ ($x \mapsto 0$) i $u_1$ ($x \mapsto 1$)**, jinde jako $u$. Ukáže se, že aspoň jeden splní $S$.

> [!karta|11]- V důkazu eliminace: proč $u_0(S_{\neg x}) = 1$ a $u_1(S_x) = 1$?
> V $u_0$ je **$\neg x$ pravdivé** a každá klauzule z $S_{\neg x}$ ho obsahuje; v $u_1$ je pravdivé $x$, které je v každé klauzuli z $S_x$.

> [!karta|12]- V důkazu eliminace: proč nemůže $u_0$ pokazit $x \vee \gamma$ a zároveň $u_1$ pokazit $\neg x \vee \delta$?
> Pak $\gamma$ i $\delta$ jsou nepravdivé v $u_0$ i $u_1$ (neobsahují $x$). Ale $\gamma \vee \delta \in R_x$ musí být pravdivá: **spor**.

> [!karta|13]- Kde se v důkazu věty o eliminaci proměnné použije základní tvar?
> $\gamma$ a $\delta$ **neobsahují $x$**, takže mají v $u_0$ a $u_1$ stejnou hodnotu; také proto jsou $S_x$ a $S_{\neg x}$ disjunktní.

> [!karta|14]- Proč smíš v rezoluční tabulce po spočítání $R_x$ vyhodit klauzule s $x$?
> Podle věty o eliminaci jsou $S$ a $S_0 \cup R_x$ **ekvisplnitelné**; zapomenuté rezolventy k rozhodnutí nejsou potřeba.

> [!karta|15]- Jak rezoluční tabulka dokončí důkaz směru „⇐“ rezolučního principu ($\mathrm{ff} \notin R^*(S)$ ⇒ $S$ splnitelná)?
> Každá klauzule v tabulce je rezolventa klauzulí z $S$, tedy **$T \subseteq R^*(S)$**. Když $\mathrm{ff} \notin R^*(S)$, pak ani $\mathrm{ff} \notin T$, takže tabulka **skončí s $\emptyset$**. Prázdná množina je splnitelná a věta o eliminaci proměnné krok po kroku zpětně dá svědka pro $S$.

> [!karta|16]- Jak z rezoluční tabulky získáš svědka splnitelnosti?
> **Pozpátku** $x_n, \dots, x_1$: zkus $x_i = 0$; když to pokazí klauzuli z množiny před tímto krokem, dej $x_i = 1$ (podle důkazu eliminace jedna z voleb vyjde).

### Příklady na procvičení

> [!priklad|17]- Spočítej $\mathrm{res}_x(x \vee y \vee z, \neg x \vee y \vee w)$.
> **$y \vee z \vee w$** ($y$ jen jednou).

> [!priklad|18]- Vypiš všechny klauzule nad $\{x, y\}$. Kolik jich je?
> $\mathrm{ff}$, $x$, $\neg x$, $y$, $\neg y$, $x \vee y$, $x \vee \neg y$, $\neg x \vee y$, $\neg x \vee \neg y$: **$9 = 3^2$**.

> [!priklad|19]- Najdi ohodnocení, ve kterém jsou $x \vee y$ i $\neg x \vee \neg y \vee z$ pravdivé, ale $z$ ne.
> **$u(x) = 1$, $u(y) = 0$, $u(z) = 0$**: $x \vee y$ díky $x$, $\neg x \vee \neg y \vee z$ díky $\neg y$.

> [!priklad|20]- Spočítej nové klauzule v $R^1(M)$ pro $M = \{p \vee q, \neg q \vee s, \neg q \vee \neg r, \neg t \vee r, \neg s \vee t, \neg p\}$.
> **$q$, $p \vee s$, $p \vee \neg r$, $\neg q \vee t$, $\neg q \vee \neg t$, $r \vee \neg s$**, celkem $|R^1(M)| = 12$.

> [!priklad|21]- Ve které generaci poprvé vznikne $\mathrm{ff}$ pro výletovou množinu $M$?
> V **$R^3(M)$**: $q \in R^1$ ($p \vee q$, $\neg p$), $\neg q \in R^2$ (z $\neg q \vee t$ a $\neg q \vee \neg t$ z $R^1$), pak $\mathrm{res}_q(q, \neg q) = \mathrm{ff}$.

> [!priklad|22]- Pro $S = \{x \vee y, x \vee z \vee t, \neg x, y \vee z\}$ urči $S_0$, $S_x$, $S_{\neg x}$ a $R_x$.
> $S_0 = \{y \vee z\}$, $S_x = \{x \vee y, x \vee z \vee t\}$, $S_{\neg x} = \{\neg x\}$, **$R_x = \{y, z \vee t\}$**.

> [!priklad|23]- (slajd 18) Rozhodni tabulkou (pořadí $x, y, z$), zda je splnitelná $\{\neg z \vee x \vee y,\ \neg x \vee y,\ \neg y \vee x,\ \neg x,\ y \vee z\}$ (z $\{z \Rightarrow (x \vee y), x \Leftrightarrow y, \neg x \wedge (y \vee z)\}$).
> Přes $x$: $R_x = \{\neg y, \neg z \vee y\}$, $S_0 = \{y \vee z\}$. Přes $y$: $R_y = \{\neg z, z\}$. Přes $z$: $\mathrm{ff}$. **Nesplnitelná.**

> [!priklad|24]- (slajd 26) Rozhodni tabulkou (pořadí $x, y, z, w$) a případně najdi svědka: $S = \{x \vee y \vee w,\ x \vee \neg y,\ y \vee z \vee \neg w,\ \neg x \vee y \vee \neg z,\ z \vee w\}$.
> Přes $x$: $R_x = \{w \vee y \vee \neg z\}$ (druhá rezolventa $\neg y \vee y \vee \neg z$ je tautologie), $S := \{y \vee z \vee \neg w, z \vee w, w \vee y \vee \neg z\}$. Přes $y$: $S_{\neg y} = \emptyset$, $S := \{z \vee w\}$. Přes $z$: $S_{\neg z} = \emptyset$, $S := \emptyset$; přes $w$ už zbývá $\emptyset$, **splnitelná**. Pozpátku: $w$ nic neomezuje, zvolme třeba $w = 0$, pak $z = 1$, pak $y$: $w \vee y \vee \neg z$ vynutí $y = 1$, pak $x$: $x \vee \neg y$ vynutí $x = 1$. Svědek **$x = y = z = 1$, $w = 0$**.

---
← [[LGR 04 – Sémantický důsledek a klauzální tvar|8. 10. 2026 Sémantický důsledek a klauzální tvar]] · [[LGR 06 – Rezoluční tabulka a přirozená dedukce|15. 10. 2026 Rezoluční tabulka a přirozená dedukce]] →

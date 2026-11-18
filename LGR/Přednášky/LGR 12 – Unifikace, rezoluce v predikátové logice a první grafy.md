---
predmet: LGR
prednaska: 12
datum: 2026-11-12
zdroj: "handout 7, slajdy 23–40; handout 8, slajdy 3–7"
tags: [prednaska, LGR]
---

# LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy

*Přednáška 12 · čtvrtek 12. 11. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 7 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_7.pdf) · [handout 8 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_8.pdf)

Témata: `povolené substituce` · `unifikační algoritmus` · `maximální unifikátor` · `rezolventa formálně` · `rezoluční princip v predikátové logice` · `příliš agresivní unifikátor` · `nekonečná výroba rezolvent` · `nerozhodnutelnost` · `graf` · `Kn, Dn, Km,n` · `bipartitní graf`

Minule jsme viděli, že konflikt mezi klauzulemi v predikátové logice nastává jen na nějaké části universa a najde se [[dosazení termu do klauzule|dosazením termů]]. Dnes se z toho stane přesný postup: **unifikační algoritmus** najde nejmenší nutné dosazení, s ním se definuje [[rezolventa predikátové logiky|rezolventa]] a rezoluční princip platí stejně jako ve výrokové logice. Jen se výroba rezolvent nemusí zastavit. Konec přednášky otevírá druhou polovinu předmětu: **teorii grafů** (handout 8).

## §0 Přehled na jedné stránce

| pojem | co to je | pozor na |
|---|---|---|
| [[povolená substituce]] | za proměnnou dosadit term, ve kterém ta proměnná není | za konstantu ani za $f(x)$ se nedosazuje |
| [[unifikační algoritmus]] | čte dvě atomické formule zleva, při rozdílu dosadí za proměnnou | vstup musí mít **různé proměnné**; $x$ proti $f(\dots x \dots)$ = NELZE |
| [[maximální unifikátor]] | seznam jen **nutných** substitucí, které atomy srovnají | [[příliš agresivní unifikátor]] může minout spor |
| rezolventa | $\alpha(\vartheta)$, $\beta(\vartheta)$ mají komplementární literály, zbytek $+\ \forall$ | $\{\alpha, \beta\} \models \mathrm{res}(\alpha, \beta)$ |
| [[rezoluční princip predikátové logiky]] | konečná $S$ nesplnitelná $\iff \mathrm{ff} \in R^*(S)$ | $R^*(S)$ může být nekonečná |
| [[nerozhodnutelnost splnitelnosti v predikátové logice]] | žádný algoritmus vždy nezastaví se správnou odpovědí | ani tautologičnost nejde rozhodnout |
| [[graf]] | $G = (V, E)$, $E \subseteq \binom{V}{2}$ | bez smyček a násobných hran |
| [[úplný graf]] $K_n$, [[diskrétní graf]] $D_n$ | všechny hrany, žádná hrana | $\binom{n}{2} = \frac{n(n-1)}{2}$ hran, 0 hran |
| [[bipartitní graf]], [[úplný bipartitní graf]] $K_{m,n}$ | hrany jen mezi partitami $V_1$, $V_2$ | $K_{m,n}$ má $m \cdot n$ hran |

## §1 Povolené substituce

Otázka „je $\{\alpha, \beta\}$ splnitelná?“ vede k hledání modelu. Konflikt najdeme tak, že z $\alpha$, $\beta$ uděláme důsledky $\alpha'$, $\beta'$ ($\alpha \models \alpha'$, $\beta \models \beta'$), které už mají [[komplementární literály]]. Smíme proto dělat jen takové substituce, které **vedou k sémantickému důsledku**.

> [!definice] Povolená substituce · handout 7, slajdy 24–25
> $\alpha(x := t)$ je klauzule, která vznikne dosazením termu $t$ za všechny výskyty proměnné $x$ v otevřeném jádru klauzule $\alpha$ a doplněním obecných kvantifikátorů (dopředu) pro všechny proměnné, které v jádru zůstaly. Pro seznam $\vartheta = (x_1 := t_1, \dots, x_n := t_n)$ je $\alpha(\vartheta)$ výsledek postupného provedení substitucí od první po $n$-tou.
>
> V rezoluční metodě jsou *povolené* tyto substituce (pro každou z nich $\alpha \models \alpha(x := t)$):
> - $x := y$, kde $x$ lze [[legální přejmenování|legálně přejmenovat]] na $y$,
> - $x := a$, kde $a$ je [[konstantní symbol]],
> - $x := g(t_1, \dots, t_n)$, kde $g$ je [[funkční symbol]] arity $n$ a termy $t_1, \dots, t_n$ **neobsahují $x$**.
>
> Ostatní substituce jsou v rezoluční metodě zakázané.

^def-povolena-substituce

> [!pozor] Proč zakázat $x := f(x)$
> Důsledek by dosazení $x := f(x)$ dalo taky: $\forall x\,P(x) \models \forall x\,P(f(x))$, dosadit do obecné klauzule smíš libovolný term. Zakazuje se kvůli **unifikaci**: rovnice $x = f(x)$ nemá konečné řešení (řetězec $f(f(f(\dots)))$ se nikdy nesrovná), proto algoritmus kontroluje, že term neobsahuje dosazovanou proměnnou.

> [!lidsky] Lidsky
> Obecné tvrzení smíš zúžit: co platí pro každé $x$, platí pro $a$ i pro každé $f(y)$. Opačně to nejde: z tvrzení o jednom prvku $a$ neplyne nic o všech. Proto se dosazuje **jen za proměnné**, nikdy za konstantu ani za složený term.

> [!example] Příklad
> $\alpha = \forall x\,\forall y\,(\neg T(x, y, x) \vee S(y))$. Povolené: $\alpha(x := a) = \forall y\,(\neg T(a, y, a) \vee S(y))$, dále $\alpha(x := a,\ y := f(z)) = \forall z\,(\neg T(a, f(z), a) \vee S(f(z)))$: proměnná $z$ zůstala v jádru, takže dostala $\forall z$.
>
> Nepovolené: z $P(a)$ udělat $\forall x\,P(x)$ (dosazení $a := x$ za konstantu), protože $P(a) \not\models \forall x\,P(x)$: model $U = \{0, 1\}$, $[\![a]\!] = 0$, $[\![P]\!] = \{0\}$.

## §2 Unifikační algoritmus

Mají-li $\alpha$ literál $P(t_1, \dots, t_n)$ a $\beta$ literál $\neg P(s_1, \dots, s_n)$, rezolventa vznikne, jen když jdou povolenými substitucemi srovnat na stejné $P(r_1, \dots, r_n)$. Navíc chceme dělat **pouze nutné** substituce: tak zachytíme konflikt v celé šíři a dostaneme nejobecnější rezolventu.

> [!definice] Unifikační algoritmus a maximální unifikátor · handout 7, slajdy 27–29
> **Vstup:** dvě atomické formule $L_1$, $L_2$ se stejným predikátovým symbolem, které mají **různé proměnné**.
> **Výstup:** *maximální unifikátor* $\vartheta$, tj. seznam nezbytně nutných povolených substitucí, po kterých $L_1(\vartheta) = L_2(\vartheta)$, nebo hláška NELZE.
>
> Řetězce $L_1$, $L_2$ čteme zleva doprava a stejné znaky mažeme. Na prvním rozdílu:
> 1. není-li ani jeden ze znaků proměnná, unifikátor neexistuje (NELZE),
> 2. je-li jeden proměnná $x$ a druhý term obsahuje $x$ (např. $f(x)$), unifikátor neexistuje (NELZE),
> 3. jinak za proměnnou dosadíme term z druhého řetězce, substituci přidáme do $\vartheta$, provedeme ji na **zbytky obou řetězců** a čteme dál.
>
> Když se podaří smazat oba řetězce celé, je $\vartheta$ maximální unifikátor.

^def-unifikace

> [!lidsky] Lidsky
> Dva výrazy přikládáš k sobě jako dvě pravítka a jedeš zleva. Kde se liší, zkusíš „přizpůsobit jednu stranu druhé“: proměnnou smíš přepsat na cokoli, co ji samu neobsahuje. Dva různé konstantní nebo funkční symboly přepsat nejde, tam algoritmus končí NELZE.

> [!example] Příklad (slajd 30)
> $L_1 = T(x, y, x)$, $L_2 = T(a, f(z), z)$. Po smazání $T($: $x$ proti $a$, tedy $x := a$; zbytky $y, a$ a $f(z), z$. $y$ proti $f(z)$, $y$ v $f(z)$ není, tedy $y := f(z)$; zbytky $a$ a $z$. $z := a$. Oba řetězce jsou smazané:
>
> $$
> \vartheta = (x := a,\ y := f(z),\ z := a), \qquad L_1(\vartheta) = L_2(\vartheta) = T(a, f(a), a).
> $$
>
> Další: $S(f(x))$ a $S(f(a))$ dají $\vartheta = (x := a)$. $S(f(a))$ a $S(f(b))$ pro různé konstanty $a$, $b$: rozdíl $a$ proti $b$, žádná proměnná, **NELZE**.

> [!obrazek] Unifikace $T(x, y, x)$ a $T(a, f(z), z)$
> ![[lgr12-unifikace.png]]
> *Modře to, co z řetězců ještě zbývá přečíst, oranžově substituce přidaná do $\vartheta$ (hned se provede na oba zbytky), šedě důvod, proč je povolená. Zeleně výsledek.*

> [!pozor] Častá chyba: $x$ proti $f(x)$
> Substituce $x := f(x)$ řetězce nikdy nesrovná: z $x$ proti $f(x)$ se stane $f(x)$ proti $f(f(x))$ a rozdíl se jen posune dovnitř. Proto pravidlo 2 končí NELZE. Typicky: $R(x, x)$ a $R(y, f(y))$ dají $x := y$, pak $y$ proti $f(y)$, **NELZE** (slajd 23: $\forall x\,R(x, x)$ a $\forall y\,\neg R(y, f(y))$ mají model $U = \mathbb{N}$, $[\![R]\!]$ rovnost, $[\![f]\!] : n \mapsto n + 1$).

> [!navic] Proč musí mít vstupní formule různé proměnné
> Klauzule $\forall x\,\neg P(x)$ a $\forall x\,P(f(x))$ jsou spolu ve sporu ($[\![P]\!]$ by musela být prázdná a zároveň obsahovat $\mathrm{Im}\,[\![f]\!] \neq \emptyset$). S tímtéž $x$ by unifikace $P(x)$ s $P(f(x))$ skončila NELZE a spor bychom minuli. Po přejmenování druhé klauzule na $\forall y\,P(f(y))$ vyjde $x := f(y)$ a rezolventa $\mathrm{ff}$. Vázané proměnné každé klauzule se proto před rezolucí přejmenují tak, aby se žádná nevyskytovala ve dvou klauzulích.

## §3 Rezolventa a rezoluční princip

> [!definice] Rezolventa (formálně) · handout 7, slajd 31
> Buďte $\alpha$, $\beta$ klauzule s různými proměnnými, $\alpha$ obsahuje literál $P(t_1, \dots, t_n)$, $\beta$ literál $\neg P(s_1, \dots, s_n)$ a existuje maximální unifikátor $\vartheta$ atomů $P(t_1, \dots, t_n)$ a $P(s_1, \dots, s_n)$. **Tehdy a jen tehdy** je definována rezolventa: $\alpha(\vartheta)$ a $\beta(\vartheta)$ obsahují komplementární literály $P(r_1, \dots, r_n)$ a $\neg P(r_1, \dots, r_n)$; $\mathrm{res}(\alpha, \beta)$ je klauzule, jejíž otevřené jádro je disjunkce všech **ostatních** literálů z $\alpha(\vartheta)$ a $\beta(\vartheta)$ (každý jednou) a vpředu jsou obecné kvantifikátory všech proměnných, které v jádru zůstaly.

^def-rezolventa-formalne

> [!lidsky] Lidsky
> „Disjunkce konců opatřená $\forall$“: unifikátorem srovnáš sporný pár, ten vyškrtneš, zbytky obou klauzulí spojíš pomocí $\vee$ a před to dáš $\forall$ pro proměnné, které přežily. Když unifikátor neexistuje, rezolventa není.

> [!example] Příklad (slajd 32)
> $\alpha = \forall x\,\forall y\,(\neg T(x, y, x) \vee S(y))$, $\beta = \forall z\,T(a, f(z), z)$. S $\vartheta$ z §2 je $\alpha(\vartheta) = \neg T(a, f(a), a) \vee S(f(a))$, $\beta(\vartheta) = T(a, f(a), a)$, tedy **$\mathrm{res}(\alpha, \beta) = S(f(a))$** (bez proměnných, žádný $\forall$).
>
> $\alpha = \forall x\,\neg S(f(x))$, $\beta = S(f(a))$: $\vartheta = (x := a)$ a $\mathrm{res} = \mathrm{ff}$. Pro $\beta = S(a)$ unifikátor neexistuje a rezolventa **není definována**.

> [!veta] Tvrzení · handout 7, slajd 33
> ==Jsou-li $\alpha$, $\beta$ klauzule s různými proměnnými==, pak **$\{\alpha, \beta\} \models \mathrm{res}(\alpha, \beta)$**. Množiny $\{\alpha, \beta\}$ a $\{\alpha, \beta, \mathrm{res}(\alpha, \beta)\}$ mají stejné modely.
>
> > [!note]- Důkaz
> > Unifikátor obsahuje jen povolené substituce, takže $\alpha \models \alpha(\vartheta)$ a $\beta \models \beta(\vartheta)$. Klauzule $\alpha(\vartheta)$, $\beta(\vartheta)$ mají komplementární literály a stejně jako ve výrokové logice $\{\alpha(\vartheta), \beta(\vartheta)\} \models \mathrm{res}(\alpha(\vartheta), \beta(\vartheta)) = \mathrm{res}(\alpha, \beta)$. Tranzitivitou sémantického důsledku $\{\alpha, \beta\} \models \mathrm{res}(\alpha, \beta)$.

^veta-dusledek-rezolventy

> [!lidsky] Lidsky
> Rezolventa nic nového nevymýšlí, jen vyslovuje, co z obou klauzulí už plyne. Přidat ji k množině proto nezmění, které interpretace jsou modely.

> [!definice] Populace rezolvent v predikátové logice · handout 7, slajd 34
> Pro množinu klauzulí $S$ s různými proměnnými je $R(S) = S \cup \{$všechny rezolventy dvojic z $S\}$, $R^0(S) = S$, $R^{i+1}(S) = R(R^i(S))$ a $R^*(S) = \bigcup_{i \geq 0} R^i(S)$.

^def-populace-pl

> [!lidsky] Lidsky
> Stejné jako [[populace rezolvent]] ve výrokové logice: přidáváš rezolventy, rezolventy rezolvent atd. Rozdíl je jen v tom, že tady se ta populace nemusí nikdy uzavřít (§5).

> [!example] Příklad
> $S = \{\forall x\,\neg S(f(x)),\ S(f(a))\}$: $R^1(S) = S \cup \{\mathrm{ff}\}$ a $R^*(S) = R^1(S)$, protože $\mathrm{ff}$ s ničím dál nerezolvuje. Pro $S = \{\forall x\,\neg S(f(x)),\ S(a)\}$ žádná rezolventa není, tedy $R^*(S) = S$.

> [!veta] Rezoluční princip · handout 7, slajd 34
> ==Konečná množina klauzulí $S$== je nesplnitelná, **právě když $R^*(S)$ obsahuje $\mathrm{ff}$**.
>
> > [!note]- Důkaz (jen jeden směr)
> > Je-li $\mathrm{ff} \in R^*(S)$: $S$ a $R^*(S)$ mají stejné modely (indukcí podle $i$ z tvrzení o rezolventě) a $\mathrm{ff}$ nemá žádný model, takže ani $S$. Opačný směr (úplnost rezoluce) se zde nedokazuje.

^veta-rezolucni-princip-pl

> [!lidsky] Lidsky
> Stejné jako [[rezoluční princip]] ve výrokové logice: nesplnitelnost se vždy dá prokázat odvozením $\mathrm{ff}$. Háček je v opačném směru: že $\mathrm{ff}$ **nevznikne**, poznáš jistě jen tehdy, když se výroba rezolvent zastaví.

### Celý příklad: je množina klauzulí $S$ splnitelná?

> [!example] Příklad (slajd 35)
> $S = \{\alpha, \beta, \gamma, \delta\}$ v jazyce s predikáty $T$ (arita 3), $R$ (2), $S$ (1), konstantami $a$, $b$ a funkcí $f$:
>
> $$
> \alpha = \forall x\,\forall y\,(\neg T(x, y, x) \vee S(y)),\quad \beta = \forall z\,T(a, f(z), z),\quad \gamma = \forall t\,(R(b, t) \vee \neg S(t)),\quad \delta = \forall u\,\forall v\,\neg R(u, f(v)).
> $$
>
> Proměnné v $\delta$ bylo nejdřív potřeba přejmenovat na $u$, $v$, aby se nekryly s ostatními klauzulemi.
> 1. $\rho_1 = \mathrm{res}(\alpha, \beta) = S(f(a))$, $\vartheta = (x := a,\ y := f(z),\ z := a)$.
> 2. $\rho_2 = \mathrm{res}(\gamma, \delta) = \forall v\,\neg S(f(v))$: unifikace $R(b, t)$ a $R(u, f(v))$ dá $\vartheta = (u := b,\ t := f(v))$.
> 3. $\mathrm{res}(\rho_1, \rho_2) = \mathrm{ff}$, $\vartheta = (v := a)$.
>
> Podle rezolučního principu je **$S$ nesplnitelná**.

> [!obrazek] Zamítací strom
> ![[lgr12-zamitaci-strom.png]]
> *Oranžově klauzule z $S$, modře rezolventy, červeně $\mathrm{ff}$, šedě maximální unifikátor použitý v daném kroku. Stejný [[zamítací strom]] jako ve výrokové logice, jen každá hrana nese unifikátor.*

> [!pozor] Příliš agresivní unifikátor (slajd 36)
> Pro $R(b, t)$ a $R(u, f(v))$ jde vzít i $\theta = (u := b,\ v := b,\ t := f(b))$. Výsledek $\neg S(f(b))$ z $\{\gamma, \delta\}$ sice plyne, ale **není to rezolventa**: substituce $v := b$ nebyla nutná a konflikt jsme zúžili jen na bod $f(b)$. S $\rho_1 = S(f(a))$ pak $S(f(a))$ a $\neg S(f(b))$ nejdou unifikovat a spor bychom minuli. ^def-agresivni

## §4 Rezoluční metoda v predikátové logice

> [!definice] Rezoluční metoda · handout 7, slajdy 34–40
> Ověření $S \models \varphi$ pro konečnou množinu sentencí $S$:
> 1. podle [[věta o sémantickém důkazu sporem|věty o důkazu sporem]] stačí zjistit, zda je $S \cup \{\neg\varphi\}$ nesplnitelná,
> 2. převedeme ji na [[klauzální tvar predikátové logiky|klauzální tvar]] (každá sentence vlastní skolemizační symboly, každá klauzule vlastní proměnné); je s ní [[ekvisplnitelné množiny|ekvisplnitelný]],
> 3. vyrábíme rezolventy; vznikne-li $\mathrm{ff}$, je $S \models \varphi$,
> 4. zastaví-li se výroba (žádná nová rezolventa) bez $\mathrm{ff}$, je $S \not\models \varphi$.

^def-rezolucni-metoda-pl

> [!lidsky] Lidsky
> Stejný recept jako ve výrokové logice: přidej negovaný závěr a hledej spor. Spor = důsledek platí. Nový je krok se skolemizací a to, že bod 4 nemusí nikdy nastat.

> [!example] Příklad (slajdy 39–40)
> **$\exists x\,\forall y\,R(x, y) \models \forall y\,\exists x\,R(x, y)$.** Negace závěru je $\exists y\,\forall x\,\neg R(x, y)$, skolemizace dá $\mathrm{Kl} = \{\forall y\,R(a, y),\ \forall x\,\neg R(x, b)\}$. Unifikace $R(a, y)$ a $R(x, b)$: $\vartheta = (x := a,\ y := b)$, rezolventa $\mathrm{ff}$, **důsledek platí**.
>
> **$\forall y\,\exists x\,R(x, y) \not\models \exists x\,\forall y\,R(x, y)$.** $\mathrm{Kl} = \{\forall y\,R(f(y), y),\ \forall x\,\neg R(x, g(x))\}$. Unifikace $R(f(y), y)$ a $R(x, g(x))$: $x := f(y)$, pak $y$ proti $g(f(y))$, kde $y$ uvnitř je: **NELZE**. Žádná rezolventa, $R^*(S) = S$ bez $\mathrm{ff}$, množina je splnitelná a **důsledek neplatí**.

## §5 Proč se rezoluce nemusí zastavit

Ve výrokové logice s $n$ proměnnými existuje nejvýš $3^n$ klauzulí (bez komplementárních dvojic, každá proměnná je v klauzuli kladně, záporně, nebo vůbec), takže $R^*(S)$ je konečná a výroba se vždy zastaví. V predikátové logice termy rostou do nekonečna ($a$, $f(a)$, $f(f(a))$, …), a s nimi i rezolventy.

> [!example] Příklad (slajd 38)
> $S = \{\forall x\,(P(x) \vee \neg P(f(x))),\ \forall y\,(P(y) \vee \neg P(f(f(y))))\}$. Unifikace $\neg P(f(x))$ s $P(y)$ dá $y := f(x)$ a rezolventu $\forall x\,(P(x) \vee \neg P(f^3(x)))$, kde $f^n(x)$ je $f$ použité $n$-krát. Další kolo dá $f^4$, $f^5$, …: v $R^*(S)$ jsou rezolventy $\forall x\,(P(x) \vee \neg P(f^n(x)))$ pro **každé $n \geq 3$** a výroba se nezastaví.
>
> Přitom $S$ je splnitelná: stačí $[\![P]\!] = U$. Rezoluce to ale nikdy „neohlásí“, protože $\mathrm{ff}$ nevznikne a nové rezolventy pořád přibývají.

> [!obrazek] Nekonečná výroba rezolvent
> ![[lgr12-nekonecno.png]]
> *Oranžově klauzule z $S$, modře rezolventy. Každá nová rezolventa jde zase rezolvovat s $\alpha$ (čárkovaně) a exponent u $f$ roste bez konce.*

> [!veta] Nerozhodnutelnost · handout 7, slajd 37
> **Problém splnitelnosti množiny klauzulí v predikátové logice je nerozhodnutelný**: neexistuje univerzální algoritmus, který by pro libovolnou konečnou množinu klauzulí zastavil a správně rozhodl o její splnitelnosti. Tudíž je nerozhodnutelné i to, zda je sentence tautologie. Důkaz se zde neuvádí.

^veta-nerozhodnutelnost

> [!lidsky] Lidsky
> Rezoluce v predikátové logice je hlídač, který spor vždycky najde, když tam je (dřív nebo později). Když spor není, může hledat donekonečna, a nikdo nedokáže napsat program, který by tohle čekání vždy zkrátil. Ve výrokové logice tenhle problém není: tabulka má $2^n$ řádků.

> [!navic] Co z handoutu 7 patří do testů
> 1. semestrální test (pátek 27. 11.) má handouty 1–3 a 5–6, takže unifikace a rezoluce v predikátové logice v něm **nejsou**. Patří ke zkoušce: typická úloha je „rozhodněte rezolucí, zda $S \models \varphi$“ jako v §4.

## §6 Neorientované grafy

Druhá polovina předmětu. Graf je nejjednodušší model „věcí a vztahů mezi dvojicemi“: křižovatky a silnice, lidé a přátelství, počítače a kabely.

> [!definice] Graf · handout 8, slajd 3
> *Graf* (neorientovaný graf) $G$ je dvojice $(V, E)$, kde $V$ je neprázdná konečná množina, jejíž prvky jsou *vrcholy*, a $E \subseteq \binom{V}{2}$ je množina (některých) dvouprvkových podmnožin $V$, jejíž prvky jsou *hrany*. Pro hranu $e = \{u, v\}$ jsou $u$, $v$ její *koncové vrcholy* a hrana je s nimi *incidentní* (spojuje je). Hranu $\{u, v\}$ zapisujeme i krátce $uv$.

^def-graf

> [!lidsky] Lidsky
> Vrcholy jsou tečky, hrany čáry mezi dvojicemi teček. Protože hrana je **množina dvou různých** vrcholů, nemůže vést z vrcholu do sebe (smyčka) a mezi dvěma vrcholy může být nejvýš jedna (žádné násobné hrany). Takovému grafu se říká i *obyčejný graf*.

> [!example] Příklad
> $G = (V, E)$, $V = \{1, 2, 3, 4\}$, $E = \{\{1, 2\}, \{2, 3\}, \{3, 4\}, \{2, 4\}\} = \{12, 23, 34, 24\}$: 4 vrcholy, 4 hrany, vrchol 2 je koncem tří hran. Nepříklad: $(\{1, 2\}, \{\{1, 1\}\})$ graf není, $\{1, 1\} = \{1\}$ není dvouprvková.

Graf je **množina**, obrázek je jen jeho *nakreslení*: tentýž graf jde nakreslit mnoha způsoby a na poloze teček ani tvaru čar nezáleží, jen na tom, které dvojice jsou spojené. ^nakresleni

> [!obrazek] Dvě nakreslení téhož grafu
> ![[lgr12-nakresleni.png]]
> *Tentýž graf $G$ z příkladu: vlevo jako čtverec s úhlopříčkou 24, vpravo jako trojúhelník 2, 3, 4 s „ocáskem“ 1. Množiny $V$ a $E$ jsou stejné.*

> [!definice] Speciální grafy · handout 8, slajd 4
> - *Úplný graf* $K_n$ je graf na $n$ vrcholech s $E = \binom{V}{2}$: každé dva vrcholy jsou spojené hranou.
> - *Diskrétní graf* $D_n$ je graf na $n$ vrcholech bez hran, $E = \emptyset$.
> - *Bipartitní graf* je graf, jehož množinu vrcholů lze rozdělit na dvě disjunktní podmnožiny (*partity*) $V_1$, $V_2$ tak, že každá hrana má jeden koncový vrchol ve $V_1$ a druhý ve $V_2$.
> - *Úplný bipartitní graf* $K_{m,n}$ je bipartitní graf s $\lvert V_1 \rvert = m$, $\lvert V_2 \rvert = n$, který obsahuje všechny možné hrany mezi $V_1$ a $V_2$.

^def-specialni-grafy

> [!lidsky] Lidsky
> $K_n$: na večírku si podal ruku každý s každým. $D_n$: nikdo s nikým. Bipartitní: dvě skupiny (třeba studenti a předměty) a čáry vedou jen **mezi** skupinami, nikdy uvnitř jedné. $K_{m,n}$: každý z první skupiny je spojen s každým z druhé.

> [!example] Příklad
> $K_3$ je trojúhelník (3 hrany). $D_3$ jsou tři samostatné tečky. Graf $(\{1, 2, 3, 4\}, \{12, 13, 24, 34\})$ je bipartitní s $V_1 = \{1, 4\}$, $V_2 = \{2, 3\}$ a obsahuje všechny 4 hrany mezi nimi, takže je to $K_{2,2}$. Nepříklad: $K_3$ bipartitní není, ze tří vrcholů trojúhelníku musí dva skončit ve stejné partitě a hrana mezi nimi by vedla uvnitř ní.

> [!veta] Tvrzení · handout 8, slajd 5
> **$K_n$ má $\binom{n}{2} = \frac{n(n-1)}{2}$ hran** a **$K_{m,n}$ má $m \cdot n$ hran**.
>
> > [!note]- Důkaz
> > Hrany $K_n$ jsou právě všechny dvouprvkové podmnožiny $n$-prvkové množiny, a těch je $\binom{n}{2}$. Hrana $K_{m,n}$ je určena dvojicí (vrchol z $V_1$, vrchol z $V_2$), a těch je $m \cdot n$.

^veta-pocet-hran

> [!lidsky] Lidsky
> V $K_n$ má každý z $n$ vrcholů hranu ke všem $n - 1$ ostatním, to je $n(n-1)$ konců hran, a každá hrana má konce dva: proto děleno 2. V $K_{m,n}$ jde z každého z $m$ vrcholů nahoře $n$ hran dolů.

> [!example] Příklad
> $K_4$: $\frac{4 \cdot 3}{2} = 6$ hran, $K_{2,3}$: $2 \cdot 3 = 6$ hran, $K_{10}$: $45$ hran.

> [!obrazek] Speciální grafy
> ![[lgr12-specialni.png]]
> *Nahoře $K_4$ (6 hran) a $D_4$ (0 hran). Dole bipartitní graf s partitami $V_1$ (oranžově) a $V_2$ (zeleně), hrany vedou jen mezi nimi, a vpravo úplný bipartitní $K_{2,3}$ se všemi $2 \cdot 3 = 6$ hranami.*

> [!navic] Krajní případy (slajd 5)
> Diskrétní graf je bipartitní (žádná hrana nic neporušuje). I jednovrcholový graf $H = (\{1\}, \emptyset)$ se považuje za bipartitní: $V_1 = \{1\}$ a $V_2 = \emptyset$, jedna partita smí být prázdná. Obecnější definice grafu (handout 8, slajd 6) jako trojice $(V, E, \varepsilon)$ připouští i smyčky a násobné hrany; pokud nebude řečeno jinak, graf je vždy obyčejný graf $(V, E)$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč smí rezoluční metoda dosazovat jen za proměnné, a ne za konstanty nebo složené termy?
> Substituce musí vést k **sémantickému důsledku** ($\alpha \models \alpha'$). Z „pro každé $x$“ plyne tvrzení o $a$ i o $f(y)$, ale z tvrzení o jednom prvku $[\![a]\!]$ **neplyne nic o všech**: $P(a) \not\models \forall x\,P(x)$.

> [!karta|02]- Kdy unifikační algoritmus skončí hláškou NELZE?
> Na prvním rozdílu, když:
> - **ani jeden** znak není proměnná (např. $a$ proti $b$, $a$ proti $f(\dots)$),
> - jeden je proměnná $x$ a druhý term **obsahuje $x$** (např. $x$ proti $f(x)$).

> [!karta|03]- Proč nejde unifikovat $x$ s $f(x)$?
> Po $x := f(x)$ by se porovnávalo $f(x)$ s $f(f(x))$ a rozdíl by se jen **posunul dovnitř**; řetězce se nikdy nesrovnají. Navíc $x := f(x)$ není povolená substituce (term obsahuje $x$).

> [!karta|04]- Proč musí mít dvě klauzule před unifikací různé proměnné?
> Jinak bychom mohli **minout spor**. $\forall x\,\neg P(x)$ a $\forall x\,P(f(x))$ jsou ve sporu, ale $P(x)$ s $P(f(x))$ dá NELZE. Po přejmenování na $\forall y\,P(f(y))$ vyjde $x := f(y)$ a $\mathrm{ff}$.

> [!karta|05]- Proč se při rezoluci dělají jen nutné substituce (maximální unifikátor)?
> Zbytečná substituce zúží konflikt na **menší část universa** a vznikne slabší důsledek, který už nemusí jít dál rezolvovat. Např. $\neg S(f(b))$ místo $\forall v\,\neg S(f(v))$ nejde unifikovat s $S(f(a))$ a **spor se mine**.

> [!karta|06]- Proč platí $\{\alpha, \beta\} \models \mathrm{res}(\alpha, \beta)$ v predikátové logice?
> Unifikátor má jen povolené substituce, takže $\alpha \models \alpha(\vartheta)$, $\beta \models \beta(\vartheta)$. Z nich jako ve výrokové logice plyne rezolventa, a **tranzitivita** $\models$ dá $\{\alpha, \beta\} \models \mathrm{res}$.

> [!karta|07]- Kdy (tehdy a jen tehdy) je definována rezolventa klauzulí $\alpha$, $\beta$ v predikátové logice?
> Když mají **různé proměnné**, $\alpha$ obsahuje $P(t_1, \dots, t_n)$, $\beta$ obsahuje $\neg P(s_1, \dots, s_n)$ a atomy $P(\bar t)$, $P(\bar s)$ mají **maximální unifikátor**. Jinak rezolventa neexistuje.

> [!karta|08]- Jak se rezolucí ověří $S \models \varphi$ v predikátové logice?
> 1. Vezmi $S \cup \{\neg\varphi\}$ (důkaz sporem).
> 2. Převeď na klauzule (vlastní skolemizační symboly, vlastní proměnné).
> 3. Rezolvuj: $\mathrm{ff}$ ⇒ **$S \models \varphi$**.
> 4. Výroba se zastaví bez $\mathrm{ff}$ ⇒ **$S \not\models \varphi$**.

> [!karta|09]- Proč se výroba rezolvent ve výrokové logice vždy zastaví, ale v predikátové ne?
> Ve výrokové logice je nad $n$ proměnnými jen **konečně mnoho klauzulí** ($3^n$). V predikátové logice se termy zanořují ($f(x)$, $f(f(x))$, …), takže rezolvent může být **nekonečně mnoho**.

> [!karta|10]- Co znamená, že splnitelnost v predikátové logice je nerozhodnutelná?
> **Neexistuje algoritmus**, který by pro každou konečnou množinu klauzulí zastavil a správně řekl, zda je splnitelná. Rezoluce nesplnitelnost vždy prokáže ($\mathrm{ff}$), ale u splnitelné množiny může běžet **donekonečna**. Proto je nerozhodnutelné i to, zda je sentence tautologie.

> [!karta|11]- Proč má $K_n$ právě $\frac{n(n-1)}{2}$ hran?
> Hrany $K_n$ jsou **všechny dvouprvkové podmnožiny** $V$, a těch je $\binom{n}{2} = \frac{n(n-1)}{2}$. Jinak: každý vrchol má $n - 1$ sousedů, $n(n-1)$ konců hran, každá hrana má **dva konce**.

> [!karta|12]- Proč nemá graf podle definice $G = (V, E)$, $E \subseteq \binom{V}{2}$ smyčky ani násobné hrany?
> Hrana je **dvouprvková množina** $\{u, v\}$, takže $u \neq v$ (žádná smyčka). $E$ je **množina**, takže se v ní $\{u, v\}$ nemůže vyskytovat dvakrát (žádné násobné hrany).

> [!karta|13]- Proč je diskrétní graf bipartitní, i jednovrcholový?
> Podmínka „každá hrana vede mezi $V_1$ a $V_2$“ je **bez hran splněna vždy**. U jednoho vrcholu se bere $V_1 = \{1\}$, $V_2 = \emptyset$: **partita smí být prázdná**.

> [!karta|14]- Proč dvě různě vypadající nakreslení mohou být tentýž graf?
> Graf je jen dvojice **množin** $(V, E)$. Poloha teček a tvar čar nejsou jeho součástí, rozhoduje jen, **které dvojice vrcholů** jsou spojené.

### Příklady na procvičení

> [!priklad|15]- Najdi maximální unifikátor $R(x, f(x))$ a $R(a, y)$.
> $x$ proti $a$: $x := a$, zbytky $f(a)$ a $y$. $y$ proti $f(a)$: $y := f(a)$.
>
> **$\vartheta = (x := a,\ y := f(a))$**, obě formule se stanou $R(a, f(a))$.

> [!priklad|16]- Najdi maximální unifikátor $P(x, x)$ a $P(f(y), y)$.
> $x := f(y)$, zbytky $f(y)$ a $y$. Teď $y$ proti $f(y)$, kde je $y$ uvnitř: **NELZE**, unifikátor neexistuje.

> [!priklad|17]- Najdi maximální unifikátor $Q(x, f(a))$ a $Q(g(y), f(y))$.
> $x := g(y)$, zbytky $f(a)$ a $f(y)$; smažeme $f($, zbývá $a$ proti $y$: $y := a$.
>
> **$\vartheta = (x := g(y),\ y := a)$**, výsledek $Q(g(a), f(a))$.

> [!priklad|18]- Najdi rezolventu klauzulí $\forall x\,\forall y\,(\neg P(x, y) \vee Q(y))$ a $\forall z\,P(z, g(z))$.
> Unifikace $P(x, y)$ a $P(z, g(z))$: $x := z$ (přejmenování), $y := g(z)$. Po vyškrtnutí sporné dvojice zbývá $Q(g(z))$ s proměnnou $z$:
>
> **$\mathrm{res} = \forall z\,Q(g(z))$.**

> [!priklad|19]- Je množina klauzulí $\{\forall x\,(\neg P(x) \vee Q(f(x))),\ P(a),\ \forall y\,\neg Q(y)\}$ splnitelná?
> $\mathrm{res}$ první a druhé ($x := a$): $Q(f(a))$. S třetí ($y := f(a)$): $\mathrm{ff}$.
>
> **Nesplnitelná** (rezoluční princip).

> [!priklad|20]- Kolik hran má $K_6$ a kolik $K_{3,4}$?
> **$K_6$: $\frac{6 \cdot 5}{2} = 15$**, **$K_{3,4}$: $3 \cdot 4 = 12$.**

> [!priklad|21]- Je graf $G = (\{1, 2, 3, 4\}, \{12, 23, 34, 24\})$ bipartitní?
> **Ne.** Obsahuje trojúhelník $2, 3, 4$ (hrany 23, 34, 24): ze tří vrcholů musí dva být ve stejné partitě a hrana mezi nimi by vedla uvnitř ní.

> [!priklad|22]- Je graf $(\{1, 2, 3, 4\}, \{12, 13, 24, 34\})$ bipartitní? Je to nějaký $K_{m,n}$?
> **Ano**, $V_1 = \{1, 4\}$, $V_2 = \{2, 3\}$: každá hrana má jeden konec v každé partitě. Obsahuje všechny $2 \cdot 2 = 4$ hrany mezi nimi, je to **$K_{2,2}$**.

---
← [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice|6. 11. 2026 Klauzální tvar a rezolventy v predikátové logice]]

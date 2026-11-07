---
predmet: LGR
prednaska: 11
datum: 2026-11-06
zdroj: "handout 7, slajdy 11–22"
tags: [prednaska, LGR]
---

# LGR 11 – Klauzální tvar a rezolventy v predikátové logice

*Přednáška 11 · pátek 6. 11. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 7 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_7.pdf) · [verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_7a.pdf)

Témata: `algoritmus převodu na klauzule` · `prenexní tvar v krocích` · `skolemizace na modelu` · `Kl(φ) ≈ φ` · `skolemizace po větvích stromu` · `pořadí negace a skolemizace` · `rezolventa v predikátové logice` · `konflikt na podmnožině U` · `dosazení termu`

Minule jsme poznali [[prenexní tvar]] a [[skolemizace|skolemizaci]]. Dnes se z nich složí celý **algoritmus převodu sentence na klauzule**: výsledná množina $\mathrm{Kl}(\varphi)$ je s $\varphi$ jen [[ekvisplnitelné množiny|ekvisplnitelná]], ne tautologicky ekvivalentní. Druhá polovina začíná **rezolventy v predikátové logice**: konflikt mezi literály už není vidět na první pohled a nastává jen na nějaké části universa. Obecné pravidlo, jak ho najít (unifikace), přijde příště.

## §0 Přehled na jedné stránce

| krok / pojem | co se děje | zachová |
|---|---|---|
| 1. přejmenování | každý kvantifikátor váže jinou proměnnou | $\mathrel{\vert\!=\!\vert}$ |
| 2. spojky | jen $\neg, \wedge, \vee$ ($\alpha \Rightarrow \beta$ na $\neg\alpha \vee \beta$) | $\mathrel{\vert\!=\!\vert}$ |
| 3. negace | De Morgan a negování kvantifikátorů až k atomům | $\mathrel{\vert\!=\!\vert}$ |
| 4. vytýkání | kvantifikátory dopředu: prenexní tvar | $\mathrel{\vert\!=\!\vert}$ |
| 5. CNF | otevřená část za kvantifikátory do konjunktivní normální formy | $\mathrel{\vert\!=\!\vert}$ |
| 6. skolemizace | $\exists$ pryč, nové konstanty a funkce | jen $\approx$ |
| 7. $\forall$ pod $\wedge$ | obecné kvantifikátory jen k částem, kde je jejich proměnná | $\mathrel{\vert\!=\!\vert}$ |
| 8. rozdělení | konjunkty jsou klauzule, množina $\mathrm{Kl}(\varphi)$ | $\approx$ |
| [[rezolventa predikátové logiky]] | klauzule, která plyne z $\{\alpha, \beta\}$ díky konfliktu literálů | $\{\alpha, \beta\} \models \mathrm{res}$ |
| konflikt | $P(x)$ vs. $\neg P(x)$: celé $U$; vs. $\neg P(a)$: bod $[\![a]\!]$; vs. $\neg P(f(y))$: $\mathrm{Im}\,[\![f]\!]$; $P(f(x))$ vs. $\neg P(a)$: žádný | |

## §1 Algoritmus převodu na klauzální tvar

Připomenutí z minula: [[klauzule predikátové logiky]] je sentence, která má jen obecné kvantifikátory, všechny vpředu, a za nimi [[literál]] nebo disjunkci literálů; literál je atomická formule nebo její negace. Rezoluce pracuje jen s klauzulemi, takže každou sentenci je nejdřív potřeba na klauzule převést.

> [!definice] Algoritmus 1 · handout 7, slajdy 12–13
> K sentenci $\varphi$ najdeme ekvisplnitelnou množinu klauzulí $\mathrm{Kl}(\varphi)$, její *klauzální tvar*:
>
> 1. přejmenujeme vázané proměnné tak, aby každý kvantifikátor vázal jinou proměnnou,
> 2. ostatní spojky přepíšeme tautologicky ekvivalentně na $\neg, \wedge, \vee$,
> 3. negaci dostaneme až před atomické podformule (De Morganovy zákony, negování kvantifikátorů),
> 4. vytkneme kvantifikátory před konjunkce a disjunkce (vznikne prenexní tvar),
> 5. otevřenou podformuli za kvantifikátory upravíme do CNF (distributivita, $\wedge$ nad $\vee$),
> 6. skolemizací odstraníme existenční kvantifikátory,
> 7. obecné kvantifikátory distribuujeme pod konjunkci k těm podformulím, ve kterých se jejich proměnná vyskytuje,
> 8. sentenci rozdělíme v místech konjunkcí; vzniklé klauzule tvoří $\mathrm{Kl}(\varphi)$.
>
> Úpravy se dělají vždy od kořene syntaktického stromu směrem k listům.

^def-klauzalni-tvar-pl

> [!lidsky] Lidsky
> Kroky 1–4 jsou převod do [[prenexní tvar|prenexního tvaru]] z minula, krok 5 je CNF jako ve výrokové logice. Nové jsou kroky 6–8: [[skolemizace]] vyhodí $\exists$ a pak se konjunkce „rozstříhá“ na jednotlivé klauzule, každá si vezme svoje $\forall$. Všechno kromě skolemizace zachovává význam ($\mathrel{\vert\!=\!\vert}$), skolemizace jen odpověď na „má to model?“.

> [!example] Příklad (slajd 17)
> $\varphi = \forall x\,P(x) \Rightarrow \forall x\,\exists y\,(R(x, y) \wedge Q(a))$, jazyk s konstantou $a$.
>
> 1. Druhé $\forall x$ přejmenujeme na $z$: $\forall x\,P(x) \Rightarrow \forall z\,\exists y\,(R(z, y) \wedge Q(a))$.
> 2. Implikace: $\neg\forall x\,P(x) \vee \forall z\,\exists y\,(R(z, y) \wedge Q(a))$.
> 3. Negace dovnitř: $\exists x\,\neg P(x) \vee \forall z\,\exists y\,(R(z, y) \wedge Q(a))$.
> 4. Vytknutí: $\exists x\,\forall z\,\exists y\,\big(\neg P(x) \vee (R(z, y) \wedge Q(a))\big)$.
> 5. CNF: $\exists x\,\forall z\,\exists y\,\big((\neg P(x) \vee R(z, y)) \wedge (\neg P(x) \vee Q(a))\big)$.
> 6. Skolemizace $x := c$, $y := f(z)$ ($c$ nová konstanta, $f$ nový funkční symbol arity 1): $\forall z\,\big((\neg P(c) \vee R(z, f(z))) \wedge (\neg P(c) \vee Q(a))\big)$.
> 7. $\forall z$ jen k první části, ve druhé se $z$ nevyskytuje: $\forall z\,(\neg P(c) \vee R(z, f(z))) \wedge (\neg P(c) \vee Q(a))$.
> 8. **$\mathrm{Kl}(\varphi) = \{\forall z\,(\neg P(c) \vee R(z, f(z))),\ \neg P(c) \vee Q(a)\}$**, dvě klauzule v obohaceném jazyce.
>
> Platí $\varphi \mathrel{\vert\!=\!\vert} \varphi_p \approx \varphi_s$ (ověřeno na všech interpretacích s universem o 1 a 2 prvcích): z $\varphi_s$ plyne $\varphi$, obráceně ne.

> [!pozor] Častá chyba: $\forall$ ke klauzuli, kde jeho proměnná není
> Psát $\forall z\,(\neg P(c) \vee Q(a))$ není chyba v pravdivosti (kvantifikátor bez proměnné nic nemění), ale krok 7 říká dát $\forall z$ jen tam, kde se $z$ vyskytuje. Výsledek je pak kratší a hned vidíš, že $\neg P(c) \vee Q(a)$ je klauzule bez proměnných.

> [!veta] Tvrzení · handout 7, slajd 14
> **Množina klauzulí $\mathrm{Kl}(\varphi)$ vytvořená algoritmem 1 je ekvisplnitelná se sentencí $\varphi$.** ==Je-li $S$ konečná množina sentencí== a $\mathrm{Kl}(S)$ sjednocení klauzálních tvarů jednotlivých sentencí, ==přičemž u skolemizace zavádíme pro každou sentenci jiné nové symboly==, pak **$S \approx \mathrm{Kl}(S)$**.
>
> > [!note]- Důkaz
> > Všechny kroky kromě šestého zachovávají tautologickou ekvivalenci, tedy i množinu modelů. Skolemizace zachovává splnitelnost: $\varphi_s \models \varphi$ a z každého modelu $\varphi$ se vhodnou interpretací nových symbolů udělá model $\varphi_s$. Pro množinu $S$: model $S$ se rozšíří o interpretace skolemizačních symbolů všech sentencí naráz, což jde, jen když jsou symboly různé.

^veta-ekvisplnitelnost-kl

> [!lidsky] Lidsky
> Klauzální tvar není „totéž jinak napsané“, je to jen **stejně splnitelné**. Pro rezoluci to stačí, protože rezoluce odpovídá jen na otázku, jestli množina má model.

> [!example] Příklad
> $S = \{\exists x\,P(x),\ \exists x\,\neg P(x)\}$ je splnitelná ($U = \{0, 1\}$, $[\![P]\!] = \{0\}$). Se dvěma různými skolemizačními konstantami vyjde $\mathrm{Kl}(S) = \{P(c), \neg P(d)\}$, splnitelná ($[\![c]\!] = 0$, $[\![d]\!] = 1$). Se stejnou konstantou by vyšlo $\{P(c), \neg P(c)\}$, nesplnitelná: odpověď by se změnila.

> [!pozor] Nejdřív negace, potom skolemizace (slajd 15)
> Pořadí skolemizace a negace nejde prohodit, protože negace otočí kvantifikátory, a skolemizovat se pak budou jiné proměnné. Při ověřování $S \models \varphi$ se proto převádí na klauzule až **$\neg\varphi$**, nikdy se neneguje skolemizovaná $\varphi_s$.
>
> Příklad: $\varphi = \forall x\,\exists y\,R(x, y)$. Správně $\neg\varphi \mathrel{\vert\!=\!\vert} \exists x\,\forall y\,\neg R(x, y)$, skolemizace dá klauzuli $\forall y\,\neg R(c, y)$. Špatně: $\varphi_s = \forall x\,R(x, f(x))$ a její negace $\exists x\,\neg R(x, f(x))$ klauzule vůbec není.

> [!navic] Prenexní tvar ani $\mathrm{Kl}(\varphi)$ nejsou jednoznačné (slajd 15)
> Při vytýkání si můžeš vybrat pořadí. Vyplatí se dávat **$\exists$ co nejblíž ke kořeni** (co nejvíc vlevo), protože pak má skolemizační funkce menší aritu. $\exists x\,\neg P(x) \vee \forall z\,\exists y\,(\dots)$ jde vytknout jako $\exists x\,\forall z\,\exists y$ (skolemizuje se $x := c$) nebo jako $\forall z\,\exists x\,\exists y$, a pak by bylo $x := g(z)$, zbytečně funkce.

## §2 Skolemizace na konkrétním modelu

Skolemizace (slajdy 8–11) mění $\forall x\,\exists y\,R(x, y)$ na $\forall x\,R(x, f(x))$ s novým [[funkční symbol|funkčním symbolem]] $f$ arity 1. Proč zachová splnitelnost, je nejlépe vidět na jednom modelu.

> [!example] Příklad: z modelu $\varphi$ model $\varphi_s$
> $\varphi = \forall x\,\exists y\,R(x, y)$. Interpretace s $U = \{0, 1, 2\}$ a $[\![R]\!] = \{(0, 1), (1, 1), (1, 2), (0, 2), (2, 0)\}$ je model $\varphi$: **z každého prvku vede aspoň jedna šipka** (z 0 do 1 i 2, z 1 do 1 i 2, z 2 do 0).
>
> $\varphi_s = \forall x\,R(x, f(x))$. Stačí za $[\![f]\!]$ vybrat z každého prvku jednu šipku, třeba $[\![f]\!] : 0 \mapsto 1,\ 1 \mapsto 2,\ 2 \mapsto 0$. Pak $(u, [\![f]\!](u)) \in [\![R]\!]$ pro každé $u \in U$ a interpretace je model $\varphi_s$. Takových výběrů je tu $2 \cdot 2 \cdot 1 = 4$.
>
> Obráceně $\varphi_s \models \varphi$ vždy: když platí $R(u, [\![f]\!](u))$, je $[\![f]\!](u)$ svědek pro $\exists y$. Ale $\varphi \not\models \varphi_s$: v témže modelu s $[\![f]\!] : 0 \mapsto 0, 1 \mapsto 0, 2 \mapsto 0$ je $\varphi$ pravdivá a $\varphi_s$ ne, protože $(0, 0) \notin [\![R]\!]$.

> [!obrazek] Skolemizační funkce vybírá svědky
> ![[lgr11-skolem-model.png]]
> *Vlevo modře všechny šipky $[\![R]\!]$ na $U = \{0, 1, 2\}$. Vpravo oranžově šipky $u \to [\![f]\!](u)$, které vybrala skolemizační funkce; šedé šipky v $[\![R]\!]$ zůstaly, jen nejsou potřeba.*

> [!navic] Proč musí být $f$ nový symbol a co je obohacený jazyk
> Kdyby $f$ už v jazyce byl, měl by v interpretaci pevný význam, který vůbec nemusí šipky z $[\![R]\!]$ trefit. Jen nový symbol si smíme vyložit, jak se nám hodí, totiž jako výběr svědků (u nekonečného universa k tomu potřebujeme axiom výběru, slajd 9). Skolemizace proto **obohacuje jazyk** o nové konstanty a funkční symboly: $\mathrm{Kl}(\varphi)$ je napsaná v obohaceném jazyce $L'$, ne v původním $L$ (slajd 11). ^obohaceny-jazyk

> [!definice] Algoritmus 2 · handout 7, slajd 16
> Při převodu na klauzule není nutné jít přes prenexní tvar. Po krocích 1–3 algoritmu 1 lze skolemizovat *po větvích syntaktického stromu*: najdeme první existenční kvantifikátor ve větvi a proměnnou za ním nahradíme termem $f(x_1, \dots, x_n)$, kde $f$ je nový funkční symbol a $x_1, \dots, x_n$ jsou proměnné obecných kvantifikátorů nad ním směrem ke kořeni (pro $n = 0$ nová konstanta).

^def-algoritmus-2

> [!lidsky] Lidsky
> Svědek pro $\exists y$ smí záviset jen na tom, co bylo vybráno „před ním“, tedy na proměnných $\forall$, které jsou v [[syntaktický strom|syntaktickém stromu]] nad ním (blíž ke kořeni). Kolik takových $\forall$ je, tolik argumentů dostane skolemizační funkce.

> [!example] Příklad
> Po krocích 1–3 v příkladu ze slajdu 17 máme $\exists x\,\neg P(x) \vee \forall z\,\exists y\,(R(z, y) \wedge Q(a))$. Nad $\exists x$ žádné $\forall$ není, tedy $x := c$; nad $\exists y$ je $\forall z$, tedy $y := f(z)$. Vyjde $\neg P(c) \vee \forall z\,(R(z, f(z)) \wedge Q(a))$, a po vytknutí a CNF stejné klauzule jako algoritmem 1.
>
> Nepříklad: v $\forall x\,P(x) \wedge \exists y\,Q(y)$ leží $\forall x$ v jiné větvi než $\exists y$, takže $y := c$, ne $y := f(x)$.

> [!obrazek] Skolemizace po větvích stromu
> ![[lgr11-strom.png]]
> *Syntaktický strom po krocích 1–3. Oranžově existenční kvantifikátory, modře obecný kvantifikátor. Nad $\exists x$ (levá větev) žádné $\forall$ není, nad $\exists y$ (pravá větev) je $\forall z$, proto $y := f(z)$.*

## §3 Rezolventy v predikátové logice

Ve výrokové logice měla [[rezolventa]] smysl, když klauzule obsahovaly [[komplementární literály]] $x$ a $\neg x$: obě nemohou platit zároveň, takže v každém ohodnocení, kde platí $\alpha$ i $\beta$, musí platit „zbytek“ jedné z nich. V predikátové logice je myšlenka stejná, ale konflikt není vidět hned: komplementární literály nemusí být přímo v $\alpha$, $\beta$, ale až v jejich důsledcích.

> [!definice] Rezolventa · handout 7, slajdy 18–19
> *Rezolventa* dvojice klauzulí $\alpha, \beta$ je klauzule, která je sémantickým důsledkem množiny $\{\alpha, \beta\}$ a vznikne z ostatních literálů $\alpha$ a $\beta$, když jejich literály (případně v důsledcích $\alpha'$, $\beta'$ vzniklých dosazením termů za proměnné) jsou ve sporu na nějaké části universa. Vznikne-li při vytváření rezolvent prázdná klauzule $\mathrm{ff}$, je původní množina klauzulí nesplnitelná (a jen tehdy).

^def-rezolventa-pl

> [!lidsky] Lidsky
> Hledáš místo, kde „$P$ platí“ z jedné klauzule a „$P$ neplatí“ z druhé narazí na tytéž prvky universa. Na těch prvcích musí platit zbytek $\alpha$ nebo zbytek $\beta$, a to je rezolventa. Kde se literály nepotkají, žádná rezolventa nevzniká.

> [!example] Příklad 1 (slajd 20): konflikt na celém universu
> $\alpha = \forall x\,(P(x) \vee Q(x))$, $\beta = \forall x\,(\neg P(x) \vee S(a))$ (vázanou proměnnou $\beta$ lze přejmenovat, takže stejné $x$ nevadí).
>
> V modelu $\{\alpha, \beta\}$ pro každý kontext $x \mapsto u \in U$: z $\alpha$ je $u \in [\![P]\!]$ nebo $u \in [\![Q]\!]$, z $\beta$ je $u \notin [\![P]\!]$ nebo $[\![a]\!] \in [\![S]\!]$. Podmínky na $P$ se vylučují pro **každé** $u$, takže $u \in [\![Q]\!]$ nebo $[\![a]\!] \in [\![S]\!]$:
>
> $$
> \{\alpha, \beta\} \models \mathbf{\forall x\,(Q(x) \vee S(a))} = \mathrm{res}(\alpha, \beta).
> $$

> [!veta] Dosazení termu · handout 7, slajd 21
> ==Je-li $\alpha = \forall x\,\gamma$ klauzule a $t$ term==, pak **$\alpha \models \gamma[x := t]$**: dosazením termu za obecně vázanou proměnnou vznikne důsledek. Obsahuje-li $t$ proměnné, zůstanou obecně vázané (např. $\forall x\,(P(x) \vee Q(x)) \models \forall y\,(P(f(y)) \vee Q(f(y)))$).

^veta-dosazeni

> [!lidsky] Lidsky
> Co platí pro všechny prvky, platí i pro ten jeden konkrétní, který jmenuje $a$, a pro všechny, které jdou zapsat jako $f(y)$. Dosazení zúží obecné tvrzení na menší část universa, kde se pak dá najít konflikt.

> [!example] Příklad 2 (slajd 21): konflikt v jednom bodě
> $\alpha = \forall x\,(P(x) \vee Q(x))$, $\beta = \neg P(a) \vee S(a)$. Konflikt může nastat jen v kontextu $x \mapsto [\![a]\!]$. Dosazením $x := a$ dostaneš $\alpha' = P(a) \vee Q(a)$ s $\alpha \models \alpha'$, a $\alpha'$, $\beta$ už mají komplementární literály $P(a)$, $\neg P(a)$:
>
> $$
> \mathrm{res}(\alpha, \beta) = \mathrm{res}(\alpha', \beta) = \mathbf{Q(a) \vee S(a)}.
> $$
>
> Příklad 3: $\alpha = \forall x\,(P(x) \vee Q(x))$, $\beta = \forall y\,(\neg P(f(y)) \vee S(a))$. Dosazením $x := f(y)$ je $\alpha' = \forall y\,(P(f(y)) \vee Q(f(y)))$, konflikt nastává na $\mathrm{Im}\,[\![f]\!]$ a **$\mathrm{res} = \forall y\,(Q(f(y)) \vee S(a))$**.

> [!example] Příklad 4 (slajd 22): konflikt nenastane
> $\alpha = \forall x\,(P(f(x)) \vee Q(x))$, $\beta = \neg P(a) \vee S(a)$. Literál $P(f(x))$ mluví jen o prvcích $\mathrm{Im}\,[\![f]\!]$, literál $\neg P(a)$ jen o prvku $[\![a]\!]$, a ten v $\mathrm{Im}\,[\![f]\!]$ ležet nemusí. Pravdivost obou klauzulí jde zajistit **jen volbou $[\![P]\!]$**, bez jakékoli podmínky na $[\![Q]\!]$ a $[\![S]\!]$: třeba $U = \{0, 1\}$, $[\![f]\!] : n \mapsto 0$, $[\![P]\!] = \{0\}$, $[\![a]\!] = 1$, $[\![Q]\!] = [\![S]\!] = \emptyset$. **Rezolventa nevzniká.** (Handout dává model na $U = \mathbb{N}$, $[\![P]\!] = \{0\}$, $[\![f]\!] : n \mapsto 0$, $[\![a]\!] = 1$.)

> [!obrazek] Kde nastává konflikt
> ![[lgr11-konflikt.png]]
> *Červeně část universa, kde se literály s $P$ a $\neg P$ srazí: v příkladu 1 celé $U$, v příkladu 2 jen bod $[\![a]\!]$, v příkladu 3 obraz $\mathrm{Im}\,[\![f]\!]$. V příkladu 4 zeleně šrafovaná $[\![P]\!]$ pokryje oranžový $\mathrm{Im}\,[\![f]\!]$ a modrý bod $[\![a]\!]$ leží mimo, takže obě klauzule platí bez sporu.*

> [!pozor] Konstanta není term s proměnnou
> Za proměnnou smíš dosadit libovolný term, ale za konstantu ani za $f(x)$ nic dosadit nejde. Proto $P(x)$ a $\neg P(a)$ konflikt mají ($x := a$), ale $P(f(x))$ a $\neg P(a)$ ne: žádné dosazení z $f(x)$ neudělá $a$. Obecná pravidla, kdy jdou dva literály dosazením srovnat (unifikace), přijdou příště.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč je klauzální tvar $\mathrm{Kl}(\varphi)$ v predikátové logice s $\varphi$ jen ekvisplnitelný, a ne tautologicky ekvivalentní?
> Všechny kroky algoritmu zachovávají $\mathrel{\vert\!=\!\vert}$ **kromě skolemizace**. Ta zavede nové symboly: platí $\varphi_s \models \varphi$, ale ne obráceně, protože nový symbol může být vyložen „špatně“. Zachová se jen to, že **model existuje**.

> [!karta|02]- Proč nejde prohodit pořadí skolemizace a negace?
> Negace **otočí kvantifikátory** ($\neg\forall \to \exists$), takže se pak skolemizují jiné proměnné. Při ověřování $S \models \varphi$ se proto na klauzule převádí **až $\neg\varphi$**; negace skolemizované $\varphi_s$ dá formuli s $\exists$, která klauzulí není.

> [!karta|03]- Proč se při vytýkání kvantifikátorů vyplatí dávat $\exists$ co nejblíž ke kořeni?
> Skolemizační funkce dostane za argumenty proměnné všech $\forall$ před $\exists$. Čím dřív $\exists$ stojí, tím **menší arita**; $\exists$ úplně vpředu se nahradí **konstantou**.

> [!karta|04]- Jak se v algoritmu 2 (skolemizace po větvích stromu) určí arita skolemizační funkce?
> Arita = **počet obecných kvantifikátorů nad daným $\exists$** ve stejné větvi syntaktického stromu, směrem ke kořeni; jejich proměnné jsou argumenty. Žádný $\forall$ nad ním znamená novou **konstantu**.

> [!karta|05]- Proč se u množiny sentencí $S$ zavádějí pro každou sentenci jiné skolemizační symboly?
> Stejný symbol by **vnutil stejného svědka** dvěma sentencím. $\{\exists x\,P(x), \exists x\,\neg P(x)\}$ je splnitelná, ale se společnou konstantou vyjde $\{P(c), \neg P(c)\}$, nesplnitelná: změnila by se odpověď.

> [!karta|06]- Proč z modelu $\forall x\,\exists y\,R(x, y)$ vždy vznikne model $\forall x\,R(x, f(x))$?
> V modelu má každé $u$ aspoň jednoho svědka $v$ s $(u, v) \in [\![R]\!]$. Symbol $f$ je **nový**, takže ho smíme interpretovat jako **výběr jednoho svědka** pro každé $u$ (u nekonečného universa přes axiom výběru).

> [!karta|07]- Proč v predikátové logice nemusí být konflikt mezi klauzulemi vidět přímo na jejich literálech?
> Komplementární literály se mohou objevit až v **důsledcích** $\alpha'$, $\beta'$ vzniklých **dosazením termů** za obecně vázané proměnné: $\forall x\,(P(x) \vee Q(x)) \models P(a) \vee Q(a)$, a teprve tady je $P(a)$ proti $\neg P(a)$.

> [!karta|08]- Na jaké části universa nastává konflikt literálu $P(x)$ (pod $\forall x$) s $\neg P(x)$, s $\neg P(a)$ a s $\neg P(f(y))$?
> S $\neg P(x)$ na **celém $U$**, s $\neg P(a)$ jen v **bodě $[\![a]\!]$**, s $\neg P(f(y))$ na **$\mathrm{Im}\,[\![f]\!]$**. Podle toho rezolventa zůstane obecná, bude bez proměnné, nebo bude obecná přes $y$.

> [!karta|09]- Proč klauzule $\forall x\,(P(f(x)) \vee Q(x))$ a $\neg P(a) \vee S(a)$ nemají rezolventu?
> $P(f(x))$ mluví jen o prvcích $\mathrm{Im}\,[\![f]\!]$, $\neg P(a)$ o prvku $[\![a]\!]$, který tam **ležet nemusí**, a konstantu $a$ nejde dosazením získat z $f(x)$. Obě klauzule splníš samotnou volbou $[\![P]\!]$, **bez podmínky na $Q$ a $S$**.

> [!karta|10]- Proč z odvození prázdné klauzule $\mathrm{ff}$ rezolucí plyne, že množina klauzulí $S$ je nesplnitelná?
> Každá rezolventa je **sémantický důsledek** svých rodičů, takže každý model $S$ je i modelem všech rezolvent. $\mathrm{ff}$ nemá žádný model, tedy **ani $S$** model nemá.

> [!karta|11]- Proč v kroku 7 smíme rozdělit $\forall z$ pod konjunkci?
> $\forall$ se rozkládá pod $\wedge$: $\forall z\,(\alpha \wedge \beta) \mathrel{\vert\!=\!\vert} \forall z\,\alpha \wedge \forall z\,\beta$ („všichni splňují obojí“ = „všichni první a všichni druhé“). Kde se $z$ nevyskytuje, **kvantifikátor nic nemění** a vynechá se.

### Příklady na procvičení

> [!priklad|12]- Převeď na klauzální tvar $\forall x\,(P(x) \Rightarrow \exists y\,R(x, y))$.
> Implikace: $\forall x\,(\neg P(x) \vee \exists y\,R(x, y))$; vytknutí: $\forall x\,\exists y\,(\neg P(x) \vee R(x, y))$, už je v CNF. Skolemizace $y := f(x)$ (nad $\exists y$ je $\forall x$).
>
> **$\mathrm{Kl} = \{\forall x\,(\neg P(x) \vee R(x, f(x)))\}$**, jedna klauzule.

> [!priklad|13]- Převeď na klauzule $\neg\forall x\,\exists y\,R(x, y)$.
> Negace dovnitř: $\exists x\,\forall y\,\neg R(x, y)$. Nad $\exists x$ není žádné $\forall$, takže $x := c$ (nová konstanta).
>
> **$\mathrm{Kl} = \{\forall y\,\neg R(c, y)\}$.** Kdybys nejdřív skolemizoval a pak negoval, vyšlo by $\exists x\,\neg R(x, f(x))$, což klauzule není.

> [!priklad|14]- Interpretace s $U = \{0, 1, 2\}$ a $[\![R]\!] = \{(0, 0), (1, 0), (2, 1)\}$ je model $\forall x\,\exists y\,R(x, y)$. Najdi všechna $[\![f]\!]$, pro která je to model $\forall x\,R(x, f(x))$.
> Z každého prvku vede právě jedna šipka: $0 \to 0$, $1 \to 0$, $2 \to 1$. Výběr je jediný: **$[\![f]\!] : 0 \mapsto 0,\ 1 \mapsto 0,\ 2 \mapsto 1$** (z $3^3 = 27$ zobrazení vyhoví jen toto).

> [!priklad|15]- Najdi rezolventu klauzulí $\forall x\,(\neg P(x) \vee Q(x))$ a $P(a)$.
> Dosaď $x := a$: $\neg P(a) \vee Q(a)$, konflikt v bodě $[\![a]\!]$ s $P(a)$.
>
> **$\mathrm{res} = Q(a)$** (sylogismus: „každé $P$ je $Q$, $a$ je $P$, tedy $a$ je $Q$“).

> [!priklad|16]- Najdi rezolventu klauzulí $\forall x\,(P(x) \vee Q(x))$ a $\forall y\,(\neg P(f(y)) \vee S(y))$.
> Dosaď $x := f(y)$: $\forall y\,(P(f(y)) \vee Q(f(y)))$, konflikt na $\mathrm{Im}\,[\![f]\!]$.
>
> **$\mathrm{res} = \forall y\,(Q(f(y)) \vee S(y))$** (ověřeno na všech interpretacích s $|U| \le 3$).

> [!priklad|17]- Mají klauzule $P(a) \vee Q(b)$ a $\neg P(b)$ rezolventu ($a$, $b$ různé konstanty)?
> **Ne.** $P(a)$ a $\neg P(b)$ mluví o prvcích $[\![a]\!]$ a $[\![b]\!]$, které se nemusí rovnat, a konstantu za konstantu dosadit nejde. Model bez podmínky na $Q$: $U = \{0, 1\}$, $[\![a]\!] = 0$, $[\![b]\!] = 1$, $[\![P]\!] = \{0\}$, $[\![Q]\!] = \emptyset$.

### Typové příklady na semestrální test

*Převod do prenexního tvaru patří do 1. testu (handout 6); skolemizace a rezoluce v predikátové logice (handout 7) do něj nepatří. Na testu je potřeba každý krok zdůvodnit zákonem, který používáš.*

> [!priklad|18]- Převeď do prenexního tvaru $\forall x\,P(x) \vee \exists x\,Q(x)$.
> Přejmenuj: $\forall x\,P(x) \vee \exists y\,Q(y)$ (různé proměnné, takže vytýkat smíš před $\vee$ oba kvantifikátory). Vytkni:
>
> **$\forall x\,\exists y\,(P(x) \vee Q(y))$** (stejně dobře $\exists y\,\forall x\,(P(x) \vee Q(y))$, obě $\mathrel{\vert\!=\!\vert}$ s původní, ověřeno na $|U| \le 3$).

> [!priklad|19]- Převeď do prenexního tvaru $\neg\exists x\,(P(x) \wedge \forall y\,R(x, y))$.
> Negace dovnitř: $\forall x\,\neg(P(x) \wedge \forall y\,R(x, y)) \mathrel{\vert\!=\!\vert} \forall x\,(\neg P(x) \vee \exists y\,\neg R(x, y))$ (De Morgan, $\neg\forall = \exists\neg$). Vytkni $\exists y$ před $\vee$ ($y$ v $\neg P(x)$ není):
>
> **$\forall x\,\exists y\,(\neg P(x) \vee \neg R(x, y))$.**

> [!priklad|20]- Převeď do prenexního tvaru $\exists x\,P(x) \Rightarrow \forall y\,Q(y)$.
> Implikace: $\neg\exists x\,P(x) \vee \forall y\,Q(y) \mathrel{\vert\!=\!\vert} \forall x\,\neg P(x) \vee \forall y\,Q(y)$. Proměnné se jmenují různě, takže oba $\forall$ smíš vytknout i před $\vee$:
>
> **$\forall x\,\forall y\,(\neg P(x) \vee Q(y))$.** Pozor: $\exists x$ z předpokladu implikace se při vytýkání otočí na $\forall x$.

---
← [[LGR 10 – Zákony pro kvantifikátory, prenexní tvar a skolemizace|5. 11. 2026 Zákony pro kvantifikátory, prenexní tvar a skolemizace]]

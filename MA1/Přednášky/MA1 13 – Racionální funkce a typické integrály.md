---
predmet: MA1
prednaska: 13
datum: 2026-11-05
zdroj: "Handout 7A (Praktický výpočet integrálu: část 2), slajdy 2–12"
tags: [prednaska, MA1]
---

# MA1 13 – Racionální funkce a typické integrály

*Přednáška 13 · čtvrtek 5. 11. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 7A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout07a.pdf)

Témata: `dělení polynomů se zbytkem` · `násobnost kořene` · `základní věta algebry` · `ireducibilní polynomy` · `parciální zlomky` · `doplnění na čtverec` · `polynom krát sinus` · `polynom krát exponenciála` · `exponenciála krát sinus`

Minule vznikly nástroje (linearita, per partes, substituce), dnes se na nich trénují typické určité integrály. Hlavní část je integrace **racionálních funkcí** (podíl dvou polynomů): napřed algebra o polynomech (dělení se zbytkem, kořeny, rozklad), pak **rozklad na parciální zlomky**, ze kterých se každý zintegruje substitucí. Na konci tři šablony pro per partes: polynom krát $\sin$/$\cos$, polynom krát exponenciála a exponenciála krát $\sin$, kde se výpočet „zacyklí“.

## §0 Přehled na jedné stránce

| typ integrálu | postup | příklad |
|---|---|---|
| $\int \frac{a(t)}{b(t)}$, $\deg a \geq \deg b$ | vydělit se zbytkem: polynom $+$ ryze lomená část | $\frac{t^2 + 1}{t} = t + \frac{1}{t}$ |
| ryze lomená $\frac{r(t)}{b(t)}$ | rozložit $b$ na ireducibilní činitele, pak na parciální zlomky | $\frac{4t + 8}{(t+3)(t-1)} = \frac{1}{t+3} + \frac{3}{t-1}$ |
| $\frac{A}{(at+b)^n}$ | substituce $u = at + b$ | $\int \frac{3}{t-1} = 3\ln\vert t - 1\vert$ |
| $\frac{At + B}{at^2 + bt + c}$, $D < 0$ | rozdělit na „derivace jmenovatele“ $+$ zbytek, doplnit na čtverec | $\frac{1}{t^2 + 2t + 2} = \frac{1}{(t+1)^2 + 1}$ |
| polynom $\cdot \sin$, $\cos$, $e^{\lambda t}$ | per partes, polynom derivovat, opakovat | $\int t^2 \sin t$: dvakrát per partes |
| $e^{\lambda t} \cdot \sin$, $\cos$ | per partes dvakrát, vznikne rovnice pro $I$ | $\int_0^b e^{-t}\sin t = \frac{1}{2} - \frac{1}{2}e^{-b}(\cos b + \sin b)$ |

> [!navic] Co čekat na testech
> Na testech ani u zkoušky nebudou integrály takhle náročné; „exotické“ určité integrály se neobjeví (handout 7A, slajd 12). Rozklad s mocninou kvadratického činitele ve jmenovateli ($n > 1$, substituce $t = \tan u$) u zkoušky není vůbec (slajd 6). Postupy z této přednášky jsou ale základ, který se u jednodušších integrálů hodí.

## §1 Polynomy: dělení, kořeny, rozklad

Všechny integrály z této přednášky se počítají nástroji z minula: [[linearita určitého integrálu|linearitou]], [[metoda per partes|per partes]] a [[věta o substituci v určitém integrálu|substitucí]]; na konci každého postupu stojí [[tabulka primitivních funkcí]]. Nové je jen to, jak integrand na tabulkové kusy rozebrat. U podílu dvou [[polynom|polynomů]] to vyžaduje trochu algebry. Pojmy kořen, násobnost, základní věta algebry a ireducibilita handout 7A přímo nezavádí (pracuje s nimi na slajdech 3–6 jako se známými), proto jsou tady shrnuté jako doplněk.

> [!definice] Definice · slajd 4
> **Racionální funkce** je podíl $\frac{a(x)}{b(x)}$, kde $a$, $b$ jsou polynomy a $b$ není [[nulový polynom]]. Je definovaná na množině $\{x : b(x) \neq 0\}$.
>
> Racionální funkce je **ryze lomená**, když $\deg a < \deg b$ ([[stupeň polynomu|stupeň]] čitatele je menší než stupeň jmenovatele).

^def-racionalni-funkce

> [!lidsky] Lidsky
> Racionální funkce je „zlomek z polynomů“. Ryze lomená je obdoba pravého zlomku $\frac{2}{3}$: čitatel je „menší“ než jmenovatel. Neryze lomená je obdoba $\frac{17}{5}$, ze které jde vytáhnout celou část $3$.

^def-ryze-lomena

> [!example] Příklad
> $\frac{4t + 8}{t^2 + 2t - 3}$ je racionální funkce definovaná mimo $t = -3$ a $t = 1$ (tam je $t^2 + 2t - 3 = (t + 3)(t - 1)$ nulový) a je ryze lomená ($1 < 2$). $\frac{t^2 + 1}{t}$ je racionální, ale ne ryze lomená ($2 \geq 1$). $\frac{\sin t}{t}$ racionální funkce není: $\sin$ není polynom.

### Dělení se zbytkem (slajd 4)

> [!veta] Věta · slajd 4 (dělení polynomů se zbytkem)
> ==Ať $a$, $b$ jsou polynomy a $b$ není nulový polynom.== Potom existují **právě jedny** polynomy $q$ (podíl) a $r$ (zbytek) takové, že
>
> $$
> \mathbf{a = q \cdot b + r}, \qquad \deg r < \deg b \text{ (nebo } r = 0\text{)}.
> $$
>
> Po vydělení $b$: $\frac{a}{b} = q + \frac{r}{b}$, kde $\frac{r}{b}$ je ryze lomená.

^veta-deleni-se-zbytkem

> [!lidsky] Lidsky
> Stejné jako písemné dělení čísel: $17 : 5 = 3$, zbytek $2$, tedy $\frac{17}{5} = 3 + \frac{2}{5}$. U polynomů se dělí podle nejvyšší mocniny, dokud zbytek nemá menší stupeň než dělitel. Každá racionální funkce = polynom (ten se integruje hned) + ryze lomená funkce.

> [!example] Příklad
> $(x^3 + 2x^2 - x + 3) : (x - 1)$: $x^3 : x = x^2$, odečtením $x^2(x - 1)$ zbude $3x^2 - x + 3$; $3x^2 : x = 3x$, zbude $2x + 3$; $2x : x = 2$, zbude $5$. Tedy
>
> $$
> x^3 + 2x^2 - x + 3 = (x^2 + 3x + 2)(x - 1) + 5.
> $$
>
> Kontrola: dosazením $x = 1$ do levé strany vyjde $5 = r$.

### Kořeny a jejich násobnost

Číslo $p$ je **kořen** polynomu $a$, když $a(p) = 0$. Tehdy dělení $a$ polynomem $(x - p)$ vyjde beze zbytku (zbytek je konstanta $r$ a dosazením $x = p$ do $a = q \cdot (x - p) + r$ vyjde $r = a(p) = 0$), takže $(x - p)$ jde z polynomu vytknout. ^koren

> [!definice] Definice · doplněk k handoutu 7A (násobnost kořene)
> Číslo $p$ je **$k$-násobný kořen** polynomu $a$ ($k \geq 1$), když
>
> $$
> a(x) = (x - p)^k \cdot a^\ast(x) \quad\text{pro nějaký polynom } a^\ast \text{ s } a^\ast(p) \neq 0.
> $$
>
> Pro $k = 1$ mluvíme o **jednoduchém**, pro $k = 2$ o **dvojnásobném** kořenu.

^def-nasobnost-korene

> [!lidsky] Lidsky
> Násobnost říká, kolikrát lze závorku $(x - p)$ z polynomu vytknout. Podmínka $a^\ast(p) \neq 0$ znamená „vytkni všechno, co jde“. Na grafu: v jednoduchém kořenu graf osu $x$ protne, v dvojnásobném se jí jen dotkne (jako parabola $x^2$ v nule).

> [!example] Příklad
> $x^3 - 3x + 2$: kořen $1$ uhodneme ($1 - 3 + 2 = 0$), dělením $x^3 - 3x + 2 = (x - 1)(x^2 + x - 2)$ a $x^2 + x - 2 = (x - 1)(x + 2)$. Tedy $x^3 - 3x + 2 = (x - 1)^2(x + 2)$: **$1$ je dvojnásobný kořen** ($a^\ast(x) = x + 2$, $a^\ast(1) = 3 \neq 0$), **$-2$ jednoduchý**. Nepříklad: $1$ není trojnásobný kořen, protože $x + 2$ v bodě $1$ nulové není.

> [!obrazek] Jednoduchý a dvojnásobný kořen
> ![[ma113-nasobnost.png]]
> *Modrý graf $x^3 - 3x + 2 = (x - 1)^2(x + 2)$. V oranžovém jednoduchém kořenu $-2$ graf osu $x$ protne (mění znaménko), v zeleném dvojnásobném kořenu $1$ se osy jen dotkne a znaménko nemění.*

> [!veta] Věta · doplněk k handoutu 7A (základní věta algebry)
> ==Ať $a$ je polynom s komplexními koeficienty stupně $n \geq 1$.== Potom má $a$ **právě $n$ komplexních kořenů, počítáno s násobností**, tj.
>
> $$
> \mathbf{a(x) = c\,(x - p_1)^{k_1} \cdots (x - p_m)^{k_m}}, \qquad k_1 + \dots + k_m = n,
> $$
>
> kde $c \neq 0$ je vedoucí koeficient a $p_1, \dots, p_m \in \mathbb{C}$ jsou navzájem různé kořeny.

^veta-zakladni-veta-algebry

> [!lidsky] Lidsky
> V komplexních číslech se každý nekonstantní polynom rozpadne na lineární závorky, nic „nerozložitelného“ nezbude. Polynom stupně $n$ má tedy $n$ kořenů, jen se některé mohou opakovat. V reálných číslech to neplatí: $x^2 + 1$ reálný kořen nemá.

> [!example] Příklad
> $x^2 + 1 = (x - i)(x + i)$, kořeny $\pm i$. $x^3 - 3x + 2 = (x - 1)^2(x + 2)$ má kořeny $1, 1, -2$, tedy tři počítáno s násobností ($2 + 1 = 3$).

> [!veta] Věta · doplněk k handoutu 7A (Abelova–Ruffiniho věta)
> Pro kořeny polynomu stupně **nejvýš $4$** existuje obecný vzorec, který je vyjádří z koeficientů pomocí $+$, $-$, $\cdot$, $:$ a odmocnin. Pro stupeň **$5$ a vyšší** takový obecný vzorec **neexistuje**.

^veta-abel-ruffini

> [!lidsky] Lidsky
> Vzorec $x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ má obdobu pro stupně $3$ a $4$ (Cardanovy a Ferrariho vzorce), ale je tak složitá, že se v praxi nepoužívá. Od stupně $5$ je dokázáno, že žádný takový vzorec být nemůže. Proto se kořeny jmenovatele v příkladech **hádají** (celočíselný kořen polynomu s celými koeficienty dělí absolutní člen) a v obecném případě hledají numericky.

> [!example] Příklad
> Rovnice $x^5 - x - 1 = 0$ má reálný kořen $\approx 1{,}1673$, který se pomocí odmocnin zapsat nedá. Naproti tomu $t^3 - 2t^2 + 4t - 8$ ze slajdu 4 má „hezký“ kořen $2$ (dělitel absolutního členu $8$): $8 - 8 + 8 - 8 = 0$.

### Ireducibilní polynomy nad $\mathbb{R}$

> [!definice] Definice · doplněk k handoutu 7A (ireducibilní polynom)
> Reálný polynom $a$ stupně $\deg a \geq 1$ je **ireducibilní** v $\mathbb{R}[x]$, když z každého rozkladu $a = a_1 \cdot a_2$ na reálné polynomy plyne $\deg a_1 = 0$ nebo $\deg a_2 = 0$.

^def-ireducibilni-polynom

> [!lidsky] Lidsky
> Ireducibilní polynom je obdoba prvočísla: nejde napsat jako součin dvou reálných polynomů menšího stupně, jde z něj jen vytknout konstantu ($2t^2 + 2 = 2 \cdot (t^2 + 1)$ se nepočítá).

> [!example] Příklad
> $t - 3$ je ireducibilní (každý polynom stupně $1$). $t^2 + 1$ je ireducibilní: rozklad by musel mít dva lineární činitele, tedy reálný kořen, a $t^2 + 1 \geq 1$. Naopak $t^2 + 2t - 3 = (t + 3)(t - 1)$ ireducibilní není. A pozor, $x^4 + 4$ nemá reálný kořen, a přesto ireducibilní **není**: $x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)$.

> [!veta] Věta · doplněk k handoutu 7A, srov. slajd 6 (o ireducibilních reálných polynomech)
> 1. Ireducibilní polynomy v $\mathbb{R}[x]$ mají **stupeň $1$ nebo $2$**.
> 2. Kvadratický polynom $ax^2 + bx + c$ je ireducibilní **právě když $b^2 - 4ac < 0$**.
> 3. Každý reálný polynom $a$ stupně $\geq 1$ se rozloží jako
>
> $$
> \mathbf{a(x) = c \cdot \prod_i (x - p_i)^{k_i} \cdot \prod_j (x^2 + p_j x + q_j)^{m_j}}, \qquad p_j^2 - 4q_j < 0.
> $$
>
> > [!note]- Důkaz (idea)
> > Podle [[základní věta algebry|základní věty algebry]] se $a$ rozloží v $\mathbb{C}$ na lineární závorky. Má-li reálný polynom komplexní kořen $z$, je kořenem i $\bar z$ (komplexní sdružení koeficienty nezmění, protože jsou reálné). Součin $(x - z)(x - \bar z) = x^2 - 2\,\mathrm{Re}\,z \cdot x + |z|^2$ je **reálný** kvadratický polynom bez reálných kořenů, tedy se záporným diskriminantem. Spárováním každého nereálného kořene s jeho sdruženým vznikne reálný rozklad na lineární a kvadratické činitele; nic stupně $3$ a víc nezbude.

^veta-ireducibilni-realne

> [!lidsky] Lidsky
> Nad $\mathbb{R}$ jsou „prvočísla mezi polynomy“ jen dvojího druhu: lineární $(x - p)$ a kvadratické bez reálných kořenů. Komplexní kořeny chodí v párech $z$, $\bar z$ a každý pár dá jeden reálný kvadratický kus. Na tom stojí celý rozklad na parciální zlomky: víc typů jmenovatelů není potřeba.

> [!example] Příklad
> $t^3 - 2t^2 + 4t - 8 = t^2(t - 2) + 4(t - 2) = (t - 2)(t^2 + 4)$ a $t^2 + 4$ má $D = -16 < 0$, takže to je úplný rozklad na ireducibilní činitele. Důsledek: polynom **lichého** stupně má vždy reálný kořen (samé kvadratické činitele by daly sudý stupeň), ale polynom sudého stupně nemusí: $x^4 + 1 > 0$.

> [!pozor] Bez reálných kořenů neznamená ireducibilní
> Pro stupeň $2$ (a $3$) platí „nemá reálný kořen ⟹ ireducibilní“. Pro stupeň $4$ a víc to neplatí: $x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)$ a $x^4 + 1 = (x^2 - \sqrt{2}x + 1)(x^2 + \sqrt{2}x + 1)$ reálné kořeny nemají, ale rozložit se dají.

## §2 Rozklad na parciální zlomky

> [!definice] Definice · slajd 6 (parciální zlomek)
> **Parciální zlomek** je racionální funkce jednoho ze dvou tvarů
>
> $$
> \frac{A}{(at + b)^n}, \quad a \neq 0, \qquad\text{nebo}\qquad \frac{At + B}{(at^2 + bt + c)^n}, \quad b^2 - 4ac < 0,
> $$
>
> kde $n \geq 1$ a $A$, $B$ jsou reálné konstanty.

^def-parcialni-zlomek

> [!lidsky] Lidsky
> Parciální zlomek je nejjednodušší stavební kostka: ve jmenovateli mocnina **jednoho** [[ireducibilní polynom|ireducibilního]] polynomu, v čitateli polynom stupně menšího než ten ireducibilní kus (konstanta u lineárního, $At + B$ u kvadratického).

> [!example] Příklad
> $\frac{3}{t - 1}$, $\frac{-3}{(t - 3)^2}$ a $\frac{t - 8}{t^2 + 1}$ jsou parciální zlomky. $\frac{1}{t^2 - 1}$ není: $t^2 - 1 = (t - 1)(t + 1)$ ireducibilní není. $\frac{t}{(t - 1)^2}$ také není (u lineárního činitele smí být v čitateli jen konstanta), rozloží se jako $\frac{1}{t - 1} + \frac{1}{(t - 1)^2}$.

> [!veta] Věta · slajdy 3 a 6 (rozklad na parciální zlomky)
> ==Ať $\frac{r}{b}$ je [[ryze lomená racionální funkce]] a $b$ je rozložený na ireducibilní činitele.== Potom je $\frac{r}{b}$ **součet parciálních zlomků**, a to:
> - za každý činitel $(t - p)^k$ zlomky $\frac{A_1}{t - p} + \frac{A_2}{(t - p)^2} + \dots + \frac{A_k}{(t - p)^k}$,
> - za každý činitel $(t^2 + pt + q)^m$ s $p^2 - 4q < 0$ zlomky $\frac{B_1 t + C_1}{t^2 + pt + q} + \dots + \frac{B_m t + C_m}{(t^2 + pt + q)^m}$.
>
> Koeficienty $A_i$, $B_j$, $C_j$ jsou určené **jednoznačně**.

^veta-rozklad-parcialni-zlomky

> [!lidsky] Lidsky
> Rozklad je sčítání zlomků pozpátku: $\frac{1}{t + 3} + \frac{3}{t - 1}$ dá po převedení na společného jmenovatele $\frac{4t + 8}{(t + 3)(t - 1)}$ a my jdeme opačně. Dělá se to proto, že každý parciální zlomek umíme zintegrovat substitucí, kdežto celý zlomek ne. Počet neznámých koeficientů je vždy roven stupni jmenovatele.

> [!example] Příklad (slajd 3)
> $$
> \frac{t^2 - 13t + 33}{(t - 3)^2(t - 4)} = \frac{4}{t - 3} - \frac{3}{(t - 3)^2} - \frac{3}{t - 4}, \qquad \frac{4t^2 - 4t + 8}{(t - 1)^2(t^2 - 2t + 5)} = \frac{1}{t - 1} + \frac{2}{(t - 1)^2} + \frac{-t + 3}{t^2 - 2t + 5}.
> $$
>
> Ve druhém je $t^2 - 2t + 5$ ireducibilní ($D = 4 - 20 = -16 < 0$), proto má lineární čitatel.

> [!definice] Postup · slajd 3 (metoda neurčitých koeficientů)
> Napíšeme tvar rozkladu s neznámými koeficienty, celou rovnost vynásobíme jmenovatelem $b$ a porovnáme koeficienty u stejných mocnin $t$: dva polynomy se rovnají pro všechna $t$ **právě když** mají stejné koeficienty. Vznikne soustava lineárních rovnic pro neznámé. Rychlejší alternativa: dosazovat do rovnosti kořeny jmenovatele.

^def-neurcite-koeficienty

> [!lidsky] Lidsky
> Neznámé $A$, $B$, … jsou „díry“ v rozkladu, které se doplní tak, aby obě strany byly stejný polynom. Dosazení kořene jmenovatele vynuluje všechny členy kromě jednoho, a jeden koeficient tak vyjde hned.

> [!example] Příklad
> $\frac{4t + 8}{(t + 3)(t - 1)} = \frac{A}{t + 3} + \frac{B}{t - 1}$, po vynásobení $4t + 8 = A(t - 1) + B(t + 3)$. Porovnání: u $t^1$ je $4 = A + B$, u $t^0$ je $8 = -A + 3B$; sečtením $12 = 4B$, tedy $B = 3$, $A = 1$. Dosazením $t = 1$ vyjde rovnou $12 = 4B$, dosazením $t = -3$ vyjde $-4 = -4A$.

> [!obrazek] Rozklad na parciální zlomky jako součet grafů
> ![[ma113-parcialni-zlomky.png]]
> *Zelený čárkovaný $\frac{1}{t + 3}$ a oranžový čárkovaný $\frac{3}{t - 1}$ dají sečtením modrou funkci $\frac{4t + 8}{(t + 3)(t - 1)}$. Červené tečkované svislice jsou kořeny jmenovatele $-3$ a $1$, kde funkce není definovaná. Modrá plocha je $\int_2^3 = \ln\frac{48}{5} \approx 2{,}262$; interval $[2; 3]$ žádný kořen jmenovatele neobsahuje.*

### Celý postup na příkladu (slajdy 4–5)

$\int \frac{t^4 - 2t^3 + 5t^2 - 8t + 5}{t^3 - 2t^2 + 4t - 8}\,\mathrm{d}t$ se rozebere ve třech krocích:

1. **Dělení se zbytkem** (stupeň čitatele $4 \geq 3$): $t^4 - 2t^3 + 5t^2 - 8t + 5 = t \cdot (t^3 - 2t^2 + 4t - 8) + (t^2 + 5)$.
2. **Rozklad jmenovatele**: $t^3 - 2t^2 + 4t - 8 = (t - 2)(t^2 + 4)$.
3. **Parciální zlomky**: $\frac{t^2 + 5}{(t - 2)(t^2 + 4)} = \frac{9/8}{t - 2} + \frac{-\frac{1}{8}t - \frac{1}{4}}{t^2 + 4}$.

Integrand je tedy $t + \frac{9}{8} \cdot \frac{1}{t - 2} - \frac{1}{8} \cdot \frac{t}{t^2 + 4} - \frac{1}{4} \cdot \frac{1}{t^2 + 4}$ a jednotlivé kusy se zintegrují substitucemi $u = t - 2$ (logaritmus), $u = t^2 + 4$ (logaritmus, $\mathrm{d}u = 2t\,\mathrm{d}t$) a $u = \frac{t}{2}$ (arkustangens, $t^2 + 4 = 4(u^2 + 1)$). ^hlavni-priklad

> [!pozor] Meze nesmí obsahovat kořen jmenovatele
> Na slajdu 4 se tento integrál počítá s mezemi $2$ a $6$. Jenže jmenovatel má kořen $2$ a čitatel je tam $9 \neq 0$, takže integrand není na $[2; 6]$ spojitý (ani definovaný v $2$) a věty o [[určitý integrál|určitém integrálu]] se použít nedají; člen $\frac{9}{8}\int \frac{\mathrm{d}t}{t - 2}$ vede na $\int_0^4 \frac{\mathrm{d}u}{u}$, který jako určitý integrál neexistuje. **Před integrací racionální funkce vždy zkontroluj, že jmenovatel na $[a; b]$ nemá nulový bod.** Postup rozkladu je správně, jen meze musí ležet mimo $2$, třeba $[3; 6]$.

### Integrace parciálních zlomků (slajdy 5–7)

- $\frac{A}{(at + b)^n}$: substituce $u = at + b$ dá $\frac{A}{a}\int \frac{\mathrm{d}u}{u^n}$, tedy logaritmus ($n = 1$) nebo mocninu ($n > 1$).
- $\frac{At + B}{at^2 + bt + c}$ s $b^2 - 4ac < 0$: čitatel se napíše jako násobek derivace jmenovatele $2at + b$ plus konstanta. První kus dá substitucí $u = at^2 + bt + c$ logaritmus, druhý se **doplněním na čtverec** převede na $\arctan$.
- $\frac{At + B}{(at^2 + bt + c)^n}$ s $n > 1$: doplnění na čtverec a substituce $t = \tan u$. Tento typ u zkoušky nebude (slajd 6).

> [!definice] Postup · slajdy 5–7 (doplnění na čtverec)
> $$
> t^2 + pt + q = \left(t + \frac{p}{2}\right)^2 + \left(q - \frac{p^2}{4}\right).
> $$
>
> Pro $p^2 - 4q < 0$ je konstanta $q - \frac{p^2}{4} > 0$, takže po substituci $z = t + \frac{p}{2}$ (a přeškálování) vznikne $\int \frac{\mathrm{d}z}{z^2 + 1} = \arctan z$, pod odmocninou $\int \frac{\mathrm{d}z}{\sqrt{z^2 + 1}} = \operatorname{argsinh} z$.

^def-doplneni-na-ctverec

> [!lidsky] Lidsky
> Z $t^2 + pt$ uděláš kus čtverce $(t + \frac{p}{2})^2$ a co přebývá, odečteš. Posunutím proměnné o $\frac{p}{2}$ se pak jmenovatel změní na „$z^2 + $ kladné číslo“, což je tabulkový tvar arkustangenty.

> [!example] Příklad
> $t^2 + 2t + 2 = (t + 1)^2 + 1$. Substituce $z = t + 1$ ($\mathrm{d}z = \mathrm{d}t$, meze $0 \mapsto 1$, $1 \mapsto 2$):
>
> $$
> \int_0^1 \frac{\mathrm{d}t}{t^2 + 2t + 2} = \int_1^2 \frac{\mathrm{d}z}{z^2 + 1} = \arctan 2 - \frac{\pi}{4} \approx 0{,}322.
> $$

> [!obrazek] Doplnění na čtverec je jen posunutí grafu
> ![[ma113-doplneni-ctverec.png]]
> *Vlevo modrá plocha pod $\frac{1}{t^2 + 2t + 2}$ na $[0; 1]$, vpravo zelená plocha pod $\frac{1}{z^2 + 1}$ na $[1; 2]$. Je to tentýž graf posunutý o $1$ doprava, plochy jsou stejné: $\arctan 2 - \frac{\pi}{4}$ (oranžově).*

> [!example] Příklad (slajd 7): strategie „derivace jmenovatele + zbytek“
> $I = \int_0^4 \frac{t + 3}{\sqrt{t^2 + 2t + 2}}\,\mathrm{d}t$. Derivace výrazu pod odmocninou je $2t + 2$, proto $t + 3 = \frac{1}{2}(2t + 2) + 2$:
>
> 1. $\frac{1}{2}\int_0^4 \frac{2t + 2}{\sqrt{t^2 + 2t + 2}}\,\mathrm{d}t$: substituce $u = t^2 + 2t + 2$, meze $2$ a $26$, dá $\frac{1}{2}\int_2^{26} u^{-1/2}\,\mathrm{d}u = [\sqrt{u}]_2^{26} = \sqrt{26} - \sqrt{2}$.
> 2. $2\int_0^4 \frac{\mathrm{d}t}{\sqrt{(t + 1)^2 + 1}}$: substituce $z = t + 1$, meze $1$ a $5$, dá $2[\operatorname{argsinh} z]_1^5$, protože $(\operatorname{argsinh} z)' = \frac{1}{\sqrt{z^2 + 1}}$.
>
> Celkem $I = \sqrt{26} - \sqrt{2} + 2(\operatorname{argsinh} 5 - \operatorname{argsinh} 1) \approx 6{,}547$.

> [!navic] Shrnutí: každá racionální funkce má elementární primitivní funkci
> Dělení se zbytkem, rozklad jmenovatele a parciální zlomky převedou každou racionální funkci na polynom a součet parciálních zlomků, a každý z nich vede substitucí na tabulkový integrál (slajd 6). Jediné, co se nedá zaručit, je **najít** kořeny jmenovatele (viz Abelova–Ruffiniho věta); v příkladech jsou proto vždy „hezké“.

## §3 Šablony pro per partes

### Polynom krát $\sin$, $\cos$ nebo $e^{\lambda t}$ (slajdy 8 a 10)

Ve [[metoda per partes|per partes]] $\int_a^b f' g = [fg]_a^b - \int_a^b f g'$ se za $g$ volí **polynom** (ten se derivuje) a za $f'$ funkce $\sin$, $\cos$ nebo $e^{\lambda t}$ (ta se integruje a nezhorší se). Každý krok sníží stupeň polynomu o $1$, po $\deg g$ krocích zbude tabulkový integrál. ^polynom-krat

> [!example] Příklad (slajd 8)
> $\int_{-2}^3 t^2 \sin t\,\mathrm{d}t$: první per partes ($g = t^2$, $f = -\cos t$) dá $[-t^2\cos t]_{-2}^3 + \int_{-2}^3 2t\cos t\,\mathrm{d}t$, druhé ($g = 2t$, $f = \sin t$) dá $[2t\sin t]_{-2}^3 - \int_{-2}^3 2\sin t\,\mathrm{d}t$. Dohromady
>
> $$
> \int_{-2}^3 t^2\sin t\,\mathrm{d}t = \left[-t^2\cos t + 2t\sin t + 2\cos t\right]_{-2}^3 = -7\cos 3 + 6\sin 3 + 2\cos 2 - 4\sin 2 \approx 3{,}307.
> $$

> [!example] Příklad (slajd 10)
> $\int t^2 e^{-2t}\,\mathrm{d}t$: dvakrát per partes s $g = t^2$, pak $g = t$ a pokaždé $f' = e^{-2t}$, $f = -\frac{1}{2}e^{-2t}$. Primitivní funkce je $-\frac{1}{4}(2t^2 + 2t + 1)e^{-2t}$ (kontrola derivováním: $\left(-\frac{1}{4}(2t^2 + 2t + 1)e^{-2t}\right)' = t^2e^{-2t}$).

> [!pozor] Opačná volba integrál zhorší
> Kdybys v $\int t^2\sin t$ zvolil $f' = t^2$ (integruješ polynom) a $g = \sin t$, vznikne $\int \frac{t^3}{3}\cos t$: stupeň vzroste a integrál je horší. Polynom se **derivuje**.

> [!navic] Integrály Fourierova typu (slajd 9)
> $\int_{-\pi}^{\pi} \sin(mt)\sin(nt)\,\mathrm{d}t$, $\int_{-\pi}^{\pi} \sin(mt)\cos(nt)\,\mathrm{d}t$ a $\int_{-\pi}^{\pi} \cos(mt)\cos(nt)\,\mathrm{d}t$ se počítají přes vzorce pro součin goniometrických funkcí na součet (ty není třeba se učit nazpaměť). Např. $\int_{-\pi}^{\pi} \sin 6t\cos 9t\,\mathrm{d}t = 0$. Tyto integrály jsou základ Fourierových řad.

### Exponenciála krát $\sin$, $\cos$: zacyklení (slajd 11)

> [!veta] Postup · slajd 11 (per partes se zacyklením)
> Pro $I = \int e^{\lambda t}\sin t\,\mathrm{d}t$ (nebo s $\cos t$) použijeme per partes **dvakrát se stejnou volbou** (v obou krocích derivujeme exponenciálu, nebo v obou goniometrickou funkci). Druhý krok vrátí původní integrál a vznikne rovnice
>
> $$
> \mathbf{I = F - c \cdot I}, \quad c > 0, \qquad\text{tedy}\qquad I = \frac{F}{1 + c},
> $$
>
> kde $F$ je už spočítaná část (hraniční členy).

^veta-zacykleni

> [!lidsky] Lidsky
> Exponenciála ani sinus se derivováním nezjednoduší, jen se „točí“: $\sin \to \cos \to -\sin$. Po dvou krocích jsi zpátky u $I$, jen s jiným znaménkem. Místo nekonečného cyklu stačí zapsat rovnici pro neznámé $I$ a vyřešit ji jako $2I = \dots$.

> [!example] Příklad (slajd 11)
> $I = \int_0^b e^{-t}\sin t\,\mathrm{d}t$, $b > 0$. Per partes s $g = e^{-t}$, $f' = \sin t$: $I = [-e^{-t}\cos t]_0^b - \int_0^b e^{-t}\cos t\,\mathrm{d}t = 1 - e^{-b}\cos b - J$. Znovu s $g = e^{-t}$, $f' = \cos t$: $J = [e^{-t}\sin t]_0^b + \int_0^b e^{-t}\sin t\,\mathrm{d}t = e^{-b}\sin b + I$. Tedy
>
> $$
> I = 1 - e^{-b}\cos b - e^{-b}\sin b - I \quad\Longrightarrow\quad I = \frac{1}{2} - \frac{1}{2}e^{-b}(\cos b + \sin b).
> $$

> [!pozor] Ve druhém kroku stejnou volbu
> Kdybys ve druhém per partes derivoval $\cos t$ a integroval $e^{-t}$ (opačně než v prvním), vrátí se krok zpátky a vyjde identita $I = I$, ze které nic neplyne.

> [!obrazek] Zacyklená per partes: hodnota integrálu jako funkce horní meze
> ![[ma113-zacykleni.png]]
> *Modrá křivka je integrand $e^{-t}\sin t$, oranžová hodnota $I(b) = \frac{1}{2} - \frac{1}{2}e^{-b}(\cos b + \sin b)$ pro horní mez $b$. Oranžová roste tam, kde je modrá kladná, a klesá, kde je záporná; pro velká $b$ se blíží zelené hodnotě $\frac{1}{2}$.*

> [!navic] Integrování je umění (slajd 12)
> Výpočet určitých integrálů nemá univerzální algoritmus, tahle přednáška ukázala jen nejběžnější šablony. Na trénink doporučuje přednášející Děmidovičovu sbírku (úlohy 1031–1781). U zkoušky „exotické“ integrály nebudou.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč se racionální funkce před rozkladem na parciální zlomky nejdřív dělí se zbytkem?
> Rozklad na parciální zlomky platí jen pro **ryze lomenou** funkci ($\deg r < \deg b$). Dělení dá $\frac{a}{b} = q + \frac{r}{b}$: polynom $q$ se zintegruje hned a na ryze lomený zbytek se použije rozklad.

> [!karta|02]- Jak poznáš násobnost kořene $p$ a proč je v definici podmínka $a^\ast(p) \neq 0$?
> Násobnost $k$ = kolikrát lze vytknout $(x - p)$: $a(x) = (x - p)^k a^\ast(x)$. Podmínka **$a^\ast(p) \neq 0$** zaručí, že se vytklo všechno; jinak by šlo vytknout ještě jednou a $k$ by nebylo určené jednoznačně.

> [!karta|03]- Proč má každý reálný polynom lichého stupně aspoň jeden reálný kořen?
> Nad $\mathbb{R}$ se rozloží na **lineární a kvadratické** ireducibilní činitele. Kdyby byly všechny kvadratické, byl by stupeň sudý. Lichý stupeň proto vynutí aspoň jeden **lineární činitel** $(x - p)$, tedy reálný kořen $p$.

> [!karta|04]- Proč nad $\mathbb{R}$ nejsou ireducibilní polynomy stupně 3 a vyšší, když nad $\mathbb{C}$ jsou jen stupně 1?
> Podle základní věty algebry se v $\mathbb{C}$ rozloží na lineární závorky. Komplexní kořeny reálného polynomu chodí v **párech $z$, $\bar z$** a $(x - z)(x - \bar z)$ je **reálný kvadratický** polynom se záporným diskriminantem. Víc než stupeň 2 tedy nad $\mathbb{R}$ zůstat nemůže.

> [!karta|05]- Je pravda, že reálný polynom bez reálných kořenů je ireducibilní v $\mathbb{R}[x]$?
> **Ne**, platí to jen pro stupeň 2 (a 1). Protipříklad: $x^4 + 4$ nemá reálné kořeny, ale $x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)$.

> [!karta|06]- Jaký tvar má rozklad na parciální zlomky pro jmenovatel $(t - 1)^2(t^2 + 1)$ a proč právě tolik neznámých?
> $\dfrac{A_1}{t - 1} + \dfrac{A_2}{(t - 1)^2} + \dfrac{Bt + C}{t^2 + 1}$: za dvojnásobný kořen $1$ **dva zlomky s konstantou** (mocniny $1$ a $2$), za ireducibilní $t^2 + 1$ **jeden zlomek s lineárním čitatelem**. Neznámých je **4 = stupeň jmenovatele**, stejně jako rovnic při porovnání koeficientů.

> [!karta|07]- Proč má parciální zlomek s kvadratickým jmenovatelem v čitateli $Bt + C$, a ne jen konstantu?
> V čitateli smí být libovolný polynom **stupně menšího než ireducibilní kus**, u kvadratického tedy stupeň až 1. S jedinou konstantou by neznámých bylo málo a např. $\frac{t - 8}{t^2 + 1}$ by rozložit nešlo.

> [!karta|08]- Jak se integruje $\frac{At + B}{at^2 + bt + c}$ se záporným diskriminantem?
> Čitatel se napíše jako **násobek derivace jmenovatele** plus konstanta. První část dá substitucí $u = at^2 + bt + c$ **logaritmus**, druhá se **doplněním na čtverec** a substitucí převede na $\int \frac{\mathrm{d}z}{z^2 + 1} = \arctan z$.

> [!karta|09]- Co musíš zkontrolovat, než integruješ racionální funkci od $a$ do $b$?
> Že jmenovatel **nemá na $[a; b]$ nulový bod**: věty o určitém integrálu jsou pro funkce spojité na $[a; b]$. Např. $\int_2^6 \frac{\mathrm{d}t}{t - 2}$ vede na $\int_0^4 \frac{\mathrm{d}u}{u}$, který jako určitý integrál neexistuje.

> [!karta|10]- Kterou funkci v per partes derivuješ u $\int p(t)\sin t$ nebo $\int p(t)e^{\lambda t}$, kde $p$ je polynom, a proč?
> **Polynom derivuješ** ($u = p$), $\sin$ nebo $e^{\lambda t}$ integruješ. Každý krok sníží stupeň polynomu o 1 a integrovaná funkce se nezhorší, takže po $\deg p$ krocích zbude tabulkový integrál.

> [!karta|11]- Jak funguje per partes se zacyklením u $\int e^{-t}\sin t$?
> Dvakrát per partes se **stejnou volbou** (exponenciálu derivuješ v obou krocích) vrátí původní integrál: $I = (\text{známé}) - I$. Vznikne **rovnice** $2I = \dots$, ze které se $I$ vyjádří.

> [!karta|12]- Proč v praxi kořeny jmenovatele hádáme, místo abychom je počítali vzorcem?
> Podle **Abelovy–Ruffiniho věty** obecný vzorec z koeficientů a odmocnin existuje jen pro stupeň **$\leq 4$** (pro stupeň 3 a 4 je navíc nepraktický), pro stupeň **5 a vyšší neexistuje**. Rozklad jmenovatele proto stojí na **uhodnutých kořenech** (zkoušej dělitele absolutního členu) a dělení polynomů; ve zkouškových úlohách jsou kořeny „hezké“.

### Příklady na procvičení

> [!priklad|13]- Vyděl se zbytkem $(x^3 + 2x^2 - x + 3) : (x - 1)$.
> $x^3 + 2x^2 - x + 3 = (x^2 + 3x + 2)(x - 1) + 5$, tedy **$q = x^2 + 3x + 2$, $r = 5$**. Kontrola: $a(1) = 5 = r$.

> [!priklad|14]- Urči kořeny polynomu $x^3 - 3x + 2$ i s násobností.
> Uhodnutý kořen 1, dělením $x^3 - 3x + 2 = (x - 1)(x^2 + x - 2) = (x - 1)^2(x + 2)$. **1 je dvojnásobný, $-2$ jednoduchý kořen** (celkem 3 = stupeň).

> [!priklad|15]- Rozlož na parciální zlomky $\frac{3t + 5}{(t + 1)(t + 3)}$.
> $3t + 5 = A(t + 3) + B(t + 1)$. $t = -1$: $2 = 2A$, $A = 1$; $t = -3$: $-4 = -2B$, $B = 2$. **$\frac{1}{t + 1} + \frac{2}{t + 3}$**. Kontrola $t = 0$: $\frac{5}{3} = 1 + \frac{2}{3}$.

> [!priklad|16]- Spočítej $\int_2^3 \frac{4t + 8}{t^2 + 2t - 3}\,\mathrm{d}t$.
> Rozklad $\frac{1}{t + 3} + \frac{3}{t - 1}$ (jmenovatel je na $[2; 3]$ nenulový). $\left[\ln(t + 3) + 3\ln(t - 1)\right]_2^3 = \ln 6 - \ln 5 + 3\ln 2 =$ **$\ln\frac{48}{5} \approx 2{,}262$**.

> [!priklad|17]- Spočítej $\int_0^1 \frac{1}{t^2 + 2t + 2}\,\mathrm{d}t$.
> Doplnění na čtverec: $t^2 + 2t + 2 = (t + 1)^2 + 1$, substituce $z = t + 1$: $\int_1^2 \frac{\mathrm{d}z}{z^2 + 1}$ $=$ **$\arctan 2 - \frac{\pi}{4} \approx 0{,}322$**.

> [!priklad|18]- Spočítej $\int_0^\pi t^2\cos t\,\mathrm{d}t$.
> Per partes ($u = t^2$): $\left[t^2\sin t\right]_0^\pi - \int_0^\pi 2t\sin t\,\mathrm{d}t = 0 - 2\left(\left[-t\cos t\right]_0^\pi + \int_0^\pi \cos t\,\mathrm{d}t\right) = -2(\pi + 0) =$ **$-2\pi$**.

> [!priklad|19]- Spočítej $\int_0^\pi e^t\cos t\,\mathrm{d}t$.
> Dvakrát per partes ($v' = e^t$ v obou krocích): $I = \left[e^t\cos t\right]_0^\pi + \int_0^\pi e^t\sin t\,\mathrm{d}t = (-e^\pi - 1) + \left[e^t\sin t\right]_0^\pi - I$. Tedy $2I = -e^\pi - 1$, **$I = -\frac{e^\pi + 1}{2} \approx -12{,}07$**.

> [!priklad|20]- Rozhodni, zda je $x^2 + x + 1$ ireducibilní v $\mathbb{R}[x]$.
> $D = 1 - 4 = -3 < 0$, reálné kořeny nemá, a protože jde o stupeň 2, **je ireducibilní** (rozklad by musel obsahovat lineární činitel, tedy reálný kořen).

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 2. semestrálnímu testu (J. Velebil, 7.–11. 12. 2026, témata 06A–08A). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|21]- Nalezněte velikost plochy obrazce vymezeného grafem funkce $x \mapsto x\sin x$ a osou $x$ na intervalu $[0; \pi]$.
> Na $[0; \pi]$ je $x\sin x \geq 0$, plocha je tedy $\int_0^\pi x\sin x\,\mathrm{d}x$. Per partes ($u = x$, $v' = \sin x$): $\left[-x\cos x\right]_0^\pi + \int_0^\pi \cos x\,\mathrm{d}x = \pi + 0$. **Plocha je $\pi$.**

> [!priklad|22]- Spočítejte $\int_1^2 \frac{2x + 3}{x^2 + 3x}\,\mathrm{d}x$.
> Jmenovatel $x(x + 3)$ je na $[1; 2]$ nenulový a čitatel je jeho derivace. Substituce $u = x^2 + 3x$, $\mathrm{d}u = (2x + 3)\,\mathrm{d}x$: $\int_4^{10}\frac{\mathrm{d}u}{u} = \ln 10 - \ln 4 =$ **$\ln\frac{5}{2}$**. (Rozklad $\frac{1}{x} + \frac{1}{x + 3}$ dá totéž.)

> [!priklad|23]- Nalezněte velikost plochy obrazce vymezeného grafem $x \mapsto x e^{-x}$, osou $x$ a přímkami $x = 0$ a $x = 1$.
> Na $[0; 1]$ je $xe^{-x} \geq 0$. Per partes ($u = x$, $v' = e^{-x}$, $v = -e^{-x}$): $\left[-xe^{-x}\right]_0^1 + \int_0^1 e^{-x}\,\mathrm{d}x = -e^{-1} + 1 - e^{-1}$. **Plocha je $1 - \frac{2}{e} \approx 0{,}264$.**

> [!priklad|24]- Dokažte nebo vyvraťte: Každý polynom stupně 4 s reálnými koeficienty má aspoň jeden reálný kořen.
> **Tvrzení neplatí.** Protipříklad: $p(x) = x^4 + 1$. Pro každé reálné $x$ je $x^4 \geq 0$, tedy $p(x) \geq 1 > 0$, takže $p$ reálný kořen nemá. (Rozkládá se na dva ireducibilní kvadratické činitele $(x^2 + \sqrt{2}\,x + 1)(x^2 - \sqrt{2}\,x + 1)$, oba se záporným diskriminantem $2 - 4 < 0$.)

> [!priklad|25]- Dokažte nebo vyvraťte: Ať $f$ je spojitá na $[0; 1]$ a $\int_0^1 f(x)\,\mathrm{d}x = 0$. Potom $f(x) = 0$ pro všechna $x \in [0; 1]$.
> **Tvrzení neplatí.** Protipříklad $f(x) = 2x - 1$: je spojitá, $\int_0^1 (2x - 1)\,\mathrm{d}x = \left[x^2 - x\right]_0^1 = 0$, ale $f(0) = -1 \neq 0$.

---
← [[MA1 12 – Linearita, per partes a substituce v integrálu|4. 11. 2026 Linearita, per partes a substituce v integrálu]] · [[MA1 14 – Nevlastní integrál, délka křivky a objem rotačního tělesa|11. 11. 2026 Nevlastní integrál, délka křivky a objem rotačního tělesa]] →

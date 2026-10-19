---
predmet: MA1
prednaska: 2
datum: 2026-09-24
zdroj: "Handout 1B (Celá, racionální a reálná čísla), slajdy 3–14"
tags: [prednaska, MA1]
---

# MA1 02 – Celá, racionální a reálná čísla

*Přednáška 2 · čtvrtek 24. 9. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 1B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout01b.pdf)

Témata: `ℤ` · `ℚ` · `√2 ∉ ℚ` · `Dedekindovy řezy` · `ℝ` · `absolutní hodnota` · `úplnost` · `Archimedova vlastnost`

Minule vznikla [[přirozená čísla]] z prázdné množiny. Dnes se z nich postaví celá a racionální čísla a pak reálná. Důvod pro ℝ je jediný, ale zásadní: v ℚ jsou „díry“ a [[supremum]] shora omezené množiny v ℚ nemusí existovat. V ℝ existuje vždy, a na tom stojí celá analýza (limity, spojitost, integrál).

## §0 Přehled na jedné stránce

| množina | postavená z | prvek je | co přibude | co ještě chybí |
|---|---|---|---|---|
| $\mathbb{Z}$ | dvojic $(m, n)$ z $\mathbb{N}$ | „rozdíl“ $m - n$ | odčítání | dělení |
| $\mathbb{Q}$ | dvojic $(a, b)$ ze $\mathbb{Z}$, $b \neq 0$ | „zlomek“ $a/b$ | dělení (ne nulou) | díry, např. $\sqrt{2}$ |
| $\mathbb{R}$ | Dedekindových řezů $(L, U)$ na $\mathbb{Q}$ | „střih“ racionální přímky | supremum každé neprázdné shora omezené množiny | nic, je úplné |

## §1 Celá čísla ℤ

[[celá čísla|Celá čísla]] obsahují i čísla menší než $0$. Jenže co to je, když zatím máme jen $\mathbb{N}$? Zkonstruují se z $\mathbb{N}$:

> [!definice] Idea · slajd 3
> $$
> -3 = \{(n, n + 3) \mid n \in \mathbb{N}\}, \qquad -5 = \{(n, n + 5) \mid n \in \mathbb{N}\}
> $$
>
> Uspořádaná dvojice $(5, 8)$ „kóduje“ rozdíl $5 - 8$. Celé číslo je celá množina dvojic, které kódují stejný rozdíl.

^def-cela

> [!lidsky] Lidsky
> Záporné číslo je dluh. Dvojice $(m, n)$ znamená „mám $m$, dlužím $n$“. Stav $(5, 8)$, $(0, 3)$ i $(100, 103)$ je pořád stejný dluh $3$, tedy číslo $-3$. Protože v $\mathbb{N}$ ještě neumíme odčítat, pamatujeme si obě čísla a rozdíl „necháme na potom“.

> [!navic] Kdy dvě dvojice kódují stejné číslo
> $(m, n)$ a $(m', n')$ představují stejné celé číslo, právě když $m + n' = m' + n$. Podmínka používá jen sčítání, které v $\mathbb{N}$ máme. Příklad: $(5, 8)$ a $(0, 3)$: $5 + 3 = 8 = 0 + 8$ ✓.

> [!navic] Co je ještě potřeba dodělat · slajdy 3–4
> Definovat uspořádané dvojice, definovat $+$ a $\cdot$ se správnými vlastnostmi a ukázat, že $\mathbb{N}$ se svými operacemi „zůstane“ uvnitř $\mathbb{Z}$. Přesně se konstrukce dělá pomocí tříd ekvivalence, a ty se probírají v předmětu [[LGR – Logika a grafy|Logika a grafy]].

## §2 Racionální čísla ℚ

[[racionální čísla|Racionální čísla]] jsou čísla, která jdou napsat zlomkem. Zkonstruují se ze $\mathbb{Z}$:

> [!definice] Idea · slajd 4
> $$
> \frac{2}{-3} = \{(a, b) \mid a, b \in \mathbb{Z},\ b \neq 0 \text{ a } -3a = 2b\}
> $$
>
> Dvojice $(6, -9)$ „kóduje“ zlomek $\frac{6}{-9}$, který je stejným číslem jako $\frac{2}{-3}$.

^def-racionalni

Kontrola podmínky: $-3 \cdot 6 = -18 = 2 \cdot (-9)$ ✓. Podmínka $-3a = 2b$ je rovnost $\frac{a}{b} = \frac{2}{-3}$ „vynásobená do kříže“, aby se v ní nedělilo.

> [!lidsky] Lidsky
> Zlomky $\frac{2}{-3}$, $\frac{4}{-6}$ a $\frac{6}{-9}$ vypadají různě, ale jde o stejné číslo. Racionální číslo proto není jeden zlomek, ale celá „rodina“ zlomků, které se dají zkrátit na stejný tvar.

> [!obrazek] Celá a racionální čísla jako třídy dvojic
> ![[ma102-konstrukce.png]]
> *Vlevo mřížka dvojic (m, n) přirozených čísel. Body na jedné úhlopříčce kódují stejný rozdíl m − n: oranžová −3 (mj. dvojice (5, 8)), šedá 0, modrá 2. Vpravo dvojice (a, b) celých čísel s b ≠ 0 (červená čárkovaná řada je zakázaná). Body na jedné přímce přes počátek kódují stejný zlomek: modrá 2/−3, zelená 1.*

Současná situace: $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q}$.

> [!navic] Proč ⊆ jen „v uvozovkách“
> Prvky $\mathbb{Z}$ jsou množiny dvojic, prvky $\mathbb{N}$ ne. Doslova tedy $\mathbb{N} \not\subseteq \mathbb{Z}$. Přirozené číslo $n$ se do $\mathbb{Z}$ **vnoří** jako třída dvojice $(n, 0)$ a stejně se $\mathbb{Z}$ vnoří do $\mathbb{Q}$ jako zlomky se jmenovatelem $1$. Zápis $\subseteq$ znamená „až na tohle přejmenování“.

## §3 √2 není racionální

> [!veta] Tvrzení · slajd 5
> **Neexistuje $r \in \mathbb{Q}$ takové, že $r^2 = 2$.**
>
> > [!note]- Důkaz sporem (tři případy)
> > - **$r = 0$:** $r \cdot r = r^2 = 0 \neq 2$ ↯
> > - **$r > 0$:** zapíšeme $r = \frac{p}{q}$, kde $p, q \in \mathbb{N}$ jsou nesoudělná (zlomek v základním tvaru). Z $\frac{p^2}{q^2} = 2$ plyne $2q^2 = p^2$, tedy $p^2$ je sudé, a proto $p$ je sudé: $p = 2k$. Dosazením $2q^2 = 4k^2$, tedy $q^2 = 2k^2$, takže $q^2$ je sudé a $q$ je sudé. Obě čísla $p, q$ jsou sudá, ale měla být nesoudělná ↯
> > - **$r < 0$:** $r = -s$, kde $s > 0$. Pak $r^2 = (-s)(-s) = s^2 = 2$, a to je případ $s > 0$, který už vede ke sporu ↯

^veta-odmocnina

> [!navic] Proč z „p² je sudé“ plyne „p je sudé“
> Obměnou: je-li $p$ liché, $p = 2m + 1$, pak $p^2 = 4m^2 + 4m + 1 = 2(2m^2 + 2m) + 1$ je liché. Tenhle krok se u zkoušky vyplatí napsat, sám o sobě je to malý důkaz.

Takže „$\sqrt{2} \notin \mathbb{Q}$“ a řetězec $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq {?}$ potřebuje další patro.

> [!lidsky] Lidsky
> Racionální čísla leží na přímce hustě: mezi každými dvěma je další. Přesto v ní mají díry. Tam, kde by mělo ležet číslo s druhou mocninou $2$, žádné racionální číslo není. Zlomky $1{,}4$; $1{,}41$; $1{,}414$ se k té díře blíží zleva, $1{,}5$; $1{,}42$; $1{,}415$ zprava, ale díru nezaplní.

## §4 Dedekindovy řezy

Díru popíšeme tím, co leží nalevo a napravo od ní:

$$
L = \{r \in \mathbb{Q} \mid r^2 < 2 \text{ nebo } r < 0\} \quad \text{(dolní racionální aproximace } \sqrt{2}\text{)},
$$

$$
U = \{r \in \mathbb{Q} \mid r^2 > 2 \text{ a současně } r > 0\} \quad \text{(horní racionální aproximace } \sqrt{2}\text{)},
$$

$$
\sqrt{2} \overset{\text{def}}{=} (L, U).
$$

To znamená, že podobně jako u $\mathbb{Z}$ máme dvojici. [[Dedekindův řez|Dedekindovým řezem]] se dá definovat jakékoliv reálné číslo.

> [!obrazek] Řez racionální přímky v místě √2
> ![[ma102-rez.png]]
> *Nahoře: modrá L (záporná čísla a čísla s r² < 2), oranžová U (kladná s r² > 2). Mezi nimi je v ℚ díra, prázdné kolečko; řez (L, U) je nové číslo √2. Dole: M = (0; 1) má supremum 1, které v M neleží, takže maximum neexistuje; červeně další horní odhady.*

> [!definice] Dedekindův řez · slajd 7
> Dvojice $(L, U)$ je *Dedekindův řez* na $\mathbb{Q}$, pokud
>
> 1. $\emptyset \neq L \subseteq \mathbb{Q}$ a $\emptyset \neq U \subseteq \mathbb{Q}$,
> 2. $L$ je přesně množina všech dolních odhadů $U$ a $U$ je přesně množina všech horních odhadů $L$.
>
> *Reálná čísla* $\mathbb{R}$ jsou množina všech Dedekindových řezů na $\mathbb{Q}$.

^def-rez

> [!lidsky] Lidsky
> Řez je střih nůžkami přes racionální přímku: co je nalevo, jde do $L$, co napravo, do $U$. Když se střih trefí přímo do racionálního čísla $q$, leží $q$ v obou částech a řez je prostě $q$. Když se trefí do díry, vznikne nové, [[iracionální číslo|iracionální]] číslo. Reálné číslo tedy není „nekonečný desetinný rozvoj“, ale místo střihu.

> [!question]- Jak vypadá řez pro racionální číslo ½?
> $L = \{r \in \mathbb{Q} \mid r \le \frac12\}$, $U = \{r \in \mathbb{Q} \mid r \ge \frac12\}$. Dolní odhady $U$ jsou přesně čísla $\le \frac12$ a horní odhady $L$ přesně čísla $\ge \frac12$, takže obě podmínky platí.

## §5 ℝ je uspořádané těleso

[[reálná čísla|Reálná čísla]] $\mathbb{R}$ vybudovaná pomocí řezů mají dvě důležité vlastnosti:

- jsou [[číselné těleso|těleso]]: existují operace $+$ a $\cdot$ se známými vlastnostmi, $r^{-1}$ existuje pro $r \neq 0$ `slajd 8`,
- jsou uspořádaná pomocí [[pozitivní kužel|pozitivního kužele]] $\mathbb{R}^+$ (kladných čísel), který je uzavřený na součet a součin: $r, s \in \mathbb{R}^+ \Rightarrow r + s \in \mathbb{R}^+$ a $r \cdot s \in \mathbb{R}^+$.

> [!definice] Uspořádané těleso · slajd 8
> $\mathbb{R}$ je uspořádané: existuje $\mathbb{R}^+ \subseteq \mathbb{R}$ takové, že
>
> 1. $\mathbb{R} = \{-r \mid r \in \mathbb{R}^+\} \cup \{0\} \cup \mathbb{R}^+$ a tyto tři části jsou disjunktní,
> 2. $r, s \in \mathbb{R}^+ \Rightarrow r + s \in \mathbb{R}^+$ a $r \cdot s \in \mathbb{R}^+$.
>
> Pomocí $\mathbb{R}^+$ se pak definuje nerovnost: $r < s$ právě když $s - r \in \mathbb{R}^+$.

^def-kuzel

> [!obrazek] Pozitivní kužel a nerovnost
> ![[ma102-kuzel.png]]
> *Modře kladná čísla ℝ⁺, oranžově čísla k nim opačná, uprostřed 0. Zelená šipka: r < s znamená, že rozdíl s − r je kladný, tedy od r k s se jde doprava.*

> [!pozor] Kladná čísla se nesmí definovat nerovností
> Dvojice „$\mathbb{R}^+ = \{r \in \mathbb{R} \mid r > 0\}$“ a „$r < s \Leftrightarrow s - r \in \mathbb{R}^+$“ je definice v kruhu: $>$ se definuje pomocí $\mathbb{R}^+$ a $\mathbb{R}^+$ pomocí $>$. Správně je $\mathbb{R}^+$ dané **napřed** (vlastnosti 1 a 2 výše) a nerovnost se z něj teprve vyrobí. Zápis $\{r \mid r > 0\}$ je až důsledek.

> [!lidsky] Lidsky
> Stačí vědět, která čísla jsou kladná, a uspořádání dostaneš zadarmo: „$r < s$“ znamená „od $r$ k $s$ se jde doprava“, tedy rozdíl $s - r$ je kladný. Vlastnost 1 říká, že každé číslo je buď kladné, nebo nula, nebo opačné ke kladnému, a nic z toho zároveň.

Z nerovnosti se jednoduše definuje [[absolutní hodnota]]:

$$
|r| = \begin{cases} r & \text{pro } r \ge 0, \\ -r & \text{pro } r < 0. \end{cases}
$$

^def-abs

Tři důležité vlastnosti $|\cdot|$:

1. $|x| \ge 0$ a $|x| = 0 \Leftrightarrow x = 0$,
2. $|x \cdot y| = |x| \cdot |y|$,
3. $|x + y| \le |x| + |y|$ (trojúhelníková nerovnost).

*Vzdálenost* čísel $x, y \in \mathbb{R}$ definujeme jako $|x - y|$.

> [!lidsky] Lidsky
> $|x|$ je vzdálenost $x$ od nuly, $|x - y|$ vzdálenost dvou bodů na přímce. Trojúhelníková nerovnost říká, že zajížďka přes třetí bod není kratší: $|x - z| \le |x - y| + |y - z|$. Příklad: $|3 + (-5)| = 2 \le |3| + |{-5}| = 8$; rovnost nastane, jen když mají $x$ a $y$ stejné znaménko (nebo je jedno z nich nula).

> [!veta] Počítání s nerovnostmi · slajd 9
> - Trichotomie: vždy platí právě jedno z $r < s$, $r = s$, $s < r$.
> - $r < s$ a $t > 0$ $\Rightarrow$ $rt < st$ (násobení kladným číslem nerovnost nemění).
> - $0 < r < s$ $\Rightarrow$ $0 < \frac{1}{s} < \frac{1}{r}$.
> - $|x| < s \Leftrightarrow -s < x < s$. Tohle se u limit použije pořád.

^veta-nerovnosti

## §6 Úplnost ℝ a supremum

$\mathbb{R}$ je [[Dedekindovská úplnost|úplné]] uspořádané těleso (ve smyslu Dedekinda).

> [!veta] Dedekindovská úplnost · slajd 10
> ==Ať $M \subseteq \mathbb{R}$, $M \neq \emptyset$ a $M$ je shora omezená== (existuje $u \in \mathbb{R}$ tak, že $x \le u$ pro všechna $x \in M$). Potom **$\sup M$ existuje v $\mathbb{R}$**.

^def-uplnost

Každé takové $u$ je [[horní odhad]] $M$, $\sup M$ je nejmenší horní odhad (definice z [[MA1 01 – Množiny, uspořádání a přirozená čísla#^def-sup|přednášky 1]]).

> [!lidsky] Lidsky
> V $\mathbb{R}$ nejsou díry: každá neprázdná [[shora omezená množina]] má nejnižší strop přímo v $\mathbb{R}$. V $\mathbb{Q}$ to neplatí. Množina $L$ z řezu $\sqrt{2}$ je shora omezená (třeba číslem $2$), ale v $\mathbb{Q}$ nemá nejmenší horní odhad: ke každému racionálnímu stropu nad $\sqrt{2}$ najdeš ještě menší. Proto analýza pracuje v $\mathbb{R}$, ne v $\mathbb{Q}$.

Příklady:

1. $M = (0; 1)$: $\sup M = 1$, ale $1 \notin M$, takže **maximum neexistuje** (obrázek výše, dole).
2. $M = L$ (dolní část řezu $\sqrt{2}$): $\sup M = \sqrt{2}$.

Po vynásobení $M \cdot (-1)$ získáme i infimum:

> [!veta] Infimum · slajd 12
> ==Každá neprázdná zdola omezená $M \subseteq \mathbb{R}$== **má infimum** a platí
>
> $$
> \inf M = -\sup(-M), \qquad \text{kde } -M = \{-m \mid m \in M\}.
> $$
>
> Zdola omezená $M$ dává shora omezenou $-M$, ta má supremum a to se otočí zpět.

^veta-inf

> [!veta] Supremum pomocí ε · slajd 13
> $s = \sup M$ právě když
>
> 1. $x \le s$ pro všechna $x \in M$ ($s$ je horní odhad),
> 2. pro každé $\varepsilon > 0$ existuje $x \in M$ tak, že $s - \varepsilon < x \le s$ (strop nejde snížit ani o kousek).
>
> Tuhle podobu použiješ skoro v každém důkazu s limitou.

^veta-eps-sup

> [!lidsky] Lidsky
> Infimum dostaneš ze suprema „přes zrcadlo“: otoč množinu kolem nuly, najdi strop a otoč zpátky. A supremum poznáš podle toho, že je to strop, pod který už nejde slézt ani o kousek: kdybys ho snížil o libovolně malé $\varepsilon$, nějaký prvek $M$ by ho přelezl.

> [!obrazek] Strop, který nejde snížit
> ![[ma102-supremum.png]]
> *M = {1 − 1/n}: čárky jsou prvky M, prázdné kolečko je s = sup M = 1 (v M neleží). Zelený pás (s − ε; s] obsahuje nekonečně mnoho prvků M, ať je ε jakkoli malé; nad s neleží nic.*

## §7 Archimedova vlastnost

Z Dedekindovy úplnosti plyne [[Archimedova vlastnost]]:

> [!veta] Archimedova vlastnost · slajd 14
> **Pro každé $s \in \mathbb{R}$ a každé $r \in \mathbb{R}^+$ existuje $n \in \mathbb{N}^+$ tak, že $s < n \cdot r$.**
>
> Důsledky: mezi každými dvěma reálnými čísly $r < s$ leží racionální $q$ ($r < q < s$) a $\inf\{\frac{1}{n} \mid n \in \mathbb{N}^+\} = 0$.

^veta-archimedes

> [!pozor] Záleží na pořadí kvantifikátorů
> Bez „pro každé“ a „existuje“ věta nic neříká. Správně: **pro každé** $s$ a **každé** $r > 0$ **existuje** $n$. Číslo $n$ smí záviset na $s$ i $r$; kdyby jedno $n$ mělo fungovat pro všechna $s$, tvrzení by neplatilo.

> [!lidsky] Lidsky
> Krokem délky $r$ (třeba 1 mm) dojdeš za libovolné číslo $s$ (třeba $10^{100}$), když uděláš dost kroků. Neexistuje tedy „nekonečně velké“ reálné číslo. Otočeně: $\frac{1}{n}$ se dostane pod libovolné kladné číslo, takže neexistuje ani „nekonečně malé“ kladné reálné číslo.

> [!obrazek] Archimedova vlastnost
> ![[ma102-archimedes.png]]
> *Kroky délky r (modře) od nuly. Číslo s (červeně) leží mezi 7r a 8r, osmý krok (zeleně) ho přeskočí: 8 · r > s. Pro větší s nebo menší r jen potřebuješ víc kroků.*

> [!navic] Důkaz z úplnosti (typ B2)
> Sporem: ať $n \cdot r \le s$ pro všechna $n \in \mathbb{N}^+$. Pak je $M = \{n \cdot r \mid n \in \mathbb{N}^+\}$ neprázdná a shora omezená číslem $s$, takže má supremum $S$. Číslo $S - r < S$ už horní odhad není, existuje tedy $n$ s $n \cdot r > S - r$. Pak ale $(n + 1) \cdot r > S$, a přitom $(n + 1) \cdot r \in M$ ↯

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- Kdy dvojice $(m, n)$ a $(m', n')$ kódují stejné celé číslo? Zapiš to bez odčítání.
> $m + n' = m' + n$. Např. $(5, 8)$ a $(0, 3)$: $5 + 3 = 0 + 8$.

> [!karta|04]- Dokaž, že neexistuje $r \in \mathbb{Q}$, $r > 0$, s $r^2 = 2$.
> $r = \frac{p}{q}$, $p, q$ nesoudělná. $2q^2 = p^2 \Rightarrow p$ sudé, $p = 2k \Rightarrow q^2 = 2k^2 \Rightarrow q$ sudé. Obě sudá, ale nesoudělná ↯

> [!karta|05]- Proč z toho, že $p^2$ je sudé, plyne, že $p$ je sudé?
> Obměnou: $p = 2m + 1$ liché dává $p^2 = 2(2m^2 + 2m) + 1$ liché.

> [!karta|06]- Jak je $\sqrt{2}$ definována Dedekindovým řezem?
> $\sqrt{2} = (L, U)$, $L = \{r \in \mathbb{Q} \mid r < 0 \text{ nebo } r^2 < 2\}$, $U = \{r \in \mathbb{Q} \mid r > 0 \text{ a } r^2 > 2\}$.

> [!karta|08]- Proč se kladná čísla nesmí definovat jako $\mathbb{R}^+ = \{r \mid r > 0\}$?
> Nerovnost se definuje **z** $\mathbb{R}^+$: $r < s \Leftrightarrow s - r \in \mathbb{R}^+$. Definice v kruhu. $\mathbb{R}^+$ je dané napřed: rozklad $\mathbb{R} = -\mathbb{R}^+ \cup \{0\} \cup \mathbb{R}^+$ a uzavřenost na $+$ a $\cdot$.

> [!karta|09]- Tři základní vlastnosti absolutní hodnoty?
> 1. $|x| \ge 0$ a $|x| = 0 \Leftrightarrow x = 0$
> 2. $|xy| = |x| \cdot |y|$
> 3. $|x + y| \le |x| + |y|$

> [!karta|10]- Kdy nastane v $|x + y| \le |x| + |y|$ rovnost?
> Když mají $x$ a $y$ stejné znaménko nebo je jedno z nich nula, tj. $xy \ge 0$. Např. $|3 + (-5)| = 2 < 8$.

> [!karta|13]- Jak se z úplnosti získá infimum a za jakých předpokladů?
> Pro neprázdnou zdola omezenou $M$: $\inf M = -\sup(-M)$, kde $-M = \{-m \mid m \in M\}$.

> [!karta|14]- Charakterizuj $s = \sup M$ pomocí $\varepsilon$.
> $x \le s$ pro všechna $x \in M$ **a** pro každé $\varepsilon > 0$ existuje $x \in M$ s $s - \varepsilon < x \le s$.

> [!karta|16]- Dokaž Archimedovu vlastnost z úplnosti $\mathbb{R}$.
> Sporem: ať $nr \le s$ pro všechna $n$. $M = \{nr\}$ je omezená, má $\sup M = S$. $S - r$ není horní odhad, tedy $nr > S - r$ pro nějaké $n$, a pak $(n + 1)r > S$ ↯

### Příklady na procvičení

> [!priklad|01]- Jak se v konstrukci $\mathbb{Z}$ zapíše $-3$ a co „kóduje“ dvojice $(5, 8)$?
> $-3 = \{(n, n + 3) \mid n \in \mathbb{N}\}$. Dvojice $(5, 8)$ kóduje rozdíl $5 - 8 = -3$.

> [!priklad|03]- Které dvojice kódují racionální číslo $\frac{2}{-3}$?
> $\{(a, b) \mid a, b \in \mathbb{Z},\ b \neq 0,\ -3a = 2b\}$, např. $(2, -3)$, $(6, -9)$, $(-4, 6)$.

> [!priklad|07]- Jak vypadá Dedekindův řez odpovídající racionálnímu číslu $\frac12$?
> $L = \{r \in \mathbb{Q} \mid r \le \frac12\}$, $U = \{r \in \mathbb{Q} \mid r \ge \frac12\}$. Číslo $\frac12$ leží v obou.

> [!priklad|11]- Uveď shora omezenou množinu, která nemá supremum v $\mathbb{Q}$.
> $L = \{r \in \mathbb{Q} \mid r < 0 \text{ nebo } r^2 < 2\}$. Je omezená číslem $2$, ale nejmenší horní odhad by byl $\sqrt{2} \notin \mathbb{Q}$.

> [!priklad|12]- Má $M = (0; 1)$ maximum a supremum?
> $\sup M = 1$, maximum **neexistuje**, protože $1 \notin M$.

> [!priklad|15]- Proč je $\inf\{\frac{1}{n} \mid n \in \mathbb{N}^+\} = 0$?
> $0$ je dolní odhad. Pro libovolné $\varepsilon > 0$ dá Archimedova vlastnost $n$ s $1 < n\varepsilon$, tedy $\frac{1}{n} < \varepsilon$. Žádné $\varepsilon > 0$ proto dolní odhad není.

---
← [[MA1 01 – Množiny, uspořádání a přirozená čísla|23. 9. 2026 Množiny, uspořádání a přirozená čísla]] · [[MA1 03 – Rozšířená reálná čísla a limita ve směru|30. 9. 2026 Rozšířená reálná čísla a limita ve směru]] →

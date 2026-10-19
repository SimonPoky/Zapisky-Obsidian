---
predmet: MA1
prednaska: 3
datum: 2026-09-30
zdroj: "Handout 1B, slajdy 15–16; handout 2A (Limita ve směru), slajdy 3–31"
tags: [prednaska, MA1]
---

# MA1 03 – Rozšířená reálná čísla a limita ve směru

*Přednáška 3 · středa 30. 9. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 1B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout01b.pdf) · [Handout 2A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout02a.pdf)

Témata: `ℝ*` · `okolí` · `směr` · `definice limity` · `jednoznačnost` · `7/(n − 6)` · `(−1)ⁿ` · `monotónní posloupnost`

Velebil zavádí [[limita ve směru|limitu]] jedinou definicí pro všechny případy: $x \to p$, $x \to p^+$, $n \to +\infty$, $x \to -\infty$… Liší se jen *směr*, odkud se blížíme. Místo šesti různých „ε-δ“ definic stačí jedna a ty ostatní z ní vyčteš.

## §0 Přehled na jedné stránce

| co | značka | pro $L \in \mathbb{R}$ | pro $+\infty$ |
|---|---|---|---|
| okolí cíle $L$ | $U_\varepsilon(L) \in \mathcal{N}(L)$ | $(L - \varepsilon; L + \varepsilon)$ | $(\varepsilon; +\infty]$ |
| kus směru | $P \in \mathcal{S}$ | $x \to p$: $(p - \delta; p) \cup (p; p + \delta)$ | $x \to +\infty$: $(\delta; +\infty)$ |
| limita | $\lim_{\mathcal{S}} f = L$ | ke každému $U$ existuje $P$ s $f[P] \subseteq U$ | totéž |

## §1 Rozšířená reálná čísla jako řezy

Řez $(L, U)$ z [[MA1 02 – Celá, racionální a reálná čísla#^def-rez|minulé přednášky]] má obě části neprázdné. Když podmínku neprázdnosti pustíme, dostaneme dva nové „řezy“:

$$
-\infty = (\emptyset, \mathbb{Q}), \qquad +\infty = (\mathbb{Q}, \emptyset).
$$

^rezy-nekonecna

> [!lidsky] Lidsky
> Střih úplně vlevo, před všemi čísly, je $-\infty$: nalevo nic, napravo všechno. Střih úplně vpravo je $+\infty$. Druhá podmínka řezu pro ně pořád platí ($\mathbb{Q}$ nemá v $\mathbb{Q}$ žádný dolní odhad, takže $L = \emptyset$ sedí), porušena je jen neprázdnost. Proto to nejsou reálná čísla, ale přidané krajní body.

> [!definice] Rozšířená reálná čísla · handout 1B, slajd 15
> $\mathbb{R}^* = \mathbb{R} \cup \{-\infty, +\infty\}$, kde $-\infty < r < +\infty$ pro všechna $r \in \mathbb{R}$. Počítání pro $r \in \mathbb{R}$:
>
> - $(+\infty) + r = +\infty$, $(-\infty) + r = -\infty$,
> - $r \cdot (+\infty) = +\infty$ a $r \cdot (-\infty) = -\infty$ pro $r > 0$; pro $r < 0$ obráceně,
> - $\frac{1}{\pm\infty} = 0$.
>
> **Nedefinované:** $+\infty - \infty$, $0 \cdot (\pm\infty)$, $\frac{\pm\infty}{\pm\infty}$, $\frac{1}{0}$.

^def-rstar

> [!veta] Suprema v ℝ* existují vždy · handout 1B, slajd 16
> Pro každou $M \subseteq \mathbb{R}$: $\sup M$ je obyčejné supremum, je-li $M \neq \emptyset$ shora omezená; $\sup M = +\infty$, je-li $M \neq \emptyset$ shora neomezená; $\sup \emptyset = -\infty$. Zrcadlově $\inf M = -\sup(-M)$ vždy existuje v $\mathbb{R}^*$. Je to stejný trik jako u $\mathbb{N}^*$ v [[MA1 01 – Množiny, uspořádání a přirozená čísla#^def-nstar|přednášce 1]].

^veta-sup-rstar

> [!lidsky] Lidsky
> $\mathbb{R}^*$ je číselná osa s přidanými dvěma konci. Díky nim má supremum úplně každá množina: neomezená má strop $+\infty$ a prázdná $-\infty$ (každé číslo je jejím horním odhadem, takže nejnižší strop je úplně dole). S nekonečny se počítá „selským rozumem“, jen kde by výsledek mohl být cokoli ($\infty - \infty$, $0 \cdot \infty$), zůstává nedefinovaný.

## §2 Funkce a posloupnost

$$
f : D \to \mathbb{R}, \qquad D \subseteq \mathbb{R},\ D \neq \emptyset.
$$

Je-li $D \subseteq \mathbb{N}$ nekonečná, mluvíme o [[posloupnost|posloupnosti]] a místo $f(n)$ píšeme $a_n$. ^def-posl-ma

> [!pozor] Zápisy f(2) = +∞ nebo f(−∞) = 1 nedávají smysl
> Funkce bere reálná čísla a vrací reálná čísla. $\pm\infty$ nejsou ani v definičním oboru, ani mezi hodnotami. Nekonečna se objeví jen jako *cíl* ($x \to +\infty$) nebo *výsledek* limity ($\lim f = +\infty$).

## §3 Idea limity

$\lim_{x \to p} f(x) = L$ znamená: ať chceš mít $f(x)$ jakkoli blízko $L$ (pás šířky $\varepsilon$ kolem $L$), stačí vzít $x$ dost blízko $p$ (pás šířky $\delta$ kolem $p$), ale $x \neq p$. Hodnota $f(p)$ v tom nehraje žádnou roli.

> [!obrazek] Limita v bodě: pás ε a pás δ
> ![[ma103-epsdelta.png]]
> *Modrý pás: hodnoty vzdálené od L méně než ε (terč). Oranžový pás: x vzdálená od p méně než δ, bez samotného p. Zelený kus grafu nad oranžovým pásem leží celý v modrém pásu. Červený bod: hodnota f(p) může být kdekoli, nebo nemusí existovat vůbec.*

Zbytek přednášky tuhle představu zobecní tak, aby stejná definice fungovala i pro $x \to +\infty$, $n \to +\infty$ nebo jednostranné limity: k tomu slouží okolí cíle (§4) a směr (§5).

## §4 Okolí bodu v ℝ*

> [!definice] Systém okolí · handout 2A, slajd 8
> Pro $L \in \mathbb{R}^*$ a $\varepsilon > 0$ je *otevřené ε-okolí*
>
> $$
> U_\varepsilon(L) = \begin{cases} (L - \varepsilon; L + \varepsilon), & L \in \mathbb{R}, \\ (\varepsilon; +\infty], & L = +\infty, \\ [-\infty; -\varepsilon), & L = -\infty, \end{cases}
> $$
>
> a $\mathcal{N}(L) = \{U_\varepsilon(L) \mid \varepsilon > 0\}$ je *systém okolí* bodu $L$ (anglicky neighbourhoods).

^def-okoli

Vlastnosti $\mathcal{N}(L)$:

1. $U \in \mathcal{N}(L) \Rightarrow U \neq \emptyset$,
2. $U, U' \in \mathcal{N}(L) \Rightarrow U \subseteq U'$ nebo $U' \subseteq U$ (okolí jsou do sebe vnořená),
3. $\bigcap_{U \in \mathcal{N}(L)} U = \{L\}$.

> [!lidsky] Lidsky
> [[okolí|Okolí]] je terč kolem $L$; čím menší $\varepsilon$, tím menší terč. U $+\infty$ je to naopak: terč $(\varepsilon; +\infty]$ je „všechno větší než $\varepsilon$“, takže **velké** $\varepsilon$ znamená **malý** terč. Průnik všech terčů je jen samotný střed $L$.

> [!obrazek] Okolí a směry
> ![[ma103-okoli.png]]
> *Nahoře okolí cíle: oranžově [−∞; −ε), modře (L − ε; L + ε), zeleně (ε; +∞]. Dole kusy směrů: modře x → p (bez bodu p, prázdné kolečko), oranžově x → p⁺, zeleně x → +∞.*

## §5 Směr

> [!definice] Směr · handout 2A, slajd 9
> *Směr* je kolekce $\mathcal{S} = \{P_i \subseteq \mathbb{R} \mid i \in I\}$ taková, že
>
> 1. každé $P \in \mathcal{S}$ je neprázdné,
> 2. pro každá $P, P' \in \mathcal{S}$ je $P \subseteq P'$ nebo $P' \subseteq P$,
> 3. $\bigcap_{P \in \mathcal{S}} P = \emptyset$.

^def-smer

> [!lidsky] Lidsky
> [[směr|Směr]] popisuje, **odkud** se k cíli blížíme. Je to kolekce „[[prstencové okolí|propíchnutých okolí]]“: zmenšují se k cíli, ale cíl samotný do nich nepatří. Proto je průnik prázdný, na rozdíl od okolí, kde průnik je $\{L\}$. Přibližujeme se k ideálnímu cíli, který v $\mathbb{R}$ může i chybět ($+\infty$), a hodnota v cíli nás nezajímá: $f$ tam klidně nemusí být definovaná, jako $\frac{\sin x}{x}$ v nule.

> [!obrazek] Okolí vs. směr
> ![[ma103-vnoreni.png]]
> *Vlevo okolí bodu L pro ε = 1; 0,6; 0,3; 0,1: všechna obsahují L, takže jejich průnik je {L}. Vpravo kusy směru x → p pro δ = 1; 0,6; 0,3; 0,1: bod p (prázdné kolečko) chybí ve všech, a proto je průnik prázdný.*

Příklady směrů (handout 2A, slajdy 11–16; pro všechna $\delta > 0$, resp. $n \in \mathbb{N}$):

| směr                          | kus směru $P$                                        |
| ----------------------------- | ---------------------------------------------------- |
| $x \to p$, $p \in \mathbb{R}$ | $P_\delta(p) = (p - \delta; p) \cup (p; p + \delta)$ |
| $x \to p^+$                   | $P^+_\delta(p) = (p; p + \delta)$                    |
| $x \to p^-$                   | $P^-_\delta(p) = (p - \delta; p)$                    |
| $n \to +\infty$               | $P_n(+\infty) = \{k \in \mathbb{N} \mid k > n\}$     |
| $x \to +\infty$               | $P_\delta(+\infty) = (\delta; +\infty)$              |
| $x \to -\infty$               | $P_\delta(-\infty) = (-\infty; -\delta)$             |

> [!veta] Nejmenší z konečně mnoha · handout 2A, slajd 10
> Z konečně mnoha prvků $P_1, \dots, P_k$ směru jde vždy vybrat ten nejmenší, který je obsažen ve všech ostatních (plyne z vlastnosti 2). Na tomhle stojí důkaz jednoznačnosti v §7 i většina dalších vět o limitách.

^veta-nejmensi-kus

> [!lidsky] Lidsky
> Kusy směru jsou do sebe vnořené jako matrjošky. Z konečně mnoha vždy vybereš ten nejmenší a ten leží ve všech ostatních, takže se v něm splní všechny podmínky naráz. U nekonečně mnoha to nejde: intervaly $(0; \frac{1}{n})$ nemají společný bod.

## §6 Definice limity

> [!definice] Limita ve směru · handout 2A, slajdy 17 a 19
> Ať $f$ je *definována ve směru* $\mathcal{S}$, tj. existuje $P_0 \in \mathcal{S}$ takové, že $f$ je definována na $P_0$. Řekneme, že
>
> $$
> \lim_{\mathcal{S}} f = L \qquad (L \in \mathbb{R}^*),
> $$
>
> když **pro každé $U \in \mathcal{N}(L)$ existuje $P \in \mathcal{S}$ tak, že $f[P] \subseteq U$**, kde $f[P] = \{f(x) \mid x \in P\}$.

^def-limita

> [!lidsky] Lidsky
> Hra se soupeřem. Soupeř nakreslí kolem $L$ terč $U$, jakkoli malý. Ty musíš najít kus směru $P$ (dost blízko cíli), jehož celý obraz padne do terče. Když umíš vyhrát proti každému terči, je limita $L$. Na obrázku: „pro každý“ je napravo (terče), „existuje“ nalevo (kus směru).

> [!obrazek] Dva terče: definice limity obrázkem
> ![[ma103-terce.png]]
> *Vpravo modrý čárkovaný terč U kolem L, soupeř ho volí jakkoli malý. Vlevo oranžový kus směru P kolem p bez bodu p, ten hledáš ty. Zelená skvrna f[P] (obraz P) musí ležet celá v terči. Dole menší terč, a proto i menší P. Kruhy jsou schéma, v ℝ jde o intervaly.*

> [!obrazek] Graf → brambory: jak číst obrázky k důkazům
> ![[ma103-prevod.png]]
> *Vlevo klasický graf, vpravo totéž jako „brambory“: levá brambora jsou vstupy x, pravá výstupy y a šipka je funkce f. Barvy si odpovídají: modrý vodorovný pás = modrý terč U kolem L, oranžový svislý pás = oranžový kus směru P kolem p (bez p, prázdné kolečko), zelená část grafu = zelený obraz f[P]. Červená f(p) na brambory nepatří, limitu neovlivní. Stejné schéma mají všechny obrázky k důkazům v MA1.*

*Vlastní limita:* $L \in \mathbb{R}$. *[[nevlastní limita|Nevlastní limita]]:* $L \in \{-\infty, +\infty\}$.

> [!pozor] Vlastní a nevlastní je výsledek, ne směr
> Rozlišuje se podle **výsledku** $L$, ne podle směru. $\lim_{x \to +\infty} \frac{1}{x} = 0$ je vlastní limita, i když se jde do nekonečna.

Příklad: $a_n = \dfrac{1}{(n^2 + 15)(n - 15)(n - 1112)}$. Posloupnost není definovaná pro $n = 15$ a $n = 1112$, ale ve směru $n \to +\infty$ definovaná je: stačí $P_0 = \{n \in \mathbb{N} \mid n > 1112\}$. Pointa: **na prvních členech nezáleží**, limita se dívá jen na „ocas“. Jmenovatel roste nade všechny meze, takže $\lim_{n \to +\infty} a_n = 0$.

> [!navic] „Telefonní seznam“ · handout 2A, slajdy 25–31
> Obecná definice přeložená do nerovností pro konkrétní směr a cíl, např.:
>
> - $\lim_{n \to +\infty} a_n = L \in \mathbb{R}$: pro všechna $\varepsilon > 0$ existuje $n_0$ tak, že pro všechna $n \ge n_0$ je $|a_n - L| < \varepsilon$.
> - $\lim_{x \to p} f(x) = L \in \mathbb{R}$: pro všechna $\varepsilon > 0$ existuje $\delta > 0$ tak, že z $0 < |x - p| < \delta$ plyne $|f(x) - L| < \varepsilon$.
> - $\lim_{x \to +\infty} f(x) = +\infty$: pro všechna $\varepsilon > 0$ existuje $\delta > 0$ tak, že z $x > \delta$ plyne $f(x) > \varepsilon$.
>
> Nazpaměť to učit nemusíš: dosadíš $U_\varepsilon(L)$ a $P$ do jedné definice a vyjde to samo.

## §7 Jednoznačnost limity

> [!veta] Věta · handout 2A, slajd 20
> ==Jestliže $\lim_{\mathcal{S}} f = L_1$ a $\lim_{\mathcal{S}} f = L_2$,== potom **$L_1 = L_2$**.
>
> > [!note]- Důkaz sporem
> > Ať $L_1 \neq L_2$. Zvolíme disjunktní okolí $U_1 \in \mathcal{N}(L_1)$ a $U_2 \in \mathcal{N}(L_2)$ (pro $L_1, L_2 \in \mathbb{R}$ stačí poloměr $\varepsilon = \frac{|L_1 - L_2|}{2}$). Podle definice existují $P_1, P_2 \in \mathcal{S}$ s $f[P_1] \subseteq U_1$ a $f[P_2] \subseteq U_2$. Směr je vnořený, takže např. $P_2 \subseteq P_1$. Pak $f[P_2] \subseteq U_1 \cap U_2 = \emptyset$, ale $P_2 \neq \emptyset$ ↯

^veta-jednoznacnost

> [!lidsky] Lidsky
> Hodnoty $f$ nemůžou zároveň „sedět“ ve dvou oddělených terčích. Kdyby limity byly dvě, stačí nakreslit terče tak malé, aby se nepřekrývaly, a hodnoty dost blízko cíli by musely být v obou najednou.

> [!obrazek] Proč limita nemůže být dvě
> ![[ma103-jednoznacnost.png]]
> *Vlevo graf: modré pásy U₁ kolem L₁ a U₂ kolem L₂ se nepřekrývají, oranžové pásy P₁ ⊇ P₂ jsou kusy směru. Pro bod x z menšího P₂ by hodnota f(x) musela ležet na obou červených úsečkách najednou, a to nejde (↯). Vpravo brambory: P₂ leží uvnitř P₁, šipka f by ho musela poslat do obou terčů, ale U₁ ∩ U₂ = ∅.*

## §8 Příklady

### $\lim_{n \to +\infty} \frac{7}{n - 6} = 0$ z definice

$f[P] = \{\frac{7}{n - 6} \mid n \ge n_0\}$. Máme $\varepsilon > 0$ a hledáme $n_0$ tak, aby $\left|\frac{7}{n - 6}\right| < \varepsilon$ pro všechna $n \ge n_0$. Pro $n > 6$ je zlomek kladný, takže

$$
\left|\frac{7}{n - 6}\right| < \varepsilon \iff \frac{7}{\varepsilon} < n - 6 \iff n > \frac{7}{\varepsilon} + 6.
$$

Stačí tedy vzít za $n_0$ libovolné přirozené číslo větší než $\frac{7}{\varepsilon} + 6$ (a větší než 6).

> [!example] Konkrétně pro ε = 0,5
> $\frac{7}{0{,}5} + 6 = 20$, takže $n_0 = 21$. Kontrola: $a_{21} = \frac{7}{15} \approx 0{,}467 < 0{,}5$ ✓, kdežto $a_{20} = \frac{7}{14} = 0{,}5$ už podmínku $< 0{,}5$ nesplní. Pro $\varepsilon = 0{,}01$ vyjde $n_0 = 707$.

> [!navic] Proč se smí vynechat absolutní hodnota a násobit
> Úprava $\frac{7}{n - 6} < \varepsilon \Rightarrow \frac{7}{\varepsilon} < n - 6$ je násobení kladnými čísly $\frac{n - 6}{\varepsilon}$, a to platí jen pro $n > 6$. U písemky to stačí napsat jednou větou.

> [!obrazek] 7/(n − 6) → 0 obrázkem
> ![[ma103-limita.png]]
> *Vlevo graf: modrý pás je terč U = (−0,5; 0,5), oranžově kus směru P = {n ≥ 21}. Členy nad P (zelené) leží všechny v terči, dřívější (šedé) ne. Vpravo brambory: P se zobrazí do zeleného f[P] uvnitř terče U kolem 0. Šedé členy a₈, a₉ leží mimo terč, ale nepatří do P, takže nevadí.*

### $\lim_{n \to +\infty} (-1)^n$ neexistuje

Důkaz sporem: ať $\lim (-1)^n = L \in \mathbb{R}^*$. Každý kus směru $\{n > n_0\}$ obsahuje sudá i lichá $n$, tedy obraz obsahuje $1$ i $-1$.

- $L = +\infty$: okolí $(\frac12; +\infty]$ neobsahuje $-1$ ↯
- $L = -\infty$: okolí $[-\infty; -\frac12)$ neobsahuje $1$ ↯
- $L \in \mathbb{R}$: okolí $(L - \frac12; L + \frac12)$ má délku $1$, a tak neobsahuje zároveň $1$ i $-1$ (jsou od sebe $2$) ↯

> [!obrazek] (−1)ⁿ obrázkem: ocas se rozdělí na dvě hodnoty
> ![[ma103-neexistuje.png]]
> *Vlevo graf: oranžový kus směru P = {n > 4}, modrý pás je terč délky 1 kolem L. Zelené členy 1 v něm leží, červené členy −1 ne. Vpravo brambory: sudá n z P jdou na 1, lichá na −1. Terč délky 1 obě hodnoty nepokryje, ať je L kdekoli (↯).*

### Monotónní posloupnost

> [!veta] Věta · handout 2A, slajd 22
> ==Je-li $(a_n)_{n \ge n_0}$ neklesající (tj. $a_n \le a_{n+1}$ pro všechna $n$),== pak
>
> $$
> \lim_{n \to +\infty} a_n = \sup\{a_n \mid n \ge n_0\} \quad (\text{v } \mathbb{R}^*).
> $$
>
> Pro nerostoucí posloupnost analogicky s infimem.

^veta-monotonni

> [!lidsky] Lidsky
> [[neklesající posloupnost|Neklesající posloupnost]] leze nahoru ke svému stropu. Když je strop $s$ konečný, podle [[MA1 02 – Celá, racionální a reálná čísla#^veta-eps-sup|ε-charakterizace suprema]] leží nějaký člen nad $s - \varepsilon$ a všechny další jsou ještě výš, ale pořád $\le s$. Tedy od toho členu dál jsou všechny v okolí $s$. Když strop neexistuje, $\sup = +\infty$ a limita je $+\infty$. Příklady: $1 - \frac{1}{n} \to 1$, $a_n = n \to +\infty$.

> [!obrazek] Neklesající posloupnost se „přilepí“ ke svému supremu
> ![[ma103-monotonni.png]]
> *Vlevo graf: členy aₙ = 2 − 1,6/n rostou k s = 2. Modrý pás (s − ε; s] pro ε = 0,15: od n₀ = 11 (zelené body nad oranžovým kusem směru P = {n ≥ 11}) leží v pásu všechny členy, dřívější (šedé) ne. Vpravo brambory: ocas P se zobrazí do levé půlky terče U, tedy pod s, protože nad supremem žádný člen neleží.*

> [!example] Jednostranné limity · handout 2A, slajd 23
> Pro $f(x) = -1$ ($x < 0$), $f(0) = 0$, $f(x) = 1$ ($x > 0$) je $\lim_{x \to 0^-} f(x) = -1$, $\lim_{x \to 0^+} f(x) = 1$ a $\lim_{x \to 0} f(x)$ **neexistuje**. Hodnota $f(0) = 0$ na nic z toho nemá vliv.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jaké řezy odpovídají $-\infty$ a $+\infty$ a proč to nejsou reálná čísla?
> $-\infty = (\emptyset, \mathbb{Q})$, $+\infty = (\mathbb{Q}, \emptyset)$. Porušují podmínku neprázdnosti obou částí řezu.

> [!karta|02]- Které výrazy v $\mathbb{R}^*$ nejsou definované?
> $+\infty - \infty$, $0 \cdot (\pm\infty)$, $\frac{\pm\infty}{\pm\infty}$ a $\frac{1}{0}$. Naopak $\frac{1}{\pm\infty} = 0$.

> [!karta|03]- Kolik je $\sup \emptyset$ a $\inf \emptyset$ v $\mathbb{R}^*$?
> $\sup \emptyset = -\infty$, $\inf \emptyset = +\infty$. Každý prvek $\mathbb{R}^*$ je horním i dolním odhadem $\emptyset$.

> [!karta|04]- Proč velké $\varepsilon$ dává u $U_\varepsilon(+\infty)$ malé okolí?
> $U_\varepsilon(+\infty) = (\varepsilon; +\infty]$ jsou čísla větší než $\varepsilon$. Čím větší $\varepsilon$, tím méně čísel.

> [!karta|05]- Proč má směr prázdný průnik, zatímco okolí bodu $L$ mají průnik $\{L\}$?
> Směr popisuje přibližování k cíli, který sám nebereme: bod $p$ ani $+\infty$ v žádném $P$ neleží. Hodnota v cíli limitu neovlivňuje.

> [!karta|06]- Zapiš kusy směru pro $x \to p^+$ a pro $n \to +\infty$.
> $P^+_\delta(p) = (p; p + \delta)$ pro $\delta > 0$. $P_n(+\infty) = \{k \in \mathbb{N} \mid k > n\}$ pro $n \in \mathbb{N}$.

> [!karta|07]- Co znamená, že $f$ je definována ve směru $\mathcal{S}$? Příklad.
> Existuje $P_0 \in \mathcal{S}$, na kterém je $f$ definována. Např. $\frac{1}{(n - 15)(n - 1112)}$ ve směru $n \to +\infty$: $P_0 = \{n > 1112\}$.

> [!karta|11]- Myšlenka důkazu, že limita je nejvýš jedna?
> Pro $L_1 \neq L_2$ vezmi disjunktní okolí $U_1, U_2$ a k nim $P_1, P_2$. Směr je vnořený, menší z nich (třeba $P_2$) se zobrazí do $U_1 \cap U_2 = \emptyset$, ale $P_2 \neq \emptyset$ ↯

> [!karta|14]- Přepiš $\lim_{x \to p} f(x) = L \in \mathbb{R}$ pomocí $\varepsilon$ a $\delta$.
> Pro všechna $\varepsilon > 0$ existuje $\delta > 0$ tak, že z $0 < |x - p| < \delta$ plyne $|f(x) - L| < \varepsilon$.

> [!karta|15]- Přepiš $\lim_{x \to +\infty} f(x) = +\infty$ pomocí $\varepsilon$ a $\delta$.
> Pro všechna $\varepsilon > 0$ existuje $\delta > 0$ tak, že z $x > \delta$ plyne $f(x) > \varepsilon$.

### Příklady na procvičení

> [!priklad|08]- Dokaž z definice $\lim_{n \to +\infty} \frac{7}{n - 6} = 0$.
> Pro $\varepsilon > 0$ a $n > 6$: $\frac{7}{n - 6} < \varepsilon \iff n > \frac{7}{\varepsilon} + 6$. Stačí $n_0 > \frac{7}{\varepsilon} + 6$; pak $f[P] \subseteq (-\varepsilon; \varepsilon)$ pro $P = \{n \ge n_0\}$.

> [!priklad|09]- Jaké $n_0$ stačí u $\lim \frac{7}{n - 6} = 0$ pro $\varepsilon = 0{,}5$?
> $n > \frac{7}{0{,}5} + 6 = 20$, tedy $n_0 = 21$ ($a_{21} = \frac{7}{15} \approx 0{,}467$).

> [!priklad|10]- Proč $\lim_{n \to +\infty} (-1)^n$ neexistuje?
> Každý ocas obsahuje $1$ i $-1$. Okolí $(\frac12; +\infty]$ neobsahuje $-1$, $[-\infty; -\frac12)$ neobsahuje $1$ a $(L - \frac12; L + \frac12)$ má délku 1, takže nepokryje obě ↯

> [!priklad|13]- Existuje $\lim_{x \to 0} \operatorname{sgn} x$?
> **Ne.** Zleva je limita $-1$, zprava $1$. Hodnota $\operatorname{sgn} 0 = 0$ na tom nic nemění.

---
← [[MA1 02 – Celá, racionální a reálná čísla|24. 9. 2026 Celá, racionální a reálná čísla]] · [[MA1 04 – Nerovnosti ve směru a věta o sevření|1. 10. 2026 Nerovnosti ve směru a věta o sevření]] →

---
predmet: MA1
prednaska: 5
datum: 2026-10-07
zdroj: "Handout 2B (Počítání limit), slajdy 14–25; handout 3A, slajd 3"
tags: [prednaska, MA1]
---

# MA1 05 – Aritmetika limit a substituce

*Přednáška 5 · středa 7. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 2B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout02b.pdf) · [Handout 3A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout03a.pdf)

Témata: `aritmetika limit` · `∞/∞ není definováno` · `lineární podprostor W` · `věta o substituci` · `f(z) = 200 v bodě 1` · `vybraná podposloupnost` · `posloupnost přes funkci` · `detekce limity` · `sudé a liché členy` · `(−1)ⁿ` · `spojitost v bodě`

Minule jsme limity počítali přes nerovnosti a sevření. Dnes přibyly dva hlavní nástroje: [[věta o aritmetice limit|aritmetika limit]] (limita součtu je součet limit, pokud výsledek v $\mathbb{R}^*$ dává smysl) a [[věta o substituci|substituce]] (limita složené funkce). Ze substituce pak plyne práce s [[podposloupnost|podposloupnostmi]], převod posloupnosti na funkci a rozdělení posloupnosti na sudé a liché členy. Na konci přišla definice [[spojitost v bodě|spojitosti]].

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| aritmetika limit | $\lim_{\mathcal{S}} f = L$, $\lim_{\mathcal{S}} g = M$, $L \star M$ definováno | $\lim_{\mathcal{S}} (f \star g) = L \star M$ |
| linearita | $L, M \in \mathbb{R}$ | $\lim_{\mathcal{S}} (rf + sg) = rL + sM$, funkce s vlastní limitou tvoří podprostor |
| substituce | $\lim_{\mathcal{T}} f = L$ a $\forall T \in \mathcal{T}\ \exists P \in \mathcal{S}: \varphi[P] \subseteq T$ | $\lim_{\mathcal{S}} (f \circ \varphi) = L$ |
| podposloupnost | $\lim_{n \to +\infty} a_n = L$, $n_k$ rostoucí | $\lim_{k \to +\infty} a_{n_k} = L$ |
| funkce → posloupnost | $\lim_{x \to +\infty} f(x) = L$ | $\lim_{n \to +\infty} f(n) = L$ (opak neplatí) |
| detekce limity | $\lim (f \circ \varphi_i) = L$ pro všechna $i$, obrazy kusů pokryjí kus $\mathcal{T}$ | $\lim_{\mathcal{T}} f = L$ |
| posun | $N$ pevné | $\lim_n a_n = L \iff \lim_k a_{k+N} = L$ |
| sudé a liché | | $\lim_n a_n = L \iff \lim_k a_{2k} = L = \lim_k a_{2k+1}$ |
| spojitost v $p$ | | $\lim_{x \to p} f(x) = f(p)$ |

## §1 Věta o aritmetice limit

> [!veta] Věta o aritmetice limit · handout 2B, slajd 16
> ==Ať $\lim_{\mathcal{S}} f = L$ a $\lim_{\mathcal{S}} g = M$, kde $L, M \in \mathbb{R}^*$, a ať $\star$ je jedna z operací $+$, $-$, $\cdot$, $/$.== Je-li **výraz $L \star M$ v $\mathbb{R}^*$ definovaný**, potom **$\lim_{\mathcal{S}} (f \star g)$ existuje a**
>
> $$
> \lim_{\mathcal{S}} (f \star g) = \Big(\lim_{\mathcal{S}} f\Big) \star \Big(\lim_{\mathcal{S}} g\Big) = L \star M.
> $$

^veta-aritmetika

> [!lidsky] Lidsky
> Limitu složitého výrazu smíš rozebrat na limity kousků a výsledky spojit stejnou operací, **pokud ta operace s výsledky dává smysl**. Kdy dává smysl, říkají pravidla [[rozšířená reálná čísla|počítání v ℝ*]] z přednášky 3. U dělení je navíc schované, že $M \neq 0$; podle [[MA1 04 – Nerovnosti ve směru a věta o sevření#^veta-znamenko|věty o znaménku]] pak $g \neq 0$ na nějakém kusu směru, takže $\frac{f}{g}$ je tam definovaná.

Připomenutí, co v $\mathbb{R}^*$ je a co není definované ($r \in \mathbb{R}$):

| definováno | výsledek | **nedefinováno** |
|---|---|---|
| $(+\infty) + r$, $(+\infty) + (+\infty)$ | $+\infty$ | $(+\infty) + (-\infty)$, tedy i $(+\infty) - (+\infty)$ |
| $r \cdot (+\infty)$ pro $r > 0$, $(+\infty)(+\infty)$ | $+\infty$ | $0 \cdot (\pm\infty)$ |
| $(+\infty)(-\infty)$, $r \cdot (+\infty)$ pro $r < 0$ | $-\infty$ | $\frac{\pm\infty}{\pm\infty}$ (všechny čtyři kombinace) |
| $\frac{r}{\pm\infty}$ | $0$ | $\frac{L}{0}$ pro jakékoli $L$, i $\frac{1}{0}$ a $\frac{0}{0}$ |

> [!navic] Rychlý test, jestli je výraz definovaný
> Říká-li ti intuice jednoznačně, co má vyjít ($+\infty + 3$ je pořád nekonečno, $2 \cdot (+\infty)$ taky), výraz definovaný je. Objeví-li se něco podivného, tedy nekonečno minus nekonečno, nekonečno krát nula, nekonečno lomeno nekonečnem nebo cokoli lomeno nulou, zpomal: věta o aritmetice tu nic neříká a výraz je potřeba upravit.

> [!example] (1) $\lim_{x \to +\infty} (2x + 3)$
> $\lim x = +\infty$, tedy $\lim 2x = 2 \cdot (+\infty) = +\infty$ a
>
> $$
> \lim_{x \to +\infty} (2x + 3) = (+\infty) + 3 = +\infty.
> $$

> [!example] (2) $\lim_{x \to +\infty} \frac{x}{x}$
> Čitatel i jmenovatel mají limitu $+\infty$, ale $\frac{+\infty}{+\infty}$ není definováno, takže věta o aritmetice **nic neříká**. Psát $\lim \frac{x}{x} = \frac{+\infty}{+\infty}$ je chyba.
>
> Správně: pro $x \neq 0$ je $\frac{x}{x} = 1$, tedy $\frac{x}{x} =_{x \to +\infty} 1$ a podle [[MA1 04 – Nerovnosti ve směru a věta o sevření#^veta-rovnost|věty o rovnosti ve směru]]
>
> $$
> \lim_{x \to +\infty} \frac{x}{x} = \lim_{x \to +\infty} 1 = 1.
> $$

> [!example] (3) $\lim_{x \to +\infty} \frac{3x}{x}$
> Zase typ $\frac{+\infty}{+\infty}$, ale $\frac{3x}{x} = 3$ pro $x \neq 0$, takže $\lim_{x \to +\infty} \frac{3x}{x} = \lim 3 = 3$.

> [!pozor] Nedefinovaný výraz neznamená, že limita neexistuje
> Příklady (2) a (3) mají stejný typ $\frac{+\infty}{+\infty}$ a limity $1$ a $3$. Proto se $\frac{\infty}{\infty}$ nedá „dodefinovat“ žádným číslem: výsledek závisí na tom, *jak rychle* čitatel a jmenovatel rostou. Nedefinovaný výraz jen říká, že věta o aritmetice nepomůže a musíš výraz nejdřív upravit (krátit, vytknout).

> [!obrazek] Typ ∞/∞ může dát cokoli
> ![[ma105-nekonecno.png]]
> *Čtyři podíly, u kterých čitatel i jmenovatel jdou k +∞. Modrá x/x je stále 1, zelená 3x/x stále 3, oranžová x²/x = x roste do nekonečna a červená čárkovaná x/x² = 1/x klesá k nule.*

### Tabulka limit polynomů a racionálních funkcí · handout 2B, slajdy 23–25

Z aritmetiky limit plyne „telefonní seznam“ limit, který se vyplatí znát zpaměti, protože se na cvičeních a v testech počítá pořád. Ať $f(x) = a_n x^n + \dots + a_1 x + a_0$ s $a_n \neq 0$, $n \ge 1$, a $g(x) = b_m x^m + \dots + b_0$ s $b_m \neq 0$.

| limita | výsledek |
|---|---|
| polynom, $x \to p \in \mathbb{R}$ (i zleva, zprava) | $f(p)$, stačí dosadit |
| polynom, $x \to +\infty$ | $+\infty$ pro $a_n > 0$, $-\infty$ pro $a_n < 0$ |
| polynom, $x \to -\infty$ | jako u $+\infty$ pro sudé $n$, s opačným znaménkem pro liché $n$ |
| $\frac{f}{g}$, $x \to p \in \mathbb{R}$, $g(p) \neq 0$ | $\frac{f(p)}{g(p)}$ |
| $\frac{f}{g}$, $x \to \pm\infty$, $n = m$ | $\frac{a_n}{b_m}$ |
| $\frac{f}{g}$, $x \to \pm\infty$, $n < m$ | $0$ |
| $\frac{f}{g}$, $x \to +\infty$, $n > m$ | $\frac{a_n}{b_m} \cdot (+\infty)$ |
| $\frac{f}{g}$, $x \to -\infty$, $n > m$ | $\frac{a_n}{b_m} \cdot (-1)^{n-m} \cdot (+\infty)$ |

^tabulka-polynomy

> [!lidsky] Lidsky
> Daleko od nuly rozhoduje jen **nejvyšší mocnina**, ostatní členy jsou proti ní zanedbatelné. Proč: vytkneš ji, $f(x) = x^n\big(a_n + \frac{a_{n-1}}{x} + \dots + \frac{a_0}{x^n}\big)$, a závorka jde k $a_n$. U zlomku se pak porovnají nejvyšší mocniny čitatele a jmenovatele: vyhraje vyšší stupeň, při stejném stupni zbude podíl vedoucích koeficientů.

> [!example] Dvě limity z tabulky
> $\lim_{x \to +\infty} \frac{2x^2 - x}{5x^2 + 3} = \frac{2}{5}$ (stejné stupně). $\lim_{x \to -\infty} \frac{x^3}{x + 1} = 1 \cdot (-1)^{3-1} \cdot (+\infty) = +\infty$; kontrola: pro $x = -1000$ je $\frac{-10^9}{-999} \approx 10^6 > 0$.

> [!pozor] Kořen jmenovatele tabulka neřeší
> Je-li $g(p) = 0$, tabulka nic neříká. Pak je potřeba krátit (jako $\frac{x^2 - 9}{x - 3}$ v [[MA1 04 – Nerovnosti ve směru a věta o sevření#^veta-rovnost|přednášce 4]]) nebo počítat jednostranné limity zvlášť.

## §2 Linearita a podprostor funkcí s vlastní limitou

> [!veta] Důsledek (linearita) · handout 2B, slajd 17
> ==Mají-li $f_1, \dots, f_n$ ve směru $\mathcal{S}$ **vlastní** limity a $r_1, \dots, r_n \in \mathbb{R}$,== potom
>
> $$
> \lim_{\mathcal{S}} \sum_{i=1}^{n} r_i f_i = \sum_{i=1}^{n} r_i \lim_{\mathcal{S}} f_i.
> $$
>
> Pro $D \in \mathcal{S}$ je $\mathrm{Func}(D; \mathbb{R})$, všechny funkce $D \to \mathbb{R}$, [[lineární prostor]] nad $\mathbb{R}$ (je to [[prostor funkcí]] z LAG). Množina
>
> $$
> W = \{f \in \mathrm{Func}(D; \mathbb{R}) \mid \lim_{\mathcal{S}} f \in \mathbb{R}\}
> $$
>
> je jeho **[[lineární podprostor]]** a $\lim_{\mathcal{S}} : W \to \mathbb{R}$, $f \mapsto \lim_{\mathcal{S}} f$, zachovává lineární kombinace.

^dusledek-linearita

> [!lidsky] Lidsky
> Proč podprostor: nulová funkce má limitu $0$, součet dvou funkcí s vlastní limitou má limitu $L + M \in \mathbb{R}$ a $r$-násobek limitu $rL \in \mathbb{R}$. Z $W$ se sčítáním ani násobením nedá utéct. Slovo **vlastní** je podstatné: $f = x$ a $g = -x$ mají pro $x \to +\infty$ limity $\pm\infty$, a $\lim (f + g) = 0$ by se z nich spočítat nedalo, protože $(+\infty) + (-\infty)$ není definováno.

> [!obrazek] Limita jako lineární zobrazení
> ![[ma105-podprostor.png]]
> *Šedá brambora jsou všechny funkce na D, modrý rovnoběžník W ty s vlastní limitou. Červená funkce limitu nemá nebo je nevlastní, leží mimo W. Modrá šipka lim𝒮 posílá každou funkci z W na číslo; zelená kombinace rf + sg jde na stejnou kombinaci čísel.*

## §3 Věta o substituci v limitě

Chceme počítat limitu složené funkce $f \circ \varphi$, tedy $f(\varphi(x))$: nejdřív vnitřní funkce $\varphi$ (substituce), pak vnější $f$. Jsou tu dva směry: $\mathcal{S}$ pro proměnnou $x$ a $\mathcal{T}$ pro „vnitřní“ proměnnou $z = \varphi(x)$.

> [!veta] Věta o substituci v limitě · handout 2B, slajd 19
> ==Ať==
>
> 1. ==$\lim_{\mathcal{T}} f = L$,==
> 2. ==pro každé $T \in \mathcal{T}$ existuje $P \in \mathcal{S}$ tak, že $\varphi[P] \subseteq T$.==
>
> Potom **$\lim_{\mathcal{S}} (f \circ \varphi) = L$**.
>
> > [!note]- Důkaz
> > Ať $U \in \mathcal{N}(L)$. Podle (1) existuje $T \in \mathcal{T}$ s $f[T] \subseteq U$. Podle (2) k tomuto $T$ existuje $P \in \mathcal{S}$ s $\varphi[P] \subseteq T$. Potom
> >
> > $$
> > (f \circ \varphi)[P] = f\big[\varphi[P]\big] \subseteq f[T] \subseteq U.
> > $$

^veta-substituce

> [!lidsky] Lidsky
> Podmínka (2) říká: **„$\varphi$ míří do cíle a nikdy do něj nedopadne.“** Ke každému kusu směru $\mathcal{T}$, ať je jakkoli malý, umí $\varphi$ dostat celý kus směru $\mathcal{S}$ dovnitř. Kusy směru cíl samotný neobsahují ([[prstencové okolí]]), takže se $\varphi$ cílovému bodu musí na nějakém kusu $P$ úplně vyhnout ($\varphi[P] \subseteq T$). Jinak by se do hry dostala hodnota $f$ *v* cíli, a ta s limitou nemá nic společného.

> [!obrazek] Důkaz obrázkem: řetěz U → T → P
> ![[ma105-substituce.png]]
> *Vlevo kus P směru 𝒮, uprostřed kus T směru 𝒯 (prázdné kolečko je cíl, do T nepatří), vpravo modrý terč U kolem L. Hledá se pozpátku: soupeř zvolí U, limita f dá T, podmínka (2) dá P. Šipka φ pošle P dovnitř T a šipka f pošle T do zeleného f[T] ⊆ U.*

### Proč je podmínka (2) nutná

> [!example] Protipříklad · handout 2B, slajd 18
> $$
> f(z) = \begin{cases} 200, & z = 1, \\ 3, & z \neq 1, \end{cases} \qquad \varphi(x) = 1 \text{ pro všechna } x \in \mathbb{R}.
> $$
>
> - $\lim_{z \to 1} f(z) = 3$, protože hodnota v bodě $1$ limitu neovlivní.
> - $\lim_{x \to 5} \varphi(x) = 1$, konstanta má limitu svou hodnotu.
> - Ale $f(\varphi(x)) = f(1) = 200$ pro všechna $x$, tedy $\lim_{x \to 5} f(\varphi(x)) = 200 \neq 3$.
>
> Selhala podmínka (2): každé $T \in \mathcal{T}$ (směr $z \to 1$) je prstencové okolí a bod $1$ neobsahuje, zatímco $\varphi[P] = \{1\}$ pro každé $P$. Žádné $\varphi[P]$ se do $T$ nevejde.

^protipriklad-substituce

> [!obrazek] Protipříklad obrázkem
> ![[ma105-protipriklad.png]]
> *Vlevo graf f: modrá vodorovná čára ve výšce 3 s dírou v bodě 1, červený bod f(1) = 200 (svislá osa je zkrácená). Vpravo brambory: celé P kolem 5 se zobrazí do jediného bodu 1, který je přesně díra v T. Odtud f pošle všechno na červenou hodnotu 200, mimo modrý terč kolem 3.*

> [!pozor] Častá chyba: „vnitřní limita jde k 1, tak dosadím limitu vnější funkce“
> Z $\lim \varphi = 1$ a $\lim_{z \to 1} f = 3$ samo nic neplyne. Musíš ověřit podmínku (2), typicky tak, že $\varphi(x) \neq 1$ na nějakém kusu směru $\mathcal{S}$. Nebo musí být $f$ v bodě $1$ [[spojitost v bodě|spojitá]] (viz §6).

> [!example] Př. (1): $\lim_{k \to +\infty} \big(2(k^2 + 6) + 1\big)$ · handout 2B, slajd 18
> Vnější funkce $f(n) = 2n + 1$, vnitřní $\varphi(k) = k^2 + 6 = n$. Víme $\lim_{n \to +\infty} (2n + 1) = +\infty$ a $\lim_{k \to +\infty} (k^2 + 6) = +\infty$. Podmínka (2): ke kusu $\{n \ge N\}$ stačí $P = \{k \ge N\}$, protože $k^2 + 6 > k$. Odtud
>
> $$
> \lim_{k \to +\infty} \big(2(k^2 + 6) + 1\big) = +\infty.
> $$

## §4 Důsledky věty o substituci

> [!veta] Důsledek 1: limita vybrané podposloupnosti · handout 2B, slajd 20
> ==Ať $\lim_{n \to +\infty} a_n = L$ a $n_k$, $k \ge k_0$, je **rostoucí** posloupnost přirozených čísel.== Potom **$\lim_{k \to +\infty} a_{n_k} = L$**.
>
> > [!note]- Důkaz
> > Je to věta o substituci pro $f(n) = a_n$, $\varphi(k) = n_k$, $\mathcal{S}$: $k \to +\infty$, $\mathcal{T}$: $n \to +\infty$. Rostoucí posloupnost přirozených čísel roste aspoň o $1$ za krok, tedy $n_k \ge k - k_0$. Ke kusu $T = \{n \ge N\}$ stačí $P = \{k \ge N + k_0\}$, pak $\varphi[P] \subseteq T$.

^dusledek-podposloupnost

> [!lidsky] Lidsky
> [[podposloupnost|Vybraná podposloupnost]] vznikne tak, že z posloupnosti vyškrtáš některé členy, ale nekonečně mnoho jich necháš a pořadí nezměníš. Když celá posloupnost míří k $L$, míří tam i každý výběr. Např. $f(n) = 2n + 1$ a $\varphi(k) = k^2 + 6$: z čísel $a_n = 1, 3, 5, \dots$ vybereme $a_6 = 13$, $a_7 = 15$, $a_{10} = 21$, $a_{15} = 31$, … a to je přesně Př. (1) výše.

> [!veta] Důsledek 2: limitu posloupnosti lze nahradit limitou funkce · handout 2B, slajd 20
> ==Ať $f$ je definovaná ve směru $x \to +\infty$ a $\lim_{x \to +\infty} f(x) = L$.== Potom **$\lim_{n \to +\infty} f(n) = L$**.
>
> > [!note]- Důkaz
> > Substituce $\varphi(n) = n$ (přirozené číslo chápané jako reálné), $\mathcal{S}$: $n \to +\infty$, $\mathcal{T}$: $x \to +\infty$. Ke kusu $T = (\delta; +\infty)$ stačí $P = \{n > \delta\}$.

^dusledek-funkce

> [!lidsky] Lidsky
> Posloupnost je funkce, ze které vidíš jen hodnoty v celých číslech. Když se celá funkce blíží k $L$, blíží se k $L$ i tyhle vybrané hodnoty. Limitu posloupnosti tak smíš spočítat jako limitu funkce a použít na ni všechny nástroje pro funkce.

> [!example] $\lim_{n \to +\infty} (n^3 + 1)$
> Podle aritmetiky $\lim_{x \to +\infty} (x^3 + 1) = (+\infty)(+\infty)(+\infty) + 1 = +\infty$, a proto i $\lim_{n \to +\infty} (n^3 + 1) = +\infty$. U posloupností tak smíš používat všechno, co umíš o funkcích (později třeba derivace).

> [!pozor] Opačně to neplatí
> Z $\lim_{n \to +\infty} f(n) = L$ **neplyne** $\lim_{x \to +\infty} f(x) = L$. Pro $f(x) = \sin(\pi x)$ je $f(n) = 0$ pro všechna $n$, takže limita posloupnosti je $0$, ale $\lim_{x \to +\infty} \sin(\pi x)$ neexistuje: funkce mezi celými čísly pořád kmitá mezi $-1$ a $1$.

> [!obrazek] Posloupnost má limitu, funkce ne
> ![[ma105-sin-pi.png]]
> *Modře graf $\sin(\pi x)$, který pořád kmitá mezi $-1$ a $1$. Červeně hodnoty v přirozených číslech: všechny jsou $0$, takže posloupnost $f(n)$ má limitu $0$, funkce limitu nemá.*

> [!pozor] Posloupnost se nederivuje
> Častá chyba ze střední školy: použít l'Hospitalovo pravidlo (derivovat čitatele a jmenovatele) přímo na posloupnost, třeba $\frac{n^2 + 1}{n}$. Posloupnost je definovaná jen v přirozených číslech, derivaci nemá. Správně: přejdi k funkci $f(x) = \frac{x^2 + 1}{x}$, spočítej $\lim_{x \to +\infty} f(x)$ jakýmkoli nástrojem pro funkce a výsledek přenes na posloupnost podle důsledku 2.

## §5 Detekce limity pomocí substitucí

Věta o substituci jde jedním směrem: z limity $f$ dostaneme limitu $f \circ \varphi$. Obráceně to jde, když substitucí vezmeme **dost** na to, aby dohromady pokryly celý kus směru.

> [!veta] Věta: limitu lze detekovat dostatečně mnoha „dobrými“ substitucemi · handout 2B, slajd 21
> ==Ať $f$ je definovaná ve směru $\mathcal{T}$ a $L \in \mathbb{R}^*$.== Následující podmínky jsou ekvivalentní:
>
> 1. **$\lim_{\mathcal{T}} f = L$.**
> 2. **Existuje neprázdná kolekce funkcí $\varphi_i$, $i \in I$, a směrů $\mathcal{S}_i$ tak, že**
>     - $\lim_{\mathcal{S}_i} (f \circ \varphi_i) = L$ pro všechna $i \in I$ a
>     - pro každou volbu $P_i \in \mathcal{S}_i$ ($i \in I$) existuje $P \in \mathcal{T}$ s $P \subseteq \bigcup_{i \in I} \varphi_i[P_i]$.
>
> > [!note]- Důkaz
> > (1) ⇒ (2): stačí jediná substituce $\varphi = \mathrm{id}$ a $\mathcal{S} = \mathcal{T}$; ke kusu $P_1$ vezmeme $P = P_1$.
> >
> > (2) ⇒ (1): ať $U \in \mathcal{N}(L)$. Pro každé $i$ existuje $P_i \in \mathcal{S}_i$ s $f\big[\varphi_i[P_i]\big] \subseteq U$. K této volbě existuje $P \in \mathcal{T}$, který je pokrytý obrazy $\varphi_i[P_i]$. Každé $x \in P$ leží v některém $\varphi_i[P_i]$, takže $f(x) \in U$. Tedy $f[P] \subseteq U$.

^veta-detekce

> [!lidsky] Lidsky
> Rozdělíš si cestu do cíle na několik „pruhů“ (třeba sudé a liché indexy). Když v každém pruhu vyjde limita $L$ a pruhy dohromady pokryjí celý konec cesty, je limita celé funkce $L$. Jeden pruh nestačí, pokud nepokrývá všechno: vybraná podposloupnost $k^2 + 6$ trefí jen některá $n$.

> [!obrazek] Které substituce pokryjí kus směru n → +∞
> ![[ma105-indexy.png]]
> *Šedé čtverečky jsou indexy k, kolečka indexy n. Barevná kolečka jsou ta, kam substituce dopadne, šedá zůstala netrefená. Nahoře k ↦ k² + 6 trefí jen 6, 7, 10, 15, 22, …, na detekci limity to nestačí. Uprostřed posun k ↦ k + 3 trefí všechna n ≥ 3. Dole sudé (modře) a liché (oranžově) indexy dohromady trefí úplně všechno.*

> [!veta] Důsledek 1: limita posunuté posloupnosti · handout 2B, slajd 22
> ==Pro pevné $N \in \mathbb{N}$:==
>
> $$
> \lim_{n \to +\infty} a_n = L \iff \lim_{k \to +\infty} a_{k+N} = L.
> $$
>
> ⇒ je substituce $\varphi(k) = k + N$, ⇐ je detekce s jedinou substitucí: obraz kusu $\{k \ge K\}$ je celý kus $\{n \ge K + N\}$.

^dusledek-posun

> [!example] Posun o 17
> $\lim_{n \to +\infty} (2n + 1) = +\infty \iff \lim_{k \to +\infty} \big(2(k + 17) + 1\big) = +\infty$. Prvních 17 členů limitu neovlivní: na začátku posloupnosti nezáleží.

> [!veta] Důsledek 2: sudé a liché členy · handout 2B, slajd 22
> $$
> \lim_{n \to +\infty} a_n = L \iff \lim_{k \to +\infty} a_{2k} = L \ \text{ a } \ \lim_{k \to +\infty} a_{2k+1} = L.
> $$
>
> ⇒ jsou dvě vybrané podposloupnosti, ⇐ je detekce se substitucemi $\varphi_1(k) = 2k$ a $\varphi_2(k) = 2k + 1$: obrazy kusů $\{k \ge K_1\}$ a $\{k \ge K_2\}$ pokryjí kus $\{n \ge 2\max(K_1, K_2)\}$.

^dusledek-suda-licha

> [!lidsky] Lidsky
> Sudé a liché indexy dohromady pokryjí všechny. Když se sudé členy i liché členy blíží ke stejnému $L$, nemá posloupnost kam utéct. Když každá skupina míří jinam (jako u $(-1)^n$), limita neexistuje.

> [!example] $\lim_{n \to +\infty} (2n + 1)$ přes sudé a liché členy
> $\lim_{k \to +\infty} \big(2(2k) + 1\big) = +\infty$ a $\lim_{k \to +\infty} \big(2(2k + 1) + 1\big) = +\infty$, tedy $\lim_{n \to +\infty} (2n + 1) = +\infty$.

### $(-1)^n$ podruhé, tentokrát přes podposloupnosti

> [!example] $\lim_{n \to +\infty} (-1)^n$ neexistuje
> $$
> \lim_{k \to +\infty} (-1)^{2k} = \lim_{k \to +\infty} 1 = 1, \qquad \lim_{k \to +\infty} (-1)^{2k+1} = \lim_{k \to +\infty} (-1) = -1.
> $$
>
> Kdyby $\lim (-1)^n = L$ existovala, musely by podle důsledku 1 z §4 mít obě podposloupnosti limitu $L$, takže $L = 1$ a zároveň $L = -1$ ↯. Je to kratší důkaz než sporem přes okolí z [[MA1 03 – Rozšířená reálná čísla a limita ve směru|přednášky 3]].

> [!obrazek] (−1)ⁿ rozdělená na sudé a liché členy
> ![[ma105-minus-jedna.png]]
> *Zeleně sudé členy, všechny rovné 1, oranžově liché, všechny −1. Každá z obou podposloupností má limitu, ale jinou, takže celá posloupnost limitu nemá.*

> [!pozor] Na obou polovinách musí vyjít totéž
> Návod „limita neexistuje“: najdi **dvě podposloupnosti s různými limitami** (nebo jednu bez limity). Naopak pro existenci nestačí jedna podposloupnost s limitou: $(-1)^{2k} \to 1$, a přesto $(-1)^n$ limitu nemá.

## §6 Spojitost v bodě

> [!definice] Spojitost v bodě · handout 3A, slajd 3
> Ať $f$ je definovaná na nějakém okolí bodu $p \in \mathbb{R}$. Funkce $f$ je **spojitá v bodě $p$**, když
>
> $$
> \lim_{x \to p} f(x) = f(p).
> $$

^def-spojitost

> [!lidsky] Lidsky
> Limita „předpovídá“, kam se graf blíží, a spojitost říká, že funkce v bodě $p$ opravdu stojí tam, kam se blíží. Graf jde přes $p$ bez zvednutí tužky. V jazyce terčů: ke každému terči kolem $f(p)$ existuje okolí $p$, jehož celý obraz padne do terče, a tentokrát smí být v okolí i samotné $p$.

> [!example] Příklad
> F(x) = x² je spojitá v 3: lim_{x→3} x² = 9 = f(3). Funkce sgn (−1 pro x < 0, 0 v nule, 1 pro x > 0) spojitá v 0 není: zleva jde k −1, zprava k 1, limita v 0 neexistuje.

> [!obrazek] Spojitá a nespojitá funkce v bodě p
> ![[ma105-spojitost.png]]
> *Vlevo spojitá: modrý bod f(p) leží přesně tam, kam graf míří; nad oranžovým okolím p leží zelená část grafu celá v modrém terči kolem f(p). Vpravo nespojitá: graf míří k L (prázdné kolečko), ale červená hodnota f(p) je jinde.*

> [!navic] Proč nestačí „graf bez přerušení“
> Školní představa je dobrý začátek, ale brzy přijdou „patologické“ funkce, u kterých obrázek nepomůže nebo klame, a rozhodne jen definice. Ta má schované dva předpoklady: $f(p)$ musí existovat (jinak není s čím limitu porovnat) a $f$ musí být definovaná kolem $p$ (jinak nemá smysl limita). A protože se porovnává s $f(p)$, smí v okolí ležet i bod $p$ sám, na rozdíl od prstencového okolí u limity.

> [!navic] Spojitost a substituce
> Funkce $f$ z protipříkladu v §3 je v bodě $1$ nespojitá ($\lim_{z \to 1} f = 3 \neq 200 = f(1)$), a právě proto substituce selhala. Když je vnější funkce v cílovém bodě spojitá, smí se dosadit vždy: $\lim \varphi = p$ a $f$ spojitá v $p$ ⇒ $\lim f(\varphi(x)) = f(p)$. Tomu se věnuje handout 3A. Spojité jsou například všechny polynomy: $\lim_{x \to p} f(x) = f(p)$ pro každé $p \in \mathbb{R}$ (handout 2B, slajd 23).

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- Které výrazy v $\mathbb{R}^*$ nejsou definované?
> $(+\infty) + (-\infty)$, $0 \cdot (\pm\infty)$, $\frac{\pm\infty}{\pm\infty}$ a $\frac{L}{0}$ pro jakékoli $L$ (i $\frac{1}{0}$).

> [!karta|03]- Co víš o $\lim (f \star g)$, když $L \star M$ není definováno?
> **Nic.** Věta o aritmetice nepomůže, limita může vyjít cokoli nebo neexistovat: $\frac{x}{x} \to 1$, $\frac{3x}{x} \to 3$, obojí typu $\frac{+\infty}{+\infty}$. Výraz je třeba upravit.

> [!karta|04]- Proč funkce s vlastní limitou ve směru $\mathcal{S}$ tvoří lineární podprostor $\mathrm{Func}(D; \mathbb{R})$?
> Nulová funkce má limitu $0$; podle aritmetiky $\lim (f + g) = L + M \in \mathbb{R}$ a $\lim rf = rL \in \mathbb{R}$. Navíc $\lim_{\mathcal{S}}$ zachovává **lineární kombinace**: $\lim \sum r_i f_i = \sum r_i \lim f_i$.

> [!karta|06]- Dokaž větu o substituci.
> K $U \in \mathcal{N}(L)$ najdi $T$ s $f[T] \subseteq U$ (z 1), k $T$ najdi $P$ s $\varphi[P] \subseteq T$ (z 2). Pak $(f \circ \varphi)[P] = f[\varphi[P]] \subseteq f[T] \subseteq U$.

> [!karta|07]- Proč ve větě o substituci nestačí, že $f$ i $\varphi$ mají limitu? Protipříklad.
> $f(z) = 200$ pro $z = 1$, jinak $3$; $\varphi \equiv 1$. $\lim_{z \to 1} f = 3$, $\lim_{x \to 5} \varphi = 1$, ale $f(\varphi(x)) = 200$. Kusy směru $z \to 1$ bod $1$ **neobsahují**, takže $\varphi[P] = \{1\}$ se do žádného nevejde.

> [!karta|09]- Jak souvisí $\lim_{x \to +\infty} f(x)$ a $\lim_{n \to +\infty} f(n)$?
> Je-li $\lim_{x \to +\infty} f(x) = L$, pak **$\lim_{n \to +\infty} f(n) = L$** (substituce $\varphi(n) = n$). Limitu posloupnosti tak smíš počítat jako limitu funkce.

> [!karta|10]- Plyne z $\lim_{n \to +\infty} f(n) = L$, že $\lim_{x \to +\infty} f(x) = L$? Protipříklad.
> **Ne.** $f(x) = \sin(\pi x)$: $f(n) = 0 \to 0$, ale $\lim_{x \to +\infty} \sin(\pi x)$ neexistuje.

> [!karta|12]- Dokaž: když všechny $f \circ \varphi_i$ mají limitu $L$ a obrazy $\varphi_i[P_i]$ dohromady vždy pokryjí kus směru, je $L$ limitou $f$.
> K $U$ vyber $P_i$ s $f[\varphi_i[P_i]] \subseteq U$ pro každé $i$. Podle pokrytí existuje $P \subseteq \bigcup \varphi_i[P_i]$; každé $x \in P$ leží v některém $\varphi_i[P_i]$, tedy $f[P] \subseteq U$.

> [!karta|13]- Jak souvisí $\lim a_n$ s limitou posunuté posloupnosti $a_{k+N}$?
> Pro pevné $N$: **$\lim_n a_n = L \iff \lim_k a_{k+N} = L$**. Na prvních $N$ členech nezáleží.

> [!karta|14]- Jak souvisí $\lim a_n$ s limitami sudých a lichých členů?
> **$\lim_n a_n = L \iff \lim_k a_{2k} = L = \lim_k a_{2k+1}$.** ⇐ je detekce: obrazy $k \mapsto 2k$ a $k \mapsto 2k + 1$ dohromady pokryjí všechna $n$.

> [!karta|15]- Jak pomocí podposloupností dokázat, že limita posloupnosti neexistuje?
> Najdi **dvě podposloupnosti s různými limitami** (nebo jednu bez limity). Kdyby $\lim a_n = L$ existovala, měly by obě limitu $L$.

> [!karta|25]- Jakou limitu má polynom $a_n x^n + \dots + a_0$ ($a_n \neq 0$, $n \ge 1$) pro $x \to +\infty$ a $x \to -\infty$?
> $x \to +\infty$: **znaménko $a_n$ krát $\infty$**. $x \to -\infty$: totéž pro sudé $n$, opačné znaménko pro liché $n$. Rozhoduje nejvyšší mocnina.

> [!karta|26]- Jak spočítáš $\lim_{x \to \pm\infty} \frac{f(x)}{g(x)}$ pro polynomy stupňů $n$ a $m$?
> $n = m$: **podíl vedoucích koeficientů** $\frac{a_n}{b_m}$. $n < m$: **0**. $n > m$: **$\pm\infty$** podle znaménka $\frac{a_n}{b_m}$ (u $-\infty$ navíc krát $(-1)^{n-m}$).

> [!karta|27]- Smíš na limitu posloupnosti použít l'Hospitalovo pravidlo přímo?
> **Ne**, posloupnost derivaci nemá. Přejdi k funkci $f(x)$, spočítej $\lim_{x \to +\infty} f(x)$ a výsledek přenes na posloupnost (limita funkce ⇒ limita posloupnosti).

### Příklady na procvičení

> [!priklad|18]- Spočítej $\lim_{x \to +\infty} \frac{x}{x}$ a $\lim_{x \to +\infty} \frac{3x}{x}$. Proč nejde použít aritmetika limit?
> Oboje je typ $\frac{+\infty}{+\infty}$, který není definován. Pro $x \neq 0$ je ale $\frac{x}{x} = 1$ a $\frac{3x}{x} = 3$, takže podle rovnosti ve směru vyjdou limity **1** a **3**: stejný typ, jiný výsledek.

> [!priklad|20]- Spočítej $\lim_{k \to +\infty} \big(2(k^2 + 6) + 1\big)$ pomocí substituce.
> $f(n) = 2n + 1 \to +\infty$, $\varphi(k) = k^2 + 6 \to +\infty$ a $k^2 + 6 > k$, takže ke kusu $\{n \ge N\}$ stačí $\{k \ge N\}$. Limita je **$+\infty$**.

> [!priklad|21]- Spočítej $\lim_{n \to +\infty} (n^3 + 1)$ přes limitu funkce.
> $\lim_{x \to +\infty} (x^3 + 1) = (+\infty)^3 + 1 = +\infty$, a proto i $\lim_{n \to +\infty} (n^3 + 1) =$ **$+\infty$**.

> [!priklad|22]- Dokaž, že $\lim_{n \to +\infty} (-1)^n$ neexistuje.
> $(-1)^{2k} = 1 \to 1$ a $(-1)^{2k+1} = -1 \to -1$. Dvě podposloupnosti s různými limitami, tedy limita **neexistuje**.

> [!priklad|24]- Spočítej $\lim_{n \to +\infty} \frac{2n + 1}{n + 3}$.
> Pro $n \ge 1$ je zlomek roven $\frac{2 + \frac{1}{n}}{1 + \frac{3}{n}}$. Čitatel $\to 2 + 0$, jmenovatel $\to 1 + 0 \neq 0$, podle aritmetiky je limita **2**.

> [!priklad|29]- Spočítej $\lim_{x \to -\infty} \frac{x^3}{x + 1}$.
> $n - m = 2$, $\frac{a_n}{b_m} = 1$, tedy $1 \cdot (-1)^2 \cdot (+\infty) =$ **$+\infty$**.

---
← [[MA1 04 – Nerovnosti ve směru a věta o sevření|1. 10. 2026 Nerovnosti ve směru a věta o sevření]] · [[MA1 06 – Spojitost a spojité funkce na intervalu|8. 10. 2026 Spojitost a spojité funkce na intervalu]] →

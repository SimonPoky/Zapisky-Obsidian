---
predmet: MA1
prednaska: 4
datum: 2026-10-01
zdroj: "Handout 2B (Počítání limit), slajdy 3–12"
tags: [prednaska, MA1]
---

# MA1 04 – Nerovnosti ve směru a věta o sevření

*Přednáška 4 · čtvrtek 1. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 2B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout02b.pdf)

Témata: `nerovnost ve směru` · `f = g ve směru` · `lim(−f)` · `znaménko limity` · `věta o sevření` · `x · sin(1/x)` · `omezenost` · `jednostranné limity` · `0 · omezená`

Minule jsme [[limita ve směru|limitu]] definovali, dnes začínáme s nástroji, jak ji počítat bez ε. Klíčová myšlenka: stačí, aby nerovnost nebo rovnost platila jen „kousek před cílem“, tedy na jednom kusu [[směr|směru]]. Z toho plyne krácení zlomků v limitě, přenos znaménka mezi funkcí a limitou a věta o sevření.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| rovnost ve směru | $f =_{\mathcal{S}} g$, $\lim_{\mathcal{S}} f = L$ | $\lim_{\mathcal{S}} g = L$ |
| opačná funkce | $\lim_{\mathcal{S}} f = L$ | $\lim_{\mathcal{S}} (-f) = -L$ |
| znaménko limity → funkce | $L > 0$ (resp. $L < 0$) | $f >_{\mathcal{S}} 0$ (resp. $f <_{\mathcal{S}} 0$) |
| znaménko funkce → limita | $f \ge_{\mathcal{S}} 0$ (resp. $\le$) | $L \ge 0$ (resp. $L \le 0$), ostrá nerovnost se **nepřenáší** |
| věta o sevření | $f \le_{\mathcal{S}} g \le_{\mathcal{S}} h$, $\lim f = \lim h = L$ | $\lim_{\mathcal{S}} g = L$ |
| tvrzení I | $\lim_{\mathcal{S}} f = L \in \mathbb{R}$ | $f$ je ve směru omezená |
| tvrzení II | $p \in \mathbb{R}$ | $\lim_{x \to p} f = L \iff \lim_{x \to p^-} f = \lim_{x \to p^+} f = L$ |
| tvrzení III | $\lim_{\mathcal{S}} f = 0$, $\lvert g \rvert \le_{\mathcal{S}} c$ | $\lim_{\mathcal{S}} (f \cdot g) = 0$ |

## §1 Nerovnost ve směru

> [!definice] Nerovnost ve směru · handout 2B, slajdy 3–6
> Pro $f_1, f_2$ a směr $\mathcal{S}$ píšeme
>
> - $f_1 \le_{\mathcal{S}} f_2$, když **existuje** $P \in \mathcal{S}$ tak, že $f_1(x) \le f_2(x)$ pro všechna $x \in P$,
> - $f_1 =_{\mathcal{S}} f_2$, $f_1 <_{\mathcal{S}} f_2$ obdobně,
> - $f$ je *omezená ve směru* $\mathcal{S}$, když $\lvert f \rvert \le_{\mathcal{S}} c$ pro nějaké $c \in \mathbb{R}$.
>
> Pro množinu $X$ znamená $f_1 \le_X f_2$, že $f_1(x) \le f_2(x)$ pro **všechna** $x \in X$.

^def-nerovnost

> [!lidsky] Lidsky
> [[nerovnost ve směru|Nerovnost ve směru]] platí „nakonec“: stačí jeden kus směru, tedy dost blízko cíle. Co se děje daleko od cíle, nás nezajímá. Posloupnost $a_n = n - 100$ je kladná ve směru $n \to +\infty$, i když prvních sto členů kladných není.

> [!example] f(x) = x² − 1 na [−1; 2]
> | otázka | odpověď | proč |
> |---|---|---|
> | $0 \le f$ na $[-1; 2]$? | **ne** | $f(0) = -1$ |
> | $f \le 0$ na $[-1; 0)$? | **ano** | tam $x^2 < 1$ |
> | $f \le 0$ ve směru $x \to 1$? | **ne** | každé $P_\delta(1)$ obsahuje i body $x > 1$, kde $f > 0$ |
> | $f < 0$ ve směru $x \to 1^-$? | **ano** | stačí $P = (0; 1)$ |

> [!obrazek] Nerovnost ve směru x → 1
> ![[ma104-nerovnost.png]]
> *Oranžově část grafu s f < 0, zeleně s f > 0. Modrý pás je kus směru x → 1; jakkoli úzký vždy zasáhne obě barvy, takže f ≤ 0 ve směru x → 1 neplatí. Levá polovina pásu ale celá leží v oranžové části: f < 0 ve směru x → 1⁻.*

## §2 Rovnost ve směru

> [!veta] Věta · handout 2B, slajd 7
> ==Jestliže $f =_{\mathcal{S}} g$ a $\lim_{\mathcal{S}} f = L$,== potom **$\lim_{\mathcal{S}} g$ existuje a rovná se $L$**.
>
> > [!note]- Důkaz
> > Máme $P' \in \mathcal{S}$, na kterém $f = g$. Ať $U \in \mathcal{N}(L)$. Z definice limity existuje $P$ s $f[P] \subseteq U$. Směr je vnořený, vezmeme menší z $P, P'$, označme ho $P''$. Na $P''$ je $g = f$, tedy $g[P''] = f[P''] \subseteq f[P] \subseteq U$.

^veta-rovnost

> [!lidsky] Lidsky
> Dvě funkce, které se kousek před cílem shodují, mají stejnou limitu. Proto smíš v limitě krátit: $\frac{x^2 - 9}{x - 3}$ a $x + 3$ se liší jen v bodě $3$, a ten do žádného kusu směru $x \to 3$ nepatří.

> [!obrazek] Důkaz obrázkem: rovnost ve směru
> ![[ma104-rovnost.png]]
> *Vlevo graf: černá f a oranžová čárkovaná g se daleko od p liší, ale na světle oranžovém kusu P′ splývají. Tmavší P″ je menší z P′ a P (P z definice limity f). Vpravo brambory: na P″ posílají šipky f i g každý bod na stejné místo, takže g[P″] = f[P″] leží v modrém terči U.*

> [!example] $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$
> $\frac{x^2 - 9}{x - 3} = \frac{(x - 3)(x + 3)}{x - 3} = x + 3$ pro $x \neq 3$, tedy $\frac{x^2 - 9}{x - 3} =_{x \to 3} x + 3$. Proto
>
> $$
> \lim_{x \to 3} \frac{x^2 - 9}{x - 3} = \lim_{x \to 3} (x + 3) = 6.
> $$
>
> Krácení je legální právě proto, že se k trojce nikdy nedostaneme.

> [!obrazek] Krácení v limitě
> ![[ma104-kraceni.png]]
> *Modře g(x) = x + 3, oranžově čárkovaně f(x) = (x² − 9)/(x − 3), která v bodě 3 není definovaná (prázdné kolečko). Na zeleném kusu směru se obě funkce shodují, a proto mají stejnou limitu 6.*

## §3 Znaménko limity

> [!veta] Věta · handout 2B, slajd 8
> ==Ať $\lim_{\mathcal{S}} f = L$.== Potom
>
> 1. **$\lim_{\mathcal{S}} (-f) = -L$**,
> 2. a) **$L > 0 \Rightarrow f >_{\mathcal{S}} 0$**, b) **$L < 0 \Rightarrow f <_{\mathcal{S}} 0$**,
> 3. a) **$f \ge_{\mathcal{S}} 0 \Rightarrow L \ge 0$**, b) **$f \le_{\mathcal{S}} 0 \Rightarrow L \le 0$**.

^veta-znamenko

> [!lidsky] Lidsky
> Limita a znaménko funkce si „rozumí“: je-li limita kladná, je funkce blízko cíle taky kladná (třeba $L = 3$, pak hodnoty kolem $3$ jsou nad nulou). Obráceně z $f \ge 0$ plyne jen $L \ge 0$, ne $L > 0$: funkce $\frac{1}{x} > 0$ má pro $x \to +\infty$ limitu $0$.

### Důkaz (1)

Pro $U \subseteq \mathbb{R}^*$ označme $-U = \{r \in \mathbb{R}^* \mid -r \in U\}$, zrcadlový obraz $U$ podle nuly. Zrcadlení převádí okolí $-L$ na okolí $L$: $-U_\varepsilon(-L) = U_\varepsilon(L)$, a u nekonečen se $(\varepsilon; +\infty]$ mění na $[-\infty; -\varepsilon)$ a naopak. Ať $U \in \mathcal{N}(-L)$. Pak $-U \in \mathcal{N}(L)$, takže existuje $P$ s $f[P] \subseteq -U$, a tedy $(-f)[P] \subseteq U$.

> [!obrazek] Důkaz (1) obrázkem: zrcadlo podle nuly
> ![[ma104-opacna.png]]
> *Vlevo graf: −f (oranžově čárkovaně) je f překlopená přes červenou nulu, s ní se překlopí i pás −U kolem L na pás U kolem −L. Vpravo brambory: stejný kus P pošle f do terče −U a −f do zrcadlového terče U.*

### Důkaz (2a)

$L > 0$, tedy $L \in (0; +\infty]$. Zvolíme okolí $U \in \mathcal{N}(L)$, které celé leží v $(0; +\infty]$: pro $L \in \mathbb{R}$ stačí $\varepsilon = L$, tedy $U = (0; 2L)$; pro $L = +\infty$ stačí $U = (1; +\infty]$. K němu existuje $P$ s $f[P] \subseteq U$, takže každá hodnota $f$ na $P$ je kladná: $f >_{\mathcal{S}} 0$. Bod 2b plyne z 2a použitého na $-f$ a z bodu 1.

> [!obrazek] Kladná limita drží funkci nad nulou
> ![[ma104-znamenko.png]]
> *Vlevo graf: modrý pás je terč U = (0; 2L), tedy ε = L, a končí přesně na červené nule. Nad oranžovým kusem směru P leží zelená část grafu celá v terči, a proto je tam f > 0. Vpravo brambory: červená čára dělí výstupy na kladné a záporné, terč U leží celý nad ní, a s ním i obraz f[P].*

### Důkaz (3a) sporem

Ať $f \ge_{\mathcal{S}} 0$ (na $P_1$) a $L < 0$. Podle 2b je $f <_{\mathcal{S}} 0$ (na $P_2$). Menší z $P_1, P_2$ je neprázdný a $f$ by na něm byla zároveň $\ge 0$ i $< 0$ ↯. Bod 3b plyne z 3a pro $-f$.

> [!obrazek] Důkaz (3a) obrázkem: dvě protichůdné podmínky
> ![[ma104-znamenko-spor.png]]
> *Vlevo graf: na světle oranžovém P₁ je f ≥ 0, ale terč U kolem L < 0 leží celý pod červenou nulou. Nad menším P₂ by graf musel být v U, a přitom je nad nulou (↯). Vpravo brambory: P₂ ⊆ P₁ se musí zobrazit do zelené oblasti y ≥ 0 i do modrého terče U pod nulou, a ty nemají společný bod.*

> [!pozor] Ostrá nerovnost se do limity nepřenáší
> Z $f >_{\mathcal{S}} 0$ **neplyne** $L > 0$, jen $L \ge 0$. Příklad: $\frac{1}{x} > 0$ pro $x > 0$, ale $\lim_{x \to +\infty} \frac{1}{x} = 0$. Limitním přechodem se $<$ mění na $\le$.

> [!navic] Hodnota v cíli limitu neovlivní
> $f(x) = 0$ pro $x \in [0; 3)$ a $f(3) = 2$. Pak $\lim_{x \to 3^-} f(x) = 0$, protože kus směru $(3 - \delta; 3)$ bod $3$ neobsahuje. Skok v samotném bodě $3$ je pro limitu neviditelný.

## §4 Věta o sevření

> [!veta] Věta o sevření (o dvou policajtech) · handout 2B, slajd 9
> ==Jestliže $f \le_{\mathcal{S}} g \le_{\mathcal{S}} h$ a $\lim_{\mathcal{S}} f = \lim_{\mathcal{S}} h = L$,== potom **$\lim_{\mathcal{S}} g$ existuje a rovná se $L$**.
>
> > [!note]- Důkaz
> > Ať $U \in \mathcal{N}(L)$. Existují $P_f, P_h$ s $f[P_f] \subseteq U$ a $h[P_h] \subseteq U$ a kus $P_0$, na kterém $f \le g \le h$. Vezmeme nejmenší z těchto tří, $P$. Pro $x \in P$ leží $f(x)$ i $h(x)$ v $U$ a $g(x)$ je mezi nimi. Okolí je interval, takže $g(x) \in U$. Tedy $g[P] \subseteq U$.

^veta-sevreni

> [!lidsky] Lidsky
> [[věta o sevření|Dva policajti]] $f$ a $h$ vedou vězně $g$ mezi sebou. Když oba dojdou na stejnou stanici $L$, vězeň tam dojde taky. Pozor: věta zároveň **zaručuje existenci** $\lim g$, nemusíš ji dokazovat předem.

> [!obrazek] Důkaz obrázkem: věta o sevření
> ![[ma104-sevreni-dukaz.png]]
> *Vlevo graf: modrá f a oranžová h jdou k L, černá g kmitá mezi nimi. Nad oranžovým kusem P (nejmenší ze tří kusů v důkazu) leží zelená část g v modrém pásu U. Vpravo brambory: jeden bod x z P se zobrazí na f(x) a h(x), oba v terči U. Hodnota g(x) leží na zelené úsečce mezi nimi, a protože U je interval, je v U taky.*

> [!example] $\lim_{x \to 0} x \cdot \sin\frac{1}{x} = 0$
> $\lvert \sin\frac{1}{x} \rvert \le 1$, tedy pro $x \neq 0$
>
> $$
> -\lvert x \rvert \le x \cdot \sin\frac{1}{x} \le \lvert x \rvert.
> $$
>
> $\lim_{x \to 0} (-\lvert x \rvert) = \lim_{x \to 0} \lvert x \rvert = 0$, takže podle věty o sevření $\lim_{x \to 0} x \sin\frac{1}{x} = 0$. Funkce $\sin\frac{1}{x}$ sama v nule limitu nemá (osciluje mezi $-1$ a $1$), ale vynásobená $x$ se „zmáčkne“.

> [!pozor] Častá chyba: meze −x ≤ x · sin(1/x) ≤ x
> Pro $x < 0$ je $-x > x$, takže nerovnost $-x \le x \sin\frac{1}{x} \le x$ by říkala, že kladné číslo je menší než záporné. Správné meze jsou $\pm\lvert x \rvert$. Šlo by to zachránit i tak, že se limita spočítá zvlášť pro $x \to 0^+$ (meze $\pm x$) a $x \to 0^-$ (meze $\pm(-x)$) a spojí tvrzením II.

> [!obrazek] Sevření x · sin(1/x)
> ![[ma104-sevreni.png]]
> *Oranžově horní mez |x|, modře dolní −|x|, zeleně x · sin(1/x), která mezi nimi kmitá stále rychleji, ale amplituda se k nule zmenšuje. Červená tečkovaná −x je pro x < 0 nad grafem, a proto jako dolní mez nefunguje.*

## §5 Tři užitečná tvrzení

> [!veta] Tvrzení I · handout 2B, slajd 10
> ==Je-li $\lim_{\mathcal{S}} f = L \in \mathbb{R}$,== pak **$\lvert f \rvert \le_{\mathcal{S}} c$ pro nějaké $c \in \mathbb{R}$** (vlastní limita ⇒ omezenost ve směru).
>
> > [!note]- Důkaz
> > Pro $U = (L - 1; L + 1)$ existuje $P$ s $f[P] \subseteq U$, takže na $P$ je $\lvert f \rvert \le \lvert L \rvert + 1 = c$.

^tvrzeni-omezenost

> [!lidsky] Lidsky
> Obrácená (kontrapoziční) verze se používá víc: **není-li $f$ ve směru omezená, nemá tam vlastní limitu**. Limita je pak $\pm\infty$, nebo vůbec neexistuje. Např. $\frac{1}{x}$ na $(0; +\infty)$ není omezená ve směru $x \to 0^+$ a opravdu $\lim_{x \to 0^+} \frac{1}{x} = +\infty$. Omezenost naopak limitu nezaručí: $\sin x$ je omezená, ale $\lim_{x \to +\infty} \sin x$ neexistuje.

> [!obrazek] Důkaz tvrzení I obrázkem
> ![[ma104-omezenost.png]]
> *Vlevo graf: modrý pás (L − 1; L + 1) a nad oranžovým kusem P zelená část grafu celá v něm. Červené čáry ±c s c = |L| + 1 tento pás obklopují, takže na P je |f| ≤ c. Mimo P může f utéct do nekonečna, to nevadí. Vpravo brambory: terč U = (L − 1; L + 1) leží uvnitř červené oblasti |y| ≤ c kolem nuly, a s ním i obraz f[P].*

> [!veta] Tvrzení II · handout 2B, slajd 11
> ==Pro $p \in \mathbb{R}$ a $f$ definovanou kolem $p$:==
>
> $$
> \lim_{x \to p} f(x) = L \iff \lim_{x \to p^-} f(x) = L = \lim_{x \to p^+} f(x).
> $$

^tvrzeni-jednostranne

> [!lidsky] Lidsky
> Oboustranná limita existuje, právě když se obě [[jednostranná limita|jednostranné]] shodují. Typické použití: dokázat, že limita **neexistuje**, protože zleva a zprava vyjde něco jiného, jako u $\operatorname{sgn} x$ v nule z [[MA1 03 – Rozšířená reálná čísla a limita ve směru|minulé přednášky]].

> [!veta] Tvrzení III · handout 2B, slajd 12
> ==Jestliže $\lim_{\mathcal{S}} f = 0$ a $\lvert g \rvert \le_{\mathcal{S}} c$,== potom **$\lim_{\mathcal{S}} (f \cdot g) = 0$**.
>
> > [!note]- Důkaz
> > $-c\lvert f \rvert \le f \cdot g \le c\lvert f \rvert$ ve směru $\mathcal{S}$ a obě meze mají limitu $0$, zbytek udělá věta o sevření.

^tvrzeni-nula-krat-omezena

> [!lidsky] Lidsky
> „Nula krát omezená je nula.“ Příklad $x \sin\frac{1}{x}$ z §4 je přesně tohle: $x \to 0$ a $\lvert \sin\frac{1}{x} \rvert \le 1$. Podobně $\lim_{n \to +\infty} \frac{n \sin(n!)}{n^2 + 1} = 0$, protože $\frac{n}{n^2 + 1} \to 0$ a $\lvert \sin(n!) \rvert \le 1$.

> [!pozor] Nestačí, aby g měla limitu „nějakou“
> Tvrzení III potřebuje **omezenost** $g$. Pro $f(x) = x$ a $g(x) = \frac{1}{x^2}$ je $\lim_{x \to 0} x = 0$, ale $x \cdot \frac{1}{x^2} = \frac{1}{x}$ limitu v nule nemá vůbec.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|02]- K čemu se hodí věta o rovnosti ve směru? Příklad.
> Ospravedlňuje **krácení v limitě**: $\frac{x^2 - 9}{x - 3} =_{x \to 3} x + 3$ (liší se jen v bodě $3$), takže $\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6$.

> [!karta|03]- Jak se dokáže $\lim_{\mathcal{S}} (-f) = -L$?
> Zrcadlení $-U = \{r \mid -r \in U\}$ převede okolí $-L$ na okolí $L$. K $-U$ najdi $P$ s $f[P] \subseteq -U$, pak $(-f)[P] \subseteq U$.

> [!karta|04]- Co plyne z $\lim_{\mathcal{S}} f = L > 0$ pro znaménko $f$? Myšlenka důkazu.
> **$f >_{\mathcal{S}} 0$.** Zvol okolí $L$, které celé leží v $(0; +\infty]$ (např. $(0; 2L)$, u $+\infty$ interval $(1; +\infty]$); obraz vhodného $P$ v něm leží, takže $f > 0$ na $P$.

> [!karta|05]- Dokaž: $f \ge_{\mathcal{S}} 0$ a $\lim_{\mathcal{S}} f = L$ ⇒ $L \ge 0$.
> Sporem: $L < 0$ dává $f <_{\mathcal{S}} 0$ na $P_2$; $f \ge 0$ na $P_1$. Na menším z nich (neprázdném) je $f \ge 0$ i $< 0$ ↯

> [!karta|06]- Plyne z $f >_{\mathcal{S}} 0$, že $\lim_{\mathcal{S}} f > 0$? Protipříklad.
> **Ne**, jen $\ge 0$. $\frac{1}{x} > 0$, ale $\lim_{x \to +\infty} \frac{1}{x} = 0$.

> [!karta|08]- Myšlenka důkazu věty o sevření?
> K okolí $U$ vezmi $P_f$, $P_h$ a kus, kde platí nerovnosti; nejmenší z nich $P$. Na něm $f(x), h(x) \in U$ a $g(x)$ leží mezi nimi; okolí je interval, tedy $g(x) \in U$.

> [!karta|09]- Jak se obráceně (kontrapozicí) použije věta, že funkce s vlastní limitou je ve směru omezená?
> Kontrapozicí: je-li $f$ ve směru **neomezená**, je její limita $\pm\infty$, nebo neexistuje. Vlastní být nemůže.

> [!karta|10]- Plyne z omezenosti $f$ ve směru existence limity?
> **Ne.** $\sin x$ je omezená, ale $\lim_{x \to +\infty} \sin x$ neexistuje.

> [!karta|11]- Jak souvisí $\lim_{x \to p} f$ s jednostrannými limitami?
> $\lim_{x \to p} f = L \iff \lim_{x \to p^-} f = L = \lim_{x \to p^+} f$. Různé jednostranné limity ⇒ oboustranná neexistuje.

> [!karta|13]- Proč je ve větě „$\lim_{\mathcal{S}} f = 0$ a $g$ omezená ⇒ $\lim_{\mathcal{S}} (f \cdot g) = 0$“ nutná omezenost $g$? Protipříklad.
> $f = x \to 0$, $g = \frac{1}{x^2}$ neomezená v $x \to 0$: $fg = \frac{1}{x}$ v nule limitu nemá.

### Příklady na procvičení

> [!priklad|14]- Platí pro $f(x) = x^2 - 1$ na $[-1; 2]$ nerovnost $f \le 0$ ve směru $x \to 1$? A ve směru $x \to 1^-$?
> $x \to 1$: **ne**, každé $P_\delta(1)$ obsahuje $x > 1$ s $f(x) > 0$. $x \to 1^-$: **ano**, na $(0; 1)$ je $f < 0$.

> [!priklad|15]- Spočítej $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$ a zdůvodni krácení.
> Pro $x \neq 3$ je zlomek $x + 3$, tedy $=_{x \to 3}$; podle věty o rovnosti ve směru je limita $\lim_{x \to 3} (x + 3) =$ **6**.

> [!priklad|16]- Spočítej $\lim_{x \to 0} x \sin\frac{1}{x}$.
> $-\lvert x \rvert \le x \sin\frac{1}{x} \le \lvert x \rvert$ a obě meze jdou k 0, sevření dá **0**. (Meze $\pm x$ jsou pro $x < 0$ špatně.)

> [!priklad|17]- Spočítej $\lim_{n \to +\infty} \frac{n \sin(n!)}{n^2 + 1}$.
> $\frac{n}{n^2 + 1} \to 0$ a $\lvert \sin(n!) \rvert \le 1$, podle [[věta o součinu nulové a omezené funkce|věty o součinu nulové a omezené funkce]] je limita **0**.

> [!priklad|18]- $f(x) = 0$ na $[0; 3)$, $f(3) = 2$. Kolik je $\lim_{x \to 3^-} f(x)$?
> **0.** Kus směru $(3 - \delta; 3)$ bod 3 neobsahuje, hodnota $f(3)$ limitu neovlivní.

> [!priklad|19]- Má $f(x) = \frac{1}{x}$ na $(0; +\infty)$ vlastní limitu pro $x \to 0^+$?
> **Ne.** Není ve směru $x \to 0^+$ omezená, takže podle [[věta o omezenosti funkce s vlastní limitou|věty o omezenosti funkce s vlastní limitou]] vlastní limitu mít nemůže; $\lim_{x \to 0^+} \frac{1}{x} = +\infty$.

---
← [[MA1 03 – Rozšířená reálná čísla a limita ve směru|30. 9. 2026 Rozšířená reálná čísla a limita ve směru]] · [[MA1 05 – Aritmetika limit a substituce|7. 10. 2026 Aritmetika limit a substituce]] →

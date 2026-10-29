---
predmet: MA1
prednaska: 11
datum: 2026-10-29
zdroj: "Handout 5B (Gradient descent), slajdy 2–8; Handout 6A (Axiomatické zavedení integrálu), slajdy 2–14"
tags: [prednaska, MA1]
---

# MA1 11 – Lemma o konvexních funkcích a axiomatický integrál

*Přednáška 11 · čtvrtek 29. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 5B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout05b.pdf) · [Handout 6A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout06a.pdf)

Témata: `lemma o konvexních funkcích` · `tečna pod grafem` · `lokální minimum = globální` · `Jensenova nerovnost` · `gradient descent (bonus)` · `axiomy integrálu: aditivita a omezenost` · `∫ₐᵃ f = 0, obrácené meze` · `integrál jako funkce horní meze` · `F′ = f` · `primitivní funkce` · `jednoznačnost integrálu` · `dolní a horní součet`

Minule se ukázalo, že konvexita funkce s derivací znamená neklesající $f'$. Dnes z toho plyne důležité lemma: tečna konvexní funkce leží pod grafem, každé lokální minimum je globální a platí Jensenova nerovnost. Lemma je jádro metody gradient descent, kterou se učí neuronové sítě; ta sama je jen ukázka navíc. Pak začíná **integrál**: místo vzorce se zavede dvěma vlastnostmi (aditivita a omezenost), z nich vyjde, že derivace integrálu podle horní meze je $f$, a tím i to, že integrál se počítá přes primitivní funkci.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| lemma (1) tečna pod grafem | $f$ konvexní, $f'$ na $\mathbb{R}$ | $f(p) + f'(p)(x - p) \le f(x)$ pro všechna $p, x$ |
| lemma (2) | totéž | lokální minimum je globální |
| lemma (3) Jensen | totéž, $a_i \ge 0$, $\sum a_i = 1$ | $f\bigl(\sum a_i x_i\bigr) \le \sum a_i f(x_i)$ |
| axiomy integrálu | $f$ spojitá na $[a; b]$ | aditivita $\int_a^v f = \int_a^u f + \int_u^v f$; omezenost $(v - u)\min f \le \int_u^v f \le (v - u)\max f$ |
| důsledky | | $f \ge 0 \Rightarrow \int_a^b f \ge 0$; $\int_a^a f = 0$; $\int_b^a f := -\int_a^b f$ |
| derivace podle horní meze | $f$ spojitá na $[a; b]$, $F(x) = \int_a^x f$ | $F'(x) = f(x)$ na $[a; b]$ |
| primitivní funkce | $G' = f$ na $[a; b]$ | $G(v) - G(u)$ splňuje oba axiomy, tedy $= \int_u^v f$ |
| vlastnosti primitivních | $F_1, F_2$ primitivní k $f$ | $F_1 = F_2 + c$; s $G(x_0) = y_0$ existuje právě jedna |
| existence | dělení $\Delta$, součty $L(f; \Delta) \le U(f; \Delta)$ | $\sup_\Delta L = \inf_\Delta U = \int_a^b f$ |

## §1 Lemma o konvexních funkcích

> [!definice] Globální minimum · handout 5B, slajd 6
> Ať je funkce $f$ definována na množině $M$. Bod $p \in M$ je *globální minimum* funkce $f$ na $M$, jestliže $f(p) \le f(x)$ pro **všechna** $x \in M$.

^def-globalni-minimum

> [!lidsky] Lidsky
> [[lokální minimum|Lokální minimum]] je dno jedné kotliny: v okolí $p$ není nic nižšího. [[globální minimum|Globální minimum]] je nejnižší bod **celé** krajiny. Každé globální minimum je lokální, obráceně ne.

> [!example] Příklad
> $f(x) = x^2$ má v $0$ globální minimum: $0 \le x^2$ pro všechna $x$. Funkce $f(x) = x^3 - 3x$ má v $1$ lokální minimum $f(1) = -2$, ale globální ne: $f(-3) = -18 < -2$ a $f$ jde k $-\infty$.

> [!veta] Lemma o konvexních funkcích · handout 5B, slajd 8
> Ať ==$f$ má první derivaci na $\mathbb{R}$ a je na $\mathbb{R}$ konvexní== (to je podle minulé přednášky totéž jako $f'$ neklesající). Potom:
>
> 1. **Pro všechna $p$ a všechna $x$ platí $f'(p)(x - p) + f(p) \le f(x)$.** Levá strana je výška tečny v bodě $p$ nad bodem $x$.
> 2. **Každé lokální minimum funkce $f$ je globální minimum.**
> 3. **Jensenova nerovnost:** pro jakákoli $x_1, \dots, x_n$ a jakákoli ==$a_1, \dots, a_n \ge 0$ s $\sum_{i=1}^n a_i = 1$== platí
> $$
> f\Bigl(\sum_{i=1}^n a_i x_i\Bigr) \le \sum_{i=1}^n a_i f(x_i).
> $$
>
> > [!note]- Důkaz (1)
> > Pro $x = p$ platí rovnost. Ať $x < p$ (případ (i)). Podle [[Lagrangeova věta|Lagrangeovy věty]] na $[x; p]$ existuje $t \in (x; p)$ s
> > $$
> > \frac{f(x) - f(p)}{x - p} = f'(t) \le f'(p),
> > $$
> > protože $t < p$ a $f'$ je [[konvexita pomocí první derivace|neklesající]]. Vynásobením záporným číslem $x - p$ se nerovnost otočí: $f(x) - f(p) \ge f'(p)(x - p)$.
> > Ať $x > p$ (případ (ii)). Lagrange na $[p; x]$ dá $t \in (p; x)$ s $\frac{f(x) - f(p)}{x - p} = f'(t) \ge f'(p)$, protože $t > p$. Násobí se kladným $x - p$, takže znovu $f(x) - f(p) \ge f'(p)(x - p)$.
>
> > [!note]- Důkaz (2)
> > V lokálním minimu $p$ je $f'(p) = 0$ ([[nutná podmínka lokálního extrému]]). Podle (1) je $f(x) \ge f(p) + 0 \cdot (x - p) = f(p)$ pro **všechna** $x$, tedy $p$ je globální minimum.
>
> > [!note]- Důkaz (3)
> > Označ $p = \sum_{i=1}^n a_i x_i$. Podle (1) je $f(x_i) \ge f(p) + f'(p)(x_i - p)$ pro každé $i$. Vynásob $a_i \ge 0$ a sečti:
> > $$
> > \sum a_i f(x_i) \ge \Bigl(\sum a_i\Bigr) f(p) + f'(p)\Bigl(\sum a_i x_i - \bigl(\textstyle\sum a_i\bigr) p\Bigr) = f(p) + f'(p)(p - p) = f(p).
> > $$

^veta-lemma-konvexni

> [!lidsky] Lidsky
> [[lemma o konvexních funkcích|Lemma]] lidsky: na misce leží tečna vždycky **pod** okrajem misky, nikde ji nepropíchne. Proto když je někde vodorovná tečna (dno, $f'(p) = 0$), je celá miska nad ní: lokální dno je zároveň nejnižší bod. [[Jensenova nerovnost]] je totéž co definice konvexity, jen pro víc bodů najednou: funkce průměru je nejvýš průměr funkcí.

> [!example] Příklad
> - **(1)** pro $f(x) = e^x$ a $p = 0$: tečna je $y = 1 + x$, takže $1 + x \le e^x$ pro všechna $x$ (třeba $x = 1$: $2 \le e \approx 2{,}72$).
> - **(3)** pro $f(x) = x^2$, body $0, 2, 4$ s vahami $\tfrac14, \tfrac14, \tfrac12$: vážený průměr bodů je $2{,}5$, $f(2{,}5) = 6{,}25 \le \tfrac14 \cdot 0 + \tfrac14 \cdot 4 + \tfrac12 \cdot 16 = 9$.

> [!obrazek] Tečna pod grafem a myšlenka důkazu
> ![[ma111-tecna-pod-grafem.png]]
> *Vlevo: oranžová tečna v bodě p leží celá pod modrým grafem konvexní funkce, zelené úsečky jsou nezáporné rozdíly f(x) − (tečna). Vpravo případ x < p: červená sečna z x do p má podle Lagrange směrnici f′(t) pro nějaké t mezi nimi, a protože f′ je neklesající, je nejvýš směrnice tečny f′(p).*

> [!pozor] Bez konvexity lemma neplatí
> $f(x) = x^3 - 3x$ má derivaci všude a v $1$ ostré lokální minimum $f(1) = -2$ ($f'(1) = 0$, $f''(1) = 6 > 0$), ale $f(-3) = -18$. Není konvexní ($f'' = 6x < 0$ pro $x < 0$), takže část (2) se na ni nevztahuje.

> [!navic] Definice konvexity je Jensen pro $n = 2$
> Konvexita na $\mathbb{R}$ byla definována jako $f(a x_1 + (1 - a) x_2) \le a f(x_1) + (1 - a) f(x_2)$: to je přesně (3) pro dva body s vahami $a$ a $1 - a$. Lemma říká, že pro funkce s derivací to platí pro libovolný počet bodů.

## §2 Gradient descent (ukázka navíc)

Neuronová síť je funkce, která ze vstupu a z vah synapsí spočítá odpověď. Učení = najít váhy, při kterých je **ztráta** (loss, rozdíl mezi odpovědí a správným výsledkem) nejmenší. To je hledání minima funkce; pro mnoho proměnných se to probírá v MA2. Pro jednu proměnnou to dělá [[gradient descent]]:

> [!navic] Gradient descent pro jednu proměnnou · handout 5B, slajdy 5–7
> *Gradient descent* (gradientní sestup) je iterační metoda, která hledá lokální minimum funkce $f$ s derivací. Myšlenka: stojíš na grafu, popojdeš kousek **směrem dolů** a opakuješ. Vstup: $f$, start $x_0$, délka kroku $\gamma > 0$, počet kroků $T$. Krok:
> $$
> x_{i+1} = x_i - \gamma \cdot f'(x_i).
> $$
> Je-li $f'(x_i) > 0$ (graf stoupá), jde se doleva, je-li $f'(x_i) < 0$, doprava. Procedura vrací průměr $x_{\mathrm{avg}} = \frac{1}{T}\sum_{i=0}^{T-1} x_i$. Pro konvexní $f$ s $|f'| \le L$, $|x_0 - x_{\min}| = R$ a $\gamma = R/(L\sqrt{T})$ platí odhad $|f(x_{\mathrm{avg}}) - f(x_{\min})| \le RL/\sqrt{T}$ (důkaz se zde neuvádí, stojí na lemmatu z §1). Backpropagation je způsob, jak derivace pro mnoho vah spočítat efektivně „pozpátku“.

^gradient-descent

> [!example] Příklad
> $f(x) = x^2$, $f'(x) = 2x$, $x_0 = 1$, $\gamma = \tfrac14$: $x_1 = 1 - \tfrac14 \cdot 2 = 0{,}5$, $x_2 = 0{,}5 - \tfrac14 \cdot 1 = 0{,}25$, $x_3 = 0{,}125$. Každý krok vzdálenost od minima $0$ půlí.

> [!obrazek] Proč gradient descent chce konvexitu
> ![[ma111-gradient-descent.png]]
> *Oranžové body jsou kroky metody. Vlevo konvexní funkce: lokální minimum je podle lemmatu globální (zelená hvězda), metoda dojde tam, kam má. Vpravo nekonvexní funkce: kroky skončí v lokálním minimu (červený kroužek) a globální minimum vlevo nenajdou.*

> [!navic] Co z této části patří ke zkoušce
> Podle handoutu 5B (slajd 2) chce ústní zkouška jen základní myšlenku gradient descentu (slajdy 5 a 6) a lemma z §1. Věta o konvergenci a backpropagation jsou rozšíření.

## §3 Axiomatické zavedení určitého integrálu

**Cíl:** k funkci $f$ [[spojitost na intervalu|spojité]] na $[a; b]$ přiřadit reálné číslo $\int_a^b f$, *integrál $f$ od $a$ do $b$*. Pro kladnou $f$ má to být obsah plochy mezi grafem a osou $x$ mezi kolmicemi v $a$ a $b$. Místo vzorce se řekne, jaké dvě vlastnosti musí mít.

> [!definice] Určitý integrál (axiomy) · handout 6A, slajd 5
> Ať je $f$ spojitá na omezeném uzavřeném intervalu $[a; b]$. Přiřazení, které každé dvojici $u, v$ s $a \le u \le v \le b$ dá reálné číslo $\int_u^v f$, je *určitý integrál*, jestliže platí:
>
> 1. **Aditivita:** $\displaystyle\int_a^v f = \int_a^u f + \int_u^v f$.
> 2. **Omezenost:** $\displaystyle(v - u) \cdot \min_{t \in [u; v]} f(t) \le \int_u^v f \le (v - u) \cdot \max_{t \in [u; v]} f(t)$.

^def-urcity-integral

> [!lidsky] Lidsky
> [[určitý integrál|Určitý integrál]] modeluje plochu. [[aditivita integrálu|Aditivita]]: plocha od $a$ do $v$ je plocha do $u$ plus plocha od $u$ dál, jako když rozřízneš pozemek na dva. [[omezenost integrálu|Omezenost]]: plocha pod grafem je aspoň obdélník s výškou nejnižšího bodu a nejvýš obdélník s výškou nejvyššího bodu (oba se šířkou $v - u$). Minimum a maximum na $[u; v]$ existují, protože $f$ je spojitá ([[věta o extrémech]]).

> [!example] Příklad
> $f(x) = x$ na $[0; 2]$. Plocha je trojúhelník, $\int_0^2 x = 2$, $\int_0^1 x = \tfrac12$, $\int_1^2 x = \tfrac32$. Aditivita: $\tfrac12 + \tfrac32 = 2$. Omezenost na $[0; 2]$: $2 \cdot 0 = 0 \le 2 \le 2 \cdot 2 = 4$. Naopak přiřazení $\int_u^v f := 0$ pro všechna $u, v$ je aditivní, ale pro $f = 1$ porušuje omezenost: $(v - u) \cdot 1 \le 0$ neplatí pro $u < v$.

> [!obrazek] Dva axiomy
> ![[ma111-aditivita-omezenost.png]]
> *Vlevo aditivita: oranžová plocha od a do u plus zelená od u do v je plocha od a do v. Vpravo omezenost: modrá plocha od u do v leží mezi zeleným obdélníkem s výškou min f a červeným čárkovaným s výškou max f.*

> [!navic] Značení a názvy · handout 6A, slajd 6
> V tvrzeních se píše $\int_u^v f$, při počítání $\int_u^v f(t)\,\mathrm{d}t$ (stejně dobře $\int_u^v f(s)\,\mathrm{d}s$). $f$ je *integrand*, $t$ *integrační proměnná*, $u$ *dolní* a $v$ *horní integrační mez*. Zatím není jasné, jestli takové přiřazení **existuje** a jestli je **jediné**: obojí se dokáže níže.

## §4 Co by integrál musel splňovat

> [!veta] Důsledky axiomů · handout 6A, slajd 7
> Ať $\int$ splňuje aditivitu a omezenost pro spojitou $f$ na $[a; b]$. Potom
>
> 1. **je-li ==$0 \le f$ na $[a; b]$==, je $0 \le \int_a^b f$**;
> 2. **$\int_a^a f = 0$.**
>
> > [!note]- Důkaz
> > (1) Z $f \ge 0$ je $\min_{t \in [a; b]} f(t) \ge 0$, takže podle omezenosti $0 \le (b - a) \cdot \min f(t) \le \int_a^b f$.
> > (2) Aditivita pro $u = a$, $v = b$: $\int_a^b f = \int_a^a f + \int_a^b f$, odečti $\int_a^b f$.

^veta-dusledky-axiomu

> [!lidsky] Lidsky
> [[nezápornost integrálu|Plocha pod grafem]], který je nad osou, nemůže vyjít záporná. A pruh nulové šířky má nulovou plochu.

> [!definice] Integrál s obrácenými mezemi · handout 6A, slajd 7
> Pro $a \le b$ definujeme $\displaystyle\int_b^a f = -\int_a^b f$.

^def-obracene-meze

> [!lidsky] Lidsky
> [[integrál s obrácenými mezemi|Integrovat „pozpátku“]] znamená brát plochu se záporným znaménkem. Definice je zvolená tak, aby aditivita platila i pro meze v libovolném pořadí: $\int_b^a f + \int_a^b f = \int_b^b f = 0$.

> [!example] Příklad
> $\int_0^2 x = 2$, tedy $\int_2^0 x = -2$. Kontrola aditivitou: $\int_0^2 x + \int_2^0 x = 2 - 2 = 0 = \int_0^0 x$.

## §5 Integrál jako funkce horní meze

> [!definice] Integrál jako funkce horní meze · handout 6A, slajd 7
> Pro $x \in [a; b]$ označme $\displaystyle F(x) = \int_a^x f$. Tím je definována funkce $F : [a; b] \to \mathbb{R}$. Platí $F(a) = 0$ a
> $$
> F(b) - F(a) = F(b) = \int_a^b f.
> $$

^def-horni-mez

> [!lidsky] Lidsky
> [[integrál jako funkce horní meze|$F(x)$]] je „kolik plochy se nasbíralo“ od $a$ do $x$, jako počítadlo ujeté vzdálenosti, které na startu ukazuje 0. Kde je $f$ pod osou, plocha se odečítá a $F$ klesá.

> [!example] Příklad
> Pro $f(t) = \cos t$ na $[0; 2\pi]$ je $F(x) = \int_0^x \cos t\,\mathrm{d}t = \sin x$: $F(0) = 0$, $F(\tfrac{\pi}{2}) = 1$ (nasbíraná kladná plocha), $F(\pi) = 0$ (kladná a záporná část se vyruší).

> [!veta] Derivace integrálu jako funkce horní meze · handout 6A, slajd 8
> Ať ==$f$ je spojitá na $[a; b]$== a $F(x) = \int_a^x f$. Potom **$F$ má derivaci na $[a; b]$ a pro všechna $x \in [a; b]$ platí**
> $$
> F'(x) = \frac{\mathrm{d}}{\mathrm{d}x}\Bigl(\int_a^x f\Bigr) = f(x).
> $$
> „Derivace na $[a; b]$“ znamená derivaci ve vnitřních bodech, zprava v $a$ a zleva v $b$ ([[derivace na intervalu]]).
>
> > [!note]- Důkaz
> > Ať $h > 0$ a $x + h \in [a; b]$. Podle aditivity je $F(x + h) - F(x) = \int_x^{x + h} f$ a podle omezenosti (šířka $h$)
> > $$
> > \min_{t \in [x; x + h]} f(t) \le \frac{F(x + h) - F(x)}{h} \le \max_{t \in [x; x + h]} f(t).
> > $$
> > Pro $h \to 0^+$ se interval $[x; x + h]$ smršťuje do bodu $x$ a ze spojitosti $f$ jdou minimum i maximum k $f(x)$. Podle [[věta o sevření|věty o sevření]] je $\lim_{h \to 0^+} \frac{F(x + h) - F(x)}{h} = f(x)$. Pro $h \to 0^-$ analogicky.

^veta-derivace-horni-meze

> [!lidsky] Lidsky
> [[věta o derivaci integrálu podle horní meze|Proč to platí]]: o kolik přibude plocha, když posuneš horní mez o malé $h$? Zhruba o proužek šířky $h$ a výšky $f(x)$. Rychlost přibývání plochy je tedy právě $f(x)$. Integrování a derivování jsou opačné operace.

> [!example] Příklad
> $F(x) = \int_0^x t^2\,\mathrm{d}t$ má $F'(x) = x^2$, takže $F'(3) = 9$, a to bez počítání integrálu. U $F(x) = \int_0^x \cos t\,\mathrm{d}t = \sin x$ sedí $F'(x) = \cos x$.

> [!obrazek] Plocha se znaménkem a funkce F
> ![[ma111-horni-mez.png]]
> *Nahoře modrý graf f(t) = cos t; F(x) je zelená plocha nad osou minus červená plocha pod osou od 0 po oranžovou čáru x. Dole oranžový graf F(x) = sin x: roste, kde je f kladná, klesá, kde je záporná, a F(0) = 0.*

## §6 Primitivní funkce

> [!definice] Primitivní funkce · handout 6A, slajd 9
> Ať je $f$ spojitá na $[a; b]$. Funkce $G : [a; b] \to \mathbb{R}$, která má na $[a; b]$ derivaci a $G'(x) = f(x)$ pro všechna $x \in [a; b]$, se nazývá *primitivní funkce* k $f$ na $[a; b]$.

^def-primitivni-funkce

> [!lidsky] Lidsky
> [[primitivní funkce|Primitivní funkce]] je „derivace pozpátku“: hledáš funkci, jejíž derivace je zadaná $f$. Podle §5 jednu vždycky máš: $F(x) = \int_a^x f$.

> [!example] Příklad
> K $f(x) = 2x$ je primitivní $x^2$, ale také $x^2 + 4$ nebo $x^2 - 7$: všechny mají derivaci $2x$. K $\cos x$ je primitivní $\sin x$. $x^2$ **není** primitivní k $x$ (její derivace je $2x$), primitivní je $\tfrac12 x^2$.

> [!veta] Primitivní funkce má obě vlastnosti integrálu · handout 6A, slajd 9
> Ať ==$f$ je spojitá na $[a; b]$ a $G$ je k ní primitivní==. Potom pro $a \le u \le v \le b$:
>
> 1. **aditivita:** $G(v) - G(a) = \bigl(G(u) - G(a)\bigr) + \bigl(G(v) - G(u)\bigr)$;
> 2. **omezenost:** $(v - u) \cdot \min_{x \in [u; v]} f(x) \le G(v) - G(u) \le (v - u) \cdot \max_{x \in [u; v]} f(x)$.
>
> Slogan: **$G(v) - G(u)$ „je“ integrál z $f$ od $u$ do $v$.**
>
> > [!note]- Důkaz
> > (1) je jen přičtení a odečtení $G(u)$. (2) Pro $u = v$ jsou všechny tři výrazy $0$. Pro $u < v$ dá [[Lagrangeova věta]] bod $t \in (u; v)$ s
> > $$
> > \min_{[u; v]} f \le \frac{G(v) - G(u)}{v - u} = G'(t) = f(t) \le \max_{[u; v]} f;
> > $$
> > vynásob kladným $v - u$.

^veta-primitivni-axiomy

> [!lidsky] Lidsky
> [[primitivní funkce splňuje axiomy integrálu|Rozdíl hodnot primitivní funkce]] se chová přesně jako plocha: sčítá se po kouscích a je mezi „malým“ a „velkým“ obdélníkem. Protože integrál je těmi dvěma vlastnostmi určen jednoznačně (viz níže), **je** to ta plocha.

> [!veta] Vlastnosti primitivních funkcí · handout 6A, slajd 10
> Ať ==$f$ je spojitá na omezeném uzavřeném intervalu $[a; b]$==.
>
> 1. **Jsou-li ==$F_1, F_2$ primitivní funkce k $f$ na $[a; b]$==, existuje konstanta $c \in \mathbb{R}$ taková, že $F_1(x) = F_2(x) + c$ na $[a; b]$.**
> 2. **Je-li ==$F$ primitivní funkce k $f$==, pak pro každé ==$x_0 \in [a; b]$ a každé $y_0 \in \mathbb{R}$== existuje právě jedna primitivní funkce $G$ k $f$ s $G(x_0) = y_0$.**
>
> > [!note]- Důkaz
> > (1) $(F_1 - F_2)' = F_1' - F_2' = f - f = 0$ na $[a; b]$, takže podle [[věta o nulové derivaci|věty o nulové derivaci]] je $F_1 - F_2$ konstantní.
> > (2) Existence: $G(x) := F(x) + \bigl(y_0 - F(x_0)\bigr)$; závorka je konstanta, takže $G' = F' = f$, a $G(x_0) = F(x_0) + y_0 - F(x_0) = y_0$. Jednoznačnost: dvě takové $G_1, G_2$ se podle (1) liší o konstantu $c$, a v $x_0$ je $c = G_1(x_0) - G_2(x_0) = y_0 - y_0 = 0$.

^veta-vlastnosti-primitivnich

> [!lidsky] Lidsky
> Primitivních funkcí je nekonečně mnoho, ale všechny vypadají stejně, jen posunuté nahoru nebo dolů ([[primitivní funkce se liší o konstantu|liší se o konstantu]]). Jakmile předepíšeš jeden bod, kterým má graf projít, zbude [[primitivní funkce s předepsanou hodnotou|právě jedna]]. To se bude hodit u diferenciálních rovnic (počáteční podmínka).

> [!example] Příklad
> Primitivní funkce k $f(x) = 2x$ na $[-2; 2]$ jsou přesně $x^2 + c$. S podmínkou $G(1) = 5$: $1 + c = 5$, tedy $c = 4$ a $G(x) = x^2 + 4$. Postup z důkazu dá totéž: $F(x) = x^2$, $G(x) = x^2 + (5 - F(1)) = x^2 + 4$.

> [!obrazek] Rodina primitivních funkcí
> ![[ma111-primitivni.png]]
> *Šedomodré křivky x² + c jsou všechny primitivní funkce k 2x, navzájem posunuté o konstantu. Oranžová je jediná z nich, která prochází bodem (1; 5).*

> [!veta] Jednoznačnost určitého integrálu · handout 6A, slajd 11
> Ať ==$f$ je spojitá na $[a; b]$==. Pak **je číslo $\int_a^u f$ (pro každé $u \in [a; b]$) určeno jednoznačně**: každé přiřazení splňující aditivitu a omezenost dá totéž.
>
> > [!note]- Důkaz
> > Pro libovolné takové přiřazení je $F(x) = \int_a^x f$ podle §5 primitivní funkce k $f$ a $F(a) = 0$. Podle vlastnosti (2) je primitivní funkce s hodnotou $0$ v bodě $a$ jediná, takže $F$ a s ní všechna čísla $\int_a^u f = F(u)$ jsou určená jednoznačně.

^veta-jednoznacnost-integralu

> [!lidsky] Lidsky
> [[jednoznačnost určitého integrálu|Jednoznačnost]]: dvě „různé“ definice plochy, které obě splňují aditivitu a omezenost, musí dávat stejná čísla. Proto stačí najít **jakoukoli** primitivní funkce $G$ a integrál je $G(v) - G(u)$; nic jiného to být nemůže.

## §7 Existence: dolní a horní součty

Zbývá ukázat, že integrál vůbec **existuje**. Myšlenka (Archimedes, později Riemann a Darboux): plochu přibližovat obdélníky zespoda a shora.

> [!definice] Dělení, dolní a horní součet · handout 6A, slajd 13
> *Dělení* $\Delta$ intervalu $[a; b]$ jsou body $a = x_0 < x_1 < \dots < x_{n-1} < x_n = b$. Pro spojitou $f$ na $[a; b]$ je
>
> - *dolní součet* $\displaystyle L(f; \Delta) = \sum_{i=0}^{n-1} (x_{i+1} - x_i) \cdot \min_{t \in [x_i; x_{i+1}]} f(t)$,
> - *horní součet* $\displaystyle U(f; \Delta) = \sum_{i=0}^{n-1} (x_{i+1} - x_i) \cdot \max_{t \in [x_i; x_{i+1}]} f(t)$.

^def-darboux

> [!lidsky] Lidsky
> Rozřež $[a; b]$ na proužky ([[dělení intervalu|dělení]]). [[dolní součet|Dolní součet]]: do každého proužku dej co nejvyšší obdélník, který se ještě vejde **pod** graf. Horní součet: co nejnižší obdélník, který graf **přikryje** ([[horní součet]]). Skutečná plocha je mezi nimi; čím jemnější řezání, tím jsou si blíž.

> [!example] Příklad
> $f(x) = x^2$ na $[0; 2]$. Pro $\Delta$: $0 < 1 < 2$ je $L = 1 \cdot 0 + 1 \cdot 1 = 1$ a $U = 1 \cdot 1 + 1 \cdot 4 = 5$. Pro jemnější $\Delta'$: $0 < 0{,}5 < 1 < 1{,}5 < 2$ je $L = 1{,}75$ a $U = 3{,}75$. Skutečná hodnota $\int_0^2 x^2 = \tfrac83 \approx 2{,}67$ je mezi nimi.

> [!obrazek] Dolní a horní součet
> ![[ma111-darboux.png]]
> *Modrý graf x² na [0; 2] rozdělený na čtyři proužky šířky 0,5. Vlevo zelené obdélníky s výškou minima (dolní součet 1,75), vpravo červené s výškou maxima (horní součet 3,75).*

> [!veta] Existence určitého integrálu · handout 6A, slajd 13
> Vždy platí $L(f; \Delta) \le U(f; \Delta)$ a pro dělení $\Delta'$ jemnější než $\Delta$ (obsahuje všechny body $\Delta$ a možná další)
> $$
> L(f; \Delta) \le L(f; \Delta') \le U(f; \Delta') \le U(f; \Delta).
> $$
> Pro ==$f$ spojitou na $[a; b]$== platí **$\sup_\Delta L(f; \Delta) = \inf_\Delta U(f; \Delta)$ a tato společná hodnota je $\int_a^b f$**: splňuje aditivitu i omezenost. Důkaz (ε-δ výpočet) se zde neuvádí.

^veta-existence-integralu

> [!lidsky] Lidsky
> [[existence určitého integrálu|Existence]]: zjemňováním se dolní součty zvětšují a horní zmenšují. U spojité funkce se k sobě přiblíží libovolně těsně a číslo, ve kterém se „potkají“, je integrál.

> [!veta] Fundamentální věta kalkulu · handout 6A, slajd 14
> Ať ==$f$ je spojitá na omezeném uzavřeném intervalu $[a; b]$==. Potom
>
> 1. **integrál $\int_a^x f(t)\,\mathrm{d}t$ existuje pro všechna $x \in [a; b]$;**
> 2. **$\frac{\mathrm{d}}{\mathrm{d}x}\int_a^x f(t)\,\mathrm{d}t = f(x)$ pro všechna $x \in [a; b]$;**
> 3. **$\int_a^x f(t)\,\mathrm{d}t = F(x) - F(a)$, kde $F$ je libovolná primitivní funkce k $f$ na $[a; b]$** (Newtonova–Leibnizova formule, rozdíl se píše $[F(t)]_a^x$).

^veta-fundamentalni

> [!lidsky] Lidsky
> [[fundamentální věta kalkulu|Fundamentální věta]] je shrnutí celé dnešní stavby: integrál existuje (součty), jeho derivace podle horní meze je $f$ (§5) a počítá se rozdílem hodnot libovolné primitivní funkce (§6). Jak primitivní funkce chytře hledat, přijde v dalších přednáškách.

> [!example] Příklad
> $\int_0^2 3x^2\,\mathrm{d}x = [x^3]_0^2 = 8 - 0 = 8$, protože $(x^3)' = 3x^2$. Totéž vyjde s primitivní funkcí $x^3 + 3$: $(8 + 3) - (0 + 3) = 8$; konstanta se odečte.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč je u konvexní funkce s derivací na $\mathbb{R}$ každé lokální minimum globální?
> V lokálním minimu $p$ je **$f'(p) = 0$**, takže tečna je vodorovná přímka $y = f(p)$. Podle lemmatu leží tečna **pod grafem**: $f(x) \ge f(p)$ pro všechna $x$.

> [!karta|02]- Dokaž, že konvexní $f$ s derivací na $\mathbb{R}$ splňuje $f(p) + f'(p)(x - p) \le f(x)$ pro $x < p$.
> Lagrange na $[x; p]$: $\frac{f(x) - f(p)}{x - p} = f'(t)$ pro nějaké $t \in (x; p)$. $f'$ je **neklesající**, $t < p$, tedy $f'(t) \le f'(p)$. Násobení **záporným** $x - p$ otočí nerovnost: $f(x) - f(p) \ge f'(p)(x - p)$.

> [!karta|03]- Jak z nerovnosti „tečna pod grafem“ plyne Jensenova nerovnost?
> Polož $p = \sum a_i x_i$. Pro každé $i$ je $f(x_i) \ge f(p) + f'(p)(x_i - p)$. Vynásob $a_i \ge 0$ a sečti: díky $\sum a_i = 1$ je $\sum a_i (x_i - p) = p - p = 0$, zbude **$\sum a_i f(x_i) \ge f(p)$**.

> [!karta|04]- Proč lemma „lokální minimum je globální“ potřebuje konvexitu? Uveď protipříklad.
> $f(x) = x^3 - 3x$: v $1$ je lokální minimum $f(1) = -2$, ale **$f(-3) = -18$**. Funkce není konvexní ($f'' < 0$ pro $x < 0$), tečna v $1$ graf protíná.

> [!karta|05]- Proč z axiomů integrálu plyne $\int_a^a f = 0$?
> **Aditivita** pro $u = a$, $v = b$: $\int_a^b f = \int_a^a f + \int_a^b f$. Odečtením $\int_a^b f$ vyjde $\int_a^a f = 0$.

> [!karta|06]- Proč z omezenosti plyne: $f \ge 0$ na $[a; b]$ ⇒ $\int_a^b f \ge 0$?
> Z $f \ge 0$ je $\min_{[a; b]} f \ge 0$, a omezenost dává $\int_a^b f \ge (b - a) \cdot \min f \ge 0$ (protože **$b - a \ge 0$**).

> [!karta|07]- Proč se definuje $\int_b^a f = -\int_a^b f$?
> Aby **aditivita platila pro libovolné pořadí mezí**: chceme $\int_b^a f + \int_a^b f = \int_b^b f = 0$, a to vynutí $\int_b^a f = -\int_a^b f$.

> [!karta|08]- Proč v axiomech integrálu nestačí samotná aditivita?
> Aditivitu splňuje i nesmyslné přiřazení **$\int_u^v f := 0$** pro všechno. Až **omezenost** váže číslo k funkci: pro $f = 1$ vynutí $\int_u^v 1 = v - u$.

> [!karta|09]- Jak se dokáže, že $F(x) = \int_a^x f$ má derivaci $f(x)$?
> **Aditivita**: $F(x + h) - F(x) = \int_x^{x+h} f$. **Omezenost**: $\min_{[x; x+h]} f \le \frac{F(x + h) - F(x)}{h} \le \max_{[x; x+h]} f$. Pro $h \to 0^+$ jdou min i max ze **spojitosti** k $f(x)$, **věta o sevření** dá limitu $f(x)$; pro $h \to 0^-$ analogicky.

> [!karta|10]- Jak se dokáže, že pro primitivní funkci $G$ k $f$ platí $(v - u)\min_{[u; v]} f \le G(v) - G(u) \le (v - u)\max_{[u; v]} f$?
> Pro $u < v$ dá **Lagrangeova věta** $t \in (u; v)$ s $\frac{G(v) - G(u)}{v - u} = G'(t) = f(t)$, a $f(t)$ leží mezi minimem a maximem $f$ na $[u; v]$. Vynásob kladným $v - u$. Pro $u = v$ jsou všechny výrazy 0.

> [!karta|11]- Dokaž, že dvě primitivní funkce $F_1, F_2$ k téže $f$ na $[a; b]$ se liší o konstantu.
> $(F_1 - F_2)' = F_1' - F_2' = f - f = 0$ na $[a; b]$, a funkce s **nulovou derivací na intervalu je konstantní** (důsledek Lagrangeovy věty). Tedy $F_1 = F_2 + c$.

> [!karta|12]- Jak najdeš primitivní funkci $G$ k $f$ s $G(x_0) = y_0$, když znáš primitivní $F$, a proč je jediná?
> **$G(x) = F(x) + \bigl(y_0 - F(x_0)\bigr)$**: posunutí o konstantu, takže $G' = f$, a $G(x_0) = y_0$. Jiná taková funkce se od $G$ liší o konstantu $c$, a dosazením $x_0$ vyjde $c = 0$.

> [!karta|13]- Proč je určitý integrál spojité funkce určen jednoznačně (myšlenka)?
> Pro jakékoli přiřazení splňující oba axiomy je $F(x) = \int_a^x f$ **primitivní funkce** k $f$ (derivace podle horní meze) s **$F(a) = 0$**. Primitivní funkce s předepsanou hodnotou v jednom bodě je **jediná**.

> [!karta|14]- Čím se liší primitivní funkce k $f$ a určitý integrál z $f$?
> Primitivní funkce je **funkce** ($G' = f$) a je jich nekonečně mnoho (liší se o konstantu). Určitý integrál $\int_u^v f$ je **číslo** a je jediné; spojuje je $\int_u^v f = G(v) - G(u)$ pro libovolnou primitivní $G$.

> [!karta|15]- Jak souvisí dolní součet, horní součet a integrál a co udělá zjemnění dělení?
> **$L(f; \Delta) \le \int_a^b f \le U(f; \Delta)$** pro každé dělení. Zjemněním dolní součet **neklesne** a horní **nestoupne**; pro spojitou $f$ je $\sup L = \inf U = \int_a^b f$.

### Příklady na procvičení

> [!priklad|16]- Ověř Jensenovu nerovnost pro $f(x) = x^2$, body $0, 2, 4$ a váhy $\tfrac14, \tfrac14, \tfrac12$.
> Vážený průměr bodů: $\tfrac14 \cdot 0 + \tfrac14 \cdot 2 + \tfrac12 \cdot 4 = 2{,}5$, $f(2{,}5) = 6{,}25$. Vážený průměr hodnot: $\tfrac14 \cdot 0 + \tfrac14 \cdot 4 + \tfrac12 \cdot 16 = 9$. **$6{,}25 \le 9$**, nerovnost platí.

> [!priklad|17]- Odvoď z lemmatu o konvexních funkcích (tečna pod grafem) nerovnost pro $f(x) = e^x$ a $p = 0$.
> $e^x$ je konvexní ($f'' = e^x > 0$), $f(0) = f'(0) = 1$. Tečna v $0$: $y = 1 + x$, tedy **$1 + x \le e^x$ pro všechna $x \in \mathbb{R}$**.

> [!priklad|18]- (Gradient descent, navíc) Udělej tři kroky metody pro $f(x) = x^2$, $x_0 = 1$, $\gamma = \tfrac14$.
> $x_{i+1} = x_i - \tfrac14 \cdot 2x_i = \tfrac12 x_i$: **$x_1 = 0{,}5$, $x_2 = 0{,}25$, $x_3 = 0{,}125$**, blíží se k minimu $0$.

> [!priklad|19]- Spočítej $\int_0^2 x\,\mathrm{d}x$ pomocí primitivní funkce a ověř aditivitu pro $u = 1$ a omezenost na $[0; 2]$.
> Primitivní: $\tfrac12 x^2$, takže $\int_0^2 x = 2 - 0 = $ **$2$**, $\int_0^1 x = \tfrac12$, $\int_1^2 x = 2 - \tfrac12 = \tfrac32$. Aditivita: $\tfrac12 + \tfrac32 = 2$. Omezenost: $2 \cdot 0 \le 2 \le 2 \cdot 2$.

> [!priklad|20]- Urči $F(x) = \int_0^x \cos t\,\mathrm{d}t$ a $F'(x)$.
> $\sin$ je primitivní ke $\cos$, takže $F(x) = \sin x - \sin 0 = $ **$\sin x$** a $F'(x) = $ **$\cos x$**, přesně podle věty o derivaci podle horní meze.

> [!priklad|21]- Najdi primitivní funkci $G$ k $f(x) = 2x$ na $[-2; 2]$, pro kterou $G(1) = 5$.
> Všechny primitivní jsou $x^2 + c$; $1 + c = 5$ dá $c = 4$. **$G(x) = x^2 + 4$**, a je jediná.

> [!priklad|22]- Spočítej $L(f; \Delta)$ a $U(f; \Delta)$ pro $f(x) = x^2$ na $[0; 2]$ a dělení $\Delta$: $0 < 1 < 2$.
> Na $[0; 1]$: min $0$, max $1$; na $[1; 2]$: min $1$, max $4$. **$L = 1 \cdot 0 + 1 \cdot 1 = 1$**, **$U = 1 \cdot 1 + 1 \cdot 4 = 5$**. Integrál $\tfrac83 \approx 2{,}67$ je mezi nimi.

> [!priklad|23]- Spočítej $\frac{\mathrm{d}}{\mathrm{d}x}\int_0^x t^2\,\mathrm{d}t$ v bodě $x = 3$.
> Podle věty o derivaci integrálu podle horní meze je derivace rovna integrandu v horní mezi: $3^2 = $ **$9$**. (Kontrola: $\int_0^x t^2 = \tfrac{x^3}{3}$, derivace $x^2$.)

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 2. semestrálnímu testu (J. Velebil, 7.–11. 12. 2026, témata 06A–08A). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|24]- Dokažte nebo vyvraťte: Ať je $f$ spojitá na $[0; 4]$ a $\int_0^4 f(s)\,\mathrm{d}s = 12$. Potom existuje $p \in [0; 4]$ s $f(p) \ge 3$.
> **Tvrzení platí.** Podle omezenosti integrálu je $12 = \int_0^4 f \le (4 - 0) \cdot \max_{t \in [0; 4]} f(t)$, tedy $\max f \ge 3$. Spojitá funkce na $[0; 4]$ maxima nabývá (věta o extrémech), takže existuje $p$ s $f(p) = \max f \ge 3$.

> [!priklad|25]- Dokažte nebo vyvraťte: Je-li $f$ spojitá na $[1; 3]$ a $\int_1^3 f(s)\,\mathrm{d}s = 0$, je $f(x) = 0$ pro všechna $x \in [1; 3]$.
> **Tvrzení neplatí.** Protipříklad $f(x) = x - 2$: primitivní je $\tfrac{x^2}{2} - 2x$, takže $\int_1^3 (x - 2)\,\mathrm{d}x = (4{,}5 - 6) - (0{,}5 - 2) = 0$, ale $f(1) = -1 \ne 0$.

> [!priklad|26]- Pečlivě zformulujte větu o derivaci integrálu jako funkce horní meze (s předpoklady, českými větami).
> Ať je funkce $f$ spojitá na omezeném uzavřeném intervalu $[a; b]$ a pro $x \in [a; b]$ označme $F(x) = \int_a^x f$. Potom **funkce $F$ má derivaci na $[a; b]$** (ve vnitřních bodech, zprava v $a$, zleva v $b$) **a pro všechna $x \in [a; b]$ platí $F'(x) = f(x)$**.

> [!priklad|27]- Najděte stacionární body funkce $x \mapsto \int_0^x (t^2 - 4)\,\mathrm{d}t$ na intervalu $[-3; 3]$.
> Integrand je spojitý, takže podle věty o derivaci podle horní meze je derivace funkce rovna $x^2 - 4$. Ta je nulová v **$x = -2$ a $x = 2$**; oba body leží uvnitř $(-3; 3)$, jsou to tedy stacionární body.

> [!priklad|28]- Pečlivě zformulujte tvrzení o existenci a jednoznačnosti primitivní funkce s předepsanou hodnotou.
> Ať je $f$ spojitá na omezeném uzavřeném intervalu $[a; b]$ a ať $F$ je primitivní funkce k $f$ na $[a; b]$. Potom **pro každé $x_0 \in [a; b]$ a každé $y_0 \in \mathbb{R}$ existuje právě jedna primitivní funkce $G$ k $f$ na $[a; b]$ taková, že $G(x_0) = y_0$**.

---
← [[MA1 10 – Druhá derivace, konvexita a inflexe|22. 10. 2026 Druhá derivace, konvexita a inflexe]]

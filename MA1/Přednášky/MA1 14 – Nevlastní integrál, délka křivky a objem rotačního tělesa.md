---
predmet: MA1
prednaska: 14
datum: 2026-11-11
zdroj: "Handout 7B (Nevlastní integrál), slajdy 2–15; handout 8A (Geometrie a určitý integrál), slajdy 3–10"
tags: [prednaska, MA1]
---

# MA1 14 – Nevlastní integrál, délka křivky a objem rotačního tělesa

*Přednáška 14 · středa 11. 11. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 7B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout07b.pdf) · [Handout 8A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout08a.pdf)

Témata: `∫ₐᵇ f = lim ∫ₐˣ f` · `nevlastní integrál` · `integrál do ±∞` · `konečně mnoho nespojitostí` · `konverguje a diverguje` · `signum nemá primitivní funkci` · `Darbouxova vlastnost` · `obecná věta o určitém integrálu` · `plocha mezi grafy` · `délka křivky` · `objem rotačního tělesa`

Dosud jsme integrovali jen funkce spojité na uzavřeném intervalu $[a; b]$. Dnes se integrál rozšíří limitou: na funkce, které na kraji intervalu „utíkají“ (třeba do nekonečna), na neomezené intervaly a na funkce s konečně mnoha skoky. Druhá část ukazuje, jak z integrálu dostat geometrii: *obecná věta o určitém integrálu* převede požadavky „aditivita + omezenost“ na vzorec pro plochu mezi grafy, délku křivky a objem rotačního tělesa.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| nevlastní integrál | $f$ spojitá na $[a; x]$ pro $x < b$: $\int_a^b f = \lim_{x \to b^-}\int_a^x f$ | $\int_0^1 \frac{\mathrm{d}t}{\sqrt{1-t}} = 2$ |
| integrál na neomezeném intervalu | $\int_a^{+\infty} f = \lim_{x \to +\infty}\int_a^x f$; přes celé $\mathbb{R}$ rozdělit v $c$ | $\int_1^{+\infty} \frac{\mathrm{d}t}{t^2} = 1$ |
| integrál funkce s konečně mnoha nespojitostmi | rozdělit v bodech nespojitosti a sečíst | $\int_{-1}^{1}\operatorname{signum} = 0$ |
| konvergentní integrál | vyjde reálné číslo = konverguje; $\pm\infty$ nebo neexistuje = diverguje | $\int_0^1 \frac{\mathrm{d}t}{t} = +\infty$ diverguje |
| funkce signum | $-1$, $0$, $1$ podle znaménka $x$ | integrál má, primitivní funkci ne |
| Darbouxova vlastnost | $f$ nabývá všech hodnot mezi $f(a)$ a $f(b)$ | spojité funkce ano, signum ne |
| Darbouxova věta | má-li $f$ primitivní funkci, má Darbouxovu vlastnost | signum primitivní funkci nemá |
| obecná věta o určitém integrálu | aditivní $G$ sevřené odhady s min a max $\Rightarrow$ $G = \int (g \star h)$ | zdroj všech vzorců níže |
| obsah plochy mezi grafy | $f \geq g$: $\int_a^b (f - g)$ | $x + 2$ a $x^2$: $\frac{9}{2}$ |
| délka křivky | $L = \int_a^b \sqrt{1 + (f'(t))^2}\,\mathrm{d}t$ | $\frac{2}{3}x^{3/2}$ na $[0; 3]$: $\frac{14}{3}$ |
| objem rotačního tělesa | $V = \int_a^b \pi (f(t))^2\,\mathrm{d}t$ | koule: $\frac{4}{3}\pi r^3$ |

## §1 Integrál jako limita: omezený interval (handout 7B)

Výchozí bod je [[fundamentální věta kalkulu]]: pro $f$ [[spojitost na intervalu|spojitou]] na $[a; b]$ je $\int_a^b f = F(b) - F(a)$, kde $F$ je [[primitivní funkce]] k $f$. Funkce $F$ má derivaci, je tedy spojitá, a proto $F(b) = \lim_{x \to b^-} F(x)$. Totéž tedy jde zapsat limitou (slajd 3):

$$
\int_a^b f = \lim_{x \to b^-}\int_a^x f = \lim_{x \to a^+}\int_x^b f.
$$

Pravá strana ale dává smysl i tehdy, když $f$ v bodě $b$ spojitá není, nebo tam vůbec není definovaná. Stačí, aby existovaly integrály $\int_a^x f$ pro $x < b$ a jejich [[jednostranná limita]].

> [!definice] Definice · handout 7B, slajd 4 (nevlastní integrál)
> Ať je $f$ spojitá na každém intervalu $[a; x]$, kde $a \leq x < b$. Pak definujeme
>
> $$
> \int_a^b f = \lim_{x \to b^-}\int_a^x f,
> $$
>
> pokud tato limita existuje (vlastní, nebo [[nevlastní limita|nevlastní]]). Analogicky pro $f$ spojitou na každém $[x; b]$ s $a < x \leq b$: $\int_a^b f = \lim_{x \to a^+}\int_x^b f$.

^def-nevlastni-integral

> [!lidsky] Lidsky
> Když funkce u kraje intervalu „utíká“ (do nekonečna, nebo tam není definovaná), kraj nejdřív o kousek odsuneš, spočítáš obyčejný integrál a pak kraj pomalu vracíš limitou. Výsledek může být číslo, $\pm\infty$, nebo limita nemusí existovat vůbec.

> [!example] Příklad (slajdy 5–7)
> - $\int_0^1 \frac{\mathrm{d}t}{\sqrt{1 - t}}$: funkce je spojitá na $[0; x]$ pro $x < 1$ a $\int_0^x \frac{\mathrm{d}t}{\sqrt{1 - t}} = \left[-2\sqrt{1 - t}\right]_0^x = 2 - 2\sqrt{1 - x} \to 2$ pro $x \to 1^-$. **Integrál je $2$**, i když funkce u jedničky roste nade všechny meze.
> - $\int_0^1 \frac{\mathrm{d}t}{t}$: pro $0 < x \leq 1$ je $\int_x^1 \frac{\mathrm{d}t}{t} = -\ln x \to +\infty$ pro $x \to 0^+$. **Integrál je $+\infty$.**
> - $\int_{-1/\pi}^{0} \frac{1}{t^2}\cos\frac{1}{t}\,\mathrm{d}t$: primitivní funkce je $-\sin\frac{1}{t}$ a $\lim_{x \to 0^-}\sin\frac{1}{x}$ neexistuje (podle [[Heineova věta|Heineovy věty]] stačí dvě posloupnosti jdoucí k $0$ zleva s různými limitami hodnot). **Integrál neexistuje.**
> - Nepříklad: $\int_0^1 \sin\frac{1}{t}\,\mathrm{d}t$ by šel touto definicí také, ale $\int_0^1 t^2\,\mathrm{d}t$ nové definice nepotřebuje: pro spojitou funkci dá limita totéž, co [[určitý integrál]].

> [!obrazek] Nevlastní integrál jako limita ploch
> ![[ma114-nevlastni-integral.png]]
> *Vlevo modrá plocha pod $\frac{1}{\sqrt{1 - t}}$ od $0$ do oranžového $x$; když se $x$ blíží k červené mezi $1$, plocha roste k $2$. Vpravo zelená plocha pod $\frac{1}{t}$ od oranžového $x$ do $1$; když se $x$ blíží k červené $0$, plocha roste nade všechny meze.*

> [!pozor] Nevlastní integrál nejde spočítat přímým dosazením mezí
> $\int_0^1 \frac{\mathrm{d}t}{t} = [\ln t]_0^1$ je nesmysl: $\ln 0$ neexistuje a fundamentální větu nejde použít, protože $\frac{1}{t}$ není spojitá na celém $[0; 1]$. Vždy nejdřív integruj do $x$ a pak počítej limitu. Stejně tak $\int_{-1}^1 \frac{\mathrm{d}t}{t^2}$ „tabulkou“ dá $-2$, ale integrál kladné funkce je $+\infty$ (rozděl v nule, viz §3).

## §2 Neomezený interval

> [!definice] Definice · handout 7B, slajdy 8 a 9 (integrál na neomezeném intervalu)
> Ať je $f$ spojitá na $[a; +\infty)$. Pak definujeme
>
> $$
> \int_a^{+\infty} f = \lim_{x \to +\infty}\int_a^x f,
> $$
>
> pokud limita existuje. Analogicky pro $f$ spojitou na $(-\infty; b]$: $\int_{-\infty}^b f = \lim_{x \to -\infty}\int_x^b f$.
>
> Ať je $f$ spojitá na $\mathbb{R}$ a $c \in \mathbb{R}$. Pokud součet napravo dává smysl, definujeme
>
> $$
> \int_{-\infty}^{+\infty} f = \int_{-\infty}^{c} f + \int_{c}^{+\infty} f.
> $$
>
> Hodnota nezávisí na volbě $c$.

^def-integral-neomezeny-interval

> [!lidsky] Lidsky
> Plocha „až do nekonečna“: integruješ do $x$ a necháš $x$ utéct. Nekonečně dlouhý pás může mít konečnou plochu, pokud funkce klesá k nule dost rychle. Přes celou přímku se integrál rozdělí v libovolném bodě a každá polovina se počítá zvlášť.

> [!example] Příklad
> - $\int_1^{+\infty}\frac{\mathrm{d}t}{t^2} = \lim_{x \to +\infty}\left(1 - \frac{1}{x}\right) = 1$, ale $\int_1^{+\infty}\frac{\mathrm{d}t}{t} = \lim_{x \to +\infty}\ln x = +\infty$.
> - $\int_{-\infty}^{+\infty}\frac{\mathrm{d}t}{1 + t^2} = \lim_{x \to -\infty}(\arctan 0 - \arctan x) + \lim_{x \to +\infty}(\arctan x - \arctan 0) = \frac{\pi}{2} + \frac{\pi}{2} = \pi$ (s $c = 0$).
> - Slajd 10: $\int_0^{+\infty} e^{-t}\sin t\,\mathrm{d}t$. [[per partes se zacyklením|Per partes dvakrát]] dá $\int_0^x e^{-t}\sin t\,\mathrm{d}t = \frac{1}{2} - \frac{e^{-x}(\sin x + \cos x)}{2}$; zlomek jde k $0$ (omezená krát nulová), takže integrál je **$\frac{1}{2}$**.

> [!obrazek] Dvě funkce jdoucí k nule, jen jedna konečná plocha
> ![[ma114-neomezeny-interval.png]]
> *Modrá $\frac{1}{t^2}$ klesá dost rychle a modrá plocha od $1$ do nekonečna je $1$. Oranžová $\frac{1}{t}$ klesá pomaleji a světle oranžový pás mezi grafy přidá nekonečnou plochu: $\int_1^{+\infty}\frac{\mathrm{d}t}{t} = +\infty$.*

> [!pozor] Ne symetrickou limitou
> $\int_{-\infty}^{+\infty} f$ není $\lim_{x \to +\infty}\int_{-x}^{x} f$. Pro $f(t) = t$ je $\int_{-x}^{x} t\,\mathrm{d}t = 0$ pro každé $x$, ale $\int_0^{+\infty} t = +\infty$ a $\int_{-\infty}^0 t = -\infty$, součet $+\infty + (-\infty)$ smysl nedává a integrál **neexistuje**. Obě poloviny se musí spočítat zvlášť.

> [!navic] Proč nezáleží na $c$
> Pro $c_1 < c_2$ je podle [[aditivita integrálu|aditivity]] $\int_{-\infty}^{c_2} f = \int_{-\infty}^{c_1} f + \int_{c_1}^{c_2} f$ a $\int_{c_1}^{+\infty} f = \int_{c_1}^{c_2} f + \int_{c_2}^{+\infty} f$ (aditivita platí pro $\int_a^x$ a přechází do limity). Konečné číslo $\int_{c_1}^{c_2} f$ se jen přesune z jednoho sčítance do druhého, takže součet je stejný.

## §3 Funkce s konečně mnoha nespojitostmi

> [!definice] Definice · handout 7B, slajd 11 (integrál funkce s konečně mnoha nespojitostmi)
> Ať $f$ není spojitá v bodech $x_1 < x_2 < \dots < x_k$ intervalu $[a; b]$ a jinde na $[a; b]$ spojitá je. Pak definujeme
>
> $$
> \int_a^b f = \int_a^{x_1} f + \int_{x_1}^{x_2} f + \dots + \int_{x_k}^{b} f,
> $$
>
> kde každý sčítanec je [[nevlastní integrál]] ve smyslu §1, pokud součet dává smysl. Analogicky pro neomezené intervaly.

^def-integral-nespojitosti

> [!lidsky] Lidsky
> Interval rozřízneš v místech, kde funkce skáče, na každém kousku spočítáš integrál (u skoku limitou) a výsledky sečteš. Co funkce dělá v samotném bodě skoku, je jedno: bod nemá šířku.

> [!example] Příklad (slajd 12)
> $f(x) = -1$ pro $-1 \leq x < 0$ a $f(x) = \sin x$ pro $0 \leq x \leq \pi$. Nespojitost je jen v $0$:
>
> $$
> \int_{-1}^{\pi} f = \lim_{x \to 0^-}\int_{-1}^{x}(-1)\,\mathrm{d}t + \int_0^{\pi}\sin t\,\mathrm{d}t = \lim_{x \to 0^-}(-x - 1) + [-\cos t]_0^{\pi} = -1 + 2 = 1.
> $$

Výsledek nevlastního integrálu má jméno podle toho, jak dopadla limita (slajd 13):

> [!definice] Definice · handout 7B, slajd 13 (konvergence a divergence)
> Integrál $\int_a^b f$ ve smyslu předchozích definic **konverguje**, je-li jeho hodnota reálné číslo. **Diverguje**, je-li roven $+\infty$ nebo $-\infty$, nebo pokud neexistuje.

^def-konvergence-integralu

> [!lidsky] Lidsky
> Konverguje = vyšlo konečné číslo. Všechno ostatní (nekonečno, nebo limita vůbec neexistuje) je divergence.

> [!example] Příklad
> $\int_0^1 \frac{\mathrm{d}t}{\sqrt{1 - t}} = 2$ a $\int_1^{+\infty}\frac{\mathrm{d}t}{t^2} = 1$ konvergují. $\int_0^1 \frac{\mathrm{d}t}{t} = +\infty$ diverguje, $\int_{-1/\pi}^0 \frac{1}{t^2}\cos\frac{1}{t}\,\mathrm{d}t$ neexistuje, také diverguje.

> [!pozor] Limita funkce nerozhoduje
> Ani $f \to +\infty$ u kraje neznamená divergenci ($\frac{1}{\sqrt{1 - t}}$ na $[0; 1)$ má integrál $2$), ani $f \to 0$ v nekonečnu neznamená konvergenci ($\frac{1}{t}$ na $[1; +\infty)$ má integrál $+\infty$). Rozhoduje, jak rychle.

## §4 Signum a Darbouxova vlastnost

> [!definice] Definice · handout 7B, slajd 14 (funkce signum)
> $$
> \operatorname{signum}(x) = \begin{cases} -1, & x < 0,\\ 0, & x = 0,\\ 1, & x > 0. \end{cases}
> $$

^def-signum

> [!lidsky] Lidsky
> Signum vrátí jen znaménko čísla. V nule má skok, a proto ukazuje, že mít integrál a mít primitivní funkci není totéž.

> [!example] Příklad (slajd 14)
> $\operatorname{signum}(-3{,}7) = -1$, $\operatorname{signum}(0) = 0$, $\operatorname{signum}(\pi) = 1$. Integrál podle §3: $\int_{-1}^{1}\operatorname{signum} = \lim_{x \to 0^-}\int_{-1}^{x}(-1) + \lim_{x \to 0^+}\int_x^1 1 = -1 + 1 = 0$. Integrál tedy existuje, ale funkci $F$ s $F' = \operatorname{signum}$ na $[-1; 1]$ najít nejde.

Proč primitivní funkce neexistuje, ukazuje vlastnost, kterou každá derivace má:

> [!definice] Definice · handout 7B, slajd 15 (Darbouxova vlastnost)
> Funkce $f$ má na $[a; b]$ **Darbouxovu vlastnost**, jestliže pro každé $r$ ležící mezi $f(a)$ a $f(b)$ existuje $t \in [a; b]$ takové, že $f(t) = r$.

^def-darbouxova-vlastnost

> [!lidsky] Lidsky
> Funkce na cestě z $f(a)$ do $f(b)$ nevynechá žádnou hodnotu, nemůže „přeskočit“.

> [!example] Příklad
> $f(x) = x^2$ na $[0; 2]$ ji má, třeba hodnotu $3$ mezi $f(0) = 0$ a $f(2) = 4$ nabývá v $t = \sqrt{3}$. Funkce signum na $[-1; 1]$ ji nemá: hodnotu $\frac{1}{2}$ mezi $-1$ a $1$ nenabývá nikde.

> [!veta] Darbouxova věta · handout 7B, slajd 15
> ==Ať $F$ je primitivní funkce k $f$ na $[a; b]$, tj. $F' = f$ na $[a; b]$.== Potom **$f$ má na $[a; b]$ Darbouxovu vlastnost**.
>
> > [!note]- Důkaz
> > Ať například $f(a) < r < f(b)$ (pro $r = f(a)$ nebo $r = f(b)$ stačí $t = a$ nebo $t = b$; opačné pořadí je symetrické). Položme $H(x) = F(x) - rx$. Pak $H' = f - r$, takže $H'(a) < 0$ a $H'(b) > 0$. Funkce $H$ má derivaci, je tedy spojitá a podle [[věta o největší a nejmenší hodnotě|věty o největší a nejmenší hodnotě]] nabývá na $[a; b]$ minima v nějakém bodě $t$. Z $H'(a) < 0$ plyne $H(x) < H(a)$ pro $x$ kousek napravo od $a$, takže $t \neq a$; z $H'(b) > 0$ plyne $H(x) < H(b)$ pro $x$ kousek nalevo od $b$, takže $t \neq b$. Bod $t$ leží uvnitř a podle [[nutná podmínka lokálního extrému|nutné podmínky lokálního extrému]] je $H'(t) = 0$, tedy $f(t) = r$.

^veta-darbouxova

> [!lidsky] Lidsky
> Spojité funkce „nepřeskakují hodnoty“ ([[věta o mezihodnotě]]). Derivace spojitá být nemusí, ale přeskakovat hodnoty nesmí ani ona. Funkce se skokem proto nemůže být derivací ničeho.

> [!example] Příklad
> $x^2$ na $[1; 3]$ je spojitá, Darbouxovu vlastnost má: nabude každou hodnotu mezi $1$ a $9$, třeba $5$ v $t = \sqrt{5}$. Signum na $[-1; 1]$ ji nemá: $\frac{1}{2}$ leží mezi $-1$ a $1$, ale signum ji nenabývá. Podle Darbouxovy věty tedy signum **nemá primitivní funkci** na $[-1; 1]$.

> [!obrazek] Signum přeskočí hodnotu $\frac{1}{2}$
> ![[ma114-signum.png]]
> *Modrý graf signa: $-1$ vlevo, plný bod $0$ v nule, $1$ vpravo (prázdné kroužky = hodnoty, které se v nule nenabývají). Červená čárkovaná hladina $r = \frac{1}{2}$ graf nikde neprotne. Zelené plochy $-1$ a $+1$ dávají $\int_{-1}^1\operatorname{signum} = 0$.*

> [!navic] Integrál vs. primitivní funkce
> Pro **spojitou** $f$ existují oba ([[fundamentální věta kalkulu]]). Pro funkci s konečně mnoha skoky integrál podle §3 existovat může, primitivní funkce na celém intervalu ale ne. Takový integrál se počítá rozdělením a limitami, ne jako $F(b) - F(a)$ přes celý interval. Kdo chce do hloubky: I. M. Roussos, *Improper Riemann Integrals* (doporučení ze slajdu 15, nepovinné).

## §5 Obecná věta o určitém integrálu (handout 8A)

[[určitý integrál|Určitý integrál]] spojité funkce je jediná veličina, která splňuje dva axiomy (slajd 3): [[aditivita integrálu|aditivitu]] $\int_a^v f = \int_a^u f + \int_u^v f$ a [[omezenost integrálu|omezenost]] $(v - u)\min f \leq \int_u^v f \leq (v - u)\max f$ na $[u; v]$. Obecná věta to zobecní: kdykoli se nějaká geometrická nebo fyzikální veličina sčítá po kouscích a na každém kousku jde sevřít stejným vzorcem s minimy a maximy, je to integrál.

Velebil píše $\overset{v}{\underset{u}{G}}$ pro hodnotu veličiny $G$ na kousku od $u$ do $v$ (jako $\int_u^v$).

> [!veta] Věta · handout 8A, slajd 4 (obecná věta o určitém integrálu)
> ==Ať $g$, $h$ jsou spojité na $[a; b]$, $\star$ je algebraická operace (třeba $g \cdot h$ nebo $\sqrt{g + h^2}$) a $g \star h$ je spojitá na $[a; b]$. Ať pro všechna $u \leq v$ z $[a; b]$ platí==
> 1. ==aditivita: $\overset{v}{\underset{a}{G}} = \overset{u}{\underset{a}{G}} + \overset{v}{\underset{u}{G}}$,==
> 2. ==omezenost: $(v - u)\cdot\left((A\,g) \star (B\,h)\right) \leq \overset{v}{\underset{u}{G}} \leq (v - u)\cdot\left((C\,g) \star (D\,h)\right)$, kde $A, B, C, D \in \{\min, \max\}$ jsou brané přes $[u; v]$.==
>
> Potom **$\overset{b}{\underset{a}{G}} = \int_a^b (g \star h)$**.
>
> > [!note]- Důkaz (náznak)
> > Ukáže se, že $x \mapsto \overset{x}{\underset{a}{G}}$ je primitivní funkce k $g \star h$. Z aditivity je $\frac{1}{\delta}\left(\overset{x+\delta}{\underset{a}{G}} - \overset{x}{\underset{a}{G}}\right) = \frac{1}{\delta}\overset{x+\delta}{\underset{x}{G}}$ a podle omezenosti leží mezi $(A\,g) \star (B\,h)$ a $(C\,g) \star (D\,h)$ na $[x; x + \delta]$. Pro $\delta \to 0$ jdou minima i maxima spojitých $g$, $h$ k hodnotám $g(x)$, $h(x)$, takže obě meze jdou k $g(x) \star h(x)$ a podle [[věta o sevření|věty o sevření]] je derivace $g(x) \star h(x)$. Pak podle fundamentální věty $\overset{b}{\underset{a}{G}} = \overset{b}{\underset{a}{G}} - \overset{a}{\underset{a}{G}} = \int_a^b (g \star h)$ (z aditivity $\overset{a}{\underset{a}{G}} = 0$).

^veta-obecna

> [!lidsky] Lidsky
> Recept na vzorce: (1) veličina se sčítá po kouscích, (2) na každém kousku ji umíš odhadnout zespoda a shora „obdélníkem“ s nejmenší a největší hodnotou. Pak je to integrál z toho, co je v odhadu napsané mezi $\min$ a $\max$.

> [!example] Příklad
> Pro $\star$ = součin, $g = 1$, $h = f$ a $A = B = \min$, $C = D = \max$ je to přesně axiomatika integrálu: $G = \int f$. Pro plochu mezi grafy $f \geq g$ je $\star = -$ a obsah nad $[u; v]$ leží mezi obdélníky s výškou $\min f - \max g$ a $\max f - \min g$, takže obsah je $\int_a^b (f - g)$.

> [!veta] Důsledek · handout 8A, slajd 4 (obsah plochy mezi grafy)
> ==Ať $f$, $g$ jsou spojité na $[a; b]$ a $f \geq g$ na $[a; b]$.== Potom obsah plochy mezi grafy $f$ a $g$ nad $[a; b]$ je
>
> $$
> \mathbf{A(f, g) = \int_a^b (f - g)}.
> $$
>
> (Obecná věta s $\star = -$, $A = \min$, $B = \max$, $C = \max$, $D = \min$.)

^veta-plocha-mezi-grafy

> [!lidsky] Lidsky
> Plocha pod horní křivkou minus plocha pod dolní. Nejdřív je potřeba zjistit, která je nahoře; kde se grafy kříží, interval se rozdělí.

> [!example] Příklad
> $x + 2$ a $x^2$: průsečíky z $x^2 = x + 2$ jsou $-1$ a $2$, v $0$ je $2 > 0$, takže přímka je nahoře. Obsah je $\int_{-1}^{2}(x + 2 - x^2)\,\mathrm{d}x = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2} = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}$. Pro $\sin$ na $[0; 2\pi]$ a osu $x$ by „slepý“ integrál dal $0$; obsah je $\int_0^{\pi}\sin - \int_{\pi}^{2\pi}\sin = 4$.

## §6 Délka křivky

Délku grafu $f$ od $u$ do $v$ značíme $\overset{v}{\underset{u}{L}}(f)$. Požadavky (slajdy 5–6): délka je aditivní, úsečka $y = px + q$ nad $[u; v]$ má délku $(v - u)\sqrt{1 + p^2}$ (Pythagorova věta: odvěsny $v - u$ a $p(v - u)$) a kousek grafu je sevřený mezi délkami úseček s nejmenší a největší strmostí na $[u; v]$.

> [!definice] Definice · handout 8A, slajdy 6 a 7 (délka křivky)
> Ať $f$ je spojitá a má spojitou derivaci $f'$ na $[a; b]$. Na každém $[u; v] \subseteq [a; b]$ označme $m = \min |f'|$ a $M = \max |f'|$; délka splňuje odhad
>
> $$
> \sqrt{1 + m^2}\,(v - u) \leq \overset{v}{\underset{u}{L}}(f) \leq \sqrt{1 + M^2}\,(v - u).
> $$
>
> Z obecné věty (s $g = 1$, $h = |f'|$, $g \star h = \sqrt{g + h^2}$, $A = B = \min$, $C = D = \max$) je délka grafu $f$ od $a$ do $b$
>
> $$
> \mathbf{L(f) = \int_a^b \sqrt{1 + (f'(t))^2}\,\mathrm{d}t}.
> $$

^def-delka-krivky

> [!lidsky] Lidsky
> Na malém kousku vypadá graf jako úsečka se sklonem $f'(t)$. Úsečka nad šířkou $\mathrm{d}t$ má podle Pythagorovy věty délku $\sqrt{1 + f'(t)^2}\,\mathrm{d}t$. Integrál tyhle kousky sečte.

> [!example] Příklad
> - $f(x) = \frac{2}{3}x^{3/2}$ na $[0; 3]$: $f'(x) = \sqrt{x}$, $L = \int_0^3\sqrt{1 + t}\,\mathrm{d}t = \left[\frac{2}{3}(1 + t)^{3/2}\right]_0^3 = \frac{2}{3}(8 - 1) = \frac{14}{3}$.
> - Kontrola na přímce $y = 2x$ na $[0; 1]$: $L = \int_0^1\sqrt{1 + 4} = \sqrt{5}$, přesně přepona trojúhelníku s odvěsnami $1$ a $2$.
> - Slajd 7: $x^{3/2}$ na $[1; 4]$: $L = \int_1^4\sqrt{1 + \frac{9t}{4}}\,\mathrm{d}t = \frac{8}{27}\left[\left(1 + \frac{9t}{4}\right)^{3/2}\right]_1^4 = \frac{80\sqrt{10} - 13\sqrt{13}}{27} \approx 7{,}63$.

> [!pozor] Odhad přes $\min |f'|$, ne přes $\min f'$
> Délka úsečky závisí jen na **absolutní hodnotě** sklonu: klesající úsečka se sklonem $-2$ je stejně dlouhá jako stoupající se sklonem $2$. Odhad s $\min f'$ a $\max f'$ proto neplatí, když $f'$ mění znaménko. Pro $f(x) = x^2$ na $[-1; 1]$ je $\min f' = -2$ a „dolní odhad“ $\sqrt{1 + (-2)^2}\cdot 2 = 2\sqrt{5} \approx 4{,}47$ je větší než skutečná délka $\approx 2{,}96$. Správně $m = \min |f'| = 0$, $M = \max |f'| = 2$: $2 \leq L \leq 2\sqrt{5}$. Samotný vzorec $\int_a^b\sqrt{1 + (f')^2}$ to neovlivní, protože $(f')^2 = |f'|^2$.

> [!obrazek] Délka kousku grafu a správný odhad
> ![[ma114-delka-krivky.png]]
> *Vlevo modrý graf $\frac{2}{3}x^{3/2}$, zelená odvěsna $\Delta$, oranžová $p\Delta$ a červená čárkovaná přepona s délkou $\Delta\sqrt{1 + p^2}$. Vpravo $x^2$ na $[-1; 1]$: zelené sloupce jsou správné odhady s $\min |f'|$ a $\max |f'|$, modrý skutečná délka, červený chybný „dolní“ odhad s $\min f' = -2$, který je nad skutečnou délkou.*

## §7 Objem rotačního tělesa

Objem tělesa, které vznikne rotací grafu nezáporné $f$ nad $[u; v]$ kolem osy $x$, značíme $\overset{v}{\underset{u}{V}}(f)$. Požadavky (slajd 8): aditivita a omezenost $\pi(\min f)^2(v - u) \leq \overset{v}{\underset{u}{V}}(f) \leq \pi(\max f)^2(v - u)$, tedy těleso leží mezi vepsaným a opsaným válcem.

> [!definice] Definice · handout 8A, slajd 9 (objem rotačního tělesa)
> Ať $f \geq 0$ je spojitá na $[a; b]$. Objem tělesa vzniklého rotací grafu $f$ od $a$ do $b$ kolem osy $x$ je (obecná věta s $g = \pi$, $h = f$, $g \star h = g \cdot h^2$)
>
> $$
> \mathbf{V(f) = \int_a^b \pi\,(f(t))^2\,\mathrm{d}t}.
> $$

^def-objem-rotacniho-telesa

> [!lidsky] Lidsky
> Těleso rozkrájíš kolmo na osu na tenké kotouče. Kotouč v bodě $t$ má poloměr $f(t)$, tedy obsah $\pi f(t)^2$, a objem $\pi f(t)^2\,\mathrm{d}t$. Integrál kotouče sečte.

> [!example] Příklad
> - $\sqrt{x}$ na $[0; 4]$: $V = \pi\int_0^4 t\,\mathrm{d}t = 8\pi \approx 25{,}13$.
> - Koule (slajd 10): $f(x) = \sqrt{r^2 - x^2}$ na $[-r; r]$, $V = \pi\int_{-r}^{r}(r^2 - t^2)\,\mathrm{d}t = \pi\left(2r^3 - \frac{2r^3}{3}\right) = \frac{4}{3}\pi r^3$.
> - Kužel: $f(x) = \frac{r}{h}x$ na $[0; h]$, $V = \pi\frac{r^2}{h^2}\cdot\frac{h^3}{3} = \frac{1}{3}\pi r^2 h$.

> [!obrazek] Rotační těleso mezi válci
> ![[ma114-rotacni-teleso.png]]
> *Modrý graf $\sqrt{x}$ a jeho tečkovaný zrcadlový obraz ohraničují řez tělesem. Oranžové elipsy jsou kruhové řezy s poloměrem $f(t)$. Na kousku $[u; v]$ leží těleso mezi zeleným vepsaným válcem (poloměr $\min f$) a červeným čárkovaným opsaným válcem (poloměr $\max f$).*

> [!pozor] $\pi f^2$, ne $\pi f$
> Řez tělesem je kruh, takže se integruje jeho obsah $\pi f(t)^2$. $\int \pi f$ nemá ani rozměr objemu (délka krát délka). Kontrola na válci $f = r$ na $[0; h]$: $\int_0^h \pi r^2 = \pi r^2 h$.

> [!navic] Torricelliho trumpeta (slajd 17)
> Stejnou úvahou (slajdy 11–13) vyjde obsah pláště $S = \int_a^b 2\pi f\sqrt{1 + (f')^2}$. Pro $f(t) = \frac{1}{t}$ na $[1; +\infty)$ je objem nevlastní integrál $\int_1^{+\infty}\frac{\pi}{t^2}\,\mathrm{d}t = \pi$, ale plášť $S \geq \int_1^{+\infty}\frac{2\pi}{t}\,\mathrm{d}t = +\infty$. Těleso s konečným objemem a nekonečným povrchem: nevlastní integrál z §2 v praxi.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč pro $f$ spojitou na $[a; b]$ platí $\int_a^b f = \lim_{x \to b^-}\int_a^x f$?
> $\int_a^x f = F(x) - F(a)$ pro primitivní $F$. Ta má derivaci, je tedy **spojitá, v $b$ zleva**: $\lim_{x \to b^-}F(x) = F(b)$. Limita je proto $F(b) - F(a) = \int_a^b f$. Nová definice tak pro spojité funkce dává **totéž** co dřív.

> [!karta|02]- Proč nejde $\int_0^1 \frac{\mathrm{d}t}{t}$ spočítat přímo jako $[\ln t]_0^1$?
> $\frac{1}{t}$ **není spojitá na $[0; 1]$** (v 0 není definovaná) a $\ln 0$ neexistuje, takže fundamentální věta nejde použít. Správně: $\int_x^1 \frac{\mathrm{d}t}{t} = -\ln x \to +\infty$ pro $x \to 0^+$, integrál **diverguje**.

> [!karta|03]- Proč se $\int_{-\infty}^{+\infty} f$ nedefinuje jako $\lim_{x \to +\infty}\int_{-x}^{x} f$?
> Symetrická limita by „vyrušila“ nekonečna: pro $f(t) = t$ je $\int_{-x}^{x} t = 0$, ale **$\int_0^{+\infty} t = +\infty$ a $\int_{-\infty}^0 t = -\infty$**. Definice žádá, aby součet $\int_{-\infty}^c f + \int_c^{+\infty} f$ dával smysl, a ten tu nedává: integrál **neexistuje**.

> [!karta|04]- Proč u $\int_{-\infty}^{+\infty} f = \int_{-\infty}^{c} f + \int_{c}^{+\infty} f$ nezáleží na volbě $c$?
> Díky **aditivitě**: pro $c_1 < c_2$ je $\int_{-\infty}^{c_2} f = \int_{-\infty}^{c_1} f + \int_{c_1}^{c_2} f$ a $\int_{c_1}^{+\infty} f = \int_{c_1}^{c_2} f + \int_{c_2}^{+\infty} f$. Prostřední kus je **konečné číslo**, takže se přesune z jednoho sčítance do druhého a součet se nezmění.

> [!karta|05]- Jak se počítá $\int_a^b f$, když $f$ má skok v bodě $x_1 \in (a; b)$, a záleží na hodnotě $f(x_1)$?
> **Rozdělí se:** $\int_a^b f = \int_a^{x_1} f + \int_{x_1}^b f$, každý kus jako limitu u kraje se skokem. Na hodnotě $f(x_1)$ **nezáleží**, bod má nulovou šířku; integrál se nezmění, ani když $f$ v jednom bodě předefinuješ.

> [!karta|06]- Dokaž, že signum nemá na $[-1; 1]$ primitivní funkci.
> Kdyby $F' = \operatorname{signum}$, měla by podle **Darbouxovy věty** funkce signum Darbouxovu vlastnost. Ale $\frac{1}{2}$ leží mezi $\operatorname{signum}(-1) = -1$ a $\operatorname{signum}(1) = 1$ a **signum hodnoty $\frac{1}{2}$ nenabývá**. Spor.

> [!karta|07]- Jaký je vztah mezi existencí $\int_a^b f$ a existencí primitivní funkce k $f$ na $[a; b]$?
> Pro **spojitou** $f$ existují obě (fundamentální věta). Pro nespojitou ne: **$\int_{-1}^{1}\operatorname{signum} = 0$ existuje, primitivní funkce ne**. Takový integrál se počítá rozdělením a limitami, ne jako $F(b) - F(a)$ přes celý interval.

> [!karta|08]- Proč je $x \mapsto \overset{x}{\underset{a}{G}}$ z obecné věty primitivní k $g \star h$ (myšlenka důkazu)?
> Z aditivity je $\frac{G(x + \delta) - G(x)}{\delta} = \frac{1}{\delta}\overset{x+\delta}{\underset{x}{G}}$ a podmínka 2 ho **sevře** mezi $(A\,g) \star (B\,h)$ a $(C\,g) \star (D\,h)$ na $[x; x + \delta]$. Pro $\delta \to 0$ jdou min i max k hodnotám v $x$, ze **spojitosti** obě meze k $g(x) \star h(x)$, takže derivace je $g(x) \star h(x)$.

> [!karta|09]- Jak z obecné věty vyjde vzorec pro plochu mezi grafy $f \geq g$? Které min a max se zvolí?
> Plocha nad $[u; v]$ je aspoň obdélník výšky **$\min f - \max g$** a nejvýš obdélník výšky **$\max f - \min g$**. To je obecná věta s $\star = -$, $A = \min$, $B = \max$, $C = \max$, $D = \min$, tedy **$A(f, g) = \int_a^b (f - g)$**.

> [!karta|10]- Proč je ve vzorci pro délku křivky $\sqrt{1 + (f')^2}$?
> Úsečka se sklonem $p$ nad intervalem délky $\Delta$ má podle **Pythagorovy věty** délku $\sqrt{\Delta^2 + (p\Delta)^2} = \Delta\sqrt{1 + p^2}$; záleží jen na $p^2$, ne na znaménku sklonu. Kousek grafu, kde $m \leq \lvert f' \rvert \leq M$, má proto délku mezi $\Delta\sqrt{1 + m^2}$ a $\Delta\sqrt{1 + M^2}$ (odhad přes $\min f'$ a $\max f'$ by při změně znaménka $f'$ neplatil) a obecná věta dá **$L = \int_a^b\sqrt{1 + (f')^2}$**.

> [!karta|11]- Proč je objem rotačního tělesa $\int_a^b \pi f^2$, a ne $\int_a^b \pi f$?
> Řez tělesem kolmo na osu je **kruh s poloměrem $f(t)$** a obsahem $\pi f(t)^2$. Kousek tělesa nad $[u; v]$ leží mezi válci $\pi(\min f)^2(v - u)$ a $\pi(\max f)^2(v - u)$; obecná věta s $g \star h = g \cdot h^2$ dá $\int \pi f^2$. ($\pi f$ nemá ani jednotku objemu.)

### Příklady na procvičení

> [!priklad|12]- Spočítej $\int_0^1 \frac{\mathrm{d}t}{\sqrt{t}}$, nebo rozhodni, že diverguje.
> Pro $0 < x \leq 1$: $\int_x^1 t^{-1/2}\,\mathrm{d}t = \left[2\sqrt{t}\right]_x^1 = 2 - 2\sqrt{x} \to 2$ pro $x \to 0^+$. **Konverguje, $\int_0^1 \frac{\mathrm{d}t}{\sqrt{t}} = 2$.**

> [!priklad|13]- Spočítej $\int_0^{+\infty} e^{-2t}\,\mathrm{d}t$.
> $\int_0^x e^{-2t}\,\mathrm{d}t = \left[-\frac{1}{2}e^{-2t}\right]_0^x = \frac{1}{2} - \frac{1}{2}e^{-2x} \to \frac{1}{2}$ pro $x \to +\infty$. **Konverguje, hodnota $\frac{1}{2}$.**

> [!priklad|14]- Rozhodni, zda $\int_1^{+\infty}\frac{\mathrm{d}t}{t}$ a $\int_1^{+\infty}\frac{\mathrm{d}t}{t^2}$ konvergují.
> $\int_1^x \frac{\mathrm{d}t}{t} = \ln x \to +\infty$: **diverguje**. $\int_1^x \frac{\mathrm{d}t}{t^2} = 1 - \frac{1}{x} \to 1$: **konverguje, $= 1$**. Obě funkce jdou k nule, ale $\frac{1}{t^2}$ dost rychle.

> [!priklad|15]- Spočítej $\int_0^2 f$ pro $f(t) = 1$ na $[0; 1)$ a $f(t) = t^2$ na $[1; 2]$.
> $f$ má skok v 1, rozdělíme: $\lim_{b \to 1^-}\int_0^b 1\,\mathrm{d}t + \int_1^2 t^2\,\mathrm{d}t = 1 + \left[\frac{t^3}{3}\right]_1^2 = 1 + \frac{7}{3} =$ **$\frac{10}{3}$**.

> [!priklad|16]- Spočítej objem tělesa, které vznikne rotací grafu $f(x) = \sqrt{x}$ na $[0; 4]$ kolem osy $x$.
> $V = \pi\int_0^4 (\sqrt{t})^2\,\mathrm{d}t = \pi\left[\frac{t^2}{2}\right]_0^4 =$ **$8\pi \approx 25{,}13$**.

> [!priklad|17]- Spočítej délku grafu $f(x) = \frac{2}{3}x^{3/2}$ na $[0; 3]$.
> $f'(x) = \sqrt{x}$, $L = \int_0^3 \sqrt{1 + t}\,\mathrm{d}t = \left[\frac{2}{3}(1 + t)^{3/2}\right]_0^3 = \frac{2}{3}(8 - 1) =$ **$\frac{14}{3}$**.

> [!priklad|18]- Odvoď vzorcem pro objem rotačního tělesa objem kužele s poloměrem podstavy $r$ a výškou $h$.
> Rotace přímky $f(x) = \frac{r}{h}x$ na $[0; h]$: $V = \pi\frac{r^2}{h^2}\int_0^h t^2\,\mathrm{d}t = \pi\frac{r^2}{h^2}\cdot\frac{h^3}{3} =$ **$\frac{1}{3}\pi r^2 h$**.

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 2. semestrálnímu testu (J. Velebil, 7.–11. 12. 2026, témata 06A–08A). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|19]- Nalezněte velikost plochy obrazce vymezeného grafy funkcí $x \mapsto x + 2$ a $x \mapsto x^2$.
> Průsečíky: $x^2 = x + 2$, tedy $x = -1$ a $x = 2$. Na $[-1; 2]$ je $x + 2 \geq x^2$ (např. v 0: $2 \geq 0$, a mezi průsečíky se pořadí nemění). Obsah je $\int_{-1}^{2}(x + 2 - x^2)\,\mathrm{d}x = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2} = \frac{10}{3} + \frac{7}{6} =$ **$\frac{9}{2}$**.

> [!priklad|20]- Dokažte nebo vyvraťte: Ať $f$ je spojitá na $[0; 1)$ a $\lim_{x \to 1^-} f(x) = +\infty$. Potom $\int_0^1 f = +\infty$.
> **Tvrzení neplatí.** Protipříklad $f(t) = (1 - t)^{-1/3}$: je spojitá na $[0; 1)$ a jde k $+\infty$ pro $t \to 1^-$, ale $\int_0^x f = \left[-\frac{3}{2}(1 - t)^{2/3}\right]_0^x = \frac{3}{2} - \frac{3}{2}(1 - x)^{2/3} \to \frac{3}{2}$, tedy $\int_0^1 f = \frac{3}{2}$.

> [!priklad|21]- Dokažte nebo vyvraťte: Ať $f$ je spojitá na $[1; +\infty)$ a $\lim_{x \to +\infty} f(x) = 0$. Potom $\int_1^{+\infty} f$ konverguje.
> **Tvrzení neplatí.** Protipříklad $f(t) = \frac{1}{t}$: je spojitá na $[1; +\infty)$ s limitou 0, ale $\int_1^x \frac{\mathrm{d}t}{t} = \ln x \to +\infty$, takže integrál diverguje.

> [!priklad|22]- Dokažte nebo vyvraťte: Ať $f$ je definovaná na $[0; 2]$, $f(0) = 0$, $f(2) = 4$ a $f$ nenabývá hodnoty 1. Potom $f$ nemá na $[0; 2]$ primitivní funkci.
> **Tvrzení platí.** Kdyby $F$ byla primitivní k $f$ na $[0; 2]$, měla by $f$ podle **Darbouxovy věty** Darbouxovu vlastnost: každé $r$ mezi $f(0) = 0$ a $f(2) = 4$, tedy i $r = 1$, by nabývala. To je spor s předpokladem.

---
← [[MA1 13 – Racionální funkce a typické integrály|5. 11. 2026 Racionální funkce a typické integrály]]

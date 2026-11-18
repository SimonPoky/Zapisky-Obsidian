---
predmet: MA1
prednaska: 15
datum: 2026-11-18
zdroj: "Handout 8A (Geometrie, fyzika, pravděpodobnost), slajdy 18–25; handout 8B (Sinus, kosinus, exponenciála a logaritmus), slajdy 1–11"
tags: [prednaska, MA1]
---

# MA1 15 – Momenty, střední hodnota, sinus, kosinus a logaritmus

*Přednáška 15 · středa 18. 11. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 8A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout08a.pdf) · [Handout 8B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout08b.pdf)

Témata: `průměr funkce` · `první moment` · `těžiště` · `hustota rozdělení pravděpodobnosti` · `střední hodnota` · `exponenciální rozdělení` · `π jako integrál` · `funkce P(z)` · `cos a sin z plochy výseče` · `(cos x)′ = −sin x` · `lim sin h / h` · `10ˣ a log₁₀` · `ln x = ∫₁ˣ dt/t` · `ln(x₁x₂) = ln x₁ + ln x₂` · `Eulerovo číslo e`

První část dokončuje aplikace [[obecná věta o určitém integrálu|obecné věty o určitém integrálu]] z minula: průměr hodnot funkce, první moment a těžiště, a stejné vzorce v pravděpodobnosti jako střední hodnota. Druhá část odpovídá na otázku, kterou jsme dosud obcházeli: co vlastně *jsou* funkce $\sin$, $\cos$ a $\ln$? Zavedou se jen pomocí integrálu a derivace: $\pi$ a kosinus z plochy pod půlkružnicí, logaritmus jako plocha pod $\frac{1}{t}$, a vzorce pro jejich derivace se z toho odvodí, místo aby se braly „na víru“.

## §0 Přehled na jedné stránce

| pojem / věta | co říká | příklad |
| --- | --- | --- |
| průměr funkce | $\operatorname{avg} f = \frac{1}{b - a}\int_a^b f$ | $\operatorname{avg}_{[1; 3]} t^2 = \frac{13}{3}$ |
| první moment, těžiště | $M = \int_a^b t\,f(t)\,\mathrm{d}t$, $\bar{x} = \frac{\int t f}{\int f}$ | hustota $t^2$ na $[0; 1]$: $\bar{x} = \frac{3}{4}$ |
| hustota, spojitá náhodná veličina | $P(a \leq X \leq b) = \int_a^b f$ | — |
| střední hodnota | $E(X) = \int_{-\infty}^{+\infty} t\,f(t)\,\mathrm{d}t$ | exponenciální: $E(X) = \frac{1}{\lambda}$ |
| číslo $\pi$ | $\pi = 2\int_{-1}^{1}\sqrt{1 - t^2}\,\mathrm{d}t$ | plocha jednotkového kruhu |
| funkce $P(z)$ | plocha výseče od bodu nad $z$ k bodu $1$ | $P(-1) = \frac{\pi}{2}$, $P(1) = 0$, $P' < 0$ |
| kosinus, sinus | $\cos x$ = jediné $z$ s $P(z) = \frac{x}{2}$; $\sin x = \sqrt{1 - \cos^2 x}$ | $\cos\frac{\pi}{2} = 0$ |
| derivace sinu a kosinu | $(\cos x)' = -\sin x$, $(\sin x)' = \cos x$ pro $0 < x < \pi$ | z derivace inverzní funkce |
| důležitá limita sinu | $\lim_{h \to 0}\frac{\sin h}{h} = \sin'(0) = 1$ | bez l'Hospitala |
| přirozený logaritmus | $\ln x = \int_1^x \frac{\mathrm{d}t}{t}$ pro $x > 0$ | $\ln 1 = 0$, $(\ln x)' = \frac{1}{x}$ |
| logaritmus součinu | $\ln(x_1 x_2) = \ln x_1 + \ln x_2$ | $\ln 8 = 3\ln 2$ |
| Eulerovo číslo | jediné $e$ s $\ln e = 1$; $2 < e < 3$ | $e \approx 2{,}718$ |

## §1 Průměr funkce, první moment a těžiště (handout 8A)

Aritmetický průměr čísel $x_1, \dots, x_n$ je $\bar{x} = \frac{1}{n}\sum_{k=1}^{n} x_k$; průměr $n$ stejných čísel $x$ je zase $x$. Pro spojitou funkci se součet nahradí integrálem a počet $n$ délkou intervalu (slajd 18).

> [!definice] Definice · handout 8A, slajd 18 (průměr funkce)
> Ať je $f$ spojitá na $[a; b]$, $a < b$. **Průměr hodnot** funkce $f$ na $[a; b]$ je
>
> $$
> \operatorname*{avg}_{t \in [a; b]} f(t) = \frac{1}{b - a}\int_a^b f(t)\,\mathrm{d}t.
> $$

^def-prumer

> [!lidsky] Lidsky
> Výška obdélníku nad $[a; b]$, který má stejnou plochu jako plocha pod grafem. Kdybys „kopce“ grafu rozhrnul do rovna, skončíš přesně v této výšce.

> [!example] Příklad (slajd 19)
> $\operatorname{avg}_{t \in [1; 3]} t^2 = \frac{1}{2}\int_1^3 t^2\,\mathrm{d}t = \frac{1}{2}\cdot\frac{27 - 1}{3} = \frac{13}{3} \approx 4{,}33$. Leží mezi $\min = 1$ a $\max = 9$. Průměr $\sin$ na $[0; \pi]$ je $\frac{1}{\pi}\int_0^\pi \sin = \frac{2}{\pi} \approx 0{,}64$.

> [!obrazek] Průměr jako výška obdélníku se stejnou plochou
> ![[ma115-prumer.png]]
> *Modrá plocha pod $t^2$ na $[1; 3]$ je $\frac{26}{3}$. Oranžový obdélník s výškou průměru $\frac{13}{3}$ má stejnou plochu. Zelená tečkovaná je minimum, červená maximum: průměr leží mezi nimi.*

Ze slajdu 19: průměr konstantní funkce $\operatorname{avg} f$ je zase $\operatorname{avg} f$ a platí $\min_{[a; b]} f \leq \operatorname{avg}_{[a; b]} f \leq \max_{[a; b]} f$. Druhé je jen [[omezenost integrálu]] vydělená délkou $b - a$.

Fyzikálně: hmotné body $x_1, \dots, x_n$ s hmotnostmi $m_1, \dots, m_n$ mají **první moment** $x_1 m_1 + \dots + x_n m_n$ (otáčivý účinek vzhledem k počátku) a **těžiště** $\bar{x} = \frac{x_1 m_1 + \dots + x_n m_n}{m_1 + \dots + m_n}$, vážený průměr poloh. Pro spojitě rozloženou hmotu je $f$ **hustota hmotnosti** na $[a; b]$ a $\int_a^b f$ celková hmotnost (slajd 20).

> [!definice] Definice · handout 8A, slajdy 20 a 21 (první moment a těžiště)
> Ať je $f \geq 0$ spojitá na $[a; b]$ (hustota rozložení hmotnosti). Moment $\overset{v}{\underset{u}{M}}(f)$ je aditivní a pro $[u; v] \subseteq [a; b] \subseteq [0; +\infty)$ splňuje
>
> $$
> (v - u)\cdot\min_{t \in [u; v]} t\cdot\min_{t \in [u; v]} f(t) \;\leq\; \overset{v}{\underset{u}{M}}(f) \;\leq\; (v - u)\cdot\max_{t \in [u; v]} t\cdot\max_{t \in [u; v]} f(t).
> $$
>
> Podle obecné věty (s $g(t) = t$, $h = f$, $\star$ = součin) je **první moment** a **těžiště**
>
> $$
> \overset{b}{\underset{a}{M}}(f) = \int_a^b t\,f(t)\,\mathrm{d}t, \qquad \bar{x} = \frac{\int_a^b t\,f(t)\,\mathrm{d}t}{\int_a^b f(t)\,\mathrm{d}t}.
> $$

^def-moment-teziste

> [!lidsky] Lidsky
> Každý kousek tyče „tahá“ za otáčení silou úměrnou své hmotnosti $f(t)\,\mathrm{d}t$ krát vzdálenost $t$ od počátku; moment je součet těchto tahů. Těžiště je bod, kam bys musel soustředit celou hmotnost, aby byl moment stejný: tam tyč podepřeš a nepřevrátí se.

> [!example] Příklad (slajdy 22 a 23)
> - Hustota $f = 1$ na $[0; 2]$: $M = \int_0^2 t\,\mathrm{d}t = 2$, hmotnost $\int_0^2 1 = 2$, těžiště $\bar{x} = 1$, přesně uprostřed.
> - Hustota $f(t) = t^2$ na $[0; 1]$: $M = \int_0^1 t^3 = \frac{1}{4}$, hmotnost $\int_0^1 t^2 = \frac{1}{3}$, $\bar{x} = \frac{1/4}{1/3} = \frac{3}{4}$. Tyč je těžší vpravo, těžiště se posune doprava od středu $\frac{1}{2}$.

> [!obrazek] Těžiště a střední hodnota
> ![[ma115-tezisko.png]]
> *Vlevo modrá hustota $t^2$ na $[0; 1]$, oranžový trojúhelník je těžiště $\frac{3}{4}$, zelená tečkovaná střed intervalu $\frac{1}{2}$. Vpravo modrá hustota exponenciálního rozdělení s $\lambda = 2$ (pro $t < 0$ nulová), zelená plocha je pravděpodobnost $P(1 \leq X \leq 2) \approx 0{,}117$, oranžová čárkovaná střední hodnota $\frac{1}{2}$ (§2).*

> [!navic] Průměr je těžiště s konstantní hustotou
> S hustotou $f = 1$ je $\bar{x} = \frac{\int_a^b t\,\mathrm{d}t}{b - a} = \operatorname{avg}_{[a; b]} t = \frac{a + b}{2}$. Aritmetický průměr je vážený průměr se stejnými vahami $m_1 = \dots = m_n = 1$. Odhad s $\min t$ a $\max t$ ve tvaru výše platí pro $t \geq 0$ (pro záporná $t$ by se nerovnosti při násobení otočily); výsledný vzorec $\int t f$ ale platí na libovolném intervalu.

## §2 Střední hodnota náhodné veličiny

Momenty se v teorii pravděpodobnosti objevují pod jinými jmény (slajd 24): hmota je pravděpodobnost, hustota hmotnosti je hustota pravděpodobnosti a [[těžiště]] je střední hodnota.

> [!definice] Definice · handout 8A, slajd 24 (spojitá náhodná veličina, hustota)
> Náhodná veličina $X$ je **spojitá**, pokud existuje funkce $f$ definovaná na celém $\mathbb{R}$ (se splněnými dalšími vlastnostmi, viz Navíc níže) taková, že pro všechna $a \leq b$
>
> $$
> \operatorname{Prob}(a \leq X \leq b) = \int_a^b f(t)\,\mathrm{d}t.
> $$
>
> Funkci $f$ říkáme **hustota rozdělení pravděpodobnosti** spojité náhodné veličiny $X$.

^def-hustota

> [!lidsky] Lidsky
> Náhodná veličina je číslo, které vyjde z pokusu (doba čekání na tramvaj, chyba měření). U spojité veličiny nemá smysl ptát se na pravděpodobnost jednoho přesného čísla, ta je nulová; ptáš se na interval a pravděpodobnost je plocha pod hustotou nad tím intervalem.

> [!example] Příklad
> Rovnoměrné rozdělení na $[0; 10]$ (třeba minuty čekání na tramvaj jezdící po 10 minutách): $f(t) = \frac{1}{10}$ na $[0; 10]$, jinde $0$. Pak $\operatorname{Prob}(2 \leq X \leq 5) = \int_2^5 \frac{1}{10} = 0{,}3$ a $\operatorname{Prob}(X = 3) = \int_3^3 f = 0$. Nepříklad: $f(t) = 2$ na $[0; 1]$ hustota není, protože $\int_{-\infty}^{+\infty} f = 2$, a pravděpodobnost „něco vyjde“ by byla $2$.

> [!definice] Definice · handout 8A, slajd 24 (střední hodnota)
> **Střední hodnota** $E(X)$ (anglicky *expected value*) spojité náhodné veličiny $X$ s hustotou $f$ je první moment hustoty:
>
> $$
> E(X) = \int_{-\infty}^{+\infty} t\cdot f(t)\,\mathrm{d}t.
> $$

^def-stredni-hodnota

> [!lidsky] Lidsky
> Dlouhodobý průměr výsledků: kdybys pokus opakoval mockrát a výsledky zprůměroval, dostaneš zhruba $E(X)$. Geometricky je to těžiště plochy pod hustotou, protože celková „hmotnost“ je $\int f = 1$ a není čím dělit.

> [!example] Příklad
> Rovnoměrné rozdělení na $[1; 3]$, $f = \frac{1}{2}$ na $[1; 3]$: $E(X) = \int_1^3 \frac{t}{2}\,\mathrm{d}t = \frac{9 - 1}{4} = 2$, prostředek intervalu. Integrál přes $\mathbb{R}$ je [[integrál na neomezeném intervalu|nevlastní]], ale mimo $[1; 3]$ je integrand nulový.

> [!definice] Definice · handout 8A, slajd 25 (exponenciální rozdělení)
> Náhodná veličina $X$ má **exponenciální rozdělení** s parametrem $\lambda > 0$, má-li hustotu
>
> $$
> f(x) = \begin{cases} 0, & x < 0,\\ \lambda e^{-\lambda x}, & x \geq 0. \end{cases}
> $$

^def-exponencialni-rozdeleni

> [!lidsky] Lidsky
> Model doby čekání na událost, která přichází „bez paměti“ (rozpad atomu, příchod dalšího zákazníka). Krátké čekání je nejpravděpodobnější, dlouhé čekání je čím dál vzácnější. Parametr $\lambda$ je, kolik událostí v průměru přijde za jednotku času.

> [!example] Příklad (slajd 25)
> Střední hodnota per partes:
>
> $$
> E(X) = \lambda\int_0^{+\infty} t\,e^{-\lambda t}\,\mathrm{d}t = \lim_{x \to +\infty}\left(\left[-t e^{-\lambda t}\right]_0^x + \int_0^x e^{-\lambda t}\,\mathrm{d}t\right) = \lim_{x \to +\infty}\left(-x e^{-\lambda x} + \frac{1 - e^{-\lambda x}}{\lambda}\right) = \frac{1}{\lambda}.
> $$
>
> Pro $\lambda = 2$ (dvě události za minutu) je průměrné čekání $\frac{1}{2}$ minuty a $\operatorname{Prob}(1 \leq X \leq 2) = \int_1^2 2e^{-2t}\,\mathrm{d}t = e^{-2} - e^{-4} \approx 0{,}117$.

> [!pozor] Nespojitá hustota
> $f$ není spojitá v nule (skok z $0$ na $\lambda$), takže $\int_{-\infty}^{+\infty} f$ se počítá jako [[integrál funkce s konečně mnoha nespojitostmi]]. Ve výpočtu $E(X)$ to nevadí: $t \cdot f(t)$ je v nule spojitá (obě strany dají $0$), takže stačí integrovat od $0$.

> [!navic] Jaké „další vlastnosti“ musí hustota mít
> Aby šlo o pravděpodobnosti, musí být $f \geq 0$ a $\int_{-\infty}^{+\infty} f = 1$. Exponenciální hustota to splňuje: $\int_0^{+\infty}\lambda e^{-\lambda t}\,\mathrm{d}t = \lim_{x \to +\infty}(1 - e^{-\lambda x}) = 1$. Podrobně v kapitole 4 knihy Montgomery, Runger: *Applied Statistics and Probability for Engineers* (doporučení ze slajdu 24, nepovinné).

## §3 Číslo π a funkce P (handout 8B)

Dosud jsme s $\sin$, $\cos$, $e^x$ a $\ln$ zacházeli „lehkovážně“: jejich derivace jsme brali z tabulky. Teď se ukáže, že jdou zavést jen pomocí integrálu a derivací se pak dají dokázat (slajd 2, inspirováno knihou M. Spivak, *Calculus*).

Intuice (slajd 3): bod $p = (\cos x; \sin x)$ leží na jednotkové kružnici tak, že oblouk od $(1; 0)$ k $p$ má délku $x$. Výseč s tímto obloukem má plochu $A(x) = \frac{x}{2}$, protože plocha je úměrná úhlu: $\frac{A(x)}{A(2\pi)} = \frac{x}{2\pi}$ a celý kruh má $A(2\pi) = \pi$. Kosinus se tedy dá najít z plochy, a plochu umíme počítat integrálem. Nejdřív ale potřebujeme samotné $\pi$.

> [!definice] Definice · handout 8B, slajd 4 (číslo π)
> Číslo $\pi$ je definováno jako reálné číslo
>
> $$
> \pi = 2\int_{-1}^{1}\sqrt{1 - t^2}\,\mathrm{d}t.
> $$

^def-pi

> [!lidsky] Lidsky
> Graf $\sqrt{1 - t^2}$ na $[-1; 1]$ je horní polovina jednotkové kružnice. Plocha pod ním je půlkruh, tedy $\frac{\pi}{2}$, a $\pi$ je dvojnásobek: plocha celého kruhu s poloměrem $1$. Integrál existuje, protože funkce je spojitá ([[existence určitého integrálu]]), takže definice je poctivá.

> [!example] Příklad
> Numericky $2\int_{-1}^{1}\sqrt{1 - t^2}\,\mathrm{d}t \approx 3{,}14159$. Hrubý odhad z [[omezenost integrálu|omezenosti]]: na $[-1; 1]$ je $0 \leq \sqrt{1 - t^2} \leq 1$, takže $0 \leq \pi \leq 4$; s rozdělením na kousky se odhad zpřesní.

> [!navic] π je i délka půlkružnice (domácí cvičení)
> Podle vzorce pro [[délka křivky|délku křivky]] má půlkružnice $f(t) = \sqrt{1 - t^2}$ délku $\int_{-1}^{1}\sqrt{1 + (f'(t))^2}\,\mathrm{d}t$ a $1 + (f'(t))^2 = 1 + \frac{t^2}{1 - t^2} = \frac{1}{1 - t^2}$. Úkol je ukázat $2\int_{-1}^1\sqrt{1 - t^2}\,\mathrm{d}t = \int_{-1}^{1}\frac{\mathrm{d}t}{\sqrt{1 - t^2}}$, kde napravo je [[nevlastní integrál]] na obou krajích ($\lim_{a \to -1^+}\int_a^0 + \lim_{b \to 1^-}\int_0^b$). Návod: [[metoda per partes|per partes]] s $\sqrt{1 - t^2} = 1 \cdot \sqrt{1 - t^2} = (t)' \cdot \sqrt{1 - t^2}$. Řešení je kartička 15.

> [!definice] Definice · handout 8B, slajd 5 (funkce P)
> Pro $z \in [-1; 1]$ definujeme
>
> $$
> P(z) = \frac{z\sqrt{1 - z^2}}{2} + \int_z^1\sqrt{1 - t^2}\,\mathrm{d}t.
> $$
>
> Je to plocha „výseče“ ohraničené úsečkou z počátku do bodu $(z; \sqrt{1 - z^2})$ na kružnici, obloukem od tohoto bodu k $(1; 0)$ a osou $x$. Má platit $P(\cos x) = A(x)$.

^def-funkce-p

> [!lidsky] Lidsky
> Výseč rozřízneš svislou čarou v $z$: vlevo je trojúhelník s odvěsnami $z$ a $\sqrt{1 - z^2}$ (plocha $\frac{z\sqrt{1 - z^2}}{2}$), vpravo kus pod kružnicí od $z$ do $1$ (integrál). Pro $z < 0$ je „trojúhelník“ se záporným znaménkem, protože tam přebývá kus plochy pod kružnicí, který do výseče nepatří.

> [!example] Příklad
> $P(1) = 0 + 0 = 0$ (výseč s nulovým úhlem), $P(-1) = 0 + \int_{-1}^1\sqrt{1 - t^2} = \frac{\pi}{2}$ (celý půlkruh), $P(0) = 0 + \int_0^1\sqrt{1 - t^2} = \frac{\pi}{4}$ (čtvrtkruh). Pro $z = -\frac{1}{2}$ vyjde $P = \frac{\pi}{3} \approx 1{,}047$.

> [!obrazek] Výseč $A(x)$ a jak ji měří funkce $P$
> ![[ma115-vysec.png]]
> *Vlevo oranžová výseč jednotkové kružnice s obloukem délky $x$ (zeleně) a červeným bodem $p = (\cos x; \sin x)$; její plocha je $\frac{x}{2}$. Vpravo totéž rozřezané v $z = \cos x$: zelený trojúhelník $\frac{z\sqrt{1 - z^2}}{2}$ a oranžová plocha pod kružnicí od $z$ do $1$. Součet je $P(z)$.*

> [!veta] Tvrzení · handout 8B, slajd 5 (vlastnosti P)
> ==Ať $P$ je funkce z definice výše na $[-1; 1]$.== Potom **$P$ je spojitá na $[-1; 1]$, $P(-1) = \frac{\pi}{2}$, $P(1) = 0$** a na $(-1; 1)$ je
>
> $$
> P'(z) = \frac{1 - z^2 - z^2 - 2(1 - z^2)}{2\sqrt{1 - z^2}} = -\frac{1}{2\sqrt{1 - z^2}} < 0,
> $$
>
> takže **$P$ na $[-1; 1]$ klesá**. Proto pro každé $x \in [0; \pi]$ existuje **právě jedno** $z \in [-1; 1]$ s $P(z) = \frac{x}{2}$.
>
> > [!note]- Výpočet derivace
> > První sčítanec podle pravidla pro součin a složenou funkci: $\left(\frac{z\sqrt{1 - z^2}}{2}\right)' = \frac{1}{2}\left(\sqrt{1 - z^2} - \frac{z^2}{\sqrt{1 - z^2}}\right) = \frac{1 - z^2 - z^2}{2\sqrt{1 - z^2}}$. Druhý sčítanec: $\int_z^1 = -\int_1^z$, takže podle [[věta o derivaci integrálu podle horní meze|věty o derivaci integrálu podle horní meze]] je jeho derivace $-\sqrt{1 - z^2} = -\frac{2(1 - z^2)}{2\sqrt{1 - z^2}}$. Součet: $\frac{1 - 2z^2 - 2 + 2z^2}{2\sqrt{1 - z^2}} = -\frac{1}{2\sqrt{1 - z^2}}$.
> >
> > Existence $z$: $\frac{x}{2} \in [0; \frac{\pi}{2}] = [P(1); P(-1)]$ a $P$ je spojitá, takže podle [[věta o mezihodnotě|věty o mezihodnotě]] nějaké $z$ existuje. Jednoznačnost: $P$ je [[ryze monotónní funkce|klesající]], dvě různá $z$ nemohou dát stejnou hodnotu.

^veta-vlastnosti-p

> [!lidsky] Lidsky
> Když bod $z$ posouváš zprava doleva od $1$ k $-1$, výseč se plynule zvětšuje od nuly po celý půlkruh. Každou plochu mezi $0$ a $\frac{\pi}{2}$ proto potká právě jednou.

> [!obrazek] Graf $P$ a hledání $\cos x$
> ![[ma115-funkce-p.png]]
> *Modrý graf $P$ klesá od $\frac{\pi}{2}$ v $-1$ k $0$ v $1$. Oranžová hladina $\frac{x}{2}$ pro $x = 2$ ho protne v jediném červeném bodě; jeho první souřadnice je $\cos 2 \approx -0{,}416$.*

## §4 Kosinus, sinus a jejich derivace

> [!definice] Definice · handout 8B, slajd 5 (kosinus a sinus)
> Ať $0 \leq x \leq \pi$. To jediné $z \in [-1; 1]$, pro které $P(z) = \frac{x}{2}$, se nazývá **kosinus** úhlu $x$ a značí $\cos x$. **Sinus** úhlu $x$ je definován rovností
>
> $$
> \sin x = \sqrt{1 - \cos^2 x}.
> $$

^def-sin-cos

> [!lidsky] Lidsky
> Kosinus je místo na ose $x$, kde musíš výseč „říznout“, aby měla plochu $\frac{x}{2}$, tedy aby oblouk měřil $x$. Sinus je pak výška bodu na kružnici nad tímto místem (Pythagoras: $\cos^2 + \sin^2 = 1$).

> [!example] Příklad
> - $\cos 0 = 1$, protože $P(1) = 0 = \frac{0}{2}$; $\cos\pi = -1$, protože $P(-1) = \frac{\pi}{2}$.
> - $\cos\frac{\pi}{2} = 0$, protože $P(0) = \frac{\pi}{4} = \frac{1}{2}\cdot\frac{\pi}{2}$; pak $\sin\frac{\pi}{2} = \sqrt{1 - 0} = 1$.
> - $\cos\frac{2\pi}{3} = -\frac{1}{2}$, protože $P(-\frac{1}{2}) = \frac{\pi}{3}$; $\sin\frac{2\pi}{3} = \sqrt{1 - \frac{1}{4}} = \frac{\sqrt{3}}{2}$.

> [!pozor] Zatím jen pro $x \in [0; \pi]$
> Definice dává $\cos$ a $\sin$ jen na $[0; \pi]$ a $\sin \geq 0$ tam (odmocnina). Pro ostatní $x$ se funkce dodefinují (sinus liše, kosinus sudě, pak periodicky s periodou $2\pi$); to je podle slajdu 7 „téměř hračka“ a na přednášce se dělat nebude. Součtové vzorce přijdou v partii o diferenciálních rovnicích.

Pro derivaci kosinu je potřeba věta z handoutu 3B, kterou jsme zatím jen zmínili:

> [!veta] Věta o derivaci inverzní funkce · handout 3B, slajd 15
> ==Ať má $f$ na nějakém okolí bodu $p$ spojitou derivaci a $f'(p) \neq 0$.== Potom
> 1. **existuje interval $(a; b) \ni p$, na kterém má $f$ [[inverzní funkce|inverzní funkci]] $f^{-1}$,**
> 2. **$f^{-1}$ má derivaci v bodě $q = f(p)$ a $(f^{-1})'(q) = \dfrac{1}{f'(p)} = \dfrac{1}{f'(f^{-1}(q))}$.**
>
> > [!note]- Proč (náznak)
> > Ze spojitosti $f'$ a $f'(p) \neq 0$ má $f'$ blízko $p$ stálé znaménko, takže $f$ je tam ryze monotónní a má spojitou inverzi ([[věta o spojitosti inverzní funkce]]). Vzorec plyne z $f(f^{-1}(y)) = y$: derivací podle [[věta o derivaci složené funkce|pravidla pro složenou funkci]] je $f'(f^{-1}(y))\cdot(f^{-1})'(y) = 1$. Poctivý důkaz existence $(f^{-1})'$ jde přes [[Carathéodoryho trik]].

^veta-derivace-inverzni

> [!lidsky] Lidsky
> Graf inverzní funkce je graf $f$ převrácený podle přímky $y = x$. Převrácením se tečna se sklonem $k$ změní na tečnu se sklonem $\frac{1}{k}$. Proto nesmí být $f'(p) = 0$: vodorovná tečna by se převrátila na svislou, a ta směrnici nemá.

> [!example] Příklad (slajd 15 handoutu 3B)
> $f(x) = e^x$, $f'(p) = e^p \neq 0$, inverze je $\ln$. Pro $q = e^p$: $(\ln)'(q) = \frac{1}{e^p} = \frac{1}{q}$. Konkrétně $(\ln)'(e^2) = e^{-2} \approx 0{,}135$. Nepříklad: $f(x) = x^3$ v $p = 0$ má $f'(0) = 0$ a inverze $\sqrt[3]{y}$ v nule derivaci nemá (svislá tečna).

> [!navic] Proč spojitá derivace
> Handout píše jen „$f'(p) \neq 0$“. Bez spojitosti $f'$ ale první bod neplatí: $f(x) = \frac{x}{2} + x^2\sin\frac{1}{x}$ ($f(0) = 0$) má $f'(0) = \frac{1}{2}$, ale v každém okolí nuly je $f'$ někde záporná, $f$ tam není monotónní, a tedy ani prostá. V přednáškových použitích ($\cos$, $\ln$, $e^x$) je derivace spojitá vždy.

> [!veta] Tvrzení · handout 8B, slajd 6 (derivace sinu a kosinu)
> ==Ať $0 < x < \pi$.== Potom **$(\cos x)' = -\sin x$** a **$(\sin x)' = \cos x$**.
>
> > [!note]- Důkaz (slajd 6)
> > 1. Označme $Q = 2P$. Z definice je $Q(\cos x) = x$ pro $x \in [0; \pi]$, tedy $\cos = Q^{-1}$ (kosinus je inverze ke $Q$).
> > 2. $Q'(z) = 2P'(z) = -\dfrac{1}{\sqrt{1 - z^2}}$, nenulová a spojitá na $(-1; 1)$.
> > 3. Podle [[věta o derivaci inverzní funkce|věty o derivaci inverzní funkce]]: $(\cos x)' = (Q^{-1})'(x) = \dfrac{1}{Q'(Q^{-1}(x))} = \dfrac{1}{Q'(\cos x)} = -\sqrt{1 - \cos^2 x} = -\sin x$.
> > 4. Derivace definiční rovnosti $\sin x = \sqrt{1 - \cos^2 x}$ podle pravidla pro složenou funkci: $(\sin x)' = \dfrac{-2\cos x\cdot(-\sin x)}{2\sqrt{1 - \cos^2 x}} = \dfrac{\cos x\sin x}{\sin x} = \cos x$. Krátit smíme, protože pro $0 < x < \pi$ je $\cos x \in (-1; 1)$, a tedy $\sin x > 0$.

^veta-derivace-sin-cos

> [!lidsky] Lidsky
> Kosinus je $Q$ „pozpátku“, takže jeho derivace je převrácená hodnota derivace $Q$. A ta je po dosazení $z = \cos x$ přesně $-\frac{1}{\sin x}$. Vzorce, které jsme dosud brali z tabulky, tak vyplynuly jen z definice $\pi$ a integrálu.

> [!example] Příklad
> V $x = \frac{\pi}{2}$: $(\cos)'(\frac{\pi}{2}) = -\sin\frac{\pi}{2} = -1$ a $Q'(\cos\frac{\pi}{2}) = Q'(0) = -1$, převrácená hodnota sedí. V $x = \frac{2\pi}{3}$: $(\cos)'(\frac{2\pi}{3}) = -\frac{\sqrt{3}}{2} \approx -0{,}866$.

Ze vzorce pro derivaci teď plyne známá limita (slajd 7):

> [!veta] Důležitá limita sinu · handout 8B, slajd 7
> $$
> \lim_{h \to 0}\frac{\sin h}{h} = \lim_{h \to 0}\frac{\sin(0 + h) - \sin 0}{h} = \sin'(0) = \cos 0 = \mathbf{1}.
> $$

^veta-limita-sin

> [!lidsky] Lidsky
> Podíl $\frac{\sin h}{h}$ je směrnice sečny grafu sinu mezi $0$ a $h$, takže jeho limita je derivace sinu v nule. Blízko nuly je $\sin h \approx h$: pro $h = 0{,}1$ je $\frac{\sin 0{,}1}{0{,}1} \approx 0{,}9983$.

> [!pozor] Nepoužívej l'Hospitala tam, kde dokazuješ derivaci sinu
> S [[l'Hospitalovo pravidlo|l'Hospitalovým pravidlem]] je limita „snadná“ ($\frac{\cos h}{1} \to 1$), ale potřebuje vědět, že $(\sin)' = \cos$. Ve školním přístupu přes geometrii se přitom $(\sin)' = \cos$ dokazuje právě pomocí této limity, takže by to byl kruh. Tady je pořadí poctivé: derivace z definice přes $P$, limita až z ní. (Vzorec jsme odvodili pro $0 < x < \pi$; pro $x = 0$ je potřeba sinus dodefinovat i pro záporná $x$, slajd to přeskakuje.)

## §5 Motivace: $10^x$ a $\log_{10}$

Než přijde [[přirozený logaritmus|logaritmus]], intuice (slajdy 8 a 9) na funkci $f(x) = 10^x$, kterou známe ze střední školy. Platí $f(x_1 + x_2) = 10^{x_1}\cdot 10^{x_2} = f(x_1)\cdot f(x_2)$. Derivace z definice:

$$
f'(x) = \lim_{h \to 0}\frac{10^{x + h} - 10^x}{h} = 10^x\cdot\lim_{h \to 0}\frac{10^h - 1}{h} = f(x)\cdot f'(0).
$$

Derivace je tedy násobek funkce samé, ale konstantu $f'(0)$ neznáme. Inverze $g(z) = \log_{10} z$ ($z > 0$) má podle [[věta o derivaci inverzní funkce|věty o derivaci inverzní funkce]]

$$
g'(z) = \frac{1}{f'(f^{-1}(z))} = \frac{1}{f(f^{-1}(z))\cdot f'(0)} = \frac{1}{f'(0)}\cdot\frac{1}{z}.
$$

Protože $10^0 = 1$, je $g(1) = 0$, a podle [[fundamentální věta kalkulu|fundamentální věty]] $g(z) = \frac{1}{f'(0)}\int_1^z \frac{\mathrm{d}t}{t}$. Stejný výsledek dá přímý výpočet: $\frac{\log_{10}(x + h) - \log_{10}x}{h} = \frac{\log_{10}(1 + h/x)}{h}$, kde se použije $\log_{10}(x_1 x_2) = \log_{10}x_1 + \log_{10}x_2$. Nápad: konstantu $\frac{1}{f'(0)}$ zahodit. Integrál $\int_1^z\frac{\mathrm{d}t}{t}$ by pak měl být „nějaký logaritmus“, a ten vezmeme za definici.

> [!navic] Kolik je $f'(0)$
> Až bude zavedena obecná mocnina $a^x = e^{x\ln a}$ (slajd 12), vyjde $f'(0) = \ln 10 \approx 2{,}303$. Proto $(10^x)' = \ln 10\cdot 10^x$ a $(\log_{10}x)' = \frac{1}{x\ln 10}$.

## §6 Přirozený logaritmus

> [!definice] Definice · handout 8B, slajd 9 (přirozený logaritmus)
> Ať $x > 0$. Reálné číslo
>
> $$
> \ln x = \int_1^x \frac{1}{t}\,\mathrm{d}t
> $$
>
> nazýváme **přirozený logaritmus** čísla $x$.

^def-ln

> [!lidsky] Lidsky
> Plocha pod hyperbolou $\frac{1}{t}$ od $1$ do $x$. Pro $x > 1$ je kladná, pro $0 < x < 1$ jdou meze „pozpátku“, a proto je záporná ([[integrál s obrácenými mezemi]]). Integrál existuje, protože $\frac{1}{t}$ je na intervalu mezi $1$ a $x$ spojitá.

> [!example] Příklad
> $\ln 1 = \int_1^1 = 0$. $\ln 2 = \int_1^2\frac{\mathrm{d}t}{t} \approx 0{,}693$ a podle omezenosti integrálu leží mezi $(2 - 1)\cdot\frac{1}{2}$ a $(2 - 1)\cdot 1$. $\ln\frac{1}{2} = \int_1^{1/2}\frac{\mathrm{d}t}{t} = -\int_{1/2}^1\frac{\mathrm{d}t}{t} \approx -0{,}693$. Nepříklad: $\ln 0$ ani $\ln(-1)$ definovaný není, $\frac{1}{t}$ není spojitá na intervalu obsahujícím $0$.

> [!obrazek] Logaritmus jako plocha pod $\frac{1}{t}$
> ![[ma115-ln.png]]
> *Vlevo modrá hyperbola $\frac{1}{t}$. Zelená plocha od $1$ do $3$ je $\ln 3 \approx 1{,}099 > 0$, červená od $0{,}4$ do $1$ se počítá se záporným znaménkem: $\ln 0{,}4 \approx -0{,}916$. Vpravo modrý graf $\ln$: červený bod $\ln 1 = 0$, oranžová hladina $1$ protne graf v $e \approx 2{,}718$, zelený pruh je odhad $2 < e < 3$ (§7).*

> [!veta] Vlastnosti přirozeného logaritmu · handout 8B, slajd 10
> 1. **$\ln$ je spojitá na $(0; +\infty)$ a $(\ln x)' = \frac{1}{x}$**, podle [[věta o derivaci integrálu podle horní meze|věty o derivaci integrálu podle horní meze]].
> 2. **$\ln$ je rostoucí na $(0; +\infty)$**, protože $(\ln x)' = \frac{1}{x} > 0$.
> 3. **$\ln 1 = 0$.**
> 4. **$\lim_{x \to 0^+}\ln x = -\infty$ a $\lim_{x \to +\infty}\ln x = +\infty$**; $\ln$ není zdola ani shora omezená.
>
> > [!note]- Důkaz bodu 4
> > $\ln 2 = \int_1^2\frac{\mathrm{d}t}{t} \geq (2 - 1)\cdot\frac{1}{2} > 0$. Podle [[logaritmus součinu|logaritmu součinu]] (níže) je $\ln 2^n = n\ln 2$ a $\ln\frac{1}{2^n} = -n\ln 2$, a to jde k $+\infty$, resp. $-\infty$. Funkce je tedy neomezená, a protože roste, jsou limity v krajích $+\infty$ a $-\infty$ (rostoucí funkce má v kraji limitu supremum, resp. infimum svých hodnot, jako u [[věta o limitě monotónní posloupnosti|monotónních posloupností]]).

^veta-vlastnosti-ln

> [!lidsky] Lidsky
> Logaritmus roste pořád, ale čím dál pomaleji (sklon $\frac{1}{x}$ klesá k nule). Přesto dojde až do nekonečna: každé zdvojnásobení $x$ přidá stejný kus $\ln 2 \approx 0{,}69$.

> [!example] Příklad
> $\ln 1024 = \ln 2^{10} = 10\ln 2 \approx 6{,}93$, takže $\ln x > 6$ už pro $x = 1024$, a $\ln 2^{100} \approx 69{,}3$. Naopak $\ln\frac{1}{1024} \approx -6{,}93$. Tečna v $x = 1$ má sklon $1$, v $x = 100$ už jen $0{,}01$.

> [!veta] Logaritmus součinu · handout 8B, slajd 10
> ==Ať $x_1, x_2 > 0$.== Potom **$\ln(x_1 x_2) = \ln x_1 + \ln x_2$**. Důsledky: $\ln x^n = n\ln x$ pro $n \in \mathbb{N}$ a $\ln\frac{x_1}{x_2} = \ln x_1 - \ln x_2$.
>
> > [!note]- Důkaz (slajd 10)
> > Pevně zvol $x_2 > 0$ a polož $f(x) = \ln(x\cdot x_2)$ pro $x > 0$. Podle pravidla pro složenou funkci $f'(x) = \frac{1}{x x_2}\cdot x_2 = \frac{1}{x}$. Funkce $f$ a $\ln$ mají stejnou derivaci na intervalu $(0; +\infty)$, takže se liší o konstantu ([[primitivní funkce se liší o konstantu]]): $f(x) = \ln x + c$. Dosazením $x = 1$: $\ln x_2 = \ln 1 + c = c$. Tedy $\ln(x x_2) = \ln x + \ln x_2$.
> >
> > $\ln x^n = n\ln x$ indukcí z $\ln x^{n+1} = \ln x^n + \ln x$. Podíl: $\ln x_1 = \ln\left(\frac{x_1}{x_2}\cdot x_2\right) = \ln\frac{x_1}{x_2} + \ln x_2$.
>
> > [!note]- Druhý důkaz substitucí (domácí cvičení z tabule)
> > Podle aditivity $\ln(x_1 x_2) = \int_1^{x_1}\frac{\mathrm{d}t}{t} + \int_{x_1}^{x_1 x_2}\frac{\mathrm{d}t}{t}$. Ve druhém integrálu substituce $t = x_1 s$, $\mathrm{d}t = x_1\,\mathrm{d}s$, meze $s = 1$ a $s = x_2$: $\int_1^{x_2}\frac{x_1\,\mathrm{d}s}{x_1 s} = \int_1^{x_2}\frac{\mathrm{d}s}{s} = \ln x_2$.

^veta-ln-soucin

> [!lidsky] Lidsky
> Logaritmus převádí násobení na sčítání. Geometricky: plocha pod $\frac{1}{t}$ od $x_1$ do $x_1 x_2$ je stejná jako od $1$ do $x_2$, protože roztažení vodorovně $x_1$-krát a stlačení svisle $x_1$-krát plochu nezmění.

> [!example] Příklad
> $\ln 6 = \ln 2 + \ln 3 \approx 0{,}693 + 1{,}099 = 1{,}792$. $\ln 8 = 3\ln 2 \approx 2{,}079$. $\ln\frac{1}{4} = \ln 1 - \ln 4 = -2\ln 2 \approx -1{,}386$.

> [!pozor] Logaritmus součtu žádný vzorec nemá
> $\ln(x_1 + x_2) \neq \ln x_1 + \ln x_2$: třeba $\ln(1 + 1) = \ln 2 \approx 0{,}69$, ale $\ln 1 + \ln 1 = 0$. Stejně tak $\ln(x_1 x_2) \neq \ln x_1\cdot\ln x_2$.

## §7 Eulerovo číslo $e$

> [!definice] Definice · handout 8B, slajd 11 (Eulerovo číslo)
> Existuje právě jedno reálné číslo $e > 0$, pro které $\ln e = 1$, tedy $\int_1^e\frac{\mathrm{d}t}{t} = 1$. Říkáme mu **Eulerovo číslo**. Platí $2 < e < 3$.
>
> > [!note]- Proč existuje, je jediné a leží mezi 2 a 3
> > Odhady [[horní součet|horním]] a [[dolní součet|dolním součtem]]: na $[1; 2]$ s dělením na $[1; 1{,}5]$ a $[1{,}5; 2]$ je $\ln 2 \leq 0{,}5\cdot 1 + 0{,}5\cdot\frac{2}{3} = \frac{5}{6} < 1$. Na $[1; 3]$ s osmi kousky délky $\frac{1}{4}$ je $\ln 3 \geq \frac{1}{4}\left(\frac{1}{1{,}25} + \frac{1}{1{,}5} + \dots + \frac{1}{3}\right) \approx 1{,}020 > 1$.
> >
> > Tedy $\ln 2 < 1 < \ln 3$. Funkce $\ln$ je spojitá na $[2; 3]$, podle [[věta o mezihodnotě|věty o mezihodnotě]] existuje $e \in (2; 3)$ s $\ln e = 1$. Jediné je, protože $\ln$ je rostoucí.

^def-e

> [!lidsky] Lidsky
> $e$ je místo, kde plocha pod $\frac{1}{t}$ (počítáno od $1$) dosáhne přesně $1$. Je to „přirozený“ základ logaritmu: žádná nepohodlná konstanta jako $\frac{1}{\ln 10}$ u $\log_{10}$.

> [!example] Příklad
> $e \approx 2{,}71828$. Kontrola z odhadů: $\ln 2 \approx 0{,}693 < 1$ a $\ln 3 \approx 1{,}099 > 1$, takže opravdu $2 < e < 3$. Plocha pod $\frac{1}{t}$ od $1$ do $e^2$ je $\ln e^2 = 2\ln e = 2$.

> [!navic] Jak to pokračuje (slajdy 11 a 12)
> Protože [[přirozený logaritmus|logaritmus]] je rostoucí, spojitá a neomezená na obě strany, má inverzní funkci $\exp: \mathbb{R} \to (0; +\infty)$, **exponenciálu**. Podle [[věta o derivaci inverzní funkce|věty o derivaci inverzní funkce]] $(\exp x)' = \frac{1}{1/\exp x} = \exp x$ a z [[logaritmus součinu|logaritmu součinu]] plyne $\exp(x_1 + x_2) = \exp x_1\cdot\exp x_2$. Handout definuje $e = \exp 1$, což je totéž co $\ln e = 1$. Pak se zavede $e^x = \exp x$, $a^x = e^{x\ln a}$ pro $a > 0$ a $\log_a$ jako inverze k $a^x$. Racionální hodnotu ani dobrý odhad $e$ zatím neumíme; ten dá [[Taylorův polynom exponenciály]].

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč leží průměr spojité funkce na $[a; b]$ mezi jejím minimem a maximem, a nabývá ho funkce někde?
> Z **omezenosti integrálu** $(b - a)\min f \leq \int_a^b f \leq (b - a)\max f$; vydělením $b - a$ dostaneš $\min f \leq \operatorname{avg} f \leq \max f$. Spojitá funkce na $[a; b]$ nabývá minima i maxima a podle **věty o mezihodnotě** i každé hodnoty mezi nimi, takže existuje $p$ s **$f(p) = \operatorname{avg} f$**.

> [!karta|02]- Jak z obecné věty o určitém integrálu vyjde vzorec pro první moment $\int_a^b t\,f(t)\,\mathrm{d}t$?
> Moment je **aditivní** a na $[u; v] \subseteq [0; +\infty)$ ho sevřou $(v - u)\cdot\min t\cdot\min f$ a $(v - u)\cdot\max t\cdot\max f$. To je obecná věta s $g(t) = t$, $h = f$, $\star$ = **součin**, $A = B = \min$, $C = D = \max$, takže $M = \int_a^b t\,f(t)\,\mathrm{d}t$.

> [!karta|03]- Čím se liší první moment a těžiště a proč se při výpočtu těžiště dělí $\int_a^b f$?
> Moment $\int t f$ závisí na celkové hmotnosti (dvojnásobná hustota = dvojnásobný moment). Těžiště je **poloha**: bod $\bar{x}$, kam soustředěná celá hmotnost $\int f$ dá stejný moment, $\bar{x}\cdot\int f = \int t f$. Proto **$\bar{x} = \frac{\int t f}{\int f}$**, vážený průměr poloh.

> [!karta|04]- Proč je u spojité náhodné veličiny $\operatorname{Prob}(X = c) = 0$ pro každé $c$ a proč u střední hodnoty není co dělit?
> $\operatorname{Prob}(c \leq X \leq c) = \int_c^c f = 0$, **integrál přes bod je nula**. Hustota má celkovou „hmotnost“ $\int_{-\infty}^{+\infty} f = 1$, takže vzorec pro těžiště $\frac{\int t f}{\int f}$ se zjednoduší na **$E(X) = \int t f$**.

> [!karta|05]- Proč by měla výseč jednotkové kružnice s obloukem délky $x$ mít plochu $\frac{x}{2}$ a jak z toho vznikne definice kosinu?
> Plocha výseče je **úměrná oblouku**: $\frac{A(x)}{A(2\pi)} = \frac{x}{2\pi}$ a celý kruh má $A(2\pi) = \pi$, tedy $A(x) = \frac{x}{2}$. Funkce $P(z)$ měří plochu výseče řezané v $z$, a protože bod na kružnici je $(\cos x; \sin x)$, má platit $P(\cos x) = \frac{x}{2}$. Proto **$\cos x$ = to $z$, pro které $P(z) = \frac{x}{2}$**.

> [!karta|06]- Proč pro každé $x \in [0; \pi]$ existuje právě jedno $z \in [-1; 1]$ s $P(z) = \frac{x}{2}$?
> Existence: $P$ je **spojitá**, $P(1) = 0$, $P(-1) = \frac{\pi}{2}$ a $\frac{x}{2} \in [0; \frac{\pi}{2}]$, takže podle **věty o mezihodnotě** takové $z$ je. Jednoznačnost: $P'(z) = -\frac{1}{2\sqrt{1 - z^2}} < 0$, $P$ **klesá**, a klesající funkce nenabude žádné hodnoty dvakrát.

> [!karta|07]- Vyslov větu o derivaci inverzní funkce i s předpoklady.
> Ať má $f$ na okolí $p$ **spojitou derivaci a $f'(p) \neq 0$**. Pak má $f$ na nějakém intervalu $(a; b) \ni p$ inverzní funkci a ta má v $q = f(p)$ derivaci **$(f^{-1})'(q) = \frac{1}{f'(p)} = \frac{1}{f'(f^{-1}(q))}$**.

> [!karta|08]- Dokaž, že $(\cos x)' = -\sin x$ pro $0 < x < \pi$.
> Pro $Q = 2P$ je $Q(\cos x) = x$, tedy **$\cos = Q^{-1}$**. $Q'(z) = -\frac{1}{\sqrt{1 - z^2}} \neq 0$ na $(-1; 1)$. Podle věty o derivaci inverzní funkce $(\cos x)' = \frac{1}{Q'(\cos x)} = -\sqrt{1 - \cos^2 x} =$ **$-\sin x$**.

> [!karta|09]- Odvoď $(\sin x)' = \cos x$ z definice $\sin x = \sqrt{1 - \cos^2 x}$. Kde se použije $0 < x < \pi$?
> Složená funkce: $(\sin x)' = \frac{-2\cos x\cdot(\cos x)'}{2\sqrt{1 - \cos^2 x}} = \frac{\cos x\sin x}{\sin x} = \cos x$. Krácení $\sin x$ vyžaduje **$\sin x \neq 0$**: pro $0 < x < \pi$ je $\cos x \in (-1; 1)$, tedy **$\sin x > 0$** (a $Q'$ v $\cos x$ existuje).

> [!karta|10]- Jak plyne $\lim_{h \to 0}\frac{\sin h}{h} = 1$ bez l'Hospitala a proč by l'Hospital při dokazování $(\sin)' = \cos$ byl kruhový argument?
> $\frac{\sin h}{h} = \frac{\sin(0 + h) - \sin 0}{h}$ je **směrnice sečny**, limita je $\sin'(0) = \cos 0 = 1$. L'Hospital potřebuje $(\sin)' = \cos$, a v geometrickém přístupu se právě tento vzorec dokazuje **pomocí této limity**; tady je derivace odvozená z definice přes $P$, takže kruh nevzniká.

> [!karta|11]- Jak z $10^{x_1 + x_2} = 10^{x_1}\cdot 10^{x_2}$ plyne $f'(x) = f(x)\cdot f'(0)$ pro $f(x) = 10^x$ a co z toho dostaneme pro $\log_{10}$?
> $\frac{10^{x + h} - 10^x}{h} = 10^x\cdot\frac{10^h - 1}{h} \to 10^x\cdot f'(0)$. Pro inverzi $g = \log_{10}$ je $g'(z) = \frac{1}{f'(g(z))} = \frac{1}{f'(0)}\cdot\frac{1}{z}$ a $g(1) = 0$, takže **$\log_{10} z = \frac{1}{f'(0)}\int_1^z\frac{\mathrm{d}t}{t}$**: logaritmus je až na konstantu integrál z $\frac{1}{t}$.

> [!karta|12]- Dokaž $\ln(x_1 x_2) = \ln x_1 + \ln x_2$ pomocí derivace.
> Pro pevné $x_2$ má $f(x) = \ln(x x_2)$ derivaci $\frac{x_2}{x x_2} = \frac{1}{x}$, stejnou jako $\ln$. Na intervalu $(0; +\infty)$ se proto **liší o konstantu**: $f(x) = \ln x + c$. Dosazení $x = 1$: $c = \ln x_2$. Tedy **$\ln(x x_2) = \ln x + \ln x_2$**.

> [!karta|13]- Proč je $\lim_{x \to +\infty}\ln x = +\infty$ a $\lim_{x \to 0^+}\ln x = -\infty$?
> $\ln 2 \geq \frac{1}{2} > 0$ a **$\ln 2^n = n\ln 2 \to +\infty$**, $\ln 2^{-n} = -n\ln 2 \to -\infty$, takže $\ln$ není omezená shora ani zdola. Protože je **rostoucí**, jsou limity v krajích supremum a infimum jejích hodnot, tedy $+\infty$ a $-\infty$.

> [!karta|14]- Proč existuje právě jedno $e$ s $\ln e = 1$ a proč je $2 < e < 3$?
> Horní součet dá **$\ln 2 \leq \frac{5}{6} < 1$**, dolní součet s osmi kousky **$\ln 3 \geq 1{,}02 > 1$**. $\ln$ je spojitá, podle **věty o mezihodnotě** je $e \in (2; 3)$ s $\ln e = 1$; je jediné, protože $\ln$ je **rostoucí**.

> [!karta|15]- Ukaž, že $2\int_{-1}^1\sqrt{1 - t^2}\,\mathrm{d}t = \int_{-1}^1\frac{\mathrm{d}t}{\sqrt{1 - t^2}}$, tedy že $\pi$ je délka půlkružnice.
> Per partes s $(t)' = 1$: $I = \int\sqrt{1 - t^2} = \left[t\sqrt{1 - t^2}\right]_{-1}^1 + \int\frac{t^2}{\sqrt{1 - t^2}} = 0 + \int\left(\frac{1}{\sqrt{1 - t^2}} - \sqrt{1 - t^2}\right) = J - I$. Tedy **$2I = J$** (u krajů jako nevlastní integrály, $J = \lim_{a \to -1^+}\int_a^0 + \lim_{b \to 1^-}\int_0^b$). $J$ je délka půlkružnice, protože $1 + (f')^2 = \frac{1}{1 - t^2}$.

### Příklady na procvičení

> [!priklad|16]- Spočti průměr funkce $\sin$ na $[0; \pi]$.
> $\operatorname{avg} = \frac{1}{\pi}\int_0^\pi\sin t\,\mathrm{d}t = \frac{1}{\pi}[-\cos t]_0^\pi = \frac{2}{\pi} \approx$ **$0{,}637$**.

> [!priklad|17]- Spočti těžiště intervalu $[0; 2]$ s hustotou $f(t) = t$.
> $M = \int_0^2 t^2\,\mathrm{d}t = \frac{8}{3}$, hmotnost $\int_0^2 t\,\mathrm{d}t = 2$, takže $\bar{x} = \frac{8/3}{2} =$ **$\frac{4}{3}$** (vpravo od středu $1$, kde je tyč těžší).

> [!priklad|18]- $X$ má rovnoměrné rozdělení na $[1; 3]$ (hustota $\frac{1}{2}$ na $[1; 3]$, jinde $0$). Spočti $E(X)$ a $\operatorname{Prob}(2 \leq X \leq 5)$.
> $E(X) = \int_1^3\frac{t}{2}\,\mathrm{d}t = \frac{9 - 1}{4} =$ **$2$**. $\operatorname{Prob}(2 \leq X \leq 5) = \int_2^3\frac{1}{2} + \int_3^5 0 =$ **$\frac{1}{2}$**.

> [!priklad|19]- Zjisti z definice $\cos\frac{\pi}{2}$ a $\sin\frac{\pi}{2}$.
> Hledáme $z$ s $P(z) = \frac{\pi}{4}$. $P(0) = 0 + \int_0^1\sqrt{1 - t^2}\,\mathrm{d}t = \frac{\pi}{4}$ (čtvrtkruh) a $z$ je jediné, takže **$\cos\frac{\pi}{2} = 0$** a $\sin\frac{\pi}{2} = \sqrt{1 - 0} =$ **$1$**.

> [!priklad|20]- Vyjádři $\ln 12$ a $\ln\frac{1}{8}$ pomocí $\ln 2$ a $\ln 3$.
> $\ln 12 = \ln(4\cdot 3) = 2\ln 2 + \ln 3 \approx$ **$2{,}485$**. $\ln\frac{1}{8} = \ln 1 - \ln 8 = -3\ln 2 \approx$ **$-2{,}079$**.

> [!priklad|21]- Spočti $(\log_{10} x)'$ v bodě $x = 10$, víš-li, že $(10^x)'|_{x=0} = \ln 10$.
> $(\log_{10}x)' = \frac{1}{\ln 10}\cdot\frac{1}{x}$, v $x = 10$: $\frac{1}{10\ln 10} \approx$ **$0{,}0434$**.

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 2. semestrálnímu testu (J. Velebil, 7.–11. 12. 2026, témata 06A–08A). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|22]- Dokažte nebo vyvraťte: Ať $f$ je spojitá na $[0; 4]$ a $\int_0^4 f(s)\,\mathrm{d}s = 8$. Potom existuje $p \in [0; 4]$ s $f(p) = 2$.
> **Tvrzení platí.** Průměr je $\frac{1}{4}\int_0^4 f = 2$. Z omezenosti integrálu $4\min f \leq 8 \leq 4\max f$, tedy $\min f \leq 2 \leq \max f$. Spojitá $f$ na $[0; 4]$ nabývá minima a maxima (věta o extrémech) a podle **věty o mezihodnotě** i hodnoty $2$ v nějakém $p \in [0; 4]$.

> [!priklad|23]- Dokažte nebo vyvraťte: Ať $f$ je spojitá a kladná na $[0; 2]$. Potom těžiště intervalu $[0; 2]$ s hustotou $f$ je bod $1$.
> **Tvrzení neplatí.** Protipříklad $f(t) = t + 1$, spojitá a kladná na $[0; 2]$: $\int_0^2 t(t + 1)\,\mathrm{d}t = \frac{8}{3} + 2 = \frac{14}{3}$ a $\int_0^2 (t + 1)\,\mathrm{d}t = 4$, takže těžiště je $\frac{14/3}{4} = \frac{7}{6} \neq 1$. Těžiště je $1$ jen u hustot „vyvážených“ kolem středu, třeba konstantní.

> [!priklad|24]- Náhodná veličina $X$ má hustotu $f(x) = 3x^2$ pro $x \in [0; 1]$ a $f(x) = 0$ jinde. Ověřte, že jde o hustotu, a spočtěte $E(X)$.
> $f \geq 0$ a $\int_0^1 3x^2\,\mathrm{d}x = [x^3]_0^1 = 1$, takže je to hustota. $E(X) = \int_0^1 t\cdot 3t^2\,\mathrm{d}t = \left[\frac{3t^4}{4}\right]_0^1 =$ **$\frac{3}{4}$**.

---
← [[MA1 14 – Nevlastní integrál, délka křivky a objem rotačního tělesa|11. 11. 2026 Nevlastní integrál, délka křivky a objem rotačního tělesa]]

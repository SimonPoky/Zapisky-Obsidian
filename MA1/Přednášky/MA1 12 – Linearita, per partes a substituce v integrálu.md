---
predmet: MA1
prednaska: 12
datum: 2026-11-04
zdroj: "Handout 6B (Praktický výpočet integrálu: část 1), slajdy 2–13"
tags: [prednaska, MA1]
---

# MA1 12 – Linearita, per partes a substituce v integrálu

*Přednáška 12 · středa 4. 11. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 6B (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout06b.pdf)

Témata: `integrál jako antiderivace` · `[F]ₐᵇ = F(b) − F(a)` · `integrační proměnná je vázaná` · `tabulka primitivních funkcí` · `linearita integrálu` · `metoda per partes` · `věta o substituci` · `dt = φ′(z) dz` · `směr substituce` · `pozor na bezmyšlenkovitou substituci`

Minule jsme určitý integrál spojité funkce zavedli axiomy a z fundamentální věty víme, že se počítá jako $F(b) - F(a)$ pro libovolnou primitivní funkci $F$. Dnes jsme z toho udělali výpočetní nástroje: tabulku integrálů „otočením“ tabulky derivací, linearitu, metodu per partes (otočené pravidlo pro derivaci součinu) a substituci (otočené pravidlo pro derivaci složené funkce). Na konci přišlo varování, že substituce použitá „pozpátku“ bez kontroly mezí dává nesmysl.

## §0 Přehled na jedné stránce

| nástroj | předpoklady | vzorec | otočené pravidlo |
| --- | --- | --- | --- |
| [[integrál jako antiderivace]] | $f'$ spojitá na $[a; b]$ | $\int_a^b f'(t)\,\mathrm{d}t = f(b) - f(a)$ | derivace |
| [[dosazení mezí]] | | $[F]_a^b = F(b) - F(a)$ | |
| [[tabulka primitivních funkcí]] | integrand spojitý na $[a; b]$ | $\int_a^b t^n = \frac{b^{n+1} - a^{n+1}}{n+1}$, $\int_a^b \cos t = \sin b - \sin a$, … | tabulka derivací |
| [[linearita určitého integrálu]] | $f, g$ spojité, $r, s \in \mathbb{R}$ | $\int_a^b (rf + sg) = r\int_a^b f + s\int_a^b g$ | $(rF + sG)' = rf + sg$ |
| [[metoda per partes]] | $f, g$ se spojitými derivacemi | $\int_a^b f'g = [fg]_a^b - \int_a^b fg'$ | $(fg)' = f'g + fg'$ |
| [[věta o substituci v určitém integrálu]] | $\varphi'$ spojitá, $f \circ \varphi$ spojitá | $\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t = \int_a^b f(\varphi(z))\varphi'(z)\,\mathrm{d}z$ | Chain Rule |
| [[směr substituce]] | | zprava doleva snadné, zleva doprava hlídat meze | |

## §1 Integrál jako antiderivace

Připomenutí z minula ([[fundamentální věta kalkulu]]): pro $f$ [[spojitost na intervalu|spojitou]] na $[a; b]$

1. $\int_a^x f$ existuje pro každé $x \in [a; b]$,
2. $\frac{\mathrm{d}}{\mathrm{d}x}\left(\int_a^x f\right) = f(x)$,
3. $\int_a^b f = F(b) - F(a)$, kde $F$ je libovolná [[primitivní funkce]] k $f$, tj. $F' = f$ na $[a; b]$.

Primitivní funkce ke spojité $f$ vždy existuje a dvě se [[primitivní funkce se liší o konstantu|liší jen o konstantu]].

> [!definice] Značení · slajd 3
> Pro funkci $F$ definovanou v bodech $a$ a $b$ píšeme
>
> $$
> [F(t)]_a^b = [F]_a^b = F(b) - F(a).
> $$

^def-dosazeni-mezi

> [!lidsky] Lidsky
> Hranatá závorka s mezemi je jen zkratka „dosaď horní mez, dosaď dolní mez, odečti“. Díky ní jde výpočet integrálu zapsat na jeden řádek: najdi primitivní funkci, dej ji do závorky, dosaď.

> [!example] Příklad
> $[t^3/3]_{10}^{15} = \frac{15^3}{3} - \frac{10^3}{3} = \frac{3375 - 1000}{3} = \frac{2375}{3}$. A $[\sin t]_0^{\pi} = \sin \pi - \sin 0 = 0$.

> [!veta] Důsledek · slajd 3 (určitý integrál jako antiderivace)
> ==Ať $f$ má na $[a; b]$ spojitou derivaci $f'$.== Potom
>
> $$
> \mathbf{\int_a^b f'(t)\,\mathrm{d}t = f(b) - f(a)}.
> $$
>
> > [!note]- Důkaz
> > Funkce $f'$ je spojitá a $f$ je k ní primitivní (její derivace je $f'$). Podle bodu 3 fundamentální věty je $\int_a^b f' = f(b) - f(a)$.

^veta-antiderivace

> [!lidsky] Lidsky
> Integrál rychlosti je změna polohy. Kdo umí derivovat, umí i integrovat to, co jako derivaci pozná: integrovat znamená „hádat, co se zderivovalo“.

> [!example] Příklad
> $\int_{10}^{15} t^2\,\mathrm{d}t$: protože $\left(\frac{t^3}{3}\right)' = t^2$, je $\int_{10}^{15} t^2\,\mathrm{d}t = \left[\frac{t^3}{3}\right]_{10}^{15} = \frac{2375}{3} \approx 791{,}67$.

Proměnná $t$ v zápisu $\int_a^b f(t)\,\mathrm{d}t$ je **integrační proměnná**. Je [[vázaná proměnná|vázaná]]: výsledek na jejím jménu nezávisí, takže $\int_{10}^{15} t^2\,\mathrm{d}t = \int_{10}^{15} x^2\,\mathrm{d}x$. Je to stejné jako u kvantifikátorů, kde formule $(\forall x)\,\alpha(x)$ a $(\forall y)\,\alpha(y)$ říkají totéž ([[legální přejmenování]]). Volné jsou jen meze: výsledek je funkcí $a$ a $b$, ne $t$. ^integracni-promenna

> [!pozor] Integrační proměnná nesmí splynout s mezí
> $\int_0^x f(x)\,\mathrm{d}x$ je špatný zápis: totéž $x$ je jednou vázané (proměnná) a jednou volné (mez). Správně $\int_0^x f(t)\,\mathrm{d}t$.

### Tabulka: otočení derivací (slajdy 4–6)

Každý řádek tabulky derivací dává řádek tabulky integrálů. Pro $a, b$, na jejichž intervalu je integrand spojitý: ^tabulka

| integrál | výsledek | protože |
| --- | --- | --- |
| $\int_a^b t^n\,\mathrm{d}t$, $n \ne -1$ | $\frac{b^{n+1} - a^{n+1}}{n+1}$ | $\left(\frac{t^{n+1}}{n+1}\right)' = t^n$ |
| $\int_a^b \frac{1}{t}\,\mathrm{d}t$, $a, b > 0$ | $\ln b - \ln a = \ln\frac{b}{a}$ | $(\ln t)' = \frac{1}{t}$ |
| $\int_a^b e^t\,\mathrm{d}t$ | $e^b - e^a$ | $(e^t)' = e^t$ |
| $\int_a^b \sin t\,\mathrm{d}t$ | $-\cos b + \cos a$ | $(-\cos t)' = \sin t$ |
| $\int_a^b \cos t\,\mathrm{d}t$ | $\sin b - \sin a$ | $(\sin t)' = \cos t$ |
| $\int_a^b \frac{1}{\sqrt{1 - t^2}}\,\mathrm{d}t$, $a, b \in (-1; 1)$ | $\arcsin b - \arcsin a$ | $(\arcsin t)' = \frac{1}{\sqrt{1 - t^2}}$ |
| $\int_a^b \frac{1}{1 + t^2}\,\mathrm{d}t$ | $\arctan b - \arctan a$ | $(\arctan t)' = \frac{1}{1 + t^2}$ |
| $\int_a^b \frac{1}{\sin^2 t}\,\mathrm{d}t$ | $-\cot b + \cot a$ | $(-\cot t)' = \frac{1}{\sin^2 t}$ |
| $\int_a^b \frac{1}{\cos^2 t}\,\mathrm{d}t$ | $\tan b - \tan a$ | $(\tan t)' = \frac{1}{\cos^2 t}$ |

> [!example] Příklad
> $\int_0^1 \frac{1}{1 + t^2}\,\mathrm{d}t = \arctan 1 - \arctan 0 = \frac{\pi}{4}$. $\int_1^e \frac{1}{t}\,\mathrm{d}t = \ln e - \ln 1 = 1$.

> [!pozor] Podmínka spojitosti na celém $[a; b]$
> Vzorec platí jen tehdy, když je integrand spojitý na **celém** intervalu mezi mezemi. $\int_{-1}^1 \frac{1}{t^2}\,\mathrm{d}t$ tabulkou ($[-\frac{1}{t}]_{-1}^1 = -2$) spočítat nejde: $\frac{1}{t^2}$ v nule spojitá není (ani definovaná), a záporný výsledek pro kladnou funkci prozrazuje nesmysl.

## §2 Linearita integrálu

> [!veta] Věta · slajd 7 (linearita určitého integrálu)
> ==Pro funkce $f, g$ spojité na $[a; b]$ a pro libovolná $r, s \in \mathbb{R}$== platí
>
> $$
> \mathbf{\int_a^b (r \cdot f + s \cdot g) = r \cdot \int_a^b f + s \cdot \int_a^b g}.
> $$
>
> > [!note]- Důkaz
> > Ať $F$, $G$ jsou primitivní k $f$, $g$. Podle [[věta o aritmetice derivací|linearity derivace]] je $(rF + sG)' = rf + sg$, takže $rF + sG$ je primitivní k $rf + sg$ a
> >
> > $$
> > \int_a^b (rf + sg) = [rF + sG]_a^b = r(F(b) - F(a)) + s(G(b) - G(a)) = r\int_a^b f + s\int_a^b g.
> > $$

^veta-linearita

> [!lidsky] Lidsky
> Integrál součtu je součet integrálů a konstanty se vytknou před integrál. Mnohočlen tak integruješ člen po členu. Platí to proto, že derivace se chová stejně.

> [!example] Příklad (slajd 7)
> $$
> \int_2^6 (-3t^4 - 5t^2 + 12\cos t)\,\mathrm{d}t = -3\left[\frac{t^5}{5}\right]_2^6 - 5\left[\frac{t^3}{3}\right]_2^6 + 12[\sin t]_2^6 = -3 \cdot \frac{7744}{5} - 5 \cdot \frac{208}{3} + 12(\sin 6 - \sin 2),
> $$
>
> tedy $-\frac{74896}{15} + 12(\sin 6 - \sin 2) \approx -5007{,}33$.

> [!pozor] Linearita není multiplikativita
> $\int_a^b f \cdot g \ne \int_a^b f \cdot \int_a^b g$. Třeba $\int_0^1 x \cdot x\,\mathrm{d}x = \frac{1}{3}$, ale $\int_0^1 x \cdot \int_0^1 x = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. Na součin je per partes.

## §3 Metoda per partes

> [!veta] Věta · slajd 8 (metoda per partes)
> ==Ať $f$, $g$ mají spojité derivace na $[a; b]$.== Potom
>
> $$
> \int_a^b f' \cdot g + \int_a^b f \cdot g' = [f \cdot g]_a^b, \quad\text{neboli}\quad \mathbf{\int_a^b f' \cdot g = [f \cdot g]_a^b - \int_a^b f \cdot g'}.
> $$
>
> > [!note]- Důkaz
> > Podle pravidla pro derivaci součinu je $(fg)' = f'g + fg'$, takže $fg$ je primitivní k $f'g + fg'$ (tato funkce je spojitá, protože $f, f', g, g'$ jsou spojité). Tedy $\int_a^b (f'g + fg') = [fg]_a^b$ a podle linearity se integrál součtu rozdělí na dva.

^veta-per-partes

> [!lidsky] Lidsky
> Per partes (po částech) přehodí derivaci z jednoho činitele na druhý za cenu „hraniční“ závorky $[fg]_a^b$. Vyplatí se, když činitel $g$ derivováním zjednodušíš (polynom, $\ln$) a druhý činitel umíš integrovat (sinus, exponenciála).

> [!example] Příklad (slajd 8)
> $\int_3^7 t \cdot \sin t\,\mathrm{d}t$: zvolíme $g(t) = t$ (derivace $1$) a $f'(t) = \sin t$, tedy $f(t) = -\cos t$:
>
> $$
> \int_3^7 t \sin t\,\mathrm{d}t = [-t\cos t]_3^7 - \int_3^7 1 \cdot (-\cos t)\,\mathrm{d}t = [-t\cos t]_3^7 + [\sin t]_3^7 = (-7\cos 7 + 3\cos 3) + (\sin 7 - \sin 3) \approx -7{,}73.
> $$

> [!obrazek] Per partes jako skládačka obdélníků
> ![[ma112-per-partes.png]]
> *Oranžová křivka je $(u; v) = (f(x); g(x)) = (x; x^2)$ pro $x \in [1; 2]$. Modrá plocha pod ní je $\int g\,\mathrm{d}f = \int_1^2 x^2\,\mathrm{d}x = \frac{7}{3}$, zelená plocha vlevo od ní $\int f\,\mathrm{d}g = \int_1^2 x \cdot 2x\,\mathrm{d}x = \frac{14}{3}$. Dohromady vyplní velký obdélník $2 \cdot 4 = 8$ bez červeného malého $1 \cdot 1$: $\frac{7}{3} + \frac{14}{3} = 7 = [fg]_1^2$.*

> [!pozor] Špatná volba činitelů
> V $\int t\sin t$ s volbou $f' = t$, $g = \sin t$ vyjde $[\frac{t^2}{2}\sin t] - \int \frac{t^2}{2}\cos t$: mocnina vzrostla a integrál je těžší. Derivovat chceš ten činitel, který se derivováním zjednoduší.

## §4 Věta o substituci

> [!veta] Věta · slajd 9 (o substituci v určitém integrálu)
> ==Ať $\varphi$ je spojitá na $[a; b]$ a má na $[a; b]$ spojitou derivaci. Ať $f$ je taková, že složená funkce $f \circ \varphi$ je spojitá na $[a; b]$.== Potom
>
> $$
> \mathbf{\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t = \int_a^b f(\varphi(z)) \cdot \varphi'(z)\,\mathrm{d}z}.
> $$
>
> > [!note]- Důkaz
> > Ať $F$ je primitivní k $f$. Pak $\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t = F(\varphi(b)) - F(\varphi(a)) = (F \circ \varphi)(b) - (F \circ \varphi)(a)$. Podle [[věta o derivaci složené funkce|Chain Rule]] je $\frac{\mathrm{d}}{\mathrm{d}z}(F \circ \varphi)(z) = F'(\varphi(z)) \cdot \varphi'(z) = f(\varphi(z)) \cdot \varphi'(z)$, takže $F \circ \varphi$ je primitivní k integrandu vpravo a pravý integrál je také $(F \circ \varphi)(b) - (F \circ \varphi)(a)$.

^veta-substituce-integral

> [!lidsky] Lidsky
> Když v integrandu vidíš „vnitřní funkci“ $\varphi(z)$ a vedle ní její derivaci $\varphi'(z)$, celou dvojici nahradíš novou proměnnou $t = \varphi(z)$. Meze se přepočítají stejnou funkcí: $a \mapsto \varphi(a)$, $b \mapsto \varphi(b)$. Je to Chain Rule čtená pozpátku.

> [!example] Příklad
> $\int_0^{\sqrt{\pi/2}} \cos(z^2) \cdot 2z\,\mathrm{d}z$: je to $f(\varphi(z))\varphi'(z)$ s $\varphi(z) = z^2$, $f = \cos$. Meze: $\varphi(0) = 0$, $\varphi(\sqrt{\pi/2}) = \frac{\pi}{2}$. Tedy integrál $= \int_0^{\pi/2} \cos t\,\mathrm{d}t = [\sin t]_0^{\pi/2} = 1$.

> [!obrazek] Substituce zachová hodnotu integrálu
> ![[ma112-substituce.png]]
> *Vlevo modrá plocha pod $\cos(z^2) \cdot 2z$ pro $z \in [0; \sqrt{\pi/2}]$, vpravo zelená plocha pod $\cos t$ pro $t \in [0; \frac{\pi}{2}]$. Oranžové čárkované čáry jsou horní meze, spojené vztahem $t = \varphi(z) = z^2$. Obě plochy mají velikost $1$, i když tvary se liší.*

### Formální zápis: $\mathrm{d}t = \varphi'(z)\,\mathrm{d}z$ (slajdy 10–11)

Pro praktický výpočet se věta píše „nepořádně“: zavedeme $t = \varphi(z)$ a z $\frac{\mathrm{d}t}{\mathrm{d}z} = \varphi'(z)$ „vynásobením“ dostaneme $\mathrm{d}t = \varphi'(z)\,\mathrm{d}z$. Tím se v integrálu nahradí jak $\varphi(z)$, tak $\varphi'(z)\,\mathrm{d}z$ a meze se přepočítají. Je to jen mnemotechnika: zlomek $\frac{\mathrm{d}t}{\mathrm{d}z}$ zlomkem není a zdůvodnit „násobení“ by vyžadovalo teorii diferenciálních forem. Správnost zaručuje věta o substituci. ^formalni-zapis

> [!example] Příklad (slajdy 10–11)
> $\int_0^2 \frac{x^2}{(x^3 + 2)^4}\,\mathrm{d}x$. Zavedeme $t = x^3 + 2$, pak $\mathrm{d}t = 3x^2\,\mathrm{d}x$, tedy $x^2\,\mathrm{d}x = \frac{1}{3}\mathrm{d}t$. Meze: $x = 0 \mapsto t = 2$, $x = 2 \mapsto t = 10$.
>
> $$
> \int_0^2 \frac{x^2}{(x^3 + 2)^4}\,\mathrm{d}x = \int_2^{10} \frac{1}{3t^4}\,\mathrm{d}t = \frac{1}{3}\left[-\frac{1}{3t^3}\right]_2^{10} = \frac{1}{3}\left(-\frac{1}{3000} + \frac{1}{24}\right) = \frac{31}{2250}.
> $$

> [!pozor] Primitivní funkce k $t^{-4}$
> $\int t^{-4}\,\mathrm{d}t$ podle tabulky s $n = -4$: $\frac{t^{-3}}{-3} = -\frac{1}{3t^3}$. Exponent se **zvýší** o $1$ a dělí se **novým** exponentem. Častá chyba je vydělit $-4$ a exponent nechat: $-\frac{1}{4t^4}$ je špatně. Kontrola derivováním: $\left(-\frac{1}{3}t^{-3}\right)' = t^{-4}$. ✓

> [!example] Příklad (slajd 12): dvě substituce za sebou
> $I = \int_5^{15} \frac{\sqrt{x} - 1}{\sqrt{x}\,(x - 2\sqrt{x} + 2)^2}\,\mathrm{d}x$.
>
> 1. $t = \sqrt{x}$, $\mathrm{d}t = \frac{1}{2\sqrt{x}}\,\mathrm{d}x$, meze $\sqrt{5}$ a $\sqrt{15}$: $I = \int_{\sqrt{5}}^{\sqrt{15}} \frac{2(t - 1)}{(t^2 - 2t + 2)^2}\,\mathrm{d}t = \int_{\sqrt{5}}^{\sqrt{15}} \frac{2(t - 1)}{((t - 1)^2 + 1)^2}\,\mathrm{d}t$.
> 2. $u = (t - 1)^2 + 1$, $\mathrm{d}u = 2(t - 1)\,\mathrm{d}t$: $I = \int_{(\sqrt{5} - 1)^2 + 1}^{(\sqrt{15} - 1)^2 + 1} \frac{1}{u^2}\,\mathrm{d}u = \left[-\frac{1}{u}\right]_{(\sqrt{5} - 1)^2 + 1}^{(\sqrt{15} - 1)^2 + 1} \approx 0{,}2875$.

### Směr substituce a past (slajd 13)

Rovnost ve větě se dá číst dvěma směry. **Zprava doleva** (jednodušší): v integrálu $\int_a^b \dots\,\mathrm{d}z$ poznáš tvar $f(\varphi(z))\varphi'(z)$ a nahradíš ho $\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t$; meze vzniknou dosazením a nic se nemusí hlídat. **Zleva doprava** (pozor): zadaný integrál $\int_c^d f(t)\,\mathrm{d}t$ přepíšeš dosazením $t = \varphi(z)$, a k tomu musíš **najít** $a, b$ s $\varphi(a) = c$ a $\varphi(b) = d$ a ověřit předpoklady věty na $[a; b]$. Takové $a$, $b$ existovat nemusí. ^smer-substituce

> [!example] Příklad (slajd 13): bezmyšlenkovitá substituce
> $I = \int_0^2 \sqrt[3]{1 - x^2}\,\mathrm{d}x$. Nabízí se $x = \cos t$, $\mathrm{d}x = -\sin t\,\mathrm{d}t$ a „$I = -\int_0^2 \sqrt[3]{1 - \cos^2 t}\,\sin t\,\mathrm{d}t = -\int_0^2 \sin^{5/3} t\,\mathrm{d}t$“. Výsledek je nepříjemný integrál, ale to není hlavní problém. Jde o substituci zleva doprava, takže by mělo platit $I = \int_{\varphi(a)}^{\varphi(b)} \sqrt[3]{1 - x^2}\,\mathrm{d}x$ s $\varphi = \cos$, $\varphi(a) = 0$, $\varphi(b) = 2$. **Žádné $b$ s $\cos b = 2$ neexistuje**, takže substituce je špatně (a meze $0$, $2$ v $t$ jsou prostě opsané, nepřepočítané).

> [!obrazek] Proč $x = \cos t$ nemůže pokrýt meze $0$ až $2$
> ![[ma112-spatna-substituce.png]]
> *Modrá křivka $\varphi(t) = \cos t$ se drží v pásu $[-1; 1]$ (světle modrý). Zelená dolní mez $x = 0$ se zasáhne (např. $t = \frac{\pi}{2}$), červená horní mez $x = 2$ nikdy.*

> [!navic] Obtížnost na testu
> Příklady obtížnosti slajdů 12–13 (několik substitucí za sebou, past substituce zleva doprava) se v semestrálních testech počítat nebudou (sdělení přednášejícího 4. 11. 2026). Ze slajdu 13 si odnes princip: u substituce zleva doprava je potřeba ověřit meze. Další, rafinovanější substituce přijdou v handoutu 7A.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Dokaž, že $\int_a^b f'(t)\,\mathrm{d}t = f(b) - f(a)$, má-li $f$ na $[a; b]$ spojitou derivaci.
> $f'$ je spojitá a **$f$ je k ní primitivní** ($f$ má derivaci $f'$). Podle **fundamentální věty** (bod 3) je integrál rozdíl hodnot primitivní funkce v mezích: $f(b) - f(a)$.

> [!karta|02]- Proč při výpočtu $\int_a^b f = [F]_a^b$ nezáleží na tom, kterou primitivní funkci $F$ vezmeš?
> Dvě primitivní se **liší o konstantu**: $G = F + c$. Pak $[G]_a^b = (F(b) + c) - (F(a) + c) = F(b) - F(a)$, **konstanta se odečte**.

> [!karta|03]- Proč $\int_{10}^{15} t^2\,\mathrm{d}t = \int_{10}^{15} x^2\,\mathrm{d}x$ a proč je zápis $\int_0^x f(x)\,\mathrm{d}x$ chybný?
> Integrační proměnná je **vázaná**: výsledek závisí jen na mezích a funkci, ne na jménu proměnné (jako $(\forall x)\alpha(x)$ a $(\forall y)\alpha(y)$). V $\int_0^x f(x)\,\mathrm{d}x$ je **totéž $x$ zároveň vázané a volné** (horní mez); správně $\int_0^x f(t)\,\mathrm{d}t$.

> [!karta|04]- Dokaž linearitu určitého integrálu: $\int_a^b (rf + sg) = r\int_a^b f + s\int_a^b g$ pro spojité $f, g$.
> Ať $F$, $G$ jsou primitivní k $f$, $g$. **$(rF + sG)' = rf + sg$**, takže $rF + sG$ je primitivní k $rf + sg$ a $\int_a^b (rf + sg) = [rF + sG]_a^b = r[F]_a^b + s[G]_a^b$.

> [!karta|05]- Dokaž metodu per partes $\int_a^b f'g = [fg]_a^b - \int_a^b fg'$.
> **$(fg)' = f'g + fg'$**, takže $fg$ je primitivní k $f'g + fg'$ a $\int_a^b (f'g + fg') = [fg]_a^b$. **Linearita** rozdělí levou stranu na $\int f'g + \int fg'$; odečtením vyjde vzorec.

> [!karta|06]- Proč se v metodě per partes předpokládá, že $f$ a $g$ mají na $[a; b]$ spojité derivace?
> Aby integrandy **$f'g$ a $fg'$ byly spojité**: jen pro spojité funkce máme určitý integrál zavedený a jen pro ně platí fundamentální věta (existence primitivní funkce). Spojitost $f$, $g$ plyne z existence derivace.

> [!karta|07]- Jak v per partes volíš, který činitel derivovat a který integrovat? Ukaž na $\int t\sin t\,\mathrm{d}t$.
> Derivuj činitel, který se **derivováním zjednoduší** (polynom, $\ln$), integruj ten, který integrovat **umíš bez zhoršení** ($\sin$, $e^t$). Pro $t\sin t$: $g = t$, $f' = \sin t$, zbude $\int \cos t$. Opačná volba dá $\int \frac{t^2}{2}\cos t$, **horší** integrál.

> [!karta|08]- Dokaž větu o substituci $\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t = \int_a^b f(\varphi(z))\varphi'(z)\,\mathrm{d}z$.
> Ať $F$ je primitivní k $f$; levá strana je $F(\varphi(b)) - F(\varphi(a))$. Podle **Chain Rule** je $(F \circ \varphi)'(z) = f(\varphi(z))\varphi'(z)$, takže **$F \circ \varphi$ je primitivní k pravému integrandu** a pravá strana je $(F \circ \varphi)(b) - (F \circ \varphi)(a)$, totéž.

> [!karta|09]- Které tři předpoklady má věta o substituci v určitém integrálu a k čemu jsou?
> $\varphi$ **spojitá na $[a; b]$**, $\varphi$ má **spojitou derivaci** a **$f \circ \varphi$ je spojitá** na $[a; b]$. Pak je integrand $f(\varphi(z))\varphi'(z)$ spojitý, integrál vpravo existuje a v důkazu jde použít Chain Rule a fundamentální větu.

> [!karta|10]- Čím se liší použití substituce „zprava doleva“ a „zleva doprava“ a který směr je bezpečnější?
> **Zprava doleva**: v integrandu poznáš $f(\varphi(z))\varphi'(z)$ a meze **jen dosadíš** do $\varphi$; bezpečné. **Zleva doprava**: dosazuješ $t = \varphi(z)$ a musíš **najít $a, b$ s $\varphi(a)$, $\varphi(b)$ rovnými zadaným mezím** a ověřit předpoklady; taková čísla nemusí existovat.

> [!karta|11]- Proč je substituce $x = \cos t$ v $\int_0^2 \sqrt[3]{1 - x^2}\,\mathrm{d}x$ chybná?
> Je to substituce **zleva doprava**, takže by muselo platit $\cos a = 0$ a $\cos b = 2$. **Kosinus nikdy nenabývá hodnoty $2$** ($|\cos t| \le 1$), takže potřebné $b$ neexistuje a meze $0$, $2$ nejde přepočítat.

> [!karta|12]- Co se při substituci $t = \varphi(x)$ stane s mezemi a proč se pak nevracíš k proměnné $x$?
> Meze se **přepočítají**: dolní na $\varphi(a)$, horní na $\varphi(b)$. Nový integrál v $t$ je **číslo**, které se rovná původnímu, takže ho dopočítáš rovnou v $t$, bez zpětného dosazování.

> [!karta|13]- Co znamená zápis $\mathrm{d}t = \varphi'(z)\,\mathrm{d}z$ a proč ho lze používat?
> Je to **mnemotechnika**: vznikne „vynásobením“ $\frac{\mathrm{d}t}{\mathrm{d}z} = \varphi'(z)$, i když $\frac{\mathrm{d}t}{\mathrm{d}z}$ není zlomek (rigorózně by to chtělo diferenciální formy). Používat ho lze, protože výsledek přepisu je přesně **věta o substituci**.

### Příklady na procvičení

> [!priklad|14]- Spočítej $\int_1^3 (3x^2 - 4x + 1)\,\mathrm{d}x$.
> Linearita a tabulka: $[x^3 - 2x^2 + x]_1^3 = (27 - 18 + 3) - (1 - 2 + 1) =$ **$12$**.

> [!priklad|15]- Spočítej per partes $\int_0^1 x e^x\,\mathrm{d}x$.
> $g = x$, $f' = e^x$, $f = e^x$: $[xe^x]_0^1 - \int_0^1 e^x\,\mathrm{d}x = e - (e - 1) =$ **$1$**.

> [!priklad|16]- Spočítej $\int_1^e \ln x\,\mathrm{d}x$.
> Per partes s $f' = 1$, $f = x$, $g = \ln x$, $g' = \frac{1}{x}$: $[x\ln x]_1^e - \int_1^e x \cdot \frac{1}{x}\,\mathrm{d}x = e - (e - 1) =$ **$1$**.

> [!priklad|17]- Spočítej $\int_0^1 x^2 e^x\,\mathrm{d}x$.
> Per partes dvakrát: $[x^2e^x]_0^1 - 2\int_0^1 xe^x\,\mathrm{d}x = e - 2 \cdot 1 =$ **$e - 2 \approx 0{,}718$** (druhý integrál je příklad 15).

> [!priklad|18]- Spočítej substitucí $\int_0^1 \frac{2x}{x^2 + 1}\,\mathrm{d}x$.
> $t = x^2 + 1$, $\mathrm{d}t = 2x\,\mathrm{d}x$, meze $1$ a $2$: $\int_1^2 \frac{1}{t}\,\mathrm{d}t = \ln 2 - \ln 1 =$ **$\ln 2 \approx 0{,}693$**.

> [!priklad|19]- Spočítej $\int_0^{\pi/2} \sin^2 x \cos x\,\mathrm{d}x$.
> $t = \sin x$, $\mathrm{d}t = \cos x\,\mathrm{d}x$, meze $\sin 0 = 0$, $\sin\frac{\pi}{2} = 1$: $\int_0^1 t^2\,\mathrm{d}t =$ **$\frac{1}{3}$**.

> [!priklad|20]- Spočítej $\int_0^{1/2} \frac{1}{\sqrt{1 - t^2}}\,\mathrm{d}t$.
> Tabulka: $[\arcsin t]_0^{1/2} = \arcsin\frac{1}{2} - 0 =$ **$\frac{\pi}{6}$**. Integrand je spojitý na $[0; \frac{1}{2}] \subseteq (-1; 1)$.

### Typové příklady na semestrální test

*Stejný typ úloh jako v ukázce k 2. semestrálnímu testu (J. Velebil, 7.–11. 12. 2026, témata 06A–08A). Odpovídej celou větou a každé tvrzení zdůvodni; obrázek není argument.*

> [!priklad|21]- Pečlivě zformulujte větu o substituci v určitém integrálu (s předpoklady, českými větami).
> Ať je funkce $\varphi$ spojitá na omezeném uzavřeném intervalu $[a; b]$ a má na něm spojitou derivaci. Ať je $f$ funkce taková, že složená funkce $f \circ \varphi$ je spojitá na $[a; b]$. Potom **platí $\int_{\varphi(a)}^{\varphi(b)} f(t)\,\mathrm{d}t = \int_a^b f(\varphi(z)) \cdot \varphi'(z)\,\mathrm{d}z$**.

> [!priklad|22]- Pečlivě zformulujte větu o linearitě určitého integrálu.
> Ať jsou funkce $f$ a $g$ spojité na omezeném uzavřeném intervalu $[a; b]$ a ať $r, s$ jsou libovolná reálná čísla. Potom **platí $\int_a^b (r \cdot f + s \cdot g) = r \cdot \int_a^b f + s \cdot \int_a^b g$**.

> [!priklad|23]- Dokažte nebo vyvraťte: Ať $f$ má na $[0; 2]$ spojitou derivaci, $f(0) = 1$ a $f(2) = 5$. Potom existuje $p \in [0; 2]$ s $f'(p) \ge 2$.
> **Tvrzení platí.** Protože $f'$ je spojitá, je $\int_0^2 f'(t)\,\mathrm{d}t = f(2) - f(0) = 4$. Podle omezenosti integrálu je $4 \le (2 - 0) \cdot \max_{[0; 2]} f'$, tedy $\max f' \ge 2$. Spojitá $f'$ na $[0; 2]$ maxima nabývá v nějakém bodě $p$, a v něm je $f'(p) \ge 2$.

> [!priklad|24]- Najděte stacionární body funkce $x \mapsto \int_0^x \cos\left(t + \frac{\pi}{2}\right)\mathrm{d}t$ na intervalu $[1; 7]$.
> Integrand je spojitý, takže podle věty o derivaci integrálu podle horní meze je derivace funkce $\cos\left(x + \frac{\pi}{2}\right) = -\sin x$. Ta je nulová pro $x = k\pi$; v intervalu $[1; 7]$ leží **$x = \pi$ a $x = 2\pi$** ($2\pi \approx 6{,}28 < 7$, $3\pi > 7$, $0 < 1$). To jsou stacionární body.

> [!priklad|25]- Nalezněte velikost plochy obrazce ohraničeného grafy funkcí $y = x$ a $y = x^2$.
> Grafy se protínají pro $x = x^2$, tj. v $x = 0$ a $x = 1$; na $[0; 1]$ je $x \ge x^2$. Podle linearity je plocha $\int_0^1 (x - x^2)\,\mathrm{d}x = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3}$, tedy **$\frac{1}{6}$**.

---
← [[MA1 11 – Lemma o konvexních funkcích a axiomatický integrál|29. 10. 2026 Lemma o konvexních funkcích a axiomatický integrál]]

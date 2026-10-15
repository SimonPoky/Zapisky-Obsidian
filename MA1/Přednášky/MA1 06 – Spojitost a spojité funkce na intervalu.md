---
predmet: MA1
prednaska: 6
datum: 2026-10-08
zdroj: "Handout 3A (Spojitost funkce), slajdy 3–17, 19 a 20"
tags: [prednaska, MA1]
---

# MA1 06 – Spojitost a spojité funkce na intervalu

*Přednáška 6 · čtvrtek 8. 10. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 3A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout03a.pdf)

Témata: `spojitost přes okolí a ε-δ` · `spojitost zleva a zprava` · `|x| je spojitá` · `aritmetika spojitých funkcí` · `složená funkce` · `Heineova věta` · `sin(1/x)` · `spojitost na [a; b]` · `lokální a aditivní systém` · `Creeping Theorem` · `IVT, BT, EVT, PIT` · `patologická funkce` · `věta o pevném bodě`

Minule přišla definice [[spojitost v bodě|spojitosti v bodě]]: limita v $p$ se rovná hodnotě $f(p)$. Dnes se z ní stal nástroj. Spojité funkce se dají sčítat, násobit, dělit a skládat a zůstanou spojité; nespojitost se nejsnáz dokazuje posloupnostmi (Heineova věta). Druhá polovina patřila funkcím spojitým na celém uzavřeném intervalu $[a; b]$: jedna obecná metoda důkazu, *Creeping Theorem*, dá najednou čtyři velké věty (mezihodnota, omezenost, extrémy, obraz je interval) a z nich větu o pevném bodě.

## §0 Přehled na jedné stránce

| tvrzení | předpoklad | závěr |
|---|---|---|
| spojitost v $p$ | $f$ definovaná na okolí $p$ | $\lim_{x \to p} f(x) = f(p)$, ekvivalentně $\forall U \ni f(p)\ \exists V \ni p: f[V] \subseteq U$ |
| jednostranná spojitost | | $f$ spojitá v $p$ $\iff$ spojitá zleva i zprava v $p$ |
| aritmetika | $f, g$ spojité v $p$ | $\lvert f \rvert$, $f \pm g$, $f \cdot g$ spojité v $p$; $\frac{f}{g}$ navíc při $g(p) \neq 0$ |
| složená funkce | $f$ spojitá v $p$, $g$ spojitá v $f(p)$ | $g \circ f$ spojitá v $p$ (jednostranně **neplatí**) |
| Heineova věta | $f$ definovaná v $p$ a kolem $p$ | spojitá v $p$ $\iff$ $\lim f(x_n) = f(p)$ pro **každou** $x_n \to p$ |
| Creeping Theorem | $\mathcal{A}$ lokální a aditivní na $[a; b]$ | $[a; b] \in \mathcal{A}$ |
| IVT | $f$ spojitá na $[a; b]$, $r$ mezi $f(a)$ a $f(b)$ | existuje $t \in [a; b]$, $f(t) = r$ |
| BT | $f$ spojitá na $[a; b]$ | $f$ je na $[a; b]$ omezená |
| EVT | $f$ spojitá na $[a; b]$ | $f$ na $[a; b]$ nabývá maxima i minima |
| PIT | $f$ spojitá na $[a; b]$ | $f\big[\,[a; b]\,\big] = [\min f; \max f]$, interval |
| pevný bod | $f: [a; b] \to [a; b]$ spojitá | existuje $t$, $f(t) = t$ |

## §1 Spojitost v bodě podruhé

> [!definice] Spojitost v bodě, tři ekvivalentní zápisy · handout 3A, slajd 3
> Ať $f$ je definovaná na nějakém okolí bodu $p \in \mathbb{R}$, včetně bodu $p$. Následující říká totéž:
>
> 1. $\lim_{x \to p} f(x) = f(p)$,
> 2. pro **každé** okolí $U$ bodu $f(p)$ **existuje** okolí $V$ bodu $p$ tak, že $f[V] \subseteq U$,
> 3. pro **každé** $\varepsilon > 0$ **existuje** $\delta > 0$ tak, že $\lvert x - p \rvert < \delta \Rightarrow \lvert f(x) - f(p) \rvert < \varepsilon$.

^spojitost-tri-zapisy

> [!lidsky] Lidsky
> Je to hra se soupeřem jako u limity: soupeř zvolí terč $U$ kolem $f(p)$, ty musíš najít okolí $V$ kolem $p$, které celé padne do terče. Rozdíl proti limitě: $V$ je **plné** okolí, bod $p$ v něm leží, a terč je kolem $f(p)$, ne kolem nějakého $L$. Proto spojitost zaručí, že $f(p)$ „nevyskočí“ z grafu.

> [!obrazek] Spojitost přes okolí
> ![[ma106-okoli.png]]
> *Oranžové okolí V bodu p (i s bodem p) se zobrazí do zelené množiny f[V], která celá leží v modrém terči U kolem f(p). Pro každý, jakkoli malý terč U musí jít takové V najít.*

> [!pozor] Spojitost vs. limita
> U limity se bere [[prstencové okolí]] a hodnota $f(p)$ nehraje roli, nemusí ani existovat. U spojitosti musí $f(p)$ existovat a okolí je plné. Funkce s limitou v $p$ proto ještě nemusí být spojitá: $f(z) = 3$ pro $z \neq 1$, $f(1) = 200$ má limitu $3$, ale spojitá v $1$ není.

### Jednostranná spojitost

> [!definice] Spojitost zleva a zprava · handout 3A, slajd 3
> $f$ je **spojitá zleva** v $p$, když je definovaná v $p$ a ve směru $x \to p^-$ a $\lim_{x \to p^-} f(x) = f(p)$. **Spojitá zprava** obdobně s $x \to p^+$.

^def-jednostranna-spojitost

> [!veta] Tvrzení · handout 3A, slajd 3
> **$f$ je spojitá v $p$, právě když je v $p$ spojitá zleva i zprava.**

^tvrzeni-jednostranna-spojitost

> [!lidsky] Lidsky
> [[jednostranná spojitost|Jednostranná spojitost]] je spojitost, při které se díváš jen z jedné strany. Plyne z toho, že oboustranná limita existuje, právě když se shodují obě [[jednostranná limita|jednostranné limity]]: tady se obě musí rovnat $f(p)$. Typické použití: v krajních bodech intervalu $[a; b]$, kde se dá přijít jen z jedné strany.

> [!obrazek] Skok, který je spojitý zprava
> ![[ma106-zprava.png]]
> *Modře funkce $f(x) = 0$ pro $x < 1$ a $f(x) = 1$ pro $x \ge 1$. Zelený plný bod je hodnota $f(1) = 1$, prázdný kroužek hodnota, kterou funkce nenabude. Zelená šipka: zprava se hodnoty blíží k $1 = f(1)$, funkce je spojitá zprava. Červená šipka: zleva se blíží k $0 \neq f(1)$, spojitá zleva ani v bodě $1$ není.*

### Příklad: $\lvert x \rvert$ je spojitá v každém bodě

> [!example] $f(x) = \lvert x \rvert$, důkaz přes ε-δ
> Soupeř zadá $\varepsilon > 0$, hledáme $\delta > 0$ tak, že $\lvert x - p \rvert < \delta \Rightarrow \big\lvert \lvert x \rvert - \lvert p \rvert \big\rvert < \varepsilon$. Stačí **$\delta = \varepsilon$**, protože podle obrácené trojúhelníkové nerovnosti
>
> $$
> \big\lvert \lvert x \rvert - \lvert p \rvert \big\rvert \le \lvert x - p \rvert < \delta = \varepsilon.
> $$

^priklad-abs

> [!navic] Obrácená trojúhelníková nerovnost
> Z [[absolutní hodnota|trojúhelníkové nerovnosti]] $\lvert x \rvert = \lvert (x - p) + p \rvert \le \lvert x - p \rvert + \lvert p \rvert$, tedy $\lvert x \rvert - \lvert p \rvert \le \lvert x - p \rvert$. Prohozením $x$ a $p$ dostaneš totéž pro $\lvert p \rvert - \lvert x \rvert$, a obojí dohromady je $\big\lvert \lvert x \rvert - \lvert p \rvert \big\rvert \le \lvert x - p \rvert$. Lidsky: rozdíl vzdáleností od nuly je nejvýš vzdálenost těch dvou bodů.

> [!obrazek] δ = ε u absolutní hodnoty
> ![[ma106-abs.png]]
> *Modrý pás je terč |p| ± ε, oranžový pás okolí p ± δ s δ = ε. Zelená část grafu nad oranžovým pásem leží celá v modrém pásu, protože |x| má sklon nejvýš 1.*

## §2 Aritmetika a skládání spojitých funkcí

> [!veta] Věta o aritmetice spojitých funkcí · handout 3A, slajd 4
> ==Ať $f$ a $g$ jsou spojité v $p$.== Potom **$\lvert f \rvert$, $f + g$, $f - g$ a $f \cdot g$ jsou spojité v $p$**. Je-li navíc ==$g(p) \neq 0$==, je **spojitá v $p$ i $\frac{f}{g}$**. Totéž platí pro spojitost zleva i zprava.
>
> > [!note]- Důkaz
> > Pro $\star \in \{+, -, \cdot, /\}$ podle [[věta o aritmetice limit|aritmetiky limit]]: $\lim (f \star g) = \lim f \star \lim g = f(p) \star g(p) = (f \star g)(p)$. Výraz $f(p) \star g(p)$ je reálné číslo, takže je vždy definovaný; u dělení díky $g(p) \neq 0$. Pro $\lvert f \rvert$ stačí složit $f$ se spojitou funkcí $\lvert x \rvert$ (§1) a použít větu o složené funkci níže.

^veta-aritmetika-spojitych

> [!lidsky] Lidsky
> [[věta o aritmetice spojitých funkcí|Aritmetika spojitých funkcí]]: ze spojitých funkcí sčítáním, násobením a dělením (ne nulou) vznikají zase spojité funkce. Proto jsou spojité všechny polynomy (vyrobené z konstant a $x$) a všechny racionální funkce mimo kořeny jmenovatele. A spojitou funkci smíš v limitě prostě **dosadit**.

> [!veta] Věta o spojitosti složené funkce · handout 3A, slajd 5
> ==Ať $f$ je spojitá v $p$ a $g$ je spojitá v $f(p)$.== Potom **$g \circ f$ je spojitá v $p$**.
>
> > [!note]- Důkaz
> > Ať $U$ je okolí $g(f(p))$. Ze spojitosti $g$ v $f(p)$ existuje okolí $W$ bodu $f(p)$ s $g[W] \subseteq U$. Ze spojitosti $f$ v $p$ existuje okolí $V$ bodu $p$ s $f[V] \subseteq W$. Potom
> >
> > $$
> > (g \circ f)[V] = g\big[f[V]\big] \subseteq g[W] \subseteq U.
> > $$

^veta-slozena

> [!lidsky] Lidsky
> [[věta o spojitosti složené funkce|Složená funkce]] a řetěz terčů pozpátku: terč kolem $g(f(p))$ určí, jak blízko $f(p)$ musíš být, a to zase, jak blízko $p$. Je to stejný důkaz jako u [[věta o substituci|věty o substituci]], ale bez starosti „nedopadnout do cíle“: díky spojitosti $g$ do cíle $f(p)$ dopadnout smíš, hodnota tam sedí.

### Jednostranná verze neplatí

> [!example] Protipříklad · handout 3A, slajd 5
> $$
> f(x) = -x^2 + 1, \qquad g(z) = \begin{cases} 2, & z \ge 1, \\ 0, & z < 1. \end{cases}
> $$
>
> - $f$ je spojitá zprava v $0$: $\lim_{x \to 0^+} f(x) = 1 = f(0)$.
> - $g$ je spojitá zprava v $1 = f(0)$: $\lim_{z \to 1^+} g(z) = 2 = g(1)$.
> - Ale $g(f(x)) = 2$ pro $x = 0$ a $0$ pro $x \neq 0$ (tam $f(x) < 1$), takže $\lim_{x \to 0^+} g(f(x)) = 0 \neq 2 = g(f(0))$.

^protipriklad-jednostranna

> [!obrazek] Proč se zprava pokazí
> ![[ma106-slozena.png]]
> *Vlevo f: pro x jdoucí k 0 zprava (oranžová část) se hodnoty f blíží k 1 **zdola**. Uprostřed g: oranžový pás ukazuje, kam tyto hodnoty padají, totiž nalevo od skoku, kde g = 0. Vpravo výsledek g(f(x)): všude 0, jen v bodě 0 hodnota 2.*

> [!pozor] Strana se při skládání může otočit
> Spojitost zprava u $f$ říká jen, odkud přicházejí $x$, ne odkud přicházejí hodnoty $f(x)$. Rostoucí $x$ tu dává klesající $f(x)$, takže z $x \to 0^+$ se stane $z \to 1^-$, a zleva $g$ spojitá není. Oboustranná spojitost takový problém nemá.

## §3 Heineova věta: spojitost přes posloupnosti

> [!veta] Heineova věta o spojitosti · handout 3A, slajd 6
> ==Ať $f$ je definovaná v bodě $p$ a ve směru $x \to p$.== Následující je ekvivalentní:
>
> 1. **$f$ je spojitá v $p$**, tj. $\lim_{x \to p} f(x) = f(p)$.
> 2. **Pro každou posloupnost $x_n$ s $\lim_{n \to +\infty} x_n = p$ platí $\lim_{n \to +\infty} f(x_n) = f(p)$.**
>
> > [!note]- Důkaz (1) ⇒ (2)
> > Ať $U$ je okolí $f(p)$. Ze spojitosti existuje okolí $V$ bodu $p$ s $f[V] \subseteq U$. Protože $x_n \to p$, leží $x_n$ od jistého $n_0$ ve $V$, a tedy $f(x_n) \in U$ pro $n \ge n_0$. Na rozdíl od [[věta o substituci|věty o substituci]] nevadí, když $x_n = p$: $p$ leží ve $V$ a $f(p) \in U$.
> >
> > Směr (2) ⇒ (1) se nedokazuje; potřebuje slabou verzi axiomu výběru.

^veta-heine

> [!lidsky] Lidsky
> [[Heineova věta]] říká, že spojitá funkce „respektuje posloupnosti“: když se body $x_n$ blíží k $p$, hodnoty $f(x_n)$ se blíží k $f(p)$. A naopak, stačí najít **jedinou** posloupnost, kde to selže, a spojitost padá.

> [!navic] Praktické použití: obměna
> Implikace (1) ⇒ (2) je totéž co NOT (2) ⇒ NOT (1). Návod na důkaz nespojitosti v $p$: najdi posloupnost $x_n \to p$, pro kterou buď $\lim f(x_n) \neq f(p)$, nebo $\lim f(x_n)$ vůbec neexistuje. Pak $f$ v $p$ spojitá není.

> [!example] $\sin \frac{1}{x}$ není spojitá v 0 · handout 3A, slajd 7
> $$
> f(x) = \begin{cases} \sin \frac{1}{x}, & x \neq 0, \\ 0, & x = 0. \end{cases}
> $$
>
> Vezmi $x_n = \dfrac{1}{n\pi + \frac{\pi}{2}}$. Pak $\lim x_n = 0$ a
>
> $$
> f(x_n) = \sin\Big(n\pi + \frac{\pi}{2}\Big) = (-1)^n,
> $$
>
> což [[MA1 05 – Aritmetika limit a substituce#^dusledek-suda-licha|limitu nemá]]. Podle Heineovy věty $f$ v $0$ spojitá není. Žádná volba $f(0)$ to nespraví, protože $\lim_{x \to 0} \sin \frac{1}{x}$ neexistuje.

^priklad-sin

> [!obrazek] Graf sin(1/x) u nuly
> ![[ma106-sin.png]]
> *Modrý graf u nuly kmitá stále rychleji mezi −1 a 1. Oranžové body jsou hodnoty v xₙ, střídavě 1 a −1, a blíží se k 0 zprava. Červený bod je f(0) = 0.*

## §4 Spojitost na intervalu

> [!definice] Spojitost na intervalu · handout 3A, slajdy 9 a 11
> $f$ je **spojitá na intervalu $I$**, když $I$ má aspoň dva body, $f$ je definovaná v každém bodě $I$, je spojitá v každém vnitřním bodě $I$, zprava v levém krajním bodě (patří-li do $I$) a zleva v pravém krajním bodě (patří-li do $I$).
>
> Pro uzavřený interval: $f$ je spojitá na $[a; b]$, když $a < b$, $f$ je definovaná na celém $[a; b]$, spojitá v každém $p \in (a; b)$ a
>
> $$
> \lim_{x \to a^+} f(x) = f(a), \qquad \lim_{x \to b^-} f(x) = f(b).
> $$

^def-spojitost-interval

> [!lidsky] Lidsky
> [[spojitost na intervalu|Spojitost na intervalu]]: uvnitř normálně, na krajích jen z té strany, odkud se dá přijít. Co se děje mimo interval, nehraje roli. Například $\sqrt{x}$ je spojitá na $[0; 1]$, i když nalevo od nuly není vůbec definovaná.

## §5 Creeping Theorem

Velké věty o funkcích spojitých na $[a; b]$ mají společný vzor důkazu: vlastnost platí „lokálně“ kolem každého bodu a dá se „slepovat“, proto platí na celém intervalu. Ten vzor zachycuje jedna věta.

> [!definice] Lokální a aditivní systém intervalů · handout 3A, slajd 12
> Ať $\mathcal{A}$ je systém uzavřených podintervalů intervalu $[a; b]$, $a < b$.
>
> - $\mathcal{A}$ je **lokální**, když ke každému $x \in (a; b)$ existuje $[c; d] \in \mathcal{A}$ s $c < x < d$, k bodu $a$ existuje $[a; d] \in \mathcal{A}$ s $a < d$ a k bodu $b$ existuje $[c; b] \in \mathcal{A}$ s $c < b$.
> - $\mathcal{A}$ je **aditivní**, když pro $I_1, I_2 \in \mathcal{A}$ s $I_1 \cap I_2 \neq \emptyset$ platí $I_1 \cup I_2 \in \mathcal{A}$.

^def-lokalni-aditivni

> [!lidsky] Lidsky
> Představ si $\mathcal{A}$ jako sbírku „dobrých“ úseků, třeba úseků, na kterých je funkce omezená. [[lokální systém intervalů|Lokální]]: každý bod má kolem sebe nějaký dobrý úsek (krajní body aspoň z jedné strany). [[aditivní systém intervalů|Aditivní]]: dva dobré úseky, které se překrývají nebo dotýkají, se dají slepit v jeden dobrý úsek.

> [!veta] Creeping Theorem · handout 3A, slajd 13
> ==Je-li $\mathcal{A}$ lokální a aditivní systém podintervalů $[a; b]$,== potom **$[a; b] \in \mathcal{A}$**.
>
> > [!note]- Důkaz
> > Ať $M = \{x \in (a; b] \mid [a; x] \in \mathcal{A}\}$. Z lokality v bodě $a$ je $M \neq \emptyset$ a $M$ je shora omezená číslem $b$, takže existuje $s = \sup M$ a $a < s \le b$.
> >
> > Ať $s < b$. Z lokality existuje $[c; e] \in \mathcal{A}$ s $c < s < e$. Protože $c < s = \sup M$, není $c$ horní odhad $M$: existuje $x_1 \in M$, $x_1 > c$. Intervaly $[a; x_1]$ a $[c; e]$ se protínají (v $x_1$), z aditivity $[a; e] \in \mathcal{A}$, tedy $e \in M$ a $e > s$ ↯.
> >
> > Tedy $s = b$. Z lokality v $b$ existuje $[c; b] \in \mathcal{A}$, $c < b$, k němu $x_1 \in M$ s $x_1 > c$ a z aditivity $[a; x_1] \cup [c; b] = [a; b] \in \mathcal{A}$.

^veta-creeping

> [!lidsky] Lidsky
> [[Creeping Theorem]] je „plížení“ od $a$ doprava: začneš malým dobrým úsekem u $a$ a pořád ho prodlužuješ slepováním. Kde by ses zastavil (v [[supremum|supremu]] $s$), tam ti lokalita dá další úsek přes $s$ a slepení tě posune dál. Zastavit se tedy jde jen v $b$. Je to obdoba matematické indukce pro reálná čísla.

> [!obrazek] Proč se plížení nezastaví před b
> ![[ma106-plizeni.png]]
> *Červený bod s = sup M je místo, kam se plížení zdánlivě dostalo. Modrý úsek [a; x₁] už je dobrý, oranžový [c; e] je dobrý úsek kolem s z lokality. Překrývají se, takže slepený zelený [a; e] je taky dobrý a sahá za s, což je spor.*

> [!navic] Odkud se bere supremum
> Celý důkaz stojí na [[Dedekindovská úplnost|Dedekindovské úplnosti]] $\mathbb{R}$: neprázdná shora omezená $M$ má supremum. V $\mathbb{Q}$ by věta neplatila a s ní by padla i věta o mezihodnotě: $x^2 - 2$ mění na $[0; 2] \cap \mathbb{Q}$ znaménko, a přesto v $\mathbb{Q}$ nemá kořen.

## §6 Čtyři velké věty o spojitých funkcích na [a; b]

> [!veta] Vlastnosti spojitých funkcí na uzavřeném intervalu · handout 3A, slajd 14
> ==Ať $f$ je spojitá na $[a; b]$.== Potom:
>
> 1. **IVT** (věta o mezihodnotě, Bolzanova věta): **je-li $r$ mezi $f(a)$ a $f(b)$, existuje $t \in [a; b]$ s $f(t) = r$.**
> 2. **BT** (věta o omezenosti): **$f$ je na $[a; b]$ omezená.**
> 3. **EVT** (věta o extrémech, Weierstrassova věta): **$f$ na $[a; b]$ nabývá maxima i minima**, tj. existují $x_{\max}, x_{\min} \in [a; b]$ s $f(x_{\min}) \le f(x) \le f(x_{\max})$ pro všechna $x \in [a; b]$.
> 4. **PIT** (věta o zachování intervalů): **obraz $\{f(x) \mid x \in [a; b]\}$ je interval**, a to $[f(x_{\min}); f(x_{\max})]$.

^veta-ctyri

> [!lidsky] Lidsky
> Graf spojité funkce na $[a; b]$ je jedna nepřerušená čára s oběma konci. Proto: aby se dostala z výšky $f(a)$ do výšky $f(b)$, musí projít každou výškou mezi nimi ([[věta o mezihodnotě|IVT]]); neuteče do nekonečna ([[věta o omezenosti spojité funkce|BT]]); má nejvyšší a nejnižší bod ([[věta o extrémech|EVT]]); a výšky, které navštíví, tvoří souvislý úsek bez děr ([[věta o zachování intervalů|PIT]]).

> [!obrazek] IVT, BT, EVT a PIT
> ![[ma106-vety.png]]
> *Vlevo nahoře: oranžová výška r leží mezi modrými f(a) a f(b) a graf ji protne v zeleném bodě. Vpravo nahoře: celý graf se vejde do oranžového pásu. Vlevo dole: zelený nejvyšší a červený nejnižší bod existují. Vpravo dole: oranžová úsečka na svislé ose je obraz, celý interval od minima po maximum.*

> [!obrazek] Proč musí být interval uzavřený
> ![[ma106-otevreny.png]]
> *Vlevo modře $\frac{1}{x}$ na $(0; 1]$: je spojitá, ale u nuly (červená šipka) roste nade všechny meze, BT selže. Vpravo $x$ na $(0; 1)$: je omezená, ale oranžové hranice $0$ a $1$ (prázdné kroužky) nenabude, EVT selže.*

### Důkaz IVT

> [!note]- Důkaz IVT · handout 3A, slajd 15
> Pro $r = f(a)$ nebo $r = f(b)$ stačí $t = a$, resp. $t = b$. Ať tedy $r$ leží ostře mezi, třeba $f(a) > r > f(b)$ (druhý případ je stejný). Polož $g = f - r$; je spojitá na $[a; b]$ a $g(a) > 0 > g(b)$.
>
> Sporem: ať $g(x) \neq 0$ pro všechna $x \in [a; b]$. Ať $\mathcal{A}$ jsou uzavřené podintervaly $[a; b]$, na kterých **$g$ nemění znaménko**.
>
> - **Lokální:** $g(x) \neq 0$ a $g$ je spojitá v $x$, takže podle [[věta o znaménku limity|věty o znaménku]] má $g$ na nějakém okolí $x$ (u krajních bodů jednostranném) stejné znaménko jako $g(x)$.
> - **Aditivní:** dva překrývající se intervaly bez změny znaménka mají společný bod, tedy stejné znaménko, a jejich sjednocení znaménko nemění.
>
> Podle Creeping Theorem je $[a; b] \in \mathcal{A}$, tedy $g$ nemění znaménko na celém $[a; b]$. To je spor s $g(a) > 0 > g(b)$.

^dukaz-ivt

### Důkaz BT

> [!note]- Důkaz BT · handout 3A, slajd 15
> Ať $\mathcal{A}$ jsou uzavřené podintervaly $[a; b]$, na kterých je $f$ omezená.
>
> - **Lokální:** ze spojitosti v $x$ (pro $\varepsilon = 1$) existuje okolí $x$, na kterém $\lvert f(y) - f(x) \rvert < 1$, tedy $\lvert f(y) \rvert < \lvert f(x) \rvert + 1$.
> - **Aditivní:** je-li $\lvert f \rvert \le K_1$ na $I_1$ a $\lvert f \rvert \le K_2$ na $I_2$, je $\lvert f \rvert \le \max(K_1, K_2)$ na $I_1 \cup I_2$.
>
> Podle Creeping Theorem $[a; b] \in \mathcal{A}$.

^dukaz-bt

### Důkaz EVT

> [!note]- Důkaz EVT · handout 3A, slajd 16
> Stačí maximum, minimum je obdobné (nebo maximum funkce $-f$). Podle BT je obraz omezený, takže $s = \sup\{f(x) \mid x \in [a; b]\} \in \mathbb{R}$. Je-li $s$ hodnotou $f$, je to maximum.
>
> Sporem: ať $f(x) < s$ pro všechna $x$. Pak
>
> $$
> g(x) = \frac{1}{s - f(x)}
> $$
>
> je spojitá na $[a; b]$ (aritmetika, jmenovatel nikde není $0$) a kladná. Pro každé $K > 0$ není $s - \frac{1}{K}$ horní odhad, takže existuje $x$ s $f(x) > s - \frac{1}{K}$, tedy $g(x) > K$. Funkce $g$ je neomezená, spor s BT.

^dukaz-evt

### Důkaz PIT

> [!note]- Důkaz PIT · handout 3A, slajd 17
> Podle EVT existují $x_{\min}, x_{\max}$. Obraz zřejmě leží v $[f(x_{\min}); f(x_{\max})]$. Naopak každé $r$ z tohoto intervalu je podle IVT (použité na uzavřený interval mezi $x_{\min}$ a $x_{\max}$, kde je $f$ taky spojitá) rovno $f(t)$ pro nějaké $t$. Je-li $x_{\min} = x_{\max}$, je $f$ konstantní a tvrzení je triviální.

^dukaz-pit

> [!pozor] Všechny předpoklady jsou potřeba
> - **Uzavřenost intervalu:** $f(x) = \frac{1}{x}$ je spojitá na $(0; 1]$, ale neomezená (BT padá). $f(x) = x$ na $(0; 1)$ je omezená, ale maxima ani minima nenabude (EVT padá).
> - **Spojitost na celém intervalu:** $f(x) = \frac{1}{x}$ pro $x \neq 0$, $f(0) = 0$ na $[-1; 1]$ je neomezená; skok $\mathrm{sgn}\,x$ na $[-1; 1]$ nenabude hodnoty $\frac{1}{2}$, i když leží mezi $f(-1) = -1$ a $f(1) = 1$.

> [!navic] K čemu je IVT v praxi: metoda půlení intervalu
> Mění-li spojitá $f$ na $[a; b]$ znaménko, má tam podle IVT kořen. Rozpůlíš interval, ponecháš polovinu, kde se znaménko mění, a opakuješ. Po $n$ krocích je kořen chycen v intervalu délky $\frac{b - a}{2^n}$: po 10 krocích je to méně než tisícina původní délky ($2^{10} = 1024$). Tak počítač hledá řešení rovnic (handout 3A, slajd 19).

## §7 Patologie: obraz je interval, a přesto nespojitá

> [!example] Patologická funkce (z přednášky; souvisí s Darbouxovou vlastností, handout 3A, slajd 22)
> $$
> f(x) = \begin{cases} x, & x \in [0; 1] \cap \mathbb{Q}, \\ 1 - x, & x \in [0; 1] \setminus \mathbb{Q}. \end{cases}
> $$
>
> - **Spojitá jen v $x = \frac{1}{2}$.** Pro $p \in (0; 1)$ vezmi racionální $x_n \to p$ a iracionální $y_n \to p$ (existují, protože racionální i iracionální čísla jsou všude hustá). Pak $f(x_n) = x_n \to p$ a $f(y_n) = 1 - y_n \to 1 - p$. Podle Heineovy věty spojitost vyžaduje $p = f(p) = 1 - p$, tedy $p = \frac{1}{2}$. V krajních bodech $0$ a $1$ stejně, jen s jednostrannou verzí (posloupnosti zprava, resp. zleva). V $\frac{1}{2}$ spojitá je: $\lvert f(x) - \frac{1}{2} \rvert = \lvert x - \frac{1}{2} \rvert$ v obou případech, takže stačí $\delta = \varepsilon$.
> - **Obraz je celý $[0; 1]$.** Racionální $q$ je obrazem sebe sama, iracionální $y$ je obrazem iracionálního $1 - y$.
> - **Má pevné body**, dokonce nekonečně mnoho: každé racionální $q$ splňuje $f(q) = q$.

^priklad-patologie

> [!obrazek] Dvě tečkované přímky
> ![[ma106-patologie.png]]
> *Modře hodnoty v racionálních bodech (přímka y = x), oranžově v iracionálních (y = 1 − x). Obě „tečkované“ přímky jsou husté a navzájem se proplétají; jen v zeleném bodě x = 1/2 se potkají, a jen tam je funkce spojitá.*

> [!lidsky] Lidsky
> Věty z §6 jdou jen jedním směrem: spojitost ⇒ obraz je interval. Obráceně to neplatí, tahle funkce má obraz $[0; 1]$ a pevné body, a přitom je nespojitá skoro všude. A IVT pro ni selže na menším intervalu: na $[0; \frac{1}{4}]$ je $f(0) = 0$, $f(\frac{1}{4}) = \frac{1}{4}$, ale iracionální hodnotu $r = \frac{\sqrt{2}}{10} \approx 0{,}141$ nenabude (musel by to být bod $1 - r \approx 0{,}859$, a ten v $[0; \frac{1}{4}]$ neleží).

## §8 Věta o pevném bodě

> [!veta] Věta o pevném bodě · handout 3A, slajd 20
> ==Ať $f: [a; b] \to [a; b]$ je spojitá na $[a; b]$.== Potom **existuje $t \in [a; b]$ s $f(t) = t$.**
>
> > [!note]- Důkaz
> > Je-li $f(a) = a$ nebo $f(b) = b$, hotovo. Jinak, protože hodnoty leží v $[a; b]$, je $f(a) > a$ a $f(b) < b$. Funkce $g(x) = f(x) - x$ je spojitá na $[a; b]$ (rozdíl spojitých), $g(a) > 0$ a $g(b) < 0$. Podle IVT existuje $t$ s $g(t) = 0$, tedy $f(t) = t$.

^veta-pevny-bod

> [!lidsky] Lidsky
> Graf spojité funkce, který začíná na levé hraně čtverce $[a; b] \times [a; b]$ a končí na pravé, musí někde protnout úhlopříčku $y = x$. Průsečík je [[věta o pevném bodě|pevný bod]]: bod, který funkce „nechá na místě“. Praktický příklad: rovnice $x = \cos x$ má řešení v $[0; 1]$, protože $\cos$ zobrazuje $[0; 1]$ do $[\cos 1; 1] \subseteq [0; 1]$.

> [!obrazek] Pevný bod jako průsečík s úhlopříčkou
> ![[ma106-pevny-bod.png]]
> *Šedý čtverec je [a; b] × [a; b]. Modrý graf f začíná nad oranžovou úhlopříčkou y = x a končí pod ní, takže ji v zeleném bodě protne: f(t) = t.*

> [!navic] Brouwerova věta
> Ve více rozměrech platí totéž (Brouwerova věta o pevném bodě): spojité zobrazení uzavřené koule do sebe má pevný bod. Používá se třeba v teorii her k důkazu existence Nashovy rovnováhy.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- V čem se liší definice spojitosti v $p$ od definice limity v $p$?
> U spojitosti musí **$f(p)$ existovat**, terč je kolem $f(p)$ a okolí $p$ je **plné** (obsahuje $p$). U limity je okolí prstencové a hodnota $f(p)$ nehraje roli.

> [!karta|02]- Dokaž, že $\lvert x \rvert$ je spojitá v každém bodě $p$.
> K $\varepsilon > 0$ vezmi **$\delta = \varepsilon$**: $\big\lvert \lvert x \rvert - \lvert p \rvert \big\rvert \le \lvert x - p \rvert < \delta = \varepsilon$ (obrácená trojúhelníková nerovnost).

> [!karta|03]- Proč je každý polynom spojitý v každém bodě $p \in \mathbb{R}$?
> Konstanty a $x$ jsou spojité a polynom se z nich složí **sčítáním a násobením**, které spojitost zachovávají (aritmetika spojitých funkcí). Limitu polynomu proto stačí spočítat dosazením.

> [!karta|04]- Dokaž větu o spojitosti složené funkce $g \circ f$.
> K okolí $U$ bodu $g(f(p))$ najdi okolí $W$ bodu $f(p)$ s $g[W] \subseteq U$, k $W$ okolí $V$ bodu $p$ s $f[V] \subseteq W$. Pak $(g \circ f)[V] \subseteq g[W] \subseteq U$.

> [!karta|05]- Platí věta o složené funkci pro spojitost zprava? Protipříklad.
> **Ne.** $f(x) = -x^2 + 1$ (spojitá zprava v $0$), $g = 2$ pro $z \ge 1$, jinak $0$ (spojitá zprava v $1$). Pro $x \to 0^+$ jdou hodnoty $f$ k $1$ **zdola**, takže $g(f(x)) \to 0 \neq 2 = g(f(0))$.

> [!karta|06]- Jak pomocí Heineovy věty dokážeš, že $f$ není spojitá v $p$?
> Najdi **jednu** posloupnost $x_n \to p$, pro kterou $\lim f(x_n) \neq f(p)$, nebo $\lim f(x_n)$ neexistuje. To je obměna implikace „spojitá ⇒ $f(x_n) \to f(p)$ pro každou $x_n \to p$“.

> [!karta|07]- Dokaž Creeping Theorem (náčrt).
> $M = \{x : [a; x] \in \mathcal{A}\}$, $s = \sup M$. Kdyby $s < b$, lokalita dá $[c; e] \ni s$, $c < s < e$; vezmi $x_1 \in M$, $x_1 > c$, aditivita dá $[a; e] \in \mathcal{A}$, tedy $e \in M$, $e > s$ ↯. Tedy $s = b$ a stejný krok v $b$ dá **$[a; b] \in \mathcal{A}$**.

> [!karta|08]- Dokaž IVT pomocí Creeping Theorem (náčrt).
> $g = f - r$, $g(a) > 0 > g(b)$; sporem $g \neq 0$ všude. $\mathcal{A}$ = intervaly, kde **$g$ nemění znaménko**: lokální (věta o znaménku), aditivní (překryv má společný bod). Tedy $[a; b] \in \mathcal{A}$, spor se znaménky v $a$ a $b$.

> [!karta|09]- Dokaž, že spojitá funkce na $[a; b]$ je omezená (náčrt).
> $\mathcal{A}$ = intervaly, kde je **$f$ omezená**. Lokální: ze spojitosti $\lvert f \rvert < \lvert f(x) \rvert + 1$ kolem $x$. Aditivní: na sjednocení stačí $\max(K_1, K_2)$. Creeping Theorem dá $[a; b] \in \mathcal{A}$.

> [!karta|10]- Dokaž, že spojitá funkce na $[a; b]$ nabývá maxima (náčrt).
> $s = \sup f$ je konečné (BT). Kdyby $f < s$ všude, byla by $g = \frac{1}{s - f}$ spojitá a **neomezená** (hodnoty $f$ jsou libovolně blízko $s$), spor s BT.

> [!karta|11]- Proč je obraz spojité funkce na $[a; b]$ interval?
> Podle EVT existují $\min$ a $\max$, obraz leží v $[\min; \max]$. Každé $r$ mezi nimi se podle **IVT** (na intervalu mezi $x_{\min}$ a $x_{\max}$) nabude. Obraz je tedy **$[\min f; \max f]$**.

> [!karta|12]- Dokaž větu o pevném bodě.
> Když $f(a) = a$ nebo $f(b) = b$, hotovo. Jinak $f(a) > a$, $f(b) < b$, takže $g(x) = f(x) - x$ má $g(a) > 0 > g(b)$ a podle **IVT** existuje $t$ s $g(t) = 0$, tj. $f(t) = t$.

> [!karta|13]- Proč ve větě o omezenosti a o extrémech nestačí neuzavřený interval?
> $\frac{1}{x}$ je spojitá na $(0; 1]$, ale **neomezená**. $x$ na $(0; 1)$ je omezená, ale **nenabude** maxima ani minima (supremum $1$ a infimum $0$ nejsou hodnoty).

> [!karta|14]- Plyne z toho, že obraz $f$ na $[0; 1]$ je interval, že $f$ je spojitá?
> **Ne.** $f(x) = x$ pro racionální, $1 - x$ pro iracionální $x$ má obraz $[0; 1]$, a přitom je spojitá jen v $\frac{1}{2}$. PIT platí jen jedním směrem.

### Příklady na procvičení

> [!priklad|15]- Je $f(x) = \sin \frac{1}{x}$, $f(0) = 0$, spojitá v $0$?
> **Ne.** $x_n = \frac{1}{n\pi + \frac{\pi}{2}} \to 0$, ale $f(x_n) = (-1)^n$ limitu nemá.

> [!priklad|16]- $f(x) = -x^2 + 1$, $g(z) = 2$ pro $z \ge 1$, $0$ pro $z < 1$. Spočítej $\lim_{x \to 0^+} g(f(x))$ a $g(f(0))$.
> Pro $x \neq 0$ je $f(x) < 1$, tedy $g(f(x)) = 0$ a limita je **0**. $g(f(0)) = g(1) =$ **2**.

> [!priklad|17]- Ve kterých bodech je spojitá $f(x) = x$ pro $x \in [0; 1] \cap \mathbb{Q}$, $f(x) = 1 - x$ jinak na $[0; 1]$?
> Pro $p \in (0; 1)$: racionální posloupnost dá limitu $p$, iracionální $1 - p$, a Heineova věta vyžaduje $p = 1 - p$. V bodech $0$ a $1$ totéž jednostranně. Spojitá jen v **$x = \frac{1}{2}$**.

> [!priklad|18]- Nabude funkce z předchozího příkladu na $[0; \frac{1}{4}]$ hodnoty $\frac{\sqrt{2}}{10}$?
> **Ne.** Racionální $t$ dá racionální $f(t)$, iracionální $t$ dá $1 - t \ge \frac{3}{4}$. IVT tu selže, protože $f$ není spojitá.

> [!priklad|19]- Ověř, že $f(x) = x^2 \sin x$ je spojitá na $[0; \pi]$.
> $x^2$ je polynom, $\sin$ je spojitý, součin spojitých je spojitý v každém bodě ([[věta o aritmetice spojitých funkcí|aritmetika]]). Z oboustranné spojitosti plyne jednostranná v $0$ a $\pi$. **Ano.**

> [!priklad|20]- Má rovnice $\cos x = x$ řešení v $[0; 1]$?
> **Ano.** $g(x) = \cos x - x$ je spojitá, $g(0) = 1 > 0$ a $g(1) = \cos 1 - 1 \approx -0{,}46 < 0$, podle IVT má kořen.

> [!priklad|21]- Pro $f(x) = \lvert x \rvert$ v bodě $p = 3$ a $\varepsilon = 0{,}01$ najdi vhodné $\delta$.
> **$\delta = 0{,}01$**: z $\lvert x - 3 \rvert < 0{,}01$ plyne $\big\lvert \lvert x \rvert - 3 \big\rvert \le \lvert x - 3 \rvert < 0{,}01$.

---
← [[MA1 05 – Aritmetika limit a substituce|7. 10. 2026 Aritmetika limit a substituce]] · [[MA1 07 – Derivace a Carathéodoryho trik|14. 10. 2026 Derivace a Carathéodoryho trik]] →

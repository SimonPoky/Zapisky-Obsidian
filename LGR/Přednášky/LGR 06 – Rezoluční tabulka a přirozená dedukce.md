---
predmet: LGR
prednaska: 6
datum: 2026-10-15
zdroj: "Prezentace 3, slajdy 23–26; Prezentace 4 (Přirozená dedukce), slajdy 1–10"
tags: [prednaska, LGR]
---

# LGR 06 – Rezoluční tabulka a přirozená dedukce

*Přednáška 6 · čtvrtek 15. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 3 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_3.pdf) · [Prezentace 4 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_4.pdf) · [Přirozená dedukce, Nentvich (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/natded.pdf)

Témata: `rezoluční tabulka na příkladu` · `svědek splnitelnosti pozpátku` · `pravdivost vs. odvoditelnost` · `S ⊢ φ` · `korektní a úplný systém` · `sporný systém` · `přirozená dedukce` · `∧i, ⇒i` · `boxy a lokální předpoklady` · `odvození`

Minule se dokázala [[věta o eliminaci proměnné]] a z ní [[rezoluční tabulka]]. Dnes se tabulka projde celá na příkladu se šesti klauzulemi a hlavně se z ní pozpátku vyrobí [[svědek splnitelnosti]]. Druhá polovina otevírá novou kapitolu: místo otázky „je $\varphi$ pravdivá všude, kde platí $S$?“ ($S \models \varphi$) se ptáme „dá se $\varphi$ z $S$ **odvodit** podle pravidel?“ ($S \vdash \varphi$). Nástrojem je [[přirozená dedukce]], pravidla, která kopírují běžné matematické dokazování.

## §0 Přehled na jedné stránce

| pojem | zápis | význam |
|---|---|---|
| [[rezoluční tabulka]] | $S \to S' \to \dots \to S^{(n)}$ | vyrezolvuj $x_1, \dots, x_n$; konec $\emptyset$ = splnitelná, $\{\mathrm{ff}\}$ = nesplnitelná |
| [[svědek splnitelnosti\|svědek]] pozpátku | od $S^{(n)} = \emptyset$ k $S$ | doplňuj hodnoty $x_n, \dots, x_1$ tak, aby platily klauzule daného kroku |
| [[sémantický důsledek]] | $S \models \varphi$ | pravdivost: $\varphi$ platí všude, kde platí $S$ (tabulka, rezoluce) |
| [[logický důsledek]] | $S \vdash \varphi$ | odvoditelnost: $\varphi$ jde z $S$ odvodit pravidly (důkazový systém) |
| [[korektní důkazový systém\|korektní systém]] | $S \vdash \varphi \Rightarrow S \models \varphi$ | odvoditelné $\subseteq$ pravdivé |
| [[úplný důkazový systém\|úplný systém]] | $S \vdash \varphi \Leftrightarrow S \models \varphi$ | odvoditelné $=$ pravdivé |
| [[sporný důkazový systém\|sporný systém]] | $S \vdash \varphi$ pro každé $\varphi$ | odvodí všechno, i $\varphi$ a $\neg\varphi$; nechceme |
| [[zavedení konjunkce\|∧i]] | $\dfrac{\varphi \quad \psi}{\varphi \wedge \psi}$ | konjunkci dokážeš tak, že dokážeš oba členy |
| [[zavedení implikace\|⇒i]] | box $\varphi \dots \psi$ $\Rightarrow$ $\varphi \Rightarrow \psi$ | přímý důkaz implikace: předpokládej $\varphi$, odvoď $\psi$ |
| [[odvození]] | posloupnost formulí s odůvodněním | důkaz $\varphi$ z předpokladů $S$; poslední řádek je $\varphi$ |

## §1 Rezoluční tabulka na příkladu

Zadání (slajd 26 rozšířený o klauzuli $\neg w$): rozhodni, zda je splnitelná množina klauzulí nad $A = \{x, y, z, w\}$

$$
S = \{\underbrace{x \vee y \vee w}_{\alpha},\ \underbrace{x \vee \neg y}_{\beta},\ \underbrace{\neg x \vee y \vee \neg z}_{\gamma},\ \underbrace{y \vee z \vee \neg w}_{\delta},\ \underbrace{z \vee w}_{\varepsilon},\ \neg w\},
$$

a pokud ano, najdi [[svědek splnitelnosti|svědka]]. Proměnné se eliminují v pořadí $x, y, z, w$. ^zadani

### Eliminace $x$

Rozklad podle $x$: $S_x = \{\alpha, \beta\}$, $S_{\neg x} = \{\gamma\}$, $S_0 = \{\delta, \varepsilon, \neg w\}$. [[rezolventa|Rezolventy]] přes $x$ tvoří dvojice z $S_x \times S_{\neg x}$:

- $\mathrm{res}_x(\alpha, \gamma) = y \vee w \vee \neg z$,
- $\mathrm{res}_x(\beta, \gamma) = \neg y \vee y \vee \neg z \mathrel{\vert\!=\!\vert} \mathrm{tt} \vee \neg z \mathrel{\vert\!=\!\vert} \mathrm{tt}$, [[tautologie]], do $R_x$ nepatří.

Tedy $R_x = \{y \vee w \vee \neg z\}$ a

$$
S' = S_0 \cup R_x = \{\delta,\ \varepsilon,\ \neg w,\ y \vee w \vee \neg z\} \quad \text{nad } A' = \{y, z, w\}.
$$

### Eliminace $y$, $z$, $w$

| krok | $S_v$ | $S_{\neg v}$ | $R_v$ | nová množina |
|---|---|---|---|---|
| $y$ | $\delta = y \vee z \vee \neg w$, $\ y \vee w \vee \neg z$ | $\emptyset$ | $\emptyset$ | $S'' = \{z \vee w, \neg w\}$ nad $\{z, w\}$ |
| $z$ | $z \vee w$ | $\emptyset$ | $\emptyset$ | $S''' = \{\neg w\}$ nad $\{w\}$ |
| $w$ | $\emptyset$ | $\neg w$ | $\emptyset$ | $S'''' = \emptyset$ nad $\emptyset$ |

Když je jedna z $S_v$, $S_{\neg v}$ prázdná, není s čím rezolvovat: $R_v = \emptyset$ a klauzule s $v$ prostě zmizí. ^prazdne-rv

**Konec:** zbyla prázdná množina klauzulí, a ta je splnitelná (svědkem je libovolné ohodnocení). Podle [[věta o eliminaci proměnné|věty o eliminaci]] je každý krok [[ekvisplnitelné množiny|ekvisplnitelný]] s předchozím, takže **$S$ je splnitelná**. ^konec-prazdna

> [!obrazek] Rezoluční tabulka pro $S$
> ![[lgr06-tabulka.png]]
> *Sloupce jsou klauzule: oranžově z $S$, modře rezolventa přes $x$, červeně tautologická rezolventa (vypustí se). Číslo stojí v řádku proměnné, při jejíž eliminaci se klauzule použije naposledy: $1$ = obsahuje ji pozitivně, $0$ = negativně. Šrafované buňky pod ním: klauzule je „umrtvená“. Zeleně dole literály, díky kterým je klauzule ve výsledném svědkovi pravdivá; šipka vlevo ukazuje směr hledání svědka.*

> [!lidsky] Lidsky
> Tabulka se čte jako „kdo má na starosti kterou klauzuli“. Klauzule $\alpha$, $\beta$, $\gamma$ obsahují $x$, takže se s nimi vyřídí v prvním řádku a dál se neřeší. Řádek $y$ dostane na starost $\delta$ a novou rezolventu, řádek $z$ klauzuli $\varepsilon$, řádek $w$ klauzuli $\neg w$. Zápis v tabulce šetří papír: nevypisuješ znovu celé množiny $S'$, $S''$, …

## §2 Svědek splnitelnosti pozpátku

> [!veta] Postup · slajd 25
> ==Rezoluční tabulka skončila prázdnou množinou.== Svědka pro $S$ najdeš **od konce**:
> 1. Pro $S^{(n)} = \emptyset$ je svědkem libovolné ohodnocení.
> 2. Máš-li svědka $u$ pro $S^{(i)} = S_0 \cup R_{x_i}$, urči $u(x_i)$ tak, aby byly pravdivé i klauzule z $S_{x_i}$ a $S_{\neg x_i}$ (tj. ty, co mají v tabulce číslo v řádku $x_i$). Hodnoty ostatních proměnných nech.
> 3. **Podle [[věta o eliminaci proměnné|věty o eliminaci proměnné]] se to vždy povede**: aspoň jedna z voleb $x_i \mapsto 0$, $x_i \mapsto 1$ funguje.
> 4. Po kroku pro $x_1$ máš svědka pro $S$.

^veta-svedek-postup

> [!lidsky] Lidsky
> Jako skládání puzzle od posledního dílku: na konci nejsou žádné podmínky, takže začneš čímkoli. Pak se vracíš po krocích a v každém nastavíš jen tu proměnnou, kterou jsi v tom kroku vyrezolvoval. Ostatní už jsou nastavené tak, že rezolventy platí, a rezolventy „pamatují“ všechno, co je potřeba, takže vhodná hodnota vždy existuje.

> [!example] Svědek pro $S$ z §1
> | množina | proměnná | volba | proč |
> |---|---|---|---|
> | $S'''' = \emptyset$ | (žádná) | cokoli | prázdná množina je splnitelná vždy |
> | $S''' = \{\neg w\}$ | $w$ | $w \mapsto 0$ | jinak by neplatila $\neg w$ |
> | $S'' = \{z \vee w, \neg w\}$ | $z$ | $z \mapsto 1$ | při $w = 0$ jinak neplatí $z \vee w$ |
> | $S' = \{\delta, \varepsilon, \neg w, y \vee w \vee \neg z\}$ | $y$ | $y \mapsto 1$ | při $w = 0$, $z = 1$ jinak neplatí $y \vee w \vee \neg z$ |
> | $S$ | $x$ | $x \mapsto 1$ | při $y = 1$ jinak neplatí $\beta = x \vee \neg y$ |
>
> Svědek: **$u(x) = u(y) = u(z) = 1$, $u(w) = 0$**, tj. $u(S) = 1$. Kontrola v každé klauzuli je ve spodním řádku obrázku výše. (Přepočítáním všech 16 ohodnocení vyjde, že je to dokonce jediný svědek.)

^priklad-svedek

> [!obrazek] Svědek se staví pozpátku
> ![[lgr06-svedek.png]]
> *Modře množiny z jednotlivých kroků tabulky, zeleně volba hodnoty eliminované proměnné, vpravo klauzule, která volbu vynutí.*

### Poslední krok podrobně

V posledním kroku má svědek $u'$ pro $S' = S_0 \cup R_x$ hodnoty $y \mapsto 1$, $z \mapsto 1$, $w \mapsto 0$. Protože v $S'$ není $x$, jsou svědky pro $S'$ hned **dva**, $u'_0$ ($x \mapsto 0$) a $u'_1$ ($x \mapsto 1$), a podle důkazu věty o eliminaci aspoň jeden z nich je svědkem pro celou $S$:

| | $x$ | $y$ | $z$ | $w$ | $\alpha$ | $\beta$ | $\gamma$ | $S_0 \cup R_x$ |
|---|---|---|---|---|---|---|---|---|
| $u'_0$ | $0$ | $1$ | $1$ | $0$ | $1$ | **$0$** | $1$ | $1$ |
| $u'_1$ | $1$ | $1$ | $1$ | $0$ | $1$ | $1$ | $1$ | $1$ |

$u'_0$ pokazí $\beta \in S_x$, ale $u'_1$ splní $S_x$ (díky $x$) i $S_{\neg x}$ ($\gamma$ díky $y$). **Svědkem pro $S$ je $u'_1$.** ^posledni-krok

> [!pozor] Častá chyba: měnit při zpětném kroku i jiné proměnné
> V kroku pro $x_i$ se smí určit **jen** $u(x_i)$. Kdybys „opravoval“ i dříve nastavené proměnné, můžeš pokazit klauzule z pozdějších množin ($S_0$ a rezolventy), na kterých celý postup stojí. Věta o eliminaci zaručuje, že změna samotné $x_i$ vždy stačí.

## §3 Pravdivost a odvoditelnost

Na otázku „plyne $\varphi$ z $S$?“ jsou dva pohledy (slajdy 3–4 prezentace 4):

| | sémantika | syntax |
|---|---|---|
| zápis | $S \models \varphi$, [[sémantický důsledek]] | $S \vdash \varphi$, [[logický důsledek]] |
| otázka | Je ve všech ohodnoceních, kde je $S$ pravdivá, pravdivá i $\varphi$? | Dá se z formulí $S$ (axiomů) podle pravidel odvodit $\varphi$? |
| pojem | **pravdivost** | **odvoditelnost** |
| nástroje | pravdivostní tabulka o $2^n$ řádcích; rezoluční metoda (v nejhorším případě také exponenciální) | důkazové systémy, např. [[přirozená dedukce]] |

^pravdivost-odvoditelnost

> [!definice] Logický důsledek (odvoditelnost) · slajdy 3, 10
> Formule $\varphi$ je *logickým důsledkem* množiny formulí $S$, píše se **$S \vdash \varphi$**, jestliže existuje [[odvození]] $\varphi$ z formulí v $S$ podle pravidel daného důkazového systému. Pro $S = \emptyset$ se píše $\vdash \varphi$.

^def-logicky-dusledek

> [!lidsky] Lidsky
> $\models$ je „zkontroluj všechny světy“: projdi všechna ohodnocení. $\vdash$ je „napiš důkaz“: krok za krokem podle pevných pravidel, jako když ve škole dokazuješ větu a u každého řádku napíšeš, proč platí. Symbol $\vdash$ připomíná „turniket“: projde jen to, co má platný doklad.

> [!definice] Korektní a úplný důkazový systém · slajd 4
> Důkazový systém je
> - *korektní*, jestliže každá odvoditelná formule je pravdivá: **$S \vdash \varphi \Rightarrow S \models \varphi$** (odvoditelné $\subseteq$ pravdivé);
> - *úplný*, jestliže navíc jde odvodit každý sémantický důsledek: **$S \vdash \varphi \Leftrightarrow S \models \varphi$** (odvoditelné $=$ pravdivé).

^def-korektni-uplny

> [!lidsky] Lidsky
> Korektní systém nikdy nelže: co dokáže, to opravdu platí. Úplný systém navíc nic nevynechá: co platí, to taky umí dokázat. Korektnost je nutnost (lhář je k ničemu), úplnost je přání.

> [!definice] Co nechceme · slajd 4
> - *Příliš agresivní* ([[korektní důkazový systém|nekorektní]]) systém: odvodí i formule, které z $S$ sémanticky neplynou, tj. existuje $\varphi$ s $S \vdash \varphi$, ale $S \not\models \varphi$.
> - *Sporný* systém: odvodí **všechno**, tj. $S \vdash \varphi$ pro každou $\varphi \in \mathrm{Fla}(A)$, tedy i $\varphi$ a $\neg\varphi$ naráz, i $\mathrm{ff}$.

^def-nechceme

> [!lidsky] Lidsky
> Agresivní systém občas „dokáže“ nepravdu, takže mu nejde věřit. Sporný je extrém: dokáže úplně cokoli, a tím pádem nic nerozliší. Je to jako detektor kovů, který pípá pořád.

> [!obrazek] Korektní, úplný, agresivní a sporný systém
> ![[lgr06-systemy.png]]
> *Šedě všechny formule $\mathrm{Fla}(A)$, modře pravdivé ($S \models \varphi$), oranžově šrafované odvoditelné ($S \vdash \varphi$). Korektní: oranžová leží uvnitř modré. Úplný: kryjí se. Agresivní: oranžová přečnívá ven. Sporný: oranžová je celé $\mathrm{Fla}(A)$.*

> [!navic] Hilbert vs. Gentzen · slajd 4
> *Hilbertův systém* (1908) má málo pravidel a hodně axiomů: pro výrokovou logiku tři typy axiomů, jediné pravidlo [[modus ponens]] a jen spojky $\neg$, $\Rightarrow$. Důkazy v něm jsou krátké na popis, ale dlouhé a neintuitivní na psaní. *Přirozená dedukce* (Gentzen, kolem 1930) naopak nemá žádné axiomy a má hodně pravidel, která odpovídají tomu, jak se dokazuje „přirozeně“.

## §4 Přirozená dedukce

> [!definice] Přirozená dedukce · slajdy 4–8
> *Přirozená dedukce* je důkazový systém bez axiomů, se spojkami $\wedge$, $\vee$, $\Rightarrow$, $\neg$ (ekvivalence se dokazuje jako dvě implikace). Ke každé spojce má
> - **i-pravidlo** (introduction, zavedení): jak formuli s touto spojkou **dokázat**,
> - **e-pravidlo** (elimination, odstranění): jak formuli s touto spojkou **použít**.
>
> Symbol $\bot$ (spor) zastupuje libovolnou formuli tvaru $\varphi \wedge \neg\varphi$.

^def-prirozena-dedukce

> [!lidsky] Lidsky
> Každá spojka má „návod na výrobu“ a „návod k použití“. Konjunkci vyrobíš ze dvou dílů, a když ji máš, smíš si vzít kterýkoli díl. Implikaci vyrobíš tak, že si na chvíli něco předpokládáš, a použiješ ji tak, že do ní dosadíš předpoklad. Pravidla jsou přesně ty kroky, které děláš v matematických důkazech, jen pojmenované.

### Pravidla

Zlomková čára znamená: z formulí nad čarou smíš odvodit formuli pod čarou.

| pravidlo | tvar | lidsky |
|---|---|---|
| [[zavedení konjunkce\|∧i]] | $\dfrac{\varphi \quad \psi}{\varphi \wedge \psi}$ | máš obě části, máš i konjunkci |
| [[eliminace konjunkce\|∧e₁, ∧e₂]] | $\dfrac{\varphi \wedge \psi}{\varphi}$, $\ \dfrac{\varphi \wedge \psi}{\psi}$ | z konjunkce smíš vzít kterýkoli člen |
| [[zavedení implikace\|⇒i]] | box s předpokladem $\varphi$ končící $\psi$, pak $\varphi \Rightarrow \psi$ | přímý důkaz implikace |
| ⇒e (MP) | $\dfrac{\varphi \quad \varphi \Rightarrow \psi}{\psi}$ | [[modus ponens]] |
| ∨i₁, ∨i₂ | $\dfrac{\varphi}{\varphi \vee \psi}$, $\ \dfrac{\psi}{\varphi \vee \psi}$ | k pravdivé formuli smíš cokoli přidat „nebo“ |
| [[eliminace disjunkce\|∨e]] | $\varphi \vee \psi$, box $\varphi \dots \chi$, box $\psi \dots \chi$, pak $\chi$ | rozbor případů: $\chi$ plyne v obou |
| ¬i | box s předpokladem $\varphi$ končící $\bot$, pak $\neg\varphi$ | předpoklad vedl ke sporu, neplatí |
| [[eliminace negace\|¬e]] | $\dfrac{\varphi \quad \neg\varphi}{\bot}$ | $\varphi$ a $\neg\varphi$ naráz je spor |
| ¬¬e, ¬¬i | $\dfrac{\neg\neg\varphi}{\varphi}$, $\ \dfrac{\varphi}{\neg\neg\varphi}$ | dvojitá negace |
| [[eliminace sporu\|⊥e]] | $\dfrac{\bot}{\varphi}$ | ze sporu plyne cokoli |
| [[iterace\|it]] | $\dfrac{\varphi}{\varphi}$ | dříve odvozenou formuli smíš zopakovat (i do vnořeného boxu) |

^pravidla

Dnes se podrobně probrala pravidla $\wedge$i a $\Rightarrow$i; ostatní se v příkladech jen použila a podrobně se probírají dál.

### Pravidlo $\wedge$i a proč respektuje pravdivost

> [!definice] Zavedení konjunkce ($\wedge$i, „and introduction“) · slajdy 5–8
> $$
> \frac{\varphi \qquad \psi}{\varphi \wedge \psi}
> $$
> Z formulí $\varphi$, $\psi$ lze odvodit formuli $\varphi \wedge \psi$. **Typ důkazu:** konjunkci $\varphi \wedge \psi$ dokážeme tak, že dokážeme oba konjunkty $\varphi$ i $\psi$.

^def-and-i

> [!lidsky] Lidsky
> Chceš dokázat „číslo je sudé a kladné“: dokážeš zvlášť „je sudé“ a zvlášť „je kladné“ a spojíš.

Pravidlo **respektuje pravdivost**: $\{\varphi, \psi\} \models \varphi \wedge \psi$. Je-li v ohodnocení $u$ pravdivá $\varphi$ i $\psi$, je i $u(\varphi \wedge \psi) = 1$. ^and-i-korektni

### Pravidlo $\Rightarrow$i a boxy

> [!definice] Zavedení implikace ($\Rightarrow$i) · slajdy 5–8
> Když se podaří odvodit z **pomocného předpokladu** $\varphi$ formuli $\psi$, pak jsme na globální úrovni odvodili $\varphi \Rightarrow \psi$:
> $$
> \frac{\boxed{\begin{matrix}\varphi \\ \vdots \\ \psi\end{matrix}}}{\varphi \Rightarrow \psi}
> $$
> **Typ důkazu:** přímý důkaz implikace.

^def-impl-i

> [!lidsky] Lidsky
> „Předpokládejme, že $n$ je sudé. … Tedy $n^2$ je sudé. Dokázali jsme: je-li $n$ sudé, je $n^2$ sudé.“ Box je ta pasáž „předpokládejme…“. Po jejím skončení už $n$ sudé není dokázané, dokázaná je jen implikace.

> [!definice] Pomocný (lokální) předpoklad a box · slajd 9
> *Pomocný (lokální) předpoklad* se smí zavést kdykoli; otevírá **box** (rámeček), který vyznačuje jeho platnost. Formule uvnitř boxu (předpoklad i vše odvozené z něj) se smějí používat **jen uvnitř** tohoto boxu a v boxech do něj vnořených. Box se uzavře pravidlem, které ho „spotřebuje“ (třeba $\Rightarrow$i, $\neg$i, $\vee$e); pak je *pasivní*. Odvození je hotové, až když jsou **všechny boxy uzavřené**. *Globální předpoklady* (formule z $S$) platí v celém odvození.

^def-pomocny

> [!lidsky] Lidsky
> Box je „co kdyby“: na chvíli předpokládáš něco, co nemáš dokázané. Uvnitř s tím smíš počítat, ale ven smí jen výsledek ve tvaru „když …, pak …“. Kdyby smělo ven i to, co platí jen „za předpokladu“, dokázal bys cokoli.

> [!definice] Iterace (it) · slajd 9
> Formuli, která je v odvození už dříve (výše a v boxu, který je pořád otevřený, nebo na globální úrovni), smíš napsat znovu, i dovnitř vnořeného boxu: $\dfrac{\varphi}{\varphi}$, odůvodnění „it $k$“, kde $k$ je číslo řádku.

^def-iterace

> [!lidsky] Lidsky
> Zkopíruj si, co už víš. Hodí se, když box musí **končit** konkrétní formulí, kterou už máš o patro výš.

Pravidlo $\Rightarrow$i taky **respektuje pravdivost**. Tady je schovaný indukční předpoklad, že odvozování uvnitř boxu pravdivost respektuje. Pak v boxu platí $S \cup \{\varphi\} \models \psi$ a podle [[věta o dedukci|věty o dedukci]] $S \models \varphi \Rightarrow \psi$. Bez dalších předpokladů ($S = \emptyset$): v boxu $\varphi \models \psi$, globálně $\emptyset \models (\varphi \Rightarrow \psi)$, neboli $\varphi \Rightarrow \psi$ je [[tautologie]]. ^impl-i-korektni

> [!pozor] Častá chyba: použít formuli z uzavřeného boxu
> Po uzavření boxu jsou jeho řádky pasivní. Kdyby šlo předpoklad z boxu použít venku, odvodil bys z ničeho cokoli: otevři box s $a$, uzavři ho třeba jako $a \Rightarrow a$, a pak „použij“ $a$ venku. Dostal bys $\vdash a$, ale $a$ tautologie není; systém by byl **nekorektní**.

## §5 Odvození a příklady

> [!definice] Odvození (důkaz) · slajd 9
> *Odvození* formule $\varphi$ z množiny předpokladů $S$ je konečná posloupnost formulí $\varphi_1, \dots, \varphi_k$, kde každá $\varphi_i$
> - patří do $S$ (globální předpoklad, značka P), nebo
> - je [[pomocný předpoklad]] otevírající box (P), nebo
> - vznikne z předchozích formulí podle některého pravidla,
>
> poslední formule je $\varphi_k = \varphi$ a všechny boxy jsou uzavřené. Zapisuje se po řádcích: číslo řádku, formule, odůvodnění (pravidlo a čísla řádků, ze kterých vzniká; box se uvádí rozsahem, např. $\Rightarrow$i 2–3).

^def-odvozeni

> [!lidsky] Lidsky
> Odvození je důkaz, který by zkontroloval i počítač: každý řádek má u sebe razítko, podle kterého pravidla a ze kterých řádků vznikl. Nic se „nevidí“ ani „zjevně neplyne“.

> [!example] $a \wedge b \vdash b \wedge a$ · slajd 10
> | # | formule | odůvodnění |
> |---|---|---|
> | 1. | $a \wedge b$ | P (globální předpoklad) |
> | 2. | $a$ | $\wedge$e₁ 1 |
> | 3. | $b$ | $\wedge$e₂ 1 |
> | 4. | $b \wedge a$ | $\wedge$i 3, 2 |

^priklad-komutativita

> [!example] $\vdash a \Rightarrow (b \Rightarrow a)$ (bez dalších předpokladů) · slajd 10
> | # | formule | odůvodnění |
> |---|---|---|
> | 1. | $\quad a$ | P (lokální, velký box) |
> | 2. | $\qquad b$ | P (lokální, malý box) |
> | 3. | $\qquad a$ | it 1 |
> | 4. | $\quad b \Rightarrow a$ | $\Rightarrow$i 2–3 (malý box) |
> | 5. | $a \Rightarrow (b \Rightarrow a)$ | $\Rightarrow$i 1–4 (velký box) |
>
> Řádek 3 je potřeba, protože malý box musí končit formulí $a$, aby z něj šlo udělat $b \Rightarrow a$. Tato posloupnost formulí je **odvození** (důkaz) formule $a \Rightarrow (b \Rightarrow a)$, tedy $\vdash a \Rightarrow (b \Rightarrow a)$.

^priklad-k

> [!example] $\neg a \vee b \vdash a \Rightarrow b$ · slajd 10
> Rozbor případů ($\vee$e): v obou případech se dokáže $a \Rightarrow b$.
>
> | # | formule | odůvodnění |
> |---|---|---|
> | 1. | $\neg a \vee b$ | P (globální) |
> | 2. | $\quad \neg a$ | P (1. případ) |
> | 3. | $\qquad a$ | P |
> | 4. | $\qquad \bot$ | $\neg$e 3, 2 |
> | 5. | $\qquad b$ | $\bot$e 4 |
> | 6. | $\quad a \Rightarrow b$ | $\Rightarrow$i 3–5 |
> | 7. | $\quad b$ | P (2. případ) |
> | 8. | $\qquad a$ | P |
> | 9. | $\qquad b$ | it 7 |
> | 10. | $\quad a \Rightarrow b$ | $\Rightarrow$i 8–9 |
> | 11. | $a \Rightarrow b$ | $\vee$e 1, boxy 2–6, 7–10 |

^priklad-disjunkce

> [!obrazek] Boxy v odvozeních
> ![[lgr06-boxy.png]]
> *Červeně globální předpoklad, oranžově rámečky boxů a jejich lokální předpoklady, modře odvozené řádky, zeleně výsledek. Vnořený box se uzavře dřív než vnější.*

> [!navic] Proč to pravidla dělají „správně“
> V prvním případě ($\neg a$) je předpoklad $a$ ve sporu s $\neg a$, a ze sporu plyne cokoli, tedy i $b$. Odpovídá to tabulce implikace: při $a = 0$ je $a \Rightarrow b$ pravdivá vždy. Ve druhém případě platí $b$, takže $a \Rightarrow b$ platí, ať je $a$ jakékoli. Opačný směr $a \Rightarrow b \vdash \neg a \vee b$ potřebuje pravidlo navíc (TND, $\varphi \vee \neg\varphi$; slajd 12).

> [!question]- Kolik řádků by potřebovala pravdivostní tabulka pro ověření $\models a \Rightarrow (b \Rightarrow a)$?
> $2^2 = 4$. U formule se 30 proměnnými by to bylo přes miliardu řádků, odvození může být pořád krátké. Naopak dokázat, že $S \nvdash \varphi$, odvozením nejde: musel bys vyloučit všechna možná odvození (slajd 16).

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Proč se svědek splnitelnosti z rezoluční tabulky hledá pozpátku, a ne od první proměnné?
> Svědka známe jen pro **poslední** množinu $S^{(n)} = \emptyset$ (libovolné ohodnocení). Věta o eliminaci převádí svědka pro $S_0 \cup R_x$ na svědka pro předchozí množinu, takže se jde od konce k $S$.

> [!karta|02]- Proč při zpětném kroku stačí určit jen hodnotu eliminované proměnné $x_i$?
> Množina $S_0 \cup R_{x_i}$ neobsahuje $x_i$, takže její svědek je svědkem pro **obě** hodnoty $x_i$. Podle důkazu věty o eliminaci jedna z nich splní i $S_{x_i}$ a $S_{\neg x_i}$.

> [!karta|03]- Co se v rezoluční tabulce stane, když je $S_x = \emptyset$ nebo $S_{\neg x} = \emptyset$, a jakou hodnotu pak dáš $x$ ve svědkovi?
> Není s čím rezolvovat: **$R_x = \emptyset$** a klauzule s $x$ zmizí. Ve svědkovi dáš $x$ hodnotu, která je všechny splní: $x \mapsto 1$, když je $x$ jen pozitivně, $x \mapsto 0$, když jen negativně.

> [!karta|04]- Proč se tautologická rezolventa (např. $\neg y \vee y \vee \neg z$) do $R_x$ nezapisuje?
> Je pravdivá v každém ohodnocení, takže **nic nevyžaduje**: $u(S \cup \{\mathrm{tt}\}) = u(S)$. Navíc by porušila základní tvar ($y$ dvakrát).

> [!karta|05]- Jaký je rozdíl mezi $S \models \varphi$ a $S \vdash \varphi$?
> $S \models \varphi$ je **pravdivost** (sémantika): $\varphi$ platí v každém ohodnocení, kde platí $S$. $S \vdash \varphi$ je **odvoditelnost** (syntax): existuje odvození $\varphi$ z $S$ podle pravidel.

> [!karta|06]- Jakými nástroji se ověřuje $S \models \varphi$ a jakými $S \vdash \varphi$?
> $\models$: pravdivostní tabulka ($2^n$ řádků) nebo rezoluční metoda (v nejhorším případě taky exponenciální). $\vdash$: **důkazové systémy**, např. přirozená dedukce; stačí najít jedno odvození.

> [!karta|07]- Jaký je vztah množin odvoditelných a pravdivých formulí v korektním a v úplném systému?
> Korektní: **odvoditelné $\subseteq$ pravdivé** ($S \vdash \varphi \Rightarrow S \models \varphi$). Úplný: **odvoditelné $=$ pravdivé** ($S \vdash \varphi \Leftrightarrow S \models \varphi$).

> [!karta|08]- Jaké dva druhy důkazových systémů nechceme a proč?
> **Příliš agresivní**: odvodí i formule, které neplatí (nekorektní, nejde mu věřit). **Sporný**: odvodí všechno, i $\varphi$ a $\neg\varphi$, takže nic nerozliší.

> [!karta|09]- Čím se liší Hilbertův systém od přirozené dedukce?
> Hilbert: **hodně axiomů, málo pravidel** (tři typy axiomů, jen modus ponens, spojky $\neg$, $\Rightarrow$). Přirozená dedukce (Gentzen): **žádné axiomy, hodně pravidel**, i- a e-pravidlo ke každé spojce.

> [!karta|10]- Co dělá i-pravidlo a co e-pravidlo spojky v přirozené dedukci?
> **i-pravidlo** (zavedení) říká, jak formuli s danou spojkou **dokázat**; **e-pravidlo** (odstranění) říká, jak ji **použít** v dalším odvozování.

> [!karta|11]- Proč pravidlo $\wedge$i respektuje pravdivost?
> Platí $\{\varphi, \psi\} \models \varphi \wedge \psi$: je-li v $u$ pravdivá $\varphi$ i $\psi$, je **$u(\varphi \wedge \psi) = 1$**.

> [!karta|12]- Proč pravidlo $\Rightarrow$i respektuje pravdivost?
> Indukční předpoklad: uvnitř boxu se pravdivost respektuje, tedy **$S \cup \{\varphi\} \models \psi$**. Podle věty o dedukci pak $S \models \varphi \Rightarrow \psi$; pro $S = \emptyset$ je $\varphi \Rightarrow \psi$ tautologie.

> [!karta|13]- Proč se formule z uzavřeného boxu nesmí použít mimo něj?
> Platí jen **za lokálního předpokladu**. Kdyby šla ven, dokázal by se z ničeho třeba $a$ (otevřít box s $a$, uzavřít, použít $a$), ale $a$ není tautologie: systém by byl nekorektní.

> [!karta|14]- Proč je v odvození $\vdash a \Rightarrow (b \Rightarrow a)$ potřeba iterace?
> Malý box s předpokladem $b$ musí **končit formulí $a$**, aby z něj $\Rightarrow$i udělalo $b \Rightarrow a$. Formule $a$ je o patro výš (řádek 1), tak se do boxu zkopíruje: „it 1“.

> [!karta|15]- Jak je postaveno odvození $\neg a \vee b \vdash a \Rightarrow b$?
> **Rozbor případů** ($\vee$e na řádek 1): v boxu $\neg a$ z předpokladu $a$ vznikne $\bot$ ($\neg$e) a z něj $b$ ($\bot$e), tedy $a \Rightarrow b$; v boxu $b$ stačí $a$ předpokládat a $b$ zopakovat (it). Oba boxy dají $a \Rightarrow b$.

### Příklady na procvičení

> [!priklad|16]- Rozhodni rezoluční tabulkou (pořadí $x, y, z, w$), zda je splnitelná $S = \{x \vee y \vee w,\ x \vee \neg y,\ \neg x \vee y \vee \neg z,\ y \vee z \vee \neg w,\ z \vee w,\ \neg w\}$, a najdi svědka.
> $R_x = \{y \vee w \vee \neg z\}$ (druhá rezolventa je tautologie), $S' = \{y \vee z \vee \neg w, z \vee w, \neg w, y \vee w \vee \neg z\}$; $R_y = \emptyset$, $S'' = \{z \vee w, \neg w\}$; $R_z = \emptyset$, $S''' = \{\neg w\}$; $R_w = \emptyset$, $S'''' = \emptyset$: **splnitelná**. Pozpátku $w \mapsto 0$, $z \mapsto 1$, $y \mapsto 1$, $x \mapsto 1$: svědek **$x = y = z = 1$, $w = 0$**.

> [!priklad|17]- Pro $S$ z příkladu 16 a $u'$: $y \mapsto 1, z \mapsto 1, w \mapsto 0$ rozhodni, který z $u'_0$ ($x \mapsto 0$) a $u'_1$ ($x \mapsto 1$) je svědkem pro $S$.
> $u'_0$ pokazí $x \vee \neg y$ ($0 \vee 0$). $u'_1$ splní $x \vee y \vee w$ i $x \vee \neg y$ díky $x$ a $\neg x \vee y \vee \neg z$ díky $y$. **Svědkem je $u'_1$.**

> [!priklad|18]- Odvoď v přirozené dedukci $a \wedge b \vdash b \wedge a$.
> 1. $a \wedge b$ P; 2. $a$ $\wedge$e₁ 1; 3. $b$ $\wedge$e₂ 1; 4. **$b \wedge a$ $\wedge$i 3, 2**.

> [!priklad|19]- Odvoď $\vdash a \Rightarrow (b \Rightarrow a)$.
> 1. $a$ P (box); 2. $b$ P (vnořený box); 3. $a$ it 1; 4. $b \Rightarrow a$ $\Rightarrow$i 2–3; 5. **$a \Rightarrow (b \Rightarrow a)$ $\Rightarrow$i 1–4**.

> [!priklad|20]- Odvoď $\neg a \vee b \vdash a \Rightarrow b$.
> 1. $\neg a \vee b$ P. Box: 2. $\neg a$ P; box 3. $a$ P; 4. $\bot$ $\neg$e 3, 2; 5. $b$ $\bot$e 4; 6. $a \Rightarrow b$ $\Rightarrow$i 3–5. Box: 7. $b$ P; box 8. $a$ P; 9. $b$ it 7; 10. $a \Rightarrow b$ $\Rightarrow$i 8–9. 11. **$a \Rightarrow b$ $\vee$e 1, 2–6, 7–10**.

> [!priklad|21]- Odvoď $\vdash a \Rightarrow a$.
> 1. $a$ P (box); 2. **$a \Rightarrow a$ $\Rightarrow$i 1–1**. Box může mít jediný řádek: předpoklad je zároveň jeho poslední formule.

> [!priklad|22]- Odvoď $a \Rightarrow (b \Rightarrow c) \vdash (a \wedge b) \Rightarrow c$.
> 1. $a \Rightarrow (b \Rightarrow c)$ P. Box: 2. $a \wedge b$ P; 3. $a$ $\wedge$e₁ 2; 4. $b$ $\wedge$e₂ 2; 5. $b \Rightarrow c$ $\Rightarrow$e 3, 1; 6. $c$ $\Rightarrow$e 4, 5. 7. **$(a \wedge b) \Rightarrow c$ $\Rightarrow$i 2–6**.

### Typové příklady na semestrální test

*Stejný typ úloh jako na 1. semestrálním testu (rezoluce ve výrokové logice). Na testu je potřeba každé tvrzení zdůvodnit.*

> [!priklad|23]- Rozhodni rezoluční tabulkou (pořadí $a, b, c, d$), zda je splnitelná $S = \{a \vee b,\ \neg a \vee c,\ \neg b \vee c,\ \neg c \vee d,\ \neg d\}$.
> $a$: $R_a = \{b \vee c\}$, $S' = \{b \vee c, \neg b \vee c, \neg c \vee d, \neg d\}$. $b$: $R_b = \{c\}$ ($c \vee c = c$), $S'' = \{c, \neg c \vee d, \neg d\}$. $c$: $R_c = \{d\}$, $S''' = \{d, \neg d\}$. $d$: $R_d = \{\mathrm{ff}\}$. Konec $\{\mathrm{ff}\}$: **nesplnitelná**.

> [!priklad|24]- Rozhodni rezoluční tabulkou (pořadí $x, y, z, w$), zda je splnitelná $S = \{x \vee y,\ \neg x \vee z,\ \neg y \vee z,\ \neg z \vee w,\ x \vee \neg w\}$, a případně najdi svědka.
> $x$: $R_x = \{y \vee z,\ z \vee \neg w\}$, $S' = \{y \vee z, z \vee \neg w, \neg y \vee z, \neg z \vee w\}$. $y$: $R_y = \{z\}$, $S'' = \{z, z \vee \neg w, \neg z \vee w\}$. $z$: $R_z = \{w\}$ ($\mathrm{res}_z(z \vee \neg w, \neg z \vee w)$ je tautologie), $S''' = \{w\}$. $w$: $S'''' = \emptyset$: **splnitelná**. Pozpátku: $w \mapsto 1$ (kvůli $w$), $z \mapsto 1$ (kvůli $z$), $y \mapsto 0$ stačí ($y \vee z$ i $\neg y \vee z$ platí díky $z$), $x \mapsto 1$ (kvůli $x \vee y$). Svědek **$x = 1$, $y = 0$, $z = 1$, $w = 1$**.

> [!priklad|25]- Rozhodni rezolucí, zda $\{a \Rightarrow b,\ b \Rightarrow c\} \models a \Rightarrow c$.
> Podle věty o sémantickém důkazu sporem stačí ukázat, že $\{\neg a \vee b,\ \neg b \vee c,\ \neg(a \Rightarrow c)\}$ je nesplnitelná; $\neg(a \Rightarrow c) \mathrel{\vert\!=\!\vert} a \wedge \neg c$ dá klauzule $a$, $\neg c$. Tabulka: $a$: $R_a = \{b\}$, $S' = \{b, \neg b \vee c, \neg c\}$; $b$: $S'' = \{c, \neg c\}$; $c$: $\{\mathrm{ff}\}$. Nesplnitelná, tedy **důsledek platí**.

---
← [[LGR 05 – Rezoluční princip|9. 10. 2026 Rezoluční princip]]

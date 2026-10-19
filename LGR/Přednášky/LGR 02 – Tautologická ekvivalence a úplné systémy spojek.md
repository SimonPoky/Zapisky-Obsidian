---
predmet: LGR
prednaska: 2
datum: 2026-09-25
zdroj: "Prezentace 1 (Výroková logika), slajdy 15–21; Prezentace 2 (Sémantika výrokové logiky), slajdy 3–4"
tags: [prednaska, LGR]
---

# LGR 02 – Tautologická ekvivalence a úplné systémy spojek

*Přednáška 2 · pátek 25. 9. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 1 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1.pdf) · [Verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_1a.pdf)

Témata: `formalizace` · `booleovská funkce` · `|=|` · `pravidla ekvivalence` · `NAND, NOR, XOR` · `úplný systém spojek`

Minule byla [[formule]] a její [[pravdivostní ohodnocení]]. Dnes: jak přeložit větu do formule, kdy dvě různé formule „znamenají totéž“ a kolik spojek vlastně potřebuješ.

## §0 Přehled na jedné stránce

| pojem | značka | význam |
|---|---|---|
| [[tautologická ekvivalence]] | $\alpha \mathrel{\vert\!=\!\vert} \beta$ | stejná hodnota v každém ohodnocení |
| [[booleovská funkce]] | $f : \{0, 1\}^n \to \{0, 1\}$ | sloupec pravdivostní tabulky; pro $n$ proměnných jich je $2^{2^n}$ |
| NAND, NOR, XOR | $\mid$, $\downarrow$, $\oplus$ | $\neg(\alpha \wedge \beta)$, $\neg(\alpha \vee \beta)$, $\neg(\alpha \Leftrightarrow \beta)$ |
| [[úplný systém logických spojek]] | např. $\{\neg, \wedge, \vee\}$, $\{\mid\}$ | dá se jím zapsat každá booleovská funkce |

## §1 Formalizace věty

> [!example] Bude-li pršet a nebudu-li líný, půjdu do školy.
> Logické proměnné: $p$ … prší, $l$ … jsem líný, $š$ … půjdu do školy. Formalizace:
>
> $$
> (p \wedge \neg l) \Rightarrow š
> $$
>
> - **$p \mapsto 1$, $l \mapsto 1$, $š \mapsto {?}$: je formule pravdivá?** Ano, a to bez ohledu na $š$. Předpoklad $p \wedge \neg l = 1 \wedge 0 = 0$ a [[implikace]] s nepravdivým předpokladem je pravdivá.
> - **Je to [[tautologie]]?** Ne: pro $p \mapsto 1$, $l \mapsto 0$, $š \mapsto 0$ je $1 \Rightarrow 0 = 0$.

^formalizace

> [!obrazek] Vyhodnocení stromem
> ![[lgr02-strom.png]]
> *Čísla u vrcholů jsou hodnoty podformulí, zeleně 1 a červeně 0, počítané od listů (oranžové proměnné) ke kořeni. Vlevo ohodnocení p ↦ 1, l ↦ 1, š ↦ 0 (výsledek 1), vpravo protipříklad k tautologii (výsledek 0).*

Formule je nepravdivá jen v 1 z 8 ohodnocení (12,5 %), a to přesně v řádku $p = 1, l = 0, š = 0$: prší, nejsem líný, a přesto do školy nejdu.

> [!navic] Tři významy slova „ekvivalence“
> 1. $\Leftrightarrow$ je **logická spojka**, část formule: $a \Leftrightarrow b$ je formule.
> 2. $\mathrel{\vert\!=\!\vert}$ je **vztah mezi formulemi**, tvrzení o nich (v metajazyce): „$\alpha$ a $\beta$ mají vždy stejnou hodnotu“. Samo formulí není.
> 3. **Relace ekvivalence** je obecný matematický pojem: reflexivní, symetrická a tranzitivní relace. $\mathrel{\vert\!=\!\vert}$ je jedna taková relace na $\mathrm{Fle}(A)$.

## §2 Booleovská funkce

Vyplněná pravdivostní tabulka určuje tzv. [[booleovská funkce|booleovskou funkci]]. Pro formuli výše:

$$
f : \{0, 1\}^3 \to \{0, 1\}: \quad (0, 0, 0) \mapsto 1,\ (0, 0, 1) \mapsto 1,\ \dots,\ (1, 0, 0) \mapsto 0,\ \dots,\ (1, 1, 1) \mapsto 1.
$$

> [!definice] Booleovská funkce · slajd 15
> Každá funkce $f : \{0, 1\}^n \to \{0, 1\}$ se nazývá *booleovská funkce* ($n$ proměnných).

^def-boolfce

> [!lidsky] Lidsky
> Booleovská funkce bere jako vstup několik logických hodnot (0/1) a vrací jednu hodnotu. Je to přesně sloupec výsledků v pravdivostní tabulce, bez ohledu na to, jakou formulí vznikl. Logický obvod v počítači je booleovská funkce vyrobená z hradel.

**Kolik jich je:** vstupů je $2^n$ (řádky tabulky) a do každého řádku se píše 0 nebo 1, takže funkcí je $2^{2^n}$.

| $n$ | řádků $2^n$ | booleovských funkcí $2^{2^n}$ |
|---|---|---|
| 1 | 2 | 4 |
| 2 | 4 | 16 |
| 3 | 8 | 256 |
| 4 | 16 | 65 536 |

## §3 Tautologická ekvivalence

> [!definice] Tautologická ekvivalence · slajd 15
> Formule $\varphi$ a $\psi$ jsou *tautologicky ekvivalentní*, jestliže pro každé ohodnocení $u$ platí $u(\varphi) = u(\psi)$. Značíme $\varphi \mathrel{\vert\!=\!\vert} \psi$.

^def-tautekv

> [!lidsky] Lidsky
> Dvě formule říkají totéž, jen jinými slovy: v tabulce mají stejný sloupec. „Nepravda, že prší i fouká“ a „neprší, nebo nefouká“ jsou různé věty, ale pravdivé jsou přesně ve stejných situacích.

> [!pozor] Ekvivalentní jsou formule, ne funkce
> Tautologicky ekvivalentní jsou **dvě formule**, a to když **určují stejnou booleovskou funkci** (mají stejný sloupec v tabulce). Říkat, že ekvivalentní jsou dvě booleovské funkce, nedává smysl: dvě funkce se stejnými hodnotami jsou jedna a táž funkce.

Příklady: $\alpha \mathrel{\vert\!=\!\vert} \neg\neg\alpha$ a

$$
(p \wedge \neg l) \Rightarrow š \;\mathrel{\vert\!=\!\vert}\; \neg(p \wedge \neg l \wedge \neg š).
$$

Obě formule jsou nepravdivé jen pro $p = 1, l = 0, š = 0$ ✓.

> [!veta] Tvrzení · slajd 16
> - ==Pro formule $\alpha, \beta$:== **$\alpha \mathrel{\vert\!=\!\vert} \beta$ právě tehdy, když $\alpha \Leftrightarrow \beta$ je tautologie.**
> - ==Je-li $\alpha \mathrel{\vert\!=\!\vert} \gamma$ a $\beta \mathrel{\vert\!=\!\vert} \delta$,== pak **$\neg\alpha \mathrel{\vert\!=\!\vert} \neg\gamma$ a $\alpha \circ \beta \mathrel{\vert\!=\!\vert} \gamma \circ \delta$** pro každou binární spojku $\circ$.
> - $\mathrel{\vert\!=\!\vert}$ je relace ekvivalence na $\mathrm{Fle}(A)$ a pro $|A| = n$ ji rozkládá na $2^{2^n}$ tříd (slajd 19).

^veta-tautekv

> [!lidsky] Lidsky
> S $\mathrel{\vert\!=\!\vert}$ se dá zacházet podobně jako s $=$ v rovnicích: kus formule smíš nahradit ekvivalentním kusem a výsledek zůstane ekvivalentní. Pozor jen, že $\alpha \mathrel{\vert\!=\!\vert} \beta$ neznamená $\alpha = \beta$: jsou to různé řetězce se stejným významem. Tříd je tolik, kolik je booleovských funkcí: každá třída = jeden možný sloupec tabulky.

### Pravidla (slajdy 17–18)

Nejpoužívanější pravidla (úplný seznam je v prezentaci):

| pravidlo | tvar | lidsky |
|---|---|---|
| dvojitá negace | $\neg\neg\alpha \mathrel{\vert\!=\!\vert} \alpha$ | „není pravda, že neprší“ = prší |
| komutativita | $\alpha \wedge \beta \mathrel{\vert\!=\!\vert} \beta \wedge \alpha$, stejně $\vee$ | na pořadí nezáleží |
| asociativita | $\alpha \wedge (\beta \wedge \gamma) \mathrel{\vert\!=\!\vert} (\alpha \wedge \beta) \wedge \gamma$, stejně $\vee$ | závorky jde vynechat: $a \vee b \vee c$ |
| idempotence | $\alpha \wedge \alpha \mathrel{\vert\!=\!\vert} \alpha$, $\alpha \vee \alpha \mathrel{\vert\!=\!\vert} \alpha$ | zopakovat nic nemění |
| absorpce | $\alpha \wedge (\beta \vee \alpha) \mathrel{\vert\!=\!\vert} \alpha$, $\alpha \vee (\beta \wedge \alpha) \mathrel{\vert\!=\!\vert} \alpha$ | silnější podmínka „pohltí“ slabší |
| De Morgan | $\neg(\alpha \wedge \beta) \mathrel{\vert\!=\!\vert} \neg\alpha \vee \neg\beta$, $\neg(\alpha \vee \beta) \mathrel{\vert\!=\!\vert} \neg\alpha \wedge \neg\beta$ | negace otočí $\wedge$ na $\vee$ a naopak |
| distributivita | $\alpha \wedge (\beta \vee \gamma) \mathrel{\vert\!=\!\vert} (\alpha \wedge \beta) \vee (\alpha \wedge \gamma)$ a duálně | roznásobení závorky |
| implikace | $\alpha \Rightarrow \beta \mathrel{\vert\!=\!\vert} \neg\alpha \vee \beta$ | buď předpoklad neplatí, nebo platí závěr |
| obměna | $\alpha \Rightarrow \beta \mathrel{\vert\!=\!\vert} \neg\beta \Rightarrow \neg\alpha$ | základ důkazu obměnou |
| ekvivalence | $\alpha \Leftrightarrow \beta \mathrel{\vert\!=\!\vert} (\alpha \Rightarrow \beta) \wedge (\beta \Rightarrow \alpha)$ | „právě když“ = implikace oběma směry |

## §4 Další logické spojky

> [!definice] Nulární a další binární spojky · slajdy 19–20
> | $\mathrm{tt}$ | $\mathrm{ff}$ |
> |---|---|
> | 1 | 0 |
>
> | $\alpha$ | $\beta$ | $\alpha \mid \beta$ | $\alpha \downarrow \beta$ | $\alpha \oplus \beta$ |
> |---|---|---|---|---|
> | 0 | 0 | 1 | 1 | 0 |
> | 0 | 1 | 1 | 0 | 1 |
> | 1 | 0 | 1 | 0 | 1 |
> | 1 | 1 | 0 | 0 | 0 |
>
> $\mid$ je NAND ([[Shefferova čárka]]), $\downarrow$ je NOR ([[Peirceova šipka]]), $\oplus$ je XOR ([[vylučovací nebo]]).

^def-spojky

> [!veta] Jak je vyjádřit základními spojkami · slajd 21
> $\alpha \mid \beta \mathrel{\vert\!=\!\vert} \neg(\alpha \wedge \beta)$, $\quad \alpha \downarrow \beta \mathrel{\vert\!=\!\vert} \neg(\alpha \vee \beta)$, $\quad \alpha \oplus \beta \mathrel{\vert\!=\!\vert} (\alpha \wedge \neg\beta) \vee (\neg\alpha \wedge \beta) \mathrel{\vert\!=\!\vert} \neg(\alpha \Leftrightarrow \beta)$.
>
> Dále $\alpha \vee \neg\alpha \mathrel{\vert\!=\!\vert} \mathrm{tt}$ (vyloučení třetího) a $\alpha \wedge \neg\alpha \mathrel{\vert\!=\!\vert} \mathrm{ff}$ (zákon sporu).

^veta-vyjadreni-spojek

> [!lidsky] Lidsky
> XOR je „buď, anebo“: v menu „polévka nebo dezert“ dostaneš jedno, ne obojí. NAND je „ne obojí zároveň“ a NOR „ani jedno“. Počítačové čipy se staví hlavně z hradel NAND, protože z nich jde složit úplně všechno (§5).

## §5 Úplný systém logických spojek

> [!definice] Úplný systém logických spojek · prezentace 2, slajd 3
> Systém logických spojek je *úplný*, jestliže se pomocí něj dá pro každou booleovskou funkci napsat formule, která ji určuje.

^def-uss

> [!lidsky] Lidsky
> Úplný systém je stavebnice, ze které složíš libovolný obvod. Pro každou tabulku (booleovskou funkci) najdeš formuli jen z dovolených spojek. Stačí přitom ukázat, že ze stavebnice jde vyrobit $\neg$ a $\wedge$ (nebo $\neg$ a $\vee$).

Jak na to: přepisovat pravidly ze §3.

- $\{\neg, \wedge, \vee, \Rightarrow, \Leftrightarrow\} \to \{\neg, \wedge, \vee\}$:
 $\alpha \Leftrightarrow \beta \mathrel{\vert\!=\!\vert} (\alpha \Rightarrow \beta) \wedge (\beta \Rightarrow \alpha)$ a $\alpha \Rightarrow \beta \mathrel{\vert\!=\!\vert} \neg\alpha \vee \beta$.
- Podobnými úpravami se dosáhne i $\{\neg, \vee\}$, $\{\neg, \wedge\}$, $\{\neg, \Rightarrow\}$ a dokonce jediné spojky: $\{\downarrow\}$ (NOR) nebo $\{\mid\}$ (NAND).
- Naopak $\{\neg\}$ ani $\{\wedge, \vee, \Rightarrow, \Leftrightarrow\}$ úplné **nejsou**.

> [!navic] Konkrétní přepisy
> | systém | chybějící spojka | přepis |
> |---|---|---|
> | $\{\neg, \vee\}$ | $\wedge$ | $\alpha \wedge \beta \mathrel{\vert\!=\!\vert} \neg(\neg\alpha \vee \neg\beta)$ (De Morgan) |
> | $\{\neg, \wedge\}$ | $\vee$ | $\alpha \vee \beta \mathrel{\vert\!=\!\vert} \neg(\neg\alpha \wedge \neg\beta)$ |
> | $\{\neg, \Rightarrow\}$ | $\vee$ | $\alpha \vee \beta \mathrel{\vert\!=\!\vert} \neg\alpha \Rightarrow \beta$ |
> | $\{\mid\}$ | $\neg$, $\wedge$ | $\neg\alpha \mathrel{\vert\!=\!\vert} \alpha \mid \alpha$, $\quad \alpha \wedge \beta \mathrel{\vert\!=\!\vert} (\alpha \mid \beta) \mid (\alpha \mid \beta)$ |
> | $\{\downarrow\}$ | $\neg$, $\vee$ | $\neg\alpha \mathrel{\vert\!=\!\vert} \alpha \downarrow \alpha$, $\quad \alpha \vee \beta \mathrel{\vert\!=\!\vert} (\alpha \downarrow \beta) \downarrow (\alpha \downarrow \beta)$ |
>
> Stačí vždy vyrobit $\neg$ a jednu z $\wedge$, $\vee$; zbytek už umí $\{\neg, \wedge, \vee\}$.

> [!obrazek] Všechno z jediné spojky NAND
> ![[lgr02-nand.png]]
> *Syntaktické stromy jen se spojkou | (modře). Vlevo negace: a | a je pravdivé, právě když a není. Vpravo konjunkce: (a | b) je ¬(a ∧ b) a další | ho znovu zneguje. Z ¬ a ∧ se pak dá složit cokoliv.*

> [!obrazek] Všechno z jediné spojky NOR
> ![[lgr02-nor.png]]
> *Stejný trik se spojkou ↓ (modře). Vlevo negace: a ↓ a je pravdivé, právě když a není. Vpravo disjunkce: (a ↓ b) je ¬(a ∨ b) a další ↓ ho znovu zneguje. Z ¬ a ∨ se pak dá složit cokoliv.*

> [!navic] Proč je {¬, ∧, ∨} vůbec úplný
> Každou booleovskou funkci jde zapsat jako „OR řádků s jedničkou“: pro každý řádek, kde $f = 1$, napíšeš konjunkci proměnných (nebo jejich negací) popisující ten řádek a všechny je spojíš $\vee$. Pro XOR: $f = 1$ v řádcích $10$ a $01$, tedy $(a \wedge \neg b) \vee (\neg a \wedge b)$. Tomuto tvaru se říká *disjunktivní normální forma* a je na programu příští týden.

> [!navic] Proč {¬} a {∧, ∨, ⇒, ⇔} úplné nejsou
> - **$\{\neg\}$:** formule jen s negací obsahuje jedinou proměnnou (např. $\neg\neg a$), takže nezapíše nic, co závisí na dvou proměnných, třeba $a \wedge b$.
> - **$\{\wedge, \vee, \Rightarrow, \Leftrightarrow\}$:** všechny čtyři spojky dají $1$, když jsou oba vstupy $1$. Každá formule z nich je proto pravdivá v ohodnocení „vše $= 1$“ a nikdy nezapíše $\neg a$ ani $\mathrm{ff}$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|04]- Jaké tři významy má v logice slovo „ekvivalence“?
> 1. **spojka** $\Leftrightarrow$ uvnitř formule
> 2. **vztah** $\mathrel{\vert\!=\!\vert}$ mezi dvěma formulemi
> 3. **relace ekvivalence** (reflexivní, symetrická, tranzitivní)

> [!karta|05]- Kolik je booleovských funkcí $n$ proměnných? Kolik pro $n = 2$ a $n = 3$?
> $2^{2^n}$: tabulka má $2^n$ řádků a v každém je 0 nebo 1. Pro $n = 2$ je jich $16$, pro $n = 3$ už $256$.

> [!karta|06]- Jak převedeš ověření $\alpha \mathrel{\vert\!=\!\vert} \beta$ na tautologii?
> $\alpha \mathrel{\vert\!=\!\vert} \beta$ právě tehdy, když $\alpha \Leftrightarrow \beta$ je **tautologie**.

> [!karta|08]- Kolik tříd má $\mathrel{\vert\!=\!\vert}$ na formulích s $n$ proměnnými a proč?
> $2^{2^n}$: každá třída odpovídá jedné booleovské funkci (jednomu možnému sloupci tabulky).

> [!karta|09]- Napiš obě De Morganova pravidla.
> $\neg(\alpha \wedge \beta) \mathrel{\vert\!=\!\vert} \neg\alpha \vee \neg\beta$ a $\neg(\alpha \vee \beta) \mathrel{\vert\!=\!\vert} \neg\alpha \wedge \neg\beta$.

> [!karta|10]- Přepiš $\alpha \Rightarrow \beta$ pomocí $\neg$ a $\vee$ a napiš její obměnu.
> $\alpha \Rightarrow \beta \mathrel{\vert\!=\!\vert} \neg\alpha \vee \beta \mathrel{\vert\!=\!\vert} \neg\beta \Rightarrow \neg\alpha$.

> [!karta|13]- Proč platí $\alpha \oplus \beta \mathrel{\vert\!=\!\vert} \neg(\alpha \Leftrightarrow \beta)$?
> $\oplus$ je pravdivá, právě když mají $\alpha, \beta$ **různé** hodnoty, a $\Leftrightarrow$ právě když **stejné**. Sloupce jsou tedy přesně opačné, takže $\oplus$ je negace $\Leftrightarrow$.

> [!karta|14]- Proč $\{\wedge, \vee, \Rightarrow, \Leftrightarrow\}$ není úplný systém spojek?
> Všechny čtyři dají $1$ pro vstupy $1, 1$, takže každá formule z nich je pravdivá v ohodnocení „vše $= 1$“. Nejde zapsat $\neg a$ ani $\mathrm{ff}$.

> [!karta|15]- Proč $\{\neg\}$ není úplný systém spojek?
> Formule jen s negací obsahuje jedinou proměnnou ($\neg\neg a$), takže nezapíše nic, co závisí na dvou proměnných, např. $a \wedge b$.

> [!karta|16]- Proč je $\{\neg, \wedge, \vee\}$ úplný systém (myšlenka)?
> Každou booleovskou funkci zapíšeš jako $\vee$ konjunkcí popisujících řádky s $f = 1$ (disjunktivní normální forma). Např. XOR $= (a \wedge \neg b) \vee (\neg a \wedge b)$.

### Příklady na procvičení

> [!priklad|01]- Formalizuj: „Bude-li pršet a nebudu-li líný, půjdu do školy.“
> $(p \wedge \neg l) \Rightarrow š$, kde $p$ … prší, $l$ … jsem líný, $š$ … půjdu do školy.

> [!priklad|02]- Proč je $(p \wedge \neg l) \Rightarrow š$ pravdivá pro $p \mapsto 1$, $l \mapsto 1$ bez ohledu na $š$?
> Předpoklad $p \wedge \neg l = 1 \wedge 0 = 0$ a implikace s nepravdivým předpokladem je vždy pravdivá.

> [!priklad|03]- Je $(p \wedge \neg l) \Rightarrow š$ tautologie?
> **Ne.** Pro $p \mapsto 1$, $l \mapsto 0$, $š \mapsto 0$ je $1 \Rightarrow 0 = 0$. Je to jediný nepravdivý řádek z 8.

> [!priklad|07]- Jsou $(p \wedge \neg l) \Rightarrow š$ a $\neg(p \wedge \neg l \wedge \neg š)$ tautologicky ekvivalentní?
> **Ano.** Obě jsou nepravdivé jen pro $p = 1, l = 0, š = 0$.

> [!priklad|11]- Vyjádři $\neg\alpha$ a $\alpha \wedge \beta$ jen pomocí NAND ($\mid$).
> $\neg\alpha \mathrel{\vert\!=\!\vert} \alpha \mid \alpha$ a $\alpha \wedge \beta \mathrel{\vert\!=\!\vert} (\alpha \mid \beta) \mid (\alpha \mid \beta)$.

> [!priklad|12]- Vyjádři $\alpha \vee \beta$ v systému $\{\neg, \Rightarrow\}$.
> $\alpha \vee \beta \mathrel{\vert\!=\!\vert} \neg\alpha \Rightarrow \beta$.

---
← [[LGR 01 – Syntax a sémantika výrokové logiky|24. 9. 2026 Syntax a sémantika výrokové logiky]] · [[LGR 03 – Disjunktivní a konjunktivní normální forma|1. 10. 2026 Disjunktivní a konjunktivní normální forma]] →

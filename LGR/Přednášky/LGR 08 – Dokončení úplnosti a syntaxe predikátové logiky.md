---
predmet: LGR
prednaska: 8
datum: 2026-10-23
zdroj: "handout 4D, slajdy 13–14; handout 5, slajdy 1–22"
tags: [prednaska, LGR]
---

# LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky

*Přednáška 8 · pátek 23. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [handout 4D ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_4D.pdf) · [handout 5 ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_5.pdf)

Témata: `lemma o literálech řádku: krok pro ⇒` `kroky pro ∧ a ∨` `predikátová logika 1. řádu` `jazyk a arita` `termy` `atomické formule a kvantifikátory` `volný a vázaný výskyt` `legální přejmenování` `sentence` `interpretace` `formalizace vět`

Minule zbyl v důkazu [[lemma o literálech řádku|lemmatu o literálech řádku]] nedodělaný krok pro implikaci; dnes se dokončí, a tím je hotový celý důkaz [[věta o úplnosti|věty o úplnosti]] přirozené dedukce. Pak začíná **predikátová logika**: proměnné už nejsou celé výroky, ale objekty, o kterých se mluví, a přibývají kvantifikátory „pro každé“ a „existuje“. Zavede se, jak vypadají termy a formule, kdy je proměnná volná a kdy vázaná, a jak se symbolům jazyka dá význam (interpretace).

## §0 Přehled na jedné stránce

| pojem | zápis | význam |
|---|---|---|
| krok lemmatu pro ⇒ | $u(\alpha \Rightarrow \beta) = 1$: $L_u \vdash \alpha \Rightarrow \beta$ | z odvození $\neg\alpha$ nebo $\beta$ se složí odvození implikace |
| | $u(\alpha \Rightarrow \beta) = 0$: $L_u \vdash \neg(\alpha \Rightarrow \beta)$ | z odvození $\alpha$ a $\neg\beta$ se složí spor |
| predikátová logika 1. řádu | $\forall$, $\exists$, $P(x, f(x))$ | proměnné zastupují objekty jednoho typu |
| jazyk | Var, Pred, Func, Kons, arita | z čeho se staví termy a formule |
| term | $x$, $a$, $f(t_1, \dots, t_n)$ | popis objektu |
| atomická formule | $P(t_1, \dots, t_n)$, $t_1 = t_2$ | nejjednodušší tvrzení o objektech |
| formule | spojky a $\forall x\,\varphi$, $\exists x\,\varphi$ | tvrzení postavené z atomických formulí |
| vázaný výskyt | cestou ke kořeni je $\forall x$ / $\exists x$ | $x$ „patří“ kvantifikátoru |
| volný výskyt | žádný kvantifikátor s $x$ nad ním | $x$ čeká na dosazení |
| legální přejmenování | $\forall x\,\alpha \to \forall y\,\alpha[x/y]$ | žádná volná proměnná nesmí zachytit |
| sentence / otevřená formule | žádná volná / žádná vázaná proměnná | uzavřené tvrzení / „šablona“ |
| interpretace | $(U, [\![-]\!])$ | universum a význam každého symbolu |

## §1 Dokončení lemmatu o literálech řádku

### Co se dokazuje

Lemma se dokazuje [[strukturální indukce|strukturální indukcí]]. Množina [[formule|formulí]] nad proměnnými $A = \{x, y, z\}$ vzniká tak, že (1) každá proměnná je formule, (2) jsou-li $\alpha$, $\beta$ formule, jsou jimi i $(\neg\alpha)$, $(\alpha \wedge \beta)$, $(\alpha \vee \beta)$, $(\alpha \Rightarrow \beta)$, a (3) nic jiného, jen to, co vznikne konečně mnoha kroky. Třeba $\varphi = (x \Rightarrow y) \wedge \neg z$ vznikne ve čtyřech krocích.

Pro každou formuli $\varphi$ se ověřuje **vlastnost $V(\varphi)$**: pro každé ohodnocení $u$ platí

$$
u(\varphi) = 1 \;\Rightarrow\; L_u \vdash \varphi, \qquad u(\varphi) = 0 \;\Rightarrow\; L_u \vdash \neg\varphi,
$$

kde $L_u$ jsou [[literály řádku]] $u$. Sémanticky je to zřejmé: $L_u$ je pravdivá jen v řádku $u$ (sloupec $L_u$ v tabulce má jedinou jedničku), takže pro $u = (1, 0, 0)$ je $\{x, \neg y, \neg z\} \models \varphi$ pro každou $\varphi$ s $u(\varphi) = 1$ a $\{x, \neg y, \neg z\} \models \neg\psi$ pro každou $\psi$ s $u(\psi) = 0$. Lemma chce totéž se znakem $\vdash$, tedy skutečné odvození.

Základ (proměnná) a krok pro $\neg$ jsou v [[LGR 07 – Odvozená pravidla, korektnost a úplnost|LGR 07]]. Zbývá krok pro implikaci.

### Krok pro implikaci

> [!veta] Lemma o literálech řádku, krok pro ⇒ · handout 4D, slajd 13
> Nechť ==vlastnost $V$ platí pro formule $\alpha$ a $\beta$== (indukční předpoklad). Pak **platí i pro $\varphi = \alpha \Rightarrow \beta$**: pro libovolné ohodnocení $u$ je $L_u \vdash \alpha \Rightarrow \beta$, když $u(\varphi) = 1$, a $L_u \vdash \neg(\alpha \Rightarrow \beta)$, když $u(\varphi) = 0$.
>
> > [!note]- Důkaz rozborem řádků tabulky
> > Zvolíme libovolné $u$. Podle hodnot $u(\alpha)$, $u(\beta)$ je to jeden ze čtyř řádků $u_1, \dots, u_4$ tabulky implikace. Indukční předpoklad dá odvození $\alpha$ nebo $\neg\alpha$ a $\beta$ nebo $\neg\beta$ z $L_u$; ta napíšeme pod sebe („to máme“) a pak odvození dokončíme („tak to nastavíme“).
> >
> > **1) $u(\varphi) = 1$**, tedy $u$ je $u_1$, $u_2$ nebo $u_4$.
> >
> > *$u_4$: $u(\alpha) = 1$, $u(\beta) = 1$.* Podle indukčního předpokladu $L_u \vdash \beta$. V boxu s pomocným předpokladem $\alpha$ zopakujeme $\beta$ a $\Rightarrow$i dá $\alpha \Rightarrow \beta$:
> > $$
> > \begin{array}{rll}\text{1.} & \tilde x_1 & \text{P} \\  & \vdots &  \\ \text{n.} & \tilde x_n & \text{P} \\  & \vdots &  \\ \text{l.} & \beta & \text{(ind. předp.)} \\  & \begin{array}{|rll|}\hline \text{l{+}1.} & \alpha & \text{P} \\ \text{l{+}2.} & \beta & \text{it}\ l \\ \hline\end{array} &  \\ \text{l{+}3.} & \alpha\Rightarrow\beta & {\Rightarrow}\text{i}\ l{+}1\text{–}l{+}2\end{array}
> > $$
> >
> > *$u_1$, $u_2$: $u(\alpha) = 0$.* Podle indukčního předpokladu $L_u \vdash \neg\alpha$. V boxu $\alpha$ vznikne spor s $\neg\alpha$ a ze sporu plyne cokoli, i $\beta$:
> > $$
> > \begin{array}{rll}\text{1.} & \tilde x_1 & \text{P} \\  & \vdots &  \\ \text{n.} & \tilde x_n & \text{P} \\  & \vdots &  \\ \text{k.} & \neg\alpha & \text{(ind. předp.)} \\  & \begin{array}{|rll|}\hline \text{k{+}1.} & \alpha & \text{P} \\ \text{k{+}2.} & \bot & {\neg}\text{e}\ k{+}1, k \\ \text{k{+}3.} & \beta & {\bot}\text{e}\ k{+}2 \\ \hline\end{array} &  \\ \text{k{+}4.} & \alpha\Rightarrow\beta & {\Rightarrow}\text{i}\ k{+}1\text{–}k{+}3\end{array}
> > $$
> >
> > Tedy ve všech třech řádcích $L_u \vdash \varphi$.
> >
> > **2) $u(\varphi) = 0$**, tedy $u = u_3$: $u(\alpha) = 1$, $u(\beta) = 0$. Podle indukčního předpokladu $L_u \vdash \alpha$ a $L_u \vdash \neg\beta$. Vezmeme obě odvození a předpokládáme $\alpha \Rightarrow \beta$: modus ponens dá $\beta$, to je spor s $\neg\beta$, a $\neg$i dá negaci implikace:
> > $$
> > \begin{array}{rll}\text{1.} & \tilde x_1 & \text{P} \\  & \vdots &  \\ \text{n.} & \tilde x_n & \text{P} \\  & \vdots &  \\ \text{k.} & \alpha & \text{(ind. předp.)} \\  & \vdots &  \\ \text{l.} & \neg\beta & \text{(ind. předp.)} \\  & \begin{array}{|rll|}\hline \text{l{+}1.} & \alpha\Rightarrow\beta & \text{P} \\ \text{l{+}2.} & \beta & {\Rightarrow}\text{e}\ k, l{+}1 \\ \text{l{+}3.} & \bot & {\neg}\text{e}\ l{+}2, l \\ \hline\end{array} &  \\ \text{l{+}4.} & \neg(\alpha\Rightarrow\beta) & {\neg}\text{i}\ l{+}1\text{–}l{+}3\end{array}
> > $$
> > Tedy $L_u \vdash \neg\varphi$.

^veta-lemma-implikace

> [!lidsky] Lidsky
> Implikace je pravdivá ze dvou důvodů: buď je pravdivý závěr $\beta$ („slib je splněn“), nebo je nepravdivý předpoklad $\alpha$ („slib nic neslibuje“). Na každý důvod je jedno krátké odvození. Nepravdivá je jen tehdy, když $\alpha$ platí a $\beta$ ne, a pak z ní plyne spor. Důkaz jen přepisuje tabulku implikace do pravidel přirozené dedukce.

> [!obrazek] Čtyři řádky tabulky implikace a jejich odvození
> ![[lgr08-implikace.png]]
> *Zeleně řádky, kde je $\alpha \Rightarrow \beta$ pravdivá (odvodí se $\alpha \Rightarrow \beta$), červeně řádek $u_3$, kde je nepravdivá (odvodí se její negace). Vlevo od šipky je, co dá indukční předpoklad, vpravo pravidla, kterými se odvození dokončí.*

> [!navic] Řádek $u_2$ jde dvěma cestami
> V $u_2$ je $u(\alpha) = 0$ i $u(\beta) = 1$, takže funguje odvození přes $\neg\alpha$ i přes $\beta$. V $u_4$ indukční předpoklad dává i $L_u \vdash \alpha$, k odvození implikace ho ale není potřeba: stačí $\beta$.

> [!navic]- Kroky pro ∧ a ∨ (stejný princip)
> **$\varphi = \alpha \wedge \beta$.** Když $u(\varphi) = 1$, je $L_u \vdash \alpha$ i $L_u \vdash \beta$ a stačí [[zavedení konjunkce|∧i]]. Když $u(\varphi) = 0$, je třeba $u(\alpha) = 0$, tedy $L_u \vdash \neg\alpha$ (pro $u(\beta) = 0$ stejně s $\wedge$e₂):
> $$
> \begin{array}{rll} \text{k.} & \neg\alpha & \text{(ind. předp.)} \\  & \begin{array}{|rll|}\hline \text{k{+}1.} & \alpha\wedge\beta & \text{P} \\ \text{k{+}2.} & \alpha & {\wedge}\text{e}_1\ k{+}1 \\ \text{k{+}3.} & \bot & {\neg}\text{e}\ k{+}2, k \\ \hline\end{array} &  \\ \text{k{+}4.} & \neg(\alpha\wedge\beta) & {\neg}\text{i}\ k{+}1\text{–}k{+}3\end{array}
> $$
> **$\varphi = \alpha \vee \beta$.** Když $u(\varphi) = 1$, je třeba $u(\alpha) = 1$, $L_u \vdash \alpha$ a stačí [[zavedení disjunkce|∨i₁]]. Když $u(\varphi) = 0$, je $L_u \vdash \neg\alpha$ i $L_u \vdash \neg\beta$ a [[eliminace disjunkce|rozbor případů]] vede v obou větvích ke sporu:
> $$
> \begin{array}{rll} \text{k.} & \neg\alpha & \text{(ind. předp.)} \\ \text{l.} & \neg\beta & \text{(ind. předp.)} \\  & \begin{array}{|rll|}\hline \text{l{+}1.} & \alpha\vee\beta & \text{P} \\  & \begin{array}{|rll|}\hline \text{l{+}2.} & \alpha & \text{P} \\ \text{l{+}3.} & \bot & {\neg}\text{e}\ l{+}2, k \\ \hline\end{array} &  \\  & \begin{array}{|rll|}\hline \text{l{+}4.} & \beta & \text{P} \\ \text{l{+}5.} & \bot & {\neg}\text{e}\ l{+}4, l \\ \hline\end{array} &  \\ \text{l{+}6.} & \bot & {\vee}\text{e}\ l{+}1, l{+}2\text{–}l{+}3, l{+}4\text{–}l{+}5 \\ \hline\end{array} &  \\ \text{l{+}7.} & \neg(\alpha\vee\beta) & {\neg}\text{i}\ l{+}1\text{–}l{+}6\end{array}
> $$

> [!example] Příklad: $\varphi = (x \Rightarrow y) \wedge \neg z$, $u$: $x \mapsto 1$, $y \mapsto 0$, $z \mapsto 0$
> $u(x \Rightarrow y) = 0$, tedy $u(\varphi) = 0$ a $L_u = \{x, \neg y, \neg z\}$. Lemma slibuje $L_u \vdash \neg\varphi$. Odvození jde podle stavby formule: nejdřív krok pro $\Rightarrow$ (řádek $u_3$) dá $\neg(x \Rightarrow y)$, pak krok pro $\wedge$ dá $\neg\varphi$.
> $$
> \begin{array}{rll}\text{1.} & x & \text{P} \\ \text{2.} & \neg y & \text{P} \\ \text{3.} & \neg z & \text{P} \\  & \begin{array}{|rll|}\hline \text{4.} & x\Rightarrow y & \text{P} \\ \text{5.} & y & {\Rightarrow}\text{e}\ 1, 4 \\ \text{6.} & \bot & {\neg}\text{e}\ 5, 2 \\ \hline\end{array} &  \\ \text{7.} & \neg(x\Rightarrow y) & {\neg}\text{i}\ 4\text{–}6 \\  & \begin{array}{|rll|}\hline \text{8.} & (x\Rightarrow y)\wedge\neg z & \text{P} \\ \text{9.} & x\Rightarrow y & {\wedge}\text{e}_1\ 8 \\ \text{10.} & \bot & {\neg}\text{e}\ 9, 7 \\ \hline\end{array} &  \\ \text{11.} & \neg((x\Rightarrow y)\wedge\neg z) & {\neg}\text{i}\ 8\text{–}10\end{array}
> $$

Tím je lemma dokázané pro všechny formule a s ním (přes skládání řádků pomocí TND z LGR 07) [[slabá věta o úplnosti]] i [[věta o úplnosti]].

> [!navic] Která strana je lehčí
> Úplnost říká $S \vdash \varphi \iff S \models \varphi$. Pro kladnou odpověď je lehčí strana $\vdash$: stačí **najít jedno odvození**, kdežto $S \models \varphi$ chce tabulku o $2^n$ řádcích nebo rezoluční metodu, obojí v nejhorším případě exponenciálně dlouhé. Pro zápornou odpověď je lehčí strana $\models$: na $S \not\models \varphi$ stačí **jedno ohodnocení** $u$ s $u(S) = 1$ a $u(\varphi) = 0$, kdežto $S \nvdash \varphi$ by znamenalo prohledat všechna odvození.

## §2 Proč predikátová logika

> [!example] Aristotelův sylogismus · handout 5, slajdy 4–5
> *Každý člověk je smrtelný. Sokrates je člověk. Tedy Sokrates je smrtelný.*
>
> Úsudek je správný, ale ve výrokové logice to nejde ověřit: jsou to tři různé výroky $a$, $b$, $c$ a $\{a, b\} \not\models c$. Je potřeba vidět **dovnitř** výroků. S proměnnou $x$ (jsoucno), [[predikátový symbol|predikáty]] $C(x)$ „$x$ je člověk“, $S(x)$ „$x$ je smrtelný“ a [[konstantní symbol|konstantou]] $a$ (Sokrates):
> $$
> \frac{\forall x\,(C(x) \Rightarrow S(x)) \qquad C(a)}{S(a)}
> $$
> Formule pod čarou je [[sémantický důsledek|sémantickým důsledkem]] formulí nad čarou.

^sylogismus

> [!definice] Definice · handout 5, slajd 3
> **Predikátová logika** studuje kromě logických spojek i **kvantifikátory** a **vnitřní strukturu** jednoduchých výroků. Proměnné v ní neoznačují výroky, ale zastupují **objekty** (individua). V **predikátové logice 1. řádu** jsou proměnné jen pro individua, ne pro množiny individuí: všechny proměnné jsou jednoho typu.

^def-predikatova-logika

> [!lidsky] Lidsky
> Výroková logika vidí větu „Sokrates je člověk“ jako jednu nedělitelnou krabičku $a$. Predikátová logika ji rozloží na **kdo** (Sokrates, objekt) a **co o něm platí** (být člověk, predikát). „1. řád“ znamená, že smíš říct „pro každého člověka“, ale ne „pro každou vlastnost“.

> [!example] Příklad
> „Každý člověk je smrtelný“ je ve výrokové logice jen písmeno, v predikátové ∀x (C(x) ⇒ S(x)). Díky tomu z ní a z C(s) („Sokrates je člověk“) plyne S(s).

> [!navic] Sylogismy jako důkazový systém
> Aristotelových sylogismů je celkem 37 a dohromady tvoří úplný odvozovací systém predikátové logiky (dokázal to Leśniewski kolem roku 1930, Tarského škola v Polsku).

## §3 Jazyk predikátové logiky

> [!definice] Definice · handout 5, slajd 6
> **Jazyk predikátové logiky** obsahuje
> 1. **logické symboly**: proměnné (množina $\mathrm{Var}$), logické spojky $\neg, \wedge, \vee, \Rightarrow, \Leftrightarrow$ (případně $\mathrm{tt}, \mathrm{ff}, \mid, \downarrow, \oplus$), kvantifikátory $\forall$ (obecný) a $\exists$ (existenční) a symbol rovnosti $=$;
> 2. **speciální symboly**:
>    - **predikátové**, každý se svou **aritou** $n \ge 0$; jejich množina je $\mathrm{Pred}$,
>    - **funkční**, každý se svou aritou $n > 0$; jejich množina je $\mathrm{Func}$,
>    - **konstantní**; jejich množina je $\mathrm{Kons}$;
> 3. **pomocné symboly**: závorky a čárku.
>
> **Arita** symbolu je počet jeho argumentů, značí se $\mathrm{ar}(P)$.

^def-jazyk

> [!lidsky] Lidsky
> Jazyk je slovník, ze kterého smíš skládat. Logické symboly jsou pro všechny jazyky stejné, speciální si zvolíš podle toho, o čem chceš mluvit. Predikátový symbol je **vlastnost nebo vztah** ($S(x)$: „$x$ je sudé“, arita 1; $P(x, y)$: „$x < y$“, arita 2), funkční symbol **vyrábí z objektů objekt** ($f(x)$: „následník $x$“), konstantní symbol je **jméno konkrétního objektu** ($a$: „dvojka“). Arita říká, kolik věcí symbol bere.

> [!example] Příklad
> Jazyk pro přirozená čísla: predikátové symboly S (arita 1, „je sudé“) a P (arita 2, „je menší“), funkční symbol f (arita 1, „následník“) a konstantní symbol a („dvojka“). Z nich jde psát S(f(a)) nebo ∀x P(x, f(x)).

> [!navic] Poznámky ke slajdu 7
> - Proměnných se běžně bere spočetně mnoho, $\mathrm{Var} = \{x_1, x_2, \dots\}$; jazyk je pak určen jen speciálními symboly. Základní jazyk teorie přirozených čísel je třeba $\mathrm{Pred} = \{<\}$, $\mathrm{Func} = \{+, \cdot\}$, $\mathrm{Kons} = \{0, 1\}$.
> - Konstantní symboly jde brát jako funkční symboly arity 0.
> - Pracuje se s logikou **s rovností**: $=$ je logický symbol a je v každém jazyce. Bez rovnosti by se muselo předpokládat, že $\mathrm{Pred}$ je neprázdná, jinak by nešla napsat žádná formule.

## §4 Termy

> [!definice] Definice · handout 5, slajd 8
> Množina **termů** je dána pravidly:
> 1. Každá proměnná a každý konstantní symbol je term.
> 2. Je-li $f$ funkční symbol arity $n$ a $t_1, \dots, t_n$ jsou termy, je i $f(t_1, \dots, t_n)$ term.
> 3. Každý term vznikl konečným použitím pravidel 1 a 2.

^def-term

> [!lidsky] Lidsky
> Term je **jméno objektu**, včetně toho, jak objekt vznikl. V jazyce s konstantou $a$ (dvojka) a funkcí $f$ (následník) je $f(f(a))$ „následník následníka dvojky“, tedy číslo 4. Term **nic netvrdí**, nemá pravdivostní hodnotu; je to podstatné jméno, ne věta. Pravidlo 3 zaručí, že každý term je konečně dlouhý.

> [!example] Příklad
> X, a, f(a) a g(x, f(f(a))) jsou termy; S(x) term není, je to formule.

[[term|Term]] se dá nakreslit jako strom: v kořeni je poslední funkční symbol, listy jsou proměnné a konstanty. Strom termu $g(x, f(f(a)))$ je vpravo na obrázku v §6.

## §5 Formule

> [!definice] Definice · handout 5, slajd 9
> Množina **formulí** je dána pravidly:
> 1. Je-li $P$ predikátový symbol arity $n$ a $t_1, \dots, t_n$ jsou termy, je řetězec $P(t_1, \dots, t_n)$ formule, tzv. **atomická formule**. Atomická formule je i $t_1 = t_2$, kde $t_1, t_2$ jsou termy.
> 2. Jsou-li $\varphi$, $\psi$ formule, jsou formulemi i $(\neg\varphi)$, $(\varphi \wedge \psi)$, $(\varphi \vee \psi)$, $(\varphi \Rightarrow \psi)$, $(\varphi \Leftrightarrow \psi)$ (případně $\mathrm{ff}$, $\mathrm{tt}$, $(\varphi \mid \psi)$, $(\varphi \downarrow \psi)$, $(\varphi \oplus \psi)$).
> 3. Je-li $\varphi$ formule a $x$ proměnná, jsou formulemi i $(\forall x\,\varphi)$ a $(\exists x\,\varphi)$; $\forall$ a $\exists$ jsou **kvantifikátory**.
> 4. Každá formule vznikla konečným použitím pravidel 1, 2 a 3.

^def-formule-pl

> [!lidsky] Lidsky
> Atomická formule je nejjednodušší **tvrzení** o objektech: predikát s dosazenými termy, třeba $S(f(a))$ „následník dvojky je sudý“. Z atomických formulí se pak staví složitější formule spojkami (jako ve výrokové logice) a kvantifikátory: $\forall x\,\varphi$ „pro každé $x$ platí $\varphi$“, $\exists x\,\varphi$ „pro nějaké $x$ platí $\varphi$“. Atomické formule tu hrají roli, jakou měly ve výrokové logice [[logická proměnná|logické proměnné]].

> [!example] Příklad
> S(f(a)) a P(x, a) jsou atomické formule; ∀x P(x, f(x)) a ∃y (S(y) ∧ P(x, y)) jsou formule s kvantifikátory. Výraz f(S(x)) není nic: funkce dostala formuli místo termu.

> [!pozor] Term ≠ formule
> $f(a)$ je [[term]] (objekt), $S(f(a))$ je [[atomická formule|formule]] (tvrzení). Výraz $f(S(x))$ **není nic**: funkční symbol smí dostat jen termy, a $S(x)$ je formule. Stejně tak nejde $S(x) \wedge f(x)$: spojka spojuje jen formule.

### Šetření závorkami

Podle slajdu 10 se závorky vynechávají takto:
- vnější závorky kolem celé formule se nepíšou;
- negace váže silněji než ostatní spojky, takže se nepíše $(\neg\varphi)$;
- **kvantifikátory váží silněji než spojky**, takže $\forall x\,P(x, f(x)) \vee S(x)$ znamená $(\forall x\,P(x, f(x))) \vee S(x)$;
- při opakování jen $\wedge$ (nebo jen $\vee$) se vnitřní závorky nepíšou.

U symbolů pro binární vztahy a operace se smí psát infixně: $x + y$ místo $+(x, y)$, $t_1 = t_2$ místo $=(t_1, t_2)$.

> [!pozor] Kam sahá kvantifikátor
> $\forall x\,P(x) \vee S(x)$ **není** „pro každé $x$: $P(x)$ nebo $S(x)$“. Kvantifikátor váže silněji než $\vee$, takže se týká jen $P(x)$, a $x$ v $S(x)$ je s ním nesvázané. Když má kvantifikátor platit pro celou disjunkci, musí se psát závorka: $\forall x\,(P(x) \vee S(x))$.

### Syntaktický strom a podformule

> [!definice] Definice · handout 5, slajd 12
> [[syntaktický strom|Syntaktický strom]] formule predikátové logiky se tvoří jako ve výrokové logice a navíc:
> - formule $\forall x\,\alpha$ (resp. $\exists x\,\alpha$) má v kořeni $\forall x$ (resp. $\exists x$) a jediným synem je kořen stromu pro $\alpha$;
> - místo listů pro atomické formule jsou stromy, které ukazují jejich stavbu a obsahují stromy termů.
>
> **Podformule** formule $\varphi$ odpovídají podstromům, jejichž kořen neleží uvnitř stromu nějakého termu, se všemi potomky toho kořene.

^def-strom-pl

> [!lidsky] Lidsky
> Strom má teď dvě patra: nahoře „logika“ (spojky, kvantifikátory, predikáty), dole „objekty“ (stromy termů). Podformule jsou jen kousky z horního patra: $P(x, f(x))$ je podformule, ale $f(x)$ ne, to je term.

> [!example] Příklad
> Strom formule (a ∧ b) ⇒ ¬c má v kořeni ⇒, vlevo podstrom ∧ s listy a, b, vpravo podstrom ¬ s listem c. Podformule jsou a, b, c, a ∧ b, ¬c a celá formule.

## §6 Volné a vázané proměnné

> [!definice] Definice · handout 5, slajd 13
> Výskyt proměnné $x$ ve formuli $\varphi$ je **vázaný**, jestliže v syntaktickém stromu při cestě od listu s tímto $x$ ke kořeni narazíme na kvantifikátor s proměnnou $x$ ($\forall x$ nebo $\exists x$). Jinak je výskyt **volný**.
>
> Proměnná $x$ je ve formuli $\varphi$ **volná**, má-li v ní aspoň jeden volný výskyt, a **vázaná**, má-li v ní aspoň jeden vázaný výskyt.

^def-volny-vazany

> [!lidsky] Lidsky
> Vázané $x$ je „vnitřní“ proměnná kvantifikátoru, jako $i$ v $\sum_{i=1}^{n} i^2$: za $i$ nic nedosazuješ, výsledek na ní nezávisí. Volné $x$ je jako $n$ v téže sumě: hodnota formule na něm závisí a čeká, co se za něj dosadí. Volná i vázaná se týká **výskytů**; proměnná jako celek může být obojí naráz.

> [!obrazek] Syntaktický strom formule a strom termu
> ![[lgr08-stromy.png]]
> *Vlevo strom formule $\forall x\,P(x, f(x)) \vee S(x)$. Modře kvantifikátor $\forall x$ a jím vázané výskyty $x$ (cesta ke kořeni přes $\forall x$ vede), oranžově volný výskyt v $S(x)$ (cesta ke kořeni žádné $\forall x$ nepotká). Šedě podstromy termů. Vpravo strom termu $g(x, f(f(a)))$, zeleně konstanta.*

> [!example] Příklad · handout 5, slajd 13
> V $\forall x\,P(x, f(x)) \vee S(x)$ jsou oba výskyty $x$ v $P(x, f(x))$ vázané, výskyt v $S(x)$ volný. Proměnná $x$ je tedy v této formuli **[[volná proměnná|volná]] i [[vázaná proměnná|vázaná]]**.

### Legální přejmenování

> [!definice] Definice · handout 5, slajd 14
> O **legálním přejmenování** vázané proměnné $x$ v podformuli $\forall x\,\alpha$ (resp. $\exists x\,\alpha$) mluvíme, pokud
> - přejmenujeme všechny výskyty $x$ v podformuli $\alpha$ na jinou proměnnou (např. $y$) a
> - žádná volná proměnná se tím nestala vázanou (tj. $y$ neměla v $\alpha$ žádný volný výskyt).
>
> Legálním přejmenováním jde získat formuli s **čistými proměnnými**: žádná proměnná v ní není volná i vázaná.

^def-legalni-prejmenovani

> [!lidsky] Lidsky
> Jméno vnitřní proměnné je jedno: $\sum_i i^2$ a $\sum_k k^2$ je totéž. Nové jméno ale nesmí být už „obsazené“ volnou proměnnou uvnitř, jinak by ji kvantifikátor nečekaně „chytil“ a změnil význam formule.

> [!example] Příklad
> - **legální přejmenování:** v ∀x P(x, f(z)) ∨ S(x) smíš vázané x přejmenovat na y: ∀y P(y, f(z)) ∨ S(x). Na z ne: ∀z P(z, f(z)) by „chytilo“ volné z a formule by znamenala něco jiného.
> - **čisté proměnné:** ∀x P(x, f(z)) ∨ S(x) čisté proměnné nemá (x je volná i vázaná), po přejmenování ∀y P(y, f(z)) ∨ S(x) už ano.

> [!definice] Definice · handout 5, slajd 15
> Formule $\varphi$ a $\psi$ predikátové logiky jsou si **rovny**, pokud se jako řetězce znaků liší nejvýš legálním přejmenováním vázaných proměnných.

^def-rovnost-formuli-pl

> [!lidsky] Lidsky
> Ve výrokové logice byly dvě formule rovné, jen když se psaly znak po znaku stejně. V predikátové logice se navíc nehledí na jména vázaných proměnných, protože ta nic neznamenají.

> [!example] Příklad · handout 5, slajd 15
> $\varphi = \forall x\,P(x, f(z)) \vee S(x)$ jde zapsat jako $\forall y\,P(y, f(z)) \vee S(x)$; druhý zápis má [[čisté proměnné]] ($y$ jen vázaná, $x$ a $z$ jen volné).
>
> Ale $\psi = \forall z\,P(z, f(z)) \vee S(x)$ je **jiná** formule, $\varphi \ne \psi$: přejmenování $x \to z$ není legální, protože $z$ měla v $P(x, f(z))$ volný výskyt a teď je vázaná.

### Sentence a otevřené formule

> [!definice] Definice · handout 5, slajd 16
> **Sentence** (uzavřená formule) je formule bez volných proměnných: každá proměnná má všechny své výskyty vázané. **Otevřená formule** je formule bez vázaných proměnných: každá proměnná má všechny své výskyty volné.

^def-sentence

> [!lidsky] Lidsky
> Sentence je hotové tvrzení, o kterém má smysl ptát se „platí to?“, jakmile víš, co znamenají symboly: „každé číslo je menší než jeho následník“. Otevřená formule je šablona s prázdnými místy: „$x$ je sudé“ platí, nebo ne podle toho, co dosadíš za $x$.

> [!example] Příklad · handout 5, slajd 16
> - $\forall x\,S(x)$ a $S(a)$ jsou sentence ($a$ je konstanta, ne proměnná).
> - $S(x)$ a $S(a)$ jsou otevřené formule. $S(a)$ je tedy obojí: nemá žádnou proměnnou.
> - $\forall x\,S(x) \vee S(y)$ není ani sentence ($y$ je volná), ani otevřená formule ($x$ je vázaná).

## §7 Interpretace a formalizace

Abychom mohli říct, jestli [[formule predikátové logiky|formule]] platí, musíme vědět, **o čem** mluví (jaké objekty se dosazují za proměnné) a co znamená každý speciální symbol. Všechno se přitom musí odehrávat v jednom „světě“.

> [!definice] Definice · handout 5, slajd 18
> **Interpretace** jazyka predikátové logiky se symboly $\mathrm{Pred}$, $\mathrm{Kons}$, $\mathrm{Func}$ je dvojice $(U, [\![-]\!])$, kde $U$ je neprázdná množina, tzv. **universum**, a $[\![-]\!]$ je přiřazení, které
> 1. každému predikátovému symbolu $P$ arity $n > 0$ přiřadí podmnožinu $[\![P]\!] \subseteq U^n$ ($n$-ární relaci) a každému $P$ arity 0 hodnotu 0 nebo 1;
> 2. každému konstantnímu symbolu $a$ přiřadí prvek $[\![a]\!] \in U$;
> 3. každému funkčnímu symbolu $f$ arity $n > 0$ přiřadí zobrazení $[\![f]\!]: U^n \to U$.

^def-interpretace

> [!lidsky] Lidsky
> Interpretace je „slovník významů“: řekne, čím jsou objekty (universum, třeba $\mathbb{N}$) a co znamená každé slovo jazyka. Vlastnost (arita 1) se interpretuje **množinou prvků, které ji mají** (sudá čísla), vztah (arita 2) **množinou dvojic, které v něm jsou** (všechny dvojice $(m, n)$ s $m < n$). Predikát arity 0 je obyčejný výrok s hodnotou 0 nebo 1, takže výroková logika je částí predikátové.

> [!pozor] Funkce musí být všude definovaná
> $[\![f]\!]$ musí být definovaná pro **všechny** $n$-tice z universa a výsledek musí **ležet v universu**. Na $U = \mathbb{N}$ proto nejde interpretovat binární symbol jako odčítání ($2 - 5 \notin \mathbb{N}$) ani jako dělení ($m / 0$ není definované).

### Příklad: přirozená čísla

> [!example] Příklad · handout 5, slajdy 21–22
> | jazyk | interpretace |
> |---|---|
> | $\mathrm{Var} = \{x, y, z\}$ | $U = \mathbb{N}$ |
> | $\mathrm{Pred} = \{S, L, P\}$, $\mathrm{ar}(S) = \mathrm{ar}(L) = 1$, $\mathrm{ar}(P) = 2$ | $[\![S]\!] = \{n \in \mathbb{N} : n \text{ je sudé}\}$, $[\![L]\!] = \{n \in \mathbb{N} : n \text{ je liché}\}$, $[\![P]\!] = \{(m, n) \in \mathbb{N}^2 : m < n\}$ |
> | $\mathrm{Func} = \{f\}$, $\mathrm{ar}(f) = 1$ | $[\![f]\!]: \mathbb{N} \to \mathbb{N}$, $n \mapsto n + 1$ |
> | $\mathrm{Kons} = \{a\}$ | $[\![a]\!] = 2$ |
>
> Zformalizované věty:
> 1. *Následník dvojky není sudé číslo:* $\neg S(f(a))$.
> 2. *Každé číslo je menší než jeho následník:* $\forall x\,P(x, f(x))$.
> 3. *Každé liché číslo je menší než nějaké sudé číslo:* $\forall x\,\big(L(x) \Rightarrow \exists y\,(S(y) \wedge P(x, y))\big)$.

> [!obrazek] Interpretace na přirozených číslech
> ![[lgr08-interpretace.png]]
> *Universum $\mathbb{N}$: zeleně čtverečky sudá čísla ($[\![S]\!]$), modře kolečka lichá ($[\![L]\!]$). Oranžově konstanta $a$ a její následník $f(a) = 3$, který je lichý, takže [[sentence]] $\neg S(f(a))$ v této interpretaci platí. Šedě funkce následník.*

### Jak formalizovat

1. **[[atomická formule|Atomické formule]]:** najdi vlastnosti a vztahy ve větě a zapiš je predikáty s termy („$x$ je liché“ $\to L(x)$, „$x$ je menší než $y$“ $\to P(x, y)$).
2. **[[kvantifikátor|Kvantifikátory]]:** „každé“ $\to \forall$, „nějaké, existuje“ $\to \exists$; ke každému patří nová proměnná.
3. **Logické spojky:** jak spolu atomické formule souvisí ($\neg$, $\wedge$, $\Rightarrow$, …).
4. **Závorky:** ohraničí, kam sahá každý kvantifikátor.

> [!pozor] ∀ jde s ⇒, ∃ jde s ∧
> „Každé liché číslo je …“ je $\forall x\,(L(x) \Rightarrow \dots)$: tvrzení se týká jen lichých. Kdyby tam bylo $\forall x\,(L(x) \wedge \dots)$, tvrdilo by to, že **každé** číslo je liché.
>
> „Nějaké sudé číslo, které …“ je $\exists y\,(S(y) \wedge \dots)$. Kdyby tam bylo $\exists y\,(S(y) \Rightarrow \dots)$, stačilo by najít libovolné **liché** $y$: pro něj je předpoklad implikace nepravdivý a celá implikace pravdivá, takže by formule nic neříkala.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \alpha \Rightarrow \beta$ v řádku, kde $u(\beta) = 1$.
> Podle indukčního předpokladu **$L_u \vdash \beta$**. Otevři box s pomocným předpokladem $\alpha$, uvnitř zopakuj $\beta$ (**it**) a box uzavři **$\Rightarrow$i**: máš $L_u \vdash \alpha \Rightarrow \beta$. Hodnota $u(\alpha)$ tu nehraje roli.

> [!karta|02]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \alpha \Rightarrow \beta$ v řádku, kde $u(\alpha) = 0$.
> Podle indukčního předpokladu **$L_u \vdash \neg\alpha$**. Box s předpokladem $\alpha$: **$\neg$e** s $\neg\alpha$ dá $\bot$, **$\bot$e** dá $\beta$. Uzavření **$\Rightarrow$i** dá $L_u \vdash \alpha \Rightarrow \beta$.

> [!karta|03]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \alpha \Rightarrow \beta$ v řádku, kde $u(\varphi) = 0$.
> Pak $u(\alpha) = 1$, $u(\beta) = 0$, tedy **$L_u \vdash \alpha$** a **$L_u \vdash \neg\beta$**. Box s předpokladem $\alpha \Rightarrow \beta$: **$\Rightarrow$e** s $\alpha$ dá $\beta$, **$\neg$e** s $\neg\beta$ dá $\bot$. Uzavření **$\neg$i** dá $L_u \vdash \neg(\alpha \Rightarrow \beta)$.

> [!karta|04]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \alpha \wedge \beta$, když $u(\varphi) = 0$.
> Některý člen je nepravdivý, např. $u(\alpha) = 0$, tedy **$L_u \vdash \neg\alpha$**. Box s předpokladem $\alpha \wedge \beta$: **$\wedge$e₁** dá $\alpha$, **$\neg$e** s $\neg\alpha$ dá $\bot$. Uzavření **$\neg$i** dá $L_u \vdash \neg(\alpha \wedge \beta)$.

> [!karta|05]- Dokaž krok lemmatu o literálech řádku pro $\varphi = \alpha \vee \beta$, když $u(\varphi) = 0$.
> Oba členy jsou nepravdivé: **$L_u \vdash \neg\alpha$**, **$L_u \vdash \neg\beta$**. Box s předpokladem $\alpha \vee \beta$ a v něm **$\vee$e**: box $\alpha$ dá $\bot$ (s $\neg\alpha$), box $\beta$ dá $\bot$ (s $\neg\beta$), tedy $\bot$. Uzavření **$\neg$i** dá $L_u \vdash \neg(\alpha \vee \beta)$.

> [!karta|06]- Proč Aristotelův sylogismus (každý člověk je smrtelný, Sokrates je člověk, tedy Sokrates je smrtelný) nejde ověřit ve výrokové logice?
> Výroková logika vidí **tři nesouvisející výroky** $a$, $b$, $c$, a $\{a, b\} \not\models c$. Správnost úsudku stojí na **vnitřní struktuře** výroků (kdo a jakou má vlastnost), a tu zachytí až predikátová logika: $\forall x\,(C(x) \Rightarrow S(x)),\ C(a) \models S(a)$.

> [!karta|07]- Čím se liší term od formule? Je $f(a)$ term, nebo formule?
> **Term** popisuje **objekt** a nemá pravdivostní hodnotu (proměnné, konstanty, $f(t_1, \dots, t_n)$). **Formule** je **tvrzení**, které platí, nebo neplatí (predikát s termy, spojky, kvantifikátory). $f(a)$ je term („následník $a$“), $S(f(a))$ je formule.

> [!karta|08]- Jak se čte $\forall x\,P(x, f(x)) \vee S(x)$ a proč?
> Jako **$(\forall x\,P(x, f(x))) \vee S(x)$**: kvantifikátory váží silněji než spojky, takže $\forall x$ se týká jen $P(x, f(x))$. Výskyt $x$ v $S(x)$ je **volný**.

> [!karta|09]- Může být jedna proměnná v téže formuli volná i vázaná? Uveď příklad.
> **Ano**: volnost i vázanost se posuzuje u **jednotlivých výskytů**. V $\forall x\,P(x, f(x)) \vee S(x)$ jsou výskyty $x$ pod $\forall x$ vázané a výskyt v $S(x)$ volný, takže $x$ je volná i vázaná. Legálním přejmenováním ($\forall y\,P(y, f(y)) \vee S(x)$) se to odstraní.

> [!karta|10]- Kdy je přejmenování vázané proměnné $x$ v $\forall x\,\alpha$ na $y$ legální a co se pokazí, když není?
> Musí se přejmenovat **všechny výskyty $x$ v $\alpha$** a **$y$ nesmí mít v $\alpha$ volný výskyt**. Jinak by kvantifikátor volné $y$ „chytil“ a formule by znamenala něco jiného: $\forall x\,P(x, f(z))$ na $\forall z\,P(z, f(z))$ přejmenovat **nejde**.

> [!karta|11]- Proč je $S(a)$ ($a$ konstanta) zároveň sentence i otevřená formule?
> Neobsahuje **žádnou proměnnou**. Nemá tedy volnou proměnnou (podmínka sentence) ani vázanou (podmínka otevřené formule) a splňuje obě definice naráz.

> [!karta|12]- Proč nejde na universu $\mathbb{N}$ interpretovat binární funkční symbol jako odčítání?
> Interpretace funkčního symbolu musí být zobrazení **$U^n \to U$**: definované pro **všechny** dvojice z $U$ a s výsledkem **v $U$**. Odčítání vede z $\mathbb{N}$ ven ($2 - 5 = -3 \notin \mathbb{N}$).

> [!karta|13]- Proč se „existuje sudé číslo, které je větší než $x$“ formalizuje $\exists y\,(S(y) \wedge P(x, y))$, a ne $\exists y\,(S(y) \Rightarrow P(x, y))$?
> S $\Rightarrow$ by stačilo najít **liché $y$**: pro něj je $S(y)$ nepravdivé a implikace **pravdivá**, ať je $P(x, y)$ jakékoli. Formule by tak platila skoro vždy a neříkala nic. **$\exists$ jde s $\wedge$.**

> [!karta|14]- Proč se „každé liché číslo má vlastnost $Q$“ formalizuje $\forall x\,(L(x) \Rightarrow Q(x))$, a ne $\forall x\,(L(x) \wedge Q(x))$?
> $\forall x\,(L(x) \wedge Q(x))$ tvrdí, že **každé** číslo je liché a má $Q$, což je jiné (a v $\mathbb{N}$ nepravdivé) tvrzení. Implikace omezí tvrzení jen na lichá čísla: **$\forall$ jde s $\Rightarrow$.**

> [!karta|15]- Jak postupovat při formalizaci české věty do predikátové logiky?
> 1. **Atomické formule**: vlastnosti a vztahy jako predikáty s termy. 2. **Kvantifikátory**: „každý“ $\forall$, „nějaký“ $\exists$, každý s vlastní proměnnou. 3. **Spojky** mezi atomickými formulemi. 4. **Závorky**, aby bylo jasné, kam sahá každý kvantifikátor.

### Příklady na procvičení

> [!priklad|16]- Pro $\varphi = (x \Rightarrow y) \wedge \neg z$ a $u$: $x \mapsto 0$, $y \mapsto 1$, $z \mapsto 0$ urči $L_u$ a odvoď z něj $\varphi$, nebo $\neg\varphi$ podle lemmatu o literálech řádku.
> $u(x \Rightarrow y) = 1$, $u(\neg z) = 1$, tedy $u(\varphi) = 1$ a $L_u = \{\neg x, y, \neg z\}$. Cíl **$L_u \vdash (x \Rightarrow y) \wedge \neg z$**:
> $$
> \begin{array}{rll}\text{1.} & \neg x & \text{P} \\ \text{2.} & y & \text{P} \\ \text{3.} & \neg z & \text{P} \\  & \begin{array}{|rll|}\hline \text{4.} & x & \text{P} \\ \text{5.} & y & \text{it}\ 2 \\ \hline\end{array} &  \\ \text{6.} & x\Rightarrow y & {\Rightarrow}\text{i}\ 4\text{–}5 \\ \text{7.} & (x\Rightarrow y)\wedge\neg z & {\wedge}\text{i}\ 6, 3\end{array}
> $$
> Implikace jde i přes $\neg x$ (box $x$: $\bot$ ¬e 4, 1; $y$ ⊥e).

> [!priklad|17]- V jazyce s $\mathrm{Pred} = \{S, P\}$ ($\mathrm{ar}(S) = 1$, $\mathrm{ar}(P) = 2$), $\mathrm{Func} = \{f\}$ ($\mathrm{ar}(f) = 1$), $\mathrm{Kons} = \{a\}$ rozhodni, co je term, co atomická formule a co ani jedno: $f(a)$, $S(f(a))$, $P(x, a)$, $f(S(x))$, $S(x, a)$.
> - $f(a)$: **term** (funkce aplikovaná na konstantu).
> - $S(f(a))$, $P(x, a)$: **atomické formule** (predikát se správným počtem termů).
> - $f(S(x))$: **ani jedno**, $f$ smí dostat jen term a $S(x)$ je formule.
> - $S(x, a)$: **ani jedno**, $S$ má aritu 1, ne 2.

> [!priklad|18]- Urči volné a vázané výskyty proměnných ve formuli $\forall x\,P(x, f(z)) \vee S(x)$. Které proměnné jsou volné a které vázané?
> Závorkování: $(\forall x\,P(x, f(z))) \vee S(x)$. Výskyt $x$ v $P(x, f(z))$ je **vázaný**, $z$ v $f(z)$ **volný** (nad ním je jen $\forall x$), $x$ v $S(x)$ **volný**. Proměnná $x$ je **volná i vázaná**, $z$ jen **volná**.

> [!priklad|19]- Jsou formule $\forall x\,P(x, f(z)) \vee S(x)$ a $\forall z\,P(z, f(z)) \vee S(x)$ rovny?
> **Ne.** Přejmenování $x \to z$ v podformuli $\forall x\,P(x, f(z))$ **není legální**: $z$ v ní má volný výskyt, který by se stal vázaným. První formule mluví o pevném $z$, druhá v $P(z, f(z))$ ne. Legální je třeba $\forall y\,P(y, f(z)) \vee S(x)$.

> [!priklad|20]- Rozhodni, zda je formule sentence, otevřená formule, obojí, nebo nic: $\forall x\,S(x) \vee S(y)$, $P(x, f(a))$, $\forall x\,\exists y\,P(x, y)$, $S(f(a))$.
> - $\forall x\,S(x) \vee S(y)$: **ani jedno** ($y$ volná, $x$ vázaná).
> - $P(x, f(a))$: **otevřená** ($x$ jen volná).
> - $\forall x\,\exists y\,P(x, y)$: **sentence** (obě proměnné vázané).
> - $S(f(a))$: **obojí** (žádná proměnná).

> [!priklad|21]- V jazyce $S$ (sudé), $L$ (liché), $P(x, y)$ ($x < y$) zformalizuj: „Každé liché číslo je menší než nějaké sudé číslo.“
> **$\forall x\,\big(L(x) \Rightarrow \exists y\,(S(y) \wedge P(x, y))\big)$.** „Každé liché“: $\forall$ s $\Rightarrow$; „nějaké sudé, které je větší“: $\exists$ s $\wedge$. Závorka za $\exists y$ obsahuje celé $S(y) \wedge P(x, y)$.

### Typové příklady na semestrální test

*Stejný typ úloh jako na 1. semestrálním testu (9. týden), kde je syntax a sémantika predikátové logiky. Každé tvrzení zdůvodni. Jazyk a interpretace jsou z příkladu v §7: $U = \mathbb{N}$, $S$ sudé, $L$ liché, $P(x, y)$ je $x < y$, $f$ následník, $a$ je 2.*

> [!priklad|22]- Zformalizuj: „Existuje sudé číslo, které je menší než každé liché číslo.“ Platí to v dané interpretaci?
> **$\exists x\,\big(S(x) \wedge \forall y\,(L(y) \Rightarrow P(x, y))\big)$.** „Existuje sudé“: $\exists$ s $\wedge$; „každé liché“: $\forall$ s $\Rightarrow$. **Platí**: za $x$ stačí vzít 0, je sudé a $0 < y$ pro každé liché $y$.

> [!priklad|23]- Zformalizuj: „Následník každého lichého čísla je sudý.“ Platí to?
> **$\forall x\,\big(L(x) \Rightarrow S(f(x))\big)$.** Následník je term $f(x)$, „je sudý“ predikát $S$ na něm. **Platí**: $n$ liché $\Rightarrow$ $n + 1$ sudé.

> [!priklad|24]- Zformalizuj: „Žádné číslo není zároveň sudé a liché.“
> **$\neg\exists x\,\big(S(x) \wedge L(x)\big)$**, ekvivalentně $\forall x\,\neg\big(S(x) \wedge L(x)\big)$ nebo $\forall x\,\big(S(x) \Rightarrow \neg L(x)\big)$. „Žádné“ je negace existence.

> [!priklad|25]- Přelož do češtiny a rozhodni, zda platí: $\exists x\,\big(L(x) \wedge P(f(a), x)\big)$.
> $f(a)$ je následník dvojky, tedy 3, a $P(f(a), x)$ je $3 < x$. Formule říká: **„Existuje liché číslo větší než 3.“** **Platí**, např. $x = 5$.

> [!priklad|26]- Urči volné proměnné ve formuli $\exists y\,P(x, y) \wedge \forall x\,\big(S(x) \vee P(y, x)\big)$ a legálním přejmenováním ji převeď na formuli s čistými proměnnými.
> V $\exists y\,P(x, y)$ je $x$ **volná**, $y$ vázaná; v $\forall x\,(S(x) \vee P(y, x))$ je $y$ **volná**, $x$ vázaná. Obě proměnné jsou tedy volné i vázané. Přejmenuj vázané na $z$ (v žádné z podformulí nemá volný výskyt, takže je to legální): **$\exists z\,P(x, z) \wedge \forall z\,\big(S(z) \vee P(y, z)\big)$**. Teď jsou $x$, $y$ jen volné a $z$ jen vázaná.

---
← [[LGR 07 – Odvozená pravidla, korektnost a úplnost|22. 10. 2026 Odvozená pravidla, korektnost a úplnost]] · [[LGR 09 – Pravdivost formulí, model a tautologie|29. 10. 2026 Pravdivost formulí, model a tautologie]] →

---
predmet: MA1
prednaska: 1
datum: 2026-09-23
zdroj: "Handout 1A (Úvod do analýzy), slajdy 10–21"
tags: [prednaska, MA1]
---

# MA1 01 – Množiny, uspořádání a přirozená čísla

*Přednáška 1 · středa 23. 9. 2026* · [[MA1 – Matematická analýza 1|MA1]] · [Handout 1A (PDF) ↗](https://math.fel.cvut.cz/en/people/velebil/files/b0b01ma1/ma1_handout01a.pdf)

Témata: `Russellův paradox` · `potenční množina` · `uspořádání` · `supremum a infimum` · `přirozená čísla` · `rekurze` · `ℕ*`

Analýza stojí na [[supremum|supremu]]: limita, integrál i reálná čísla se jím nakonec definují. Tahle přednáška ho zavádí nejdřív v jednoduchém světě podmnožin a přirozených čísel, kde se dá všechno nakreslit a spočítat na prstech.

## §0 Přehled na jedné stránce

| pojem | v $\mathcal{P}(U)$ s $\subseteq$ | v $\mathbb{N}$ s $\le$ |
|---|---|---|
| uspořádání | inkluze $A \subseteq B$ | $m \le n$ |
| nejmenší prvek | $\emptyset$ | $0$ |
| největší prvek | $U$ | neexistuje |
| $\sup M$ | $\bigcup M$ (existuje vždy) | $\max M$, jen pro konečnou neprázdnou $M$ |
| $\inf M$ | $\bigcap M$ (existuje vždy) | $\min M$ pro neprázdnou $M$ |
| oprava | není potřeba | přidat $+\infty$: $\mathbb{N}^*$ |

## §1 Co je množina: Russellův paradox

> [!definice] Russellův paradox · slajd 10
> Uvažuj „množinu všech množin, které neobsahují samy sebe“:
>
> $$
> R = \{ X \mid X \notin X \}.
> $$
>
> Kdyby $R$ byla množina, musí platit buď $R \in R$, nebo $R \notin R$:
>
> - $R \in R \;\Rightarrow\;$ $R$ splňuje podmínku $R \notin R$, spor ↯
> - $R \notin R \;\Rightarrow\;$ $R$ podmínku splňuje, tedy $R \in R$, spor ↯
>
> $R$ tedy množina není.

^def-russell

> [!lidsky] Lidsky
> Holič v obci holí právě ty, kdo se neholí sami. Holí se holič sám? Když ano, nemá; když ne, musí. Taková obec nemůže existovat.
>
> Pointa pro nás: představa množiny jako „pytle, do kterého hodíš cokoliv s danou vlastností“ nestačí. Axiomatická teorie množin proto povoluje vybírat prvky jen z už existující množiny, např. $\{X \in U \mid X \notin X\}$. My pracujeme „naivně“, ale opatrně: vždy máme v pozadí nějaké univerzum $U$.

## §2 Potenční množina a inkluze

> [!definice] Definice · slajd 10
> Pro pevnou množinu $U$ (*univerzum*) je
>
> $$
> \mathcal{P}(U) = \{ X \mid X \subseteq U \}
> $$
>
> *potenční množina* $U$, množina všech podmnožin $U$. Přitom $A \subseteq B$ znamená: pro každé $x$ platí $x \in A \Rightarrow x \in B$.

^def-potencni

> [!lidsky] Lidsky
> $\mathcal{P}(U)$ je katalog všech možných „výběrů“ z $U$. Pro $U = \{a, b, c\}$ je to 8 výběrů: nic, tři jednotlivé prvky, tři dvojice a všechno. Obecně má $n$-prvková množina $2^n$ podmnožin, protože u každého prvku se rozhoduješ ano/ne.

Příklady pro $U = \{a, b, c\}$:

- $\emptyset \subseteq \{a\}$ **platí**: implikace $x \in \emptyset \Rightarrow x \in \{a\}$ je pravdivá, protože $x \in \emptyset$ nenastane nikdy.
- $\{a, b\} \subseteq \{a, b, c\}$ **platí**: pro $x = a$ i $x = b$ je $x \in \{a, b, c\}$.
- $\{a, b, c\} \subseteq \{a, b\}$ **neplatí**: $c \in \{a, b, c\}$, ale $c \notin \{a, b\}$.

> [!navic] Proč ∅ ⊆ cokoliv
> Implikace s nepravdivým předpokladem je vždy pravdivá („nepravda ⇒ cokoliv“). Chceš-li vyvrátit $\emptyset \subseteq A$, musel bys najít prvek $\emptyset$, který v $A$ není. Žádný prvek $\emptyset$ ale nemá.

## §3 Inkluze jako uspořádání

Binární relace [[podmnožina|inkluze]] $\subseteq$ má na $\mathcal{P}(U)$ tři vlastnosti:

> [!definice] Uspořádání · slajd 11
> Relace $\preceq$ na množině $X$ je *uspořádání*, pokud je
>
> 1. **reflexivní:** $A \preceq A$ pro všechna $A \in X$,
> 2. **tranzitivní:** $A \preceq B$ a $B \preceq C$ $\Rightarrow$ $A \preceq C$,
> 3. **antisymetrická:** $A \preceq B$ a $B \preceq A$ $\Rightarrow$ $A = B$.
>
> Dvojici $(X, \preceq)$ říkáme *uspořádaná množina* (poset). $(\mathcal{P}(U), \subseteq)$ je uspořádaná množina.

^def-usporadani

> [!lidsky] Lidsky
> Uspořádání je pravidlo „kdo je pod kým“. Tři vlastnosti jsou minimum, aby se to chovalo rozumně: každý je pod sebou, řetěz „pod–pod“ dává „pod“ a dva různí nemůžou být každý pod tím druhým. Srovnej s $\le$ na číslech: $6 \le 6$; $1 \le 2$, $2 \le 3 \Rightarrow 1 \le 3$.
>
> Rozdíl oproti číslům: u množin nemusí jít porovnat každé dvě. $\{a\}$ a $\{b\}$ nejsou jedna v druhé ani naopak. Proto „částečné“ uspořádání.

> [!obrazek] Hasseův diagram $\mathcal{P}(\{a, b, c\})$
> ![[ma101-hasse.png]]
> *Čára nahoru znamená „je podmnožinou“. Modře $\{b\}$ a $\{c\}$, zeleně jejich supremum $\{b, c\}$ (nejníž položená množina nad oběma), oranžově infimum $\emptyset$ (nejvýš položená pod oběma).*

Nakreslení [[uspořádaná množina|uspořádání]] tak, že menší je níž a spojnice vedou jen mezi „sousedy“, se říká *Hasseův diagram*. Tranzitivitu nekreslíme: $\emptyset \subseteq \{a, b\}$ vyčteš z cesty přes $\{a\}$. ^def-hasse

## §4 Supremum a infimum

> [!definice] Supremum · slajd 13
> Buď $(X, \preceq)$ uspořádaná množina a $M \subseteq X$. Prvek $s \in X$ je *supremum* $M$, píšeme $s = \sup M$, pokud
>
> 1. $x \preceq s$ pro všechna $x \in M$ (tj. $s$ je [[horní odhad]] $M$),
> 2. pokud $x \preceq u$ pro všechna $x \in M$, pak $s \preceq u$ (tj. $s$ je **nejmenší** horní odhad $M$).

^def-sup

> [!lidsky] Lidsky
> Horní odhad je „strop“, pod který se vejde celá $M$. Stropů bývá hodně; supremum je ten nejnižší. Na obrázku: nad $\{b\}$ i $\{c\}$ leží $\{b, c\}$ a $\{a, b, c\}$, nižší z nich je $\{b, c\}$.
>
> Proč to analýza potřebuje: množina $\{0{,}9;\ 0{,}99;\ 0{,}999; \dots\}$ nemá největší prvek, ale nejnižší strop má: číslo $1$. Supremum je „maximum, které existuje i tam, kde maximum chybí“.

> [!definice] Infimum · slajd 14
> Zrcadlově: $d$ je *dolní odhad* $M$, pokud $d \preceq x$ pro všechna $x \in M$. *Infimum* $\inf M$ je **největší** dolní odhad.

^def-inf

> [!veta] Věta · slajd 15
> V $(\mathcal{P}(U), \subseteq)$ má **každá** kolekce $\{A_i \mid i \in I\}$ supremum i infimum:
>
> $$
> \sup_{i \in I} A_i = \bigcup_{i \in I} A_i, \qquad \inf_{i \in I} A_i = \bigcap_{i \in I} A_i.
> $$

Supremum je tedy v $\mathcal{P}(U)$ přesně sjednocení a infimum průnik. V jiných uspořádáních ale supremum se sjednocením nesouvisí (v $\mathbb{N}$ je to maximum).

> [!example] Příklady
> - $\sup(\{b\}, \{c\}) = \{b\} \cup \{c\} = \{b, c\}$
> - $\max(\{a\}, \emptyset) = \sup(\emptyset, \{a\}) = \{a\}$, protože $\emptyset \subseteq \{a\}$ a $\{a\}$ v kolekci leží
> - $\max(\{a\}, \{b\})$ **neexistuje**: ani jedna není nad tou druhou. Supremum ale existuje: $\{a, b\}$.

> [!definice] Maximum a minimum
> $\max M$ je horní odhad $M$, který **sám leží v $M$**; $\min M$ zrcadlově. Maximum je nejvýš jedno (plyne z antisymetrie).

^def-max

> [!veta] Maximum vs. supremum · slajd 13
> Existuje-li $\max M$, existuje i $\sup M$ a platí $\sup M = \max M$. Obráceně ne: supremum nemusí ležet v $M$ (viz $\{b\}, \{c\}$ výše).

> [!navic] Horní odhad nemusí existovat
> V $\mathcal{P}(U)$ je horním odhadem čehokoliv celé $U$, takže supremum existuje vždy. V $\mathbb{N}$ nemá množina sudých čísel žádný horní odhad, a proto ani supremum. To je motivace pro $\mathbb{N}^*$ v §7.

## §5 Přirozená čísla z množin

$\mathbb{N} = \{0, 1, 2, 3, \dots\}$ je nekonečná množina a na vysoké škole obsahuje i $0$ (na rozdíl od střední).

> [!definice] Von Neumannova konstrukce · slajd 17
> $$
> 0 \overset{\text{def}}{=} \emptyset, \qquad \operatorname{succ}(n) \overset{\text{def}}{=} n \cup \{n\}.
> $$
>
> Tedy $1 = \{0\}$, $2 = \{0, 1\}$, $3 = \{0, 1, 2\}$ a obecně $n = \{0, 1, \dots, n - 1\}$. *Následník* $\operatorname{succ}(n) = \{0, \dots, n\}$ odpovídá $n + 1$ (následníkem 1 je 2).

^def-prirozena

> [!obrazek] Čísla jako množiny
> ![[ma101-vonneumann.png]]
> *Každé číslo je množina všech menších čísel, takže n má přesně n prvků. Šipka succ přidá dosavadní číslo jako nový prvek.*

> [!lidsky] Lidsky
> Z ničeho ($\emptyset$) umíš postavit všechna čísla: číslo $n$ je „krabice se všemi menšími čísly“. Bonus: uspořádání dostaneš zadarmo, $m < n$ znamená prostě $m \in n$ (a $m \le n$ je $m \subseteq n$).

## §6 Sčítání a násobení rekurzí

> [!definice] Sčítání · slajd 17
> $$
> m + 0 \overset{\text{def}}{=} m \quad \text{(kotva)}, \qquad m + \operatorname{succ}(k) \overset{\text{def}}{=} \operatorname{succ}(m + k).
> $$

^def-plus

> [!example] $2 + 3$ krok za krokem
> Dolů rozvíjíš podle definice, dokud nenarazíš na kotvu, pak se vracíš nahoru:
>
> $$
> \begin{aligned}
> 2 + 3 &= 2 + \operatorname{succ}(2) = \operatorname{succ}(2 + 2) \\
> 2 + 2 &= 2 + \operatorname{succ}(1) = \operatorname{succ}(2 + 1) \\
> 2 + 1 &= 2 + \operatorname{succ}(0) = \operatorname{succ}(2 + 0) \\
> 2 + 0 &= 2
> \end{aligned}
> $$
>
> Zpátky: $2 + 1 = \operatorname{succ}(2) = 3$, $2 + 2 = \operatorname{succ}(3) = 4$, $2 + 3 = \operatorname{succ}(4) = 5$ ✓

> [!definice] Násobení · slajd 17
> $$
> m \cdot 0 \overset{\text{def}}{=} 0 \quad \text{(kotva)}, \qquad m \cdot \operatorname{succ}(k) \overset{\text{def}}{=} m \cdot k + m.
> $$

^def-krat

> [!pozor] Kotva násobení je jen m · 0 = 0
> Svádí to přidat druhou kotvu $m \cdot 1 \overset{\text{def}}{=} m$. Není potřeba, plyne z první:
>
> $$
> m \cdot 1 = m \cdot \operatorname{succ}(0) = m \cdot 0 + m = 0 + m = m.
> $$
>
> Poslední rovnost $0 + m = m$ ale **není** kotva sčítání (ta je $m + 0 = m$), dokazuje se indukcí přes $m$. Dvě kotvy nejsou chyba, jen zbytečné; u definice je čistší mít jednu.

> [!example]- Ověř: $2 \cdot 3$
> $2 \cdot 3 = 2 \cdot 2 + 2 = (2 \cdot 1 + 2) + 2 = ((2 \cdot 0 + 2) + 2) + 2 = ((0 + 2) + 2) + 2 = 6$ ✓

> [!lidsky] Lidsky
> [[rekurzivní definice|Rekurze]] je instrukce „jak spočítat úlohu pomocí o kousek menší úlohy“ plus *kotva*, kde se zastavit. Sčítat $3$ znamená třikrát „přičíst jedničku“; násobit $3$ znamená třikrát „přičíst $m$“. Stejně fungují rekurzivní funkce v programování a kotva je podmínka ukončení.

## §7 Uspořádání na ℕ a rozšíření ℕ*

Vlastnosti $(\mathbb{N}, \le)$:

- **Největší prvek neexistuje.** Kdyby $N$ byl největší, pak $N < \operatorname{succ}(N)$, spor. Proto nekonečné podmnožiny nemají [[maximum]] ani [[supremum]].
- **Nejmenší prvek je $0$**, takže $\min \mathbb{N} = \inf \mathbb{N} = 0$.
- **Každá neprázdná** $M \subseteq \mathbb{N}$ má [[minimum]] (dobré uspořádání).

> [!pozor] Minimum má jen neprázdná množina
> Tvrzení „každá $M \subseteq \mathbb{N}$ má minimum“ neplatí pro $M = \emptyset$: prázdná množina nemá žádný prvek, který by mohl být nejmenší. Správně: každá **neprázdná** $M \subseteq \mathbb{N}$.

> [!definice] Rozšířená přirozená čísla · slajd 20
> $$
> \mathbb{N}^* = \{0, 1, 2, 3, \dots\} \cup \{+\infty\}, \qquad n \le +\infty \text{ pro všechna } n.
> $$
>
> Počítání s $+\infty$:
>
> - $n + (+\infty) = (+\infty) + n = (+\infty) + (+\infty) = +\infty$,
> - $n \cdot (+\infty) = (+\infty) \cdot n = +\infty$ pro $n \neq 0$,
> - $0 \cdot (+\infty)$ a $(+\infty) \cdot 0$ **nejsou definovány**.

^def-nstar

> [!pozor] ℕ* obsahuje nulu
> Rozšiřuje se celé $\mathbb{N}$ včetně $0$, jen se přidá $+\infty$. V jiných kurzech se hvězdičkou někdy značí naopak $\mathbb{N}$ bez nuly, tak pozor na kontext.

> [!navic] Co je +∞ jako množina
> Stejně jako $3 = \{0, 1, 2\}$ je množina všech menších čísel, je $+\infty = \mathbb{N}$ množina **všech** přirozených čísel. O krok dál, $\operatorname{succ}(\mathbb{N}) = \mathbb{N} \cup \{\mathbb{N}\}$, je už celé $\mathbb{N}^*$, ne $+\infty$.

> [!veta] Suprema v ℕ* existují vždy · slajd 21
> Pro libovolnou $M \subseteq \mathbb{N}^*$:
>
> - $\sup M = 0$ pro $M = \emptyset$, $\sup M = \max M$ pro konečnou neprázdnou $M$, $\sup M = +\infty$ pro nekonečnou $M$,
> - $\inf M = \min M$ pro $M \neq \emptyset$, $\inf \emptyset = +\infty$.
>
> Hlavně: $\sup \mathbb{N} = +\infty$ v $\mathbb{N}^*$, kdežto v samotném $\mathbb{N}$ supremum neexistuje.

> [!lidsky] Lidsky
> $+\infty$ je „umělý strop“ přidaný nad všechna čísla, aby každá množina měla supremum. Není to číslo, se kterým se dá bez omezení počítat: $0 \cdot \infty$ nemá rozumnou hodnotu, protože „nic krát nekonečně mnoho“ může dopadnout jakkoliv. U limit se tomu bude říkat *neurčitý výraz*.

> [!navic] Proč sup ∅ = 0 a inf ∅ = +∞
> Každé $u \in \mathbb{N}^*$ je horní odhad prázdné množiny (podmínka „pro všechna $x \in \emptyset$“ platí vždy). Nejmenší ze všech horních odhadů je tedy nejmenší prvek celé $\mathbb{N}^*$, tj. $0$. Zrcadlově $\inf \emptyset$ je největší prvek, $+\infty$. Stejně v $\mathcal{P}(U)$: $\sup \emptyset = \emptyset$, $\inf \emptyset = U$.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jak axiomatická teorie množin obchází Russellův paradox?
> Nedovolí tvořit množinu „všech $X$ s danou vlastností“. Prvky se smí vybírat jen z už existující množiny: $\{X \in U \mid X \notin X\}$ je v pořádku.

> [!karta|02]- Proč platí $\emptyset \subseteq A$ pro každou množinu $A$?
> $\emptyset \subseteq A$ znamená $x \in \emptyset \Rightarrow x \in A$. Předpoklad $x \in \emptyset$ neplatí nikdy a implikace s nepravdivým předpokladem je pravdivá.

> [!karta|04]- Proč je inkluze $\subseteq$ jen *částečné* uspořádání?
> Ne každé dvě množiny jdou porovnat: $\{a\} \not\subseteq \{b\}$ a zároveň $\{b\} \not\subseteq \{a\}$.

> [!karta|05]- Která vlastnost uspořádání zaručuje, že maximum je nejvýš jedno?
> Antisymetrie. Jsou-li $h_1, h_2$ obě maxima, pak $h_1 \preceq h_2$ i $h_2 \preceq h_1$, tedy $h_1 = h_2$.

> [!karta|06]- Jaký je rozdíl mezi maximem a supremem?
> Maximum musí ležet v $M$, supremum ne. Supremum je nejmenší horní odhad; existuje-li maximum, je zároveň supremem.

> [!karta|07]- Čemu se rovná supremum a infimum kolekce množin v $(\mathcal{P}(U), \subseteq)$?
> $\sup = \bigcup A_i$ (sjednocení), $\inf = \bigcap A_i$ (průnik). V $\mathcal{P}(U)$ existují vždy.

> [!karta|10]- Co znamená $m < n$ a $m \le n$ pro von Neumannova přirozená čísla?
> $m < n \Leftrightarrow m \in n$ a $m \le n \Leftrightarrow m \subseteq n$.

> [!karta|12]- Jaká je kotva násobení a proč $m \cdot 1 = m$ není potřeba definovat?
> Kotva je $m \cdot 0 = 0$. Pak $m \cdot 1 = m \cdot \operatorname{succ}(0) = m \cdot 0 + m = 0 + m = m$; rovnost $0 + m = m$ se dokazuje indukcí.

> [!karta|13]- Má každá podmnožina $M \subseteq \mathbb{N}$ minimum?
> Jen **neprázdná**. $\emptyset$ minimum nemá, protože nemá žádný prvek.

> [!karta|15]- Obsahuje $\mathbb{N}^*$ nulu? Co je $+\infty$ jako množina?
> Ano, $\mathbb{N}^* = \{0, 1, 2, \dots\} \cup \{+\infty\}$. Jako množina je $+\infty = \mathbb{N}$, množina všech přirozených čísel.

> [!karta|16]- Které součiny s $+\infty$ nejsou v $\mathbb{N}^*$ definované?
> $0 \cdot (+\infty)$ a $(+\infty) \cdot 0$. Jinak $n \cdot (+\infty) = +\infty$ pro $n \neq 0$ a $n + (+\infty) = +\infty$.

> [!karta|17]- Kolik je $\sup \emptyset$ a $\inf \emptyset$ v $\mathbb{N}^*$ a proč?
> $\sup \emptyset = 0$, $\inf \emptyset = +\infty$. Každý prvek $\mathbb{N}^*$ je horním i dolním odhadem $\emptyset$, takže nejmenší horní odhad je nejmenší prvek $0$ a největší dolní odhad je největší prvek $+\infty$.

### Příklady na procvičení

> [!priklad|03]- Vypiš potenční množinu $\mathcal{P}(\{a, b\})$.
> $\{\emptyset, \{a\}, \{b\}, \{a, b\}\}$, tedy $2^2 = 4$ prvky.

> [!priklad|08]- Urči $\sup$ a $\inf$ kolekce $\{\{a, b\}, \{b, c\}\}$ v $\mathcal{P}(\{a, b, c\})$. Existuje maximum?
> $\sup = \{a, b, c\}$, $\inf = \{b\}$. Maximum ne: žádná z obou množin není nadmnožinou té druhé.

> [!priklad|09]- Jak vypadá číslo $3$ jako množina (von Neumann) a kolik má prvků?
> $3 = \{0, 1, 2\} = \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}$, tři prvky.

> [!priklad|11]- Spočti $1 + 2$ z rekurzivní definice sčítání.
> $1 + 2 = \operatorname{succ}(1 + 1) = \operatorname{succ}(\operatorname{succ}(1 + 0)) = \operatorname{succ}(\operatorname{succ}(1)) = \operatorname{succ}(2) = 3$.

> [!priklad|14]- Má množina sudých čísel supremum v $\mathbb{N}$? A v $\mathbb{N}^*$?
> V $\mathbb{N}$ ne, nemá žádný horní odhad. V $\mathbb{N}^*$ ano: $+\infty$.

---
[[MA1 02 – Celá, racionální a reálná čísla|24. 9. 2026 Celá, racionální a reálná čísla]] →

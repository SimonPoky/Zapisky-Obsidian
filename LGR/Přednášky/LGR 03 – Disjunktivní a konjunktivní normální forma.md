---
predmet: LGR
prednaska: 3
datum: 2026-10-01
zdroj: "Prezentace 2 (Booleovské funkce, normální formy), slajdy 12–18"
tags: [prednaska, LGR]
---

# LGR 03 – Disjunktivní a konjunktivní normální forma

*Přednáška 3 · čtvrtek 1. 10. 2026* · [[LGR – Logika a grafy|LGR]] · [Prezentace 2 (PDF) ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_2.pdf) · [Verze k tisku ↗](https://math.fel.cvut.cz/en/people/gollova/lgr/lgr_2a.pdf)

Témata: `literál` · `minterm, maxterm` · `DNF` · `CNF` · `ekvivalentní úpravy` · `tabulka pravdivostních hodnot` · `úplná DNF/CNF`

Minule se ukázalo, že $\{\neg, \wedge, \vee\}$ je [[úplný systém logických spojek]]. Dnes z toho plyne víc: každou formuli jde přepsat do jednotného „učesaného“ tvaru, buď jako „nebo“ několika „a“ (DNF), nebo jako „a“ několika „nebo“ (CNF). Ukážeme si dva způsoby, jak takový tvar najít: úpravami a z tabulky.

## §0 Přehled na jedné stránce

| pojem | co to je | příklad |
|---|---|---|
| [[literál]] | proměnná nebo její negace | $a$, $\neg b$ |
| [[minterm]] | konjunkce literálů, jeden literál, nebo $\mathrm{tt}$ | $a \wedge \neg b \wedge c$ |
| [[maxterm]] (klauzule) | disjunkce literálů, jeden literál, nebo $\mathrm{ff}$ | $a \vee \neg b \vee c$ |
| [[disjunktivní normální forma\|DNF]] | disjunkce mintermů | $(a \wedge \neg b \wedge c) \vee (a \wedge b)$ |
| [[konjunktivní normální forma\|CNF]] | konjunkce maxtermů | $(a \vee \neg b \vee c) \wedge a$ |
| [[úplná normální forma\|úplná DNF/CNF]] | každý term obsahuje všechny proměnné | z tabulky pravdivostních hodnot |

Jak hledat: **(1)** ekvivalentní úpravy, **(2)** tabulka pravdivostních hodnot.

## §1 Literál, minterm, maxterm

> [!definice] Literál, minterm, maxterm · slajd 12
> - *Literál* je atomická formule ([[logická proměnná]]) nebo její negace: $a$ (pozitivní), $\neg a$ (negativní).
> - *Minterm* je konjunkce literálů, nebo jeden literál, nebo $\mathrm{tt}$.
> - *Maxterm* (též *klauzule*) je disjunkce literálů, nebo jeden literál, nebo $\mathrm{ff}$.

^def-literal

> [!lidsky] Lidsky
> Literál je nejmenší cihlička: „prší“ nebo „neprší“. Minterm je seznam podmínek, které musí platit **všechny** naráz ($\wedge$), např. „prší a nemám deštník“. Maxterm stačí splnit **aspoň jednou** ($\vee$), např. „mám deštník nebo bundu nebo zůstanu doma“.

> [!example] Příklad
> - **literál:** a, ¬a, b a ¬c jsou literály; ¬¬a ani a ∧ b ne.
> - **maxterm:** a ∨ ¬b ∨ c je úplný maxterm pro proměnné a, b, c; nepravdivý je jen pro a = 0, b = 1, c = 0.
> - **minterm:** a ∧ ¬b ∧ c je úplný minterm; pravdivý je jen pro a = 1, b = 0, c = 1.

> [!pozor] Častá chyba: minterm vs. maxterm
> **Min**term je konjunkce ($\wedge$), **max**term disjunkce ($\vee$). Pomůcka: minterm je pravdivý v co **nejméně** řádcích tabulky (úplný minterm v jediném), maxterm v co **nejvíce** (úplný maxterm ve všech kromě jednoho).

## §2 DNF a CNF

> [!definice] Normální formy · slajd 13
> - Formule je v *disjunktivní normální formě (DNF)*, je-li disjunkcí mintermů, nebo jedním mintermem, nebo $\mathrm{ff}$.
> - Formule je v *konjunktivní normální formě (CNF)*, je-li konjunkcí maxtermů, nebo jedním maxtermem, nebo $\mathrm{tt}$.

^def-nf

> [!lidsky] Lidsky
> DNF: „platí tahle skupina podmínek, **nebo** tahle, **nebo** tahle“. CNF: „musí platit tohle pravidlo **a** tohle **a** tohle“, kde každé pravidlo je nějaké „nebo“. Uvnitř nejsou žádné $\Rightarrow$, $\Leftrightarrow$ a negace stojí jen přímo u proměnných.

> [!example] Která forma to je?
> - $(a \wedge \neg b \wedge c) \vee (a \wedge b)$ je **DNF** (dva mintermy).
> - $(a \vee \neg b \vee c) \wedge a$ je **CNF** (dva maxtermy, $a$ je maxterm z jednoho literálu).
> - $(a \vee \neg b) \wedge (a \vee b \vee c) \wedge a$ je **CNF**.
> - $a \vee c$ je **obojí**: jako CNF jeden maxterm, jako DNF dva mintermy $a$ a $c$. Stejně $a \wedge b$.
> - $\neg(a \wedge b)$ není ani jedno: negace stojí před závorkou.

> [!veta] Věta · slajd 14
> ==Ke každé formuli $\varphi$== **existují formule $\varphi_{DNF}$ v DNF a $\varphi_{CNF}$ v CNF takové, že $\varphi \mathrel{\vert\!=\!\vert} \varphi_{DNF}$ a $\varphi \mathrel{\vert\!=\!\vert} \varphi_{CNF}$.** Nejsou určené jednoznačně.

^veta-nf

> [!lidsky] Lidsky
> Ať je formule jakkoli zamotaná, vždy ji jde „učesat“ do DNF i do CNF a význam (sloupec tabulky) se nezmění. Ekvivalentně: pro každou [[booleovská funkce|booleovskou funkci]] existuje formule v DNF i v CNF. Učesaných tvarů je ale víc, např. $a \vee c$ i $(a \wedge \neg c) \vee c$ jsou DNF téže formule.

## §3 Způsob 1: ekvivalentní úpravy

Postup (slajd 16), každý krok zachovává [[tautologická ekvivalence|tautologickou ekvivalenci]]:

1. Přepsat všechny spojky pomocí $\neg, \wedge, \vee$ (hlavně $\alpha \Rightarrow \beta \mathrel{\vert\!=\!\vert} \neg\alpha \vee \beta$).
2. Dostat negace až k proměnným (De Morgan, dvojitá negace).
3. Upravit pořadí $\wedge$ a $\vee$ distributivními zákony: pro DNF „roznásobit“ $\wedge$ přes $\vee$, pro CNF naopak.
4. Zjednodušit (absorpce, slučování, $\alpha \vee \neg\alpha \mathrel{\vert\!=\!\vert} \mathrm{tt}$, $\alpha \wedge \neg\alpha \mathrel{\vert\!=\!\vert} \mathrm{ff}$).
5. Výsledek je $\varphi_{DNF}$ nebo $\varphi_{CNF}$.

> [!definice] Pravidla pro zjednodušení
> - *Absorpce:* $\alpha \vee (\beta \wedge \alpha) \mathrel{\vert\!=\!\vert} \alpha$, $\quad \alpha \wedge (\beta \vee \alpha) \mathrel{\vert\!=\!\vert} \alpha$.
> - *Slučování:* $(\alpha \vee x) \wedge (\alpha \vee \neg x) \mathrel{\vert\!=\!\vert} \alpha$, $\quad (\alpha \wedge x) \vee (\alpha \wedge \neg x) \mathrel{\vert\!=\!\vert} \alpha$.

^def-zjednoduseni

> [!lidsky] Lidsky
> Absorpce: „mám hlad, nebo (mám hlad a žízeň)“ je prostě „mám hlad“. Druhý člen nic nepřidá. Slučování: „vezmu si bundu, ať prší, nebo neprší“ je prostě „vezmu si bundu“: na $x$ nezáleží. Příklad absorpce: $(a \wedge c) \vee (a \wedge c \wedge b) \mathrel{\vert\!=\!\vert} a \wedge c$.

> [!example] $\varphi = (a \Rightarrow c) \Rightarrow \big((a \Rightarrow b) \Rightarrow c\big)$
> **Krok 1 a 2 (implikace pryč, negace k proměnným):**
>
> $$
> \varphi \mathrel{\vert\!=\!\vert} \neg(\neg a \vee c) \vee \big(\neg(\neg a \vee b) \vee c\big) \mathrel{\vert\!=\!\vert} (a \wedge \neg c) \vee (a \wedge \neg b) \vee c
> $$
>
> To už je **DNF** (tři mintermy).
>
> **Převod na CNF:** vytknout $a$ a roznásobit $\vee c$:
>
> $$
> \big(a \wedge (\neg c \vee \neg b)\big) \vee c \mathrel{\vert\!=\!\vert} (a \vee c) \wedge (\neg c \vee \neg b \vee c) \mathrel{\vert\!=\!\vert} (a \vee c) \wedge \mathrm{tt} \mathrel{\vert\!=\!\vert} a \vee c
> $$
>
> $a \vee c$ je CNF (jeden maxterm) a zároveň DNF.
>
> **Kontrola:** $\varphi$ je nepravdivá, jen když závěr $(a \Rightarrow b) \Rightarrow c$ je $0$ a předpoklad $a \Rightarrow c$ je $1$, tedy $c = 0$, a pak $a = 0$. To je přesně jediný nepravdivý případ $a \vee c$ ✓ (2 z 8 ohodnocení, $b$ libovolné).

^priklad-upravy

> [!pozor] Distributivita pro CNF
> Pro CNF se roznásobuje $\vee$ přes $\wedge$: $\alpha \vee (\beta \wedge \gamma) \mathrel{\vert\!=\!\vert} (\alpha \vee \beta) \wedge (\alpha \vee \gamma)$. Tohle „násobení“ ze školy neznáš (u čísel neplatí $x + yz = (x + y)(x + z)$), ale v logice platí.

## §4 Způsob 2: tabulka pravdivostních hodnot

Postup (slajdy 17–18):

- **DNF:** pro každý řádek s hodnotou $1$ napiš minterm, který je pravdivý **jen v tom řádku**: proměnná s hodnotou $1$ jako $a$, s hodnotou $0$ jako $\neg a$. Mintermy spoj $\vee$.
- **CNF:** pro každý řádek s hodnotou $0$ napiš maxterm, který je nepravdivý **jen v tom řádku**: proměnná s hodnotou $1$ jako $\neg a$, s hodnotou $0$ jako $a$ (negace mintermu toho řádku přes De Morgana). Maxtermy spoj $\wedge$.

> [!obrazek] DNF a CNF z tabulky pro $a \Leftrightarrow b$
> ![[lgr03-tabulka.png]]
> *Zeleně řádky s hodnotou 1 a jejich mintermy (vznikne DNF), červeně řádky s hodnotou 0 a jejich maxtermy (vznikne CNF). Oranžově vstupní proměnné, modře výsledné formule.*

> [!lidsky] Lidsky
> DNF vyjmenovává, **kdy to platí**: „buď obě nepravdivé, nebo obě pravdivé“. CNF vyjmenovává zákazy, **kdy to neplatí**: „nesmí být $a = 0, b = 1$ a nesmí být $a = 1, b = 0$“. Maxterm $a \vee \neg b$ přesně zakazuje řádek $a = 0, b = 1$.

> [!pozor] Častá chyba: znaménka v maxtermu
> V maxtermu jsou literály **opačně** než hodnoty v řádku. Řádek $a = 1, b = 0$ dá maxterm $\neg a \vee b$, ne $a \vee \neg b$. Kontrola: dosaď řádek, maxterm musí vyjít $0$.

> [!definice] Úplná DNF a CNF · slajd 18
> DNF (CNF) je *úplná*, když každý její minterm (maxterm) obsahuje všechny proměnné formule. Přesně takovou dá metoda tabulky. Formule $\mathrm{tt}$ nemá úplnou CNF a $\mathrm{ff}$ nemá úplnou DNF.

^def-uplna

> [!lidsky] Lidsky
> Úplná forma je „hrubá síla“: jeden term za každý vybraný řádek tabulky. Je dlouhá, ale jde ji sestavit vždy mechanicky. $\mathrm{tt}$ nemá žádný řádek s $0$, takže není z čeho postavit maxterm (a $\mathrm{ff}$ naopak).

> [!example] Příklad
> A ⇒ b je nepravdivá jen pro ab = 10, takže úplná CNF je jediný maxterm ¬a ∨ b. Úplná DNF má minterm za každý řádek s 1: (¬a ∧ ¬b) ∨ (¬a ∧ b) ∨ (a ∧ b).

> [!navic] Kterou metodu kdy
> Pro $n$ proměnných má tabulka $2^n$ řádků (pro $n = 5$ už 32), takže tabulka se hodí do 3–4 proměnných. Úpravy bývají kratší a dají jednodušší tvar. DNF z tabulky má tolik mintermů, kolik je jedniček; když je jedniček víc než polovina, je CNF kratší.

## Kartičky

*Oranžové kartičky (pojmy a teorie) jsou v aplikaci [[Archiv přednášek#Kartičky|Kartičky]] povinné k dennímu opakování, pojmy z této přednášky taky. Zelené příklady jsou tam jen na procvičení. Nejdřív odpověz nahlas nebo na papír, pak rozklikni.*

> [!karta|01]- Jaký je rozdíl mezi mintermem a maxtermem?
> **Minterm** je konjunkce literálů (nebo literál, nebo $\mathrm{tt}$), **maxterm** disjunkce literálů (nebo literál, nebo $\mathrm{ff}$).

> [!karta|03]- Jaké jsou kroky převodu na DNF/CNF ekvivalentními úpravami?
> 1. spojky přepsat na $\neg, \wedge, \vee$
> 2. negace k proměnným (De Morgan)
> 3. pořadí $\wedge$, $\vee$ distributivitou
> 4. zjednodušit (absorpce, slučování)

> [!karta|06]- Jak z tabulky získáš DNF?
> Pro každý řádek s **1** minterm: proměnná s hodnotou 1 jako $a$, s hodnotou 0 jako $\neg a$. Mintermy spojíš $\vee$.

> [!karta|07]- Jak z tabulky získáš CNF?
> Pro každý řádek s **0** maxterm s **opačnými** literály: hodnota 1 → $\neg a$, hodnota 0 → $a$. Maxtermy spojíš $\wedge$.

> [!karta|08]- Proč $\mathrm{tt}$ nemá úplnou CNF?
> Úplná CNF má jeden maxterm za každý řádek s **0** a $\mathrm{tt}$ žádný takový řádek nemá.

> [!karta|09]- Jak zní distributivní zákon potřebný pro převod na CNF?
> $\alpha \vee (\beta \wedge \gamma) \mathrel{\vert\!=\!\vert} (\alpha \vee \beta) \wedge (\alpha \vee \gamma)$.

> [!karta|10]- Může být formule zároveň v DNF i v CNF?
> **Ano**, např. $a \vee c$ (jeden maxterm, nebo dva mintermy) nebo $a \wedge b$ nebo jediný literál.

> [!karta|16]- Proč DNF získaná z tabulky (mintermy řádků s 1) opravdu určuje danou funkci?
> Minterm řádku je pravdivý **právě v tom jednom řádku** (každý literál sedí jen na jeho hodnoty). Disjunkce mintermů je proto pravdivá přesně v řádcích s 1 a má stejný sloupec jako zadaná funkce.

### Příklady na procvičení

> [!priklad|11]- Najdi DNF a CNF formule $a \Leftrightarrow b$ z tabulky.
> DNF: $(\neg a \wedge \neg b) \vee (a \wedge b)$. CNF: $(a \vee \neg b) \wedge (\neg a \vee b)$.

> [!priklad|12]- Převeď $(a \Rightarrow c) \Rightarrow ((a \Rightarrow b) \Rightarrow c)$ na DNF a CNF.
> DNF: $(a \wedge \neg c) \vee (a \wedge \neg b) \vee c$. Zjednodušeno: **$a \vee c$**, což je CNF i DNF.

> [!priklad|13]- Zjednoduš $(a \wedge c) \vee (a \wedge c \wedge b)$.
> Absorpce: **$a \wedge c$**.

> [!priklad|14]- Je $\neg(a \wedge b)$ v DNF nebo CNF? Pokud ne, převeď ji.
> Není (negace před závorkou). De Morgan: **$\neg a \vee \neg b$**, což je CNF (jeden maxterm) i DNF.

> [!priklad|15]- Jaký maxterm odpovídá řádku $a = 1, b = 0, c = 1$ s hodnotou 0?
> **$\neg a \vee b \vee \neg c$** (dosazením vyjde $0 \vee 0 \vee 0 = 0$).

---
← [[LGR 02 – Tautologická ekvivalence a úplné systémy spojek|25. 9. 2026 Tautologická ekvivalence a úplné systémy spojek]] · [[LGR 04 – Sémantický důsledek a klauzální tvar|8. 10. 2026 Sémantický důsledek a klauzální tvar]] →

---
aliases: ["lokální předpoklad", "pomocného předpokladu", "box", "globální předpoklad"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 6
zdroj: "slajd 9 (prez. 4)"
---

# pomocný předpoklad

> [!lidsky] Lidsky
> „Co kdyby“ v důkazu: na chvíli předpokládáš něco, co nemáš dokázané, a vyznačíš to rámečkem (boxem). Uvnitř s tím smíš pracovat, ven smí jen výsledek, který předpoklad „spotřebuje“, třeba implikace.
>
> *Příklad:* v odvození ⊢ a ⇒ a je a pomocný předpoklad: box 1. a (P); po uzavření 2. a ⇒ a (⇒i 1–1). Mimo box se samotné a použít nesmí, venku zbude jen a ⇒ a.

> [!obrazek] Boxy v odvozeních
> ![[lgr06-boxy.png]]
> *Červeně globální předpoklad, oranžově rámečky boxů a jejich lokální předpoklady, modře odvozené řádky, zeleně výsledek. Vnořený box se uzavře dřív než vnější.*

**Formálně:** pomocný předpoklad otevírá box; formule z boxu se smějí použít jen v něm a v boxech vnořených; box uzavře pravidlo (⇒i, ¬i, ∨e), pak je pasivní; odvození je hotové, až jsou všechny boxy uzavřené; globální předpoklady (formule z S) platí všude

**Definice:** [[LGR 06 – Rezoluční tabulka a přirozená dedukce#^def-pomocny|přednáška 6, 15. 10. 2026]] · slajd 9

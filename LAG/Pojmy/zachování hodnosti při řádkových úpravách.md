---
aliases: ["důsledek 8.17", "řádkové úpravy zachovávají hodnost", "ERÚ zachovávají hodnost"]
tags: [pojem, LAG]
predmet: LAG
prednaska: 13
zdroj: "důsledek 8.17"
---

# zachování hodnosti při řádkových úpravách

> [!lidsky] Lidsky
> Řádkové úpravy změní obal sloupců (obraz), ale ne jeho dimenzi. Hodnost proto smíš počítat až po eliminaci.
>
> *Příklad:* (1 2; 2 4) ~ (1 2; 0 0): obraz se změní ze span{(1; 2)} na span{(1; 0)}, hodnost zůstane 1.

**Formálně:** Vznikne-li B ∈ 𝔽^{m×n} z A sledem elementárních řádkových úprav, pak rank B = rank A (protože B = TA s regulární T a prosté zobrazení zachová dimenzi im A)

**Definice:** [[LAG 13 – Inverzní matice eliminací, transpozice a grupy#^dusledek-hodnost-uprav|přednáška 13, 6. 11. 2026]] · důsledek 8.17

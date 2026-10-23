---
aliases: ["legální přejmenování vázané proměnné", "přejmenování vázaných proměnných"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 14"
---

# legální přejmenování

> [!lidsky] Lidsky
> Změna jména vázané proměnné, která nemění význam: jako přepsat ∑ᵢ i² na ∑ₖ k². Nové jméno nesmí být volné uvnitř, jinak by ho kvantifikátor „chytil“.
>
> *Příklad:* v ∀x P(x, f(z)) ∨ S(x) smíš vázané x přejmenovat na y: ∀y P(y, f(z)) ∨ S(x). Na z ne: ∀z P(z, f(z)) by „chytilo“ volné z a formule by znamenala něco jiného.

**Formálně:** v ∀x α (∃x α) přejmenuj všechny výskyty x v α na y, přičemž y nemá v α volný výskyt (žádná volná proměnná se nestane vázanou)

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-legalni-prejmenovani|přednáška 8, 23. 10. 2026]] · handout 5, slajd 14

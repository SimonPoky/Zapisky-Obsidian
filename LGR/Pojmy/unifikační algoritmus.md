---
aliases: ["unifikace", "unifikačního algoritmu", "unifikačním algoritmem", "unifikovat"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajdy 27–29"
---

# unifikační algoritmus

> [!lidsky] Lidsky
> Přiloží dvě atomické formule k sobě a čte zleva. Na prvním rozdílu přepíše proměnnou na term z druhé strany (pokud ho proměnná sama neobsahuje), provede to na obou zbytcích a pokračuje. Dva různé neproměnné symboly znamenají NELZE.
>
> *Příklad:* T(x, y, x) a T(a, f(z), z): x := a, y := f(z), z := a, obě se stanou T(a, f(a), a). S(f(a)) a S(f(b)): rozdíl a proti b, NELZE.

**Formálně:** vstup: atomy L₁, L₂ se stejným predikátem a různými proměnnými; na rozdílu: žádná proměnná ⇒ NELZE; proměnná x proti termu obsahujícímu x ⇒ NELZE; jinak x := term, přidat do ϑ, provést na oba zbytky; výstup: maximální unifikátor ϑ, nebo NELZE

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-unifikace|přednáška 12, 12. 11. 2026]] · handout 7, slajdy 27–29

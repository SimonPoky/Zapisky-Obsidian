---
aliases: ["spojitost zleva", "spojitost zprava", "spojitá zleva", "spojitá zprava", "jednostranně spojitá"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 6
zdroj: "handout 3A, slajd 3"
---

# jednostranná spojitost

> [!lidsky] Lidsky
> Spojitost, při které se díváš jen z jedné strany: limita zleva (nebo zprava) v p se rovná f(p). Funkce je spojitá v p, právě když je tam spojitá zleva i zprava.
>
> *Příklad:* f(x) = 0 pro x < 1 a f(x) = 1 pro x ≥ 1 je v bodě 1 spojitá zprava (lim_{x→1⁺} f = 1 = f(1)), ale zleva ne (lim_{x→1⁻} f = 0).

> [!obrazek] Skok, který je spojitý zprava
> ![[ma106-zprava.png]]
> *Modře funkce $f(x) = 0$ pro $x < 1$ a $f(x) = 1$ pro $x \ge 1$. Zelený plný bod je hodnota $f(1) = 1$, prázdný kroužek hodnota, kterou funkce nenabude. Zelená šipka: zprava se hodnoty blíží k $1 = f(1)$, funkce je spojitá zprava. Červená šipka: zleva se blíží k $0 \neq f(1)$, spojitá zleva ani v bodě $1$ není.*

**Formálně:** f definovaná v p a ve směru x → p⁻: f spojitá zleva v p ⇔ lim_{x→p⁻} f(x) = f(p); zprava obdobně s x → p⁺

**Definice:** [[MA1 06 – Spojitost a spojité funkce na intervalu#^def-jednostranna-spojitost|přednáška 6, 8. 10. 2026]] · handout 3A, slajd 3 · spojitost ⇔ zleva i zprava: [[MA1 06 – Spojitost a spojité funkce na intervalu#^tvrzeni-jednostranna-spojitost|tvrzení, slajd 3]]

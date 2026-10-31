---
aliases: ["substituce", "substituci", "substituce v limitě", "věty o substituci", "limita složené funkce"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 5
zdroj: "handout 2B, slajd 19"
---

# věta o substituci

> [!lidsky] Lidsky
> Limita složené funkce f(φ(x)): když f má limitu L a vnitřní φ míří do cíle tak, že na celém kusu směru do cíle samotného nedopadne, má f ∘ φ limitu L taky. Bez té podmínky to neplatí (f = 200 v bodě 1, jinak 3, a φ ≡ 1).

> [!obrazek] Důkaz obrázkem: řetěz U → T → P
> ![[ma105-substituce.png]]
> *Vlevo kus P směru 𝒮, uprostřed kus T směru 𝒯 (prázdné kolečko je cíl, do T nepatří), vpravo modrý terč U kolem L. Hledá se pozpátku: soupeř zvolí U, limita f dá T, podmínka (2) dá P. Šipka φ pošle P dovnitř T a šipka f pošle T do zeleného f[T] ⊆ U.*

> [!obrazek] Protipříklad obrázkem
> ![[ma105-protipriklad.png]]
> *Vlevo graf f: modrá vodorovná čára ve výšce 3 s dírou v bodě 1, červený bod f(1) = 200 (svislá osa je zkrácená). Vpravo brambory: celé P kolem 5 se zobrazí do jediného bodu 1, který je přesně díra v T. Odtud f pošle všechno na červenou hodnotu 200, mimo modrý terč kolem 3.*

**Formálně:** lim𝒯 f = L ∧ (∀T ∈ 𝒯)(∃P ∈ 𝒮)(φ[P] ⊆ T) ⇒ lim𝒮 (f ∘ φ) = L

**Definice:** [[MA1 05 – Aritmetika limit a substituce#^veta-substituce|přednáška 5, 7. 10. 2026]] · handout 2B, slajd 19

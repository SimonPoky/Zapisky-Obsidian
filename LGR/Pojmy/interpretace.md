---
aliases: ["interpretace jazyka", "interpretaci"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 8
zdroj: "handout 5, slajd 18"
---

# interpretace

> [!lidsky] Lidsky
> Slovník významů: řekne, čím jsou objekty (universum) a co znamená každý speciální symbol. Vlastnost je množina prvků, které ji mají; vztah množina dvojic, které v něm jsou.
>
> *Příklad:* jazyk se symboly S (arita 1), f (arita 1), a: U = ℕ, ⟦S⟧ = sudá čísla, ⟦f⟧(n) = n + 1, ⟦a⟧ = 2. Pak S(f(a)) mluví o čísle 3 a je nepravdivá. V interpretaci s ⟦a⟧ = 1 by tatáž formule byla pravdivá.

> [!obrazek] Interpretace na přirozených číslech
> ![[lgr08-interpretace.png]]
> *Universum $\mathbb{N}$: zeleně čtverečky sudá čísla ($[\![S]\!]$), modře kolečka lichá ($[\![L]\!]$). Oranžově konstanta $a$ a její následník $f(a) = 3$, který je lichý, takže [[sentence]] $\neg S(f(a))$ v této interpretaci platí. Šedě funkce následník.*

**Formálně:** (U, ⟦−⟧), U ≠ ∅; P ∈ Pred arity n > 0 ↦ ⟦P⟧ ⊆ Uⁿ, arity 0 ↦ 0 nebo 1; a ∈ Kons ↦ ⟦a⟧ ∈ U; f ∈ Func arity n ↦ ⟦f⟧: Uⁿ → U (všude definovaná, hodnoty v U)

**Definice:** [[LGR 08 – Dokončení úplnosti a syntaxe predikátové logiky#^def-interpretace|přednáška 8, 23. 10. 2026]] · handout 5, slajd 18

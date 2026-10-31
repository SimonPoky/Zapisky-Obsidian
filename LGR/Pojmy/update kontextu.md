---
aliases: ["update", "updatu", "updaty", "ρ[x:=d]"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 9
zdroj: "handout 5, slajd 23"
---

# update kontextu

> [!lidsky] Lidsky
> Oprava jednoho řádku tabulky dosazení: proměnná x dostane novou hodnotu d, ostatní zůstanou. Jako přiřazení x = d v programu.
>
> *Příklad:* ρ: x ↦ 7, y ↦ 15, z ↦ 3. Update ρ[x:=0] je x ↦ 0, y ↦ 15, z ↦ 3. Původní ρ se nezmění, update je nový kontext.

> [!obrazek] Kontext a jeho update
> ![[lgr09-kontext.png]]
> *Modře kontext $\rho$ (každá proměnná dostane číslo z ℕ), oranžově jediná změna v updatu $\rho[x:=0]$; tečkované šipky ukazují hodnoty, které se převzaly beze změny.*

**Formálně:** Buď ρ : Var → U kontext, x ∈ Var, d ∈ U. Update ρ[x:=d] : Var → U je kontext s ρ[x:=d](x) = d a ρ[x:=d](y) = ρ(y) pro všechna y ≠ x.

**Definice:** [[LGR 09 – Pravdivost formulí, model a tautologie#^def-kontext|přednáška 9, 29. 10. 2026]] · handout 5, slajd 23

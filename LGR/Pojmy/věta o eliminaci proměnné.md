---
aliases: ["eliminace proměnné", "S₀ ∪ Rₓ", "eliminaci proměnné"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 5
zdroj: "slajdy 21–22"
---

# věta o eliminaci proměnné

> [!lidsky] Lidsky
> Když k množině přidáš všechny rezolventy přes x, smíš klauzule s x zahodit a splnitelnost se nezmění. Svědka pro původní množinu dostaneš dodáním x: buď x = 0, nebo x = 1 vyjde.
>
> *Příklad:* S = {a ∨ b, ¬a ∨ c}: rezolventa přes a je b ∨ c, takže S je splnitelná, právě když {b ∨ c} je. Svědek u(b) = 1, u(c) = 0 se doplní volbou u(a) = 0, a pak platí a ∨ b i ¬a ∨ c.

> [!obrazek] Rozklad S a eliminace proměnné x
> ![[lgr05-rozklad.png]]
> *Modře $S_x$, červeně $S_{\neg x}$, oranžově $S_0$. Vpravo zeleně nová množina $S_0 \cup R_x$: proměnná $x$ v ní už není.*

> [!obrazek] Proč nemůžou selhat oba svědci
> ![[lgr05-svedci.png]]
> *Situace 4 z důkazu: $u_0$ pokazí klauzuli $x \vee \gamma$, $u_1$ pokazí $\neg x \vee \delta$ (červeně). Pak jsou $\gamma$ i $\delta$ nepravdivé v obou, jenže jejich rezolventa $\gamma \vee \delta$ leží v $R_x$ a musí být pravdivá (zeleně).*

**Formálně:** A konečná, S množina klauzulí nad A v základním tvaru, x ∈ A: S splnitelná ⟺ S₀ ∪ Rₓ splnitelná (S₀ bez x, Rₓ = rezolventy přes x bez tautologií)

**Definice:** [[LGR 05 – Rezoluční princip#^veta-eliminace|přednáška 5, 9. 10. 2026]] · slajdy 21–22

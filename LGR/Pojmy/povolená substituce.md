---
aliases: ["povolené substituce", "povolenou substituci", "povolených substitucí", "α(x := t)", "α(ϑ)"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 12
zdroj: "handout 7, slajdy 24–25"
---

# povolená substituce

> [!lidsky] Lidsky
> Dosazení termu za proměnnou, které rezoluce smí použít: obecné tvrzení smíš zúžit na konkrétní prvky, opačně ne. Zakázané x := f(x) by důsledek dalo taky, vadí jen unifikaci (x = f(x) nejde srovnat). Dosazuje se jen za proměnné, nikdy za konstantu ani za složený term.
>
> *Příklad:* z ∀x ∀y (¬T(x, y, x) ∨ S(y)) dá x := a klauzuli ∀y (¬T(a, y, a) ∨ S(y)). Nepovolené: z P(a) udělat ∀x P(x), protože P(a) ⊭ ∀x P(x).

**Formálně:** α(x := t) = dosazení t za všechny výskyty x v otevřeném jádru α + ∀ pro zbylé proměnné; povolené jsou x := y (legální přejmenování), x := a (konstanta), x := g(t₁, …, tₙ), kde t₁, …, tₙ neobsahují x; pro ně α ⊨ α(x := t) (důsledek dává i x := f(x), zakazuje se kvůli unifikaci)

**Definice:** [[LGR 12 – Unifikace, rezoluce v predikátové logice a první grafy#^def-povolena-substituce|přednáška 12, 12. 11. 2026]] · handout 7, slajdy 24–25

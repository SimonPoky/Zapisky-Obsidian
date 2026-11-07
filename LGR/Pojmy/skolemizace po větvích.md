---
aliases: ["algoritmus 2", "skolemizace bez prenexního tvaru", "skolemizace po větvích syntaktického stromu"]
tags: [pojem, LGR]
predmet: LGR
prednaska: 11
zdroj: "handout 7, slajd 16"
---

# skolemizace po větvích

> [!lidsky] Lidsky
> Skolemizace bez převodu do prenexního tvaru: v syntaktickém stromu najdeš ∃ a jeho proměnnou nahradíš novou funkcí proměnných všech ∀, které jsou nad ním ve stejné větvi. Bez ∀ nad sebou dostane novou konstantu.
>
> *Příklad:* v ∃x ¬P(x) ∨ ∀z ∃y (R(z, y) ∧ Q(a)) je x := c (nad ∃x nic) a y := f(z) (nad ∃y je ∀z). V ∀x P(x) ∧ ∃y Q(y) je y := c, protože ∀x je v jiné větvi.

**Formálně:** po krocích 1–3 algoritmu 1: první ∃y ve větvi nahraď f(x₁, …, xₙ), kde x₁, …, xₙ jsou proměnné obecných kvantifikátorů nad ∃y směrem ke kořeni a f je nový funkční symbol arity n (n = 0: nová konstanta)

**Definice:** [[LGR 11 – Klauzální tvar a rezolventy v predikátové logice#^def-algoritmus-2|přednáška 11, 6. 11. 2026]] · handout 7, slajd 16

---
aliases: ["věty o sevření", "dva policajti", "dvou policajtech", "squeeze theorem"]
tags: [pojem, MA1]
predmet: MA1
prednaska: 4
zdroj: "handout 2B, slajd 9"
---

# věta o sevření

> [!lidsky] Lidsky
> Když je g ve směru sevřená mezi f a h a ty mají stejnou limitu L, má limitu L i g. Věta zároveň zaručí, že lim g existuje.
>
> *Příklad:* −1/n ≤ (−1)ⁿ/n ≤ 1/n a obě krajní posloupnosti jdou k 0, takže lim (−1)ⁿ/n = 0. Stejně −x² ≤ x² sin(1/x) ≤ x² dá limitu 0 pro x → 0.

> [!obrazek] Sevření x · sin(1/x)
> ![[ma104-sevreni.png]]
> *Oranžově horní mez |x|, modře dolní −|x|, zeleně x · sin(1/x), která mezi nimi kmitá stále rychleji, ale amplituda se k nule zmenšuje. Červená tečkovaná −x je pro x < 0 nad grafem, a proto jako dolní mez nefunguje.*

> [!obrazek] Důkaz obrázkem: věta o sevření
> ![[ma104-sevreni-dukaz.png]]
> *Vlevo graf: modrá f a oranžová h jdou k L, černá g kmitá mezi nimi. Nad oranžovým kusem P (nejmenší ze tří kusů v důkazu) leží zelená část g v modrém pásu U. Vpravo brambory: jeden bod x z P se zobrazí na f(x) a h(x), oba v terči U. Hodnota g(x) leží na zelené úsečce mezi nimi, a protože U je interval, je v U taky.*

**Formálně:** f ≤𝒮 g ≤𝒮 h, lim𝒮 f = lim𝒮 h = L ⇒ lim𝒮 g = L

**Definice:** [[MA1 04 – Nerovnosti ve směru a věta o sevření#^veta-sevreni|přednáška 4, 1. 10. 2026]] · handout 2B, slajd 9

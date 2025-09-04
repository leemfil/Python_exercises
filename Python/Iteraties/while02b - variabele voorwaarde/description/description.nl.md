## Opdracht

Schrijf een programma dat **eerst vraagt** of de gebruiker een **klein** of **groot** doel wil, en daarna **getallen blijft vragen** tot de **som** het gekozen **doel** bereikt of overschrijdt.

- Keuze:
  - `k` → **klein doel**: `20`
  - `g` → **groot doel**: `100`
  - elke andere invoer → behandel als **groot doel** (`100`)
- Vervolgens leest het programma **gehele getallen** in (één per regel) en telt die op **tot de som ≥ doel**.
- Tenslotte print het programma:  
Doel bereikt: som = X (>= D)
waarbij `X` de som is en `D` het gekozen doel (`20` of `100`).

> Opmerking: Lees de invoer in volgorde: eerst de keuze (`k/g/…`), daarna zoveel getallen als nodig.

---

## Invoer  
1. Een **tekenreeks** met de keuze: `k` of `g` (hoofdletter of kleine letter), of iets anders.
2. Daarna **een reeks gehele getallen**, één per regel, tot de som ≥ doel.

## Uitvoer  
Exact één regel:
Doel bereikt: som = X (>= D)
---

## Voorbeelden

**Voorbeeld 1**

**Invoer**  
k  
5  
8  
7  

**Uitvoer**  
Doel bereikt: som = 20 (>= 20)
---

**Voorbeeld 2**  

**Invoer**  
g  
25  
25  
30  
15  
10  

**Uitvoer**  
Doel bereikt: som = 105 (>= 100)

> Tip: bepaal het `doel` **vóór** je de `while` start; bv. `doel = 20 if keuze == 'k' else 100` (na normalisatie).

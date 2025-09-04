## Opdracht  

Schrijf een programma dat **getallen blijft vragen** aan de gebruiker totdat de **som van alle ingegeven getallen minstens 100** is.  
Daarna wordt de bereikte som afgedrukt.

Gebruik hiervoor een **`while`-lus** met een **voorwaarde** (`som < doel`).

---

## Invoer
- De gebruiker geeft telkens een geheel getal in.  
- Er is **geen vast aantal** getallen: de lus stopt pas wanneer de som **≥ 100** is.  

## Uitvoer
- Na afloop print het programma:
Doel bereikt: som = X (>= 100)

yaml
Code kopiëren
waarbij **X** de uiteindelijke som is.

---

## Voorbeelden

**Voorbeeld 1**

**Invoer**
10
20
30
40

markdown
Code kopiëren

**Uitvoer**
Doel bereikt: som = 100 (>= 100)

yaml
Code kopiëren

---

**Voorbeeld 2**

**Invoer**
25
25
30
15
10

markdown
Code kopiëren

**Uitvoer**
Doel bereikt: som = 105 (>= 100)

yaml
Code kopiëren

---

> 💡 Tip:  
> Begin met `som = 0` en gebruik een `while som < 100:` lus.  
> Voeg telkens het ingegeven getal toe aan de som.
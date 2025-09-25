## Opdracht
<br>

Schrijf een programma dat herhaaldelijk het **aantal uren** (geheel getal) inleest waarvoor iemand wil parkeren.  
Je **stopt** wanneer het aantal uren **`-1`** is.  

Gebruik onderstaande **basistarieven** per sessie (géén toeslagen of kortingen):

- `uren <= 0` → **€0**  
- `1–2 uur` → **€3 per uur**  
- `3–5 uur` → **€2 per uur**  
- `6+ uur` → **€12** (dagplafond)

Aan het einde druk je **exact** dit overzicht af:  
Aantal sessies: X  
Brutobedrag: Y euro  
Gemiddelde tijd: G uur  

waarbij `Y` en `G` met **één decimaal** worden weergegeven.

> Opmerking:
> - Je mag ervan uitgaan dat de invoer voor uren **altijd een int** is.  
> - Negatieve waarden **anders dan `-1`** komen niet voor in de tests.

---

## Voorbeeld

**Invoer**  

    1  
    4  
    7  
    -1  

**Uitvoer**  

    Aantal sessies: 3  
    Brutobedrag: 23.0 euro  
    Gemiddelde tijd: 4.0 uur  

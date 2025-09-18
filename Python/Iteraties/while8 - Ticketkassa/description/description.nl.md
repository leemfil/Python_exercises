## Opdracht
<br>

Je bouwt een kassa voor een klein filmhuis. De kassa leest **herhaaldelijk leeftijden** in en rekent per bezoeker een tarief aan volgens onderstaande regels.

### Tarieven  
- **< 3 jaar** → €0 (gratis)  
- **3–11 jaar** → €6  
- **12–64 jaar** → €12  
- **65+ jaar** → €8  

### Kortingscodes  
Na de leeftijd lees je **één regel** met een kortingscode (hoofdletter-ongevoelig):  
- `"student"` → 20% korting, alleen als basisprijs €12 is.  
- `"pas"` → €1 vaste korting, enkel als basisprijs > 0.  
- andere of lege invoer → geen korting.  

**Niet cumulatief**: als meerdere regels lijken te gelden, neem de **beste korting** (grootste vermindering in euro).

### Invoer
- Leeftijd als geheel getal.
- Kortingcodes.
- Bij leeftijd `0` stopt het programma (de kortingscode wordt dan niet meer gelezen).

### Uitvoer
Aan het einde print je exact dit overzicht:  
Aantal tickets: X  
Brutobedrag: Y euro  
Korting: Z euro  
Te betalen: T euro  

### Voorbeeld  

**Invoer**  
2  
  
19  
student  
70  
pas  
-1  

**Uitvoer**  
Aantal tickets: 3  
Brutobedrag: 20.6 euro  
Korting: 4.4 euro  
Te betalen: 16.2 euro

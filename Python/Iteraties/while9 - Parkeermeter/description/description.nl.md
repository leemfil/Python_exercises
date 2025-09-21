## Opdracht
<br>

Je bouwt de logica van een **parkeermeter**. Het programma leest **herhaaldelijk het aantal uren** dat een bestuurder wil parkeren (geheel getal), gevolgd door een **zonecode** op de volgende regel. Stoppen doe je met **`-10`** als aantal uren.

### Basistarief per sessie
- `uren <= 0` → **€0**  
- `1–2 uur` → **€3 per uur**  
- `3–5 uur` → **€2 per uur**  
- `6+ uur` → **€12** (dagplafond)

### Zone-toeslag (één code per sessie, hoofdletter-ongevoelig)
- `centrum` → **15% toeslag** op de sessieprijs  
- `overdekt` → **€1 vaste toeslag** (alleen als de prijs > 0)  
- andere of lege invoer → **geen toeslag**

> Opmerking:
> - Als de zonecode niet herkend wordt of leeg is, wordt er **geen toeslag** toegepast.

### Invoer
- Lees telkens **eerst** het aantal uren (int).
- Lees de zoncode op de volgende regel. Lege invoer is ook mogelijk (deze moet ook gelezen worden). 
- Als het aantal uren `-10` is, **stop** (de zonecode wordt dan niet meer gelezen).

### Uitvoer
Aan het einde druk je **exact** dit overzicht af:
Aantal sessies: X
Brutobedrag: Y euro
Toeslag: Z euro
Te betalen: T euro

met **één decimaal** voor alle bedragen.

### Voorbeeld

**Invoer**  
1  
overdekt  
4  
centrum  
7  
  
-10

**Uitleg**  
- 1 uur → €3, `overdekt` → €1 toeslag → **€4**  
- 4 uur → 4×€2 = €8, `centrum` → 15% van 8 = €1,2 toeslag → **€9,2**  
- 7 uur → €12, (lege code) → **€12**  

**Uitvoer**
Aantal sessies: 3
Brutobedrag: 23.0 euro
Toeslag: 2.2 euro
Te betalen: 25.2 euro

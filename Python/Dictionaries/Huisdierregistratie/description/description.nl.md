## Huisdierregistratie

### Opdracht
<br>

Je bouwt een klein registratiesysteem voor een dierenartspraktijk.  
Het doel is om gegevens over één huisdier in te voeren en op te slaan in een **dictionary**.

Je programma moet:

- zelf een dictionary opbouwen,
- gegevens opvragen via `input()`,
- een lijst met vaccins samenstellen,
- een extra vaccin kunnen toevoegen,
- `get()` gebruiken met een standaardboodschap voor ontbrekende gegevens,
- op het einde een overzicht tonen.

### Gegevens die je moet inlezen

Lees de invoer in deze volgorde:

1. de **naam** van het huisdier (string)  
2. de **leeftijd** (geheel getal)  
3. het **aantal vaccins** (geheel getal)  
4. per vaccin: de **naam** van het vaccin (string, één per regel)  
5. vervolgens **nog één regel** voor een **extra vaccin**:  
   - als die regel leeg is → geen extra vaccin  
   - anders → voeg de naam toe aan de vaccinslijst  

### Werkwijze

1. Maak een **lege dictionary** `huisdier`.
2. Vul de keys:
   - `"naam"` → met de ingelezen naam  
   - `"leeftijd"` → met de ingelezen leeftijd (int)  
   - `"vaccins"` → met een **lijst** van vaccinnamen  
3. Bouw de lijst `vaccins` met een `for`-lus op basis van het aantal vaccins.
4. Lees een extra vaccin in:
   - als de invoer **niet leeg** is, voeg je dit vaccin toe aan de lijst.
5. Toon op het einde een overzicht:
   - print eerst de naam  
   - dan de leeftijd  
   - dan elk vaccin **onder elkaar**  
6. Toon het ras van het huisdier
   - Check of het ras aanwezig is in de dictionary. Als er nog geen ras aanwezig is dan geef je de boodschap: "Het ras is niet bekend."
  
### Voorbeeld

Invoer  

    Rocky  
    5  
    2  
    Rabiës  
    Parvo


Uitvoer

    Rocky
    5
    Rabiës
    Parvo
    Er is geen ras geregistreerd voor dit huisdier.

### Opdracht

Tijdens de jaarlijkse interscholenquiz is er een lijst opgesteld met deelnemers van verschillende scholen.  
Vlak voor de start van de wedstrijd blijkt echter dat enkele deelnemers zich hebben afgemeld.  
Sommigen sturen een vervanger, anderen blijven gewoon weg.  
Als organisator wil je een overzicht behouden van wie uiteindelijk effectief deelneemt aan de quiz.  
Omdat de puntentelling gebaseerd is op de alfabetische volgorde van de namen, is het belangrijk dat de lijst correct en gesorteerd is.  
Daarnaast wil de jury op het einde nog snel controleren of een specifieke deelnemer zich in de definitieve lijst bevindt, en op welke positie.

<br/>

**Schrijf een programma dat het volgende doet:**

1. Vraag de deelnemers op in één regel, **gescheiden door spaties**.
2. Zet de namen om naar een lijst.
3. Vraag het aantal afmeldingen.
4. Voor elke afmelding:
   - Vraag de naam van de afwezige deelnemer.
   - Vraag of er een vervanger is (antwoord `ja` of `nee`):
     - Zo ja, vraag de naam van de vervanger en **vervang** de originele naam in de lijst.
     - Zo nee, **verwijder** de deelnemer uit de lijst.
5. Sorteer de deelnemerslijst alfabetisch.
6. Toon de namen uit de aangepaste lijst achter elkaar gescheiden door een komma.
7. Vraag een naam op en geef aan of deze persoon nog in de lijst zit, en zo ja, op welke index.

---

### Invoer

- Eén regel met alle deelnemernamen, gescheiden door spaties.
- Het aantal afmeldingen.
- Per afmelding:
  - naam
  - `ja` of `nee`
  - indien `ja`: vervanger
- Een naam om op te zoeken.

---

### Uitvoer

- De definitieve namen (gesorteerd) gescheiden door een komma.
- Indien aanwezig: `De deelnemer X staat op index Y.`
- Indien niet aanwezig: `X zit niet meer in de lijst.`

---

### Voorbeeld

**Invoer**
Emma Lina Jonas Sarah Bram
2
Jonas
ja
Karel
Lina
nee
Sarah

**Uitvoer**
Bram, Emma, Karel, Sarah
De deelnemer Sarah staat op index 3.

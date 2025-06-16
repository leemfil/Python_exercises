### Opdracht
<br/>

2️⃣ FASE 2: Ontcijfer gecodeerde zendingen
Een tweede type bericht is onderschept via satelliet.
De boodschap lijkt compleet onsamenhangend, maar analyse wijst uit dat alleen de tekens op oneven indexen (1, 3, 5, …) iets betekenen.

Bovendien zijn spaties vervangen door het symbool #. We vermoeden dat de vijand hier een codewoord gebruikt om zijn identiteit te bevestigen.  

<br/>

**Schrijf een programma dat het volgende doet:**

1. Vraag een gecodeerde boodschap aan de gebruiker.
2. Bouw een nieuwe string op met **de tekens op oneven posities**.
3. Zet de gedecodeerde boodschap volledig om naar **kleine letters**.
4. Vervang elke `#` door een spatie.
5. Toon de gedecodeerde boodschap op het scherm met spaties tussen de letters.
6. Vraag het codewoord aan de gebruiker.
7. Controleer of het codewoord in de gedecodeerde boodschap voorkomt.
8. Toon hoeveel keer het codewoord voorkomt.
9. Toon ook het aantal tekens (exclusief spaties) in de decodeerde boodschap.

---

### Invoer

 1: de gecodeerde boodschap (string).
 2: het codewoord

---

### Uitvoer

- De gedecodeerde boodschap in kleine letters, met spaties op de juiste plaats.
- Een melding of het codewoord gevonden werd, en hoe vaak.
- Het aantal letters zonder spaties.

---

### Voorbeeld

**Invoer**

    Xa#gAe#nT#xA#G#E#N#t

**Uitvoer**

    a g e n t a g e n t
    Patroon 'agent' komt 2 keer voor.
    De boodschap bevat 10 letters zonder spaties.

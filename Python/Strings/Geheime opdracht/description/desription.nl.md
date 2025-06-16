### Opdracht

Je krijgt een gecodeerde boodschap die schijnbaar zinloos lijkt, maar enkel de tekens op de **oneven indexen** (1, 3, 5, ...) vormen de echte boodschap.

De boodschap bevat ook het symbool `#` op plaatsen waar een spatie hoort. Verder willen we nagaan of het woord `"agent"` in de decodeerde boodschap voorkomt.

<br/>

**Schrijf een programma dat het volgende doet:**

1. Vraag een gecodeerde boodschap aan de gebruiker.
2. Bouw een nieuwe string op met **de tekens op oneven indexen**.
3. Zet de decodeerde boodschap volledig om naar **kleine letters**.
4. Vervang elke `#` door een spatie.
5. Toon de decodeerde boodschap op het scherm.
6. Controleer of het woord `"agent"` in de decodeerde boodschap voorkomt.
7. Toon hoeveel keer het woord `"agent"` voorkomt.
8. Toon ook het aantal tekens (exclusief spaties) in de decodeerde boodschap.

---

### Invoer

Eén regel: de gecodeerde boodschap (string).

---

### Uitvoer

- De decodeerde boodschap in kleine letters, met spaties op de juiste plaats.
- Een melding of `"agent"` gevonden werd, en hoe vaak.
- Het aantal letters zonder spaties.

---

### Voorbeeld

**Invoer**

    Xa#gAe#nT#xA#G#E#N#t

**Uitvoer**

    a g e n t a g e n t
    Patroon 'agent' komt 2 keer voor.
    De boodschap bevat 10 letters zonder spaties.

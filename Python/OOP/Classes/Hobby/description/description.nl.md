### Toets OOP 2 — “Familie-manager”

**Context**  
Schrijf een Python-programma waarmee je informatie over een familie kan bewaren en bewerken. Je werkt objectgeoriënteerd en toont dat je attributen, methoden, class-variabelen, compositie, overerving en operator overloading beheerst.

**Functionele eisen (wat het programma moet kunnen)**  
1. Familie aanmaken met:
   - Eén familie-object die volgende objecten bevat:
   - Minstens twee ouder-objecten (bv. moeder, vader of twee andere voogden).
   - Kind-objecten (2 of meer).
   - Huisdier-objecten (2 of meer).

2. Weergave  
Gebruik de python methoden om de objecten weer te geven op het scherm.  
    - Een nette tekstweergave van de familie (ouders, kinderen, huisdieren).
    - Een korte weergave per individu (voornaam, achternaam, leeftijd of geboortedatum).

3. Class-variabele  
Voorzie één class-variabele voor een familie klasse: teller van aangemaakte personen. Toon dat je die gebruikt in je programma.

4. Voorzie een methode die kinder-objecten toevoegt aan een ouder-object.

5. Operator ‘+’ op ouders
     - Het optellen van twee ouder-objecten met + geeft:
       - het aantal kinderen als de twee ouders effectief één koppel vormen binnen dezelfde familie;
       - anders 0.

6. Zoek/filters (min. 1)
     - Bijvoorbeeld: alle kinderen jonger dan 12, of alle huisdieren van soort “kat”.


**Technische eisen (hoe je het bouwt)**
1. Overerving
    - Maak een basisklasse (bv. Persoon) en laat andere klassen hiervan erven .
    - Huisdier is geen Persoon, maar een aparte klasse.

2. Compositie
    - Een klasse Familie bevat collecties van ouders, kinderen  en huisdier objecten.

3. Elk naam attribuut van een klasse is private.

4. Attributen & methoden
    - Elke klasse heeft minstens 2 attributen.
    - Voorzie alle nodige methoden.
    - Van getters/setters schrijf je voor elke private variabele.

5. Operator overloading
    - Implementeer in de ouder-klasse de juiste dunder-methode om de eis over het koppel en het aantal kinderen te realiseren (zie Functionele eisen #5).

6. Test
    - Test het programma met een kort demo-script dat objecten aanmaakt, acties uitvoert en resultaten print.



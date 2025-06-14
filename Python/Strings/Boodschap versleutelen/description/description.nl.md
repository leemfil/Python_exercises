### Opdracht

In spionagefilms wordt vaak gecommuniceerd via geheime boodschappen die er op het eerste gezicht normaal uitzien. Stel dat een geheime dienst boodschappen verstuurt waarin een **codewoord** verborgen zit, en we moeten nagaan of het aanwezig is en waar het begint.

<br/>

**Voorbeelden van geheime boodschappen:**   

- "De documenten zitten in de kast onder de vloer."
- "Vergeet niet dat het woord ALPHA belangrijk is."
- "Kijk in het boek, tweede plank, derde rij."

**Schrijf een programma dat volgende bewerkingen op een boodschap uitvoert:**

* Vraag een **boodschap** en een **codewoord** aan de gebruiker.
* Zet de boodschap volledig in **kleine letters**.
* Zoek met behulp van `find()` op welke positie het codewoord voor het eerst voorkomt.
* Als het codewoord **voorkomt**, beeld dan de boodschap af vanaf dat punt tot het einde.  
Indien het niet voorkomt beeld je volgende boodschap af: "Het codewoord komt niet voor."
* Vervang elk **letterteken** in de boodschap door een sterretje `*`, behalve de spaties en leestekens. Gebruik een **for-lus**.
* Toon de gemaskeerde boodschap in een zin op het scherm.

### Invoer

De volledige boodschap (één string).  
Het codewoord (één woord, hoofdlettergevoelig bij invoer).

### Uitvoer

De positie van het codewoord in de boodschap.  
Het deel van de boodschap vanaf dat punt tot het einde.  
De gemaskeerde boodschap.  

### Voorbeeld

**Invoer**

    De documenten zitten in de kast onder de vloer.
    kast

**Uitvoer**

    Het codewoord begint op positie 27.
    kast onder de vloer.
    De gemaskeerde boodschap is: ** ********** ****** ** ** **** ***** ** *****.

**Invoer**

    Vergeet niet dat het woord ALPHA belangrijk is.
    alpha

**Uitvoer**

    Het codewoord begint op positie 27.
    alpha belangrijk is.
    De gemaskeerde boodschap is: ******* **** *** *** ***** ***** ********** **.

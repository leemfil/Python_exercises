### Opdracht

We willen alle activiteiten van de school gaan beheren. Hiervoor gebruiken we 3 lijsten. In de 1ste lijst zetten we alle activiteiten die gepland zijn in de toekomst. In de 2de lijst komen alle activiteiten die momenteel plaats hebben of uitgevoerd worden. We kunnen zelf activiteiten toevoegen en verplaatsen van lijst.  

Schrijf een programma dat:
* een string met activiteiten gescheiden door een spatie vraagt aan de gebruiker,
* de activiteiten in de 1ste lijst zet,
* een extra activiteit vraagt en achteraan toevoegt aan de 1ste lijst indien die activiteit nog niet in de lijst staat, anders voeg je niets toe en geef je een boodschap aan de gebruiker,
* de eerste activiteit uit de 1ste lijst verwijdert en in de 2de lijst zet,
* de lijsten onder elkaar afbeeldt op het scherm,
* de activiteiten selecteert, te beginnen bij de 1ste en dan telkens 2 activiteiten overslaat, de volgende activiteit selecteert, 2 activiteiten overslaat, en zo verder tot het eind, 
* de geselecteerde activiteiten onder elkaar op het scherm zet,
* de laatste activiteit uit de 1ste lijst verwijderd en in de 2de lijst achteraan toevoegt,
* de prioriteit verandert in de 1ste lijst door de eerste en de tweede activiteit om te draaien in de lijst,
* de eerste letter van elke activiteit aanpast naar een hoofdletter,
* de lijsten afbeeldt op het scherm. 

### Invoer

Een string met activiteiten gescheiden door een spatie.

### Uitvoer

* De 1ste lijst is <1ste lijst>.
* De 2de lijst is <2de lijst>.
* Eventueel volgende: "De activiteit is al aanwezig in de 1ste lijst."
* Geselecteerde activiteiten: 1ste, 4de, 7de, ...
* De 1ste lijst is <1ste lijst>.
* De 2de lijst is <2de lijst>.

### Voorbeeld

**Invoer**
    
    "voetbal galabal festival theater"
    zwemmen
    themadag
    
**Uitvoer**
   
    De 1ste lijst is ['galabal', 'festival', 'theater', 'zwemmen'].  
    De 2de lijst is ['voetbal'].  
    galabal  
    zwemmen  
    De 1ste lijst is ['Festival, 'Galabal', 'Theater'].  
    De 2de lijst is ['themadag', 'zwemmen'].  

### Opdracht

We willen alle activiteiten van de school gaan beheren. Hiervoor gebruiken we een agenda. De agenda is een lijst waarin activiteiten kunnen toegevoegd, vervangen of verwijderd worden.

Schrijf een programmma dat:
* Aan de gebruiker vraagt hoeveel activiteiten hij gaat geven om in de agenda te zetten. Vervolgens alle activiteiten aan de gebruiker vraagt en toevoegt aan een lijst. Indien de activiteit reeds in de lijst staat dan wordt deze geen 2de keer toegevoegd. Dus alle activiteiten zijn uniek. Beeldt de lijst af op het scherm.
* Doorloop de lijst en verwijder alle activiteiten die de letter "t" bevatten, klein of grote letter. Beeldt de nieuwe lijst af op het scherm.
* Beeld de plaats van de activiteit "uitstap" in de originele lijst af op het scherm in een zin. <span style="color:white">negeer invoer, uitvoer, voorbeelden</span>
* Deel de originele lijst op in 2 nieuwe lijsten, een lijst met activiteiten waarvan de 2de letter gelijk is aan "e" of "o" en een lijst met de overige activiteiten. Beeldt deze 2 nieuwe lijsten onder ekaar af op het scherm.
* Verwijder de 3de activiteit in de originele lijst. Beeldt de lijst af op het scherm.

### Invoer
    
* het aantal activiteiten die worden toegevoegd
* alle activiteiten onder elkaar

### Uitvoer

* lijst met activiteiten, geen dubbele activiteiten
* lijst met activiteiten die geen letter "t" bevatten.
* zin: "De plaats van uitstap is x." met x de juiste plaats in de originele lijst
* lijst met activiteiten met de letter "e" of "o" op de 2de plaats
* lijst met activiteiten met geen letter "e" of "o" op de 2de plaats
* lijst waarin de activiteit op de 3de plaats is verwijderd

### Voorbeeld

**Invoer**
    
    6
    voetbal
    karaoke
    uitstap
    zwemmen
    voetbal
    theater
    
**Uitvoer**
   
    [voetbal, karaoke, uitstap, zwemmen, theater]
    [karaoke, zwemmen]
    De plaats van uitstap is 3.
    [voetbal]
    [karaoke, uitstap, zwemmen, theater]
    [voetbal, karaoke, zwemmen, theater]
    

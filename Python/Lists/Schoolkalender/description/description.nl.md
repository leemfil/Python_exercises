### Opdracht

We willen alle activiteiten van de school gaan beheren. Hiervoor gebruiken we een kalender. De kalender is een lijst waarin activiteiten kunnen toegevoegd, vervangen of verwijderd worden.

Schrijf een programmma dat:
* De verschillende activiteiten die door de gebruiker gegeven worden toevoegt aan een lijst. Wanneer de gebruiker het woord "einde" geeft, stopt de invoer in de lijst. Als activiteit reeds in de lijst staat dan voegen we de activiteit opnieuw toe maar met achteraan een 2 aan de activiteit geplakt. Beeldt de lijst af op het scherm.
* Doorloop de lijst en geef alle activiteiten die met de letter "t" of "v" beginnen, klein of grote letter. Beeldt de nieuwe lijst af op het scherm.
* Beeld de plaats van de activiteit "festival" af op het scherm in een zin. <span style="color:white">negeer invoer, uitvoer, voorbeelden</span>
* Deel de lijst op in 2 nieuwe lijsten, een lijst met activiteiten die de letter "a" bevatten en een lijst met de overige activiteiten. Beeldt deze 2 nieuwe lijsten onder ekaar af op het scherm.
* Voeg de activiteit "wandelen" toe aan de originele lijst op de 3de plaats. Beeldt de lijst af op het scherm.

### Invoer
    
* activiteiten onder elkaar, met als laatste het woord "einde"

### Uitvoer

* lijst met activiteiten, dubbele activiteiten bevatten een extra 2 achteraan
* lijst met activiteiten die met een "t" of "v" beginnen
* zin: "De plaats van festival is x." met x de juiste plaats
* lijst met activiteiten met de letter "a"
* lijst met activiteiten zonder de letter "a"
* lijst met de activiteit "wandelen" op de 3de positie

### Voorbeeld

**Invoer**
    
    voetbal
    festival
    zwemmen
    voetbal
    theater
    einde
    
**Uitvoer**
   
    [voetbal, festival, zwemmen, voetbal2, theater]
    [voetbal, voetbal2, theater]
    De plaats van festival is 2.
    [voetbal, festival, voetbal2, theater]
    [zwemmen]
    [voetbal, festival, wandelen, zwemmen, voetbal2, theater]
    

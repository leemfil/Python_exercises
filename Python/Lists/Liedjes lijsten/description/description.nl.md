### Opdracht

Een muziekspeler-app is een softwaretoepassing waarmee gebruikers audiobestanden kunnen afspelen en beheren op hun apparaten, zoals smartphones, tablets of computers. Deze apps bieden een gebruiksvriendelijke interface voor het organiseren van muziekbibliotheken, het maken van afspeellijsten en het afspelen van muziek in verschillende formaten, zoals MP3, FLAC, WAV of AAC.

Schrijf een programma dat:
- een string met liedjestitels gescheiden door een ; vraagt aan de gebruiker,
- de liedjestitels apart in een afspeellijst zet en toont,
- een favorietenlijst aanmaakt en de eerste en de laatste liedjestitels van de afspeellijst verhuist naar deze favorietenlijst en de afspeellijst en favorietenlijst toont,
- de eerste en laatste liedjestitels van de afspeellijst van plaats verwisselt,
- alle liedjestitels uit de afspeellijst onder elkaar afbeeldt die het woord 'You' bevatten,  
- ook het aantal liedjestitles die het woord 'You' bevatten weergeeft in een zin en
- de plaats weergeeft van de eerste liedjestitel in de afspeellijst die 10 tekens of spaties bevatten,
- de gewijzigde lijsten telkens afbeeldt op het scherm.

### Invoer

Een string met liedjestitels gescheiden door een spatie.

### Uitvoer

- volledige afspeellijst.
- afspeellijst zonder eerste en laatste liedjestitels en de favorietenlijst.
- afspeellijst met de eerste en laatste liedjestitels verwisselt van plaats.
- alle liedjestitels die het woord 'You' bevatten onder elkaar.
- het aantal liedjestitels met het woord 'You' weergeeft op het scherm in de volgende zin: Het aantal titels dat het woord 'You' bevat is ....
- een getal die de juiste plaats weergeeft op het scherm in de volgende zin: De eerste plaats van een titel met 10 tekens is ....

### Voorbeeld

**Invoer**
    
    "Uptown Funk;Someone Like You;Let It Be;Yesterday;Hallelujah;Shape of You;We Will Rock You;All Star"

**Uitvoer**
    
    ['Uptown Funk', 'Someone Like You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'We Will Rock You', 'All Star']
    ['Someone Like You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'We Will Rock You']
    ['Uptown Funk', 'All Star']
    ['We Will Rock You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'Someone Like You']
    Someone Like You
    We Will Rock You
    Shape of You
    Het aantal titels dat het woord 'You' bevat is 3.
    De eerste plaats van een titel met 10 tekens is 4.

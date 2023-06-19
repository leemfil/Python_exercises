### Opdracht

Een muziekspeler-app is een softwaretoepassing waarmee gebruikers audiobestanden kunnen afspelen en beheren op hun apparaten, zoals smartphones, tablets of computers. Deze apps bieden een gebruiksvriendelijke interface voor het organiseren van muziekbibliotheken, het maken van afspeellijsten en het afspelen van muziek in verschillende formaten, zoals MP3, FLAC, WAV of AAC.

Schrijf een programma dat:
- een string met liedjestitels gescheiden door een spatie vraagt aan de gebruiker,
- de liedjestitels apart in een afspeellijst zet,
- een favorietenlijst aanmaakt en de eerste en de laatste liedjestitels van de afspeellijst verhuist naar de favorietenlijst,
- de eerste en laatste liedjestitels van de afspeellijst van plaats verwisselt,
- de plaats weergeeft van de eerste liedjestitel in de afspeellijst die 10 tekens of spaties bevatten,
- alle liedjestitels uit de afspeellijst onder elkaar afbeeldt die het woord 'You' bevatten,  
- ook het aantal liedjestitles die het woord 'You' bevatten weergeeft in een zin en
- de gewijzigde lijsten telkens afbeeldt op het scherm.

### Invoer

Een string met liedjestitels gescheiden door een spatie.

### Uitvoer

- volledige afspeellijst.
- afspeellijst en de favorietenlijst met eerste en laatste liedjestitels verhuist.
- afspeellijst met de eerste en laatste liedjestitels verwisselt van plaats.
- een getal die de juiste plaats weergeeft op het scherm in de volgende zin: De eerste plaats van een titel met 10 tekens is ....
- alle liedjestitels die het woord 'You' bevatten onder elkaar.
- het aantal liedjestitels met het woord 'You' weergeeft op het scherm in de volgende zin: Het aantal titels dat het woord 'You' bevat is ....

### Voorbeeld

**Invoer**
    
    "Uptown Funk;Someone Like You;Let It Be;Yesterday;Hallelujah;Shape of You;We Will Rock You;All Star"

**Uitvoer**
    
    ['Uptown Funk', 'Someone Like You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'We Will Rock You', 'All Star']
    ['Someone Like You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'We Will Rock You']
    ['Uptown Funk', 'All Star']
    ['We Will Rock You', 'Let It Be', 'Yesterday', 'Hallelujah', 'Shape of You', 'Someone Like You']
    De eerste plaats van een titel met 10 tekens is 4.
    Someone Like You
    We Will Rock You
    Shape of You
    Het aantal titels dat het woord 'You' bevat is 3.

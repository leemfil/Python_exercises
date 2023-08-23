### Opdracht

Het pad of de padnaam is de aanduiding van de exacte locatie van een bestand op de harde schijf van een computer. De padnaam bestaat uit de letter van het station op de harde schijf, de map, eventuele submappen en de bestandsnaam met bestandsextensie.   
Bijvoorbeeld C:\Mijn documenten\Netwerken\transportlaag.pdf.

Schrijf een programma dat de map en submappen geeft van de locatie een bepaald bestand uit de gegeven padnaam.  
Als laatste geeft hetv programma de extensie van het bestand:
- Vraag aan de gebruiker de padnaam waaruit je alle informatie haalt.
- Haal uit de padnaam de map en alle eventuele submappen.
- Haal de extensie van het bestand uit de padnaam.
- Beeldt alle mappen onder elkaar af op het scherm. Nummer de mappen.
- Beeldt de extensie van het bestand af in een zin. De extensie is de laatste 3 letters van de padnaam.

### Invoer

Een padnaam.

### Uitvoer

Alle mappen onder elkaar:  
1: map1  
2: map2  
...  
De extensie van het bestand is .... (laatste 3 letters).

**Hint**:  
Als je een \ in een string gebruikt moet je een extra \ toevoegen omdat het een speciaal teken is.  
Bijvoorbeeld: ``"\\"`` ipv ``"\"``

### Voorbeeld

**Invoer**

    C:\Mijn documenten\Netwerken\transportlaag.pdf

**Uitvoer**

    1: Mijn documenten
    2: Netwerken
    De extensie van het bestand is pdf.

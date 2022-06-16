### Opdracht

<br>  
<div class="dodona-centered-group"><img src="media/zeilen.jpeg" width="600" height="300"></div>
<br>

De Laser is een snelle Olympische eenmansboot. Je kunt er 3 maten zeil op zetten, van klein naar groot. Het is de grootste eenheidsklasse in de wereld. Daarom kom je overal Lasers tegen en kan je wereldwijd wedstrijden varen.

Bij het zeilen bestaat elke wedstrijd uit een aantal races. De winnaar van elke race krijgt 1 punt, de nummer 2 krijgt 2 punten enz. Degene met aan het eind het minste aantal punten wint het toernooi.

### Invoer

* De plaatsen (punten) van verschillende races van een zeiler. Er kunnen tot 25 zeilers deelnemen aan een race en elk resultaat staat op een aparte regel. De resultaten worden afgesloten met de S van stop (laatste resultaat). 
* Een zeiler kan tijdens een race ook strafpunten krijgen omwille van het overtreden van een regel. Dit staat ook in de invoer achter de race waarin de strafpunten werden toegekend en wordt aangeduid met een X.


### Uitvoer

* Het aantal punten die de zeiler heeft verzameld en het aantal keer dat hij strafpunten heeft gekregen.
* Verdeel het aantal punten in opeenvolgende schijven. Geef per schijf van 5 punten aan hoeveel keer hij daarin is geëindigd.

### Voorbeeld

**Invoer**
    
    15
    3
    X
    7
    12
    5
    X 
    8
    4
    13
    7
    X
    6
    X
    S
    

**Uitvoer**
    
    De zeiler heeft 80 punten verzameld.
    En hij heeft 4 strafpunten gekregen.
    
    1 - 5: 3
    6 - 10: 4
    11 - 15: 3
    16 - 20: 0
    21 - 25: 0

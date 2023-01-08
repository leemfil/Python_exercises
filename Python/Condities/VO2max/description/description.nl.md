De VO<sub>2</sub>max of het of het maximale zuurstofopnamevermogen is het maximale volume zuurstof dat het menselijk licdhaam kan transporteren en verwerken.

<br>  
<div class="dodona-centered-group"><img src="media/lopers.jpeg" width="450" height="252"></div>
<br>

Gemiddeld gesproken hebben mannen een VO<sub>2</sub>max tussen de 35 en 40 ml/kg/min. Voor vrouwen ligt dit tussen de 27 en 31 ml/kg/min. Topsporters kunnen waarden bereiken die tussen de 60 en 95 ml/kg/min liggen. De VO<sub>2</sub>max neemt af met de leeftijd.

<br>
<table>
     <tr>
          <th><div class="dodona-centered-group"><img src="media/VO2max_waarderingen_mannen.png" width="514" height="288"></div></th>
          <th><div class="dodona-centered-group"><img src="media/VO2max_waarderingen_vrouwen.png" width="514" height="288"></div></th>
     </tr>
</table>
<br>

Een methode om de VO<sub>2</sub>max te schatten maakt gebruik van de coopertest. Bij de coopertest is het de bedoeling dat je in 12 minuten een zo groot mogelijke afstand aflegt. Met behulp van de afgelegde afstand kan je dan met onderstaande formule de VO<sub>2</sub>max benaderen.:

<br>  
<div class="dodona-centered-group"><img src="media/form_vo2max.png" width="237" height="78"></div>
<br>

waarbij $d$<sub>12</sub> de afstand in meter die men aflegt in 12 minuten.

### Opgave

Schrijf een programma dat:

- de afstand $d$<sub>12</sub> in meter vraagt,
- het geslacht vraagt,
-  de leeftijd vraagt,
- de VO<sub>2</sub>max schatting op 1 cijfer na de komma berekent
- en vervolgens de juiste boodschap op het scherm zet afhankelijk van het geslacht en de leeftijd.

### Invoer

- De afstand afgelegd in 12 minuten in meter.
- Het geslacht.
- De leeftijd.

### Uitvoer

Volgende boodschap:  

     Je heb een VO2max van <berekende waarde> ml/kg/min en dus een <waardering> conditie. 
     
Waarbij \<berekende waarde\> vervangen wordt door het resultaat van je berekening afgerond op 1 cijfer na de komma  
en \<waardering\> door de juiste waardering uit de tabel: "slechte", "gemiddelde", "goede" of "uitstekende".

### Voorbeelden

**Invoer**

     2450
     man
     45

**Uitvoer**

     Je hebt een VO2max van 43.2 ml/kg/min en dus een goede conditie.  
     
**Invoer**

     2000
     vrouw
     29

**Uitvoer**

     Je hebt een VO2max van 33.2 ml/kg/min en dus een gemiddelde conditie. 

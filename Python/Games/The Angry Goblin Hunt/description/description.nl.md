### Opdracht

Maak een game die verloopt volgens onderstaand schema.  
Op het scherm verschijnt het volgende:

*Welcome to the Angry Goblin Hunt
An award-winning game full of adventure and excitement (!)*

*Type in your name: Stephen*

*Stephen, do you think you can find the goblin hiding in the kitchen cupboards?*  
|\_||\_||\_||\_||\_|

*Which cupboard do you think the goblin is in [type in number]: 2  
Sorry! The goblin is still lurking somewhere else.*

*Which cupboard do you think the goblin is in [type in number]: 4  
Sorry! The goblin is still lurking somewhere else.*

*Which cupboard do you think the goblin is in [type in number]: 3  
Sorry! The goblin is still lurking somewhere else.*

*Which cupboard do you think the goblin is in [type in number]: 1  
Well done!! You have found the goblin. He was so scared he ran away.*


Hier is een samenvatting:
- Toon een welkomboodschap.
- Vraag de speler naar hun naam, en wanneer ze hun naam ingegeven hebben dan volgt de rest van de welkomboodschap.
- Toon een "grafische" voorstelling van de keukenkast (ja, we houden het hier heel, heel simpel).
- Vraag de speler om te raden waar de Goblin zich verbergt door het nummer van het keukenkastje te geven.
- Als de gok niet correct is, geef dan de gepaste boodschap en vraag dan om opnieuw een gok te wagen. 
- Als de gok wel correct is, geef dan de winnende boodschap en eindig het spel.

***Testen***
- Als de goblin in keukenkastje 3 verstopt is dan zal de test bij een correct programma slagen en krijg je een groen scherm.
- Wanneer je een correct programma hebt gemaakt dan kan je het aanpassen en de goblin in een willekeurige keukenkastje verstoppen. Je kan een willekeurig getal genereren met behulp van de **random** module. De test zal dan echter niet meer slagen.  

***Achtergrondinformatie***  

De **random** module bevat een functie **randint(begingetal, eingetal)** die een willekeurig integer getal teruggeeft tussen het begingetal en tot en met het eindgetal. De import van de random module gebeurt op de 1ste regel van het programma.  

**Voorbeeld 1:**  

import random

willekeurig_getal = random.randint(1, 10)

**Of voorbeeld 2:**  

from random import randint

willekeurig_getal = randint(1, 10)

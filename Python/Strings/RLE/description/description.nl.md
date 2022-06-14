### Opdracht

Run-length encoding, kortweg RLE, is het vervangen van herhalende patronen in data door het aantal herhalingen plus wat herhaald moest worden. Een voorbeeld: stel dat we de volgende tekenreeks in het alfabet (a-z) willen comprimeren:

    dghakaaaaaaaaaaaaaabbbbaaakhffff

We kunnen dan ons alfabet uitbreiden met de tekens (0-9) om herhalingen aan te geven, en zouden dan de tekst als volgt kunnen comprimeren:

    dghak14a4b3akh4f

aaaaaaaaaaaaaa vervangen we door 14a, bbbb door 4b, aaa door 3a en ffff door 4f.

Een geval waarin RLE uitermate effectief is, is het comprimeren van grafische afbeeldingen zoals logo's en animaties. In deze beelden bevinden zich vaak grote gedeelten met pixels van dezelfde kleur. In sommige gevallen kan de bestandsgroote van een afbeelding of animatie door RLE tientallen keren worden verkleind. 

### Invoer

Verschillende hoogten en gefaalde pogingen na elkaar. Bij 3 gefaalde pogingen stopt de invoer.

### Uitvoer

* Het aantal keer dat de atleet over de lat is gegaan en het aantal keer dat hij gefaald heeft.
* Verdeel de hoogte tussen 5,00 m en 6,20 m in stukken van 20 cm. Geef per deel van 20 cm aan hoeveel keer hij erover is gegaan.

### Voorbeeld

**Invoer**
    
    5,35
    5,50
    5,60
    X
    5,70
    X
    X
    5,75
    X
    X
    X
    

**Uitvoer**
    
    De atleet is 5 keer over de lat gegaan.
    En hij heeft 6 keer gefaald.
    
    5,00 - 5,19: 0
    5,20 - 5,39: 1
    5,40 - 5,59: 1
    5,60 - 5,79: 3
    5,80 - 5,99: 0
    6,00 - 6,19: 0
    
     
  
   

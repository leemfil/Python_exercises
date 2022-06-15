### Opdracht

Run-length encoding, kortweg RLE, is het vervangen van herhalende patronen in data door het aantal herhalingen plus wat herhaald moest worden. Een voorbeeld: stel dat we de volgende tekenreeks in het alfabet (a-z) willen comprimeren:

    dghakaaaaaaaaaaaaaabbbbaaakhffff

We kunnen dan ons alfabet uitbreiden met de tekens (0-9) om herhalingen aan te geven, en zouden dan de tekst als volgt kunnen comprimeren:

    dghak14a4b3akh4f

aaaaaaaaaaaaaa vervangen we door 14a, bbbb door 4b, aaa door 3a en ffff door 4f.

Een geval waarin RLE uitermate effectief is, is het comprimeren van grafische afbeeldingen zoals logo's en animaties. In deze beelden bevinden zich vaak grote gedeelten met pixels van dezelfde kleur. In sommige gevallen kan de bestandsgroote van een afbeelding of animatie door RLE tientallen keren worden verkleind. 

### Invoer

Een string met eventueel herhalingen van bepaalde letters.

### Uitvoer

Een string waarin de herhalingen achter elkaar van een bepaalde letter worden vervangen door een getal met daarachter de letter. Het getal geeft het aantal herhalingen weer.

### Voorbeeld

**Invoer**
    
    hhhbgefvvvvvvvvvtdsfkkkknuudhhhhh
    

**Uitvoer**
    
    3hbgef9vtdsf4kn2ud5h
    
     
  
   

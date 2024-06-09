### Opdracht
Een IBAN staat gelijk aan een bankrekeningnummer. Het aantal tekens varieert van land tot land, maar het maximum is 34. Aan het begin van elke IBAN staan telkens twee letters die overeenstemmen met de code van het land waarin de rekening wordt gehouden. Bijvoorbeeld FR voor een Franse rekening of NL voor een Nederlandse rekening. 

<br/>

**Voorbeelden:**   

Belgisch rekeningnummer: BE68 5390 0754 7034

Nederlands rekeningnummer: NL54 INGB 0001 2345 67

**Schrijf een programma dat volgende bewerkingen op bankrekeningnummers uitvoert:**
* Vraag een bankrekeningnummer aan de gebruiker.
* Zet de groepen tekens die gescheiden worden door een spatie onder elkaar op het scherm.
* Neem de eerste 2 letters uit het bankrekeningnummer en beeldt deze landcode af op het scherm. <span style="color:white">negeer invoer, uitvoer, voorbeelden</span>
* Verberg de middelste tekens van het bankrekeningnummer met *-tekens. Alleen de eerste 2 en de laatste 2 tekens worden niet vervangen. Het aantal *-tekens komt overeen met het aantal tekens, ook spaties, dat vervangen wordt. Beeldt de verborgen bankrekening af op het scherm.

### Invoer

Een bankrekeningnummer, waarvan de eerste 2 letters de landcode vormen. Na de landcode volgen een aantal cijfers of letters afhankelijk van het land. Om de vier tekens is er een spatie voorzien.

### Uitvoer

Bankrekeningnummer opgesplitst per groep onder elkaar.  
Landcode in zin: De landcode is LC.  
De verborgen bankrekening is LC***************cc.  
Waarbij LC de landcode is en cc de laatste 2 cijfers.

### Voorbeeld

**Invoer**
    
    NL54 INGB 0001 2345 67
    
**Uitvoer**

    NL54  
    INGB  
    0001  
    2345  
    67  
    De landcode is NL.
    De verborgen bankrekening is NL******************67.

**Invoer**

    BE68 5390 0754 7034  

**Uitvoer**

    BE68   
    5390  
    0754  
    7034  
    De landcode is BE.
    De verborgen bankrekening is BE***************34.
    
    
   

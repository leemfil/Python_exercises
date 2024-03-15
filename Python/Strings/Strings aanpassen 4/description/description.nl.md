### Opdracht

Schrijf een programma dat:  
- 3 aparte teksten vraagt aan de gebruiker,  
- en de teksten op de volgende manieren wijzigt:

1. Zoek in de tekst 2 de positie van de eerste letter i en neem de substring van al de letters na deze i tot en het laatste teken. Zet de substring op het scherm.
2. Verwijder in tekst 1 het ".be" deel met behulp van de replace methode. Maak van de eerste letter van de overgebleven tekst een hoofdletter. Zet de overgebleven tekst op het scherm.
3. Splits tekst 1 op de punt met behulp van de splits methode. Zet de 2 delen tekst onder elkaar op het scherm.
4. Neem de lengte van tekst 3. Zet tekst 3 op het scherm met de zin " : lengte ..." eraan geplakt.
5. Tel al de spatie en leestekens (.;,:?) in tekst 2 en geef het resultaat in een zin.

### Invoer

3 teksten.

### Uitvoer

* Substring van de teks na de eerste letter i.
* Eerste tekst zonder ".be" en met hoofdletter.
* 2 delen van tekst 1 onder elkaar.        
* Tekst 3 met " : lengte ..." toegevoegd.
* Het aantal spaties en tekens in tekst 2 is ... .

### Voorbeeld

**Invoer**
    
    leemf.be
    Ik woon sinds dit jaar op het adres Brusselsesteenweg 23 1930 Zaventem.
    Programmeren is oplossingsgericht denken.

**Uitvoer**

    k woon sinds dit jaar op het adres Brusselsesteenweg 23 1930 Zaventem.
    Leemf
    leemf
    be
    Programmeren is oplossingsgericht denken.: lengte 41
    Het aantal spaties en tekens in tekst 2 is 12.
   
**Invoer**
    
    z12345.be
    Sinds 2020 is de gasprijs 2 keer duurder geworden.
    Vaak is er niet een standaard oplossing beschikbaar.

**Uitvoer**

    nds 2020 is de gasprijs 2 keer duurder geworden.
    Z12345
    z12345
    be
    Vaak is er niet een standaard oplossing beschikbaar.: lengte 51
    Het aantal spaties en tekens in tekst 2 is 9.

    

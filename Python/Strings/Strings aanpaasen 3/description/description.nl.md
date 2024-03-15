### Opdracht

Schrijf een programma dat:  
- 3 aparte teksten vraagt aan de gebruiker,  
- en de teksten op de volgende manieren wijzigt:

1. Verander de punt "." in tekst 1 door "zavo.".
2. Vervang in tekst 2 elke spatie door " - " met behulp van de split methode.
3. Geef de positie van de eerste letter "e" en eerste letter "t" in tekst 3 onder elkaar. 
4. Geef het deel van tekst 3 tussen de letter "e" en "t", dus na de eerste letter "e" en voor de eerste letter "t".
5. Tel alle cijfers in tekst 2 en geef het resultaat in een zin.
6. Begin tekst 2 met een hoofdletter en verander daarna elke vierde teken die na elkaar volgen ook door een hoofdletter.
Leestekens mogen aan de woorden blijven vastzitten.

### Invoer

3 teksten.

### Uitvoer

* Tekst 1 met "zavo." toegevoegd. 
* Tekst 2 " " vervangen door " - " met de split methode.
* Positie van eerste "e" en eerste "t" in tekst 3.        
* Tekst 3 tussen letter "e" en letter "t
* Het aantal cijfers in tekst 2 is ... .
* Tekst 2 met 1ste en daarna elke 4de letter verandert in een hoofdletter.

### Voorbeeld

**Invoer**
    
    leemf.be
    Ik woon sinds dit jaar op het adres Brusselsesteenweg 23 1930 Zaventem.
    Programmeren is oplossingsgericht denken.

**Uitvoer**

    leemf.zavo.be
    Ik - woon - sinds - dit - jaar - op - het - adres - Brusselsesteenweg - 23 - 1930 - Zaventem.
    8
    32
    ren is oplossingsgerich
    Het aantal cijfers in de tekst is 6.
    Ik wOon SindS diT jaAr oP het adrEs BRussElseSteeNweg 23 1930 ZavEnteM.
   
   
**Invoer**
    
    z12345.be
    Sinds 2020 is de gasprijs 2 keer duurder geworden.
    Vaak is er niet een standaard oplossing beschikbaar.

**Uitvoer**

    z12345.zavo.be
    Sinds - 2020 - is - de - gasprijs - 2 - keer - duurder - geworden.
    8
    14
    r nie
    Het aantal cijfers in de tekst is 5.
    SindS 2020 iS de gasPrijS 2 Keer duuRder gewOrdeN.
    

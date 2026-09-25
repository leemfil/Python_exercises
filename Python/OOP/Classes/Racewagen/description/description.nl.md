# Racewagen

Je maakt een class `Racewagen` waarmee je racewagens tijdens een kwalificatie kunt voorstellen.  
Werk de opdracht stap voor stap af.

## 1. Maak de class
Maak een class `Racewagen`. Elke racewagen heeft drie attributen:
- `naam`
- `snelheid`
- `rondetijd`

Maak daarna deze drie objecten:

wagen1 = Racewagen("Falcon", 280, 74)  
wagen2 = Racewagen("Comet", 280, 70  
wagen3 = Racewagen("Viper", 310, 71)  

### Methode
Voeg een methode versnel(extra) toe.  
Deze methode verhoogt de snelheid van de racewagen met extra.

Voorbeeld:  

    wagen = Racewagen("Falcon", 280, 74)  
    wagen.versnel(15)  
    print(wagen.snelheid)  

De uitvoer moet zijn:  

    295

### Afbeelden
Zorg ervoor dat een racewagen rechtstreeks met print() kan worden afgedrukt.

Voorbeeld:  

    wagen = Racewagen("Falcon", 280, 74)  
    print(wagen)

De uitvoer moet exact zijn: 

    Falcon | snelheid: 280 km/u | rondetijd: 74 s

### Vergelijken
Voor deze opdracht spreken we af dat twee racewagens gelijk zijn wanneer ze dezelfde snelheid hebben.
De naam en de rondetijd spelen hierbij geen rol.
Zorg ervoor dat de operator == volgens deze afspraak werkt.

Voorbeeld:  

    wagen1 = Racewagen("Falcon", 280, 74)  
    wagen2 = Racewagen("Comet", 280, 70)  
    wagen3 = Racewagen("Viper", 310, 71)  
    
    print(wagen1 == wagen2)  
    print(wagen1 == wagen3)

De uitvoer moet zijn:  

    True  
    False
    
### Een duel tussen twee racewagens
We geven ook de operator * een eigen betekenis. Wanneer we twee racewagens met * combineren, rijden ze een duel tegen elkaar. De racewagen met de laagste rondetijd wint.

Voorbeeld:  

    wagen1 = Racewagen("Falcon", 280, 74)  
    wagen2 = Racewagen("Viper", 310, 71)  
    
    print(wagen1 * wagen2)

De uitvoer moet exact zijn:  

    Viper wint!

Wanneer beide racewagens dezelfde rondetijd hebben, is het een gelijkspel.  

    wagen1 = Racewagen("Falcon", 280, 71)  
    wagen2 = Racewagen("Viper", 310, 71)  
    
    print(wagen1 * wagen2)

Uitvoer:  

    Gelijkspel!

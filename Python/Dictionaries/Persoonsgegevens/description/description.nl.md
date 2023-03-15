### Opdracht

Alle gegevens van een persoon worden opgeslagen in een dictionary. We beheren de gegevens zodat ze up-to-date blijven.

Schrijf een programma dat:
* aan de gebruiker volgende gegevens vraagt:  
voornaam, achternaam, echtgenoot, kinderen en huisdieren  
(kinderen is een list en huisdieren zijn 1 list met keys en 1 list met corresponderende values),  
* elke tuple uit de string toevoegt aan de dictionary,  
* de "voornaam" en "achternaam" uit de dictionary haalt en afbeeldt,
* de leeftijd toevoegt aan de dictionary met als key "leeftijd" en als value 50,
* de naam van de "echtgenoot" aanpast naar "Sofia",
* het 2de kind uit de lijst kinderen haalt en afbeeldt,
* de naam van de "hond" uit "huisdieren" haalt en afbeeldt,
* de keys uit de dictionary haalt en afbeeldt,
* de values uit de dictionary haalt en afbeeldt,
* de items uit de dictionary haalt en ze onder elkaar afbeeldt,
* de "geboorteplaats" uit de dictionary haalt met de get() methode en afbeeldt,
* de naam van de echtgenoot verwijdert uit de dictionary en deze naam afbeeldt,
* de hele dictionary afbeeldt. 

### Invoer

* voornaam
* achternaam
* naam van echtgenoot
* lijst met kinderen
* lijst met keys voor huisdieren
* lijst met corresponderende namen voor huisdieren

### Uitvoer

* voornaam achternaam
* naam van 2de kind
* naam van de hond
* keys
* values
* items onder elkaar
* geboorteplaats
* naam echtgenoot
* hele dictionary

### Voorbeeld

**Invoer**

    Ilyas
    Arbib
    Ava
    ['Ralph', 'Betty', 'Joey']
    ['hond', 'kat']
    ['Fido', 'Sox']

**Uitvoer**
    
    Ilyas Arbib  
    Betty
    Fido
    dict_keys(["voornaam", "achternaam", "echtgenoot", "kinderen", huisdieren", "leeftijd"])  
    dict_values(["Ilyas", "Arbib", "Ava", ["Ralph", "Betty", "Joey"], {"hond": "Fido", "kat": "Sox"}, 50])
    ("voornaam", "Ilyas")  
    ("achternaam", "Arbib")  
    ("echtgenoot", "Ava")  
    ("kinderen", ["Ralph", "Betty", "Joey"])  
    ("huisdieren", {"hond": "Fido", "kat": "Sox"})
    ("leeftijd", 50)
    None
    Sofia
    {"voornaam":"Ilyas", "achternaam": "Arbib", "kinderen": ["Ralph", "Betty", "Joey"],  
    "huisdieren": {"hond": "Fido", "kat": "Sox", "leeftijd": 50}}

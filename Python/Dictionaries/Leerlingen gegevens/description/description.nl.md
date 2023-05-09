### Opdracht

Alle gegevens van een leerling worden opgeslagen in een dictionary.  
We beheren de gegevens zodat ze up-to-date blijven.

Schrijf een programma dat:
* aan de gebruiker volgende gegevens vraagt:  
* voornaam, achternaam, gewicht en hobbies 
(hobbies worden gegeven in één string gescheiden door een spatie),  
* beeldt alle informatie uit de dictionary met behulp van een lus,  
* de "voornaam" en "achternaam" uit de dictionary haalt en afbeeldt,
* het geboortejaar toevoegt aan de dictionary en de standwaarde 2006 invult en afbeeldt,
* het geboortejaar aanpast naar 2007 en afbeeldt,
* de eerste hobby uit de lijst afbeeldt,
* 5,0 kg toevoegt aan het gewicht en afbeeldt.

### Invoer

* voornaam
* achternaam
* gewicht
* hobbies

### Uitvoer

* voornaam  
  achternaam
* gewicht
* lijst van hobbies
* voornaam achternaam
* 
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
    Ralph Betty Joey
    hond kat
    Fido Sox

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

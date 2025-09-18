## Opdracht
<br>

Je beheert een **boodschappenlijst**. We willen een functie schrijven die een basislijst aanvult, dubbele voorkomt en eventueel een product verwijdert.

Schrijf een **functie** `beheer_boodschappen(basis, extra, index)` met drie parameters:

- `basis`: een lijst van str, de bestaande boodschappen.  
- `extra`: een lijst van str, nieuwe producten die toegevoegd moeten worden.  
- `index`: een geheel getal, de **positie** van een product dat verwijderd moet worden (0-gebaseerd). Als het getal ongeldig is (te groot of negatief), wordt er niets verwijderd.  

De functie werkt als volgt:

1. Maak een nieuwe lege lijst `resultaat`.  
2. Voeg alle elementen van `basis` toe.  
3. Voeg de elementen van `extra` toe, maar **alleen als ze nog niet in de lijst zitten**.  
4. Als `index` geldig is, verwijder je dat element met die `ìndex`.  
5. Sorteer de lijst **omgekeerd alfabetisch**.  
6. Geef de aangepaste lijst **terug**.  

---

## Voorbeelden

    >>> beheer_boodschappen(["melk", "brood"], ["kaas", "brood"], 1)
    ["melk", "kaas"]

    >>> beheer_boodschappen([], ["appels", "bananen"], 0)
    ["bananen"]

    >>> beheer_boodschappen(["tomaten", "komkommer"], ["sla"], -1)
    ["tomaten", "sla", "komkommer"]

    >>> beheer_boodschappen(["water"], ["sap"], 5)
    ["water", "sap"]

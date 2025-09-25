## Opdracht
<br>

Je beheert de **catalogus** van een bibliotheek als een lijst van **boekentitels** (strings). Dubbels (meerdere exemplaren van dezelfde titel) zijn toegestaan.

Schrijf een **functie** `beheer_bibliotheek(basis, index_verwijderen, titel_verwijderen)` met drie parameters:

- `basis`: `lijst[str]` — de oorspronkelijke lijst boekentitels.  
- `index_verwijderen`: `int` — de **positie** van een element dat verwijderd moet worden. Als de index ongeldig is (negatief of te groot), verwijder je niets.  
- `titel_verwijderen`: `str` — de titel waarvan je **één** exemplaar wil verwijderen. Als de titel niet voorkomt, doe je niets.  

De functie werkt als volgt:

1. Maak een nieuwe lege lijst `resultaat`.  
2. Kopieer met een **for-lus** alle elementen van `basis` naar `resultaat` (gebruik `.append()`).  
3. Als `index_verwijderen` geldig is, verwijder dat element met de index `index_verwijderen`.  
4. Als `titel_verwijderen` voorkomt in de lijst, verwijder dat exemplaar.  
5. Sorteer `resultaat` **omgekeerd alfabetisch**.  
6. Retourneer `resultaat`.  

---

## Voorbeelden

    >>> beheer_bibliotheek(["Dune", "It", "Foundation"], 1, "Dune")
    ["It", "Foundation"]

    >>> beheer_bibliotheek(["Solaris", "Ubik"], 5, "Ubik")
    ["Solaris"]

    >>> beheer_bibliotheek(["1984"], 0, "Brave New World")
    []

    >>> beheer_bibliotheek(["A", "B", "C"], -3, "X")
    ["C", "B", "A"]

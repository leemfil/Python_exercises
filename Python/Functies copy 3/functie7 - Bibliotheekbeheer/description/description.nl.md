## Opdracht
<br>

Je beheert de **catalogus** van een bibliotheek als een lijst van **boekentitels** (strings). Dubbels (meerdere exemplaren van dezelfde titel) zijn toegestaan.

Schrijf een **functie** `beheer_bibliotheek(basis, te_verwijderen, nieuw, index)` met vier parameters:

- `basis`: `list[str]` — de oorspronkelijke lijst boekentitels (dubbels toegestaan).  
- `te_verwijderen`: `str` — de titel waarvan je **één** exemplaar wil verwijderen (als die voorkomt).  
- `nieuw`: `str` — de nieuwe titel die je wil toevoegen.  
- `index`: `int` — de **positie** waar je `nieuw` wil invoegen. Als de index ongeldig is (negatief of groter dan de lengte), voeg je `nieuw` **achteraan** toe.  

De functie werkt als volgt:

1. Maak een nieuwe lege lijst `resultaat`.  
2. Kopieer met een lus alle elementen van `basis` naar `resultaat`.  
3. **Als** `te_verwijderen` in `resultaat` zit, verwijder dan **één** voorkomen; **anders doe je niets**.  
4. Sorteer `resultaat` **omgekeerd alfabetisch**.  
5. Voeg `nieuw` in als de index geldig is, **anders** voeg je `nieuw` achteraan toe.  
6. **Retourneer** `resultaat`.

## Voorbeelden

    >>> beheer_bibliotheek(["Dune", "It", "It"], "It", "Foundation", 1)
    ["It", "Foundation", "Dune"]

    >>> beheer_bibliotheek(["Solaris", "Neuromancer"], "Hyperion", "Ubik", 5)
    ["Ubik", "Solaris", "Neuromancer"]

    >>> beheer_bibliotheek(["1984"], "1984", "Brave New World", 0)
    ["Brave New World"]

    >>> beheer_bibliotheek(["A", "B", "C"], "X", "Z", -3)
    ["Z", "C", "B", "A"]

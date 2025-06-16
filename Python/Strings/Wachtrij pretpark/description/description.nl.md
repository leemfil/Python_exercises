### Opdracht

In het pretpark Funlandia wordt de wachtrij voor een achtbaan digitaal beheerd. Bezoekers sluiten zich aan vooraan of achteraan, afhankelijk van hun tickettype. Ook kunnen personen op een bepaalde positie uit de rij worden verwijderd door de bewaking.

Je schrijft **een functie** `beheer_rij(rij, actie, index, naam)` die het wachtrijsysteem beheert.

#### Parameters

- `rij`: een lijst van strings met de namen van personen in de rij
- `actie`: een string met één van de volgende waarden:
  - `"toevoegen"`
  - `"verwijderen"`
- `index`: 
  - Als `actie == "toevoegen"` →  index = `0` → vooraan, `-1` → achteraan
  - Als `actie == "verwijderen"` → een geheel getal: de index van de te verwijderen persoon
- `naam`: 
  - Als `actie == "toevoegen"` →  waarde die moet toegevoegd worden
  - Als `actie == "verwijderen"` → `None` want heeft dan geen toepassing

#### Gedrag

- Als `"toevoegen"`:
  - Voeg de naam toe vooraan of achteraan op basis van de index (0 of -1)
- Als `"verwijderen"`:
  - Verwijder het element op de opgegeven index
  - Als de index ongeldig is, dan return je de boodschap: "Ongeldige index!"

#### Retourwaarde

- Bij `"verwijderen"` retourneert de functie de naam van de verwijderde persoon, of `None` bij fout
- Bij `"toevoegen"` retourneert de functie `None`  
<br/>

---

### Voorbeelden

    >>> rij = ["Luna", "Arne"]
    >>> beheer_rij(rij, "toevoegen", 0, "Noor")
    >>> rij
    ['Noor', 'Luna', 'Arne']

    >>> beheer_rij(rij, "toevoegen", -1, "Ella")
    >>> rij
    ['Noor', 'Luna', 'Arne', 'Ella']

    >>> beheer_rij(rij, "verwijderen", 1, None)
    'Luna'
    >>> rij
    ['Noor', 'Arne', 'Ella']

    >>> beheer_rij(rij, "verwijderen", 10, None)
    >>> rij
    'Ongeldige index!'

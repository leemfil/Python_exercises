## Opdracht
<br>
Schrijf een **functie** `zoek_of_voeg_toe(lijst, waarde)` die werkt als volgt:

- Als `waarde` **voorkomt** in `lijst`: **geef de eerste index** (0-gebaseerd) **terug**.
- Als `waarde` **niet voorkomt**: **voeg** `waarde` **achteraan** toe met `.append()` en **geef de nieuwe lijst terug**.

> Let op:
> - De functie **print niets**; ze **retourneert** een resultaat (een `int` of een `list`).
> - Werk op de meegegeven lijst wanneer je toevoegt.

<br>

## Voorbeelden

  >>> zoek_of_voeg_toe([3, 7, 9, 2, 7], 7)  
  1  
  
  Als de waarde niet voorkomt, wordt ze toegevoegd en krijg je de aangepaste lijst terug:  
  >>> zoek_of_voeg_toe([10, 20, 30], 5)  
  [10, 20, 30, 5]  
  
  Lege lijst:  
  >>> zoek_of_voeg_toe([], 42)  
  [42]
  
  Dubbele waarden → eerste index:  
  >>> zoek_of_voeg_toe([5, 5, 5, 2, 5, 9], 5)  
  0

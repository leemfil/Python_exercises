## Opdracht
<br>
Schrijf een **functie** `plaats_element(lijst, waarde)` die:

<br>  

1. de **waarde** eerst **achteraan** toevoegt,  
2. daarna dezelfde **waarde ook vooraan** plaatst,  
3. en de **aangepaste lijst teruggeeft**.

> Let op: de functie **retourneert** de lijst, ze **print niets**.

---

## Voorbeelden

    ```python
    >>> plaats_element([10, 20, 30], 5)  
    [5, 10, 20, 30, 5]
    
    >>> plaats_element([], 7)  
    [7, 7]

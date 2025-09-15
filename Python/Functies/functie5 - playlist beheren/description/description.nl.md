## Opdracht
<br>

Je beheert een **playlist** (lijst van strings) met nummers.  
Schrijf een **functie** `beheer_playlist(playlist, nieuw, verboden, max_grootte)` die deze stappen uitvoert:

1. Voeg het nummer `nieuw` **achteraan** toe met `.append()`.  
2. **Sorteer** de lijst **case-insensitive** met `.sort(key=str.lower)`.  
3. **Keer om** met `.reverse()` zodat de volgorde **omgekeerd-alfabetisch** is (Z → A).  
4. **Verwijder** met `.remove(verboden)` het **eerste** voorkomen van `verboden` **als** het (nog) aanwezig is.  
5. Als de lijst **langer** is dan `max_grootte`, **verwijder** dan het **laatste** element met `.pop()` **zolang** de lengte te groot is.  
6. **Retourneer** de aangepaste playlist.

> Voorbeeld-redenering: na stap 2–3 staat het **beste** (alfabetisch hoogst) vooraan.  
> Bij stap 5 verwijderen we telkens het **laatste** element: dat is dan het **zwakste** item.

## Voorbeelden

    >>> beheer_playlist(["Zebra", "apple", "Monkey"], "Track", "Monkey", 4)
    ["Zebra", "Track", "apple"]

    >>> beheer_playlist(["a", "b", "c"], "d", "x", 3)
    ["d", "c", "b"]

    >>> beheer_playlist(["Rock", "Pop"], "pop", "Pop", 3)
    ["pop", "Rock"]

    >>> beheer_playlist(["x", "Y", "z"], "A", "z", 2)
    ["Y", "x"]

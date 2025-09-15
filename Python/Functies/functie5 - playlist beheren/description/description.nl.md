## Opdracht
<br>

We werken met een **playlist** van muzieknummers (strings).  
Schrijf een **functie** `sorteer_playlist(playlist)` die:  

1. de lijst `playlist` **alfabetisch sorteert**,  
2. daarna de lijst **omkeert**,  
3. en de aangepaste lijst **retourneert** (dus in **omgekeerd-alfabetische volgorde**).  

> Context:  
> Stel dat een DJ zijn playlist eerst alfabetisch ordent om het overzicht te bewaren,  
> maar daarna beslist om alles **achterstevoren** af te spelen.  

---

## Voorbeelden

    >>> sorteer_playlist(["Zebra", "Apple", "Monkey"])
    ["Zebra", "Monkey", "Apple"]

    >>> sorteer_playlist(["SongA", "SongB", "SongC"])
    ["SongC", "SongB", "SongA"]

    >>> sorteer_playlist([])
    []

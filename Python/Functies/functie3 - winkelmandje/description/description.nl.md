## Opdracht
<br>
Schrijf een **functie** `bewerking_winkelmand(mand, index, artikel)` die twee stappen uitvoert op de lijst `mand`:

1. **Verwijder** het element op positie `index` en onthoud het **verwijderde** element.  
2. **Verwijder** het **eerste** voorkomen van `artikel` **indien** het (nog) in de mand zit.  

De functie **retourneert** een lijst met twee elementen:  
`[verwijderde_waarde, aangepaste_mand]`

<br>

> Let op:
> - Werk op de meegegeven lijst `mand`.  
> - Je mag ervan uitgaan dat `index` geldig is (binnen het bereik van de lijst).  
> - Als `artikel` niet in de mand zit na de verwijdering, laat je de mand verder **ongewijzigd**.

<br>
## Voorbeelden

        >>> bewerking_winkelmand(["brood", "melk", "kaas"], 1, "kaas")
        ["melk", ["brood"]]   
        
        # eerst ["brood","kaas"]; daarna "kaas" verwwijderen -> ["brood"]
        # Opletten: eerst waarde teruggeven; de tweede component is de mand NA alle bewerkingen:
 
        >>> bewerking_winkelmand(["appel", "peer", "banaan"], 0, "druif")
        ["appel", ["peer", "banaan"]]   # "druif" komt niet voor, dus geen 2de verwijdering

        >>> bewerking_winkelmand(["a", "b", "a", "c"], 3, "a")
        ["c", ["b", "a"]]   
        
        # Volledige redenering:
        # start: ["a","b","a","c"]
        # verwijder artikel op index 3 -> mand = ["a","b","a"]
        # verwijder het 1ste artikel -> mand = ["b","a"]

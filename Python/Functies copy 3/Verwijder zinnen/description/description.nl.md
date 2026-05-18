### Opdracht

Bij tekstverwerking moeten we dikwijls een deel van een tekst aanpassen.  
Om deze taak makkelijker te maken schrijven een functie die de laatste woorden uit een tekst verwijdert.  

Schrijf een functie verwijder_laatste_woorden die:
- als invoer een tekst en een getal n krijgt,
- het eerste deel van de tekst selecteert door de laatste n woorden te verwijderen,
- het geselecteerde deel teruggeeft.

### Voorbeelden 
    tekst = "Python, een krachtige en veelgebruikte programmeertaal met een eenvoudige syntax en een uitgebreide set bibliotheken,  
    heeft de harten van ontwikkelaars wereldwijd veroverd vanwege zijn brede toepassingsgebieden."
    
    >>> verwijder_laatste_woorden(tekst, 11)  
    Python, een krachtige en veelgebruikte programmeertaal met een eenvoudige syntax en een uitgebreide set bibliotheken.

    >>> verwijder_laatste_woorden(tekst, 4)  
    Python, een krachtige en veelgebruikte programmeertaal met een eenvoudige syntax en een uitgebreide set bibliotheken,  
    heeft de harten van ontwikkelaars wereldwijd veroverd.

### Opdracht

Bij tekstverwerking moeten we dikwijls een deel van een tekst selecteren en kopiëren. Om deze taak makkelijker te maken schrijven een functie.  

Schrijf een functie die:
- als invoer een tekst en een getal n krijgt,
- het eerste deel van de tekst selecteert door de laatste n zinnen te verwijderen,
- het geselecteerde deel teruggeeft.

### Voorbeelden 
    tekst = "Het is maandagochtend. De wekker gaat. Ik rek me uit. Koffiegeur vult de lucht.   
    Brood kraakt onder mijn tanden. De trein komt eraan. Mensen haasten zich. De stad ontwaakt.  
    Auto's toeteren. De lucht is grijs."
    
    >>> verwijder_laatste_zinnen(tekst, 2)  
    Het is maandagochtend. De wekker gaat. Ik rek me uit. Koffiegeur vult de lucht.  
    Brood kraakt onder mijn tanden. De trein komt eraan. Mensen haasten zich. De stad ontwaakt.

    >>> verwijder_laatste_zinnen(tekst, 4)  
    Het is maandagochtend. De wekker gaat. Ik rek me uit. Koffiegeur vult de lucht.  
    Brood kraakt onder mijn tanden. De trein komt eraan.

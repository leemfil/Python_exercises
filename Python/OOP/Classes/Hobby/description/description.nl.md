### Classes en objecten (Hobby)
**Situatie**  
Je gaat een klein programma schrijven rond een hobby naar keuze (bv. basketbal, gamen, naaien, muziek maken, lezen, …).
 Je gebruikt één eigen class en maakt daar minstens twee objecten van aan.

**Opdracht**  
Schrijf een Python-programma waarin je:  
1. Een class definieert voor jouw hobby
    - Kies zelf een passende naam voor de class (bv. Sport, Game, Boek, Instrument, …).
    - De class moet minstens 2 attributen hebben.
       - Voorbeelden van mogelijke attributen (afhankelijk van je hobby):
          - sport: naam, aantal_spelers, speellocatie
          - game: titel, genre, speeltijd_uren
          - boek: titel, auteur, aantal_paginas
          - instrument: naam, soort, moeilijkheidsgraad
    - De class moet een dunder-methode hebben die een duidelijke tekst teruggeeft met alle belangrijke informatie over het object (dus niet gewoon print in de class, maar echt return "...").  
  
2. Objecten aanmaakt
      - Maak minstens 2 objecten van je class aan met verschillende waarden voor de attributen.
         - bv. twee verschillende boeken, twee verschillende games, twee verschillende teams, …  
  
3. Alle info op het scherm toont
      - Toon de informatie van beide objecten op een nette manier op het scherm.
      - Zorg dat alle attributen van de objecten ergens zichtbaar zijn in de uitvoer.  
  
4. Overload de + operator
      - Voeg een __add__-methode toe aan je class.
      - Bedenk zelf wat het betekent om twee objecten van jouw class op te tellen.
         - Enkele ideeën:  
              Bij games: som van de speeltijd van twee games.  
              Bij boeken: totaal aantal pagina’s van twee boeken.  
              Bij teams: totaal aantal spelers.
      - Toon in je programma ook één voorbeeld waarbij je twee objecten optelt en het resultaat print op een duidelijke manier (bv. "Samen hebben deze twee boeken 560 pagina's.").

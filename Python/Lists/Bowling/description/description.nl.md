
<br>  
<div class="dodona-centered-group"><img src="media/bowling.png" width="600" height="300"></div>
<br>
  
Bij bowling is het de bedoeling om met een bal op een baan van kunststof of hout de 10 kegels, ook wel pins genoemd, aan de andere kant van de baan om te gooien met een zogenaamde bowlingbal. De pins worden in een driehoek geplaats met 1 pin voorop, daarachter 2 dan 3 en de laatste lijn heeft 4 pins.

#### Spelverloop

Elke bowlingpartij bestaat uit tien beurten (frames) per speler. Men krijgt per frame 2 beurten om alle pins om te gooien. Elke pin is 1 punt waard, maar er zijn bonuspunten te verdienen als je een strike of een spare haalt.  
<br>
Als bij de eerste worp alle pins om worden gegooid heeft die speler een strike gegooid en stopt de beurt direct.  
<br>
Als alle pins in 2 worpen omvallen heeft men een spare gegooid. Ook als bij de eerste worp 0 pins omvallen en pas bij de tweede worp in één keer 10 pins, is het nog steeds een spare en geen strike.  
<br>
Als een speler in twee worpen niet alle 10 de pins omkrijgt spreek je van een open frame.

#### Puntentelling

Als je een strike gooit, dan heb je 10 punten verdiend van de 10 pins die je omvert gegooid hebt en krijgt je nog eens 10 punten extra. Je krijgt dus in totaal 20 punten omdat je alle pins in één keer hebt omgegooit.   
<br>
Als je een spare gooit, dan heb je ook 10 punten gehaald, en dan krijg je nog eens 5 punten extra. Je krijgt dus in totaal 15 punten omdat je alle pins in twee pogingen hebt omgegooit.  
<br>
Gooi je een open frame (dus niet alles om na twee beurten, dan heb je alleen de punten gescoord van het aantal pins dat je hebt omgegooid. Dit is dan dus altijd minder dan 10. En je krijgt geen bonuspunten.

### Opdracht

<ol>
  <li>Schrijf een functie <samp>`puntenspel`</samp> waaraan 1 parameter wordt doorgegeven:<br>
    <ul><li>een string met 20 getallen gescheiden een spatie.</li></ul>
        <br>
        De 20 getallen komen overeen met de omvergeworpen pins van 10 frames want we werpen 2 keer per frame.
    <br><br>
   Bereken het totaal van de 10 frames zonder rekening te houden met strikes of spares en return een string met het resultaat.<br>
   Gebruik hiervoor volgende zin:<br><br>
   <blockquote>
        “Je hebt 10 frames gespeeld met volgend resultaat: <br>
        frame 1: &lt;punten frame 1&gt;<br>
        frame 2: &lt;punten frame 2&gt;<br>
        …<br>
        frame 10: &lt;punten frame 10&gt;<br>
        totaal: &lt;totaal aantal punten&gt;”
  </blockquote>  
  Op de plaatsen van de <...> zet je telkens het overeenkomstig getal.
  </li><br>
  
  <li>Schrijf een nieuwe functie <samp>`puntenframes`</samp> waaraan 1 parameter wordt doorgegeven:<br>
    <ul><li>een string met een even aantal getallen gescheiden door een spatie, dus het aantal frames kan variëren.</li></ul>
    <br>
    Bereken het totaal van het aantal frames en houdt rekening met strikes en spares. <br>
    Een strike levert 20 punten op en een spare 15 punten. <br>
    Gooide je een strike in een frame dan is het 2de getal van dat frame 0.<br>
    Return deze keer volgende zin:<br><br>
   <blockquote>
        “Je hebt 10 frames gespeeld met volgend resultaat: &lt;punten frame 1&gt; + &lt;punten frame 2&gt; + … + &lt;punten frame 10&gt; = &lt;totaal aantal punten&gt;”
  </blockquote>  
  Op de plaatsen van de <...> zet je telkens het overeenkomstig getal.

  </li>
</ol>


### Voorbeeld

    >>> puntenspel("3 5 6 4 3 0 6 1 7 2 8 2 10 0 9 0 0 3 0 10")
    Je hebt 10 frames gespeeld met volgend resultaat:
    frame1: 8
    frame 2: 10
    frame 3: 3
    frame 4: 7
    frame 5: 9
    frame 6: 10
    frame 7: 10
    frame 8: 9
    frame 9: 3
    frame 10: 10
    totaal: 79

    >>> puntenspel("2 4 0 10 7 0 10 0 2 3 8 1 7 3 9 1 5 5 4 4")
    Je hebt 10 frames gespeeld met volgend resultaat:
    frame1: 6
    frame 2: 10
    frame 3: 7
    frame 4: 10
    frame 5: 5
    frame 6: 9
    frame 7: 10
    frame 8: 10
    frame 9: 10
    frame 10: 8
    totaal: 85
    
    >>> puntenframes("4 6 0 10 4 3 10 0")
    62
    
    >>> puntenframes("9 1 5 3 8 0 0 5 10 0 6 4 0 0")
    71

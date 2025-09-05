## Opdracht
<br>
We maken een eenvoudig **raadspel**:

- Het **geheime getal** is vastgelegd op `7`.
- De gebruiker krijgt **maximaal 3 pogingen** om het getal te raden.
- Na elke poging:
  - Als de gok **juist** is → print `Juist!` en stop het spel.
  - Als de gok **te klein** is → print `Hoger!`.
  - Als de gok **te groot** is → print `Lager!`.
- Als de gebruiker **na 3 pogingen** het getal niet gevonden heeft, print:
Helaas, het was 7.

---

## Invoer
- Tot 3 gehele getallen (één per regel).

## Uitvoer
- Voor elke poging: een feedbackregel (`Juist!`, `Hoger!`, `Lager!`).
- Indien binnen 3 pogingen niet geraden: een slotregel
Helaas, het was 7.

---

## Voorbeelden

**Voorbeeld 1**

**Invoer**  
7

**Uitvoer**  
Juist!

---

**Voorbeeld 2**

**Invoer**  
5  
9  
7

**Uitvoer**  
Hoger!  
Lager!  
Juist!  

---

**Voorbeeld 3**

**Invoer**  
5  
6  
8

**Uitvoer**  
Hoger!  
Hoger!  
Lager!  
Helaas, het was 7.

## Opdracht
<br>
Schrijf een programma dat **een score vraagt** en blijft vragen **tot de invoer geldig is**:
- De score moet een **getal** zijn (kommagetal of geheel getal).
- De score moet tussen **1 en 10** liggen (grenzen inbegrepen).

Wanneer een **geldige score** is ingevoerd, print het programma **één regel**:
Geldige score: X
waarbij `X` de ingevoerde score is (als getal).

> Opmerking:
> - Bij ongeldige invoer (tekst, buiten bereik, leeg, …) blijft je programma **verder vragen** tot een geldige score is gelezen.
> - Bekijk de functie isinstance() om te checken of een waarde van het type int of float is.

---

## Invoer  
Eén of meerdere regels tekst. Elke regel is een poging tot score. Het programma stopt zodra een **geldige score** (1 ≤ score ≤ 10) is ingevoerd.

## Uitvoer  
Eén regel:
Geldige score: X

---

## Voorbeelden

**Voorbeeld 1**

**Invoer**  
7

**Uitvoer**  
Geldige score: 7.0

---

**Voorbeeld 2**

**Invoer**  
abc
0
10

**Uitvoer**  
Geldige score: 10.0

---

**Voorbeeld 3**

**Invoer**  
3.5

**Uitvoer**  
Geldige score: 3.5

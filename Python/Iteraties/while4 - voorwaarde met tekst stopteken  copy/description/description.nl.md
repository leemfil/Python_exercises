## Opdracht
<br>

Schrijf een programma dat **getallen blijft inlezen** (één per regel) en deze optelt tot de gebruiker het **woord `stop`** invoert.  
De tekst **`stop`** is het **stopteken (sentinel)** en **wordt niet mee opgeteld**. De vergelijking met `stop` is **hoofdletterongevoelig** (dus `STOP`, `Stop`, … tellen ook).

- Getallen mogen **geheel** of **kommagetallen** zijn.
- Na het stoppen print het programma exact **één regel**:
Totaal: X
waarbij `X` de som is van alle ingegeven getallen (als **kommagetal**).

---

## Invoer
Een reeks regels met getallen, beëindigd door een regel met `stop` (hoofdletterongevoelig).

## Uitvoer
Eén regel:
Totaal: X

---

## Voorbeelden

**Voorbeeld 1**

**Invoer**  
1  
2  
3  
stop

**Uitvoer**  
Totaal: 6.0

---

**Voorbeeld 2**

**Invoer**  
2.5  
3.25  
STOP

**Uitvoer**  
Totaal: 5.75

---

**Voorbeeld 3**

**Invoer**  
stop

**Uitvoer**  
Totaal: 0.0

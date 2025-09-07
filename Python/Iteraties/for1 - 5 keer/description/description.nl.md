## Opdracht
<br>
Schrijf een programma dat een **eenvoudig menu** verwerkt tot de gebruiker **`0`** kiest (sentinel om te stoppen).

De keuzes zijn:
- `1` → print: `2 + 2 = 4`
- `2` → print: `5 - 3 = 2`
- `0` → print: `Tot ziens!` en **stop**
- eender iets anders → print: `Ongeldige keuze.`

> Opmerking:
> - Spaties rond de invoer mogen genegeerd worden.

---

## Invoer
Een reeks regels met keuzes (`1`, `2`, `0`, …).  
Het programma **stopt** wanneer `0` gelezen is.

## Uitvoer
Per keuze **exact één regel**:
- `2 + 2 = 4` *(bij keuze `1`)*
- `5 - 3 = 2` *(bij keuze `2`)*
- `Ongeldige keuze.` *(bij andere invoer)*
- Afsluitend **exact één keer**: `Tot ziens!` *(bij `0`)*

---

## Voorbeelden

**Voorbeeld 1**

**Invoer**  
1  
2  
0  

**Uitvoer**  
2 + 2 = 4  
5 - 3 = 2  
Tot ziens!  

---

**Voorbeeld 2**

**Invoer**  
3  
x  
0  

**Uitvoer**  
Ongeldige keuze.  
Ongeldige keuze.  
Tot ziens!  

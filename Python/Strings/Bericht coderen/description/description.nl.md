### Opdracht

3️⃣ FASE 3: Zend een gecodeerd tegenbericht
Nu je de vijandelijke communicatie hebt ontcijferd, is het tijd om zelf te antwoorden. Uiteraard versleutel je jouw boodschap, zodat niemand anders de inhoud kan lezen.

Je gebruikt een eenvoudige versleuteling op basis van ASCII. Elke letter wordt vervangen door het volgende teken in de ASCII-tabel. Er gelden uitzonderingen voor de tekens "z" en "Z" — deze worden vervangen door een speciaal teken.

🔐 Let op:

"z" → "*"

"Z" → "+"

Alle andere karakters (zoals cijfers, leestekens, spaties, …) blijven behouden.


**🛠️ Schrijf een programma dar het volgende doet:**

- Vraag een bericht aan de gebruiker.
- Zet elke letter om naar het volgende ASCII-teken.
- Verwerk "z" als "*", "Z" als "+".
- Laat alle andere tekens ongewijzigd.
- Toon het versleutelde bericht.  

---

### Invoer

Een tekstbericht met hoofdletters, kleine letters en andere tekens.

---

### Uitvoer

De versleutelde tekst waarbij elke letter volgens bovenstaande regels werd vervangen.

---

### Voorbeeld

**Invoer**

    Zorro zegt: “Welkom, agent Z!”

**Uitvoer**

    +pssp* afhui: “Xfmmpn, bhfou +!”

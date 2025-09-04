# While 03 — Sentinelwaarde (-1) om te stoppen

totaal = 0.0
waarde = float(input("Geef eerste getal: "))

while waarde != -1:
    totaal += waarde
    waarde = float(input("Geef het volgend getal: "))

print(f"Totaal: {totaal}")

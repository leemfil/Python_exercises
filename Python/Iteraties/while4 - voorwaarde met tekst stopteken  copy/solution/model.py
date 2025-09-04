# While 04 — Sentinel met tekst ('stop')

totaal = 0.0

while True:
    lijn = input("Geef een getal: ").strip()
    if lijn.lower() == "stop":
        break
    # veronderstel geldige getallen in de evaluatie
    waarde = float(lijn)
    totaal += waarde

print(f"Totaal: {totaal}")

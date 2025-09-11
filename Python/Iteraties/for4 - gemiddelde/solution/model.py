# For 03 — Som en gemiddelde (met invoer)

n = int(input("Geef het aantal getallen: ").strip())
totaal = 0.0

for _ in range(n):
    waarde = float(input("Geef het volgend getal: ).strip())
    totaal += waarde

gemiddelde = totaal / n
print(f"Som: {totaal}")
print(f"Gemiddelde: {gemiddelde}")

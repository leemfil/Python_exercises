# Parkeermeter — while + gemiddelde parkeertijd

sessies = 0
bruto = 0.0
totaal_uren = 0

uren = int(input().strip())  # eerste aantal uren

while uren != -1:
    # basistarief
    if uren <= 0:
        prijs = 0.0
    elif uren <= 2:
        prijs = 3.0 * uren
    elif uren <= 5:
        prijs = 2.0 * uren
    else:
        prijs = 12.0

    bruto += prijs
    totaal_uren += uren
    sessies += 1

    uren = int(input().strip())

gemiddelde = (totaal_uren / sessies) if sessies > 0 else 0.0

print(f"Aantal sessies: {sessies}")
print(f"Brutobedrag: {bruto:.1f} euro")
print(f"Gemiddelde tijd: {gemiddelde:.1f} uur")

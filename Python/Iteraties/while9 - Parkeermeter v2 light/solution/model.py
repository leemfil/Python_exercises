# Parkeermeter — while + if/else met toeslagen

sessies = 0
bruto = 0.0
toeslag = 0.0

uren = int(input().strip())  # eerste aantal uren

while uren != -10:
    # basistarief
    if uren <= 0:
        prijs = 0.0
    elif uren <= 2:
        prijs = 3.0 * uren
    elif uren <= 5:
        prijs = 2.0 * uren
    else:
        prijs = 12.0

    # zonecode (kan leeg zijn)
    code = input().strip().lower()

    # toeslag bepalen
    t = 0.0
    if code == "centrum":
        t = 0.15 * prijs
    elif code == "overdekt" and prijs > 0.0:
        t = 1.0
    # anders: geen toeslag

    # totalen bijwerken
    bruto += prijs
    toeslag += t
    sessies += 1

    # volgende sessie
    uren = int(input().strip())

# samenvatting
print(f"Aantal sessies: {sessies}")
print(f"Brutobedrag: {bruto:.1f} euro")
print(f"Toeslag: {toeslag:.1f} euro")
print(f"Te betalen: {bruto + toeslag:.1f} euro")

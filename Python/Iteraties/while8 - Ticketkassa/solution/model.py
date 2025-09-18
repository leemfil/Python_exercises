# Ticketkassa

tickets = 0
bruto = 0.0
korting = 0.0

leeftijd = int(input(Geef je leeftijd: ).strip())

while leeftijd != -1:
    # basisprijs
    if leeftijd < 3:
        prijs = 0.0
    elif leeftijd <= 11:
        prijs = 6.0
    elif leeftijd <= 64:
        prijs = 12.0
    else:
        prijs = 8.0

    # kortingscode inlezen
    code = input("Geef de kortingscode).strip().lower()

    # korting berekenen
    korting_bedrag = 0.0
    if code == "student" and prijs == 12.0:
        korting_bedrag = 0.20 * prijs
    elif code == "pas" and prijs > 0:
        korting_bedrag = 1.0

    bruto += prijs
    korting += korting_bedrag
    tickets += 1

    # volgende leeftijd vragen
    leeftijd = int(input("Geef de volgende leeftijd: ).strip())

# samenvatting printen
print(f"Aantal tickets: {tickets}")
print(f"Brutobedrag: {bruto:.1f} euro")
print(f"Korting: {korting:.1f} euro")
print(f"Te betalen: {bruto - korting:.1f} euro")

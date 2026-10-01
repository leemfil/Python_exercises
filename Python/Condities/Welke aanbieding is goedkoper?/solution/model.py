aantal_a = int(input("Aantal stuks in aanbieding A: "))
prijs_a = float(input("Prijs per stuk in aanbieding A: "))
aantal_b = int(input("Aantal stuks in aanbieding B: "))
prijs_b = float(input("Prijs per stuk in aanbieding B: "))

totaal_a = aantal_a * prijs_a
totaal_b = aantal_b * prijs_b

goedkoper = totaal_a < totaal_b

print(goedkoper)
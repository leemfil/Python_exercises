naam = input("Geef je naam: ")
aantal_per_rij = int(input("Hoeveel foto's komen er op één rij? "))
pakketgrootte = int(input("Hoeveel foto's zitten er in één pakket? "))
prijs = float(input("Wat kost één foto? "))

aantal_fotos = aantal_per_rij ** 2
totale_prijs = aantal_fotos * prijs
volledige_pakketten = aantal_fotos // pakketgrootte
losse_fotos = aantal_fotos % pakketgrootte

print(naam + " maakt een fotomuur met " + str(aantal_fotos) + " foto's.")
print("Totale prijs:", totale_prijs, "euro")
print("Volledige pakketten:", volledige_pakketten)
print("Losse foto's:", losse_fotos)

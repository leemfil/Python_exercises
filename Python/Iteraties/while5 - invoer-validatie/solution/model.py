# While 02b — Doel kiezen vóór de lus (modeloplossing)

# Lees de keuze
keuze = input("Kies het doel 100 of 20: g (groot) of k (klein)")

# Bepaal het doel op basis van de keuze
if keuze == 'k':
    doel = 20
else:
    doel = 100  # 'g' of elke andere waarde

som = 0
while som < doel:
    getal = int(input("Geef het volgend getal: "))
    som += getal

print(f"Doel bereikt: som = {som} (>= {doel})")

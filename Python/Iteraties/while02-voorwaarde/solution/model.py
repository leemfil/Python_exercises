# While 02 — Voorwaarde-gestuurd optellen (modeloplossing)

doel = 100
som = 0

while som < doel:
    getal = int(input("Geef een volgend getal: "))
    som += getal

print(f"Doel bereikt: som = {som} (>= {doel})")

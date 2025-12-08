# dictionary maken
huisdier = {}

# basisgegevens
huisdier["naam"] = input().strip()
huisdier["leeftijd"] = int(input().strip())

# vaccins verzamelen
vaccins = []
aantal = int(input().strip())
for _ in range(aantal):
    vaccins.append(input().strip())

huisdier["vaccins"] = vaccins

# extra vaccin (optioneel)
extra = input().strip()
if extra != "":
    huisdier["vaccins"].append(extra)

# overzicht
print(huisdier["naam"])
print(huisdier["leeftijd"])
for v in huisdier["vaccins"]:
    print(v)

# check ras helemaal op het einde
print(huisdier.get("ras", "Er is geen ras geregistreerd voor dit huisdier."))

activiteit = input("Geef de eerste activiteit: ")

activiteiten = []
while activiteit != "einde":
    if activiteit in activiteiten:
        activiteit += "2"
    activiteiten.append(activiteit)

    activiteit = input("Geef de volgende activiteit: ")
print(activiteiten)

tv_lijst = []
for activiteit in activiteiten:
    if activiteit[0].lower() == "t" or activiteit[0].lower() == "v":
        tv_lijst.append(activiteit)
print(tv_lijst)

pos_festival = activiteiten.index("festival")
print(f"De plaats van festival is {pos_festival + 1}.")

lijst_met_a = []
lijst_zonder_a = []
for activiteit in activiteiten:
    if "a" in activiteit:
        lijst_met_a.append(activiteit)
    else:
        lijst_zonder_a.append(activiteit)
print(lijst_met_a)
print(lijst_zonder_a)

activiteiten.insert(2, "wandelen")
print(activiteiten)

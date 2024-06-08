aantal = int(input("Geef hat aantal woorden: "))

activiteit = ""
activiteiten = []
for index in range(aantal):
    activiteit = input("Geef het volgende woord: ")
    if activiteit not in activiteiten:
        activiteiten.append(activiteit)
print(activiteiten)

lijst_zonder_t = []
for activiteit in activiteiten:
    if "t" not in activiteit.lower():
        lijst_zonder_t.append(activiteit)
print(lijst_zonder_t)

pos_uitstap = activiteiten.index("uitstap")
print(f"De plaats van uitstap is {pos_uitstap + 1}.")

lijst_met_oe = []
lijst_zonder_oe = []
for activiteit in activiteiten:
    if activiteit[1] == "e" or activiteit[1] == "o":
        lijst_met_oe.append(activiteit)
    else:
        lijst_zonder_oe.append(activiteit)
print(lijst_met_oe)
print(lijst_zonder_oe)

activiteiten.pop(2)
print(activiteiten)

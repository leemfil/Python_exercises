attracties = ["Achtbaan", "Spookhuis", "Reuzenrad", "Wildwaterbaan", "Botsauto's"]


# Stap 1: Attractie toevoegen
toevoegen = input()

if toevoegen.lower() == "ja":
    plaats = int(input())
    naam = input()

    attracties.insert(plaats - 1, naam)
    print(f"De aangepaste planning is {attracties}.")
else:
    print(f"De planning is {attracties}.")


# Stap 2: Plaats van een attractie zoeken
gezochte_attractie = input()

if gezochte_attractie in attracties:
    plaats = attracties.index(gezochte_attractie) + 1
    print(f"De attractie {gezochte_attractie} staat op plaats {plaats}.")
else:
    print("Deze attractie staat niet in de lijst!")


# Stap 3: Voormiddagplanning maken
helft = (len(attracties) + 1) // 2
voormiddagplanning = attracties[:helft]

print(f"De voormiddagplanning is: {voormiddagplanning}")

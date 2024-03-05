aantal = int(input("Geef het aantal woorden: "))

woorden_lijst = []
for woord in range(aantal):
    woord = input("Geef het volgende woord: ")
    woorden_lijst.append(woord)
print(woorden_lijst)

woorden_lijst.sort()
print(woorden_lijst)

print(woorden_lijst[0])

lijst_meer_dan_5 = []
lijst_minder_dan_5 = []
for woord in woorden_lijst:
    if len(woord) > 5:
        lijst_meer_dan_5.append(woord)
    else:
        lijst_minder_dan_5.append(woord)
print(lijst_meer_dan_5)
print(lijst_minder_dan_5)

print(lijst_meer_dan_5 + lijst_minder_dan_5)

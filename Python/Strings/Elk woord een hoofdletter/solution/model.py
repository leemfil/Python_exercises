# Eerste letter van elk woord hoofdletter maken

tekst = input().strip()

woorden = tekst.split()
resultaat = []

for woord in woorden:
    nieuw_woord = woord[0].upper() + woord[1:]
    resultaat.append(nieuw_woord)

print(" ".join(resultaat))

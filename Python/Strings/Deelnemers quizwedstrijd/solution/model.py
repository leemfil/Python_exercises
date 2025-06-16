# Inlezen namen in één regel en splitsen naar lijst
deelnemers = input().split()

# Aantal afmeldingen
afmeldingen = int(input())

for _ in range(afmeldingen):
    afwezige = input()
    vervanger_ja_of_nee = input().strip().lower()
    if vervanger_ja_of_nee == "ja":
        vervanger = input()
        index = deelnemers.index(afwezige)
        deelnemers[index] = vervanger
    else:
        deelnemers.remove(afwezige)

# Sorteer de lijst
deelnemers.sort()

# Toon aangepaste lijst als komma-gescheiden string
print(", ".join(deelnemers))

# Zoek een deelnemer op
gezocht = input()
if gezocht in deelnemers:
    index = deelnemers.index(gezocht)
    print(f"De deelnemer {gezocht} staat op index {index}.")
else:
    print(f"{gezocht} zit niet meer in de lijst.")

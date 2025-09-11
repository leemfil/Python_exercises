# For 05 — Eerste even getal zoeken

n = int(input("Geef het aantal getallen: ").strip())
getallen = []

# vul de lijst met append
for _ in range(n):
    waarde = int(input("Geef het volgend getal: ").strip())
    getallen.append(waarde)

gevonden = False
for g in getallen:
    if g % 2 == 0:
        print(f"Eerste even getal: {g}")
        gevonden = True
        break

if not gevonden:
    print("Geen even getal gevonden")

# Spel — Strafpunten berekenen

spelers = ["Emma", "Lucas", "Noor", "Liam", "Mila"]

for i in range(len(spelers)):
    naam = spelers[i]
    strafpunten = (i + 1) * 2
    print(f"{naam} heeft {strafpunten} strafpunten verzameld.")

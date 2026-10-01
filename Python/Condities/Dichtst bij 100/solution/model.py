score1 = int(input("Score van speler 1: "))
score2 = int(input("Score van speler 2: "))

afstand1 = (score1 - 100) ** 2
afstand2 = (score2 - 100) ** 2

dichterbij = afstand1 < afstand2

print(dichterbij)
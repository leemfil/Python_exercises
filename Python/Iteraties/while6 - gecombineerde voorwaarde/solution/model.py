# While 06 — Raadspel met beperkte pogingen (modeloplossing)

geheim = 7
pogingen = 0
max_pogingen = 3
geraden = False

while pogingen < max_pogingen and not geraden:
    gok = int(input("Doe een gok: "))
    pogingen += 1

    if gok == geheim:
        print("Juist!")
        geraden = True
    elif gok < geheim:
        print("Hoger!")
    else:
        print("Lager!")

if not geraden:
    print(f"Helaas, het was {geheim}.")

# While 08 — Menu met sentinel (modeloplossing)

while True:
    keuze = input().strip()
    if keuze == "1":
        print("2 + 2 = 4")
    elif keuze == "2":
        print("5 - 3 = 2")
    elif keuze == "0":
        print("Tot ziens!")
        break
    else:
        print("Ongeldige keuze.")

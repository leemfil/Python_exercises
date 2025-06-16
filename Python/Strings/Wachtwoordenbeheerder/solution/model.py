aantal = int(input("Geef het aantal wachtwoorden in: "))
wachtwoorden = []

for _ in range(aantal):
    ww = input("Geef een wachtwoord in: ")
    if ww not in wachtwoorden:
        wachtwoorden.append(ww)

wachtwoorden.sort(key=len)
wachtwoorden.reverse()

print(",".join(wachtwoorden))

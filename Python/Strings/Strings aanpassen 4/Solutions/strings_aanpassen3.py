tekst1 = input("Geef tekst 1: ")
tekst2 = input("Geef tekst 2: ")
tekst3 = input("Geef tekst 3: ")

pos_i = tekst2.find("i")
print(tekst2[pos_i + 1:])

substring1 = tekst1.replace(".be", "").capitalize()
print(substring1)

voornaam, domein = tekst1.split(".")
print(voornaam)
print(domein)

lengte = len(tekst3)
print(tekst3 + f": lengte {lengte}")

teller = 0
for letter in tekst2:
    if letter in " .,;:?":
        teller += 1

print(f"Het aantal spaties en tekens in tekst 2 is {teller}.")


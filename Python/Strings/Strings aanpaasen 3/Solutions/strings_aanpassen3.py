tekst1 = input("Geef tekst 1: ")
tekst2 = input("Geef tekst 2: ")
tekst3 = input("Geef tekst 3: ")

samengevoegd = tekst2 + " " + tekst3
print(samengevoegd)

pos_punt = tekst1.find(".")
substring1 = tekst1[:pos_punt]
substring2 = tekst1[pos_punt + 1:]
print(substring1.capitalize())
print(substring2.capitalize())

pos_spatie = tekst2.find(" ")
eerste_woord = tekst2[:pos_spatie]
print(f"{eerste_woord} heeft een lengte van {len(eerste_woord)}.")

zonder_spaties = tekst3.replace(" ", "")
print(zonder_spaties)

teller = 0
for letter in tekst2:
    if letter in "aeiou":
        teller += 1

print(f"Het aantal klinkers in tekst 2 is {teller}.")

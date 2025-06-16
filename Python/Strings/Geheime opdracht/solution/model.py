boodschap = input()

# Bouw string op met tekens op oneven indexen
decode = ""
for i in range(1, len(boodschap), 2):
    decode += boodschap[i]

# Zet alles om naar kleine letters
decode = decode.lower()

# Vervang '#' door spatie
decode = decode.replace("#", " ")

# Toon de decodeerde boodschap
print(decode)

# Zoek het woord 'agent' in de decodeerde string
aantal = decode.count("agent")

# Toon aantal keren 'agent' voorkomt
if aantal > 0:
    print(f"Patroon 'agent' komt {aantal} keer voor.")
else:
    print("Patroon 'agent' niet gevonden.")

# Tel aantal letters zonder spaties
letters_zonder_spaties = len(decode.replace(" ", ""))
print(f"De boodschap bevat {letters_zonder_spaties} letters zonder spaties.")

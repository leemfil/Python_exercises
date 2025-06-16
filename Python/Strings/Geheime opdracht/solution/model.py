gecodeerd = input()
codewoord = input().lower()

# 1. Bouw de string op met tekens op oneven posities
decode = ""
for i in range(1, len(gecodeerd), 2):
    decode += gecodeerd[i]

# 2. Alles in kleine letters + vervang '#' door spatie
decode = decode.lower().replace("#", " ")

# 3. Toon de decodeerde boodschap
print(decode)

# 4. Tel hoe vaak het codewoord voorkomt
aantal = decode.count(codewoord)
print(f"Patroon '{codewoord}' komt {aantal} keer voor.")

# 5. Tel aantal letters zonder spaties
zonder_spaties = decode.replace(" ", "")
print(f"De boodschap bevat {len(zonder_spaties)} letters zonder spaties.")

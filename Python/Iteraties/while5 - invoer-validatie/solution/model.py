# While 05 — Invoer-validatie (score 1–10)

score = None

while True:
    try:
        lijn = input().strip()
        # Lege regel overslaan
        if lijn == "":
            continue
        waarde = float(lijn)
        if 1 <= waarde <= 10:
            score = waarde
            break
        # Buiten bereik -> opnieuw proberen
    except ValueError:
        # Geen getal -> opnieuw proberen
        continue

print(f"Geldige score: {score}")

# Boodschappenlijst

def beheer_boodschappen(basis, extra, index):
    resultaat = []

    # 1. basis kopiëren
    for product in basis:
        resultaat.append(product)

    # 2. extra toevoegen indien nog niet aanwezig
    for product in extra:
        if product not in resultaat:
            resultaat.append(product)

    # 3. element op index verwijderen als index geldig is
    if 0 <= index < len(resultaat):
        resultaat.pop(index)

    # 4. sorteren in omgekeerde alfabetische volgorde
    resultaat.sort(reverse=True)

    return resultaat

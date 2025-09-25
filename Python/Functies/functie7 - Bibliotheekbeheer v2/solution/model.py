# Bibliotheekbeheer 

def beheer_bibliotheek(basis, index_verwijderen, titel_verwijderen):
    resultaat = []

    # 1) basis kopiëren
    for titel in basis:
        resultaat.append(titel)

    # 2) verwijderen met pop indien index geldig
    if 0 <= index_verwijderen < len(resultaat):
        resultaat.pop(index_verwijderen)

    # 3) verwijderen met remove indien titel aanwezig
    if titel_verwijderen in resultaat:
        resultaat.remove(titel_verwijderen)

    # 4) sorteren in omgekeerde alfabetische volgorde
    resultaat.sort(reverse=True)

    return resultaat

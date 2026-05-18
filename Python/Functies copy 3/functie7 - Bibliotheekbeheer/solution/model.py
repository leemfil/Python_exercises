# Bibliotheekbeheer — verwijderen, omgekeerd sorteren en invoegen

def beheer_bibliotheek(basis, te_verwijderen, nieuw, index):
    resultaat = []

    # 1) basis kopiëren met for + append
    for titel in basis:
        resultaat.append(titel)

    # 2) één exemplaar verwijderen indien aanwezig
    if te_verwijderen in resultaat:
        resultaat.remove(te_verwijderen)

    # 3) omgekeerd alfabetisch sorteren
    resultaat.sort(reverse=True)

    # 4) invoegen op index (of achteraan bij ongeldige index)
    if 0 <= index <= len(resultaat):
        resultaat.insert(index, nieuw)
    else:
        resultaat.append(nieuw)

    # 5) aangepaste lijst teruggeven
    return resultaat

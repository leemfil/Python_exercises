def aanpassen(woordenlijst):
    woordenlijst.reverse()

    nieuwe_lijst = []
    for woord in woordenlijst:
        if len(woord) <= 6:
            nieuwe_lijst.append(woord)
    
    return nieuwe_lijst

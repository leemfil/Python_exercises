def selecteer(woordenlijst):
    woordenlijst.sort()
    
    nieuwe_lijst = []
    for woord in woordenlijst:
        if len(woord) > 5:
            nieuwe_lijst.append(woord)
    
    return nieuwe_lijst

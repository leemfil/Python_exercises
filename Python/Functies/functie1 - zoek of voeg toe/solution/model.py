# Lijsten 01 — Zoek of voeg toe (index + append)

def zoek_of_voeg_toe(lijst, waarde):
    """
    Als waarde in lijst zit -> return eerste index (int).
    Anders -> voeg waarde toe aan het einde en return de (aangepaste) lijst.
    """
    if waarde in lijst:
        return lijst.index(waarde)
    else:
        lijst.append(waarde)
        return lijst


# Lijsten 01 — Zoek of voeg toe (index + append)

def zoek_of_voeg_toe(lijst, waarde):
    """
    Als waarde in lijst zit -> return eerste index (int).
    Anders -> voeg waarde toe aan het einde en return de (aangepaste) lijst.
    """
    try:
        return lijst.index(waarde)
    except ValueError:
        lijst.append(waarde)
        return lijst

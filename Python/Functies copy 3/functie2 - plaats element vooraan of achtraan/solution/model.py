# Lijsten 02 — Plaats element vooraan of achteraan

def plaats_element(lijst, waarde):
    """
    Voegt waarde eerst achteraan toe met append,
    daarna ook vooraan met insert(0, waarde).
    Retourneert de aangepaste lijst.
    """
    lijst.append(waarde)
    lijst.insert(0, waarde)
    return lijst

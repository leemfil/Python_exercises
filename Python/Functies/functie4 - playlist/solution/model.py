# Lijsten 03 — Winkelmand-bewerkingen (pop + remove) — modeloplossing

def bewerking_winkelmand(mand, index, artikel):
    """
    1) pop(index) -> onthoud gepopte waarde
    2) als artikel in mand: remove(artikel)
    retourneer [gepopte_waarde, mand]
    """
    gepopt = mand.pop(index)
    if artikel in mand:
        mand.remove(artikel)
    return [gepopt, mand]

def beheer_rij(rij, actie, waarde):
    if actie == "toevoegen":
        naam, index = waarde
        if index == 0:
            rij.insert(0, naam)
        elif index == -1:
            rij.append(naam)
    elif actie == "verwijderen":
        index = waarde
        if 0 <= index < len(rij):
            return rij.pop(index)
        else:
            return "Ongeldige index!"
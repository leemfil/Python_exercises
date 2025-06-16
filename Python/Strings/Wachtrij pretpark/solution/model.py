def beheer_rij(rij, actie, index, naam):
    if actie == "toevoegen":
        if index == 0:
            rij.insert(0, naam)
        elif index == -1:
            rij.append(naam)
        return rij
    elif actie == "verwijderen":
        if 0 <= index < len(rij):
            return rij.pop(index)
        else:
            return "Ongeldige index!"

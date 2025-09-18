# Lijsten 06 — Playlist manager (alles combineren)

def beheer_playlist(playlist, nieuw, verboden, max_grootte):
    """
    1) append(nieuw)
    2) sort(key=str.lower)  # case-insensitive oplopend
    3) reverse()            # omgekeerd-alfabetisch (Z->A)
    4) indien verboden aanwezig: remove(verboden)
    5) while len(playlist) > max_grootte: pop()  # verwijder laatste (zwakste)
    6) return playlist
    """
    # 1
    playlist.append(nieuw)
    # 2
    playlist.sort(key=str.lower)
    # 3
    playlist.reverse()
    # 4
    if verboden in playlist:
        playlist.remove(verboden)
    # 5
    while len(playlist) > max_grootte:
        playlist.pop()
    # 6
    return playlist

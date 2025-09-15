# Lijsten 04 — Playlist sorteren en omkeren

def sorteer_playlist(playlist):
    """
    Sorteer alfabetisch, keer daarna om.
    Retourneer de aangepaste lijst (omgekeerd-alfabetisch).
    """
    playlist.sort()
    playlist.reverse()
    return playlist

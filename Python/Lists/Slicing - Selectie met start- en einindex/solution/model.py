# Slicing 06 — Selectie met start- en eindindex

fruitmand = ["appel", "banaan", "kiwi", "peer", "mango", "druif", "kers"]

start = int(input("Geef de startindex: ").strip())
einde = int(input("Geef de eindindex: ").strip())

resultaat = fruitmand[start:einde]

print(resultaat)

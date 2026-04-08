# Woorden omwisselen met find()

tekst = input().strip()

positie = tekst.find(" ")

woord1 = tekst[:positie]
woord2 = tekst[positie + 1:]

nieuw = woord2 + " " + woord1

print(nieuw)

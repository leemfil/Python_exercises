# For 02b — Range met grenzen en stap

start = int(input("Geef de startwaarde: ").strip())
stop = int(input("Geef de stopwaarde: ").strip())
stap = int(input("Geef de stapgrootte: ").strip())

if stap < 0:
    stop -= 1
else:
    stop += 1
    
for getal in range(start, stop, stap):
    print(getal)

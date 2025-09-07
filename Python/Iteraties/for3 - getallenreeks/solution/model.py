# For 02b — Range met grenzen en stap

start = int(input("Geef de startwaarde: ").strip())
stop = int(input("Geef de stopwaarde: ").strip())
stap = int(input("Geef de stapgrootte: ").strip())

for i in range(start, stop, stap):
    print(i)

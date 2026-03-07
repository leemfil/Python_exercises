# Ingrediëntenlijst aanpassen

ingrediënten = ["tomaat", "komkommer", "paprika", "ui", "sla", "wortel"]

del ingrediënten[len(ingrediënten) - 1]

deel = ingrediënten[:4]

deel.sort()

print(deel)

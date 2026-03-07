# Automerken opsplitsen op basis van lengte

merken = ["Audi", "Volvo", "Toyota", "Kia", "Renault", "Subaru"]

lijst1 = []
lijst2 = []

for merk in merken:
    if len(merk) > 5:
        lijst2.append(merk)
    else:
        lijst1.append(merk)

print(f"De merken met 5 letters of minder zijn {lijst1}.")
print(f"De merken met meer dan 5 letters zijn {lijst2}.")

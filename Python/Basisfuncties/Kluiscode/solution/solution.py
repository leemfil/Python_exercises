code = int(input("Geef een code van twee cijfers: "))

tiental = code // 10
eenheid = code % 10

controlescore = tiental ** 2 + eenheid ** 2

print("Cijfers:", tiental, eenheid)
print("Controlescore:", controlescore)

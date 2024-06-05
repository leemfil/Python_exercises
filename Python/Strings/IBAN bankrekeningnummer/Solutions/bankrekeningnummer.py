bankrekeningnummer = input("Geef het bankrekeningnummer: ")

delen = bankrekeningnummer.split()

for deel in delen:
    print(deel)

eerste2 = bankrekeningnummer[:2]
laatste2 = bankrekeningnummer[-2:]

print(f"De landcode is {eerste2}.")

verborgen = eerste2 + "*" * (len(bankrekeningnummer) -4) + laatste2

print(f"De verborgen bankrekening is {verborgen}.")

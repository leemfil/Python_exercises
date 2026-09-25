class Racewagen:
    def __init__(self, naam, snelheid, rondetijd):
        self.naam = naam
        self.snelheid = snelheid
        self.rondetijd = rondetijd

    def versnel(self, extra):
        self.snelheid += extra

    def __str__(self):
        return f"{self.naam} | snelheid: {self.snelheid} km/u | rondetijd: {self.rondetijd} s"

    def __eq__(self, other):
        return self.snelheid == other.snelheid

    def __mul__(self, other):
        if self.rondetijd < other.rondetijd:
            return f"{self.naam} wint!"
        elif self.rondetijd > other.rondetijd:
            return f"{other.naam} wint!"
        else:
            return "Gelijkspel!"


wagen1 = Racewagen("Falcon", 280, 74)
wagen2 = Racewagen("Comet", 280, 70)
wagen3 = Racewagen("Viper", 310, 71)

print(wagen1)
print(wagen2)
print(wagen3)

wagen3.versnel(25)
print(wagen3.snelheid)

print(wagen1 == wagen2)
print(wagen1 == wagen3)

print(wagen1 * wagen3)

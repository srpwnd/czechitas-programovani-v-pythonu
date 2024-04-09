# Vrať se k návrhu software pro zásilkovou společnost.
# U třídy Package uprav atribut state tak, aby byl chráněný.
# Ověř, že vytváření objektů i výpisy informací o něm fungují.


class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self._state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self._state}"

    @property
    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <= 20:
            return 159
        else:
            return 359

    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen"
        else:
            self._state = "doručen"
            return "Právě jsem doručil balík"


balik_1 = Package("Česká 12, Brno", 25.4, "nedoručen")

print(balik_1)

print(f"Cena baliku je {balik_1.delivery_price}")

print(balik_1.deliver())
print(balik_1.deliver())

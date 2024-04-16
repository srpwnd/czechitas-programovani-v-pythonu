# Uprav třídu Package na datovou třídu. Třída bude mít atributy address, weight, a state. U každého z atributů vymysli a nastav vhodný datový typ. Existující metody ve třídě ponech.

# Následně vyzkoušej, zda funguje vytváření balíků. A co cenné balíky, fungují pořád, i když dědí od datové třídy?

from dataclasses import dataclass


@dataclass
class Package:
    address: str
    weight: float
    _state: str

    # def __str__(self):
    #     return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self._state}."

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


@dataclass
class ValuablePackage(Package):
    value: int

    # def __str__(self):
    #     return super().__str__() + f" Má hodnotu {self.value} Kč a pojistné {self._insurance_fee}"

    @property
    def _insurance_fee(self):
        return self.value * 0.05

    @property
    def delivery_price(self):
        return super().delivery_price + self._insurance_fee


balik_1 = Package("Česká 12, Brno", 25.4, "nedoručen")

print(balik_1)

balik_2 = ValuablePackage("Tyršova 11, Praha", 2, "nedoručen", 1500)

print(balik_2)
print(f"{balik_2.delivery_price=}")

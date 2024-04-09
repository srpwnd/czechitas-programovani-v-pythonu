# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

#     - Rozšiř metodu __init__ třídy Employee o parametr probation_period.
#       Tuto hodnotu ulož jako atribut třídy Employee.
#     - Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době,
#       přidej k jeho/jejímu výpisu text Je ve zkušební době.


class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def __str__(self):
        probation = " a je ve zkušební době" if self.probation_period else ""
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}{probation}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return "Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."


frantisek = Employee("František Novák", "konstruktér", 25, True)
print(frantisek)

amelie = Employee("Amelie Novak", "CEO", 100, False)
print(amelie)

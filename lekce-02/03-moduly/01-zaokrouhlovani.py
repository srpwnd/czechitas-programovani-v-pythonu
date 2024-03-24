# Napište program, který dostane na vstupu desetinné číslo 
# a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, 
# potom dolů a potom běžným Pythonovským zaokrouhlováním.

import math

number = float(input("Zadej desetinne cislo (s teckou): "))

print(f"Zaokrouhlene nahoru: {math.ceil(number)}")
print(f"Zaokrouhlene dolu: {math.floor(number)}")
print(f"Bezne zaokrouhleni: {round(number)}")
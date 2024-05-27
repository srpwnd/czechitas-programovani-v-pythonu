num1 = float(input("Zadej prvni cislo: "))

num2 = float(input("Zadej druhe cislo: "))

try:
    vysledek = num1 / num2
    print(f"Vysledek je {vysledek}")
except ZeroDivisionError:
    print("Nulou dělit nelze.")

# if num2 != 0:
#     vysledek = num1 / num2
#     print(f"Vysledek je {vysledek}")
# else:
#     print("Nulou dělit nelze.")

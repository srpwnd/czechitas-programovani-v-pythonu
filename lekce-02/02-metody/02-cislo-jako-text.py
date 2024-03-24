# Mějme seznam celých čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']

# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:
# hodnoty = ['12', '1', '11', '-11']

print(hodnoty)

cislo = int(hodnoty[2]) + 4
hodnoty[2] = str(cislo)

print(hodnoty)

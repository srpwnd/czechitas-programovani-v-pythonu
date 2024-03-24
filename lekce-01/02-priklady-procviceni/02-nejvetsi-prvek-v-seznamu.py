# Napiš kód, který zpracuje seznam čísel
# a vypíše největší prvek v tomto seznamu
# (bez použití funkce max()).

numbers = [1, 2, 3]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"Nejvetsi prvek v seznamu je {largest}")

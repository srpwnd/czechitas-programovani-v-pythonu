# Napiš kód, který zpracuje seznam čísel 
# a vypíše pouze sudá čísla z tohoto seznamu.

numbers = [1, 2, 3, 4]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(str(num))

print(f"Suda cisla v seznamu jsou: {', '.join(even_numbers)}")
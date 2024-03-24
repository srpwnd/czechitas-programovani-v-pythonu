# Napiš kód, který zpracuje seznam čísel
# a vytvoří nový seznam se sudými čísly
# a nový seznam s lichými čísly z původního seznamu.

numbers = [1, 2, 3, 4]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))

print(f"Suda cisla v seznamu jsou: {', '.join(even_numbers)}")
print(f"Licha cisla v seznamu jsou: {', '.join(odd_numbers)}")

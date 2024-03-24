# Napiš kód, který zpracuje seznam
# a vytvoří nový seznam bez duplikátů.
# Výsledné pořadí prvků musí být zachováno.

numbers = [1, 2, 2, 3, 3, 3]

deduplicated = []

for num in numbers:
    if num not in deduplicated:
        deduplicated.append(num)

print(f"Deduplikovana cisla jsou: {deduplicated}")

# Uvažujme vysvědčení studenta, které máme uložené jako seznam.

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru.
# Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika.
# Vypočítej průměr studenta z daných předmětů s využitím modulu statistics.
# Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů.
# Nakonec použij metodu statistics.mean() k výpočtu průměru. Dále zkus využít funkce, které jsou zmíněné v textu,
# k výpočtu nejlepší a nejhorší známky z daných předmětů.

import statistics

grades = []

for subject in school_report:
    if subject[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
        grades.append(subject[1])

print(f"Prumer je: {statistics.mean(grades)}")

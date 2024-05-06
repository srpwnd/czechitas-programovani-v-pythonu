with open("lekce-09/vykaz.txt", encoding="utf-8") as file:
    vykaz = [int(line) for line in file]

hodinovka = float(input("Zadej hodinovou sazbu: "))

celkova_vyplata = sum(vykaz) * hodinovka
print(f"celkova vyplata {celkova_vyplata}")

prumer = celkova_vyplata / len(vykaz)
print(f"prumer: {prumer}")

vyplaty = []
for index, hours in enumerate(vykaz):
    vyplata = hours * hodinovka
    vyplaty.append(vyplata)


with open("mesicni_vyplaty.txt", "w") as file:
    for index, salary in enumerate(vyplaty):
        file.write(f"{index + 1}. mesic: {salary:.2f}\n")

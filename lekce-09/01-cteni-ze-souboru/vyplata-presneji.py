with open("lekce-09/vykaz.txt", encoding="utf-8") as file:
    print(file.read())
    vykaz = [int(line) for line in file]

hodinovka = float(input("Zadej hodinovou sazbu: "))

celkova_vyplata = sum(vykaz) * hodinovka
print(f"celkova vyplata {celkova_vyplata}")

prumer = celkova_vyplata / len(vykaz)
print(f"prumer: {prumer}")

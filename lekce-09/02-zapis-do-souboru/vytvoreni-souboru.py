filename = input("Zadej nazev souboru: ")

text = input("Zadej text k zapsani: ")

with open(filename, mode="w", encoding="utf-8") as output:
    print(text, file=output)

knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]

try:
    index = int(input("Zadej index knihy: "))
    print(knihy[index])
except IndexError:
    print("Zadal jsi index mimo rozsah")

# if index < len(knihy)
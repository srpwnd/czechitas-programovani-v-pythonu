pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("kalendar.txt", mode="w", encoding="utf-8") as file:
    for item in pocty_dni:
        print(item, file=file)
        # file.write(f"{item}\n")

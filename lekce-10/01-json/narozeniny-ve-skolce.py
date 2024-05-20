import csv
from datetime import datetime

class_birthdays = {}

with open("lekce-10/kids.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=["name", "class", "birthdate"])
    for row in reader:
        class_name = row["class"]
        child_name = row["name"]
        birth_month = datetime.strptime(row["birthdate"], "%d. %m. %Y").month

        if class_name not in class_birthdays:
            class_birthdays[class_name] = {}

        if birth_month not in class_birthdays[class_name]:
            class_birthdays[class_name][birth_month] = []

        class_birthdays[class_name][birth_month].append(child_name)


for class_name, months in class_birthdays.items():
    with open(f"{class_name}.txt", "w", encoding="utf-8") as file:
        file.write(f"Třída {class_name}\n")
        for month, names in sorted(months.items()):
            file.write(f"{month}: ")
            names_print = ", ".join(names)
            file.write(f"{names_print}\n")

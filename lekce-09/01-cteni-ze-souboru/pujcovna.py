total_kilometers = 0

with open("lekce-09/auta.txt", "r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.replace(",", ".").strip()
        spz, kilometers = clean_line.split()

        total_kilometers += float(kilometers)

print(f"Celkovy pocet kilometru: {total_kilometers * 1000} km")

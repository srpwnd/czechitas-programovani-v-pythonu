from datetime import datetime

datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")

if datum_narozeni[4] == "-" and datum_narozeni[-3] == "-":
    parts = datum_narozeni.split("-")
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        datum_narozeni = datetime.fromisoformat(datum_narozeni)
        print(datum_narozeni)
    except ValueError:
        print("Nejedna se o cisla")
else:
    print("Spatny format!")




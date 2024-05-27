file_path = "lekce-11/balance.txt"

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        account_balance = float(file.read())
except FileNotFoundError:
    print("Soubor neexistuje")
except ValueError:
    print("Soubor neobsahuje číslo")
except Exception as err:
    print(err)
else:
    print(f"Hodnota na ucte je {account_balance}")

    try:
        amount = float(input("Zadej castku k převedení: "))

        if amount < 0:
            raise ValueError("Částka nesmí být záporná.")
        if amount > account_balance:
            raise ValueError("Na účtu není dostatek peněz.")
    except ValueError as err:
        print(err)
    except Exception as err:
        print(f"Neocekavany error: {err}")
    else:
        account_balance -= amount

        try:
            with open(file_path, mode="w", encoding="utf-8") as file:
                file.write(f"{account_balance}\n")
        except Exception as err:
            print(f"Chyba pri zapisu do souboru: {err}")
        else:
            print(f"Castka uspesne zapsana. Nova castka na ucte je {account_balance}")

tasks_list = []

try:
    with open("lekce-11/tasks.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            tasks_list.append(line.split(","))
except FileNotFoundError:
    print("Soubor neexistuje, bude vytvořen.")
finally:
    task_text = input("Zadej nazev ukolu: ")

    try:
        task_priority = int(input("Zadej prioritu 1-3: "))
        if task_priority not in (1,2,3):
            raise ValueError("Chybna priorita. Muze byt pouze 1-3")
    except ValueError as err:
        print(f"Chyba hodnoty: {err}")
    else:
        tasks_list.append([task_text, task_priority])
        try:
            with open("lekce-11/tasks.txt", mode="w", encoding="utf-8") as output:
                for task, prio in tasks_list:
                    output.write(f"{task},{prio}\n")
        except Exception as err:
            print(f"Neocekavana chyba pri zapisu souboru: {err}")
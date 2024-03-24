# Následující tabulka obsahuje průměrné roční teploty v České republice za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).
# rok 	teplota °C
# 2001 	7.8
# 2002 	8.7
# 2003 	8.2
# 2004 	7.8
# 2005 	7.7
# 2006 	8.2
# 2007 	9.1
# 2008 	8.9
# 2009 	8.4
# 2010 	7.2

# Vytvořte reprezentaci této tabulky pomocí seznamu seznamů. Zde existují dvě možnosti. Nejprve vytvořte seznam, který obsahuje řádky tabulky jako dvouprvkové seznamy a uložte jej do proměnné radky. Poté vytvořte seznam, který obsahuje sloupce tabulky, tedy dva seznamy po deseti prvcích. Uložte jej do proměnné sloupce.

# Pro obě tyto reprezentace vyřešte následující úkoly

#     Získejte teplotu na třetím řádku tabulky.
#     Získejte rok na pátém řádku tabulky.
#     Získejte poslední řádek tabulky jako seznam.
#     Vytvořte tabulku bez prvních dvou řádků.
#     Vytvořte tabulku pouze z prvních dvou řádků.
#     Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
#     Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.

radky = [
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
]

sloupce = [
    [2001, 2002, 2003, 2004, 2005, 2005, 2007, 2008, 2009, 2010],
    [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]
]

print(f"Teplota na tretim radku: {radky[4][1]} a {sloupce[1][4]}")

print(f"Rok na patem radku: {radky[6][0]} a {sloupce[0][6]}")

print(f"Posledni radek tabulky: {radky[-1]} a {[sloupce[0][-1], sloupce[1][-1]]}")

radky_bez_prvnich_dvou = radky[2:]

sloupce_bez_prvnich_dvou = [sloupce[0][2:], sloupce[1][2:]]

print(f"Tabulka bez prvnich dvou radku: {radky_bez_prvnich_dvou} a {sloupce_bez_prvnich_dvou}")

radky_jen_prvni_dva = radky[:2]

sloupce_jen_prvni_dva = [sloupce[0][:2], sloupce[1][:2]]

print(f"Tabulka jen prvni dva radky: {radky_jen_prvni_dva} a {sloupce_jen_prvni_dva}")

radky_vyrez = radky[4:8]

sloupce_vyrez = [sloupce[0][4:8], sloupce[1][4:8]]

print(f"Tabulka vyrez: {radky_vyrez} a {sloupce_vyrez}")

print(f"Serazene teploty: {sorted(sloupce[1])}")
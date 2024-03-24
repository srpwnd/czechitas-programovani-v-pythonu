# Máme data o písemce, která obsahovala 4 otázky. Za každou otázku mohl student (studentka) získat max. 10 bodů. Výsledky studentů jsou v následující tabulce.
# Student 	Otázka 1 	Otázka 2 	Otázka 3 	Otázka 4
# A 	9 	7 	8 	5
# B 	5 	3 	6 	6
# C 	8 	4 	9 	7
# D 	8 	5 	4 	8
# E 	10 	6 	10 	7

# Ulož si známky studentů do dvourozměrného seznamu.

# Spočítej známku jednotlivých studentů. Známku urči podle celkového počtu bodů ze všech příkladů. Bodovací tabulku najdeš níže.
# Body 	Známka
# 36 a více 	1
# 32 a více 	2
# 26 a více 	3
# 20 a více 	4
# méně než 20 	5

# Vypočítej průměrné body z jednotlivých otázek. Ze které otázky dostali studenti v průměru nejvíce bodů? A ze které naopak nejméně?

points = [
    ['A' , 9 , 7 , 8 , 5],
    ['B' , 5 , 3 , 6 , 6],
    ['C' , 8 , 4 , 9 , 7],
    ['D' , 8 , 5 , 4 , 8],
    ['E' , 10 , 6 , 10 , 7]
]

grades = []

for student in points:
    total = sum(student[1:])
    grade = 5
    if total >= 36:
        grade = 1
    elif total >= 32:
        grade = 2
    elif total >= 26:
        grade = 3
    elif total >= 20:
        grade = 4
    grades.append([student[0], grade])

print("Vysledne znamky:")
for grading in grades:
    print(f"Student {grading[0]} dostal znamku {grading[1]}")



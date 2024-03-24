# Vrať se k příkladu vysvědčení studenta.

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]

# Při přihlašování na střední školu mohou být 
# důležitější příklady z některých konkrétních předmětů. 
# Uprav kód z lekce tak, aby spočítal průměr pouze z jazyků, 
# matematiky a fyziky.

accounted_subjects = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
sum_of_grades = 0

for grading in school_report:
    if grading[0] in accounted_subjects:
        sum_of_grades += grading[1]

print(f"Prumer z vybranych predmetu ({', '.join(accounted_subjects)}) je {sum_of_grades / len(accounted_subjects)}")

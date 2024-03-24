school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

soucet = 0

for predmet, znamka in school_report.items():
    soucet += znamka

prumer = soucet / len(school_report)

print(prumer)

prumer2 = sum(school_report.values()) / len(school_report)

print(prumer2)

for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

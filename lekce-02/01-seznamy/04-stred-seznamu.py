# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# kdyz pouziju celociselne deleni, tak mi to spravne odeskne 0.5 z deleni liche delky seznamu
# a diky tomu, ze indexujeme od 0 to spravne odpovida indexu prostredniho prvku
middle = len(s) // 2

print(s[middle])
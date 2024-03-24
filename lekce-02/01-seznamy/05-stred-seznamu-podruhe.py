# Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tady pak chci odecist jednicku jen v pripade, ze je delka suda
# pokud je licha, vyjde mi to jako len(s) // 2 - 1 + 1 a jednicky se tim padem vzajemne vymazou
middle = len(s) // 2 - 1 + len(s) % 2

print(s[middle])

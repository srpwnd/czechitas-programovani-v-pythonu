# V následujícím seznamu máš seznam rodných čísel pacientů,
# kteří navštívili v jeden konkrétní den lékařskou ordinaci.

rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081",
]

#   - Kolik přišlo mužů a kolik žen?
#   - Kdy se narodil nejstarší a kdy nejmladší pacient?

# Pokud nevíš, jak funguje rodné číslo, vysvětlení je níže:

# Rodné číslo je identifikační číslo,
# které slouží k jednoznačné identifikaci osoby.
# V České republice se rodné číslo skládá z 10 číslic
# a jednoho lomítka, které ho rozděluje na části.

#   - Prvních 6 číslic udává datum narození
#     v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice).
#     Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202.
#     Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby.
#   - Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě.


oldest = 999999
youngest = 000000
no_of_females = 0

for rc in rodna_cisla:
    birthdate = int(rc[:6])

    # pokud se jedna o muze, vyjde sude cislo
    # pokud o zenu, vyjde liche cislo
    is_female = (birthdate // 5000) % 2
    # a tim padem tedy prictu 0 jako muze a 1 jako zenu
    no_of_females += is_female

    if is_female:
        birthdate -= 5000

    if birthdate < oldest:
        oldest = birthdate
    if birthdate > youngest:
        youngest = birthdate

# pocet muzu spoctu jako celkovy_pocet_lidi - pocet_zen
print(
    f"Do ordinace prislo {no_of_females} zen a {len(rodna_cisla) - no_of_females} muzu."
)

# tady delam orezy cisel pomoci modulo a celociselneho deleni:
# kdyz udelam cislo % 10, dostanu posledni cifru, cislo % 100, dostanu posledni 2 cifry (tedy vzdy tolik cifer od konce kolik je pocet nul)
# napr: 123456 % 100 = 56
# obdobne pak s celociselnym delenim, tedy cislo // 10 znamena, ze dostanu vse krom posledni cifry
# napr: 123456 // 100 = 1234
# a v tomto pripade chci prvni vyriznout den (posledni 2 cifry), mesic (prostredni 2 cifry) a rok (prvni 2 cifry)
print(
    f"Nejstarsi pacient se narodil {oldest % 100}. {(oldest // 100) % 100}. 19{oldest // 10_000}"
)
print(
    f"Nejmladsi pacient se narodil {youngest % 100}. {(youngest // 100) % 100}. 19{youngest // 10_000}"
)
# dale pak muzu v cislech psat _, ktere slouzi pouze jako vizualni oddelovac cifer, aby bylo cislo lepe citelne pro programatora
# nemuzeme totiz v zapisu cisla pouzit mezery
# 10_000 je tedy to stejne jako 10000, jenom nemusim tak slozite pocitat nuly, abych vedel co je to za cislo :)

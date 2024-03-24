# Mějme seznam pohybů na nějakém bankovním účtu:

pohyby = [1200, -250, -800, 540, 721, -613, -222]

    # Vypište v pořadí třetí pohyb z uvedeného seznamu.
    # Vypište všechny pohyby kromě prvních dvou.
    # Vypište kolik je všech pohybů dohromady.
    # Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
    # Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.

# treti prvek
print(pohyby[2])
# krome prvnich dvou
print(pohyby[2:])
# pocet pohybu
print(len(pohyby))
# nejnizsi
print(min(pohyby))
# nejvyssi
print(max(pohyby))
# celkem
print(sum(pohyby))

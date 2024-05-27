import re


def validate_ip(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    match = re.match(pattern, ip)
    if match:
        groups = match.groups()

        if all(0 <= int(group) <= 255 for group in groups):
            return True
    return False


ip_address = input("Zadejte IP adresu: ")


if validate_ip(ip_address):
    print("IP adresa je platná.")
else:
    print(
        "IP adresa není platná. Zkontrolujte, zda jsou všechna čísla v rozsahu 0 až 299 a adresa má formát X.X.X.X, kde X je číslo."
    )

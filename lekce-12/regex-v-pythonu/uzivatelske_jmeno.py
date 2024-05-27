import re


def validate_username(username):
    pattern = re.compile(r"^[a-z]{1,8}$")

    return True if pattern.match(username) else False


username = input("Zadejte uživatelské jméno: ")

if validate_username(username):
    print("Uživatelské jméno je správné.")
else:
    print(
        "Uživatelské jméno je nesprávné. Musí obsahovat pouze malá písmena a být maximálně 8 znaků dlouhé."
    )

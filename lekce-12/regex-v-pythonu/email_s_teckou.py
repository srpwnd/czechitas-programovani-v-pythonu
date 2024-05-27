import re


def validate_email(email):
    pattern = re.compile(r"^[a-z0-9]+(\.[a-z0-9]+)*@[a-z]+\.[a-z]{2,}$")

    return True if pattern.match(email) else False


email = input("Zadejte e-mailovou adresu: ")

if validate_email(email):
    print("E-mailová adresa je správná.")
else:
    print("E-mailová adresa je nesprávná.")

import re

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

phone_regex = re.compile(r"\+420\d{9}")

numbers = phone_regex.findall(zaznamy)

print(numbers)

zaznamy = phone_regex.sub("XXX", zaznamy)

print(f"Modifikovane zaznamy:\n {zaznamy}")

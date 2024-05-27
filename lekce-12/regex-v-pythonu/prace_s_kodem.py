import re

kod = """
sender_field_title = "Příjemce"
copy_field_title = "Kopie"
if blind_copy == True:
    blind_copy_title = "Skrytá kopie"
if action == "send":
    button_title = "Odeslat"
else:
    button_title = "Uložit koncept"
"""

assignment_pattern = re.compile(r"\w+\s*=\s*\".*\"")
matches = assignment_pattern.findall(kod)


string_pattern = re.compile(r'".*?"')
extracted_strings = [string_pattern.search(match).group() for match in matches]

for string in extracted_strings:
    print(string)

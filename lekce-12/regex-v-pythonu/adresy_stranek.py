import re

email_s_radami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz a přihlašuj se na naše kurzy!
"""

url_pattern = re.compile(r"https?://[^\s]+")

urls = url_pattern.findall(email_s_radami)

print("Found URLs:", urls)

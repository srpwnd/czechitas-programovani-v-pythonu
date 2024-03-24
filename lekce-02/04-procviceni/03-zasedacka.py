# Níže máš seznam akcí, které se konaly v zasedačce jedné firmy.

akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]

# Napiš program, který zjistí následující:

#     Kolik se uskutečnilo pohovorů?
#     V jakých jazycích se mohou zaměstnanci firmy vzdělávat?

# Při řešení můžeš využít operátor in a slicing, případně metodu split()

no_of_interviews = 0
langs = []

for event in akce:
    if "pohovor" in event:
        no_of_interviews += 1
    elif "jazykový kurz" in event:
        lang = event.split(" - ")[1]
        langs.append(lang)

print(f"Uskutecnilo se {no_of_interviews} pohovoru.")
print(f"Zamestnanci se mohou vzdelavat v jazycich {langs}")
# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu.
# Každá kniha bude mít atributy title, pages a price.
# Hodnoty nastav ve funkci __init__.

#     - Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
#     - Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách.
#       S využitím atributu pages vypočítej čas na přečtení knihy.
#       Metoda bude mít nepovinný parametr, který udává počet minut potřebných
#       pro přečtení jedné stránky knihy. Dobu potřebnou na přečtení knihy
#       získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy.
#       Výchozí hodnota nepovinného parametru je 4.


class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"{self.title} má {self.pages} stran a stojí {self.price} korun"

    def get_time_to_read(self, time_per_page=2):
        return self.pages * time_per_page


kniha_1 = Book("Malý princ", 120, 250)

print(kniha_1.get_info())

print(f"Knizku prectes za {kniha_1.get_time_to_read()} minut")

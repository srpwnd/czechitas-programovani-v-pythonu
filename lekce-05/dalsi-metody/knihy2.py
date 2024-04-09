# Vrať se k práci se třídou Book. Pokud jsi ji nestihl(a) v minulé části vytvořit, vrať se nejprve k zadání příkladu na předchozí stránce a třídu si vytvoř.

#     - U knihy budeme chtít evidovat, kolik kusů bylo prodáno.
#       Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__().
#       Dále přidej atribut costs, které představují náklady na jednu knihu
#       (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).
#     - Přidej metodu profit(), která vrátí celkový zisk z knihy.
#       Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
#     - Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku.
#       Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák".
#       Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr".
#       Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".


class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    def get_info(self):
        return f"{self.title} má {self.pages} stran a stojí {self.price} korun"

    def get_time_to_read(self, time_per_page=2):
        return self.pages * time_per_page

    def profit(self):
        return self.sold * (self.price - self.costs)

    def rating(self):
        if self.profit() < 50_000:
            return "propadák"
        elif self.profit() < 500_000:
            return "prumer"
        else:
            return "bestseller"


kniha_1 = Book("Malý princ", 120, 250, 1200, 170)

print(kniha_1.get_info())

print(f"Knizku prectes za {kniha_1.get_time_to_read()} minut")

print(f"Knizka vydelala {kniha_1.profit()} a ziskala hodnoceni: {kniha_1.rating()}")

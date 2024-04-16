# Nyní je naším cílem práce pro společnost, která se zabývá prodejem jízdenek a letenek.

#     Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sedadla). Tato třída bude sloužit například pro cesty autobusem.
#     Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu. Vytvoř třídu TrainTicket, která bude mít navíc atribut fare_class (uvažujeme možnosti economy a business). Dále naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 30 % vyšší oproti basic_price, pokud fare_class je business.
#     U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. Vytvoř třídu PlaneTicket, která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, který udává počet odbavených zavazadel. Naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 50 % vyšší oproti basic_price, pokud fare_class je business. Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).
#     Vytvoř jízdenku na vlak se základní cenou 150 do tříd economy i business. Zkontroluj, jakou hodnotu vrací metoda get_price().
#     Vytvoř letenku se základní cenou 6000 do tříd economy i business s jedním odbaveným zavazadlem. Zkontroluj, jakou hodnotu vrací metoda get_price().

# Vyzkoušej vypočítat celkovou cenu dvou jízdenek různého typu, tj. jedné letenky a jedné jízdenky na vlak. Celkovou cenu ulož do proměnné total_price a k výpočtu použij metodu get_price().


class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number


class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == "business":
            return self.basic_price * 1.3
        return self.basic_price


class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        price = self.basic_price
        if self.fare_class == "business":
            price *= 1.5
        return price + 2000 * self.checkout_luggages


train_economy = TrainTicket(150, 45, "economy")
train_business = TrainTicket(150, 87, "business")

print(
    f"Cena vlaku v economy: {train_economy.get_price()} a v business: {train_business.get_price()}"
)

plane_economy = PlaneTicket(6000, 8, "economy", 1)
plane_business = PlaneTicket(6000, 8, "business", 1)

print(
    f"Cena letadla v economy: {plane_economy.get_price()} a v business: {plane_business.get_price()}"
)

total_price = train_business.get_price() + plane_business.get_price()

print(f"Spolecna cena: {total_price}")

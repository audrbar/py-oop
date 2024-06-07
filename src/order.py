
# 7. Sukurkite klasę Order (užsakymas), kuriame būtų saugoma užsakymo informacija (prekės, kiekiai, kainos).
# Įdiekite prekių pridėjimo, pašalinimo, bendros kainos apskaičiavimo ir nuolaidų taikymo metodus.

class Order:
    def __init__(self, id_: str):
        self.id = id_
        self.items = []
        print(f"The Order item #{self.id} was created.")

    def add_item(self, name: str, price: int, amount: int):
        self.items.append({'name': name, 'price': price, 'amount': amount})
        print(f"The {amount} pieces of '{name}' for {price}$ each where added to the Order #{self.id}.")

    def total_price(self) -> float:
        total: float = 0.0
        for item in order.items:
            total += item['price'] * item['amount']
        print(f"The Order #{self.id} total price is {total}$.")
        return round(total)

    def checkout(self):
        if self.total_price() >= 100:
            total = round(self._calculate_discount(self.total_price()))
            print(f"The Order #{self.id} checkout {total}$, 10% discount was applied.")
        else:
            print(f"The Order #{self.id} checkout {self.total_price()}$, no discount applied.")

    @staticmethod
    def _calculate_discount(total):
        return total * 0.9

    def get_order_content(self):
        print(f"The Order #{self.id} consist of:")
        for item in order.items:
            print(f"- {item['amount']} pieces of '{item['name']}' for {item['price']}$ each.")


order = Order('1')
order.add_item('bread', 2, 5)
order.add_item('milk', 5, 2)
order.add_item('nuts', 10, 2)
order.get_order_content()
order.total_price()
order.checkout()

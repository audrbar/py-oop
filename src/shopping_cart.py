class ShoppingCart:
    def __init__(self, id_: str):
        self.id = id_
        self.items = []
        print(f"The ShoppingCart #{self.id} was created.")

    def add_item(self, name: str, price: int, amount: int):
        self.items.append({'name': name, 'price': price, 'amount': amount})
        print(f"The {amount} pieces of '{name}' for {price}$ each where added to the Cart #{self.id}.")

    def total_price(self) -> float:
        total: float = 0.0
        for item in cart.items:
            total += item['price'] * item['amount']
        print(f"The Cart #{self.id} total price is {total}$.")
        return round(total)

    def checkout(self):
        if self.total_price() >= 100:
            total = round(self._calculate_discount(self.total_price()))
            print(f"The Cart #{self.id} checkout {total}$, 10% discount was applied.")
        else:
            print(f"The Cart #{self.id} checkout {self.total_price()}$, no discount applied.")

    @staticmethod
    def _calculate_discount(total):
        return total * 0.9

    def get_cart_content(self):
        print(f"The Cart #{self.id} consist of:")
        for item in cart.items:
            print(f"- {item['amount']} pieces of '{item['name']}' for {item['price']}$ each.")


cart = ShoppingCart('1')
cart.add_item('bread', 2, 5)
cart.add_item('milk', 5, 2)
cart.add_item('nuts', 10, 2)
cart.get_cart_content()
cart.total_price()
cart.checkout()

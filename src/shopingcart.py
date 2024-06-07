# 5. Sukurkite klasę ShoppingCart, kuriame būtų prekių sąrašas. Joje turėtų būti metodai:
# pridėti prekes, pašalinti prekes, peržiūrėti krepšelį ir apskaičiuoti bendrą kainą.

class ShoppingCart:
    def __init__(self, id_: str, _items: dict):
        self.id = id_
        self.items = _items

    def _calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item
        return total

    def add_item(self, name, amount):
        self.items.update({name: amount})
        print(f"The Cart #{self.id} was updated: {name} added.")
        self.get_total_items()

    def remove_item(self, name):
        self.items.pop(name)
        print(f"The Cart #{self.id} was updated: {name} removed.")
        self.get_total_items()

    def get_total_items(self):
        print(f"The Cart #{self.id}  Total: {self._calculate_total()}")


cart = ShoppingCart('1', {})
cart.add_item('banana', 5)
cart.add_item('berry', 7)
cart.add_item('apple', 9)
print(cart.items)
cart.get_total_items()
cart.remove_item('berry')
print(cart.items)

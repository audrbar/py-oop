class ShoppingCart:
    def __init__(self, items: dict):
        self.items = items

    def add_item(self):
        shop_cart = {}
        one_more = True
        while one_more:
            shop_item = input('Ivesk preke: ')
            shop_price = input('Nurodyk kaina: ')
            shop_cart[shop_item] = shop_price
            one_more = bool(input('Dar prekiu (1/0)? '))
        return shop_cart

    def total_price(self):
        pass

    def checkout(self):
        pass

    def _calculate_discount(self):
        pass


cart_1 = ShoppingCart({'duona': 5})
cart_1.add_item()
print(cart_1)
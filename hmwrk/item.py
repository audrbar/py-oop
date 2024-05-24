class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        print(f"The Item '{self.name}' for {self.price}$ was created.")

    def get_price(self):
        return self.price


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def rm_item(self, item):
        self.items.remove(item)
        print(f"The Item '{item.name}' for {item.price}$ was removed from Cart #{self.order_id}.")
        return self.items

    @staticmethod
    def order_content():
        print(f"The Order #{order.order_id} content is:")
        for item in order.items:
            print(f"{item.name} for {item.price}$.")

    def get_order_price(self):
        price = 0
        for item in self.items:
            price += item.get_price()
        print(f"The Cart Total price is: {price}$.")
        return price


item_1 = Item('apple', 2)
item_2 = Item('banana', 5)
item_3 = Item('blueberry', 9)
order = Order('1')
order.add_item(item_1)
order.add_item(item_2)
order.add_item(item_3)
order.order_content()
order.get_order_price()
order.rm_item(item_2)
order.get_order_price()

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def list_items(self):
        print(f'The item {self.name} is in stock for {self.price}$.')


if __name__ == "__main__":
    print(f'==== {__file__} ====')


class Order:
    def __init__(self, order_id: int, item: Item):
        self.item = item
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return self.items

    def rm_item(self):
        pass


item_1 = Item('apple', 2)
item_2 = Item('banana', 5)
item_3 = Item('blueberry', 9)
item_1.list_items()
item_2.list_items()
item_3.list_items()
order = Order(1, item_1)
order.add_item(item_2)
order.add_item(item_3)
print(f"Orders in a list: {order.order_id}: {order.items}")
print(order.items)

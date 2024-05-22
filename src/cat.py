class Cat:
    total_cats = 0
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        Cat.total_cats += 1
    def print_amount(self):
        print(f'Sukurta {total_cats} kaciu.')

cat1 = Cat('lola', 'green')
cat2 = Cat('big', 'black')
cat3 = Cat('red', 'red')
print(f'Sukurtos kates: {cat1.name}, {cat2.name}, {cat3.name}')
print(f'Sukurta {Cat.total_cats} kaciu.')
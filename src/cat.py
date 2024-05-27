class Cat:
    # class attributes
    total_cats: int = 0

    def __init__(self, name: str, color: str):
        # instance attributes
        self.name = name
        self.color = color
        print(f"The {self.color} cat '{self.name}' was created.")
        Cat.total_cats += 1


# instance
cat1 = Cat('lola', 'green')
cat2 = Cat('big', 'black')
cat3 = Cat('red', 'red')
print(f'Cats: {cat1.name}, {cat2.name}, {cat3.name}')
print(f'Created {Cat.total_cats} cats.')
print(f'Created {cat1.total_cats} cats.')

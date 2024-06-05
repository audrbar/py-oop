class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self, sound: str):
        print(f'{self.name} says {sound}')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Overwrite parent
    def speak(self, sound):
        print(f'{self.name} is saying {sound}!!!!')


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Bird class methods
    def fly(self):
        print(f'{self.name} can fly!')

    def speak(self, sound):
        super().speak(sound)
        print('And child info after!!!')


dog = Dog(name='Dog Name')
dog.speak('woof')
cat = Cat(name='Cat Name')
cat.speak('meow')
bird = Bird(name='Bird Name')
bird.speak('Pew')

# 2. Sukurkite statefull klasę Skaitiklis, kuri saugoja skaičių. Joje turėtų būti metodai,
# skirti skaičiui padidinti, sumažinti, atstatyti ir dabartiniam skaičiui gauti.

class Skaitiklis:
    def __init__(self, numb: int):
        self.numb = numb
        self.initial = numb

    def increase(self, amount):
        return self.numb + amount

    def decrease(self, amount):
        return self.numb - amount

    def reverse(self):
        return self.initial

    def get_numb(self):
        return f"{self.numb}"


num = Skaitiklis(3)
print(num.increase(3))
print(num.decrease(3))
print(num.reverse())
print(num.get_numb())

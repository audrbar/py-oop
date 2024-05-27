# 1. Sukurkite bazinę klasę Person su atributais name ir age. Apibrėžkite metodą introduce,
# kuris spausdina pasveikinimą. Sukurkite išvestinę klasę Student, kuri paveldi iš Person
# ir prideda atributą school_name. Pridėkite metodą print_info(), kur atspausdinkite visą žinomą
# informaciją apie žmogų.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Welcome on board, {self.name}, {self.age}.")


class Student(Person):
    def __init__(self, name: str, age: int, school_name: str):
        self.school_name = school_name
        super().__init__(name, age)

    def print_info(self):
        print(f"Student {self.name}, {self.age}, {self.school_name}.")


st_1 = Student(name='Audrius', age=19, school_name='Saule')
st_1.print_info()



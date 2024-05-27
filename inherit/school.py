# 5. Parašykite programą, kuri imituotų mokyklos systemą. Implementuokite klases:
# Person, Teacher, Student, Cource. Programoje turi būti galimybė priskirti studentą prie kurso,
# atspausdinti informaciją apie kursą: kas dėsto, kiek valandų, koks pažymys.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def describe_teacher(self):
        return f"The teacher {self.name}, {self.age}, teaches {self.subject}."


class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade

    def describe_student(self):
        return f"The student {self.name}, {self.age}, has {self.grade}."


class Course:
    def __init__(self, name, student: Student, teacher: Teacher):
        self.name = name
        self.student = student
        self.teacher = teacher

    def __str__(self):
        return f"{self.name}"


tch_1 = Teacher('Teresa', 34, 'math')
st_1 = Student('Audrius', 19, 78)
print(tch_1.describe_teacher())
print(st_1.describe_student())
cr_1 = Course('A1', st_1, tch_1)
print(f"Kurso {cr_1} studento {st_1.name} pazymys {st_1.grade}, o {tch_1.subject} ji ismoke mokytoja {tch_1.name}.")

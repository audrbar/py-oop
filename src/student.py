class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if new_grade >= 0 and new_grade < 100:
            self.grade = new_grade
        else:
            print('Ivertinimas netinka')
    def print_studen_info(self):
        print(f'Studentas: {self.name}, {self.grade}')

stu_1 = Student('Audrius', 60)
stu_1.print_studen_info()
stu_1.set_grade(101)
stu_1.set_grade(70)
stu_1.print_studen_info()
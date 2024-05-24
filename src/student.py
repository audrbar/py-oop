class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 <= new_grade < 100:
            self.grade = new_grade
        else:
            print('Ops... Grade must be between 1 and 100.')

    def print_student_info(self):
        print(f'Student: {self.name}, {self.grade}')


stu_1 = Student('Audrius', 60)
stu_1.print_student_info()
stu_1.set_grade(101)
stu_1.set_grade(70)
stu_1.print_student_info()

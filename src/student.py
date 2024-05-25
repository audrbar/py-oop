class Student:
    def __init__(self, name: str, group: str, grade: int):
        self.name = name
        self.group = group
        self.grade = grade
        print(f"Success. Student {self.name} with grade {self.grade} was created.")

    def get_grade(self) -> int:
        return self.grade

    def set_grade(self, new_grade) -> int:
        if 0 <= new_grade < 100:
            self.grade = new_grade
            print(f"Success. Student {self.name} grade was updated to {self.grade}.")
        else:
            print('Ops... Grade must be between 1 and 100.')
        return self.grade

    def print_student_info(self) -> str:
        return f"Student {self.name} from group {self.group} grade is {self.grade}."


stu_1 = Student('Audrius', 'A', 60)
stu_1.set_grade(101)
stu_1.set_grade(70)
print(stu_1.print_student_info())

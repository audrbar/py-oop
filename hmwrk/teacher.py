class Teacher:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject
        print(f'The teacher {self.name} teaches {self.subject}.')


class Classroom:
    def __init__(self, classmates: list, teacher: Teacher):
        self.classmates = classmates
        self.teacher = teacher
        print(f'The classroom {', '.join(self.classmates)} teacher {teacher_1.name} teaches {teacher_1.subject}.')

    def add_classmate(self, name):
        self.classmates.append(name)
        print(f"The classmate '{name}' was successfully added to a class.")

    def rm_classmate(self, name):
        self.classmates.remove(name)
        print(f"The classmate '{name}' was successfully removed from a class.")


teacher_1 = Teacher('Marry', 'math')
classroom_1 = Classroom(['John', 'Valery', 'Monika'], teacher_1)
classroom_1.rm_classmate('John')
classroom_1.add_classmate('Linus')
print(f'Updated classroom: {', '.join(classroom_1.classmates)}.')

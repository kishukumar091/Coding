class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        pass

class Student(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def print_details(self):
        print(f"Student: {self.name}, Age: {self.age}, Department: {self.department}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def print_details(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")

def main():
    student_info = input().split(", ")
    teacher_info = input().split(", ")

    student = Student(*student_info)
    teacher = Teacher(*teacher_info)

    student.print_details()
    teacher.print_details()

if __name__ == "__main__":
    main()

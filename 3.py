#   Design a program for creating a child class Teacher 
#   that inherits properties from the parent class Staff.


# Parent class Staff
class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Child class Teacher
class Teacher(Staff):
    def __init__(self, name, id, subject):
        
        # Calling the parent class constructor
        super().__init__(name, id)
        self.subject = subject

# Creating an instance of the Teacher class
teacher1 = Teacher('John Doe', 'T101', 'Mathematics')
print(f"Teacher Name:{teacher1.name}\nID:{teacher1.id}\nSubject:{teacher1.subject}")

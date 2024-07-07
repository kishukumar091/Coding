# 1. Develop a program for creating a class named Students,initializing 
#    attributes such as name, age, and grade during object instantiation.
class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student1=Students("Rohan",15,"10th")
print(f"Student Name:{student1.name}\nAge:{student1.age}\nGrade:{student1.grade}")
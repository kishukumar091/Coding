#  Explain how a destructor can be defined and utilized in a Python class.

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"Deleting {self.name} object")

# Creating instances of MyClass
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# Deleting an object explicitly
del obj1

# Creating a reference to obj2
obj3 = obj2

# Deleting obj2 and obj3
del obj2
del obj3


""" The MyClass defines a constructor (__init__) and a destructor (__del__).

    When an object of MyClass is created, the constructor is called to 
        initialize the object.

    When an object is deleted, either explicitly using the del keyword or 
        when it goes out of scope and there are no more references to it, the 
        destructor (__del__) is automatically called.
        
    In the example, you can see that when obj1 is deleted explicitly, 
    its destructor is called, printing a message indicating its deletion.
    Similarly, when obj2 and obj3 are deleted, their destructor is called as well."""

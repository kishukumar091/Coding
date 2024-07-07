#   Explore the usage of the 'private' access modifier 
#   in Python and discuss its implications.

class MyClass:
    def __init__(self):
        self._private_variable = 42

    def _private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self._private_method()

# Outside of the class
obj = MyClass()
print(obj._private_variable)  # Accessing private variable (not recommended)
obj._private_method()  # Accessing private method (not recommended)
obj.public_method()  # Accessing public method



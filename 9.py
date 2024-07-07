class MyClass:
    def __init__(self):
        self.public_var = "I'm public!"
        self._protected_var = "I'm protected!"
        self.__private_var = "I'm private!"

    def access_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.public_var)  # Accessible
print(obj._protected_var)  # Accessible, but not recommended
print(obj.access_private_var())  # Accessible
print(obj.__private_var)  # Will raise an AttributeError
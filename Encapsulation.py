class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__mileage = 0  # private variable
    
    def drive(self, miles):
        self.__mileage += miles
        
    def get_mileage(self):
        return self.__mileage

# Creating a car object
my_car = Car("Toyota", "Camry")

# Accessing and modifying mileage directly (Not recommended)
my_car.__mileage = 10000
print(my_car.get_mileage())  # Output will be 0

# Using the drive method to update mileage
my_car.drive(100)
print(my_car.get_mileage())  # Output will be 100






class Shape:
    def area(self):

        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Function to calculate area of any shape
def calculate_area(shape):
    return shape.area()

# Creating objects of different shapes
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calculating area using polymorphism
print(calculate_area(rectangle))  # Output will be 20
print(calculate_area(circle))     # Output will be 28.26



from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class square(Shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side*self.side
    
# Creating an object of Rectangle
rectangle = Rectangle(5, 4)
print(rectangle.area())
Square=square(8)
print(Square.area())
# Trying to create an object of abstract class Shape (will raise an error)
#shape = Shape()  # This will raise an error since Shape is an abstract class








#	Construct a child class Bus that inherits all variables
#   and methods from the Vehicle class created in question 3.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
        
Vehicle1=Bus(120,15)
print(Vehicle1.max_speed ,"\n",Vehicle1.mileage)

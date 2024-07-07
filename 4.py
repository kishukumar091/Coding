#	Devise a Python program to define a Vehicle class 
#   with instance attributes max_speed and mileage.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

Vehicle1=Vehicle(120,15)
print(f"Vehicle Max Speed:{Vehicle1.max_speed}\nMileage:{Vehicle1.mileage}")
class ElectronicDevice:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_details(self):
        pass

class Mobile(ElectronicDevice):
    def __init__(self, name, price, screen_size):
        super().__init__(name, price)
        self.screen_size = screen_size

    def print_details(self):
        return f"Mobile: {self.name}, Price: ${self.price}, Screen Size: {self.screen_size}"

class Laptop(ElectronicDevice):
    def __init__(self, name, price, screen_resolution):
        super().__init__(name, price)
        self.screen_resolution = screen_resolution

    def print_details(self):
        return f"Laptop: {self.name}, Price: ${self.price}, Screen Resolution: {self.screen_resolution}"

mobile_input = input().split(", ")
laptop_input = input().split(", ")

mobile = Mobile(*mobile_input)
laptop = Laptop(*laptop_input)

print(mobile.print_details())
print(laptop.print_details())

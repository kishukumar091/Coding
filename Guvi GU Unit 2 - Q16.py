class Product:
    def __init__(self, name, price, seller):
        self.name = name
        self.price = float(price)
        self.seller = seller

    def print_details(self):
        return f"{self.name}, Price: ${self.price:.2f}, Seller: {self.seller}"


class NewProduct(Product):
    def print_details(self):
        return f"New Product: {super().print_details()}"


class UsedProduct(Product):
    def __init__(self, name, price, seller, condition):
        super().__init__(name, price, seller)
        self.condition = condition

    def print_details(self):
        return f"Used Product: {super().print_details()}, Condition: {self.condition}"


product1_info = input().split(", ")
product2_info = input().split(", ")

product1 = NewProduct(*product1_info)
product2 = UsedProduct(*product2_info)

print(product1.print_details())
print(product2.print_details())

class Product:
    def get_details(self):
        pass

class Book(Product):
    def get_details(self):
        pass

class Electronics(Product):
    def get_details(self):
        pass

class EBook(Book, Electronics):
    pass

class Apparel(Product):
    pass

class SmartWatch(Apparel, Electronics):
    pass

class Furniture(Product):
    pass

class SmartFurniture(Furniture, Electronics):
    pass

class Organic(Product):
    pass

class Grocery(Product):
    pass

class OrganicGrocery(Organic, Grocery):
    pass

def mro_sequence(cls):
    return [c.__name__ for c in cls.mro()]

class_name = input()

cls = globals()[class_name]

print(mro_sequence(cls))

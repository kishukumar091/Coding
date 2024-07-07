class Item:
    def __init__(self, title, price):
        
        self.title = title
        self.price = float(price)

    def change_price(self, new_price):
        
        self.price = float(new_price)

    def print_details(self):
        
        return f" priced at ${self.price:.2f}"


class Book(Item):
    def __init__(self, title, author, price):
        
        super().__init__(title, price)
        self.author = author

    def print_details(self):
        
        print(f"Book: {self.title} by {self.author}, {super().print_details()}")


class Magazine(Item):
    def __init__(self, title, price, issue):
        
        super().__init__(title, price)
        self.issue = issue

    def print_details(self):
            
        print(f"Magazine: {self.title}, Issue No. {self.issue}, {super().print_details()}")


def clean_input(ip):
    return str(ip.strip())

book_title, book_author, book_price = map(clean_input, input().strip().split(","))
mz_title, mz_price, mz_issue = map(clean_input, input().strip().split(","))

book1 = Book(book_title, book_author, book_price)
magazine1 = Magazine(mz_title, mz_price, mz_issue)

book1.print_details()
magazine1.print_details()

book1.change_price(input())
magazine1.change_price(input())

book1.print_details()
magazine1.print_details()

class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type

    def borrow_book(self, book_title):
        return f"Book \"{book_title}\" successfully borrowed by {self.name}."


class Faculty(User):
    def __init__(self, name):
        super().__init__(name, "faculty")

    def borrow_book(self, title):
        if 'DVD' in title:
            return "Faculty members can only borrow DVDs."
        else:
            return super().borrow_book(title)

def main():
    while True:
        name = input()
        user_type = input().lower()
        if user_type == "faculty":
            user = Faculty(name)
        else:
            user = User(name, user_type)

        item_title = input()
        if user_type == 'faculty':
            if 'DVD' in item_title:
                print(user.borrow_book(item_title))
            else:
                print("Faculty members can only borrow DVDs.")
        else:
            print(user.borrow_book(item_title))

        choice = input().lower()
        if choice != "yes":
            print("Quitting the program.")
            break
        
if __name__ == "__main__":
    main()

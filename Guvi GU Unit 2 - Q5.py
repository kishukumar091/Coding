def get_book_details(isbn: str) -> dict:
    books = {
        "1234567890": {"title": "Python Programming", "author": "John Doe", "price": 500, "quantity": 10},
        "9876543210": {"title": "Data Structures and Algorithms", "author": "Jane Doe", "price": 600, "quantity": 5},
        "1111111111": {"title": "Machine Learning", "author": "Sam Smith", "price": 700, "quantity": 2}
    }
    if isbn in books:
        return books[isbn]
    else:
        raise ValueError("Book not found")

def handle_book_request(isbn):
    try:
        book_details = get_book_details(isbn)
        return f"Book found: {book_details['title']} by {book_details['author']}. Price: {book_details['price']}, Quantity: {book_details['quantity']}"
    except ValueError as e:
        return str(e)


isbn = input()
response = handle_book_request(isbn)
print(response)


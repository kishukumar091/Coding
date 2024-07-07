class ItemNotFoundError(Exception):
    pass

def get_stock(item):
    stock = {
        "Apples": 50,
        "Oranges": 30,
        "Grapes": 0,
    }
    if item in stock:
        return stock[item]
    else:
        raise ItemNotFoundError("Item not found")

def handle_stock_request(item):
    try:
        stock = get_stock(item)
        if stock > 0:
            return f"Stock for {item}: {stock}"
        else:
            return "Item not found"
            
    except ItemNotFoundError as e:
        return str(e)

user_input = input()

print(handle_stock_request(user_input))

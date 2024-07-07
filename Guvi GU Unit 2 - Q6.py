def get_product_details(product_id):
    products = {
        "123456": {"name": "Wireless Mouse", "category": "Electronics", "price": 500, "stock": 10},
        "789012": {"name": "Running Shoes", "category": "Sports", "price": 600, "stock": 5},
        "345678": {"name": "Coffee Maker", "category": "Home Appliances", "price": 700, "stock": 2},
    }
    if product_id in products:
        return products[product_id]
    else:
        raise Exception("Product not found")

def handle_product_request(product_id):
    try:
        product_details = get_product_details(product_id)
        return f"Product found: {product_details['name']}, Category: {product_details['category']}, Price: {product_details['price']}, Stock: {product_details['stock']}"
    except Exception as e:
        return str(e)
    finally:
        print("Request handled")

user_input = input()
result = handle_product_request(user_input)
print(result)

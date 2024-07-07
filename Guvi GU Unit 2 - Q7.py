def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

def handle_calculation(operation, num1, num2):
    try:
        result = calculate(operation, num1, num2)
        return f"Result: {result}"
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)

def main():
    inputs = input()
    operation, num1, num2 = map(str.strip, inputs.split(","))
    num1 = float(num1)
    num2 = float(num2)

    message = handle_calculation(operation, num1, num2)
    print(message)

if __name__ == "__main__":
    main()

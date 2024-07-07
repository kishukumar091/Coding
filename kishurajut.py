try:
    a=int(input("Enter number:"))
    b=int(input("Enter second Number:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Not a valid Integer")
else:
    print("No Exception occured")
finally:
    print("Finally blocked")
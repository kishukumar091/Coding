import math

class Shape:
    def area(self, *args):
        pass
    
    def perimeter(self, *args):
        pass

class Circle(Shape):
    def area(self, radius):
        return math.pi * radius**2

    def perimeter(self, radius):
        return 2 * math.pi * radius

class Rectangle(Shape):
    def area(self, width, height):
        return width * height

    def perimeter(self, width, height):
        return 2 * (width + height)

class Triangle(Shape):
    def area(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    def perimeter(self, side1, side2, side3):
        return side1 + side2 + side3

def main():
    shape_classes = {'circle':Circle(), 'rectangle': Rectangle(), 'triangle' :Triangle()}
    while True:
        shape = input().lower()
        if shape == 'quit':
            print("Quitting the program.")
            break
        elif shape not in shape_classes:
            print("Invalid input. Please enter a valid shape (circle/rectangle/triangle).")
            continue

        dimensions = list(map(float, input().split()))
        print("Area of the {}: {:.2f}".format(shape, shape_classes[shape].area(*dimensions)))
        print("Perimeter of the {}: {:.2f}".format(shape, shape_classes[shape].perimeter(*dimensions)))

if __name__ == "__main__":
    main()




        

    

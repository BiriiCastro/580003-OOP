class Circle:
    def __init__(self, radius):
        self.pi = 3.1415
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

    def display(self):
        print(f"The Area of the Radius {self.radius} is: {self.area()}")
        print(f"The Perimeter of the Radius {self.radius} is: {self.perimeter()}")

R = float(input("Enter the Radius of the Circle: "))

circle = Circle(R)
circle.area()
circle.perimeter()
circle.display()

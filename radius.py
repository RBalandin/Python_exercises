

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def radius(self):
        return self.radius

    def radius(self, value):
        self.radius = value

    def circle_area(self):
        return 3.14 * self.radius ** 2


if __name__ == '__main__':
    a = Circle(10)
    print(a.radius)
    print(a.circle_area())
    a.radius = 199
    print(a.radius)

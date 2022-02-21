

class Ex:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z


class Extended(Ex):
    def __init__(self, x, y, z, colour=None):
        super(Extended, self).__init__(x, y, z)
        if not colour:
            self.colour = "Blue"

    def volume_and_colour(self):
        return self.x * self.y * self.z, self.colour

if __name__ == '__main__':
    a = Extended(4, 10, 3)
    print(a.volume())
    print(a.volume_and_colour())


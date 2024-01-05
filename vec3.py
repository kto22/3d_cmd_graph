from math import sqrt


class vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def lenght(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    def norm(self):
        l = vec3.lenght(self)
        return vec3(self.x / l, self.y / l, self.z / l)

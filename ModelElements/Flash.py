from ModelElements.Poligon import Point3D


class Angle3D:
    pass


class Color:
    pass


class Float:
    pass


class Flash:
    def __init__(self):
        self.location = Point3D
        self.angle = Angle3D
        self.color = Color
        self.power = Float

    def rotate(self, angle3D) -> None:
        return super().rotate(angle3D)

    def move(self, point3D) -> None:
        return super().move(point3D)

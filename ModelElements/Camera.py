from ModelElements.Flash import Angle3D
from ModelElements.Poligon import Point3D


class Camera:
    def __init__(self):
        self.location = Point3D
        self.angle = Angle3D

    def rotate(self, angle3D) -> None:
        return super().rotate(angle3D)

    def move(self, point3D) -> None:
        return super().move(point3D)

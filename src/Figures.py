from math import sqrt, acos, degrees


class Point:
    def __init__(self, y, x):
        self.x = x
        self.y = y
       # print(x)
       # print(y)


class Camera(Point):
    def __init__(self, y, x, direction, alpha, range):
        # Point.x = x
        # Point.y = y
        self.x = x
        self.y = y
        self.direction = direction
        self.alpha = alpha
        self.range = range
        # print(alpha)
        # print(range)


class Polygon:
    def __init__(self, vertices, cameras):
        self.vertices = vertices
        self.cameras = cameras

    def addVertice(self, point):
        self.vertices.append(point)

    def addCamera(self, camera):
        self.cameras.append(camera)

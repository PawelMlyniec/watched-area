

class Point:
    def __init__(self, y,x):

        self.x = x
        self.y = y
        print(x)
        print(y)


class Camera(Point):

    def __init__(self,y,x,direction,alpha,range):
        # Point.x = x
        # Point.y = y
        self.x = x
        self.y = y
        self.direction = direction
        self.alpha = alpha
        self.range = range
        print(alpha)
        print(range)
class Polyghon:
    def __init__(self):
        self.vertices = []
        self.cameras = []
    def addVertice(self,point):
        self.vertices.append(point)
    def addCamera(self,camera):
        self.cameras.append(camera)

        



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x)
        print(y)


class Camera(Point):
    def __init__(self,x,y,direction,alpha,range):
        Point.x = x
        Point.y = y
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
    def isPointInPolyghon(Point ):
        pass
    def isEdgeCrossingWithPointLine(point, firstVertice,secondVertice):
        pass
    def whereEdgesAreCrossingWithPointLine(point,firstVertice,secondVertice):
        pass
    def isCrossingOnRightSiedeOfPoint(crossing, point):
        pass
    def isPointInAnyCameraView(point, camera):
        pass
    def isPointInCameraRange(point, camera):
        pass
    def isPointInCameraAngle(point,camera):
        pass
    def isAnyEdgeBeetwenCameraAndPoint(point,camera):
        pass

    

        
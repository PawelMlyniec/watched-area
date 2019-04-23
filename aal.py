from math import sqrt,acos,degrees

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

    def isPointInPolyghon(self,checkPoint ):
        cross = 0
        n = len(self.vertices)
        for i in range(n):
            if self.isEdgeCrossingWithPointLine(checkPoint,self.vertices[i],self.vertices[(i+1)%n]):
                if self.isCrossingOnRightSiedeOfPoint(checkPoint,self.vertices[i],self.vertices[(i+1)%n]):
                    cross+=1
        return cross%2 != 0 
    def isEdgeCrossingWithPointLine(self,point, firstVertice,secondVertice):
        #points on vertices problem
        #if between(point.y, firstVertice.y, secondVertice.y)
        if firstVertice.y > secondVertice.y:
            return point.y >= secondVertice.y and point.y <= firstVertice.y
        if firstVertice.y < secondVertice.y:
            return point.y <= secondVertice.y and point.y >= firstVertice.y
        if  firstVertice.y == secondVertice.y:
            return False
    def isCrossingOnRightSiedeOfPoint(self,point,firstVertice,secondVertice):
        return point.x <= self.whereEdgesAreCrossingWithPointLine(point,firstVertice,secondVertice)
    def whereEdgesAreCrossingWithPointLine(self,point,firstVertice,secondVertice):
        p = point
        a = firstVertice
        b = secondVertice
        crossing = a.x + (p.y - a.y)*(a.x-b.x)/(a.y - b.y)   
        return crossing 
    def isPointInAllCameraView(self,point, camera):
        for camera in self.cameras:
            if not self.isPointInCameraRange(point, camera):
                return False
            if not self.isPointInCameraAngle(point,camera):
                return False
            if self.isAnyEdgeBeetwenCameraAndPoint(point, camera):
                return False
        return True

    def isPointInCameraRange(self,point, camera):
        p = point
        c = camera
        d = sqrt((p.x - c.x)**2 + (p.y - c.y)**2)
        return camera.range >= d
    def isPointInCameraAngle(self,point,camera):
        p = point
        c = camera
        alpha = acos((c.y - p.y)/sqrt((c.x-p.x)**2+(c.y-p.y)**2))
        alpha = degrees(alpha)
        return camera.direction <= alpha and camera.direction + camera.alpha >= alpha
    def isAnyEdgeBeetwenCameraAndPoint(self,point,camera):
        p = point
        c = camera
        n = len(self.vertices)
        for i in range(n):
            v1 = self.vertices[i]
            v2 = self.vertices[(i+1)%n]
            if v1.x != v2.x and not(c.y == p.y and v1.y == v2.y):
                difV = (v1.y-v2.y)/(v1.x-v2.x) 
                difCP = (c.y-p.y)/(c.x+p.y)
                x = (v1.y-difV*v1.x-difCP*c.x)/(difCP - difV)
                y = difCP*x + c.y - difCP*c.x
                return between(x,c.x,p.x)  and between(y,c.y,p.y)
            if c.y == p.y and v1.y == v2.y:
                return False
            if v1.x == v2.x:
                difCP = (c.y-p.y)/(c.x+p.y)
                x = v1.x
                y = difCP*x + c.y - difCP*c.x
                return between(x,c.x,p.x)  and between(y,c.y,p.y)

            

def between(x,firstValue,secondValue):
    if firstValue > secondValue:
        return x <= firstValue and x >= secondValue
    if firstValue < secondValue:
        return x >= firstValue and x <= secondValue
    if firstValue == secondValue:
        return x == firstValue

        
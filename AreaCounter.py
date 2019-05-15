from math import sqrt,acos,degrees
from Figures import Polygon, Point, Camera
import random
 
class AreaCounter:
    def __init__(self,poly):
        self.polygon = poly       
        self.minX = min(self.polygon.vertices, key=lambda v: v.x)
        self.maxX = max(self.polygon.vertices, key=lambda v: v.x)
        self.minY = min(self.polygon.vertices, key=lambda v: v.y)
        self.maxY = max(self.polygon.vertices, key=lambda v: v.y)
    def countAreaCoveredByComeras(self,numberOfPoints):
        pointsInPolygon = 0
        pointsWatched = 0
        for i in range(numberOfPoints):
            point = self.pointInPolygonGenerator()
            if(self.isPointInPolygon(point)):
                pointsInPolygon +=1
                if(self.isPointInAllCameraView(point)) :
                    pointsWatched +=1
        return pointsWatched/pointsInPolygon
        #return pointsInPolygon
    def pointInPolygonGenerator(self) :
      x = random.uniform(self.minX.x,self.maxX.x)
      y = random.uniform(self.minY.y,self.maxY.y)
      return Point(y,x)             
    def isPointInPolygon(self,checkPoint ):
        cross = 0
        n = len(self.polygon.vertices)
        for i in range(n):
            if self.isEdgeCrossingWithPointLine(checkPoint,self.polygon.vertices[i],self.polygon.vertices[(i+1)%n]):
                if self.isCrossingOnRightSiedeOfPoint(checkPoint,self.polygon.vertices[i],self.polygon.vertices[(i+1)%n]):
                    cross+=1
        return cross%2 != 0 
    def isPointInAllCameraView(self,point):
        for camera in self.polygon.cameras:
            if not self.isPointInCameraRange(point, camera):
                return False
            if not self.isPointInCameraAngle(point,camera):
                return False
            if self.isAnyEdgeBeetwenCameraAndPoint(point, camera):
                return False
        return True
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
        if c.x<p.x :
            alpha+=180
        
        ####kąty
        #return (c.direction <= alpha and c.direction + c.alpha >= alpha)
        alphaPrim = alpha - c.direction
        return (c.alpha >= alphaPrim and alphaPrim>=0) or (alphaPrim < 0 and 360 - alphaPrim < c.alpha )
    def isAnyEdgeBeetwenCameraAndPoint(self,point,camera):
        p = point
        c = camera
        n = len(self.polygon.vertices)
        for i in range(n):
            v1 = self.polygon.vertices[i]
            v2 = self.polygon.vertices[(i+1)%n]
            if v1.x != v2.x and not(c.y == p.y and v1.y == v2.y):
                difV = (v1.y-v2.y)/(v1.x-v2.x) 
                difCP = (c.y-p.y)/(c.x+p.y)
                x = (v1.y-difV*v1.x-difCP*c.x)/(difCP - difV)
                y = difCP*x + c.y - difCP*c.x
                return self.between(x,c.x,p.x)  and self.between(y,c.y,p.y)
            if c.y == p.y and v1.y == v2.y:
                return False
            if v1.x == v2.x:
                difCP = (c.y-p.y)/(c.x+p.y)
                x = v1.x
                y = difCP*x + c.y - difCP*c.x
                return self.between(x,c.x,p.x)  and self.between(y,c.y,p.y)
    def between(self,x,firstValue,secondValue):
        if firstValue > secondValue:
            return x <= firstValue and x >= secondValue
        if firstValue < secondValue:
            return x >= firstValue and x <= secondValue
        if firstValue == secondValue:
            return x == firstValue
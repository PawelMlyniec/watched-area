import random
from Figures import *
from math import atan2
from AreaCounter import *


class PolygonGenerator:
    def __init__(self):
        pass

    def createPolygon(self, parameters):
        vertices = parameters[0]
        cameras = parameters[1]
        directions = parameters[2]
        angles = parameters[3]
        ranges = parameters[4]
        verticesList = []
        cameraList = []
        for i in range(0,len(vertices),2):
            verticesList.append(Point(vertices[i],vertices[i+1]))
        for i in range(0,len(cameras)-1,2):
            cameraList.append(Camera(cameras[i],cameras[i+1],directions[int(i/2)],angles[int(i/2)],ranges[int(i/2)]))
        return Polygon(verticesList, cameraList)

    def generatePolygon(self, numberOfVeritices, scale, numberOfcameras):

        vertices = self.generateRandomConvexPolygon(numberOfVeritices, scale)
        polygon = Polygon(vertices, [])
        areaCounter = AreaCounter()
        for i in range(numberOfcameras):
            point = areaCounter.pointInPolygonGenerator(polygon)
            camera2 = Camera(point.x, point.y, 0, 180, scale*5)
            camera = Camera(point.y, point.x, 360, 359, scale*200)
            # polygon.addCamera(camera)
            polygon.addCamera(camera2)
        return polygon

    def generateRandomConvexPolygon(self, numberOfVeritices, scale):
        n = numberOfVeritices

        xPool = self.generateSortedRandomCoordinatsList(n)
        yPool = self.generateSortedRandomCoordinatsList(n)

        minMaxX = self.isolateExtremePoints(xPool)
        minMaxY = self.isolateExtremePoints(yPool)
        minX = minMaxX[0]
        maxX = minMaxX[1]
        minY = minMaxY[0]
        maxY = minMaxY[1]

        xPoints = self.divideInteriorPointsIntoTwoChains(xPool, minX, maxX)
        yPoints = self.divideInteriorPointsIntoTwoChains(yPool, minY, maxY)
        vectors = self.createSortedRandomListOfVectors(xPoints, yPoints)
        verices = self.connectVectorsIntoPolyghon(vectors, minX, minY, scale)
        return verices

    def generateSortedRandomCoordinatsList(self, numberOfVeritices):
        n = numberOfVeritices
        listToPopulate = []
        for i in range(n):
            listToPopulate.append(random.random())
        listToPopulate.sort()
        return listToPopulate

    def isolateExtremePoints(self, pool):
        minInPool = pool[0]
        maxInPool = pool[-1]
        return [minInPool, maxInPool]

    def divideInteriorPointsIntoTwoChains(self, listToDivide, minCoordinate, maxCoordinate):
        resultList = []
        lastGreater = minCoordinate
        lastSmaller = minCoordinate
        for i in listToDivide[1:-2]:
            if(random.getrandbits(1)):
                resultList.append(i - lastGreater)
                lastGreater = i
            else:
                resultList.append(lastSmaller - i)
                lastBottom = i
        resultList.append(maxCoordinate - lastGreater)
        resultList.append(lastSmaller - maxCoordinate)
        return resultList

    def createSortedRandomListOfVectors(self, xPoints, yPoints):
        listToPopulate = []
        random.shuffle(yPoints)
        for i in range(len(xPoints)):
            listToPopulate.append(Point(xPoints[i], yPoints[i]))
        listToPopulate = sorted(listToPopulate, key=lambda v: atan2(v.x, v.y))
        return listToPopulate

    def connectVectorsIntoPolyghon(self, vectors, minX, minY, scale):
        x = 0
        y = 0
        minPolygonX = 0
        minPolygonY = 0
        points = []
        for i in vectors:
            points.append(Point(y, x))
            x += i.x
            y += i.y
            minPolygonX = min(minPolygonX, x)
            minPolygonY = min(minPolygonY, y)
        xShift = minX - minPolygonX
        yShift = minY - minPolygonY
        for i in range(len(points)):
            p = points[i]
            newPoint = Point((p.y + yShift)*scale, (p.x + xShift)*scale)
            points[i] = newPoint

        return points

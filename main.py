from polygonGenerator import *
from Figures import *



point1 = Point(0,0)
point2 = Point(0,4)
point3 = Point(4,4)
point4 = Point(4,0)
camera = Camera(2,2,45,90,4)
camera2 = Camera(2,0.00001,225,90,8)
polygon = Polygon([],[])
polygon.addVertice(point1)
polygon.addVertice(point2)
polygon.addVertice(point3)
polygon.addVertice(point4)
#polygon.addCamera(camera)
polygon.addCamera(camera2)
areaCounter = AreaCounter(polygon)
i = areaCounter.countAreaCoveredByComeras(10000)
print(i)

p = PolygonGenerator().generatePolygonWithCameras(4,1,1000)

points = AreaCounter(p).countAreaCoveredByComeras(10000)
print(points)
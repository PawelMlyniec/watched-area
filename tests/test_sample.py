from Figures import *
from AreaCounter import *
from polygonGenerator import *
# content of test_sample.py
pointOut = Point(0, 0)
pointIn = Point(3, 2.5)
point1 = Point(0, 2)
point2 = Point(0, 4)
point3 = Point(4, 4)
point4 = Point(4, 2)
camera = Camera(3, 3, 90, 180, 4)
polygon = Polygon([],[])
polygon.addVertice(point1)
polygon.addVertice(point2)
polygon.addVertice(point3)
polygon.addVertice(point4)
polygon.addCamera(camera)
areaCounter = AreaCounter()


def test_pointCreation():
    assert pointOut.x == 0 and pointOut.y == 0


def test_cameraCreation():
    assert camera.x == 3 and camera.y == 3


def test_whenPointIsAddedToPolighonItIsStoredAsVertice():
    assert polygon.vertices[0] == point1


def test_whenCameraIsAddedToPolighonIsStoredAsCamera():
    assert polygon.cameras[0] == camera


def test_givenPointOutOfPolygonProgramSaysItIsOut():
    assert areaCounter.isPointInPolygon(polygon,pointOut) == False


def test_givenPointInPolygonProgramSaysItIsIn():
    assert areaCounter.isPointInPolygon(polygon,pointIn) == True


def test_givenPointOnEdgesHightLineFromItToXInfCrossesWithEdge():
    assert areaCounter.isEdgeCrossingWithPointLine(
        pointIn, point2, point3) == True


def test_givenPointNotOnEdgesHightLineFromItToXInfIsNotCrossingWithEdge():
    # todo other case
    assert areaCounter.isEdgeCrossingWithPointLine(
        pointOut, point4, point1) == True


def test_givenPointLineAndEdgeCorossingPointIsReturned():
    assert areaCounter.whereEdgesAreCrossingWithPointLine(
        pointIn, point2, point3) == 4


def test_givenCrossingOnRightSideOfPointFunctionReturnsTrue():
    assert areaCounter.isCrossingOnRightSiedeOfPoint(
        pointIn, point2, point3) == True


def test_givenCrossingOnLeftSideOfPointFunctionReturnsFalse():
    assert areaCounter.isCrossingOnRightSiedeOfPoint(
        pointIn, point4, point1) == False


def test_givenPointInCameraViewreturnsTrue():
    assert areaCounter.isPointInAllCameraView(pointIn, camera) == True


def test_givenPointNotInCameraViewreturnsFalse():
    assert areaCounter.isPointInAllCameraView(pointOut, camera) == False


def test_givenPointInCameraRangeReturnsTrue():
    assert areaCounter.isPointInCameraRange(pointIn, camera) == True


def test_givenPointNotInCameraRangeReturnsFalse():
    assert areaCounter.isPointInCameraRange(pointOut, camera) == False


def test_givenPointInCameraAngelReturnsTrue():
    assert areaCounter.isPointInCameraAngle(pointIn, camera) == True


def test_givenPointNotInCameraAngelReturnsFalse():
    assert areaCounter.isPointInCameraAngle(pointOut, camera) == False


def test_givenPointWithoutEdgeBeetweenCameraAndPointReturnsTrue():
    assert areaCounter.isAnyEdgeBeetwenCameraAndPoint(polygon,pointIn, camera) == False


def test_givenPointWithEdgeBeetweenCameraAndPointReturnsFalse():
    pass  # TODO




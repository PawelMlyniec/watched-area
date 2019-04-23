from aal import *

# content of test_sample.py
pointOut = Point(0,0)
pointIn = Point(2.5,3)
point1 = Point(2,0)
point2 = Point(4,0)
point3 = Point(4,4)
point4 = Point(2,4)
camera = Camera(3,3,90,180,4)
polyghon = Polyghon()
polyghon.addVertice(point1)
polyghon.addVertice(point2)
polyghon.addVertice(point3)
polyghon.addVertice(point4)
polyghon.addCamera(camera)
def test_pointCreation():
    assert pointOut.x == 0 and pointOut.y == 0
def test_cameraCreation():
    assert camera.x == 2 and camera.y ==2
def test_whenPointIsAddedToPolighonItIsStoredAsVertice():
    assert polyghon.vertices[0] == point
def test_whenCameraIsAddedToPolighonIsStoredAsCamera():
    assert polyghon.cameras[0] == camera
def test_givenPointOutOfPolyghonProgramSaysItIsOut():
    assert polyghon.isPointInPolyghon(pointOut) == False
def test_givenPointInPolyghonProgramSaysItIsIn():
    assert polyghon.isPointInPolyghon(pointIn) == True
def test_givenPointOnEdgesHightLineFromItToXInfCrossesWithEdge():
    assert polyghon.isEdgeCrossingWithPointLine(pointIn,point2,point3) == True
def test_givenPointNotOnEdgesHightLineFromItToXInfIsNotCrossingWithEdge():
    assert polyghon.isEdgeCrossingWithPointLine(pointOut,point4,point1) == False
def test_givenPointLineAndEdgeCorossingPointIsReturned():
    assert polyghon.whereEdgesAreCrossingWithPointLine(pointIn,point2,point3) == {3,2}
def test_givenCrossingOnRightSideOfPointFunctionReturnsTrue():
    assert polyghon.isCrossingOnRightSiedeOfPoint({3,2},pointIn) == True
def test_givenCrossingOnLeftSideOfPointFunctionReturnsFalse():
    assert polyghon.isCrossingOnRightSiedeOfPoint({2,3},pointIn) == False
def test_givenPointInCameraViewreturnsTrue():
    assert polyghon.isPointInAnyCameraView(pointIn,camera) == True
def test_givenPointNotInCameraViewreturnsFalse():
    assert polyghon.isPointInAnyCameraView(pointOut,camera) == False
def test_givenPointInCameraRangeReturnsTrue():
    assert polyghon.isPointInCameraRange(pointIn,camera) == True
def test_givenPointNotInCameraRangeReturnsFalse():
    assert polyghon.isPointInCameraRange({-4,-4},camera) == False
def test_givenPointInCameraAngelReturnsTrue():
    assert polyghon.isPointInCameraAngle(pointIn, camera) == True
def test_givenPointNotInCameraAngelReturnsFalse():
    assert polyghon.isPointInCameraAngle(pointOut, camera) == False
def test_givenPointWithoutEdgeBeetweenCameraAndPointReturnsTrue():
    assert polyghon.isAnyEdgeBeetwenCameraAndPoint(pointIn, camera)
def test_givenPointWithEdgeBeetweenCameraAndPointReturnsFalse():
    pass #TODO




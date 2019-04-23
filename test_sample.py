from aal import *

# content of test_sample.py
pointOut = Point(0,0)
pointIn = Point(3,2.5)
point1 = Point(0,2)
point2 = Point(0,4)
point3 = Point(4,4)
point4 = Point(4,2)
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
    assert camera.x == 3 and camera.y ==3
def test_whenPointIsAddedToPolighonItIsStoredAsVertice():
    assert polyghon.vertices[0] == point1
def test_whenCameraIsAddedToPolighonIsStoredAsCamera():
    assert polyghon.cameras[0] == camera
def test_givenPointOutOfPolyghonProgramSaysItIsOut():
    assert polyghon.isPointInPolyghon(pointOut) == False
def test_givenPointInPolyghonProgramSaysItIsIn():
    assert polyghon.isPointInPolyghon(pointIn) == True
def test_givenPointOnEdgesHightLineFromItToXInfCrossesWithEdge():
    assert polyghon.isEdgeCrossingWithPointLine(pointIn,point2,point3) == True
def test_givenPointNotOnEdgesHightLineFromItToXInfIsNotCrossingWithEdge():
    #todo other case
    assert polyghon.isEdgeCrossingWithPointLine(pointOut,point4,point1) == True
def test_givenPointLineAndEdgeCorossingPointIsReturned():
    assert polyghon.whereEdgesAreCrossingWithPointLine(pointIn,point2,point3) == 4
def test_givenCrossingOnRightSideOfPointFunctionReturnsTrue():
    assert polyghon.isCrossingOnRightSiedeOfPoint(pointIn,point2,point3) == True
def test_givenCrossingOnLeftSideOfPointFunctionReturnsFalse():
    assert polyghon.isCrossingOnRightSiedeOfPoint(pointIn,point4,point1) == False

def test_givenPointInCameraViewreturnsTrue():
    assert polyghon.isPointInAllCameraView(pointIn,camera) == True
def test_givenPointNotInCameraViewreturnsFalse():
    assert polyghon.isPointInAllCameraView(pointOut,camera) == False
def test_givenPointInCameraRangeReturnsTrue():
    assert polyghon.isPointInCameraRange(pointIn,camera) == True
def test_givenPointNotInCameraRangeReturnsFalse():
    assert polyghon.isPointInCameraRange(pointOut,camera) == False
def test_givenPointInCameraAngelReturnsTrue():
    assert polyghon.isPointInCameraAngle(pointIn, camera) == True
def test_givenPointNotInCameraAngelReturnsFalse():
    assert polyghon.isPointInCameraAngle(pointOut, camera) == False
def test_givenPointWithoutEdgeBeetweenCameraAndPointReturnsTrue():
    assert polyghon.isAnyEdgeBeetwenCameraAndPoint(pointIn, camera) == False
def test_givenPointWithEdgeBeetweenCameraAndPointReturnsFalse():
    pass #TODO




from polygonGenerator import *
from Figures import *
from view import *
from AreaCounter import *
import time

def main():
    view = View()
    polygonGenerator = PolygonGenerator()
    areaCounter = AreaCounter()
    view.scan()
   
    if view.isGeneration():
        parameters = view.generationOption()
        numberVertices = parameters[0]
        scale = parameters[1]
        numberCameras = parameters[2]
        angle = parameters[3]
        numberOfPoints = parameters[4]
        if view.isTimeMesuring():
            i = 4
            while i  < numberVertices:
                polygon = polygonGenerator.generatePolygon(i,scale,numberCameras)
                start = time.time()
                p = areaCounter.countAreaCoveredByComeras(polygon,numberOfPoints)
                end = time.time()
                view.print(p,i,end-start)
                i *=2
            polygon = polygonGenerator.generatePolygon(numberVertices,scale,numberCameras)
            start = time.time()
            p = areaCounter.countAreaCoveredByComeras(polygon,numberOfPoints)
            end = time.time()
            view.print(p,numberVertices,end-start)
        else:
            polygon = polygonGenerator.generatePolygon(numberVertices,scale,numberCameras)
            p = areaCounter.countAreaCoveredByComeras(polygon,numberOfPoints)
            view.print(p,numberVertices)
    else :
        parameters = view.notGenerationOption()
        numberOfPoints = parameters[-1]
        polygon = polygonGenerator.createPolygon(parameters)
        if view.isTimeMesuring():
            start = time.time()
            p = areaCounter.countAreaCoveredByComeras(polygon,numberOfPoints)
            end = time.time()
            view.print(p,)

    
if __name__ == "__main__":
    main()

import sys


class View:
    def __init__(self):
        self.generationFlag = False
        self.timeMesuringFlag = False
        self.readFromFileFlag = False
        self.writeIntoFileFlag = False

    def scan(self):

        if sys.argv[1] == '-h':
            print(
                "Default: uses std input/output youtimeMesurinOption()an redirect stream from/into file")
            print("Options for program:")
            print("\t Files: (have to be before flags)")
            print(
                "\t [file name] for reading from file and output on standard output")
            print(
                "\t [input file name] [output file name] for input form file and autput into file")
            print("Flags:")
            print("\t -h for help")
            print("\t -g for automatic generation of data")
            print("\t -t for time measuring and presentation of results. Combined with -g flag mesures time for growing complexity  ")
            exit(0)
        else:
            if '-g' in sys.argv[1:]:
                self.generationFlag = True
            if '-t' in sys.argv[1:]:
                self.timeMesuringFlag = True
            if self.canReadFromFile():
                self.readFromFileFlag = True
            if len(sys.argv) > 2:
                if sys.argv[2] != '-h' and sys.argv[2] != '-t':
                    self.writeIntoFileFlag = True

    def isGeneration(self):
        return self.generationFlag

    def generationOption(self):
        while True:
            try:

                vertices = int(input("Insert nuber of vertices: "))

                scale = float(input("Insert scale of polygon: "))

                cameras = int(input("Insert number of cameras: "))

                angle = float(input("Insert avarage angle of cameras: "))

                points = int(input("Insert nuber of monte carlo points: "))
                break
            except ValueError:
                print("Insert proper values")

        return (vertices, scale, cameras, angle, points)

    def notGenerationOption(self):
        if not self.isReadingFromFile():
            while True:
                try:
                    vertices = [float(x) for x in input(
                        "Insert list of coordinats of vertices").split()]
                    #scale = float(input("Insert scale of polygon: "))
                    cameras = [float(x) for x in input(
                        "Insert list of coordinats of cameras").split()]
                    directions = [float(x) for x in input(
                        "Insert list of directions of cameras").split()]
                    angles = [float(x) for x in input(
                        "Insert list of angles of cameras").split()]
                    ranges = [float(x) for x in input(
                        "Insert list of ranges of cameras").split()]
                    numberOfPoints = int(
                        input("Insert number of monte carlo points: "))
                    if not (len(cameras)/2 == len(directions) == len(angles) == len(ranges)):
                        raise ValueError
                    break
                except ValueError:
                    print("Insert proper values!")
        else:
            r = self.readFromFile()
            try:
                vertices = [float(x)
                            for x in list(r.readline().strip().split())]
                cameras = [float(x) for x in r.readline().split()]
                directions = [float(x) for x in r.readline().split()]
                angles = [float(x) for x in r.readline().split()]
                ranges = [float(x) for x in r.readline().split()]
                numberOfPoints = int(r.readline())
                r.close()
            except ValueError:
                sys.stderr.write("Error while reading file")
        return (vertices,  cameras, directions, angles, ranges, numberOfPoints)

    def isTimeMesuring(self):
        return self.timeMesuringFlag

    def isReadingFromFile(self):
        return self.readFromFileFlag

    def isWriteIntoFile(self):
        return self.writeIntoFileFlag

    def canReadFromFile(self):
        try:
            r = open(sys.argv[1], 'r')
        except:
            return False
        r.close()
        return True

    def readFromFile(self):
        r = open(sys.argv[1], 'r')
        return r

    def writeIntoFile(self, string):
        try:
            w = open(sys.argv[2], 'a')
            w.write(string)
            w.close()
            return True
        except:
            return False

    def print(self, result, vertices, time):
        if self.readFromFileFlag:
            resultStr = "For polygon defined in file: " + \
                str(sys.argv[1]) + "with number of verices: " + \
                str(vertices) + " time was: " + str(time)
        else:
            resultStr = "For generated polygon with number of verices: " + \
                str(vertices) + " time was: " + \
                str(time) + " and result: " + str(result)
        if self.writeIntoFileFlag:
            self.writeIntoFile(resultStr)
        else:
            print(resultStr)

    def print(self, result, vertices):
        if self.readFromFileFlag:
            resultStr = "For polygon defined in file: " + \
                str(sys.argv[1]) + "with number of verices: " + \
                str(vertices) + " result is " + str(result)
        else:
            resultStr = "For generated polygon with number of verices: " + \
                str(vertices) + " result is: " + str(result)
        if self.writeIntoFileFlag:
            self.writeIntoFile(resultStr)
        else:
            print(resultStr)

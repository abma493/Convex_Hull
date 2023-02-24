import os
from Point import Point
from Line import Line

class ConvexHull:


    def __init__(self, filename):
        self.convexPoints = []
        self.results = filename 
        self.input = open(filename, 'w')

    def convexHull(self, points) -> list:

        if len(points) == 2:
            return [points[0], points[1]]
        elif len(points) == 3:
            if self.pointIsAboveLine(Line(points[0],points[2]), 
                                     points[1]):
                return [points[0], points[1], points[2]]


        hlf_sz = int(len(points) / 2)
        pointsA = points[:hlf_sz]
        pointsB = points[hlf_sz:]
        # Recursive divide the subarrays
        sub_convexA = self.convexHull(pointsA)
        sub_convexB = self.convexHull(pointsB)

        print(f'subConvexA')
        for i in range(len(sub_convexA)):
            print(sub_convexA[i])
        
        print(f'subConvexB')
        for i in range(len(sub_convexB)):
            print(sub_convexB[i])
        
        self.computeHull(sub_convexA, sub_convexB)

        return[]


    # o(n)
    def computeHull(self, arrayA, arrayB):
        print(arrayA, arrayB)
        #Testing lowerTangent()
        # if len(arrayA)==0:
        #     return

        # print('Testing lowerTangent():')
        # lowerTan = self.lowerTangent(arrayA, arrayB)
        # print('P: ', lowerTan.p1, ' Q: ', lowerTan.p2, ' eq: ', lowerTan)
         
        self.computeHull(sub_convexA, sub_convexB, pointsA[len(pointsA) - 1], pointsB[0])


    # o(n)
    def computeHull(self, arrayA: list, arrayB: list, rightMostPoint: Point, leftMostPoint: Point):
        upperTangent = self.findUpperTangent(leftMostPoint, rightMostPoint, arrayA, arrayB)
        assert isinstance(upperTangent, Line)

    def findUpperTangent(self, point_L: Point, point_R: Point, arrayA: list, arrayB: list) -> Line:
        myLine = Line(point_L, point_R)
        isTangentA = bool(False)
        isTangentB = bool(False)

        while(isTangentA is False and isTangentB is False):
            
            while(isTangentA is False):
                i_chk = arrayA.index(Line.getPoint2(myLine)) - 1
                if i_chk < 0:
                    isTangentA = bool(True)
                else:
                    if self.pointIsAboveLine(myLine, arrayA.__getitem__(i_chk)) is not True:
                        isTangentA = True
                    Line.setPoint2(myLine, arrayA.__getitem__(i_chk))
                

            print(f'upper tangent right: {Line.getPoint2(myLine)} {isTangentA}')

            while(isTangentB is False):
                i_chk = arrayB.index(Line.getPoint1(myLine)) + 1
                if i_chk >= len(arrayB):
                    isTangentB = bool(True)
                else:
                    print(myLine)
                    print(arrayB.__getitem__(i_chk))
                    if self.pointIsAboveLine(myLine, arrayB.__getitem__(i_chk)) is not True:
                        isTangentB = True
                    Line.setPoint2(myLine, arrayB.__getitem__(i_chk))
            
            print(f'upper tangent left: {Line.getPoint2(myLine)} {isTangentB}')
        return myLine


    def pointIsAboveLine(self, line: Line, point: Point) -> bool:
        yLine = float(Line.getSlope(line) * Point.getX(point) + Line.getY_Intercept(line))
        return bool(Point.getY(point) > yLine)

    #Function for finding the lower tangent
    #Returns a Line object
    def lowerTangent(self, pointsA: list, pointsB: list):

        #P is the right-most point of A
        print(len(pointsA)-1)
        pointP = pointsA[len(pointsA)-1]
        #Q is the left-most point of B
        pointQ = pointsB[0]

        #Fix point P
        linePQ = Line(pointP, pointQ)
        indexQNeighbor = 1
        QNeighbor = pointsB[indexQNeighbor]
        while self.pointIsAboveLine(linePQ,QNeighbor)==False:
            pointQ = pointsB[indexQNeighbor]
            linePQ = Line(pointP, pointQ)
            indexQNeighbor += 1
            if indexQNeighbor>=len(pointsB):
                break
            QNeighbor = pointsB[indexQNeighbor]
        pointT2 = pointQ

        #Fix point Q
        pointQ = pointsB[0]
        linePQ = Line(pointP, pointQ)
        indexPNeighbor = len(pointsA)-2
        PNeighbor = pointsA[indexPNeighbor]
        while self.pointIsAboveLine(linePQ,PNeighbor)==False:
            pointP = pointsA[indexPNeighbor]
            linePQ = Line(pointP, pointQ)
            indexPNeighbor -= 1
            if indexPNeighbor<0:
                break
            PNeighbor = pointsA[indexPNeighbor]
        pointT1 = pointP

        #Return lower tangent line
        return Line(pointT1, pointT2)


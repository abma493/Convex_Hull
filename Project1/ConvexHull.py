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
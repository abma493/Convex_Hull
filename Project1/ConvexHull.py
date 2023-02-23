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
        pointsA = points[hlf_sz:]
        pointsB = points[:hlf_sz]

        # Recursive divide the subarrays
        sub_convexA = self.convexHull(pointsA)
        sub_convexB = self.convexHull(pointsB)

        print(f'current arr len: {len(points)}')

        for i in range(len(sub_convexA)):
            print(sub_convexA[i])
        
        for i in range(len(sub_convexB)):
            print(sub_convexB[i])
        
        return []; 
        #self.computeHull(self, sub_convexA, sub_convexB)


    # o(n)
    def computeHull(self, arrayA, arrayB):
        print(arrayA, arrayB)

    def pointIsAboveLine(self, line: Line, point: Point):
        yLine = float(Line.getSlope(line) * Point.getX(point) + Line.getY_Intercept(line))
        return bool(Point.getY(point) > yLine)
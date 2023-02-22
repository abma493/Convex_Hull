import os
from Point import Point
from Line import Line

class ConvexHull:


    def __init__(self, filename, points):
        self.results = filename
        self.points = points 
        self.input = open(filename, 'w')

    def convexHull(self):
        
        if len(self.points) == 2:
            return Point.__init__(self.points[0], self.points[1])
        elif len(self.points) == 3:
            print("Base case size 3")

        pointsA = []
        pointsB = []

        leftHalfSz = len(self.points) / 2

        for i in range(leftHalfSz):
            pointsA.append(self.points[i])
        
        rightHalfSz = len(self.points) - leftHalfSz
        
        for j in range(rightHalfSz):
            pointsB.append(self.points[j + (rightHalfSz - 1)])
        

        # Recursive divide the subarrays
        self.convexHull(pointsA)
        self.convexHull(pointsB)

        #self.computeHull()


    # o(n)
    def computeHull(self, arrayA, arrayB):
        print(arrayA, arrayB)

    def pointIsAboveLine(line, point):
        yLine = float(Line.getSlope(line) * Point.getX(point) + Line.getY_Intercept(line))
        return bool(Point.getY(point) > yLine)
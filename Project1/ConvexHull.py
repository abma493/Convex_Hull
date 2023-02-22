import os
from Point import Point
from Line import Line

class ConvexHull:
    def __init__(self, filename, points):
        self.results = filename
        self.points = points
        self.input = open(filename, 'w')

    def convexHull(self, points):
        
        if len(points) == 2:
            return Point.__init__(points[0], points[1])
        elif len(points) == 3:
            print("Base case size 3")
        #2 convex hulls
        pointsA = []
        pointsB = []

        #Divide points into 2 halves
        leftHalfSz = len(points) / 2
        for i in range(leftHalfSz):
            pointsA.append(points[i])
        
        rightHalfSz = len(points) - leftHalfSz
        for j in range(rightHalfSz):
            pointsB.append(points[j + (rightHalfSz - 1)])
        

        # Recursive divide the subarrays
        self.convexHull(pointsA)
        self.convexHull(pointsB)

        self.computeHull()

    #Merge halves, obtaining convexhulls.
    def computeHull():
        print()

    def pointIsAboveLine(line, point):
        yLine = float(Line.getSlope(line) * Point.getX(point) + Line.getY_Intercept(line))
        return bool(Point.getY(point) > yLine)
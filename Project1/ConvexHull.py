import os
from Point import Point
from Line import Line

class ConvexHull:


    def __init__(self, filename):
        self.convexPoints = []
        self.results = filename 

    def writeToFile(self, convexList, sortedX):
        input = open(self.results, 'w')
        for convexPoint in convexList:
            index = sortedX.index(Point.getX(convexPoint))
            input.write('{index}\n'.format(index=str(index)))
        input.close()
            





    def convexHull(self, points):

        if len(points) == 2:
            return [points[0], points[1]]
        elif len(points) == 3:
            if self.pointIsAboveLine(Line(points[0],points[2]), 
                                     points[1]):
                return [points[0], points[1], points[2]]
            else:
                return [points[0], points[2], points[1]]


        hlf_sz = int(len(points) / 2)
        pointsA = points[:hlf_sz]
        pointsB = points[hlf_sz:]
        # Recursive divide the subarrays
        convexA = self.convexHull(pointsA)
        convexB = self.convexHull(pointsB)

        print("-----------------")
        if convexA is not None:
            print('subConvexA')
            for i in range(len(convexA)):
                print('{convexA} vs original {pointsA}'.format(convexA=convexA[i],pointsA=pointsA[i]))
        if convexB is not None: 
            print('subConvexB')
            for i in range(len(convexB)):
                print('{convexB} vs original {pointsB}'.format(convexB=convexB[i],pointsB=pointsB[i]))
        print()

        mergeList = self.computeHull(convexA, convexB) # merge subconvex of A and B !!!
        
        print("Displaying merged Convex Hull")
        for i in mergeList:
            print(i)
        
        return mergeList


    # o(n)
    def computeHull(self, pointsA, pointsB):
        upperTan = self.upperTangent(pointsA, pointsB)
        print(upperTan)
        print("upperTan DONE.\n")
        lowerTan = self.lowerTangent(pointsA, pointsB)
        print(lowerTan)
        print("lowerTan DONE.\n")

        self.convexPoints = [] # reset the list until the last time this function gets called.

        if Point.getX(pointsA[0]) != Point.getX(Line.getPoint1(upperTan)):
            self.convexPoints.append(pointsA[0]) # start at first clockwise point of sub-convex A
            i = 1 # counter for A
            # get to the x-coordinate of the upperTan and add any hull points in between, if any
            while i in range(len(pointsA)) and Point.getX(pointsA[i]) != Point.getX(Line.getPoint1(upperTan)):
                self.convexPoints.append(pointsA[i])
                i += 1
               
        self.convexPoints.append(Line.getPoint1(upperTan)) # now connect the upper tan p1 to hull ordered list
        upperTanP2 = Line.getPoint2(upperTan)
        self.convexPoints.append(upperTanP2) # add the connecting upper tan p2 to the convex hull ordered list

        i = pointsB.index(upperTanP2) + 1 # one point in the sub ordered list of B that is connected right after upper tan p2 
        while i in range(len(pointsB)) and Point.getX(pointsB[i]) != Point.getX(Line.getPoint2(lowerTan)):
            self.convexPoints.append(pointsB[i])   
            i += 1
   

        # add the lower tan p2 to the total list
        self.convexPoints.append(Line.getPoint2(lowerTan))
        
        if not self.convexPoints.__contains__(Line.getPoint1(lowerTan)):
            self.convexPoints.append(Line.getPoint1(lowerTan))

        k = pointsA.index(Line.getPoint1(lowerTan)) + 1 # one ahead of the lower tan p1 point in the sub ordered hull list of A
        while k in range(len(pointsA)) and not self.convexPoints.__contains__(pointsA[k]):
            self.convexPoints.append(pointsA[k])
            k += 1
        
        return self.convexPoints


    def upperTangent(self, pointsA, pointsB):

        # Point P is the rightmost point of A
        pointP = self.findRightmost(pointsA)
        # Point Q is the leftmost point of B
        pointQ = self.findLeftMost(pointsB)

        # initial line (to be tested against other points)
        linePQ = Line(pointP, pointQ)

        indexP_ngbor = pointsA.index(pointP) - 1
        P_Neighbor = pointsA[indexP_ngbor]
        while self.pointIsAboveLine(linePQ, P_Neighbor) is True:
            
            pointP = P_Neighbor
            Line.setPoint1(linePQ, pointP) # update the line
            
            if indexP_ngbor - 1 in range(len(pointsA)):
                indexP_ngbor -= 1 # counter-clockwise
            else: 
                break
            P_Neighbor = pointsA[indexP_ngbor]

        indexQ_ngbor = pointsB.index(pointQ) + 1
        Q_Neighbor = pointsB[indexQ_ngbor]
        while self.pointIsAboveLine(linePQ, Q_Neighbor) is True:
            pointQ = Q_Neighbor
            Line.setPoint2(linePQ, pointQ) # update the line

            if indexQ_ngbor + 1 in range(len(pointsB)):
                indexQ_ngbor += 1 # clockwise
            else:
                break
            Q_Neighbor = pointsB[indexQ_ngbor]
            if Point.getX(Q_Neighbor) == 2.0:
                print(Q_Neighbor)
        
        return linePQ

    def lowerTangent(self, pointsA, pointsB):

        # Point P is the rightmost point of A
        pointP = self.findRightmost(pointsA)
        # Point Q is the leftmost point of B
        pointQ = self.findLeftMost(pointsB)

        # initial line (to be tested against other points)
        linePQ = Line(pointP, pointQ)

        indexP_ngbor = pointsA.index(pointP) - 1
        P_Neighbor = pointsA[indexP_ngbor]
        while self.pointIsAboveLine(linePQ, P_Neighbor) is False:
            pointP = P_Neighbor
            Line.setPoint1(linePQ, pointP)
            if indexP_ngbor - 1 in range(len(pointsA)):
                indexP_ngbor -= 1
            else:
                break
            P_Neighbor = pointsA[indexP_ngbor]
        
        indexQ_ngbor = pointsB.index(pointQ) + 1
        Q_Neighbor = pointsB[indexQ_ngbor]
        while self.pointIsAboveLine(linePQ, Q_Neighbor) is False:
            pointQ = Q_Neighbor
            Line.setPoint2(linePQ, pointQ)
            
            if indexQ_ngbor + 1 in range(len(pointsB)):
                indexQ_ngbor += 1
            else:
                break
            Q_Neighbor = pointsB[indexQ_ngbor]

        return linePQ



    def pointIsAboveLine(self, line, point):
        yLine = float(Line.getSlope(line) * Point.getX(point) + Line.getY_Intercept(line))
        return bool(Point.getY(point) > yLine)
    

    def findLeftMost(self, pointsList):
        leftMost = pointsList[0]
        for i in pointsList:
            if Point.getX(i) < Point.getX(leftMost):
                leftMost = i
        return leftMost

        
    def findRightmost(self, pointsList):
        rightMost = pointsList[len(pointsList) - 1]
        for i in pointsList:
            if Point.getX(i) > Point.getX(rightMost):
                rightMost = i
        return rightMost
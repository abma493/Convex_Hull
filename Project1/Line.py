from Point import Point

class Line:
    
    #Param(s): Point x, Point Y
    def __init__(self, p1, p2):
        self.slope = None
        self.y_intercept = None
        self.p1 = p1
        self.p2 = p2
        self.createLine(p1, p2)

    # toString function
    def __str__(self):
        return """Line data:\nx1: {Xp1} y1: {Yp1}\n x2: {Xp2} y2: {Yp2}\n slope: {slope} | 
        y-intercept: {yInt}""".format(Xp1=Point.getX(self.p1)
                                    ,Yp1=Point.getY(self.p1) 
                                    ,Xp2=Point.getX(self.p2) 
                                    ,Yp2=Point.getY(self.p2)
                                    ,slope=self.slope
                                    ,yInt=self.y_intercept)

    # not a static method, thus, self is a param to indicate this instance
    # upon invocation by constructor
    # Param(s): Point x, Point y of this class
    def createLine(self, p1, p2):
        self.slope = round(self.computeSlope(p1, p2), 2)
        self.y_intercept = Point.getY(p1) - (self.slope * Point.getX(p1))

    def computeSlope(self, p1, p2):
        return float((Point.getY(p1) - Point.getY(p2)) / (Point.getX(p1) - Point.getX(p2)))
        
    def getSlope(self):
        return self.slope
    
    def getY_Intercept(self):
        return self.y_intercept

    def setPoint1(self, point):
        self.p1 = point
        self.createLine(self.p1, self.p2)

    def setPoint2(self, point):
        self.p2 = point
        self.createLine(self.p1, self.p2)

    def getPoint1(self):
        return self.p1
    
    def getPoint2(self):
        return self.p2
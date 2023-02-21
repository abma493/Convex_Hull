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
        return f"slope: {self.slope}\ny-intercept: {self.y_intercept}"

    # not a static method, thus, self is a param to indicate this instance
    # upon invocation by constructor
    # Param(s): Point x, Point y of this class
    def createLine(self, p1, p2):
        self.slope = self.computeSlope(self, p1, p2)
        self.y_intercept = Point.getY(p1) - (self.slope * Point.getX(p1))

    def computeSlope(self, p1, p2):
        return float((Point.getY(p1) - Point.getY(p2)) / (Point.getX(p1) - Point.getX(p2)))
        
    def getSlope(self):
        return self.slope
    
    def getY_Intercept(self):
        return self.y_intercept
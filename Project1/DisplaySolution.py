import matplotlib.pyplot as plt
import os
from Point import Point
from ConvexHull import ConvexHull

#Input file path
inputFile: str = 'input.csv'
#Open input .csv file
if not os.path.exists(inputFile):
	print('Cannot find '+ inputFile + '.')
	quit()

input = open(inputFile,'r')

x: list = []
y: list = []

#Read each line of the input file.
#Storing the x-coordinates into x.
#Storing the y-coordinates into y.
line: str = input.readline()
while line:
	coordinates: list = line.split(',')
	x.append(float(coordinates[0]))
	y.append(float(coordinates[1]))
	line = input.readline()

input.close()

# Create the array of Point objects
assert len(x) == len(y)
points = []
for i in range(len(x)):
	p = Point(float(x[i]), float(y[i]))
	points.append(p)

# convexHull solution here
convexHull = ConvexHull("output.txt")
convexPoints = ConvexHull.convexHull(convexHull, points)
ConvexHull.writeToFile(convexHull, convexPoints, x)


# ConvexHull.writeToFile(convexPoints, x)



#Adding the input points to the plot so we can visualize what the points look like.
#The scatter() function will draw just the points.
plt.scatter(x,y)



outputFile = 'output.txt'
if os.path.exists(outputFile):
	output = open(outputFile,'r')
	
	convexHullX = []
	convexHullY = []
	
	#The output file should be a list of the indices of the points from the input file that are on the convex hull.
	line = output.readline()
	firstIndex = -1
	while line:
		p = int(line)
		
		#We have to remember the first point so the convex hull can "wrap around" at the end.
		if firstIndex == -1:
			firstIndex = p
			
		convexHullX.append(x[p])
		convexHullY.append(y[p])
		
		line = output.readline()
	output.close()

	#Adding the first point into the list again to complete the convex hull.
	convexHullX.append(x[firstIndex])
	convexHullY.append(y[firstIndex])
	
	#Adding the points of the convex hull to the plot.
	#The plot() function connects the points together with line segments.
	plt.plot(convexHullX,convexHullY)
	
else:
	print("No output file detected.  Only showing the point set.")
	
#Display the points and line segments we have plotted.
plt.show()

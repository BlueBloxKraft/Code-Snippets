from turtle import *

def drawRegPolygon(noOfSides, sideLength):
    if(noOfSides>2):
        for i in range(0, noOfSides):
            forward(sideLength)
            right(360/noOfSides)
    else:
        print("The number of sides can't be less than 3")


drawRegPolygon(1000, 40)

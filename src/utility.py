# Required imports
from src.point import Point
from src.vector import Vector
from src.stem import Stem
import math

# --------------------------------------------------------------
# Utility class
# --------------------------------------------------------------

DEBUG_MODE = 0

class Utility:

    # Compute the scalar product between the two vectors
    def computeScalarBtwVectors(v1, v2):
        return v1.vX * v2.vX + v1.vY * v2.vY

    # Compute the angle between two vectors in radians
    def computeAngleBtwVectors(v1, v2):
        intRes = Utility.computeScalarBtwVectors(v1, v2) / (v1.computeModule() * v2.computeModule())
        return math.acos(intRes)

    # Compute the values of the stem
    def computeStem(xHandlebar, yHandlebar, reach, stack, directionAngle, bearingHeight, spacerHeight, stemHeight):

        # Convert the directionAngle to radians
        directionAngle = directionAngle / 180.0 * math.pi

        # Get alpha, the angle to work with
        alpha = math.pi / 2.0 - directionAngle
        if DEBUG_MODE == 1:
            print("alpha is : " + str(alpha * 180.0 / math.pi))

        # Create the point at the top of the frame
        pFrame = Point(reach, stack, "pFrame")
        if DEBUG_MODE == 1:
            pFrame.toString()

        # Create the Point on the top of the bearing
        xBearing = pFrame.x - (math.sin(alpha) * bearingHeight)
        yBearing = pFrame.y + (math.cos(alpha) * bearingHeight)
        pBearing = Point(xBearing, yBearing, "pBearing")
        if DEBUG_MODE == 1:
            pBearing.toString()

        # Create the Point at the top of the spacer
        xSpacer = pBearing.x - (math.sin(alpha) * spacerHeight)
        ySpacer = pBearing.y + (math.cos(alpha) * spacerHeight)
        pSpacer = Point(xSpacer, ySpacer, "pSpacer")
        if DEBUG_MODE == 1:
            pSpacer.toString()

        # Create the Point at the middle height of the stem
        xMiddleStem = pSpacer.x - (math.sin(alpha) * (stemHeight / 2))
        yMiddleStem = pSpacer.y + (math.cos(alpha) * (stemHeight / 2))
        pMiddleStem = Point(xMiddleStem, yMiddleStem, "pMiddleStem")
        if DEBUG_MODE == 1:
            pMiddleStem.toString()

        # Create the Point of the handlebar
        pHandlebar = Point(xHandlebar, yHandlebar, "pHandlebar")
        if DEBUG_MODE == 1:
            pHandlebar.toString() 

        # Create the Vector between the Point of the middle height of the stem and the point of the handlebar
        vStem = Vector(pMiddleStem, pHandlebar, "vStem")
        if DEBUG_MODE == 1:
            vStem.toString()

        # Create the Vector between the Point of the middle height of the stem and the Point of the top of the frame 
        vDirection = Vector(pMiddleStem, pFrame, "vDirection")
        if DEBUG_MODE == 1:
            vDirection.toString()

        # Compute the angle between the two Vectors
        beta = Utility.computeAngleBtwVectors(vStem, vDirection)
        beta = beta * 180 / math.pi
        if DEBUG_MODE == 1:
            print("")
            print("")
            print("the angle after calculation is : \t\t" + str(beta))
        angleStem = 180
        if beta < 90 and beta > 0: 
            angleStem = - (90 - beta)
        elif beta > 90 and beta < 180:
            angleStem = beta - 90

        # Compute the length of the stem
        lengthStem = vStem.computeModule()
        if DEBUG_MODE == 1:
            print("the length of the stem after calculation is : \t" + str(lengthStem))

        # Create the Stem
        stem = Stem(round(lengthStem, 1), round(angleStem, 1))
        if DEBUG_MODE == 1:
            stem.toString()
        return stem
  




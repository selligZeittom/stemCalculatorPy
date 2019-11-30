# Required imports
from point import Point
from vector import Vector
from stem import Stem
import math

# --------------------------------------------------------------
# Utility class
# --------------------------------------------------------------

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

        # Create the point at the top of the frame
        pFrame = Point(reach, stack)

        # Create the Point on the top of the bearing
        xBearing = pFrame.x - math.sin(directionAngle) * bearingHeight
        yBearing = pFrame.y + math.cos(directionAngle) * bearingHeight
        pBearing = Point(xBearing, yBearing)

        # Create the Point at the top of the spacer
        xSpacer = pBearing.x - math.sin(directionAngle) * spacerHeight
        ySpacer = pBearing.y + math.cos(directionAngle) * spacerHeight
        pSpacer = Point(xSpacer, ySpacer)

        # Create the Point at the middle height of the stem
        xMiddleStem = pSpacer.x - math.sin(directionAngle) * stemHeight / 2
        yMiddleStem = pSpacer.y + math.cos(directionAngle) * stemHeight / 2
        pMiddleStem = Point(xMiddleStem, yMiddleStem)

        # Create the Point of the handlebar
        pHandlebar = Point(xHandlebar, yHandlebar) 

        # Create the Vector between the Point of the middle height of the stem and the point of the handlebar
        vStem = Vector(pMiddleStem, pHandlebar)

        # Create the Vector between the Point of the middle height of the stem and the Point of the top of the frame 
        vDirection = Vector(pMiddleStem, pFrame)

        # Compute the angle between the two Vectors
        alpha = Utility.computeAngleBtwVectors(vStem, vDirection)
        alpha = alpha * 180 / math.pi
        print("the angle after calculation is : " + str(alpha))

        # Compute the length of the stem
        lengthStem = vStem.computeModule()
        print("the length of the stem after calculation is : " + str(lengthStem))
  




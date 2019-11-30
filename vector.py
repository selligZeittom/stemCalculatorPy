import math

# --------------------------------------------------------------
# Vector class
# --------------------------------------------------------------

class Vector:
    vX = 0.0
    vY = 0.0

    # Constructor with points
    def __init__(self, p1, p2):
        self.vX = p2.x - p1.x
        self.vY = p2.y - p1.y

    # Compute the module of the vector
    def computeModule(self):
        return math.sqrt(self.vX * self.vX + self.vY * self.vY)

    # Strech the vector
    def strechVector(self, coeff):
        self.vX = self.vX * coeff
        self.vY = self.vY * coeff

    # Print the Vector
    def toString(self):
        print("The coordinates of the Vector : [" + str(self.vX) + " ; " + str(self.vY) + "]")
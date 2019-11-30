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

    # Print the Vector
    def toString(self):
        print("The coordinates of the Vector : [" + str(self.vX) + " ; " + str(self.vY) + "]")
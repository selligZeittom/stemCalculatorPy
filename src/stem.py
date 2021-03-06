# --------------------------------------------------------------
# Stem class
# --------------------------------------------------------------

class Stem:
    length = 100.0
    angle = 0.0

    # Constructor
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    # Print the stem
    def toString(self):
        print("The stem is " + str(self.length) + "mm and has an angle of " + str(self.angle) + " degrees")
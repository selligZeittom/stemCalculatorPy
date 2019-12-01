# --------------------------------------------------------------
# Point class
# --------------------------------------------------------------

class Point:
    x = 0.0
    y = 0.0
    name = ""

    # Constructor
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    # Print the Point
    def toString(self):
        print("The coordinates of the Point (" + self.name + ") : \t" + str(self.x) + " ; " + str(self.y))
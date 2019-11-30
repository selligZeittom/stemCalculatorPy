# --------------------------------------------------------------
# Point class
# --------------------------------------------------------------

class Point:
    x = 0.0
    y = 0.0

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Print the Point
    def toString(self):
        print("The coordinates of the Point : " + str(self.x) + " ; " + str(self.y))
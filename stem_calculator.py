# Import Utility, Point and Vector
from utility import Utility, Point, Vector
from stem import Stem

if __name__ == "__main__":
    p1 = Point(10.1, 10)
    p1.toString()
    p2 = Point(-30, -40.9)
    p2.toString()

    v1 = Vector(p1, p2)
    v1.toString()
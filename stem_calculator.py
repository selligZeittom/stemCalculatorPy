# Import Utility, Point and Vector
from utility import Utility
from stem import Stem

if __name__ == "__main__":
    print("*************************************************************************************")
    print("*********************************  Stem Calculator  *********************************")
    print("*************************************************************************************")
    print("")

    # Ask for the data
    print("Please enter : ")
    print("")
    stack = float(input("\tthe stack of the frame : "))
    reach = float(input("\tthe reach of the frame : "))
    directionAngle = float(input("\tthe angle of the direction of the frame : "))
    xHandlebar = float(input("\tthe requested handlebar X : "))
    yHandlebar = float(input("\tthe requested handlebar Y : "))
    bearingHeight = float(input("\tthe height of the bearing : "))
    spacerHeight = float(input("\tthe height of the spacers : "))
    stemHeight = float(input("\tthe height of the stem : "))

    # Compute the Stem
    Utility.computeStem(xHandlebar, yHandlebar, reach, stack, directionAngle, bearingHeight, spacerHeight, stemHeight)

    
    
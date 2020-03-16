# Import Utility, Point and Vector
from src.utility import Utility
from src.stem import Stem

# Misc import
import json
import sys

# PyQt import
from PyQt5.QtWidgets import QApplication, QLabel

# Get the data manually
def getConfigFromCmdLineForStem():
    # Ask for the data
    print("Please enter : ")
    print("")
    _stack = float(input("\tthe stack of the frame : "))
    _reach = float(input("\tthe reach of the frame : "))
    _directionAngle = float(input("\tthe angle of the direction of the frame : "))
    _xHandlebar = float(input("\tthe requested handlebar X : "))
    _yHandlebar = float(input("\tthe requested handlebar Y : "))
    _bearingHeight = float(input("\tthe height of the bearing : "))
    _spacerHeight = float(input("\tthe height of the spacers : "))
    _stemHeight = float(input("\tthe height of the stem : "))
    data = {"stack" : _stack, "reach" : _reach, "directionAngle" : _directionAngle, "xHandlebar" : _xHandlebar, "yHandlebar" : _yHandlebar, "bearingHeight" : _bearingHeight, "stemHeight" : _stemHeight, "spacerHeight" : _spacerHeight}
    return data

# Read the Json file
def getConfigFromJsonForStem(filename):
    with open(filename) as json_file:
        config = json.load(json_file)
        _stack = config["stack"]
        _reach = config["reach"]
        _directionAngle = config["directionAngle"]
        _bearingHeight = config["bearingHeight"]
        _spacerHeight = config["spacerHeight"]
        _stemHeight = float(input("\tthe height of the stem : "))
        _xHandlebar = float(input("\tthe requested handlebar X : "))
        _yHandlebar = float(input("\tthe requested handlebar Y : "))
        data = {"stack" : _stack, "reach" : _reach, "directionAngle" : _directionAngle, "xHandlebar" : _xHandlebar, "yHandlebar" : _yHandlebar, "bearingHeight" : _bearingHeight, "stemHeight" : _stemHeight, "spacerHeight" : _spacerHeight}
        return data

# Read the Json file
def getConfigFromJsonForHandlebar(filename):
    with open(filename) as json_file:
        config = json.load(json_file)
        _stack = config["stack"]
        _reach = config["reach"]
        _directionAngle = config["directionAngle"]
        _bearingHeight = config["bearingHeight"]
        _spacerHeight = config["spacerHeight"]
        _stemHeight = float(input("\tthe height of the stem : "))
        _stemLength = float(input("\tthe requested stem length : "))
        _stemAngle = float(input("\tthe requested stem angle : "))
        data = {"stack" : _stack, "reach" : _reach, "directionAngle" : _directionAngle, "stemLength" : _stemLength, "stemAngle" : _stemAngle, "bearingHeight" : _bearingHeight, "stemHeight" : _stemHeight, "spacerHeight" : _spacerHeight}
        return data

if __name__ == "__main__":
    print("*************************************************************************************")
    print("********************************  <Stem Calculator>  ********************************")
    print("*************************************************************************************")
    print("")


    # Compute the Stem
    if str(sys.argv[1]) == '-c' : 
        # Json or command line input
        if len(sys.argv) == 3:
            data = getConfigFromJsonForStem(sys.argv[1])
        elif len(sys.argv) == 2:
            data = getConfigFromCmdLineForStem()
        else:
            sys.exit()
        stem = Utility.computeStem(data["xHandlebar"], data["yHandlebar"], data["reach"], data["stack"], data["directionAngle"], data["bearingHeight"], data["spacerHeight"], data["stemHeight"])
        print("The stem dimensions are :")
        print("\tangle : \t" + str(stem.angle) + " [degrees]")
        print("\tlength : \t" + str(stem.length) + " [mm]")
        print("")

    # Compute the handlebar
    elif str(sys.argv[1]) == '-d' : 
        # Json or command line input
        if len(sys.argv) == 3:
            data = getConfigFromJsonForHandlebar(sys.argv[1])
        else:
            sys.exit()
        handlebar = Utility.computeHandlebar(data["stemLength"], data["stemAngle"], data["reach"], data["stack"], data["directionAngle"], data["bearingHeight"], data["spacerHeight"], data["stemHeight"])
    print("*************************************************************************************")
    print("*******************************  </Stem Calculator >  *******************************")
    print("*************************************************************************************")
    
# Import Utility, Point and Vector
from utility import Utility
from stem import Stem

# Misc import
import json
import sys

# Get the data manually
def getDataCmdLine():
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
def getDataJson(filename):
    print("Reading the configuration file at : " + filename)
    with open(filename) as json_file:
        config = json.load(json_file)
        _stack = config["stack"]
        _reach = config["reach"]
        _directionAngle = config["directionAngle"]
        _xHandlebar = config["xHandlebar"]
        _yHandlebar = config["yHandlebar"]
        _bearingHeight = config["bearingHeight"]
        _spacerHeight = config["spacerHeight"]
        _stemHeight = config["stemHeight"]
        data = {"stack" : _stack, "reach" : _reach, "directionAngle" : _directionAngle, "xHandlebar" : _xHandlebar, "yHandlebar" : _yHandlebar, "bearingHeight" : _bearingHeight, "stemHeight" : _stemHeight, "spacerHeight" : _spacerHeight}
        return data



if __name__ == "__main__":
    print("*************************************************************************************")
    print("*********************************  Stem Calculator  *********************************")
    print("*************************************************************************************")
    print("")

    # Use the script with Json or command line
    if len(sys.argv) == 2:
        data = getDataJson(sys.argv[1])
    elif len(sys.argv) == 1:
        data = getDataCmdLine()
    else:
        sys.exit()

    # Compute the Stem
    Utility.computeStem(data["xHandlebar"], data["yHandlebar"], data["reach"], data["stack"], data["directionAngle"], data["bearingHeight"], data["spacerHeight"], data["stemHeight"])

    
    
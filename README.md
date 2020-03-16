# Stem Calculator
This tool can be used to compute the characteristics of a stem given a bike geometry and a handlebar position to reach

## How to use it 

1. Clone the repo
2. Run the script to compute the stem length and angle : use the `-c` option
* Either with a configuration file :
```python.exe stem_calculator.py -c config\scott_spark_L.json```
* Or without configuration file and give the inputs one by one : 
```python.exe stem_calculator.py -c```
3. Run the script to compute the coordinates of the handlebar : use the `-d` option
* Either with a configuration file :
```python.exe stem_calculator.py -d config\scott_spark_L.json```
* Or without configuration file and give the inputs one by one : 
```python.exe stem_calculator.py -d```
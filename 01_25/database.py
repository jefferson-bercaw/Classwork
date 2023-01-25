print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))

# import blood_calculator as bc
# from blood_calculator import * # imports everything from blood_calculator and everything has a generic name, bad practice

from blood_calculator import HDL_analysis # no import name needed when calling HDL_analysis

HDL = 55;

HDL_analysis = HDL_analysis(HDL)

print("The HDL analysis is {}".format(HDL_analysis))


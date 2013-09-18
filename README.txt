CalCalc
--------

CalCalc contains a set of functions to evaluate any string or numerical operation passed to it, either through Python or through the Wolfram|Alpha API. It can be used from the command line or by importing within Python.

Installing
--------

To install CalCalc, you can first download the source from https://github.com/alinal/AY250_HW/archive/master.zip or clone the source from git@github.com:alinal/AY250_HW.git. 

You should then set your working directory to the source directory and run the following:

python setup.py install 

This will make the CalCalc module importable into python.

Usage
--------
CalCalc.py [options]

	Options:
		-h Show this help message and exit
		-s Will store and evaluate the argument following this option 
		-f Return value will be a float 

Import into python:
	
	from CalCalc import calculate

Sample usage from within python:
	
	calculate('mass of the earth in lbs',  return_float=True)

Command line usage:

	python CalCalc.py -s '34*28' -f 

	python CalCalc.py 'Mass of the earth in lbs'

	python CalCalc.py 50/10 -f




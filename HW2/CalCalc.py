import argparse
from optparse import OptionParser
import urllib2 

def calculate(dataStr, return_float=True):
	try:	
		if isinstance(dataStr, str):
			print eval(dataStr, {'__builtins__':{}})
		else:
			print eval(str(dataStr), {'__builtins__':{}})
	except:
		print 'Asking Wolfram|Alpha'

if __name__ == "__main__":

	# Initiatie parser 
	parser = OptionParser()
	parser.add_option('-s', action='store', dest='evalString', default=[],
	                    help='Store a string for evaluation')

	(results, args) = parser.parse_args()
	
	if not results.evalString:
		for ii, item in enumerate(args):
			calculate(item)
	else:	
		calculate(results.evalString)


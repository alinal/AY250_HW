import argparse
from optparse import OptionParser
import urllib2 
import re
from xml.dom.minidom import parseString
import nose.tools as nt


def calculate(dataStr, return_float=False):
	try:	
		if isinstance(dataStr, str):
			if return_float:
				return float(eval(dataStr, {'__builtins__':{}}))
			else:
				return eval(dataStr, {'__builtins__':{}})
		else:
			if return_float:
				return float(eval(str(dataStr), {'__builtins__':{}}))
			else:
				return eval(str(dataStr), {'__builtins__':{}})
	except:
		print 'Asking Wolfram|Alpha'
		if isinstance(dataStr, str):
			dataStr=dataStr.replace(" ", '%20')
			urlName='http://api.wolframalpha.com/v2/query?input=%s&appid=UAGAWR-3X6Y8W777Q' % dataStr
			f=urllib2.urlopen(urlName)
			html=f.read()
			# Find indices of interest
			start=html.find('Result')
			begin=html.find('<plaintext>', start)
			endLine=html.find('</plaintext>', begin)
			answer=html[begin+len('<plaintext>'):endLine].strip()
			# Replace unicode characters
			answer=answer.replace('\xc3\x97', '*')
			answer=answer.replace('^', '**')

			if return_float:
				space=re.search(' ',answer)
				try:
					answerNew=answer[:space.start()]
					answerNew=eval(answerNew)
					return float(answerNew)
				except:
					answerNew=eval(answer)
					return float(answerNew)
			else:
				return answer

		else:
			print "Please enter a string."


# Test functions
def test_1():
    nt.assert_less(abs(4. - calculate('3**2')),6, msg='Calculate fail.')

def test_2():
    nt.assert_equals(5.9721986e+24, calculate('mass of the earth in kg',  return_float=True), msg='Calculate fail.')

def test_3():
    nt.assert_equals('5.9721986*10**24 kg  (kilograms)', calculate('mass of the earth in kg',  return_float=False), msg='Calculate fail. May be flag issue.')

def test_4():
    nt.assert_greater(20, calculate('average cat weight in lbs',  return_float=True), msg='Calculate fail.')

def test_5():
    nt.assert_greater(20, calculate('average cat weight in lbs',  return_float=True), msg='Calculate fail.')


if __name__ == "__main__":
""" Function CalCalc 
	Flags:
		-s: Enter a string for evaluation
		-f: Return value will be a float 
"""
	# Initiate parser 
	parser = OptionParser()
	parser.add_option('-s', action='store', dest='evalString', default=[],
	                    help='Store a string for evaluation')
	parser.add_option('-f', action='store_true', dest='return_float', default=False, 
						help='Flag for returning a floating point number')

	(results, args) = parser.parse_args()
	
	if not results.evalString:
		for ii, item in enumerate(args):
			result=calculate(item, results.return_float)
			print result
	else:	
		result=calculate(results.evalString, results.return_float)
		print result


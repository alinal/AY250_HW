import argparse
from optparse import OptionParser
import urllib2 
import re
from xml.dom.minidom import parseString
import numexpr as ne
import xml.etree.ElementTree as ET
import nose.tools as nt


def calculate(dataStr, return_float=True):
	try:	
		if isinstance(dataStr, str):
			if return_float:
				return float(ne.evaluate(dataStr, {'__builtins__':{}}))
			else:
				return eval(dataStr, {'__builtins__':{}})
		else:
			if return_float:
				return float(ne.evaluate(str(dataStr), {'__builtins__':{}}))
			else:
				return eval(str(dataStr), {'__builtins__':{}})
	except:
		print 'Asking Wolfram|Alpha'
		if isinstance(dataStr, str):
			dataStr=dataStr.replace(" ", '%20')
			urlName='http://api.wolframalpha.com/v2/query?input=%s&appid=UAGAWR-3X6Y8W777Q' % dataStr
			f=urllib2.urlopen(urlName)
			html=f.read()
			#findResult(html)
			start=html.find('Result')
			begin=html.find('<plaintext>', start)
			endLine=html.find('</plaintext>', begin)
			answer=html[begin+len('<plaintext>'):endLine].strip()
			answer=answer.replace('\xc3\x97', '*')
			answer=answer.replace('^', '**')

			if return_float:
				space=re.search(' ',answer)
				try:
					answerNew=answer[:space.start()]
					answerNew=ne.evaluate(answerNew)
					return float(answerNew)
				except:
					answerNew=ne.evaluate(answer)
					return float(answerNew)
			else:
				return answer

		else:
			print "Please enter a string."

# Parser stuff
def findResult(html):
	root=ET.fromstring(html)
	for pt in root.findall('.//plaintext'):
		if pt.text:
			print(pt.text)

def test_1():
assert abs(4. - calculate(‘2**2’)) < .001

if __name__ == "__main__":

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


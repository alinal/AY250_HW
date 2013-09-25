import numpy as np
import matplotlib.pyplot as plt
import sys
# Data descriptor to make a proper array.
import os
import csv
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Rectangle


class StationPicker(object):
	def __init__(self, axis=None):
    	self.rect = []
    	self.x1, self.y1=[]
        self.x2, self.y2=[]
        self.cid = line.figure.canvas.mpl_connect('button_press_event', onclick)
        self.cid = line.figure.canvas.mpl_connect('button_release_event', onrelease)

    def onclick(self, event):
        print 'click', event
        if event.inaxes!=self.axis: return
        self.x1, self.y1 = event.xdata, event.ydata
        # 0,0 = bottom

    def onrelease(self, event):
    	print 'release', event:
    	self.x2, self.y2=event.xdata, event.ydata
    	rectWidth=self.x2-self.x1
    	rectHeight=self.y2-self.y1
    	newRect=Rectangle((x1, y1), rectWidth, rectHeight)

        self.line.figure.canvas.draw()

     def onpress(self, event):
        'define some key press events'
        if self.lastind is None: return

        if event.key in ('q','Q'): sys.exit()

        if event.key not in ('n', 'p'): return
        if event.key=='n': inc = 1
        else:  inc = -1

        self.lastind += inc
        self.lastind = clip(self.lastind, 0, len(self.xs)-1)
        self.update()

    def onclick():
    	x1, y1=event.x, event.y
    	x2, y2=
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    

def replace_all(text, dic):
	textList=[]
   	for i, name  in enumerate(text):
	    textList.append(dic[name])
	return textList
 

if __name__ == "__main__":

	# Data file
	data_fname = 'hw_3_data/flowers.csv'

	# Open file using loadtxt
	dt=[('sepal length', np.float32), ('sepal width', np.float32), ('petal length', np.float32), ('petal width', np.float32), 
	('species', (str, 8))]
	tab = np.loadtxt(data_fname, dt, skiprows=1, delimiter=',')

	# Make color dictionary
	flowerColor={'setosa': 'r', 'versicol': 'b', 'virginic': 'g'}

	# Plot the data
	f, ax=plt.subplots(4,4)
	catNames=['sepal length', 'sepal width', 'petal length', 'petal width']
	
	textList=replace_all(tab['species'], flowerColor)
	for i in range(16):	
		ax=plt.subplot(4,4,i+1)
		row, col=divmod(i, 4)
		ax.scatter(tab[catNames[row]], tab[catNames[col]], c=textList)

	f.patch.set_facecolor('white')
	plt.show()

	1/0
	# Add rectangle
	rects=ax.bar(range(10), 20*np.random.rand(10))

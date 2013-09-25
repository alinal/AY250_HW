import numpy as np
import matplotlib.pyplot as plt
import sys
# Data descriptor to make a proper array.
import os
import csv
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Rectangle


class DataPicker(object):
    def __init__(self, figure, axis=None, tab=None, catNames=None, flowerColor=None):
        self.x1, self.y1=[],[]
        self.x2, self.y2=[],[]
        self.reset=[]
        self.patch=[]
        self.tab=tab
        self.catNames=catNames
        self.flowerColor=flowerColor
        self.textListSt=np.copy(textList)
        self.cidclick = figure.canvas.mpl_connect('button_press_event', self)
        self.cidrelease = figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.keypress=figure.canvas.mpl_connect('key_press_event', self.onpress)
        if axis is None:
            axis = figure.axes[0]
        self.axis=axis
        self.figure=figure
        self.rect = Rectangle((0,0), 1, 1)

    def __call__(self, event):
        print 'click'
        self.x1, self.y1 = event.xdata, event.ydata
        self.axis=event.inaxes
        # make sure the rectangle drawn in that subplot
        self.rect.set_axes(event.inaxes)
        print self.x1, self.y1
        # 0,0 = bottom


    def on_release(self, event):
        print 'second coords'
        if event.inaxes != self.axis:
            return
        if self.patch !=[] and self.reset !=[]: self.patch.remove() 
        newtab=[]
        self.x2, self.y2=event.xdata, event.ydata
        rectWidth=self.x2-self.x1
        rectHeight=self.y2-self.y1
        self.rect=Rectangle((self.x1, self.y1), rectWidth, rectHeight, color='.75', alpha=.5)
        self.patch=self.axis.add_patch(self.rect)
        self.reset=1
        # Find indices in rectangle, set those indices to NullFlower in data
        datCopy=np.copy(self.tab)
        newtab=findPoints(self.axis, self.x1, self.y1, self.x2, self.y2, datCopy, self.catNames)
        drawScatter(self.axis, newtab, self.catNames, self.flowerColor)
        self.axis.figure.canvas.draw()

    def onpress(self, event):
        # Quit if the user hits 'q'
        if event.key in ('q','Q'): plt.close(); 
        if event.key in ('d','D'):
            drawScatter(self.axis, self.tab, self.catNames, self.flowerColor)
            if self.patch !=[]: self.patch.remove()
            self.reset=[]



if __name__ == "__main__":

    def replace_all(text, dic):
        textList=[]
        for i, name  in enumerate(text):
            textList.append(dic[name])
        return textList

    def drawScatter(ax, tab, catNames, flowerColor, plotText=False):
        # Make color dictionary
        allPlots=[]
        textList=replace_all(tab['species'], flowerColor)
        textPlot=[1, 6, 11, 16]  
        for i in range(len(catNames)*len(catNames)): 
            ax=plt.subplot(4,4,i+1)
            row, col=divmod(i, 4)
            if i+1 in textPlot and plotText:
                ax.text(.4, .9, catNames[col], ha='center', va='center', transform=ax.transAxes)
            allPlots.append(ax.scatter(tab[catNames[row]], tab[catNames[col]], c=textList))
        return ax, allPlots

    def findPoints(axis, x1, y1, x2, y2, tab2, catNames):
        xdata=tab2[catNames[axis.rowNum]]
        ydata=tab2[catNames[axis.colNum]]
        # Get indices
        if x1>x2:
            allXind=np.where((xdata>= x2) & (xdata <= (x1)))
        else:
            allXind=np.where((xdata>= x1) & (xdata <= (x2)))
        if y1>y2:
            allYind=np.where((ydata>= y2) & (ydata <= (y1)))
        else:
            allYind=np.where((ydata>= y1) & (ydata <= (y2)))

        allIndInside=np.intersect1d(allXind[0], allYind[0])
        outsideInd=np.setdiff1d(range(len(ydata)), allIndInside)
        tab2['species'][np.array(outsideInd)]='NullFlow'
        return tab2

    # Data file
    data_fname = 'hw_3_data/flowers.csv'

    # Open file using loadtxt
    dt=[('sepal length', np.float32), ('sepal width', np.float32), ('petal length', np.float32), ('petal width', np.float32), 
    ('species', (str, 8))]
    tab = np.loadtxt(data_fname, dt, skiprows=1, delimiter=',')
   
    # Plot the data
    fig1, ax=plt.subplots(4,4)
    fig1.patch.set_facecolor('white')

    # Draw scatter plot
    flowerColor={'setosa': 'r', 'versicol': 'b', 'virginic': 'g', 'NullFlow': '0.75'}
    textList=replace_all(tab['species'], flowerColor)  
    catNames=['sepal length', 'sepal width', 'petal length', 'petal width']
    plotText=True
    ax, allPlots=drawScatter(ax, tab, catNames, flowerColor, plotText)

    # Add rectangle
    DataPicker(fig1, ax, tab, catNames, flowerColor)
    plt.show()

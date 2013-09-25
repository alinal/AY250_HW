import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import csv
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Rectangle


class DataPicker(object):
    """Allows for brushing of flowers.csv data set """
    def __init__(self, figure, axis=None, tab=None, catNames=None, flowerColor=None):
        self.x1, self.y1=[],[]
        self.x2, self.y2=[],[]
        self.reset=[]
        self.patch=[]
        self.tab=tab
        self.catNames=catNames
        self.flowerColor=flowerColor
        self.textListSt=np.copy(textList)
        # Connect figure to events
        self.cidclick = figure.canvas.mpl_connect('button_press_event', self)
        self.cidrelease = figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.keypress=figure.canvas.mpl_connect('key_press_event', self.onpress)
        if axis is None:
            axis = figure.axes[0]
        self.axis=axis
        self.figure=figure
        self.rect = Rectangle((0,0), 1, 1)

    def __call__(self, event):
        # Get first set of x and y values 
        self.x1, self.y1 = event.xdata, event.ydata
        # Get axis location of the mouse
        self.axis=event.inaxes
        # make sure the rectangle drawn in that subplot
        self.rect.set_axes(event.inaxes)
        # 0,0 = bottom

    def on_release(self, event):
        if event.inaxes != self.axis:
            return
        # If rectangle is still present, remove it
        if self.patch !=[] and self.reset !=[]: self.patch.remove() 
        newtab=[]
        # Get second set of x and y values
        self.x2, self.y2=event.xdata, event.ydata
        # Calculate rectangle width and height
        rectWidth=self.x2-self.x1
        rectHeight=self.y2-self.y1
        # Make a new rectangle
        self.rect=Rectangle((self.x1, self.y1), rectWidth, rectHeight, color='.75', alpha=.5)
        # Add a new rectangle to the axis
        self.patch=self.axis.add_patch(self.rect)
        self.reset=1
        # Find indices in rectangle, set those indices to NullFlow in data
        datCopy=np.copy(self.tab)
        newtab=findPoints(self.axis, self.x1, self.y1, self.x2, self.y2, datCopy, self.catNames)
        # Draw a new scatter plot with indices outside of the rectangle grayed out
        drawScatter(self.axis, newtab, self.catNames, self.flowerColor)
        self.axis.figure.canvas.draw()

    def onpress(self, event):
        # Quit if the user hits 'q'
        if event.key in ('q','Q'): plt.close(); 
        # Remove the rectangle if the user hits 'd'
        if event.key in ('d','D'):
            drawScatter(self.axis, self.tab, self.catNames, self.flowerColor)
            if self.patch !=[]: self.patch.remove()
            self.reset=[]



if __name__ == "__main__":
    """ 
        Running hw3_c.py will allow brushing for the flowers.csv data set. 
        This code has the following features:
        * Plots the iris dataset in a 4x4 grid
        * Allows you to interactively draw rectangles on one of the subplots
        * Identifyies the datapoints located within the drawn rectangle
        * Changes the color/opacities of the corresponding points in the other subplots 

        Usage notes:
        * After drawing a rectangle, hitting 'd' from a keyboard will remove the brushed region, 
          regardless of where the mouse is. 
        * Only one brushing rectangle can be viewed at a time. 

    """

    def replace_all(text, dic):
        """Replace all the strings with new string values found in dic and returns the list """
        textList=[]
        for i, name  in enumerate(text):
            textList.append(dic[name])
        return textList

    def drawScatter(ax, tab, catNames, flowerColor, plotText=False):
        """Draws all the scatterplots and returns the axis """
        textList=replace_all(tab['species'], flowerColor)
        textPlot=[1, 6, 11, 16]  
        for i in range(len(catNames)*len(catNames)): 
            ax=plt.subplot(4,4,i+1)
            row, col=divmod(i, 4)
            if i+1 in textPlot and plotText:
                ax.text(.4, .9, catNames[col], ha='center', va='center', transform=ax.transAxes)
            ax.scatter(tab[catNames[row]], tab[catNames[col]], c=textList)
        return ax

    def findPoints(axis, x1, y1, x2, y2, tab2, catNames):
        """
            Find all the data points in the rectangle and return all the values
            outside of those points with flower name set to 'NullFlow'. 

        """
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

    # Make color dictionary for each flower type
    flowerColor={'setosa': 'r', 'versicol': 'b', 'virginic': 'g', 'NullFlow': '0.75'}
    # Replace each flower name with a color
    textList=replace_all(tab['species'], flowerColor)  
    catNames=['sepal length', 'sepal width', 'petal length', 'petal width']
    plotText=True
    # Draw scatter plot
    ax=drawScatter(ax, tab, catNames, flowerColor, plotText)

    # Add rectangle and brushing capabilities 
    DataPicker(fig1, ax, tab, catNames, flowerColor)
    plt.show()

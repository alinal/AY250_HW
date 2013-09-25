import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


""" 
	This script loads ny_temps.txt, yahoo_data.txt, and google_data.txt and
	produces a figure plotting all three datasets. 
	
	An example of the output of this file is saved in stocks_copy.png  

"""

# Set the minor xtick locations
minorLocatorY = MultipleLocator(20)
minorLocatorX=MultipleLocator(200)
minorLocatorY2=MultipleLocator(10)

# Get data location
dataDir='hw_3_data/'
# Datafile names
allData=['yahoo_data.txt', 'google_data.txt', 'ny_temps.txt' ]
# All data labels
allLabels=['Yahoo! Stock Value', 'Google Stock Value', 'NY Mon. High Temp' ]
degreeChar = u'\N{DEGREE SIGN}'
# All data colors
dataColors=['m', 'b', 'r--']
allLines=[2, 1.5, 2]

# Initiate data plots
f, ax= plt.subplots()
ax2=ax.twinx()

# Plot the data in each file
for num, dataFile in enumerate(allData):
	x, y=np.loadtxt(dataDir+dataFile, unpack=True, skiprows=1)
	if num==len(allData)-1:
		ax2.plot(x, y, dataColors[num], linewidth= allLines[num], label=allLabels[num])
	else:
		ax.plot(x, y, dataColors[num], linewidth= allLines[num], label=allLabels[num])


# Set all axis limits
ax2.set_ylim(-150, 100)
ax.set_xlim(48800, 55800)
ax.set_ylim(-20, 780)
ax.xaxis.set_ticks_position('bottom')

# For the minor ticks, use no labels; Add minor ticks
ax.yaxis.set_minor_locator(minorLocatorY)
ax.xaxis.set_minor_locator(minorLocatorX)
ax2.yaxis.set_minor_locator(minorLocatorY2)

# Add a legend
lines, labels=ax.get_legend_handles_labels()
lines2, labels2=ax2.get_legend_handles_labels()
ax2.legend(lines+lines2, labels+labels2, loc='center left', frameon=False, fontsize='medium');

# Add a plot title and axes labels
plt.title('New York Temperature, Google, and Yahoo!', fontsize='xx-large', fontweight='bold')
ax.set_xlabel('Date (MJD)', fontsize=14); ax.set_ylabel('Value (Dollars)', fontsize=14)
ax2.set_ylabel('Temperature ('+degreeChar+'F)', fontsize=14)

f.patch.set_facecolor('white')
plt.show()

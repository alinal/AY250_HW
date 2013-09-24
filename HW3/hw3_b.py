import numpy as np
import matplotlib.pyplot as plt

dataDir='hw_3_data/'
allData=['yahoo_data.txt', 'google_data.txt', 'ny_temps.txt' ]
allLabels=['Yahoo! Stock Value', 'Google Stock Value', 'NY Mon. High Temp' ]
degreeChar = u'\N{DEGREE SIGN}'
dataColors=['m', 'b', 'r--']
allLines=[2, 1.5, 2]
f, ax= plt.subplots()
ax2=ax.twinx()

for num, dataFile in enumerate(allData):
	x, y=np.loadtxt(dataDir+dataFile, unpack=True, skiprows=1)
	if num==len(allData)-1:
		ax2.plot(x, y, dataColors[num], linewidth= allLines[num], label=allLabels[num])
	else:
		ax.plot(x, y, dataColors[num], linewidth= allLines[num], label=allLabels[num])


ax2.set_ylabel('Temperature ('+degreeChar+'F)', fontsize=14)
ax2.set_ylim(-150, 100)
ax.set_xlim(48800, 55800)
ax.set_ylim(-20, 780)
#ax.tick_params(direction='in', which='both')

lines, labels=ax.get_legend_handles_labels()
lines2, labels2=ax2.get_legend_handles_labels()
ax2.legend(lines+lines2, labels+labels2, loc='center left', frameon=False, fontsize='medium');

plt.title('New York Temperature, Google, and Yahoo!', fontsize='xx-large', fontweight='bold')
ax.set_xlabel('Date (MJD)', fontsize=14); ax.set_ylabel('Value (Dollars)', fontsize=14)
f.patch.set_facecolor('white')
plt.show()

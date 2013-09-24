import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

dataDir='hw_3_data/'
dataName=['subData.mat' ,'subData_modelFit.mat']

plotData=loadmat(dataDir+dataName[0])
modelFits=loadmat(dataDir+dataName[1])
allData=plotData['plot_data2']

f, ax= plt.subplots()

# Plot all data
ax.scatter(allData[:,0], allData[:,1], s=80, c='k', marker='o')

# Plot Gaussian derivative fit
x1=modelFits['x1'].T; y1=modelFits['y1'].T
ax.plot(x1, y1, 'r', linewidth=3, label='Model Fit')

# Plot running mean
x2=modelFits['allx_vals'].T[:-1]; y2=modelFits['mean_data'].T[:-1]
ax.plot(x2, y2, linestyle= 'dashed', linewidth=3, color='0.75', label='Running Avg.')
ax.legend(loc=1, frameon=False, fontsize=18)

# Set graph parameters
ax.set_xlim(-59.9, 59.9)
ax.set_ylim(-39.9, 39.9)
plt.setp(ax.get_xticklabels(), fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=18)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')


ax.set_ylabel('Subject Error (deg)', fontsize=18); ax.set_xlabel('1st Orientation - 2nd Orientation', fontsize=18)
f.patch.set_facecolor('white')
plt.show()

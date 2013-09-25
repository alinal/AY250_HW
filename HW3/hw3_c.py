import numpy as np
import matplotlib.pyplot as plt
import sys
# Data descriptor to make a proper array.
import os
import csv


data_fname = 'hw_3_data/flowers.csv'

# Open file using loadtxt
dt=[('sepal length', np.float32), ('sepal width', np.float32), ('petal length', np.float32), ('petal width', np.float32), 
('species', (str, 8))]
tab = np.loadtxt(data_fname, dt, skiprows=1, delimiter=',')

# Open file using CSV
#flowData=csv.reader(open(data_fname, 'rb'), delimiter=',')
#flowData=np.array(list(flowData))

# Plot the data
f, ax=plt.subplots(4,4)
catNames=['sepal length', 'sepal width', 'petal length', 'petal width']

for i in range(16):	
	ax=plt.subplot(4,4,i+1)
	row, col=divmod(i, 4)
	ax.scatter(tab[catNames[row]], tab[catNames[col]])

f.patch.set_facecolor('white')
plt.show()

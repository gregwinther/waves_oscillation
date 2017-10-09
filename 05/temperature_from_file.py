'''
How to read data from file in Python
Sample file is temperatures in Blindern, Oslo

Sebastian G. Winther-Larsen (2017)
'''

import numpy as np
from matplotlib import pyplot as plt
import datetime

# Importing file with numpy
filename = "tempblindern10aar.txt"
data = np.loadtxt(filename)

# Extracting average temperatures
min_temp = data[:,3]
max_temp = data[:,4]

# Creating datetime array, startdate is found in datafile
start_date = datetime.datetime(2003, 1, 1)
date_list = [start_date + datetime.timedelta(days=x) for x in range(len(min_temp))]

# Plotting
plt.plot(date_list, min_temp, '-b')
plt.plot(date_list, max_temp, '-r')
plt.title("Min/Max Temperatures, Blindern")
plt.xlabel("Date")
plt.ylabel("Temp [C]")
plt.show()
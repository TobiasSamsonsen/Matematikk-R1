import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# define the function
def func(x, a, b, c):
    return  a * np.exp(-b * x) + c

# load the data from excel
import pandas as pd
lap_data = pd.read_excel('Analyse av reele data\Laptimedata.xlsx')

lap_data = lap_data.replace([np.inf, -np.inf], np.nan)
lap_data = lap_data.dropna()

# extract the lap number and percentage difference columns
lap_number = lap_data['Lap Number'].values
percent_diff = lap_data['Lap Time %'].values

# fit the function to the data
popt, pcov = curve_fit(func, lap_number, percent_diff)

# plot the function and the data
plt.plot(lap_number, percent_diff, 'bo', label='data')
plt.plot(lap_number, func(lap_number, *popt), 'r-', label='fit')
plt.xlabel('Lap Number')
plt.ylabel('% Difference')
plt.legend()
plt.show()

# print the function
print(f"Function: {popt[0]:.3f} * e^({-popt[1]:.3f} * x) + {popt[2]:.3f}")

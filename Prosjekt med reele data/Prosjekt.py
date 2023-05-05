import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# read the excel file into a pandas dataframe
data = pd.read_excel('Prosjekt med reele data\Laptimedata.xlsx')

# extract the x and y variables from the dataframe
x_data = data['Laps']
y_data = data['Percentage from best time']

# Define logistic function
def logistic_func(x, a, b, c, d):
    return a / (1 + np.exp(-c * (x - d))) + b

# Set initial parameter guesses
initial_guess = [max(y_data), 0, 1, 1]

# Fit logistic function to data
popt, pcov = curve_fit(logistic_func, x_data, y_data, p0=initial_guess, maxfev=100000)

# Create a larger number of points to plot the logistic function
x_fit = np.linspace(min(x_data), max(x_data), 1000)

# Plot data and logistic function
plt.plot(x_data, y_data, 'bo', label='Data')
plt.plot(x_fit, logistic_func(x_fit, *popt), 'r-', label='Logistic Function')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.title('Logistic Function')

plt.show()

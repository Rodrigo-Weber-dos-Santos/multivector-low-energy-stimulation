"""
===============
Curve fitting
===============

Demos a simple curve fitting
"""

############################################################
# First generate some data
import numpy as np

# Seed the random number generator for reproducibility
np.random.seed(0)

x_g2 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_g2 = [67, 55, 51, 47, 44, 41, 40, 39, 39]

x_g2e = [0.15, 0.2, 0.25, 0.3, 0.35]
y_g2e = [56, 51, 47, 43, 40]

x_g3 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_g3 = [0, 54, 39, 36, 34, 29, 27, 26, 26]

x_g3e = [0.15, 0.2, 0.25, 0.3, 0.35]
y_g3e = [53, 39, 36, 34, 30]

x_g4 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_g4 = [0, 49, 37, 32, 26, 24, 23, 23, 22]

x_g4e = [0.15, 0.2, 0.25, 0.3, 0.35]
y_g4e = [49, 37, 32, 26, 23]

x_data = x_g4e
y_data = y_g4e

# And plot it
import matplotlib.pyplot as plt
#plt.figure(figsize=(6, 4))
#plt.scatter(x_data, y_data)

############################################################
# Now fit a simple sine function to the data
from scipy import optimize

def test_func(x, N, a):
    return N * x ** (a)

params, params_covariance = optimize.curve_fit(test_func, x_data, y_data)

print(params)

############################################################
# And plot the resulting curve on the data

#plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, test_func(x_data, params[0], params[1]),
         label='Fitted function')

plt.legend(loc='best')

plt.show()

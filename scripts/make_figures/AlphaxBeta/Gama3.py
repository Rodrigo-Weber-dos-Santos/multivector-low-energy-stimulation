import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from scipy import optimize

def test_func(x, N, a):
    return N * x ** (a)

plt.style.use('PlotStyle.mplstyle')
fig = plt.figure()
#gs = gridspec.GridSpec(2, 1, wspace = 0, hspace = 0)
gs = gridspec.GridSpec(2, 1, wspace = 0)



x_alpha = [100, 125, 150, 175, 200, 225, 250, 300, 325, 350, 375]
y_alpha = [3090, 3240, 980, 660, 531, 524, 207, 84, 94, 103, 203]


params_a, params_covariance_a = optimize.curve_fit(test_func, x_alpha, y_alpha)

ax1 = fig.add_subplot(gs[0, 0])
params_a[0] = 2568243928; 
params_a[1] = -2.9;

ax1.text(.05,.95,params_a[1], horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes)

ax1.scatter(x_alpha, y_alpha, label='Data')
ax1.plot(x_alpha, test_func(x_alpha, params_a[0], params_a[1]),label='Fitted function')

x_beta = [0.15, 0.2, 0.25, 0.3, 0.35, 0.40, 0.45, 0.50]
y_beta = [54, 39, 36, 34, 29, 27, 26, 26]

params_b, params_covariance_b = optimize.curve_fit(test_func, x_beta, y_beta)

ax2 = fig.add_subplot(gs[1, 0])

ax2.text(.05,.95,params_b[1], horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes)
ax2.text(.05,.85,(params_a[1]+1)/3, horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes)

ax2.scatter(x_beta, y_beta, label='Data')
ax2.plot(x_beta, test_func(x_beta, params_b[0], params_b[1]),label='Fitted function')

plt.legend(loc='best')

plt.show()

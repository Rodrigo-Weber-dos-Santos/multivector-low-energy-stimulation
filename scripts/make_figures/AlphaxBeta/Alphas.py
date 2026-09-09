from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from scipy import optimize
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import LogFormatter
import matplotlib.ticker as ticker

def test_func(x, N, a):
    return N * np.power(x,a)

plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
#gs = gridspec.GridSpec(2, 1, wspace = 0, hspace = 0)
gs = gridspec.GridSpec(3, 2, wspace = 0.30, hspace = 0.35)
formatter = ScalarFormatter()
formatter.set_scientific(False)

x_alpha_50_1 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 475]
y_alpha_50_1 = [4373, 1182, 1147, 544, 210, 445, 179, 155, 262, 266, 141, 112, 625]
c = 113252939.907
a = -2.334
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(x_alpha_50_1, y_alpha_50_1, label='Data')
ax1.plot(x_alpha_50_1, test_func(x_alpha_50_1, c, a),label='Fitted function')
ax1.loglog()
ax1.xaxis.set_major_formatter(formatter)
ax1.xaxis.set_minor_formatter(formatter)
ax1.set_xlim(95, 500)
ax1.set_ylim(50, 10000)

x_alpha_50_2 = [100, 125, 150, 175, 200, 225, 250, 300, 325, 350, 375]
y_alpha_50_2 = [3090, 3240, 980, 660, 531, 524, 207, 84, 94, 103, 203]
c = 1595530753.375
a = -2.822
ax2 = fig.add_subplot(gs[1, 0])
ax2.scatter(x_alpha_50_2, y_alpha_50_2, label='Data')
ax2.plot(x_alpha_50_2, test_func(x_alpha_50_2, c, a),label='Fitted function')
ax2.loglog()
ax2.xaxis.set_major_formatter(formatter)
ax2.xaxis.set_minor_formatter(formatter)
ax2.set_xlim(95, 500)
ax2.set_ylim(50, 10000)

x_alpha_50_3 = [100, 125, 150, 175, 200, 225, 275, 300, 325]
y_alpha_50_3 = [597, 4448, 1788, 1074, 530, 523, 274, 126, 171]
c = 72941930266.347
a = -3.482
ax3 = fig.add_subplot(gs[2, 0])
ax3.scatter(x_alpha_50_3, y_alpha_50_3, label='Data')
ax3.plot(x_alpha_50_3, test_func(x_alpha_50_3, c, a),label='Fitted function')
ax3.loglog()
ax3.xaxis.set_major_formatter(formatter)
ax3.xaxis.set_minor_formatter(formatter)
ax3.set_xlim(95, 500)
ax3.set_ylim(50, 10000)

x_beta_50_1 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_1 = [67, 55, 51, 47, 44, 41, 40, 39, 39]
x_beta_50_1_B = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_1_B = [39, 37, 36, 35, 28, 20, 20, 19, 19]
c = 27.7355
a = -0.3763
c_b = 15.9195
a_b = -0.4377
ax4 = fig.add_subplot(gs[0, 1])
ax4.scatter(x_beta_50_1, y_beta_50_1,label='No Border')
ax4.plot(x_beta_50_1, test_func(x_beta_50_1, c, a))
ax4.scatter(x_beta_50_1_B, y_beta_50_1_B,label='Border')
ax4.plot(x_beta_50_1_B, test_func(x_beta_50_1_B, c_b, a_b))
ax4.loglog()
ax4.xaxis.set_major_formatter(formatter)
ax4.xaxis.set_minor_formatter(formatter)
ax4.yaxis.set_major_formatter(formatter)
ax4.yaxis.set_minor_formatter(formatter)
ax4.set_xlim(0.1, 0.5)
ax4.set_ylim(15, 110)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(25))
ax4.legend(loc="upper right")

x_beta_50_2 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_2 = [0, 54, 39, 36, 34, 29, 27, 26, 26]
x_beta_50_2_B = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_2_B = [34, 33, 32, 31, 26, 20, 18, 17, 17]
c = 15.1995
a = -0.6359
c_b = 10.3368
a_b = -0.6798
ax5 = fig.add_subplot(gs[1, 1])
ax5.scatter(x_beta_50_2, y_beta_50_2,label='No Border')
ax5.plot(x_beta_50_2, test_func(x_beta_50_2, c, a))
ax5.scatter(x_beta_50_2_B, y_beta_50_2_B, label='Border')
ax5.plot(x_beta_50_2_B, test_func(x_beta_50_2_B, c_b, a_b))
ax5.loglog()
ax5.xaxis.set_major_formatter(formatter)
ax5.xaxis.set_minor_formatter(formatter)
ax5.yaxis.set_major_formatter(formatter)
ax5.yaxis.set_minor_formatter(formatter)
ax5.set_xlim(0.1, 0.5)
ax5.set_ylim(15, 110)
ax5.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax5.yaxis.set_minor_locator(ticker.MultipleLocator(25))
ax5.legend()

x_beta_50_3 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_3 = [0, 49, 37, 32, 26, 24, 23, 23, 22]
x_beta_50_3_B = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_3_B = [28, 28, 27, 27, 26, 24, 20, 16, 16]
c = 9.6193
a = -0.8516
c_b = 8.7878
a_b = -0.8652
ax6 = fig.add_subplot(gs[2, 1])
ax6.scatter(x_beta_50_3, y_beta_50_3,label='No Border')
ax6.plot(x_beta_50_3, test_func(x_beta_50_3, c, a))
ax6.scatter(x_beta_50_3_B, y_beta_50_3_B,label='Border')
ax6.plot(x_beta_50_3_B, test_func(x_beta_50_3_B, c_b, a_b))
ax6.loglog()
ax6.xaxis.set_major_formatter(formatter)
ax6.xaxis.set_minor_formatter(formatter)
ax6.yaxis.set_major_formatter(formatter)
ax6.yaxis.set_minor_formatter(formatter)
ax6.set_xlim(0.1, 0.5)
ax6.set_ylim(15, 110)
ax6.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax6.yaxis.set_minor_locator(ticker.MultipleLocator(25))
ax6.legend()


plt.show()
#plt.savefig("Alphas.pdf", dpi=1200)

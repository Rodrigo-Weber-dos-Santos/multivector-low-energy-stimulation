import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from scipy import optimize
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import LogFormatter

def test_func(x, N, a):
    return N * np.power(x,a)

plt.style.use('PlotStyle.mplstyle')
fig = plt.figure()
#gs = gridspec.GridSpec(2, 1, wspace = 0, hspace = 0)
gs = gridspec.GridSpec(3, 2, wspace = 0.35, hspace = 0.30)
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

x_alpha_100_1 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 475]
y_alpha_100_1 = [4373, 1182, 1147, 544, 210, 445, 179, 155, 262, 266, 141, 112, 625]
c = 113252939.907
a = -2.334
ax4 = fig.add_subplot(gs[0, 1])
ax4.scatter(x_alpha_100_1, y_alpha_100_1, label='Data')
ax4.plot(x_alpha_100_1, test_func(x_alpha_100_1, c, a),label='Fitted function')
ax4.loglog()
ax4.xaxis.set_major_formatter(formatter)
ax4.xaxis.set_minor_formatter(formatter)
ax4.set_xlim(95, 500)
ax4.set_ylim(50, 10000)

x_alpha_100_2 = [100, 125, 150, 175, 200, 225, 250, 300, 325, 350, 375]
y_alpha_100_2 = [3090, 3240, 980, 660, 531, 524, 207, 84, 94, 103, 203]
c = 1595530753.375
a = -2.822
ax5 = fig.add_subplot(gs[1, 1])
ax5.scatter(x_alpha_100_2, y_alpha_100_2, label='Data')
ax5.plot(x_alpha_100_2, test_func(x_alpha_100_2, c, a),label='Fitted function')
ax5.loglog()
ax5.xaxis.set_major_formatter(formatter)
ax5.xaxis.set_minor_formatter(formatter)
ax5.set_xlim(95, 500)
ax5.set_ylim(50, 10000)

x_alpha_100_3 = [100, 125, 150, 175, 200, 225, 275, 300, 325]
y_alpha_100_3 = [597, 4448, 1788, 1074, 530, 523, 274, 126, 171]
c = 72941930266.347
a = -3.482
ax6 = fig.add_subplot(gs[2, 1])
ax6.scatter(x_alpha_100_3, y_alpha_100_3, label='Data')
ax6.plot(x_alpha_100_3, test_func(x_alpha_100_3, c, a),label='Fitted function')
ax6.loglog()
ax6.xaxis.set_major_formatter(formatter)
ax6.xaxis.set_minor_formatter(formatter)
ax6.set_xlim(95, 500)
ax6.set_ylim(50, 10000)


plt.show()
#plt.savefig("Alphas.pdf", dpi=1200)

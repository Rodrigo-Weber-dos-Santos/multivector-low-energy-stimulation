import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from scipy import optimize
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import LogFormatter
from mpl_toolkits.axes_grid.inset_locator import inset_axes
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
import matplotlib.ticker as ticker

def test_func(x, N, a):
    return N * np.power(x,a)

formatter = ScalarFormatter()
formatter.set_scientific(False)
plt.style.use('PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(3, 2, wspace = 0, hspace = 0, left=0.005, bottom=0.005, right=0.995, top=0.995)

ax1 = fig.add_subplot(gs[0, 0])
ax1.text(.05,.95,'a - tree 1', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes, weight='bold')
inset_axes1 = inset_axes(ax1, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax1.transAxes)
inset_axes1_2 = inset_axes(ax1, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax1.transAxes)
x_alpha_50_1 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 475]
y_alpha_50_1 = [4373, 1182, 1147, 544, 210, 445, 179, 155, 262, 266, 141, 112, 625]
c = 113252939.907
a = -2.334
inset_axes1.scatter(x_alpha_50_1, y_alpha_50_1, label='Data')
inset_axes1.plot(x_alpha_50_1, test_func(x_alpha_50_1, c, a),label='Fitted function')
inset_axes1.loglog()
inset_axes1.xaxis.set_major_formatter(formatter)
inset_axes1.xaxis.set_minor_formatter(formatter)
inset_axes1.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes1.set_xlim(95, 500)
inset_axes1.set_ylim(50, 10000)
inset_axes1.set_ylabel('Occurrences')
inset_axes1.set_xlabel("Vessel Radius(µm)")
x_beta_50_1 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_1 = [67, 55, 51, 47, 44, 41, 40, 39, 39]
x_beta_50_1_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_1_B = [35, 28, 20, 20, 19, 19]
x_beta_50_1_B_out = [0.1, 0.15, 0.2]
y_beta_50_1_B_out = [39, 37, 36]
c = 27.7355
a = -0.3763
c_b = 9.1231
a_b = -0.9099
inset_axes1_2.scatter(x_beta_50_1, y_beta_50_1,label='No Border')
inset_axes1_2.plot(x_beta_50_1, test_func(x_beta_50_1, c, a))
inset_axes1_2.scatter(x_beta_50_1_B, y_beta_50_1_B,label='Border',color='green')
inset_axes1_2.plot(x_beta_50_1_B, test_func(x_beta_50_1_B, c_b, a_b),color='green')
inset_axes1_2.scatter(x_beta_50_1_B_out, y_beta_50_1_B_out,label='Border - outliers',color='red')
inset_axes1_2.loglog()
inset_axes1_2.xaxis.set_major_formatter(formatter)
inset_axes1_2.xaxis.set_minor_formatter(formatter)
inset_axes1_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes1_2.yaxis.set_major_formatter(formatter)
inset_axes1_2.yaxis.set_minor_formatter(formatter)
inset_axes1_2.set_xlim(0.1, 0.5)
inset_axes1_2.set_ylim(15, 110)
inset_axes1_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes1_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes1_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes1_2.set_ylabel('Activation time(ms)')
inset_axes1_2.set_xlabel("Field Strength(V/cm)")

ax2 = fig.add_subplot(gs[1, 0], sharey=ax1)
ax2.text(.05,.95,'b - tree 2', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes, weight='bold')
inset_axes2 = inset_axes(ax2, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax2.transAxes)
inset_axes2_2 = inset_axes(ax2, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax2.transAxes)
x_alpha_50_2 = [100, 125, 150, 175, 200, 225, 250, 300, 325, 350, 375]
y_alpha_50_2 = [3090, 3240, 980, 660, 531, 524, 207, 84, 94, 103, 203]
c = 1595530753.375
a = -2.822
inset_axes2.scatter(x_alpha_50_2, y_alpha_50_2, label='Data')
inset_axes2.plot(x_alpha_50_2, test_func(x_alpha_50_2, c, a),label='Fitted function')
inset_axes2.loglog()
inset_axes2.xaxis.set_major_formatter(formatter)
inset_axes2.xaxis.set_minor_formatter(formatter)
inset_axes2.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes2.set_xlim(95, 500)
inset_axes2.set_ylim(50, 10000)
inset_axes2.set_ylabel('Occurrences')
inset_axes2.set_xlabel("Vessel Radius(µm)")
x_beta_50_2 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_2 = [0, 54, 39, 36, 34, 29, 27, 26, 26]
x_beta_50_2_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_2_B = [31, 26, 20, 18, 17, 17]
x_beta_50_2_B_out = [0.1, 0.15, 0.2]
y_beta_50_2_B_out = [34, 33, 32]
c = 15.1995
a = -0.6359
c_b = 8.1731
a_b = -0.9325
inset_axes2_2.scatter(x_beta_50_2, y_beta_50_2,label='No Border')
inset_axes2_2.plot(x_beta_50_2, test_func(x_beta_50_2, c, a))
inset_axes2_2.scatter(x_beta_50_2_B, y_beta_50_2_B,label='Border',color='green')
inset_axes2_2.plot(x_beta_50_2_B, test_func(x_beta_50_2_B, c_b, a_b),color='green')
inset_axes2_2.scatter(x_beta_50_2_B_out, y_beta_50_2_B_out,label='Border - outliers',color='red')
inset_axes2_2.loglog()
inset_axes2_2.xaxis.set_major_formatter(formatter)
inset_axes2_2.xaxis.set_minor_formatter(formatter)
inset_axes2_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes2_2.yaxis.set_major_formatter(formatter)
inset_axes2_2.yaxis.set_minor_formatter(formatter)
inset_axes2_2.set_xlim(0.1, 0.5)
inset_axes2_2.set_ylim(15, 110)
inset_axes2_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes2_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes2_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes2_2.set_ylabel('Activation time(ms)')
inset_axes2_2.set_xlabel("Field Strength(V/cm)")

ax3 = fig.add_subplot(gs[2, 0], sharey=ax1)
ax3.text(.05,.95,'c - tree 3', horizontalalignment='left', verticalalignment='top', transform=ax3.transAxes, weight='bold')
inset_axes3 = inset_axes(ax3, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax3.transAxes)
inset_axes3_2 = inset_axes(ax3, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax3.transAxes)
x_alpha_50_3 = [100, 125, 150, 175, 200, 225, 275, 300, 325]
y_alpha_50_3 = [597, 4448, 1788, 1074, 530, 523, 274, 126, 171]
c = 72941930266.347
a = -3.482
inset_axes3.scatter(x_alpha_50_3, y_alpha_50_3, label='Data')
inset_axes3.plot(x_alpha_50_3, test_func(x_alpha_50_3, c, a),label='Fitted function')
inset_axes3.loglog()
inset_axes3.xaxis.set_major_formatter(formatter)
inset_axes3.xaxis.set_minor_formatter(formatter)
inset_axes3.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes3.set_xlim(95, 500)
inset_axes3.set_ylim(50, 10000)
inset_axes3.set_ylabel('Occurrences')
inset_axes3.set_xlabel("Vessel Radius(µm)")
x_beta_50_3 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_3 = [0, 49, 37, 32, 26, 24, 23, 23, 22]
x_beta_50_3_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_50_3_B = [27, 26, 24, 20, 16, 16]
x_beta_50_3_B_out = [0.1, 0.15, 0.2]
y_beta_50_3_B_out = [28, 28, 27]
c = 9.6193
a = -0.8516
c_b = 8.7878
a_b = -0.8652
inset_axes3_2.scatter(x_beta_50_3, y_beta_50_3,label='No Border')
inset_axes3_2.plot(x_beta_50_3, test_func(x_beta_50_3, c, a))
inset_axes3_2.scatter(x_beta_50_3_B, y_beta_50_3_B,label='Border',color='green')
inset_axes3_2.plot(x_beta_50_3_B, test_func(x_beta_50_3_B, c_b, a_b),color='green')
inset_axes3_2.scatter(x_beta_50_3_B_out, y_beta_50_3_B_out,label='Border - outliers',color='red')
inset_axes3_2.loglog()
inset_axes3_2.xaxis.set_major_formatter(formatter)
inset_axes3_2.xaxis.set_minor_formatter(formatter)
inset_axes3_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes3_2.yaxis.set_major_formatter(formatter)
inset_axes3_2.yaxis.set_minor_formatter(formatter)
inset_axes3_2.set_xlim(0.1, 0.5)
inset_axes3_2.set_ylim(15, 110)
inset_axes3_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes3_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes3_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes3_2.set_ylabel('Activation time(ms)')
inset_axes3_2.set_xlabel("Field Strength(V/cm)")

ax4 = fig.add_subplot(gs[0, 1], sharey=ax1)
ax4.text(.05,.95,'d - tree 4', horizontalalignment='left', verticalalignment='top',transform=ax4.transAxes, weight='bold')
inset_axes4 = inset_axes(ax4, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax4.transAxes)
inset_axes4_2 = inset_axes(ax4, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax4.transAxes)
x_alpha_100_1 = [75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 425, 475]
y_alpha_100_1 = [4882, 3013, 1371, 1363, 549, 349, 537, 232, 239, 84, 207, 268, 241, 657]
c = 299815886.5500
a = -2.5255
inset_axes4.scatter(x_alpha_100_1, y_alpha_100_1, label='Data')
inset_axes4.plot(x_alpha_100_1, test_func(x_alpha_100_1, c, a),label='Fitted function')
inset_axes4.loglog()
inset_axes4.xaxis.set_major_formatter(formatter)
inset_axes4.xaxis.set_minor_formatter(formatter)
inset_axes4.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes4.set_xlim(70, 500)
inset_axes4.set_ylim(50, 10000)
inset_axes4.set_ylabel('Occurrences')
inset_axes4.set_xlabel("Vessel Radius(µm)")
x_beta_100_1 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_1 = [66, 57, 46, 40, 39, 37, 35, 33, 32]
x_beta_100_1_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_1_B = [40, 27, 23, 22, 21, 20]
x_beta_100_1_B_out = [0.1, 0.15, 0.2]
y_beta_100_1_B_out = [44, 43, 41]
c = 22.7000
a = -0.4589
c_b = 9.7890
a_b = -0.9200
inset_axes4_2.scatter(x_beta_100_1, y_beta_100_1,label='No Border')
inset_axes4_2.plot(x_beta_100_1, test_func(x_beta_100_1, c, a))
inset_axes4_2.scatter(x_beta_100_1_B, y_beta_100_1_B,label='Border',color='green')
inset_axes4_2.plot(x_beta_100_1_B, test_func(x_beta_100_1_B, c_b, a_b),color='green')
inset_axes4_2.scatter(x_beta_100_1_B_out, y_beta_100_1_B_out,label='Border - outliers',color='red')
inset_axes4_2.loglog()
inset_axes4_2.xaxis.set_major_formatter(formatter)
inset_axes4_2.xaxis.set_minor_formatter(formatter)
inset_axes4_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes4_2.yaxis.set_major_formatter(formatter)
inset_axes4_2.yaxis.set_minor_formatter(formatter)
inset_axes4_2.set_xlim(0.1, 0.5)
inset_axes4_2.set_ylim(15, 110)
inset_axes4_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes4_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes4_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes4_2.set_ylabel('Activation time(ms)')
inset_axes4_2.set_xlabel("Field Strength(V/cm)")


ax5 = fig.add_subplot(gs[1, 1], sharex=ax1)
ax5.text(.05,.95,'e - tree 5', horizontalalignment='left', verticalalignment='top',transform=ax5.transAxes, weight='bold')
inset_axes5 = inset_axes(ax5, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax5.transAxes)
inset_axes5_2 = inset_axes(ax5, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax5.transAxes)
x_alpha_100_2 = [75, 100, 125, 150, 175, 200, 225, 250, 300, 350, 375]
y_alpha_100_2 = [2730, 6515, 1801, 1095, 398, 613, 672, 537, 86, 95, 312]
c = 615740789.6030
a = -2.6091
inset_axes5.scatter(x_alpha_100_2, y_alpha_100_2, label='Data')
inset_axes5.plot(x_alpha_100_2, test_func(x_alpha_100_2, c, a),label='Fitted function')
inset_axes5.loglog()
inset_axes5.xaxis.set_major_formatter(formatter)
inset_axes5.xaxis.set_minor_formatter(formatter)
inset_axes5.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes5.set_xlim(95, 500)
inset_axes5.set_ylim(50, 10000)
inset_axes5.set_ylabel('Occurrences')
inset_axes5.set_xlabel("Vessel Radius(µm)")
x_beta_100_2 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_2 = [0, 63, 42, 39, 37, 36, 34, 33, 30]
x_beta_100_2_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_2_B = [29, 25, 23, 21, 20, 18]
x_beta_100_2_B_out = [0.1, 0.15, 0.2]
y_beta_100_2_B_out = [37, 36, 35]
c = 20.8699
a = -0.5083
c_b = 11.5843
a_b = -0.6538
inset_axes5_2.scatter(x_beta_100_2, y_beta_100_2,label='No Border')
inset_axes5_2.plot(x_beta_100_2, test_func(x_beta_100_2, c, a))
inset_axes5_2.scatter(x_beta_100_2_B, y_beta_100_2_B,label='Border',color='green')
inset_axes5_2.plot(x_beta_100_2_B, test_func(x_beta_100_2_B, c_b, a_b),color='green')
inset_axes5_2.scatter(x_beta_100_2_B_out, y_beta_100_2_B_out,label='Border - outliers',color='red')
inset_axes5_2.loglog()
inset_axes5_2.xaxis.set_major_formatter(formatter)
inset_axes5_2.xaxis.set_minor_formatter(formatter)
inset_axes5_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes5_2.yaxis.set_major_formatter(formatter)
inset_axes5_2.yaxis.set_minor_formatter(formatter)
inset_axes5_2.set_xlim(0.1, 0.5)
inset_axes5_2.set_ylim(15, 110)
inset_axes5_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes5_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes5_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes5_2.set_ylabel('Activation time(ms)')
inset_axes5_2.set_xlabel("Field Strength(V/cm)")

ax6 = fig.add_subplot(gs[2, 1], sharex=ax2, sharey = ax5)
ax6.text(.05,.95,'f - tree 6', horizontalalignment='left', verticalalignment='top',transform=ax6.transAxes, weight='bold')
inset_axes6 = inset_axes(ax6, width="40%", height="55%", loc="lower left", bbox_to_anchor=(0.15,0.28,0.75,0.75), bbox_transform=ax6.transAxes)
inset_axes6_2 = inset_axes(ax6, width="40%", height="55%", loc="lower right", bbox_to_anchor=(0.22,0.28,0.75,0.75), bbox_transform=ax6.transAxes)
x_alpha_100_3 = [75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325]
y_alpha_100_3 = [609, 5159, 4053, 1708, 970, 724, 362, 93, 225, 178, 171]
c = 38806610153.453
a = -3.3975
inset_axes6.scatter(x_alpha_100_3, y_alpha_100_3, label='Data')
inset_axes6.plot(x_alpha_100_3, test_func(x_alpha_100_3, c, a),label='Fitted function')
inset_axes6.loglog()
inset_axes6.xaxis.set_major_formatter(formatter)
inset_axes6.xaxis.set_minor_formatter(formatter)
inset_axes6.xaxis.set_minor_locator(MultipleLocator(250))
inset_axes6.set_xlim(95, 500)
inset_axes6.set_ylim(50, 10000)
inset_axes6.set_ylabel('Occurrences')
inset_axes6.set_xlabel("Vessel Radius(µm)")
x_beta_100_3 = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_3 = [0, 52, 40, 35, 28, 26, 25, 23, 23]
x_beta_100_3_B = [0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
y_beta_100_3_B = [30, 26, 25, 18, 17, 16]
x_beta_100_3_B_out = [0.1, 0.15, 0.2]
y_beta_100_3_B_out = [32, 32, 32]
c = 12.2377
a = -0.7458
c_b = 7.9585
a_b = -0.9803
inset_axes6_2.scatter(x_beta_100_3, y_beta_100_3,label='No Border')
inset_axes6_2.plot(x_beta_100_3, test_func(x_beta_100_3, c, a))
inset_axes6_2.scatter(x_beta_100_3_B, y_beta_100_3_B,label='Border',color='green')
inset_axes6_2.plot(x_beta_100_3_B, test_func(x_beta_100_3_B, c_b, a_b),color='green')
inset_axes6_2.scatter(x_beta_100_3_B_out, y_beta_100_3_B_out,label='Border - outliers',color='red')
inset_axes6_2.loglog()
inset_axes6_2.xaxis.set_major_formatter(formatter)
inset_axes6_2.xaxis.set_minor_formatter(formatter)
inset_axes6_2.xaxis.set_minor_locator(MultipleLocator(0.25))
inset_axes6_2.yaxis.set_major_formatter(formatter)
inset_axes6_2.yaxis.set_minor_formatter(formatter)
inset_axes6_2.set_xlim(0.1, 0.5)
inset_axes6_2.set_ylim(15, 110)
inset_axes6_2.yaxis.set_major_locator(ticker.MultipleLocator(1000))
inset_axes6_2.yaxis.set_minor_locator(ticker.MultipleLocator(25))
inset_axes6_2.legend(bbox_to_anchor=(-0.25, 1.03, 1.25, .102), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
inset_axes6_2.set_ylabel('Activation time(ms)')
inset_axes6_2.set_xlabel("Field Strength(V/cm)")

axs = [ax1, ax2, ax3, ax4, ax5, ax6]
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])


#plt.show()
plt.savefig("Simulations.pdf", dpi=1200)


from pathlib import Path
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
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, wspace = 0, hspace = 0, left=0.005, bottom=0.005, right=0.995, top=0.995)

ax1 = fig.add_subplot(gs[0, 1])
ax1.text(.05,.95,'b', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes, weight='bold')
inset_axes1 = inset_axes(ax1, width="90%", height="90%", loc="lower left", bbox_to_anchor=(0.225,0.20,0.75,0.75), bbox_transform=ax1.transAxes)
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y1 = [9.61,10.03,6.63,5.55,4.29]
y2 = [9.22,11.35,7.85,6.32,5.78]
y3 = [2.71,13.28,8.78,8.79,7.59]
inset_axes1.plot(x, y1, "-o", label = "1 vs 2")
inset_axes1.plot(x, y2, "-D", label = "1 vs 3")
inset_axes1.plot(x, y3, "-s", label = "1 vs 4")
inset_axes1.set_xlabel("Field Strength(V/cm)")
inset_axes1.set_ylabel("Difference in activation time(ms)")
inset_axes1.legend()


y_1_01 = [39.95, 39.55, 39.4, 39.6, 40.45, 39.2]
y_1_02 = [34.7, 34.7, 34.65, 35.1, 35.2, 34.45]
y_1_03 = [28.8, 27.9, 21.55, 33.15, 31.45, 26]
y_1_04 = [25.3, 24.15, 19.55, 29.6, 28.7, 22.9]
y_1_05 = [24, 23.1, 18.35, 23.05, 27.55, 21.75]

y_2_01 = [24.55, 35.35, 24.45, 35.6, 25.2, 35.35]
y_2_02 = [21.65, 27.75, 21.55, 27.95, 22.3, 27.4]
y_2_03 = [18.2, 23, 18.95, 25.05, 19.4, 24.45]
y_2_04 = [16.5, 21.15, 16.3, 23.55, 17, 22.4]
y_2_05 = [15.8, 20.3, 15.35, 22.4, 16.9, 21.3]

y_3_01 = [25.2, 35.55, 25.5, 35.8, 25.3, 35.5]
y_3_02 = [20.95, 26.1, 20.55, 26.05, 21.1, 26]
y_3_03 = [18.15, 21.5, 18.85, 23, 17.95, 22.3]
y_3_04 = [18.85, 20, 15.6, 21.4, 16.25, 20.2]
y_3_05 = [15.2, 18.4, 14.95, 20.4, 15.15, 19.05]

y_4_01 = [31.2, 38.6, 42.9, 39, 31.75, 38.45]
y_4_02 = [20.4, 22.7, 20.25, 22.4, 20.85, 22.55]
y_4_03 = [18.65, 19.15, 19.6, 20.8, 19, 19]
y_4_04 = [15.2, 16.25, 15.6, 18.55, 15.15, 16.7]
y_4_05 = [14.7, 15.55, 14.5, 17.5, 14.2, 15.85]

eixox = "Field Strength(V/cm)"
eixoy = "Activation time(ms)"

y_01 = [y_1_01, y_2_01, y_3_01, y_4_01]
y_02 = [y_1_02, y_2_02, y_3_02, y_4_02]
y_03 = [y_1_03, y_2_03, y_3_03, y_4_03]
y_04 = [y_1_04, y_2_04, y_3_04, y_4_04]
y_05 = [y_1_05, y_2_05, y_3_05, y_4_05]
medianprops = dict(linestyle='-', linewidth=0.5, color='black')
boxprops = dict(linewidth=0.5, color='black')
whiskerprops = dict(linestyle='-',linewidth=0.5, color='black')


ax2 = fig.add_subplot(gs[0, 0], sharey=ax1)
ax2.text(.05,.95,'a', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes, weight='bold')
inset_axes2_1 = inset_axes(ax2, width="15%", height="60%", loc="lower left", bbox_to_anchor=(0.15,0.15,1,1), bbox_transform=ax2.transAxes)
inset_axes2_2 = inset_axes(ax2, width="15%", height="60%", loc="lower left", bbox_to_anchor=(0.30,0.15,1,1), bbox_transform=ax2.transAxes)
inset_axes2_3 = inset_axes(ax2, width="15%", height="60%", loc="lower left", bbox_to_anchor=(0.45,0.15,1,1), bbox_transform=ax2.transAxes)
inset_axes2_4 = inset_axes(ax2, width="15%", height="60%", loc="lower left", bbox_to_anchor=(0.60,0.15,1,1), bbox_transform=ax2.transAxes)
inset_axes2_5 = inset_axes(ax2, width="15%", height="60%", loc="lower left", bbox_to_anchor=(0.75,0.15,1,1), bbox_transform=ax2.transAxes)

box01 = inset_axes2_1.boxplot(y_01, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box02 = inset_axes2_2.boxplot(y_02, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box03 = inset_axes2_3.boxplot(y_03, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box04 = inset_axes2_4.boxplot(y_04, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box05 = inset_axes2_5.boxplot(y_05, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
ax2.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
ax2.text(.55,.025,eixox, horizontalalignment='center', verticalalignment='bottom',transform=ax2.transAxes, fontsize = 9)
inset_axes2_1.set_ylabel(eixoy)

inset_axes2_1.set_xticks([])
inset_axes2_2.set_xticks([])
inset_axes2_3.set_xticks([])
inset_axes2_4.set_xticks([])
inset_axes2_5.set_xticks([])

inset_axes2_1.set_ylim(10, 50)
inset_axes2_2.set_ylim(10, 50)
inset_axes2_3.set_ylim(10, 50)
inset_axes2_4.set_ylim(10, 50)
inset_axes2_5.set_ylim(10, 50)

inset_axes2_2.set_yticks([])
inset_axes2_3.set_yticks([])
inset_axes2_4.set_yticks([])
inset_axes2_5.set_yticks([])

ax2.set_ylim(50, 10000)

inset_axes2_1.set(xlabel='0.1')
inset_axes2_2.set(xlabel='0.2')
inset_axes2_3.set(xlabel='0.3')
inset_axes2_4.set(xlabel='0.4')
inset_axes2_5.set(xlabel='0.5')

inset_axes2_1.yaxis.set_tick_params(size=0)
inset_axes2_2.yaxis.set_tick_params(size=0)
inset_axes2_3.yaxis.set_tick_params(size=0)
inset_axes2_4.yaxis.set_tick_params(size=0)
inset_axes2_5.yaxis.set_tick_params(size=0)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for bplot in (box01, box02, box03, box04, box05):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

ax2.legend([box01["boxes"][0], box01["boxes"][1], box01["boxes"][2], box01["boxes"][3]], ['1 direction', '2 directions', '3 directions', '4 directions'], ncol=2, loc='upper center')

axs = [ax1, ax2]
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])


#plt.show()
plt.savefig("times_directions.pdf", dpi=1200)


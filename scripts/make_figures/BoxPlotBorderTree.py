from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

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
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig, axs = plt.subplots(1, 5,sharey=True, gridspec_kw={'wspace': 0})

y_01 = [y_1_01, y_2_01, y_3_01, y_4_01]
y_02 = [y_1_02, y_2_02, y_3_02, y_4_02]
y_03 = [y_1_03, y_2_03, y_3_03, y_4_03]
y_04 = [y_1_04, y_2_04, y_3_04, y_4_04]
y_05 = [y_1_05, y_2_05, y_3_05, y_4_05]

medianprops = dict(linestyle='-', linewidth=0.5, color='black')
boxprops = dict(linewidth=0.5, color='black')
whiskerprops = dict(linestyle='-',linewidth=0.5, color='black')
box01 = axs[0].boxplot(y_01, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box02 = axs[1].boxplot(y_02, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box03 = axs[2].boxplot(y_03, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box04 = axs[3].boxplot(y_04, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
box05 = axs[4].boxplot(y_05, whis = 50, patch_artist=True, medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, widths = 0.7)
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel(eixox)
plt.ylabel(eixoy)
#plt.legend()

axs[0].set_xticks([])
axs[1].set_xticks([])
axs[2].set_xticks([])
axs[3].set_xticks([])
axs[4].set_xticks([])

axs[0].set(xlabel='0.1')
axs[1].set(xlabel='0.2')
axs[2].set(xlabel='0.3')
axs[3].set(xlabel='0.4')
axs[4].set(xlabel='0.5')

axs[1].yaxis.set_tick_params(size=0)
axs[2].yaxis.set_tick_params(size=0)
axs[3].yaxis.set_tick_params(size=0)
axs[4].yaxis.set_tick_params(size=0)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for bplot in (box01, box02, box03, box04, box05):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

plt.legend([box01["boxes"][0], box01["boxes"][1], box01["boxes"][2], box01["boxes"][3]], ['1 direction', '2 directions', '3 directions', '4 directions'])
#plt.show()
plt.savefig("BoxPlotBorderTree.pdf")

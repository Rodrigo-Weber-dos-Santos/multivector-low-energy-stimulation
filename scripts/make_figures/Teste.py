from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

imgV1 = mpimg.imread('fig_vessels_2.png')
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, wspace = 0, hspace = 0)
ax1 = fig.add_subplot(gs[0, 0])
ax1.text(.05,.95,'A', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes)
ax1.text(.5,.05,' CCO', horizontalalignment='center', verticalalignment='center',transform=ax1.transAxes, fontsize=12)
ax2 = fig.add_subplot(gs[0, 1], sharey=ax1)
ax2.text(.05,.95,'B', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes)
ax2.text(.5,.05,' Smoothing', horizontalalignment='center', verticalalignment='center',transform=ax2.transAxes, fontsize=12)
axs = [ax1, ax2]
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
img = ax1.imshow(imgV1, cmap='RdBu_r')
img.set_clim([0, 1])
#ax2.imshow(imgV2)
axins1 = inset_axes(ax1, width="5%", height="80%", loc='right')
cbar = fig.colorbar(img, cax = axins1, ax=ax1, ticks=[0,0.2,0.4,0.6,0.8,1.0], orientation='vertical')
cbar.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
axins1.yaxis.set_ticks_position("left")
plt.show()
#plt.savefig("teste.pdf", dpi=1200)


from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable

img = mpimg.imread('fig_vessels_2.png')
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, wspace = 0, hspace = 0, left=0.005, bottom=0.005, right=0.995, top=0.995)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_xticks([])
ax1.set_yticks([])
ax1.text(.025,.9834,'a', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes, weight='bold')
img = ax1.imshow(img, cmap='RdBu_r', aspect = 'auto')
img.set_clim([0, 1])
axins1 = inset_axes(ax1, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax1.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar = fig.colorbar(img, ax=ax1, cax = axins1, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
#ax.set(ylabel='Vessel Radius(µm)')
ax1.yaxis.set_label_position("right")
cbar.set_label("Vessel Radius(µm)")
#axins1.yaxis.set_ticks_position("left")

ax_aux = fig.add_subplot(gs[0, 1])
ax_aux.set_xticks([])
ax_aux.set_yticks([])

innerGs = gridspec.GridSpecFromSubplotSpec(3, 2,gs[0, 1], wspace=0, hspace=0.0)

imgV1 = mpimg.imread('V1.png')
ax2 = plt.Subplot(fig, innerGs[0, 0])
ax2.imshow(imgV1, aspect = 'auto')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.text(.05,.95,'b', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes, weight='bold')
ax2.text(.5,.05,'v1 = (1, 0, 0)', horizontalalignment='center', verticalalignment='center',transform=ax2.transAxes, fontsize=9)
fig.add_subplot(ax2)

imgV2 = mpimg.imread('V2.png')
ax3 = plt.Subplot(fig, innerGs[0, 1])
ax3.imshow(imgV2, aspect = 'auto')
ax3.set_xticks([])
ax3.set_yticks([])
ax3.text(.05,.95,'c', horizontalalignment='left', verticalalignment='top',transform=ax3.transAxes, weight='bold')
ax3.text(.5,.05,'v2 = (-1, 0, 0)', horizontalalignment='center', verticalalignment='center',transform=ax3.transAxes, fontsize=9)
fig.add_subplot(ax3)

imgV3 = mpimg.imread('V3.png')
ax4 = plt.Subplot(fig, innerGs[1, 0])
ax4.imshow(imgV3, aspect = 'auto')
ax4.set_xticks([])
ax4.set_yticks([])
ax4.text(.05,.95,'d', horizontalalignment='left', verticalalignment='top',transform=ax4.transAxes, weight='bold')
ax4.text(.5,.05,'v3 = (0, 1, 0)', horizontalalignment='center', verticalalignment='center',transform=ax4.transAxes, fontsize=9)
fig.add_subplot(ax4)

imgV4 = mpimg.imread('V4.png')
ax5 = plt.Subplot(fig, innerGs[1, 1])
ax5.imshow(imgV4, aspect = 'auto')
ax5.set_xticks([])
ax5.set_yticks([])
ax5.text(.05,.95,'e', horizontalalignment='left', verticalalignment='top',transform=ax5.transAxes, weight='bold')
ax5.text(.5,.05,'v4 = (0, -1, 0)', horizontalalignment='center', verticalalignment='center',transform=ax5.transAxes, fontsize=9)
fig.add_subplot(ax5)

imgV5 = mpimg.imread('V5.png')
ax6 = plt.Subplot(fig, innerGs[2, 0])
ax6.imshow(imgV5, aspect = 'auto')
ax6.set_xticks([])
ax6.set_yticks([])
ax6.text(.05,.95,'f', horizontalalignment='left', verticalalignment='top',transform=ax6.transAxes, weight='bold')
ax6.text(.5,.05,'v5 = (0, 0, 1)', horizontalalignment='center', verticalalignment='center',transform=ax6.transAxes, fontsize=9)
fig.add_subplot(ax6)

imgV6 = mpimg.imread('V6.png')
ax7 = plt.Subplot(fig, innerGs[2, 1])
ax7.imshow(imgV6, aspect = 'auto')
ax7.set_xticks([])
ax7.set_yticks([])
ax7.text(.05,.95,'g', horizontalalignment='left', verticalalignment='top',transform=ax7.transAxes, weight='bold')
ax7.text(.5,.05,'v6 = (0, 0, -1)', horizontalalignment='center', verticalalignment='center',transform=ax7.transAxes, fontsize=9)
fig.add_subplot(ax7)

#plt.show()
plt.savefig("radius_vectors.pdf", dpi=1200)


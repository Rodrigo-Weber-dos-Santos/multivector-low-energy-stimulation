import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

imgV1 = mpimg.imread('tree1_3.png')
imgV2 = mpimg.imread('tree2_3.png')
imgV3 = mpimg.imread('tree3_3.png')
imgV4 = mpimg.imread('tree4_3.png')
imgV5 = mpimg.imread('tree5_3.png')
imgV6 = mpimg.imread('tree6_3.png')
plt.style.use('PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, wspace = 0, hspace = 0, left=0.005, bottom=0.005, right=0.995, top=0.995)
ax1 = fig.add_subplot(gs[0, 0])
ax1.text(.05,.95,'a', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes, weight='bold')
#ax1.text(.5,.05,'Tree 1 - 50 vessels', horizontalalignment='center', verticalalignment='center',transform=ax1.transAxes, fontsize=9)
ax2 = fig.add_subplot(gs[0, 1], sharey=ax1)
ax2.text(.05,.95,'b', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes, weight='bold')
#ax2.text(.5,.05,'Tree 2 - 50 vessels', horizontalalignment='center', verticalalignment='center',transform=ax2.transAxes, fontsize=9)
ax3 = fig.add_subplot(gs[0, 2], sharey=ax1)
ax3.text(.05,.95,'c', horizontalalignment='left', verticalalignment='top', transform=ax3.transAxes, weight='bold')
#ax3.text(.5,.05,'Tree 3 - 50 vessels', horizontalalignment='center', verticalalignment='center', transform=ax3.transAxes, fontsize=9)
ax4 = fig.add_subplot(gs[1, 0], sharey=ax1)
ax4.text(.05,.95,'d', horizontalalignment='left', verticalalignment='top',transform=ax4.transAxes, weight='bold')
#ax4.text(.5,.05,'Tree 4 - 100 vessels', horizontalalignment='center', verticalalignment='center',transform=ax4.transAxes, fontsize=9)
ax5 = fig.add_subplot(gs[1, 1], sharex=ax1)
ax5.text(.05,.95,'e', horizontalalignment='left', verticalalignment='top',transform=ax5.transAxes, weight='bold')
#ax5.text(.5,.05,'Tree 5 - 100 vessels', horizontalalignment='center', verticalalignment='center',transform=ax5.transAxes, fontsize=9)
ax6 = fig.add_subplot(gs[1, 2], sharex=ax2, sharey = ax5)
ax6.text(.05,.95,'f', horizontalalignment='left', verticalalignment='top',transform=ax6.transAxes, weight='bold')
#ax6.text(.5,.05,'Tree 6 - 100 vessels', horizontalalignment='center', verticalalignment='center',transform=ax6.transAxes, fontsize=9)
axs = [ax1, ax2, ax3, ax4, ax5, ax6]
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
img1 = ax1.imshow(imgV1, cmap='RdBu_r')
img1.set_clim([0, 1])
axins1 = inset_axes(ax1, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax1.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar1 = fig.colorbar(img1, ax=ax1, cax = axins1, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar1.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax1.yaxis.set_label_position("right")
cbar1.set_label("Vessel Radius(µm)")

img2 = ax2.imshow(imgV2, cmap='RdBu_r')
img2.set_clim([0, 1])
axins2 = inset_axes(ax2, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax2.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar2 = fig.colorbar(img2, ax=ax2, cax = axins2, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar2.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax2.yaxis.set_label_position("right")
cbar2.set_label("Vessel Radius(µm)")

img3 = ax3.imshow(imgV3, cmap='RdBu_r')
img3.set_clim([0, 1])
axins3 = inset_axes(ax3, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax3.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar3 = fig.colorbar(img3, ax=ax3, cax = axins3, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar3.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax3.yaxis.set_label_position("right")
cbar3.set_label("Vessel Radius(µm)")

img4 = ax4.imshow(imgV4, cmap='RdBu_r')
img4.set_clim([0, 1])
axins4 = inset_axes(ax4, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax4.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar4 = fig.colorbar(img4, ax=ax4, cax = axins4, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar4.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax4.yaxis.set_label_position("right")
cbar4.set_label("Vessel Radius(µm)")

img5 = ax5.imshow(imgV5, cmap='RdBu_r')
img5.set_clim([0, 1])
axins5 = inset_axes(ax5, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax5.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar5 = fig.colorbar(img5, ax=ax5, cax = axins5, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar5.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax5.yaxis.set_label_position("right")
cbar5.set_label("Vessel Radius(µm)")

img6 = ax6.imshow(imgV6, cmap='RdBu_r')
img6.set_clim([0, 1])
axins6 = inset_axes(ax6, width="5%", height="80%", loc='center right', bbox_to_anchor=(0.2,0,.6,1), bbox_transform=ax6.transAxes)
#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar6 = fig.colorbar(img6, ax=ax6, cax = axins6, ticks=[0,0.2,0.4,0.6,0.8,1.0])
cbar6.ax.set_yticklabels(['100', '200', '300', '400', '500', '600'])  # vertically oriented colorbar
ax6.yaxis.set_label_position("right")
cbar6.set_label("Vessel Radius(µm)")



#plt.show()
plt.savefig("trees.pdf", dpi=1200)


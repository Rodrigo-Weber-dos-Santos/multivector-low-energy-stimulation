from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec

imgV1 = mpimg.imread('FiguraAtivacaoCoracaoSemBorda_x.png')
imgV2 = mpimg.imread('FiguraAtivacaoCoracaoSemBorda_X.png')
imgV3 = mpimg.imread('FiguraAtivacaoCoracaoSemBorda_y.png')
imgV4 = mpimg.imread('FiguraAtivacaoCoracaoSemBorda_Y.png')
imgVT = mpimg.imread('FiguraAtivacaoCoracaoSemBorda_ALL.png')
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, wspace = 0, hspace = 0, left=0.005, bottom=0.005, right=0.995, top=0.995)
ax1 = fig.add_subplot(gs[0, 0])
ax1.text(.05,.95,'a', horizontalalignment='left', verticalalignment='top',transform=ax1.transAxes, weight='bold')
ax2 = fig.add_subplot(gs[0, 1], sharey=ax1)
ax2.text(.05,.95,'b', horizontalalignment='left', verticalalignment='top',transform=ax2.transAxes, weight='bold')
ax3 = fig.add_subplot(gs[0, 2], sharey=ax1)
ax3.text(.05,.95,'c', horizontalalignment='left', verticalalignment='top',transform=ax3.transAxes, weight='bold')
ax4 = fig.add_subplot(gs[1, 0], sharey=ax1)
ax4.text(.05,.95,'d', horizontalalignment='left', verticalalignment='top',transform=ax4.transAxes, weight='bold')
ax7 = fig.add_subplot(gs[1, 1:], sharey = ax4)
ax7.text(.025,.95,'e', horizontalalignment='left', verticalalignment='top',transform=ax7.transAxes, weight='bold')
axs = [ax1, ax2, ax3, ax4, ax7]
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
ax1.imshow(imgV1)
ax2.imshow(imgV2)
ax3.imshow(imgV3)
ax4.imshow(imgV4)
ax7.imshow(imgVT)
#axs[1][3].remove()
#axs[1][2].remove()
#gs = gridspec.GridSpec(2,4)
#ax7 = fig.add_subplot(gs[1, -2:)
#ax7.set_xticks([])
#ax7.set_yticks([])
#ax7.text(.15,.9,'A',
#horizontalalignment='center',
#transform=ax.transAxes)
#plt.show()
plt.savefig("MapaAtivacaoC.pdf", dpi=1200)


from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
plt.margins(0.5)
x = np.linspace(-4,-2,10)
y = (x+1)/3
#x1 = [-2.3,-2.83,-3.4,-2.3,-2.83,-3.4,-2.52,-2.6,-3.4,-2.52,-2.6,-3.4]
#y1 = [-0.38,-0.63,-0.85,-0.43,-0.68,-0.86,-0.46,-0.51,-0.75,-0.58,-0.49,-0.83]
x1 = [-2.3,-2.83,-3.4,-2.52,-2.6,-3.4]
y1 = [-0.38,-0.63,-0.85,-0.46,-0.51,-0.75]
y2 = [-0.91,-0.93,-0.87,-0.92,-0.65,-0.98]
eixox = "\u03B1"
eixoy = "\u03B2"
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
fig = plt.figure()
fig.tight_layout()
#plt.locator_params(axis='x', nbins=5)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.plot(x1, y1, "o", label = "No Border")
plt.plot(x1, y2, "^", label = "Border")
plt.plot(x, y, "-", label = "β = (α+1)/3",color="red")
plt.legend()
#plt.show()
plt.savefig("AlphaXBeta.pdf")

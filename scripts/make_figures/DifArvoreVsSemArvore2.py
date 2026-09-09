from pathlib import Path
import matplotlib.pyplot as plt
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y1 = [0.010000000000005, 0.020000000000003, 4.8, 6.9, 8.3]
y2 = [0, 0.010000000000002, 1.39, 2.52, 2.71]
y3 = [0, 0.02, 1.23, 1.69, 2.77]
y4 = [0.220000000000006, 0.010000000000002, 0.920000000000002, 3.51, 4.07]

eixox = "Field Strength(V/cm)"
eixoy = "Difference in activation time(ms)"
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
plt.locator_params(axis='x', nbins=5)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.plot(x, y1, "-o", label = "1 vectors")
plt.plot(x, y2, "-D", label = "2 vectors")
plt.plot(x, y3, "-s", label = "3 vectors")
plt.plot(x, y4, "-^", label = "4 vectors")
plt.legend()
#plt.show()
plt.savefig("DifArvoreVsSemArvore2.pdf")

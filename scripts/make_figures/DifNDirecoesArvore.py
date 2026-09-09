from pathlib import Path
import matplotlib.pyplot as plt
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y1 = [9.61,10.03,6.63,5.55,4.29]
y2 = [9.22,11.35,7.85,6.32,5.78]
y3 = [2.71,13.28,8.78,8.79,7.59]

eixox = "Field Strength(V/cm)"
eixoy = "Difference in activation time(ms)"
plt.style.use(Path(__file__).resolve().parent / 'PlotStyle.mplstyle')
plt.locator_params(axis='x', nbins=5)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.plot(x, y1, "-o", label = "1 vs 2")
plt.plot(x, y2, "-D", label = "1 vs 3")
plt.plot(x, y3, "-s", label = "1 vs 4")
plt.legend()
#plt.show()
plt.savefig("DifNDirecoesArvore.pdf")

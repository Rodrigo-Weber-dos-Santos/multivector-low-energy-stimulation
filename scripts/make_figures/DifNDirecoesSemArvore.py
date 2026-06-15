import matplotlib.pyplot as plt
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y1 = [9.62,10.04,10.04,9.93,9.88]
y2 = [9.23,11.35,11.42,11.53,11.31]
y3 = [2.5,13.29,12.66,12.18,11.82]

eixox = "Field Strength(V/cm)"
eixoy = "Difference in activation time(ms)"
plt.style.use('PlotStyle.mplstyle')
plt.locator_params(axis='x', nbins=5)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.plot(x, y1, "-o", label = "1 vs 2")
plt.plot(x, y2, "-D", label = "2 vs 3")
plt.plot(x, y3, "-s", label = "3 vs 4")
plt.legend()
#plt.show()
plt.savefig("DifNDirecoesSemArvore.pdf")

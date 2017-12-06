from pylab import  *
import pylab
import matplotlib.ticker as mtick
import numpy as np

x = [0.02, 0.05, 0.10, 0.20,0.30,0.40,0.50,0.60,0.70,0.80]
perc = [x[j] * 100 for j in range(len(x))]
y =[0.80,0.50,0.40,0.20,0.12,0.10,0.05,0.04,0.03,0.02]
percy = [y[i] *100 for i in range(len(y))]
print(percy)
fig = plt.figure(1, (7,4))
ax = fig.add_subplot(1,1,1)

ax.plot(perc, percy)
fmt = '%.0f%%'
xticks = mtick.FormatStrFormatter(fmt)
ax.xaxis.set_major_formatter(xticks)
ax.yaxis.set_major_formatter(xticks)
xlabel("False positive Rate")
ylabel('Fase Negative Rate')

title("DET curve")
plt.show()
from pylab import  *
import pylab
import matplotlib.ticker as mtick
import numpy as np

x = [20,40,60,80,100]

y =[0.699229,0.699229,0.705656,0.703085,0.70437]
percy = [y[i] *100 for i in range(len(y))]
y1 = [0.694087, 0.694087, 0.694087, 0.694087, 0.694087]
percy1 = [y1[i] *100 for i in range(len(y1))]
y2 = [0.737789,0.733933,0.735219,0.732648,0.731362]
percy2 = [y2[i] *100 for i in range(len(y2))]
fig = plt.figure(1, (7,4))
ax = fig.add_subplot(1,1,1)

ax.plot(x, percy, x, percy1, x, percy2)
fmt = '%.0f%%'
xticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(xticks)
xlabel("Ensemble Sizes")
ylabel('Accuracy%')
pylab.plot(x, percy, '-b',label='Bagging')
pylab.plot(x, percy1, '-g', label='Boosting')
pylab.plot(x, percy2, '-r', label='Random Subspace')
pylab.legend(loc='upper right')
title("3-NN with 3 different ensemble strategies")
plt.show()

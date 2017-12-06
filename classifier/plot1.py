from pylab import  *
import pylab
from scipy.interpolate import spline
import numpy as np

t = pylab.frange(0,21, 4)
x = np.array([1,5,7,11,13])
y1 = np.array([96.7, 96.6, 95.8,95.6, 94.7])
x_smooth = np.linspace(x.min(), x.max(),300)
y_smooth = spline(x,y1,x_smooth)
plot(x_smooth,y_smooth,label="smoothing line")
plot(x,y1, label="points line")
pylab.legend(loc='upper right')

T=np.array([2,3,5,10,15])
power= np.array([96.27, 97.02, 96.81,97.08, 96.39])
xnew = np.linspace(T.min(), T.max(),1000)
power_smooth = spline(T,power,xnew)

#plot(xnew, power_smooth)

xlabel("K values")
ylabel('Accuracy %')

title('Accuracy for different k values with split 0.7')
grid(True)
show()
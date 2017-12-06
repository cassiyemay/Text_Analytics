from pylab import  *

t = arange(2,6, 1)
y1 = (49, 47, 52, 52)
plot(t, y1)

xlabel("4 normal_tweets")
ylabel('edit_distance')
plt.axis([2, 5, 0, 60])
title('edit_distance scores between t1 and other 4 normal tweets')
grid(True)
show()
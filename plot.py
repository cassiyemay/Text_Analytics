from pylab import  *
import pylab

t = arange(1,21, 1)
y1= (10, 20, 32, 45, 73, 28, 50, 17, 32, 50, 17, 38, 26, 30, 22, 39, 19, 16, 44, 21)
y2 =(51, 57, 66, 78, 103, 50, 81, 54, 70, 67, 56, 57, 51, 52, 63, 60, 57, 55, 64, 60)
y3 =(48, 54, 68, 81, 105, 51, 82, 54, 67, 69, 53, 59, 48, 52, 61, 61, 54, 53, 63, 57)
y4 =(51, 57, 66, 80, 99, 56, 82, 58, 66, 69, 58, 62, 56, 59, 60, 63, 57, 56, 66, 59)
y5 =(54, 58, 69, 83, 103, 56, 85, 57, 70, 70, 56, 63, 56, 58, 63, 62, 60, 57, 67, 61)
plot(t, y1,t,y2,t,y3,t,y4,t,y5)

xlabel("20 spam_tweets")
ylabel('edit_distance')
pylab.plot(t, y1,'-b', label='normal_tweet1')
pylab.plot(t, y2, '-r',label='normal_tweet2')
pylab.plot(t, y3, '-g',label='normal_tweet3')
pylab.plot(t, y4, label='normal_tweet4')
pylab.plot(t, y5, label='normal_tweet5')
pylab.legend(loc='upper right')
title('edit_distance scores between 5 normal tweets and 20 spam tweets')
grid(True)
show()
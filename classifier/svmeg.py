__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
import time
start=time.time()

digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.00001, C=10000)

x, y = digits.data[:-10], digits.target[:-10]
classifier.fit(x, y)

print('Prediction:', classifier.predict(digits.data[-5]))
print(time.time() - start)

plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

import csv
import random
import math
import operator
from classifier.Knn import *


def get_averageAccuracy(trainingSet, testSet, predictions):
    k=5
    sum=0
    for i in range(5):
        loadDataset('iris.csv',4/k, trainingSet, testSet)
        predictions=[]
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            results = getResponse(neighbors)
            predictions.append(results)
        accuracy = getAccuracy(testSet, predictions)
        sum +=accuracy

    return sum/k

trainingSet=[]
testSet=[]
predictions=[]

#print(trainingSet)
#print(testSet)
print(get_averageAccuracy(trainingSet,testSet,predictions))
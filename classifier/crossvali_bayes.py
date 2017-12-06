import  nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'last_letter': word[-1]}

def genderfeatures(word):
    return {'last_3letter': word[-3:], "last_twoletters": word[-2:],'last_letter': word[-1]}

male_names = [(name, 'male') for name in names.words('male.txt')]

female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets =[(gender_features(n), gender) for (n, gender) in labeled_names]
featureset = [(genderfeatures(n), gender) for (n, gender) in labeled_names]
#train_set, test_set = featuresets[500:], featuresets[:500]

#classifier =nltk.NaiveBayesClassifier.train(train_set)

def loadDataset(featuresets, split, trainingSet=[] , testSet=[]):
	    for x in range(len(featuresets)):
	        if random.random() < split:
	            trainingSet.append(featuresets[x])
	        else:
	            testSet.append(featuresets[x])

def get_averageAccuracy(trainingSet, testSet):
    k=5
    totalaccuracy=0
    for i in range(5):
        loadDataset(featureset,4/k, trainingSet, testSet)
        classifier = nltk.NaiveBayesClassifier.train(trainingSet)
        sum = 0
        for x in range(len(testSet)):
            prediction1 = (classifier.classify(testSet[i][0]))
            if prediction1 == testSet[i][1]:
                sum += 1
        accuracy=sum/len(testSet)
        totalaccuracy +=accuracy

    return totalaccuracy/k

def get_averageAccuracy1(trainingSet, testSet):
    k=5
    totalaccuracy=0
    for i in range(5):
        loadDataset(featuresets,4/k, trainingSet, testSet)
        classifier = nltk.NaiveBayesClassifier.train(trainingSet)
        sum = 0
        for x in range(len(testSet)):
            prediction1 = (classifier.classify(testSet[i][0]))
            if prediction1 == testSet[i][1]:
                sum += 1
        accuracy=sum/len(testSet)
        totalaccuracy +=accuracy

    return totalaccuracy/k
trainingSet=[]
testSet=[]

#print(trainingSet)
#print(testSet)
print(get_averageAccuracy(trainingSet,testSet))
print(get_averageAccuracy1(trainingSet,testSet))



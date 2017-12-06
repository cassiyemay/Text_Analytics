import re, math, collections, itertools, sys, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures, scores
from nltk.probability import FreqDist, ConditionalFreqDist

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fdist1 = FreqDist(text1)
print(fdist1)
vocabulary = fdist1.keys()
print(vocabulary)
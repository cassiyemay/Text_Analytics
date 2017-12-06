import math
from collections import Counter
import  nltk
import nltk.cluster
import  nltk.cluster.util
import scipy.spatial.distance
from nltk.metrics import distance
import numpy as np

vector_dict = {}

def load_docs():
    doc1 = ('d1', 'semantic analysis for building model')
    doc2 = ('d2', 'learning latent semantic indexing')
    doc3 = ('d3', 'analysis of latent structures and semantic analysis of structures')
    doc4 = ('d4', 'books on latent structures for semantic analysis authored and published by university professor Keane')
    doc5 = ('d5', 'advances in structures and advances in semantic structures')
    doc6 = ('d6', 'books on semantic analysis')
    doc7 = ('d7', 'latent structures for semantic analysis')
    doc8 = ('d8', 'tutorials on latent structures')

    return (doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8)


def process_docs(all_docs):
    stop_words = ['on','of','and','by','for','in','by']
    all_words =[]
    counts_dict ={}
    for doc in all_docs:
        words = [x.lower() for x in doc[1].split() if x not in stop_words]
        words_counted = Counter(words)
        unique_words = list(words_counted.keys())
        counts_dict[doc[0]]=words_counted
        all_words = all_words + unique_words
    n = len(counts_dict)
    df_counts = Counter(all_words)
    compute_vector_len(counts_dict,n,df_counts)

def compute_vector_len(doc_dict,n, df_counts):
    global vector_dict
    for doc_name in doc_dict:
        doc_words = doc_dict[doc_name].keys()
        wd_tfidf_scores ={}
        for wd in list(set(doc_words)):
            wds_cts = doc_dict[doc_name]
            wd_tf_idf = wds_cts[wd] * math.log(n / df_counts[wd], 10)
            wd_tfidf_scores[wd] = round(wd_tf_idf, 4)
        vector_dict[doc_name] = wd_tfidf_scores

def get_cosine(d1, d2):
        vec1 = vector_dict[d1]
        vec2 = vector_dict[d2]
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum(vec1[x] * vec2[x] for x in intersection)
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        if not denominator:
            return 0.0
        else:
            return round(float(numerator) / denominator, 3)

def getarray(d1,d2):
    vec1 = vector_dict[d1]
    vec2 = vector_dict[d2]
    z = vec1.copy()
    z.update(vec2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    array1 = []
    array2 = []
    for x in intersection:
        array1.append(vec1[x])
        array2.append(vec2[x])
    for x in z.keys():
        if x not in intersection:
            if x in vec1:
                array1.append(vec1[x])
            else:
                array1.append(0)
        else:
            continue
    for x in z.keys():
        if x not in intersection:
            if x in vec2:
                array2.append(vec2[x])
            else:
                array2.append(0)
        else:
            continue
    return (array1,array2)

def get_cosinedistance(d1, d2):
        array1, array2 = getarray(d1, d2)
        result = nltk.cluster.util.cosine_distance(array1, array2)
        if not result:
            return 0.0
        else:
            return round(float(result),3)

def get_eclideandistance(d1,d2):
    array1, array2 = getarray(d1, d2)
    #result = nltk.cluster.util.euclidean_distance(array1, array2)
    result = scipy.spatial.distance.euclidean(array1, array2)
    if not result:
        return 0.0
    else:
        return round(float(result), 3)

#run program
all_docs = load_docs()
process_docs(all_docs)
#for keys,values in vector_dict.items(): print(keys,values)

d1='d1'
d2='d2'
d3='d3'
d4='d4'
d5='d5'
d6='d6'
d7='d7'
d8='d8'

cosine13 = (get_cosinedistance(d1,d3), get_eclideandistance(d1,d3))
cosine23 = (get_cosinedistance(d2,d3),get_eclideandistance(d2, d3))
cosine33 = (get_cosinedistance(d3,d3),get_eclideandistance(d3, d3))
cosine34 = (get_cosinedistance(d3,d4),get_eclideandistance(d4, d3))
cosine35 = (get_cosinedistance(d5,d3),get_eclideandistance(d5, d3))
cosine36 = (get_cosinedistance(d6,d3),get_eclideandistance(d6, d3))
cosine37 = (get_cosinedistance(d7,d3),get_eclideandistance(d7, d3))
cosine38 = (get_cosinedistance(d8,d3),get_eclideandistance(d8, d3))

print('cosine13', cosine13)
print('cosine23', cosine23)
print('cosine33', cosine33)
print('cosine34', cosine34)
print('cosine35', cosine35)
print('cosine36', cosine36)
print('cosine37', cosine37)
print('cosine38', cosine38)

#print(EuclieanDistance(d1,d2))

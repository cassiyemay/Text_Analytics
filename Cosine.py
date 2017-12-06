import math
from collections import Counter


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

def get_cosine(d1,d2):
    vec1 =  vector_dict[d1]
    #print(vec1)
    vec2 = vector_dict[d2]
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum(vec1[x] * vec2[x] for x in intersection)
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return round(float(numerator)/denominator, 3)




#run program
all_docs = load_docs()
process_docs(all_docs)
for keys,values in vector_dict.items(): print(keys,values)

d1='d1'
d2='d2'
d3='d3'
d4='d4'
d5='d5'
d6='d6'
d7='d7'
d8='d8'

cosine13 = get_cosine(d1, d3)
cosine12 = get_cosine(d1, d2)
cosine23 = get_cosine(d2, d3)
cosine34 = get_cosine(d3, d4)
cosine35 = get_cosine(d3, d5)
cosine36 = get_cosine(d6, d3)
cosine37 = get_cosine(d7, d3)
cosine38 = get_cosine(d8, d3)
cosine33 = get_cosine(d3, d3)
#print('cosine', cosine13,cosine23,cosine33,cosine34,cosine35,cosine36,cosine37,cosine38)



#print(EuclieanDistance(d1,d2))

import math
from collections import Counter
from pprint import pprint
import nltk
from nltk.corpus import stopwords

vector_dict = {}


def load_docs():
    doc1 = ('T1',
            'we see some mental issue, such as, physical war, physical battle and physical pain. But we feel war, feel battle and feel pain. Awareness and kindness')
    doc2 = (
    'T2', 'I want to remind you of a few things: Your mental health matters. It really matters. Not just on paper')
    doc3 = ('T3',
            'amidst the stress from Acads and life altogether, please remember to take care of your mental health. It matters on your physical feeling')
    doc4 = ('T4',
            'do not be afraid to speak out your mental health is important. Our team of mental health nurses in our emergency control rooms ensures patients receive the right support')
    doc5 = ('T5',
            'because everyone you meet is fighting some kind of battle, but some of us can never beat our enemy. Get check ups. Battle illness together')
    doc6 = ('T6',
            'never give up on someone with a mental illness and physical battle. When I is replaced with we, illness become wellness and health')
    doc7 = ('T7',
            'the strongest people are not those who show strength and health in front of us, but those who win battles we know nothing about mental')
    doc8 = ('T8',
            'mental health is just as important as physical health. You are not alone. I promise your mental health will be healthy')
    doc9 = ('T9',
            'mental illness does not equal to failure. We long for an Africa where openly suffering from mental illness is not a taboo')
    doc10 = ('T10',
             'we all have mental health. It is not only important to talk about mental health problems, but all about mental health. Illness becomes kindness')
    return [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10]


def process_docs(all_docs):
    stop = stopwords.words('english')
    all_words = []
    counts_dict = {}
    for doc in all_docs:
        words = [x.lower() for x in doc[1].split() if x not in stop]
        words_counted = Counter(words)
        unique_words = list(words_counted.keys())
        counts_dict[doc[0]] = words_counted
        all_words = all_words + unique_words
    return(counts_dict.keys())

def process_docs1(all_docs):
    stop = stopwords.words('english')
    counts_dict = {}
    for doc in all_docs:
        words = [x.lower() for x in doc[1].split() if x not in stop]
        words_counted = Counter(words)
        counts_dict[doc[0]] = words_counted
    return(counts_dict)

all_docs = load_docs()

process_docs(all_docs)
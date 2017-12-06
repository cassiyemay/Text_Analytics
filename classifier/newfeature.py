import  nltk
from nltk.corpus import names
import random



def gender_features(word):
    return {'last_3letter': word[-3:], "last_twoletters": word[-2:],'last_letter': word[-1]}

male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)
featuresets =[(gender_features(n), gender) for (n, gender) in labeled_names]

train_set, test_set = featuresets[500:], featuresets[:500]
classifier =nltk.NaiveBayesClassifier.train(train_set)
print(test_set[1])
print(test_set[1][1])
ans1 = classifier.classify(gender_features('hellen'))
#print("mark is", ans1)


number =0
for i in range(len(test_set)):
    prediction1=(classifier.classify(test_set[i][0]))
    if prediction1==test_set[i][1]:
        number +=1
print(number)
print(number/len(test_set))





count=0
for name in names.words('male.txt'):
    prediction = classifier.classify(gender_features(name))
    if prediction=='male':
        count +=1
print(count/len(male_names))

sum=0
for name in names.words('female.txt'):
    prediction = classifier.classify(gender_features(name))
    if prediction=='female':
        sum +=1
print(sum/len(female_names))
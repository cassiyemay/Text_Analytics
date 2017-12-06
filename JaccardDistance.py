import array

def JaccardDistance(str1,str2):
    set1=set(str1.split())
    set2=set(str2.split())
    ans = 1-(float(len(set1&set2))/len(set1 | set2))
    return round(ans,2)

entity1="tree flower sun warm green"
entity2 ="tree flower sun hot green"
entity3 ="tree leaves yellow cold sun"
entity4 ="tree snow white cold cloud"
entity5 ="tree family holiday red travel"
entity6 ="tree open school warm happy"

array = [entity1,entity2,entity3,entity4,entity5,entity6]

for i in range(len(array)):
    for j in range(i):
        print(array[i]+ " , "+ array[j] +". " +" jaccard distance is ",JaccardDistance(array[i],array[j]))
        #print(JaccardDistance(array[i],array[j]))



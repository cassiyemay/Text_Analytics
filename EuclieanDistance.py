from math import *

def euclidean_distance(x, y):

    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def EuclieanDistance(d1,d2):
    vec1 = vector_dict[d1]
    vec2 = vector_dict[d2]
    sum1 = sum([(x-y) ** 2 for x,y in zip(vec1.keys(),vec2.keys())])

    denominator = math.sqrt(sum1)
    if not denominator:
        return 0.0
    else:
        return round(float(denominator), 3)

print(euclidean_distance([0, 3, 4, 5], [7, 6, 3, -1]))
aa([0, 3, 4, 5], [7, 6, 3, -1])
from numpy import *
import numpy as np



def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        currLine = line.strip().split('\t')
        fltLine = map(float, currLine)
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for ii in range(n):
        minI = min(dataSet[:, ii])
        rangeI = float(max(dataSet[:, ii]) - minI)
        centroids[:, ii] = minI + rangeI * random.random(size=(k, 1))
    return centroids


### k-Means
def kMeans(dataSet, k, distMeas=distEclud, createRandCent=randCent):
    N = shape(dataSet)[0]
    clusterAssment = mat(zeros((N, 2)))
    centroids = createRandCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for ii in range(N):
            minDist = inf
            minIndex = -1
            for jj in range(k):
                distIJ = distMeas(centroids[jj, :], dataSet[ii, :])
                if distIJ < minDist:
                    minDist = distIJ
                    minIndex = jj
            if clusterAssment[ii, 0] != minIndex:
                clusterChanged = True
            clusterAssment[ii, :] = minIndex, minDist ** 2
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


### bisecting K-means
def biKmeans(dataSet, k, distMeas=distEclud):
    N = shape(dataSet)[0]
    clusterAssment = mat(zeros((N, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for ii in range(N):
        clusterAssment[ii, 1] = distMeas(mat(centroid0), dataSet[ii, :]) ** 2
    while (len(centList) < k):
        lowestSSE = inf
        for ii in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == ii)[0], :]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != ii)[0], 1])
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = ii
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        centList[bestCentToSplit] = bestNewCents[0, :]
        centList.append(bestNewCents[1, :])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClustAss
    return mat(centList), clusterAssment

dataset= np.array([[ 0.51446854, 0.70749231],
 [-0.5994926,  -0.5727201 ],
 [-0.21925828, -0.78560147],
 [-0.68937981,  0.69070765],
 [-0.62328728,  0.68192915],
 [-0.9323087,  -0.68863296],
 [-0.02477332, -0.27217904],
 [-0.34889671,  0.74373414],
 [ 0.54421903, -0.48559475],
 [-0.48584462,  0.25578632],
 [-0.88470734,  0.02081867],
 [-0.52069142,  0.3028937 ],
 [-0.86176655,  0.99509493],
 [-0.03208361, -0.08276554],
 [-0.75269005,  0.6257051 ]])

print(randCent(dataset,3))
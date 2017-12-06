import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1,1), random.uniform(-1,1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters = {}
    for x in X:
        #print(enumerate(mu))
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                for i in enumerate(mu)], key=lambda t:t[1])[0]

        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis=0))
    return newmu

def has_converged(mu, oldmu):
    print(set([tuple(a) for a in mu]))
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X,K):
    oldmu = random. sample(X,K)
    mu = random.sample(X,K)
    #print(mu)
    while not has_converged(mu,oldmu):
        oldmu = mu
        clusters = cluster_points(X,mu)
        mu = reevaluate_centers(oldmu, clusters)
    return (mu, clusters)

def find_newcenters(X,K):
    oldmu = X[:3]
    mu = X[4:7]
    while not has_converged(mu, oldmu):
        oldmu = mu
        clusters = cluster_points(X, mu)
        mu = reevaluate_centers(oldmu, clusters)
    return (mu, clusters)


def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0],points1[1], 'ro')
    points2= change_coords(clusters[1])
    plt.plot(points2[0],points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1],'kx')
    plt.axis([-1.0,1,-1.0,1])
    plt.show()

data = init_board(15)
#print(data)
data1 = np.array([[ 0.51446854, 0.70749231],
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

data2 = np.array([[ -0.75, -0.75], [ -0.8,  -0.8], [ -0.75, -0.80], [-0.950, -0.950],
                  [ -0.69491566, -0.55169583],  [-0.019,  -0.219],[ -0.177, -0.044],
                  [0.171,  0.132], [-0.25, -0.25], [0.20, 0.20], [0.750, 0.650],
                  [ 0.65, 0.65 ],  [0.70,  0.80] ,[ 0.90, 0.80], [ 0.60, 0.90]])

#out = find_centers(list(data1), 3)
#find_centers(list(data), 3)

out = find_newcenters(list(data1), 3)
plt.title('5')
parse_output(out)





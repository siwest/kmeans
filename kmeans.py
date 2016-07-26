import sys
import math
import random


def readData(data):
    f1 = open(data)
    data = []
    line1 = f1.readline()
    i = 0
    while (line1 != ''):
        splitLine = line1.split()
        tempLine = []
        for j in range(0, len(splitLine), 1):
            tempLine.append(int(splitLine[j]))
        data.append(tempLine)
        line1 = f1.readline()
    f1.close()
    print "Input Data Set: ", data
    return data


'''Initialize centroids (means) with a randomly selected datapoint from current data set'''
def init_centroids(data, k):
    centroids = []
    tempData = list(data)
    for i in range(0, k, 1):
        centroids.append(tempData.pop(random.randint(0, len(tempData) - 1)))
    print "Initialized centroids: ", centroids
    return centroids

''' Assign data points to a cluster '''
def assignCluster(centroids, data):
    clusters = [ list() for centroid in centroids]
    distances = [0] * len(centroids)

    for i in range(0, len(data), 1):  # for each row
        d = [0] * len(centroids)
        for k in range(0, len(centroids), 1):  # calculate data point distance to each centroid
            for j in range(0, len(data[0]), 1):  # for each col
                # print "d[" + str(k) + "] is " + str(d[k])
                # print "centroids[" + str(k) + "] is " + str(centroids[k][j])
                # print "data[" + str(i) + "][" + str(j) + "] is " + str(data[i][j])
                # print "-----------------------"

                d[k] = d[k] + (centroids[k][j] - data[i][j]) ** 2  # Euclidean distance

        for m in range(0, len(centroids), 1):
            d[m] = math.sqrt(d[m])

        # Assign cluster based on minDist
        minDist = min(d)
        #print "mindist is ", minDist
        
        for n in range(0, len(centroids), 1):
            if (minDist == d[n]):
                clusters[n].append(data[i])

    for p in range(0, len(clusters), 1):
        print "Cluster " + str(p) + " is: " + str(clusters[p])

    return clusters


''' Compute new centroids '''
def moveCentroids(clusters, k):
    centroids = []
    
    for i in range(0, k, 1): # for each cluster
        tempClusters = clusters[i]
    	tempMeans = []
        for j in range(0, len(tempClusters[0]), 1):  # for each col of tempCluster
            temp = 0
            for m in range(0, len(tempClusters), 1):  # for each row of tempCluster
                temp = temp + tempClusters[m][j]
            tempMeans.append(temp / len(tempClusters))
        centroids.append(tempMeans)
        print "Centroid" + str(i) + " is: " + str(centroids[i])
    return centroids


def predict(centroids, data, k, loopCount):
    for i in range(0, loopCount, 1): 
    	print "----------------------"
        clusters = assignCluster(centroids, data)
        centroids = moveCentroids(clusters, k)
    return

def main(data):
    k = 2
    dataList = readData(data)
    centroids = init_centroids(dataList, k)
    predict(centroids, dataList, k, 3)


if __name__ == '__main__':
    data = sys.argv[1]
    main(data)

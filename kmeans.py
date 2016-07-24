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
    print data
    return data


'''Initialize centroids (means) with a randomly selected datapoint from current data set'''
def init_centroids(data, k):
    centroids = [0] * k
	
	# ensures unique, random rows/data points are chosen for initialization
    random_rows = [0] * k
    prev = -1
    for i in range(0, k, 1):
        random_rows[i] = int(len(data) * random.random())
        while prev == random_rows[i]:  
        	random_rows[i] = int(len(data) * random.random())
    	prev = random_rows[i]

    for i in range(0, len(random_rows), 1):
        r = random_rows[i]
        for j in range(0, len(data[0]), 1):
            centroids[i] = centroids[i] + data[r][j]
        centroids[i] = centroids[i] / (len(data[0]))

    return centroids

''' Assign data points to a cluster '''
def assignCluster(centroids, data):
    clusters = [[]] * len(centroids)
    distances = [0] * len(centroids)
    templist1 = []
    templist2 = []

    for i in range(0, len(data), 1):  # for each row
        d = [0] * len(centroids)
        for k in range(0, len(centroids), 1):  # calculate data point distance to each centroid
            for j in range(0, len(data[0]), 1):  # for each col
                # print "d[" + str(k) + "] is " + str(d[k])
                # print "centroids[" + str(k) + "] is " + str(centroids[k])
                # print "data[" + str(i) + "][" + str(j) + "] is " + str(data[i][j])
                # print "-----------------------"
                d[k] = d[k] + (centroids[k] - data[i][j]) ** 2  # Euclidean distance

        for m in range(0, len(centroids), 1):
            d[m] = math.sqrt(d[m])
            #print "distance is ", d[m]

        # Assign cluster based on minDist
        minDist = min(d)
        #print "mindist is ", minDist
        
        for n in range(0, len(centroids), 1):
            if (minDist == d[n]):
                #clusters[n].append(data[i])
                #print "d[" + str(n) + "] " + str(data[i])
                if (n == 0):
                	templist1.append(data[i])
                if (n == 1):
                	templist2.append(data[i])
    clusters[0] = templist1
    clusters[1] = templist2

    for p in range(0, len(clusters), 1):
        print "Cluster " + str(p) + " is " + str(clusters[p])

    return clusters


''' Compute new centroids '''
def moveCentroids(clusters, centroids):
    for i in range(0, len(centroids), 1): # for each cluster
    	tempCluster = clusters[i]
        
        for j in range(0, len(clusters[i]), 1): # for each elem in cluster
        	temp = 0
        	for m in range (0, len(tempCluster), 1):
        		for n in range (0, len(tempCluster[0]), 1):
        			temp += tempCluster[m][n]
        temp = float(temp / (len(tempCluster) * 2))
        centroids[i] = temp
        print "Centroid" + str(i) + " is " + str(centroids[i])
    return centroids


def predict(centroids, data, loopCount):
    current_clusters = 0  # this is just for initialization
    for i in range(0, loopCount, 1): 
    	print "----------------------"
        clusters = assignCluster(centroids, data)
        current_clusters = clusters
        centroids = moveCentroids(clusters, centroids)
    return

def main(data):
    dataList = readData(data)
    cols = len(dataList[0])
    centroids = init_centroids(dataList, 2)
    print "Initialized centroids ", centroids
    predict(centroids, dataList, 3)


if __name__ == '__main__':
    data = sys.argv[1]
    main(data)

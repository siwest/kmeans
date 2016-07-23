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

def initCentroids(data, k):
	centroids = [0] * k
	randomRows = [0] * k

	for i in range (0, k, 1):
		randomRows[i] = int(len(data) * random.random())

	for i in range (0, len(randomRows), 1):
		r = randomRows[i]
		#print "centroids initialized from row ", r
		for j in range (0, len(data[0]), 1):
			centroids[i] = centroids[i] + data[r][j]
		centroids[i] = centroids[i] / (len(data[0]))
	return centroids


def assignCluster(centroids, data):
	clusters = [0] * len(centroids)
	distances = [0] * len(centroids)

	for i in range (0, len(data), 1): #for each row
		d = [0] * len(centroids)
		for k in range (0, len(centroids), 1):  # calculate data point distance to each centroid
			for j in range (0, len(data[0]), 1): # for each col
				#print "d[" + str(k) + "] is " + str(d[k])
				#print "centroids[" + str(k) + "] is " + str(centroids[k])
				#print "data[" + str(i) + "][" + str(j) + "] is " + str(data[i][j])
				#print "-----------------------"
				d[k] = d[k] + (centroids[k] - data[i][j])**2  # Euclidean distance
	
		for m in range (0, len(centroids), 1): 
			d[m] = math.sqrt(d[m])
		

		# Assign cluster based on minDist
		minDist = min(d) 
		for n in range (0, len(centroids), 1): 
			if (minDist == d[n]):
				if (clusters[n] == 0):
					clusters[n] = list(data[i])
				else:
					clusters[n].append(data[i])
		
	print "Current cluster assignment ", clusters
	return clusters


# Compute new centroids
def moveCentroids(clusters, centroids):
	temp = 0
	for i in range(0, len(centroids), 1):
		for j in range(0, len(clusters[i]), 1):  
			centroids[i] = temp + clusters[i][j]
			temp = centroids[i]
		centroids[i] = centroids[i] / (len(clusters[i])) 
		#print "Centroid" + str(i) + " is " + centroids[i]
		#print centroids
	return centroids

def predict(centroids, data):
	currentClusters = 0 # this is just for initialization
	for i in range(0, 1, 1):
		clusters = assignCluster(centroids, data)
		currentClusters = clusters
		centroids = moveCentroids(clusters, centroids)

	print "Final cluster assignment: ", clusters


def main(data):
    dataList = readData(data)
    cols = len(dataList[0])
    centroids = initCentroids(dataList, 2)
    print "Initialized centroids ", centroids
   # means = computeInitialMeans(dataList, cols, centroids)
    #print "here ", means
    predict (centroids, dataList)

if __name__ == '__main__':
    data = sys.argv[1]
    main(data)
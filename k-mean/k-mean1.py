import sys 
import math

def read_file():
	cnt_train = 0
	f = open(file_test,"r")
	while (True):
		line = f.readline().split()
		if not line:
			break
		x,y,z = line[0].split("<fff>")
		label_train.append(x) 
		ID,tf_idf = z.split(":")
		vec = {}
		vec[ID] = float(tf_idf)
		for x in line[1:]:
			ID,tf_idf = x.split(":")
			vec[ID] = float(tf_idf)
		data_train.append(vec)
		cnt_train +=1
	f.close()
	return cnt_train

def read_centroids(number_clusters,maxx):
	centroids = []
	f = open(file_centroids,"r")
	while (True):
		line = f.readline()
		if not line:
			break
		temp = [float(0) for i in range(maxx+1)]
		for i in data_train[int(line)]:
			x = int(i)
			temp[x] = data_train[int(line)][i]
		centroids.append(temp)
	f.close()
	return centroids

def distance(p1,centroid):
	sum = 0
	for ID,tf_idf1 in p1.items():
		sum += tf_idf1*centroid[int(ID)]
	return sum

def classify(centroids,point,):   
    maxxx = float(-9999999999)
    index = -1; 
    for i in range(len(centroids)): 
        dis = distance(point, centroids[i])
        if (dis > maxxx): 
            maxxx = dis
            index = i
    return index


def UpdateMean(next_centroid,point): 
    for ID,tf_idf in point.items():
    	next_centroid[int(ID)] += tf_idf
    return next_centroid

def train_kmean(centroids,max_train):
	belongsto = [0 for i in range(len(data_train))]
	next_centroids = []
	pre_cluster_sizes = [float(0) for i in range(len(centroids))]
	for i in range(number_clusters):
		next_centroids.append([0 for j in range(maxx + 1)]) 
	for e in range(max_train):
		change = False
		cluster_sizes = [0 for i in range(len(centroids))]
		for x,i in enumerate(data_train):
			index = classify(centroids,i)
			cluster_sizes[index] += 1
			next_centroids[index] = UpdateMean(next_centroids[index],i)
			if(index != belongsto[x]):
				change = True
			belongsto[x] = index
		if(change == False):
			break
		# print(cluster_sizes)
		# exit(0)
		for x,i in enumerate(centroids):
			for j in range(len(next_centroids[x])):
				if(cluster_sizes[x] != 0):
					i[j] = float(next_centroids[x][j])/cluster_sizes[x]
				next_centroids[x][j] = 0
		print(cluster_sizes)



def find_clusters(centroids):
	clusters = [[] for i in range(len(centroids))]
	for x,i in enumerate(data_train):
		index = classify(centroids,i)
		clusters[index].append(x)
	f = open("clusters.txt","w")
	for x,i in enumerate(clusters):
		f.write(str(x))
		f.write("***\n")
		for j in i:
			y = str(j)
			y = y + str(" ") + str(label_train[j])
			f.write(y)
			f.write("\n")


#file name
file_train = "train_tf_idf.txt"
file_test = "test_tf_idf.txt"
file_words = "words_idfs.txt"
file_centroids = "centroids.txt"

#train
label_train = []
data_train = []

number_clusters = 20
maxx = 10290

cnt_train = read_file()
print(len(label_train))
centroids = read_centroids(number_clusters,maxx)
print("read_centroids")
train_kmean(centroids,300)
print("train_kmean")
find_clusters(centroids)
print("find_clusters")

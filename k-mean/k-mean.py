import sys 

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

def distance(p1,p2):
	sum = 0
	tf_idf1 = float(0)
	tf_idf2 = float(0)
	for ID,tf_idf1 in p1.items():
		tf_idf2 = p2.get(ID,float(0))
		sum += (tf_idf2-tf_idf1)**2
	for ID,tf_idf2 in p2.items():
		tf_idf1 = p1.get(ID,float(0))
		if(tf_idf1 == 0):
			sum += tf_idf2**2
	return sum

def read_centroids():
	centroids = []
	f = open(file_centroids,"r")
	while (True):
		line = f.readline()
		if not line:
			break
		centroids.append(data_train[int(line)])
	f.close()
	return centroids

def classify(centroids,point):   
    minn = sys.float_info.max; 
    index = -1; 
    for i in range(len(centroids)): 
        dis = distance(point, centroids[i]); 
        if (dis < minn): 
            minn = dis; 
            index = i; 
    return index; 


def UpdateMean(mean,n,point): 
    for i in mean: 
        m = mean[i]; 
        k = point.get(i,float(0))
        m = (m*(n-1)+k)/float(n); 
        mean[i] = m
    for i in point:
    	k = mean.get(i,0)
    	if(k == 0):
    		mean[i] = point[i]*(float(n-1)/float(n))
    return mean;

def train_kmean(centroids,max_train):
	cluster_sizes = [0 for i in range(len(centroids))]
	belongsto = [0 for i in range(len(data_train))]
	for e in range(max_train):
		change = False
		for x,i in enumerate(data_train):
			index = classify(centroids,i)
			cluster_sizes[index] += 1
			centroids[index] = UpdateMean(centroids[index],cluster_sizes[index],i)
			if(index != belongsto[x]):
				change = True
			belongsto[x] = index
		if(change == False):
			break

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
			f.write(str(label_train[j]))
			f.write("\n")


#file name
file_train = "train_tf_idf.txt"
file_test = "test.txt"
file_words = "words_idfs.txt"
file_centroids = "centroids.txt"

#train
label_train = []
data_train = []

cnt_train = read_file()
print(len(label_train))
centroids = read_centroids()
print("read_centroids")
train_kmean(centroids,1000)
print(centroids[0])
print("train_kmean")
find_clusters(centroids)
print("find_clusters")

import sys 
from random import randint


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
	for ID,tf_idf1 in p1.items():
		sum += tf_idf1*p2.get(ID,float(0))
	return sum

def find_centroids():
	centroids = []
	centroids.append(0)
	for c_cnt in range(19):
		point = 0
		minn = sys.float_info.max
		for x,i in enumerate(data_train):
			d = -999999
			for j in centroids:
				temp = distance(i,data_train[j])
				d = max(d,temp)
			if(d < minn):
				minn = d
				point = x
		centroids.append(point)
		print(point, end = " ")
		print(label_train[point])
	return centroids

#file name
file_train = "train_tf_idf.txt"
file_test = "test_tf_idf.txt"
file_words = "words_idfs.txt"

#train
label_train = []
data_train = []

cnt_train = read_file()
print(len(label_train))
centroids = find_centroids()
f = open("centroids.txt","w")
for i in centroids:
	print(str(i))
	f.write(str(i))
	f.write("\n")
f.close()
#train_kmean(centroids,100)

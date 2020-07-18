import sys 

def read_file():
	set_data = []
	cnt_train = 0
	f = open(file_train,"r")
	while (True):
		line = f.readline().split()
		if not line:
			break
		x,y,z = line[0].split("<fff>")
		label_train.append(x) 
		ID,tf_idf = z.split(":")
		vec = {}
		vec[ID] = float(tf_idf)
		set_data.append(ID)
		for x in line[1:]:
			ID,tf_idf = x.split(":")
			vec[ID] = float(tf_idf)
			set_data.append(ID)
		data_train.append(vec)
		cnt_train +=1
	f.close()
	set_data = set(set_data)
	print(len(set_data))
	return cnt_train


#file name
file_train = "train_tf_idf.txt"
file_test = "test_tf_idf.txt"
file_words = "words_idfs.txt"
file_centroids = "centroids.txt"

#train
label_train = []
data_train = []

cnt_train = read_file()
print(cnt_train)

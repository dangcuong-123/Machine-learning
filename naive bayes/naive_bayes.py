import numpy as np

def read_file(file_name):
	set_ID = []
	dict_ID = {}
	f = open(file_name,"r")
	while (True):
		line = f.readline().split()
		if not line:
			break
		for x in line[1:]:
			set_ID.append(x)
	f.close()
	set_ID = set(set_ID)
	for x,ID in enumerate(set_ID):
		dict_ID[ID] = x
	return set_ID,dict_ID

def pre_process(file_name,set_ID,dict_ID):
	f = open(file_name,"r")
	P = [0,0,0,0,0]
	cnt_ID = np.zeros((len(set_ID),5))
	while (True):
		line = f.readline().split()
		if not line:
			break
		for i in range(0,5):
			if(class_[i] == line[0]):
				P[i] += 1
				for x in line[1:]:
					cnt_ID[dict_ID[x]][i] += 1
	return P,cnt_ID

def smoothing(a,b):
	return float((float(a+1))/(float(b+1)))

def train(P,cnt_ID,set_ID):
	P_class = [0,0,0,0,0]
	naive_bayes = np.zeros((len(set_ID),5))
	total = sum(P)
	for i in range(0,5):
		P_class[i] = np.log(smoothing(P[i],total))
	for i in range(0,len(set_ID)):
		for j in range(0,5):
			naive_bayes[i][j] += np.log(smoothing(cnt_ID[i][j],P[j]))
	return P_class,naive_bayes

def SCORE(file_name_test,P_class,naive_bayes,dict_ID):
	f = open(file_name_test,"r")
	total_test = 0
	res = 0
	while True:
		line = f.readline().split()
		if not line:
			break
		total_test += 1
		predict = np.zeros(5)
		for i in range(0,5):
			predict[i] = P_class[i]
		for i in line[1:]:
			if (i in set_ID):
				for j in range(0,5):
					predict[j] += naive_bayes[dict_ID[i]][j]
		maxx = max(predict)
		for i in range(0,5):
			if(maxx == predict[i] and class_[i] == line[0]):
				res += 1
	print(res)
	print(total_test)
	return float(float(res)/float(total_test))*100.0


#main
file_name_train = "agedetector_group_train.v1.0.txt"
file_name_test = "test.txt"
class_ = ["__label__18-24","__label__25-34","__label__35-44","__label__45-54","__label__55+"]

set_ID,dict_ID = read_file(file_name_train)
print("read_file")
P,cnt_ID = pre_process(file_name_train,set_ID,dict_ID)
print("pre_process")
P_class,naive_bayes = train(P,cnt_ID,set_ID)
print("train")
score = SCORE(file_name_test,P_class,naive_bayes,dict_ID)
print score
print("SCORE")



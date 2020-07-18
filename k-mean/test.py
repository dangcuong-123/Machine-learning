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
def print_test():
    f1 = open("test.txt","w")
    f = open(file_test,"r")
    d = 0
    i = 0
    sl = 0
    while (True):
        line = f.readline()
        if not line:
            break
        if(i >= 20):
            break
        if(label_train[d] == label_test[i]):
            if(sl < 10):
                f1.write(line)
                sl += 1
            else :
                sl = 0
                i += 1
        d+=1
    f1.close()
    f.close()

#file name
file_train = "train_tf_idf.txt"
file_test = "test_tf_idf.txt"
file_words = "words_idfs.txt"
file_centroids = "centroids.txt"

#train
label_train = []
data_train = []
label_test = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]

cnt_train = read_file()
print(len(label_train))
print_test()



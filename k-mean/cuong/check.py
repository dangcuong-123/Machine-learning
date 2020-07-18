
def full(k):
	for i in range(20):
		l[i][k] = 0

def read_file():
	l = []
	file_name = "clusters.txt"
	for i in range(20):
		l.append([0 for i in range(21)])
	f = open(file_name,"r")
	i = -1
	while (True):
		line = f.readline()
		if not line:
			break
		if(line[len(line)-2] == '*'):
			i+=1
			continue
		x,y = line.split()
		l[i][int(y)] += 1
	f.close()
	return l



check = [0 for i in range(21)]
clusters = [-1 for i in range(20)]
l = read_file()
d = 0
for i in range(20):
	maxx = 0
	for j in range(20):
		maxx = max(maxx,max(l[i]))
	for j in range(20):
		if(maxx == max(l[i])):
			for k in range(1,21):
				if(l[i][k] == maxx):
					if(check[k] == 0 and clusters[i] == -1):
						full(k)
						clusters[i] = k
						check[k] = 1
						d+=1
	if(d >= 20):
		break
for i in range(len(clusters)):
	if(clusters[i] == -1):
		for j in range(20):
			if(check[j] == 0):
				clusters[i] = j
				check[j] = 1
				break
l = read_file()
s = 0
for i in range(len(clusters)):
	s += l[i][clusters[i]]
print(s/float(7532)*100)
print(clusters)


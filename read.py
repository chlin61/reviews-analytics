data=[]
line_len=0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		line_len += len(line)
print('平均長度為:',float(line_len)/len(data))

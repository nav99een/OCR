import os
import pandas as pd

base_path = os.getcwd()
input_path = os.path.sep.join([base_path,'dd.txt'])

f = open(input_path,'r')

a = []

for line in f:
	line = line.rstrip().split()
	a.append(line)

a = pd.DataFrame(a)

b = dict()

for i in range(len(a.iloc[0,:])):
	b[a.iloc[0,i]] = i
#print(b)

c = []
act = ['1D','Year','Region','Revenue']
for i in range(len(act)):
	if act[i] in b:
		c.append(a.iloc[:,b[act[i]]].values)
		#print(a.iloc[:,b[act[i]]].values)
	else :
		c.append([act[i]])

d = pd.DataFrame(c)

d = d.transpose()
d.to_excel('new.xlsx',header=False,index=False)


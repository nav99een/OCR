from PIL import Image
from pytesseract import image_to_string
import os 
import cv2
import imutils
import os
import pandas as pd

base_path = os.getcwd()

input_path = os.path.sep.join([base_path,'images'])

out_path = os.path.sep.join([base_path,'output'])

for item in os.listdir(input_path):
	img_path = os.path.sep.join([input_path,item])

	print('Loading image:',item)

	image = Image.open(img_path)

	output = image_to_string(image.convert('RGB'), lang='eng',config='--psm 6')
	
	#print('Loading data from', item,'image')
	
	outfilename = out_path+'/'+item.split('.')[0]+'.txt'
	with open(outfilename,'+w') as s:
			s.write(output)
	dd = []
	for line in open(outfilename):

		data = line.rstrip().split()
		
		dd.append(data)
		
	df = pd.DataFrame(dd)

	df.to_excel(out_path+'/'+item.split('.')[0]+'.xlsx')'''



	f = open(outfilename,'r')

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
	act = ['ID','Year','Region','Revenue']
	for i in range(len(act)):
		if act[i] in b:
			c.append(a.iloc[:,b[act[i]]].values)
			#print(a.iloc[:,b[act[i]]].values)
		else :
			c.append([act[i]])

	d = pd.DataFrame(c)

	d = d.transpose()

	d.to_excel(out_path+'/'+item.split('.')[0]+'.xlsx',header=False,index=False)'''

	print("Successfully converted into excel file")

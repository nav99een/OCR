#loading the necessary modules
from PIL import Image
from pytesseract import image_to_string
import os 
import cv2
import imutils
import os
import pandas as pd
from pdf2image import convert_from_path


#defining paths for workflow
base_path = os.getcwd()

#input file path
input_path = os.path.sep.join([base_path,'test'])

#path to the output file
out_path = os.path.sep.join([base_path,'output'])

save_dir = os.path.sep.join([base_path,'save'])



def extract_data(image):
	text = image_to_string(image, lang='eng',config='--psm 6')
	return text



def image2text(text,outputpath):

	with open(outputpath+'.txt','+w') as s:
				s.write(text)



def image2docx(text,outputpath):

	with open(outputpath,'+w') as s:
				s.write(text)



def image2excel(filename):

	dd = []
	for line in open(filename+'.txt'):

		data = line.rstrip().split()
		
		dd.append(data)
		
	df = pd.DataFrame(dd)

	df.to_excel(out_path+'/'+item.split('.')[0]+'.xlsx',header=False,index = False)



def pdf2text(path):

	pages = convert_from_path(path, 500)
	j = 0
	direc = save_dir

	for page in pages:
		filename = os.path.sep.join([direc,item.split('.')[0]+str(j)+".jpg"])
		page.save(filename, 'JPEG')
		j+=1

	for img in os.listdir(direc):
		img_path = os.path.sep.join([direc,img])

		image = preprocess_image(img_path)

		output = extract_data(image)

		outfilename = os.path.sep.join([out_path,img.split('.')[0]])

		image2text(output,outfilename)
		try :
			temp1 = int(input("Docx : 1\nExcel : 2\nText(default) : 0\nEnter output file type: ").strip())
		except ValueError :
			temp1 = 0

		if temp1 == 1:
			outfilename+='.docx'
			image2docx(output,outfilename)
			print("Successfully saved into docx file")
			os.remove(outfilename.replace('.docx','.txt'))

		elif temp1==2:
			image2excel(outfilename)
			print("Successfully saved into excel file")
			os.remove(outfilename+'.txt')

		else :
			print("Successfully saved into text file")
		
	


def preprocess_image(img_path):
	image = cv2.imread(img_path)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	'''try :
		temp = int(input("Do you want to pre-process the image ?\nThreshold : 1\nGrey : 2\nNone(default) : 0\nEnter your choice : ").strip())
	except ValueError :
		temp = 0'''
	temp = 0
	# If user enter 1, Process Threshold
	if temp == "1":
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif temp == "2":
		gray = cv2.medianBlur(gray, 3)

	return gray
	


if __name__=='__main__':
	for item in os.listdir(input_path):
		
		if item.split('.')[-1] == 'pdf':
			pdf_path = os.path.sep.join([input_path,item])
			pdf2text(pdf_path)
			continue
			
		elif item.split('.')[-1]!='pdf':

			#creating path to the image
			img_path = os.path.sep.join([input_path,item])

		print('Loading image:',item)
		image = preprocess_image(img_path)
		output = extract_data(image)
		
		try :
			temp1 = int(input("Docx : 1\nExcel : 2\nText(default) : 0\nEnter output file type: ").strip())
		except ValueError :
			temp1 = 0

		outfilename = out_path+'/'+item.split('.')[0]

		image2text(output,outfilename)

		if temp1 == 1:
			outfilename+='.docx'
			image2docx(output,outfilename)
			print("Successfully saved into docx file")
			os.remove(outfilename.replace('.docx','.txt'))

		elif temp1==2:
			image2excel(outfilename)
			print("Successfully saved into excel file")
			os.remove(outfilename+'.txt')

		else :
			print("Successfully saved into text file")


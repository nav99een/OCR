# OCR

Optical character recognition or optical character reader (OCR) is the mechanical or electronic conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo. 

OCR engines have been developed into many kinds of domain-specific OCR applications, such as receipt OCR, invoice OCR, check OCR, legal billing document OCR.

They can be used for:

1). Data entry for business documents, e.g. check, passport, invoice, bank statement, and receipt

2). Automatic number plate recognition

3). In airports, for passport recognition and information extraction

4). Automatic insurance documents key information extraction

5). Extracting business card information into a contact list.

6). More quickly make textual versions of printed documents, e.g. book scanning for Project Gutenberg

7). Make electronic images of printed documents searchable, e.g. Google Books

8). Converting handwriting in real time to control a computer (pen computing) and other many more.


I have written a script in python using "pytesseract" module which is python based wrapper of tesseract-OCR(open source).
This can extract text from any type of file like image(.jpg,.jpeg,.png,etc.) and pdf. And the extracted text could be saved into 3 different type files like .docx, .xlsx and .txt


Run run.py script and see the magic...!!!

It will convert your image data into editable data and you can save it into  diiferent formats according to your choice and text format is default.

There are three directories which are as follows:
1.) test_data :- which stores input image or pdf.

2.) save_data :- it stores image type of pdf pages seperately.

3.) output_data :- it stores the outputs of the input images


This works very fine and it is highly accurate on images which contains paragraphs or well spaced words in image. If there is any table type structure in image then the iamge should be clear.

For more information please refer to these links: https://github.com/tesseract-ocr/tesseract
https://pypi.org/project/pytesseract/





import pytesseract
import cv2
from PIL import Image
import os
import argparse

print("we made it")

def image_to_text(image_text, preprocess):
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--image", required=True, 
	# 	help="path to input image to be OCR'd")
	# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	# 	help="type of preprocessing to be done")
	# args = vars(ap.parse_args())

	image = cv2.imread(image_text)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	if preprocess == "thresh":
		gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	text = pytesseract.image_to_string(gray)

	os.remove(filename)
	# print(text)

	# show the output images
	cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	
	return text

def dic_pic(text):
	words = {}
	i = 0
	last = 0
	word = ''
	while i<len(text):
		if text[i] == ' ' or text[i] == '\n':
			word = text[last:i]
			last = i+1
			if word not in words:
				words[word] = 1
			else:
				words[word] += 1
		i+=1
	print(words)
	return words

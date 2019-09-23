# EyeRead
HackMIT 2019 Submission - Education Track

EyeRead promotes children's literacy. The program uses a webcam to identify words on a page, so when a child comes across an unfamiliar word, he/she can select it and the word will be read outloud. 

OpenCV is used to record a live feed of the pages someone is reading. The filtered frames are then sent through an image to text conversion using Pytesseract that identifies the words in the image, and the words are then converted to speech using Google Cloud's machine learning API and the natural sounding voice is played outloud

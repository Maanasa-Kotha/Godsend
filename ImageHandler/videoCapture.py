import cv2
import pytesseract

cap = cv2.VideoCapture(0)

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

count = 0
frameNum = 0
refDic = None
tempText = None
print('start recording')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if count % 2 == 0:

        # Check if current img is different than reference image and set new reference image if it is
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        tempText = pytesseract.image_to_string(gray)

        different = compare(refDic, tempText):
        if refText == None or different: #If there is a reference image and there is a difference
            print("Next Page")
            refDic = dicPic(tempText)  

        # Display the resulting frame
        cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
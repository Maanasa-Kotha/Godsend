import cv2
import pytesseract
from comparorator import compare
from opencvim import image_to_text, dic_pic

cap = cv2.VideoCapture(4)

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

cap.set(28, 125)

count = 0
frameNum = 0
print('start recording')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if count % 10 == 0:
        cv2.imwrite("../images/videoFrames/frame" + str(frameNum%5) + ".png", frame)     # save frame as JPEG file
        frameNum += 1

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        tempText = pytesseract.image_to_string(gray)

        if refDic == None:
            refDic = dic_pic(tempText)  
        else:
            different = compare(refDic, tempText)
            if different: #If there is a reference image and there is a difference
                print("Next Page")
                refDic = dic_pic(tempText)  
            else:
                print("stable")
        # Display the resulting frame
        cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
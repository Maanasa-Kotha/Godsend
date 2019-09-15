from TexttoSpeech.textspc import text_to_speech
from ImageHandler.opencvim import image_to_text, dic_pic

# image_text = "images/poster.png"
# text = image_to_text(image_text, "thresh")
# text_to_speech(text)

import cv2
import pytesseract
import threading 
# from ImageHandler.comparorator import compare


cap = cv2.VideoCapture(0)
if cap != None:
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
        if count % 1 == 0:
            cv2.imwrite("../images/videoFrames/frame" + str(frameNum%5) + ".png", frame)     # save frame as JPEG file
            frameNum += 1

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            #edged = cv2.Canny(gray, 20, 200)
            # contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # #print(contours)
            # threshold_area = 10000
            # min_area = 100000
            # for cnt in contours:
            #     area = cv2.contourArea(cnt)
            #    # rect = cv2.minAreaRect(cnt)
            #     #(x,y,w,h) = cv2.boundingRect(cnt)
            #     # frame = frame[y:y+100, x-100:x+100]
            #     #min_x, max_x = min(x, min_x), max(x+w, max_x)
            #     #min_y, max_y = min(y, min_y), max(y+h, max_y)

            #     if area > threshold_area:
            #         if area < min_area:
            #             cv2.drawContours(frame, cnt, -1, (0,255,0), 3)
            #         #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)



            tempText = pytesseract.image_to_string(gray)
            # if refDic == None:
            #     refDic = dic_pic(tempText)  
            # else:
            #     different = compare(refDic, tempText)
            #     if different: #If there is a reference image and there is a difference
            #         print("Next Page")
            #         refDic = dic_pic(tempText)  
            #     else:
            #         print("stable")
            # Display the resulting frame
            #cv2.imshow('frame', frame)
            cv2.imshow('frame2', gray)
        


            try:
              text_to_speech(tempText)
            except AssertionError:
              text_to_speech("Text complete")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



import cv2

cap = cv2.VideoCapture(0)
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite("frame%d.png" % count, frame)     # save frame as JPEG file
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
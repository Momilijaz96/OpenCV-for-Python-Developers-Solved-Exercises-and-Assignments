import numpy as np 
from cv2 import cv2

######Video Feed######
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame  = cap.read() #read new frome from vieo capture
    if ret:
        frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
        cv2.imshow("Live Video Feed",frame)

    ch =cv2.waitKey(1) #####VERY IMP TO IMPLEMENT LOOP BREAK LOGIC
    if ch == ord('q'):
        break

cap.release() #####VERY IMPORTANT TO RELEASE CAP RESOURCES
cv2.destroyAllWindows()
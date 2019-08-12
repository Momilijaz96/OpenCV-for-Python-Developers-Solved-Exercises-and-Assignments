import numpy as np 
from cv2 import cv2

######Video Interfacing######
cap = cv2.VideoCapture(0)
color=(0,255,0) #assumed webcan has uint8 depth
line_width = 5 #if line_width=-1 then circle is filled
radius= 100
point = (-1,-1) #initial point

#A callback that is executed whenver we click on the video feed
def click(event,x,y,flags,param):
    global point,pressed
    if event==cv2.EVENT_LBUTTONDOWN:
        print('pressed',x,y)
        point = (x,y)

#OpenCv handler for this callback
cv2.namedWindow("Live Video Feed") #same as on line 25
cv2.setMouseCallback("Live Video Feed",click) #pass function

while(True):
    ret,frame  = cap.read() #read new frome from video capture
    if ret:
        frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
        x=cv2.circle(frame,point,radius,color,line_width,-1)
        cv2.imshow("Live Video Feed",frame)

    ch =cv2.waitKey(1) #####VERY IMP TO IMPLEMENT LOOP BREAK LOGIC
    if ch == ord('q'):
        break

cap.release() #####VERY IMPORTANT TO RELEASE CAP RESOURCES
cv2.destroyAllWindows()
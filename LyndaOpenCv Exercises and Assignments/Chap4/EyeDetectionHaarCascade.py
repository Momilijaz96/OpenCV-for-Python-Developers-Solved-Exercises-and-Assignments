import numpy as np 
from cv2 import cv2

img = cv2.imread("face3.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

path="haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)
eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.04,minNeighbors=25,minSize = (15,15))

for (x,y,w,h) in eyes:
    cv2.circle(img,(x+w//2,y+h//2),w/2,(0,255,0),2)

cv2.imshow("Eye Detected",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
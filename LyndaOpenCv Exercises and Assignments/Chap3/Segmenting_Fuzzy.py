import numpy as np 
import random as rand
from cv2 import cv2

img = cv2.imread("fuzzy.png",1) 

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hsv_split = np.concatenate((hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]),axis=1)
cv2.imshow("HSV Split",hsv_split)

#Dilating Saturation channel and thresholding to get segmentation
kernel=np.ones((3,3),'uint8')
dilate=cv2.dilate(hsv[:,:,1],kernel,iterations=1)
cv2.imshow("S Dilation",dilate)
ret,dilate_thresh = cv2.threshold(dilate,200,255,cv2.THRESH_BINARY)
cv2.imshow("S Dilate Trheshold",dilate_thresh)


#Contours
canvas = np.ones(img.shape,'uint8') * 255
contours,heirarchy = cv2.findContours(dilate_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    area = cv2.contourArea(c)
    perim = cv2.arcLength(c,True)
    print("Perimeter: {}, Area: {}".format(perim,area))
    if area > 1000:
        cv2.drawContours(canvas,[c],-1,(rand.randint(0,255),0,rand.randint(0,255)),-1)

cv2.imshow("FINAL RESULT",canvas)


cv2.waitKey(0)
cv2.destroyAllWindows()
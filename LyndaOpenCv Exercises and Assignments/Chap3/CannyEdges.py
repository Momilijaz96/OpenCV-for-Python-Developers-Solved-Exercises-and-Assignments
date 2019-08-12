import numpy as np 
from cv2 import cv2

img = cv2.imread('tomato2.jpg',1)
img = cv2.resize(img,(0,0),fx=0.6,fy=0.6)
#Convert to hsv channel for segmentation, then contour miscalculation due to segmentation overlap
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret,seg_img = cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)  #red in hue channel is b/w 0-25 and 250-255
cv2.imshow("Poor Segmentation",seg_img)

#Try contouring on overlapped segments, tomatoes group considered one object
contours,heirarchy = cv2.findContours(seg_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img2 = img.copy()
cv2.drawContours(img2,contours,-1,(0,0,0),2)
cv2.imshow("Wrong Contours",img2)

#Canny Edges
edges = cv2.Canny(img,100,70) #Lower and upper limit of threshold edges 
cv2.imshow("Canny",edges)

#Canny Contours, using edges to find better segmented img for better contour
improve_seg_img = seg_img - edges
cv2.imshow("Canny Segmentation",improve_seg_img) 

contours,heirarchy = cv2.findContours(improve_seg_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,0),1)
cv2.imshow("Canny Contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
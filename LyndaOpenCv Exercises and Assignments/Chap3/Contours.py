import numpy as np 
from cv2 import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

thresh_img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) #guassion threshold with output binary threshold type
#Make sure to binarize image before using contour functions
cv2.imshow("Adaptive Thresh Image",thresh_img)

#Contours
contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

img2 = img.copy()
index = -1 #if negative all contours are drawn, index of contour to be drawn
thickness = 4
color = (255,0,255)
cv2.drawContours(img2,contours,index,color,thickness)
cv2.imshow('Contours',img2)
print("Contours",contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
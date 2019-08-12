import numpy as np
from cv2 import cv2

face = cv2.imread("face_grid.png",1)
cv2.imshow("original",face)
hsv = cv2.cvtColor(face,cv2.COLOR_BGR2HSV)
h=hsv[:,:,0]
s=hsv[:,:,1]
v=hsv[:,:,2]

hsv_split = np.concatenate((h,s,v),axis=1)
#hsv_split=cv2.resize(hsv_split,(0,0),fx=0.5,fy=0.5)
cv2.imshow("HSV Split",hsv_split)

#Skin detection
ret,min_sat = cv2.threshold(s,40,255,cv2.THRESH_BINARY)
cv2.imshow("Sat filter",min_sat)
ret,max_hue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Hue filter",max_hue)
final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow("Final Skin detection",final)

cv2.waitKey(0)
cv2.destroyAllWindows()
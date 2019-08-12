import numpy as np 
from cv2 import cv2

img = cv2.imread('messi5.jpg',1)
cv2.imshow("Original",img)
############Scaling#############
#resize(img,absolute size for image/ (0,0) means no absolute size,fx=,fy= relative factos for changing each dim of image)
img_half = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_stretch = cv2.resize(img,(300,300),interpolation=cv2.INTER_NEAREST)
img_shrink = cv2.resize(img,(100,100),interpolation=cv2.INTER_LINEAR)

cv2.imshow("Half",img_half)
cv2.imshow("Stretch",img_stretch)
cv2.imshow("Shrink",img_shrink)

##########Rotation#########
#Rotation is done by creting a transformation matrix
#getRotationMatrix2D(centre of rotation,angle, scale factor)
M = cv2.getRotationMatrix2D((0,0),-30,1) # (0,0) means top left corner
rotated=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))#apply transformation to img, args = (img, transformation, (w,h))
cv2.imshow('Rotated',rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

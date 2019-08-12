import numpy as np 
from cv2 import cv2

image = cv2.imread('butterfly.jpg')
cv2.imshow("Original Image",image)

#Gaussian Filter / Gaussian Blur = This filter uses neighbour pixel to average the value of a pixel to smooth it and remove noise
blur = cv2.GaussianBlur(image,(5,55),0) #Blur in each direction [x,y].they have to be odd number
cv2.imshow("Blurred image",blur)


#Erosion and Dilation
#Erosion = Removes boundary pixels to objects in image, turns white into black
#Dilation = Adds boundary pixels, turns black pixels into white
#Kernel is a small pixel box move around image to get the dilationa dn erosion done
temple= cv2.imread('pic1.png',1)
cv2.imshow('Temple Original',temple)

kernel=np.ones((5,5),'uint8') #odd values in both dim, #more iterations means more effect can be seen
dilate=cv2.dilate(temple,kernel,iterations=1)
erode=cv2.erode(temple,kernel,iterations=1)
cv2.imshow('Dilate',dilate)
cv2.imshow('Erode',erode)


cv2.waitKey(0)
cv2.destroyAllWindows()



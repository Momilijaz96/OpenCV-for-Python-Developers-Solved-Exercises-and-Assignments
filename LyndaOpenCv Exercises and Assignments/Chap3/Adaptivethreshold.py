import numpy as np 
from cv2 import cv2

#########Adaptive Thresholding########
'''Simple thresholding cannot deal with uneven lighting, but adaptive
thresholding actually uses neighbouring pixels to determine the 0/255 
status for a given pixel if its value is less/greater than a relative threshold
'''

img = cv2.imread('sudoku.png',0) #we only use grayimages for doing segmentation
cv2.imshow("Original",img)

#Simple tresholding - uneven lighting issues
ret,thresh_img = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary thresh",thresh_img)

thresh_adapt=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) #115-neighbour, how far adaptive threshold will act over, 1 - mean sub from end result
cv2.imshow("Adaptive Thresholding",thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
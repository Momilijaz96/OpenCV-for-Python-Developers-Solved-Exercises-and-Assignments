import numpy as np 
from cv2 import cv2

bw = cv2.imread('messi5.jpg',0) # 0 means we want gray format
height,width = bw.shape[0:2]
cv2.imshow("Original",bw)

#slow binary segmentation
binary = np.zeros([height,width,1],'uint8')
thresh = 85

for row in range(height):
    for col in range(width):
        if bw[row][col] >= 85:
            binary[row][col] = 255
        
cv2.imshow("Slow Binary image",binary) # Slow mthod of segmentation

#cv2 binary segmentation
ret, thresh_img = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY ) #other thresh methods available on opencv.org/tutorials
cv2.imshow("CV Thres image",thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
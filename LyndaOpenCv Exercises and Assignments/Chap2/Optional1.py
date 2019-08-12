import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2

########Display image in openCV#########
img = cv2.imread('Burano.jpg',-1)

#flag=1 --> Color img
#flag=0 --> grayscale
#flag=-1 -->alpha channel / original image

######Show image in OpenCv##########
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow('Image',img)
k = cv2.waitKey(0) #msec to keep output stayed , if 0 the stays
if k==27: #if escape key is pressed, then destroy windows
    cv2.destroyAllWindows() #close all windows, for a specific window use destroyWindow(name)


######Write image in OpenCv#########
cv2.imwrite('New_image_name.png',img)
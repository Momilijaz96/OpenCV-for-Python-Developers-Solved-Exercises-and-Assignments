import numpy as np 
from cv2 import cv2

img = cv2.imread('Burano.jpg',1)
if len(img)!=0:
    print("Rows of pixels = ",len(img))
    print("Coloumns in each row = ",len(img[0]))
    print("Number of chanels = ",len(img[0][0])) #3 for RGB and 4 if there is a transparency/alpha channel
    print("simply = ",img.shape)
    print("pixel values range = ",img.dtype) #uint8 means value ranges from 0-255
    print("Any random pixel value = ",img[10,5]) #10th row and 5th column have 3 channels
    print("Specific channel pixels = ",img[:, :, 0]) #red channel or blue in case of BGR
    print("Total number of pixels = ",img.size)
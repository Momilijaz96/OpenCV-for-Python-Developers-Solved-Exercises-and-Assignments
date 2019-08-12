import numpy as np 
from cv2 import cv2

###### Writing image ######
img = cv2.imread('butterfly.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite('butterfly_grap.jpg',gray)


##### Adding channel to loaded image ######
#Avoid using cv2.split as it's computationaly comples use below
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

rgba=cv2.merge((r,g,b,r)) #for apha channel use any other channel, r'll make non red parts transparent
cv2.imwrite('rgba1.png',rgba) #for img with aplha channel use png as jpg supports 3 channel only , so it'll ignore 4th channel

###Alpha note
'''
In aplhpa channel from 0 -255, thw whites act as avisible portion and 
the black act as a transparent part from which the background is visible behind image.

Similary, if we specify a given channel as aplha it remains visible while other channels get 
transparentted out'''

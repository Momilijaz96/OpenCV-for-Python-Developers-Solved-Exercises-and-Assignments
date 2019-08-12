import numpy as np 
from cv2 import cv2

color=cv2.imread("butterfly.jpg",1) #w/o one it will still be default 1
print(color.shape)
height,width,channels = color.shape #Dont messup the order of the height and width
cv2.imshow("Burano Italy",color)
cv2.moveWindow("Burano Italy",0,0) #Move window to top right corner of screen


    ######## split channels ##########
b,g,r=cv2.split(color) #split each channel into new matrix
 
    ######## Merge channels ###########

#numpy indexing 
# Here we are assigning one width section of rgb_split a value one channel matrix and remaining two channels are kept zero
rgb_split = np.empty([height,width*3,3],'uint8')  #Empty uninitialized matrix
rgb_split[:,0:width,0]=b #blue channel have b, red have zeros and green have zeros
print("Random blue section pixel (b=value/red=0/green=0) = ",rgb_split[12,round(width/2)])
rgb_split[:,width:width*2,1]=g
print("Random green section pixel (b=0/red=0/green=value) = ",rgb_split[12,round(width*2/2)])

rgb_split[:,width*2:width*3,2]=r
print("Random red section pixel (b=0/red=value/green=0) = ",rgb_split[12,round(width*3/2)])

cv2.imshow("Seperate chanels",rgb_split)
cv2.moveWindow("Seperate chanels",0,height)


#merge function
rgb_merge = np.empty([height,width*3,3],'uint8')
rgb_merge[:,0:width] =cv2.merge([b,b,b])
rgb_merge[:,width:width*2] = cv2.merge([g,g,g])
rgb_merge[:,width*2:width*3]=cv2.merge([r,r,r])

cv2.imshow("Merge channels",rgb_merge)
cv2.moveWindow("Merge channels",0,height*2)

######Hue Saturation Value
hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1) #numpy function for concatenating arrays along given axis
print("Random pixel in hsv split h=",h[2,2]," s=",s[2,2], " v=",v[2,2])
cv2.imshow("Split hsv",hsv_split)


cv2.waitKey(0)
cv2.destroyAllWindows()

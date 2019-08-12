import numpy as np 
from cv2 import cv2

black = np.zeros([150,250,1],'uint8')#(image size[150 tall, 250 wide, 1 channel],dtype
cv2.imshow("Black image",black)
print("Random black pixel = ",black[0,0,:])#0 row 0 col with all channel i.e. 1, so only one pixel at this location

ones=np.ones([150,250,1],'uint8') #Another black image as 1 is very low comaping 25 i.e white
cv2.imshow("Ones image",ones)
print("Random ones pixel",ones[0,0,:])

#To make a white image use the max value that datatype can offer
#white=ones.copy()
#white[:,:]=255
#white[:,:]*=(2**8)-1
#white[:,:]=(255,255,255)
                        ####OR#####
white=np.ones([150,250,3],'uint16') #let's say 16 bit length img so white=2^16
white*=((2**16)-1) #scale ones matrix by 2^16 - 1, -1 bzoc value starts at zero
cv2.imshow("White",white)
print("Random white pixel = ",white[0,0,:])


color=white.copy() #deep copy of white, means not connected to each other
color[:,:] = (65535,0,0) #BGR format a image with all blue pixels, asigning same value to a whole channel
cv2.imshow("blue image",color)
print("Random blue pixel = ",color[0,0,:])

cv2.waitKey(0) #wait until any key is pressed
cv2.destroyAllWindows()

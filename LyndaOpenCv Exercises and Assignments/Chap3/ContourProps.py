import numpy as np 
from cv2 import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

thresh_img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) #guassion threshold with output binary threshold type
cv2.imshow("Adaptive Thresh Image",thresh_img)

#Contours
contours, hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

thickness = 2
color = (255,0,255)

object=np.zeros([img.shape[0],img.shape[1],3],'uint8')
for c in contours:
    cv2.drawContours(object,[c],-1,color,thickness) #Draw contour of one object at time, -1 means all but c have only 1 object contour
    area = cv2.contourArea(c) #Area of one contour
    perimeter = cv2.arcLength(c,True) #Perimiter of one contour
    print("Perimeter : {}, Area: {}".format(perimeter,area))

    M=cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(object,(cx,cy),4,color,-1) #draw centroid as a small unit cirlce in the image at centroid pos    

    cv2.imshow("Centroids",object)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
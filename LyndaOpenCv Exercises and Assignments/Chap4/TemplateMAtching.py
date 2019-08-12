import numpy as np 
from cv2 import cv2

#For template Matching use grayscale images
template =cv2.resize (cv2.imread("template1.jpg",0),(0,0),fx=0.6,fy=0.6)
frame = cv2.resize(cv2.imread("tomato2.jpg",0),(0,0),fx=0.7,fy=0.7)

cv2.imshow("Template",template)
cv2.imshow("Frame",frame)

#Template Matching
result = cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)

#Draw circle at matched location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print("Max value {}, Max loc {}".format(max_val,max_loc))
cv2.circle(result,max_loc,40,255,2) #not as grayscale is 1 cahnnel so we dont need 3 channed colour
cv2.imshow("Template Matched",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
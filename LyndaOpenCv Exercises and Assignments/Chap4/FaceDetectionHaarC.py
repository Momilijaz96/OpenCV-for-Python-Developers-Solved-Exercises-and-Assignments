import numpy as np 
from cv2 import cv2

img = cv2.resize((cv2.imread("faces.jpg",1)) ,(0,0),fx=0.7,fy=0.7)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

path = "haar_cascade_fronalface_default.xml"#Path to our xml file for detecting frontal face , which contains 
#various features for classifying ROI as a face or non-face

#Cascade object
face_cascade = cv2.CascadeClassifier(path) #Loads our file and initiates our classifier
#This face_cascade object contains the cascaded classifiers for classification task

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.10,minNeighbors =5,minSize=(40,40))
#scaleFactor =  Compensating factor for making faces closer to camera
#min neighbours = number of nearby object detection required before ROI is face
# min size = Actual min size of face before it's detected as face
#Output is a list of faces detected in form of rectangles
print("Found {} Faces".format(len(faces)) )

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #top left coner = (x,y)
    #bottom right corner = (x+w,y+h)

cv2.imshow("Faces Detected",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
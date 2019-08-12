from cv2 import cv2

############Capture LiveFeed from Camera and save it##############

cap = cv2.VideoCapture('Megamind.avi')
#1 -- For second camera
#0 -- For default camera
#n -- For nth camera 
# file_name -- For video file input 

#############Save input from video##########
fourcc=cv2.VideoWriter_fourcc(*'mp4v') #video codec format, more at www.fourcc.org
out=cv2.VideoWriter('ouput.avi',fourcc,20,(720,1280)) #filename,video codec, fps, frame size


open = cap.isOpened() #checks if the videocapture ftn target source is available
while(open):
    ret,frame = cap.read()
    #ret = bool - true if frame available else false
    #frame - the captured frame
    if ret:
        #save captured frame
        out.write(frame)

        #features of frame
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Height = ",height," Width = ",width)
        
        #Make frame gray
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Capture Frame',frame_gray)
        if cv2.waitKey(50)== ord('q'): #stop video feed if q pressed
            break
    

cap.release()
out.release()
cv2.destroyAllWindows()
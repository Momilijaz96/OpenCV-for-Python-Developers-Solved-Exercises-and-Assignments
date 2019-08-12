import numpy as np 
from cv2 import cv2


#Global Variables
window_name="canvas"
canvas_img = np.ones([500,500,3],'uint8') * 255
point=(0,0)
color1=(0,255,0)
color2=(0,0,255)
radius=1
line_width=-1
color=color1
pressed =False #Variable to tell if the mouse is pressed

#Define Callabck
def click(event,x,y,flags,param):
    global pressed #this tells function we wnt to use the global version of this variable, only globalize vars that are assigned inside function
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        print("Pressed = ",point)
        cv2.circle(canvas_img,(x,y),radius,color,line_width)
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas_img,(x,y),radius,color,line_width)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed=False

    


#window initialization, Callabck assigment
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name,click)

#Forever draw loop, as we want the canvas to be responsive throughout, and callbacks respond
while(True):

    cv2.imshow(window_name,canvas_img)
    ch =cv2.waitKey(1)
    if ch == ord('q'):
        break
    elif ch == ord('c'):
        if color == color1:
            color = color2
        else:
            color = color1    

cv2.destroyAllWindows()




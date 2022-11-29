import cv2 as cv
import numpy as np

class Mask:
  rectangles = np.zeros((480, 640, 1), dtype = "uint8")

def show_clicked(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDOWN:
    cv.rectangle(param.rectangles, (x, y), (x+50, y+50), (255), thickness=2)
    print("Click success")
    
capture = cv.VideoCapture(0)

#inf loop for video
while(1):
  #read frame from camera
  ret, frame = capture.read()
  #display the frame
  cv.namedWindow(winname='Camera')
  cv.setMouseCallback('Camera', show_clicked, param=Mask)
  
  con, hir = cv.findContours(Mask.rectangles, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
  
  cv.drawContours(frame, con, -1, (0,255,0), 1)
  cv.imshow('Camera', frame)
  if cv.waitKey(1) & 0xFF == ord('c'):
    Mask.rectangles = np.zeros((480, 640, 1), dtype = "uint8")
  #Quit from loop if "q" key was pressed
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
  

# release the camera from video capture
capture.release()
# # De-allocate any associated memory usage 
cv.destroyAllWindows()
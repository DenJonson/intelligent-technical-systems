import cv2 as cv
import numpy as np

#Get object from camera
capture = cv.VideoCapture(0)
set_ret, set_frame = capture.read()

class Mask:
  rectangles = np.ones(set_frame.shape, dtype = set_frame.dtype) * 0

def show_clicked(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDOWN:
    cv.rectangle(param.rectangles, (x, y), (x+50, y+50), (0,255,0), thickness=2)
    

#inf loop for video
while(1):
  #read frame from camera
  ret, frame = capture.read()
  #display the frame
  cv.namedWindow(winname='Camera')
  cv.setMouseCallback('Camera', show_clicked, param=Mask)
  frame = cv.merge(frame, Mask.rectangles)
  cv.imshow('Camera', frame)
  #Quit from loop if "q" key was pressed
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

# release the camera from video capture
capture.release()
# # De-allocate any associated memory usage 
cv.destroyAllWindows()
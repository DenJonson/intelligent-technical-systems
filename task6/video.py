import cv2 as cv

#Get object from camera
capture = cv.VideoCapture(0)

#inf loop for video
while(1):
  #read frame from camera
  ret, frame = capture.read()
  #display the frame
  cv.imshow('Camera', frame)
  #Quit from loop if "q" key was pressed
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

# release the camera from video capture
capture.release()
# # De-allocate any associated memory usage 
cv.destroyAllWindows()
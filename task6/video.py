import cv2 as cv

#Get object from camera
capture = cv.VideoCapture(0)
class Cords:
  rec_x = 0
  rec_y = 0

def show_clicked(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDOWN:
    param.rec_y = y
    param.rec_x = x
    



#inf loop for video
while(1):
  #read frame from camera
  ret, frame = capture.read()
  cv.rectangle(frame, (Cords.rec_x, Cords.rec_y), (Cords.rec_x + 100, Cords.rec_y + 100), (0, 0, 0), thickness=3)
  #display the frame
  cv.imshow('Camera', frame)
  cv.setMouseCallback('Camera', show_clicked, param=Cords)
  #Quit from loop if "q" key was pressed
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

# release the camera from video capture
capture.release()
# # De-allocate any associated memory usage 
cv.destroyAllWindows()
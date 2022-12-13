import cv2 as cv
import numpy as np

#Создаю класс, содержащий изображение с прямоугольниками, так как не знаю, как передать в функцию переменную, а не ее копию
class Mask:
  rectangles = np.zeros((480, 640, 1), dtype = "uint8")

#Определяю функцию-обработчик
def show_clicked(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDOWN:
    #Рисую квадрат в заданном месте
    cv.rectangle(param.rectangles, (x-25, y-25), (x+25, y+25), (255), thickness=2)
    
#Создаю объект с изображением с камеры
capture = cv.VideoCapture(0)

#inf loop for video
while(1):
  #read frame from camera
  ret, frame = capture.read()
  #display the frame
  cv.namedWindow(winname='Camera')
  #Устанавливаю обработчик событий
  cv.setMouseCallback('Camera', show_clicked, param=Mask)
  #Нахожу контуры нарисованных квадратов
  con, hir = cv.findContours(Mask.rectangles, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
  #Рисую эти контуры поверх изображения с каммеры
  cv.drawContours(frame, con, -1, (0,255,0), 1)
  #Показываю изображение
  cv.imshow('Camera', frame)
  #ЧИщу картинку от квадратов при нажатии с
  if cv.waitKey(1) & 0xFF == ord('c'):
    Mask.rectangles = np.zeros((480, 640, 1), dtype = "uint8")
  #Quit from loop if "q" key was pressed
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
  

# release the camera from video capture
capture.release()
# # De-allocate any associated memory usage 
cv.destroyAllWindows()
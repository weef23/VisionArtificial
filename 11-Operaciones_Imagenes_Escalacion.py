import numpy as np
import imutils as im
import cv2
#######################################################################################################################
### Traslacion de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
imagen2 = cv2.resize(img, (200, 200)) ## Redimensionamos la imagen a 100 x 50
alto, ancho, canal = imagen2.shape
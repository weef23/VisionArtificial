########################################################################################################################
import cv2
import numpy as np
### Funcion para dibujar circunferencia
def dibujar_Circulo(event,x,y,flags,param):
    print(event)
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x, y), 100, (255, 255, 0), -1)
#######################################################################################################################
## Creamos una imagen vacia
img =  np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("ImagenVacia", cv2.WINDOW_NORMAL)

cv2.setMouseCallback("ImagenVacia", dibujar_Circulo)
########################################################################################################################
while True:
    cv2.imshow("ImagenVacia", img)
    if cv2.waitKey(0) == 27:
        break
########################################################################################################################
cv2.destroyAllWindows()
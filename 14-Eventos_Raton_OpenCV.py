########################################################################################################################
import cv2
import numpy as np
### Funcion para dibujar circunferencia
def eventosRaton(event,x,y,flags,param):
    if(event == 1):
        print(f"Clic Izquierdo X => {x}, Y=> {y}")
    elif (event == 2):
        print(f"Clic Derecho X => {x}, Y=> {y}")
    elif (event == 3):
        print(f"Clic boton central X => {x}, Y=> {y}")
    elif (event == 4):
        print(f"Se suelta el boton izquierdo X => {x}, Y=> {y}")
    elif (event == 5):
        print(f"Se suelta el boton derecho X => {x}, Y=> {y}")

#######################################################################################################################
## Creamos una imagen vacia
img =  np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("ImagenVacia")

cv2.setMouseCallback("ImagenVacia", eventosRaton)
########################################################################################################################
while True:
    cv2.imshow("ImagenVacia", img)
    if cv2.waitKey(0) == 27:
        break
########################################################################################################################
cv2.destroyAllWindows()
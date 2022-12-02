#######################################################################################################################
### Las imagenes en si son Matrices de m x n
import cv2
import numpy as np
########################################################################################################################
## Crea dos imagenes en negro las cuales vamos a rellenar
## Creamos imagenes de 512 x 512 con canal RGB
imagen1 =  np.zeros((512, 512, 3), np.uint8)
imagen2 = np.zeros((512, 512, 3), np.uint8)
## Dibujamos un circulo primero
imagen1 = cv2.circle(imagen1, (255,255), 100, (0, 0, 255), -1)
## En la segunda imagen dibujamos un cuadrado
imagen2 = cv2.rectangle(imagen2, (150, 150), (300, 300), (255, 0, 0), cv2.FILLED)

## Ahora creamos una imagen resultante de la suma de ambas
## En la imagen resultante veremos como el rectangulo se sobrepone al circulo, muy ultil para crear filtros.
imagenSuma = cv2.add(imagen1, imagen2)
## Resta de imagenes
imagenResta = cv2.subtract(imagen1, imagen2)
## Multiplicacion de imagenes
imagenMultiplicacion = cv2.multiply(imagen1, imagen2)
## Division de Imagenes
imagenDivision = cv2.divide(imagen1, imagen2)
########################################################################################################################
cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagen2", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagenSuma", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagenResta", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagenMultiplicacion", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagenDivision", cv2.WINDOW_NORMAL)
########################################################################################################################
cv2.imshow("imagen1", imagen1)
cv2.imshow("imagen2", imagen2)
cv2.imshow("imagenSuma", imagenSuma)
cv2.imshow("imagenResta", imagenResta)
cv2.imshow("imagenDivision", imagenDivision)
########################################################################################################################
cv2.waitKey()
cv2.destroyAllWindows()
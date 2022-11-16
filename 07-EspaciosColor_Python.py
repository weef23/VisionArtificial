################## DELIMITACION DE ESPACIOS DE COLORES EN IMAGENES ############################################
import cv2
import numpy as np

img = cv2.imread("./Images/candados.jpg")
###################################################################################################
### obtenemos las dimenciones de la imagen con esto procedemos a realizar el corte
largo, ancho, canales = img.shape
### Procedemos con el corte de la imagen
primer_candado = img[0:largo, 0:int(ancho/2)]
segundo_candado = img[0:largo, int(ancho/2):ancho]

## convertimos la imagen en escala de grises para reducir el rango de colores a manejar
grayscale = cv2.cvtColor(segundo_candado, cv2.COLOR_BGR2GRAY)
## A partir del segundo candado intetaremos establecer el espacio de color para diferenciar la imagen
### Imagen binaria
umbral = 80
binaria = np.uint8((grayscale > umbral) * 255)

## Vemos ahora una mayor diferenciacion entre la imagen y el fondo que se ve completamente en blanco
## Esto es muy util en la deteccion de patrones en las imagenes
print(binaria)
cv2.namedWindow("imagen-binaria", cv2.WINDOW_NORMAL)
cv2.imshow("imagen-binaria", binaria)
cv2.waitKey()
cv2.destroyAllWindows()

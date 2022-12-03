######################################################################################################################
##### El histograma nos ayuda a determinar la escala de grises de una imagen.
import cv2
import numpy as np
import matplotlib.pyplot as ptl
########################################################################################################################
img = cv2.imread("Images/1.jpg")
## Lo convertimos al canal hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
## Lo convertimos a escala de grises
I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
########################################################################################################################
umbral = 255
## Convertimos la imagen en binaria
## Todo lo que este por debajo de 200 se convierte en 255
mascara = np.array((I < 200) * 255)
## Aplanamos la imagen con la funcion flatten
datos = I.flatten()
ptl.hist(datos, bins=100)
## Dividimos la imagen en sus tres canales
## Dividimos la imagen en sus tres canales
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
r,g,b = cv2.split(img)
rojo = r.flatten()
verde = g.flatten()
azul = b.flatten()
## Generamos los histogramas por canal aunque por la naturaleza del de la imagen en este caso esta muy complicado
## Sacar el umbral de la imagen, lo cual es lo mas comun en una imagen
ptl.hist(rojo, bins=100, histtype='stepfilled', color='red')
ptl.hist(verde, bins=100, histtype='stepfilled', color='green')
ptl.hist(azul, bins=100, histtype='stepfilled', color='blue')


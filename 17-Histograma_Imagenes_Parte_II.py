import cv2
import numpy as np
import matplotlib.pyplot as ptl
########################################################################################################################
img = cv2.imread("Images/lenna.jpg")
### Convertimos la imagen a Escala de grises
I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Anteriormente usamos la libreria Matplolib y los canales de la imagen para obtener el histograma
## En esta ocasion usaremos la funcion hist de opencv, estamos pasando la imagen en escala de grises.
## La escala de grises convierte la imagen un una matriz de dos dimensiones donde se almacena la intensidad
hist = cv2.calcHist([I], [0], None, [256], [0, 255])
## Tenemos una imagen bien distribuida en cuanto a color e intensidad.
ptl.hist(I.ravel(), 256, [0, 255])
##### Histograma de una imagen a color
color = ('b', 'g', 'r')

## Lo que estamos haciendo en esta parte es con la funcion enumerate convertir la variable color en los siguiente
## 0 : b, 1: g, 2: r esto para poder generar el histograma por cada canal de la imagen
for i, col in enumerate(color):
    hist = cv2.calcHist([I], [i], None, [256], [0, 255])
    ptl.plot(hist, color=col)
    ptl.xlim([0, 256]) ## Este es el rango de valores de los colores de la imagen.
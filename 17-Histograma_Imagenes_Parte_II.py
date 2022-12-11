import cv2
import matplotlib.pyplot as plt
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
    hist = cv2.calcHist([img], [i], None, [256], [0, 255])
    ptl.plot(hist, color=col)
    ptl.xlim([0, 256]) ## Este es el rango de valores de los colores de la imagen.
    plt.show()
########################################################################################################################
#### Uso de mascara para el calculo de histogramas
mascara = np.zeros(img.shape[:2], np.uint8)
mascara[0:300, 0:300] = 255
### Aplicamos una compuerta and bit a bir entre la misma y imagen pero unicamente a los pixeles blancos
masked_img = cv2.bitwise_and(I, I, mask=mascara)
hist_Completo = cv2.calcHist([I], [0], None, [256], [0, 255])
masked_img_hist = cv2.calcHist([masked_img], [0], None, [256], [0, 255])
########################################################################################################################
plt.subplot(221), plt.imshow(I,"gray")
plt.subplot(222), plt.imshow(mascara,"gray")
plt.subplot(223), plt.imshow(masked_img, "gray")
plt.subplot(224), plt.plot(hist_Completo), plt.plot(masked_img_hist)
plt.xlim([0, 255])
plt.show()

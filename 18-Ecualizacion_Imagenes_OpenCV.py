##### Ecualizacion del Histograma
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as ptl
########################################################################################################################
## Leemos la imagen en escala de grises
img = cv2.imread("Images/2.jpg",0)
## procedemos con la ecualizacion de la imagen, para ello usamos la funcion equalizeHist de OpenCV
equ = cv2.equalizeHist(img)
## Concatenamos la imagen original con respecto a la imagen ecualizada. Para ello usamos la funcion
## hstack de la libreria OpenCV
res = np.hstack((img, equ))
### Mostramos la imagen resultante, a la izquierda se ve la imagen original y a la derecha la imagen ecualizada
cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)
cv2.imshow("resultado", res)
cv2.waitKey()
cv2.destroyAllWindows()

### El Grafico de la imagen los podemos generar usando el metodo de np o el metodo de openCV
### En este cado utilizaremos la libreria de openCV para generar el histograma
histOriginal = cv2.calcHist([img], [0], None, [256], [0, 255])
histEqualizada = cv2.calcHist([equ], [0], None, [256], [0, 255])

## Una vez que tenemos ambos histogramas podemos proceder a graficarlos
## Procedemos a graficar el histograma
ptl.subplot(221), ptl.plot(histOriginal, color="gray")
ptl.subplot(222), ptl.plot(histEqualizada, color="black")
plt.xlim([0, 255])
plt.show()

## Ahora veamos como se hace usando la funcion histogram de np array

## Imagen normal
hist, bin = np.histogram(img.flatten(), 256, [0, 256])
ptl.hist(img.flatten(), 256, [0, 256], color='b')
ptl.xlim([0, 256])
ptl.legend('H', loc ="upper left")
ptl.show()

## Imagen ecualizada, Podemos ver una dispersion en la intensidad dando un mayor equilibrio a la imagen
hist, bin = np.histogram(equ.flatten(), 256, [0, 256])
ptl.hist(equ.flatten(), 256, [0, 256], color='b')
plt.xlim([0, 256])
ptl.legend('H', loc ="upper left")
ptl.show()
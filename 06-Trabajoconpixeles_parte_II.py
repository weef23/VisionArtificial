import cv2
import numpy as np
###################################################################################################
## Leemos la imagen como siempre y la guardamos en img
img = cv2.imread("./Images/candados.jpg")
###################################################################################################
### obtenemos las dimenciones de la imagen con esto procedemos a realizar el corte
largo, ancho, canales = img.shape
### Procedemos con el corte de la imagen
primer_candado = img[0:largo, 0:int(ancho/2)]
segundo_candado = img[0:largo, int(ancho/2):ancho]
##################################################################################################
## Nos traemos el canal original de la imagen, nuestra imagen ser una imagen de 8 bits
imgen_compuesta = np.zeros((largo, ancho, canales), np.uint8)
##################################################################################################
### Rellenamos la mitad de la imagen
imgen_compuesta[0:largo, 0:int(ancho/2)] = segundo_candado
imgen_compuesta[0:largo, int(ancho/2):ancho] = primer_candado

cv2.namedWindow("imagen-compuesta", cv2.WINDOW_NORMAL)
cv2.imshow("imagen-compuesta", imgen_compuesta)
cv2.waitKey()
cv2.destroyAllWindows()
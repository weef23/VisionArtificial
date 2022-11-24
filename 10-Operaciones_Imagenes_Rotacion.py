import numpy as np
import imutils as im
import cv2
#######################################################################################################################
### Traslacion de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
imagen2 = cv2.resize(img, (200, 200)) ## Redimensionamos la imagen a 200 x 200
alto, ancho, canal = imagen2.shape

## Definimos el angulo de rotacion el centro y la escala
angulo = 90
centro = (ancho//2, alto//2)
scale = 1

### Obtenemos la matriz de rotacion
mR = cv2.getRotationMatrix2D(centro, angulo, scale)
#### Definimos una imagen vacia, con 8 bits
imgRotada = np.zeros((alto + 1, ancho + 1, canal), np.uint8)
#######################################################################################################################
### Primero lo hacemos utilizando ciclos for

for i in range(alto):
    for j in range(ancho):
        ## Definimos el vector posision
        px = np.array(([j, i, 1]), np.uint8)

        ## Igual que con la tralacion aplicamos el producto punto entre mR y px
        ## Con esto obtenemos las nuevas coordenadasde la imagen
        dot = np.dot(mR, px)
        x = int((dot[0]))
        y = int((dot[1]))
        ### Vamos rellenando la imagen vacia por los pixeles originales
        ### Pixel por pixel en la nueva posicion
        imgRotada[y, x] = imagen2[i, j]

### Podemos usar la funcion warp para hacer la rotacion de la imagen de la misma forma que con la traslacio
## Mandamos a llamar la funcion, la ventaja es que este metodo genera menos ruidos en la imagen.
imgT2 = cv2.warpAffine(imagen2, mR, (alto, ancho))
### Tambien es posible usar la libreria imutils para realizar la rotacion

angulo = 45
imgT3 = im.rotate_bound(imagen2, angulo)

############ Mostramos la imagen original y la imagen final ###########################################

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("rotada", cv2.WINDOW_NORMAL)
cv2.namedWindow("rotacionwarp", cv2.WINDOW_NORMAL)
cv2.namedWindow("imutilrotacion", cv2.WINDOW_NORMAL)


cv2.imshow("original", imagen2)
cv2.imshow("rotada", imgRotada)
cv2.imshow("rotacionwarp", imgT2)
cv2.imshow("imutilrotacion", imgT3)

cv2.waitKey()
cv2.destroyAllWindows()
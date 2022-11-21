################### OPERACIONES /TRANSFORMACION DE UNA EMPRESA ##########################
import numpy as np
import cv2

### Traslacion de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
imagen2 = cv2.resize(img(100, 50)) ## Redimensionamos la imagen a 100 x 50
alto, ancho, canal = imagen2.shape

### Definimos el desplazamiento en x, y de la imagen
tx = 10 ## Trasladamos 10 en el eje x
ty = 2  ## Trasladamos 2 en el eje y
## Definimos la matriz de traslacion
mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)
## Imagen trasladada
imgT = np.zeros((alto + 2, ancho + 10, canal), np.uint8)

## Con el siguiente for procedemos a recorrer las filas y las columnas
## Extraemos la posicion del vector imagen
for i in range(alto):
    for j in range(ancho):
        px = np.array(([j, i, 1]), np.uint8)
        ## La posicion resultante es el producto punto entre la
        ## Matriz de posicion inicial y la matriz de traslacion mT
        dot = np.dot(mT, px)
        x = dot[0]
        y = dot[1]
        imgT[x, y] = img[i, j]

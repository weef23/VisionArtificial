################### OPERACIONES/TRANSFORMACION DE UNA EMPRESA ##########################
import numpy as np
import cv2

### Traslacion de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
imagen2 = cv2.resize(img, (100, 50)) ## Redimensionamos la imagen a 100 x 50
alto, ancho, canal = imagen2.shape

### Definimos el desplazamiento en x, y de la imagen
tx = 25 ## Trasladamos 10 en el eje x
ty = 2  ## Trasladamos 2 en el eje y
## Definimos la matriz de traslacion
mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)
## Imagen trasladada
imgT = np.zeros((alto + ty, ancho + tx, canal), np.uint8)

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
        ### Vamos rellenando la imagen vacia por los pixeles originales
        ### Pixel por pixel en la nueva posicion
        imgT[y, x] = imagen2[i, j]

## OpenCV tambien proporciona un metodo para hacer esto mismo
mT2 = np.float32([[1, 0, 10], [0, 1, 20]]) ## Generamos la matriz de transformacion

## Con la siguiente funcion pasamos la imagen, la matriz de transformacion
## El Alto y el ancho y podemos conseguir el mismo resultado
imgT2 = cv2.warpAffine(imagen2, mT2, (alto, ancho))

#######################################################################################################
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("trasladada", cv2.WINDOW_NORMAL)
cv2.namedWindow("warpAffine", cv2.WINDOW_NORMAL)
#######################################################################################################
cv2.imshow("original", imagen2)
cv2.imshow("trasladada", imgT)
cv2.imshow("warpAffine", imgT2)
#######################################################################################################
cv2.waitKey()
cv2.destroyAllWindows()
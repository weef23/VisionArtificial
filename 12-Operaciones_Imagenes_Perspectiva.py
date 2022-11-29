import cv2
import numpy as np
## Cargamos la imagen a transformar
#######################################################################################################################
### Transformacion en perspectiva de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
alto, ancho, canal = img.shape
## Cargamos la matriz de transformacion
tMatriz = np.array([[1, 1, 0], [0, 1, 0], [0, 1, 1]])

### Creamos una imagen vacia donde almacenaremos la nueva imagen
imagenResultante = np.zeros((alto+1500, ancho+1500, canal), np.uint8)

## Realizamos la traslacion usando los ciclos for
for i in range(alto):
    for j in range(ancho):
        ## Obtenemos el pixel especifico de la imagen en i y j
        pixel = img[i, j]
        ### Obtenemos el vector posicion
        vectorPos = [j, i, 1]
        ## Realizamos el producto punto entre el vector posicion y la
        ## Matriz de transformacion
        dot = np.dot(tMatriz, vectorPos)
        x = dot[0]
        y = dot[1]
        ## Rellenamos el vector de la imagen resultante
        imagenResultante[y, x] = pixel
#######################################################################################################################

#######################################################################################################################
## Procedemos a mostrar las imagenes resultantes
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("transformada", cv2.WINDOW_NORMAL)

cv2.imshow("original", img)
cv2.imshow("transformada", imagenResultante)
cv2.waitKey()
cv2.destroyAllWindows()
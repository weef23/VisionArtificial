import numpy as np
import imutils as im
import cv2
#######################################################################################################################
### Traslacion de una imagen usando OpenCV
img = cv2.imread("./Images/1.jpg")
alto, ancho, canal = img.shape
## Definimos la escala que ha de tomar la imagen
escala = 2
## Definimos la matriz de escalacion
matrizEscalacion = np.array([[escala, 0, 0], [0, escala, 0], [0, 0, 1]])
## Definimos una imagen vacia
imagenEscalada = np.zeros((alto * escala, ancho*escala, 3), np.uint8)
#######################################################################################################################
for i in range(alto):
    for j in range(ancho):
        ## Vector pixel, este vector contiene cada uno de los pixeles de la imagen
        pixel = img[i, j]
        ## Define el vector de la posicion de la imagen
        vectorPosicion = [j, i, 1]
        dot = np.dot(matrizEscalacion, vectorPosicion)
        x = dot[0]
        y = dot[1]
        ## Guardamos los pixeles en la posicion resultante de la imagen escalada
        imagenEscalada[y, x] = pixel
########################################################################################################################
## OpenCV tiene la funcion resize para realizar esta misma operacion de forma mas eficiente, ya la hemos usado antes
imagenEscalada2 = cv2.resize(img, (1024, 720), interpolation=cv2.INTER_LINEAR)
########################################################################################################################
### Mostramos la imagen original y la imagen escalada
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("escalada", cv2.WINDOW_NORMAL)
cv2.namedWindow("escalada2", cv2.WINDOW_NORMAL)
########################################################################################################################
cv2.imshow("original", img)
cv2.imshow("escalada", imagenEscalada)
cv2.imshow("escalada2", imagenEscalada2)
########################################################################################################################
cv2.waitKey()
cv2.destroyAllWindows()
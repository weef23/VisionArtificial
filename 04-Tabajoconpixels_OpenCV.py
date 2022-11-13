### Manejo de Pixeles con OpenCV
import cv2
import numpy as np
#######################################################################################################################
### Creamos una matriz de enteros de 8 bits de 100 * 100 de 3 dimensiones
### Usamos una dimension para cada canal RGB
imagenObscura = np.zeros((100, 100, 3), np.uint8)
#################################################################################
imagenObscura[97, 97] = [255, 255, 255]
pixel = imagenObscura[97, 97]
## Los rangos de valores en un canal RGB van entre 0-255
## Cada dimension representa un canal cuyo valor va entre 0 y 255
## A continuacion tenemos el color Blanco.
print(pixel)
## Obtener las dimensiones de una imagen generada
alto, ancho, canales = imagenObscura.shape
print(alto, ancho,canales)

### Podemos recorrer la imagen pixel por pixel
for i in range(alto):
    for j in range(ancho):
        print(imagenObscura[i, j])

### Modificamos el color de todos los pixeles con excepcion del pixel blanco
for i in range(alto):
    for j in range(ancho):
        pixel = imagenObscura[i, j] ## Obtenemos la imagen pixel a pixel
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            ## 255, 0, 0 Color Azul
            ## 0 , 255, 0 Color Verde
            ## 0, 0, 255 Colo Rojo
            imagenObscura[i, j] = [255, 0, 0] ## Color azul

##############################################################################################################
## Creamos una ventana vacia para mostrar la imagen por pantalla
cv2.namedWindow("black", cv2.WINDOW_NORMAL)
cv2.imshow("black", imagenObscura)
cv2.waitKey()
cv2.destroyAllWindows()
####################  Seleccion del ROI usando OpenCV ###################################
import cv2
import numpy as np
## Leemos la imagen como de costumbre
img = cv2.imread("./Images/candados.jpg")
imageCopy = img.copy()
## Obtenemos las dimensiones de la imagen
## Una imagen a color es una matriz de n x m x c, donde las
## Primeras dos dimensiones son el largo y ancho
## y c representa los colores de la imagen
largo, ancho, color = img.shape
cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)

## La funcion select ROI nos permite desplegar un selector dinamico
roi1 = cv2.selectROI("ROI", img)
print(roi1)
## A partir del roi podemos tomar las coordenadas del selector y hacer el corte.
crop1 = img[int(roi1[0]):int(roi1[1] + int(roi1[3])), int(roi1[0]):int(roi1[0] + roi1[2])]
roi2 = cv2.selectROI("ROI", img)
print(roi2)
crop2 = img[int(roi2[0]):int(roi2[1] + int(roi2[3])), int(roi2[0]):int(roi2[0] + roi2[2])]
############################################################################################################
alto1, ancho1, color1 = crop1.shape
alto2, ancho2, color2 = crop2.shape
## Cambiamos el tamaño de la imagen con un resize
nuevoCandado1 = cv2.resize(crop1, (alto2, ancho2))
nuevoCandado2 = cv2.resize(crop2, (alto1, ancho1))
#############################################################################################################
### Hacemos la sustitucion en la imagen copia.
imageCopy[int(roi1[0]):int(roi1[1] + int(roi1[3])), int(roi1[0]):int(roi1[0] + roi1[2])] = crop2
imageCopy[int(roi2[0]):int(roi2[1] + int(roi2[3])), int(roi2[0]):int(roi2[0] + roi2[2])] = crop1

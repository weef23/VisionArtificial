#### Conversion de Espacios de color con Python + OpenCV
import cv2
## Cargamos la imagen
img = cv2.imread("./Images/1.jpg")
## Con la funcion split podemos dividir la imagen
## En los distintos canales
r,g,b = cv2.split(img)
## La funcion merge nos permite volver a unir los canales
## En la imagen original
img = cv2.merge((r, g, b)) ## Unir las imagenes
## Creamos la ventana vacia
cv2.namedWindow("RGB", cv2.WINDOW_NORMAL)

### De la siguiente forma podemos filtrar cada uno de los canales rgb de la imagen.
while True:
    key = cv2.waitKey()

    if key == ord("b"):
        cv2.imshow("RGB", b)
    elif key == ord("g"):
        cv2.imshow("RGB", g)
    elif key == ord("r"):
        cv2.imshow("RGB", r)
    elif key == ord("c"):
        cv2.imshow("RGB", img)
    else:
        break
## Destruye todas las ventanas creadas
cv2.destroyAllWindows()
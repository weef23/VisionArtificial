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
## Espacio de color HSV, es mayormente utilizado para la deteccion de objetos mediante color.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv) ## Dividimos la imagen en los canales hsv

### Tambien podemos hacer la conversion de imagenes en escala de grises
### Una vez cargada la imagenPi
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
    elif key == ord("l"):
        cv2.imshow("RGB", hsv)
    elif key == ord("h"):
        cv2.imshow("RGB", h)
    elif key == ord("s"):
        cv2.imshow("RGB", s)
    elif key == ord("v"):
        cv2.imshow("RGB", v)
    elif key == ord("p"):
        cv2.imshow("RGB",grayscale)

    else:
        break
## Destruye todas las ventanas creadas
cv2.destroyAllWindows()
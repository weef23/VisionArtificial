######################### JUGANDO CON WAITKEY Y NAMEWINDOW ########################################
import cv2

img1 = cv2.imread("./Images/1.jpg")
img2 = cv2.imread("./Images/1.jpg", 0)

#cv2.imshow("Ventana", img1)
####### Con NameWindows podemos crear una ventana vacia
# cv2.namedWindow("Ventana", cv2.WND_PROP_FULLSCREEN)
####### Establecemos las caracteristicas de la ventana
# cv2.setWindowProperty("Ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.namedWindow("Ventana", cv2.WINDOW_NORMAL)
while True:
    key = cv2.waitKey()

    if key == ord("g"):
        cv2.imshow("Ventana", img2)
    elif key == ord("c"):
        cv2.imshow("Ventana", img1)
    else:
        break
## Destruye todas las ventanas creadas
cv2.destroyAllWindows()
#######################################################################################################################
import cv2
import numpy as np
## Variable Global
global listaPuntos
listaPuntos = []
########################################################################################################################
def obtenerPuntos(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        listaPuntos.append([x, y])
########################################################################################################################
img = cv2.imread("./Images/1.jpg")
h, w, c = img.shape
########################################################################################################################
cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL)
## Obtenemos los puntos dando dobleclick con el raton
cv2.setMouseCallback("imagen1", obtenerPuntos)
cv2.imshow("imagen1", img)
########################################################################################################################
#### Ahora vamos a imprimir los puntos captados desde el mouse
while True:
    if cv2.waitKey(0) == 13:
        print(listaPuntos)
        pts1 = np.float32(listaPuntos)
        pts2 = np.float32([[0, 0], [w, 0], [0, h], [h,w]])
        mT = cv2.getPerspectiveTransform(pts1, pts2)
        imgResultado = cv2.warpPerspective(img, mT, (h, w))
        cv2.imshow("imagen1", imgResultado)

    if cv2.waitKey(0) == 27:
        break
########################################################################################################################
## Destruimos todas las ventanas
cv2.destroyAllWindows()
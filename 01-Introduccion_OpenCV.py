############################### Introduccion a OpenCV ######################################################
import cv2
## La funcion imread nos permite hacer la carga de la imagen

def leer_Imagen(url):
    img = cv2.imread(url)
    ## Con imshow hacemos la carga de la imagen en una ventana
    cv2.imshow("Ventana 1", img)
    ############################################################################################################
    ### El tiempo de muestreo de la señal
    cv2.waitKey()  ## Espera que se presione una tecla
    cv2.destroyAllWindows()  ## Destruye la ventana una vez se cierra.

##################################################################################################################
def leer_img_gs(url):
    ###EL parametro IMREAD_GRAYSCALE
    img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Deteccion de anomalias", img)
    cv2.waitKey()  ## Espera que se presione una tecla
    cv2.destroyAllWindows()  ## Destruye la ventana una vez se cierra.

##################################################################################################################
menu = """
            Que desea hacer? 
            1- Abrir Imagen normal
            2- Abrir Imagen en Escala de Grises
            3- Salir

           Elija una opcion por favor: 
    """
###################################################################################################################
opcion = input(menu)
###################################################################################################################
if opcion == '3':
    exit(0)
elif opcion == '1':
    leer_Imagen("./Images/1.jpg")
elif opcion == '2':
    leer_img_gs("./Images/1.jpg")
else:
    print("La opcion seleccionada no es correcta.")



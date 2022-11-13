### Manejo de Pixeles con OpenCV
import cv2
import numpy as np

### Creamos una matriz de enteros de 8 bits de 100 * 100 de 3 dimensiones
### Usamos una dimension para cada canal RGB
imagenObscura = np.zeros((100, 100, 3), np.uint8)

#################################################################################
pixel = imagenObscura[97, 97]
print(pixel)
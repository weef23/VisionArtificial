#######################################################################################################################
import cv2
import numpy as np

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Una lista tiene muchas ventajas la primera es la facilidad de recorrerlo
## La primera es el uso de list comprehension
[print(i) for i in lista]
## Podemos hacer slicing a las listas, por eso son muy utiles en procesamiento de imagenes
print(lista[:])
print(lista[5:]) ## Imprimimos a partir de la posicion 6
print(lista[::-1]) ## Imprimimos la lista invertida

### Sustituir todos los valores de una lista a partir de una posicion
lista[5:] = [1, 1, 1, 1]
print(lista)
### Tambien es posible hacerlo de esta forma con list comprenhension y un if en una sola linea.
lista = [2 if i >= 5 else lista[i] for i in range(len(lista))]
print(lista)
## La ventaja de esta ultima forma es que podemos hacer la sustitucion por medio de una condicion
## Este es otro ejemplo.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [0 if x % 2 == 1 else x for x in a]
print(a)
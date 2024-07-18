# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

import string # para manejar los signos de puntuación

def contador():
    
    # solicitamos la frase y eliminamos los signos de puntuación
    frase = (input('Introduce frase a analizar: ')).lower()
    for punct in string.punctuation:
        frase = frase.replace(punct, "")
        
    # .. y la dividimos en palabras
    separadas = frase.split()
    
    # creamos un diccionario vacío para las palabras repetidas
    conteo = {}
    
    # contamos las palabras y vamos agregando
    for palabra in separadas:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
            
    # hacemos recuento
    for palabra, cantidad in conteo.items():
        print(f'{palabra}: {cantidad}')
    
contador()
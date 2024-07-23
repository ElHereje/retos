# /*
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */

str1 = (input('Introduce un frase: ')).lower()

lisa = str1.replace(' ','')
lisa_invertida = lisa
lisa = list(lisa)
lisa_invertida = list(lisa_invertida)
lisa_invertida.reverse()

if lisa == lisa_invertida:
    print('Es un palíndromo')
else:
    print('No lo es')
        


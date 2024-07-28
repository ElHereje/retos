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
        

# Este código en Python toma una frase del usuario, la procesa para eliminar los espacios y convertirla a minúsculas, 
# y luego verifica si es un palíndromo (una palabra o frase que se lee igual de adelante hacia atrás y viceversa). 
# Vamos a desglosar cada línea:

# str1 = (input('Introduce un frase: ')).lower()

# Aquí se solicita al usuario que introduzca una frase mediante la función input().
# La frase introducida se convierte a minúsculas con el método .lower().
# El resultado se almacena en la variable str1.

# lisa = str1.replace(' ','')

# Este paso elimina todos los espacios de la frase usando el método .replace(' ', '').
# El resultado se almacena en la variable lisa.

# lisa_invertida = lisa

# Aquí se hace una copia de lisa y se asigna a lisa_invertida.

# lisa = list(lisa)

# La variable lisa, que es una cadena de texto, se convierte en una lista de caracteres.

# lisa_invertida = list(lisa_invertida)

# Similar al paso anterior, lisa_invertida se convierte en una lista de caracteres.

# lisa_invertida.reverse()

# La lista lisa_invertida se invierte usando el método .reverse(). Ahora contiene los mismos caracteres que 
# lisa pero en orden inverso.

# if lisa == lisa_invertida:

# Se compara la lista lisa con lisa_invertida para ver si son iguales.

# print('Es un palíndromo')

# Si las listas son iguales, significa que la frase es un palíndromo, y se imprime "Es un palíndromo".

# else:

# Si las listas no son iguales, se ejecuta la siguiente instrucción.

# print('No lo es')

# Si las listas no son iguales, se imprime "No
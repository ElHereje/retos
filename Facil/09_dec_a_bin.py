# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def binario(num):
    
    # num = int(input('Introduce una cifra numérica: '))
    # print(f'{num} en binario es: {bin(num)}')

    # caso especial para el 0
    if num == 0:
        return '0'
        
    # iniciamos la cadena y convertimos
    bin = ''
    while num > 0:
        resto = num % 2
        bin = str(resto) + bin
        num = num // 2
        
    return bin
        
numero = int(input('Introduce una cifra numérica: '))
print(f'{numero} en binario es {binario(numero)}')

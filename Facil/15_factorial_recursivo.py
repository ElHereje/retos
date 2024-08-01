# /*
#  * Escribe una función que calcule y retorne el factorial de un número dado
#  * de forma recursiva.
#  */


def factorial(num):
    
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
        
num = int(input('Introduce un número: '))
print(f'El Factorial de {num} es {factorial(num)}')
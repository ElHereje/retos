# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */


# con recursividad:
# def fib(n):
#     if n < 2:
#         return n
#     else: return fibo(n-1) + fibo(n-2) 

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        siguiente = a + b
        a, b = b, siguiente
    return a
    
for i in range(10):
    print(fibo(i))
    


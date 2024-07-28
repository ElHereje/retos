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
    # Define una función llamada fibo que toma un parámetro n.
    a, b = 0, 1
    # Inicializa las variables a y b con 0 y 1 respectivamente, 
    # que son los dos primeros números en la secuencia de Fibonacci.
    for i in range(n):
        # Utiliza un bucle for para iterar desde 0 hasta n-1.
        siguiente = a + b
        # Calcula el siguiente número en la secuencia de Fibonacci 
        # sumando los dos números anteriores.
        a, b = b, siguiente
        # Actualiza las variables a y b. 
        # 'a' toma el valor de 'b' y 'b' toma el valor de 'siguiente'.
    return a
    # Devuelve el valor de 'a' que, después del bucle, 
    # será el enésimo número de Fibonacci.

# Bucle para imprimir los primeros 10 números de Fibonacci.
for i in range(10):
    # Itera desde 0 hasta 9.
    print(fibo(i))
    # Llama a la función fibo con el valor de i 
    # y imprime el resultado.
    


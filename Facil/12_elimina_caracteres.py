# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

str1 = input('Introduce cadena 1: ')
str2 = input('Introduce cadena 2: ')

out1 = []
out2 = []

for caracter in str1:
    if caracter not in str2:
        print(f'{caracter} no está en str2')
        out1.append(caracter)
        
for caracter in str2:
    if caracter not in str1:
        print(f'{caracter} no está en str1')
        out2.append(caracter)
        
print(out1)
print(out2)
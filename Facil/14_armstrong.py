# /*
#  * Escribe una función que calcule si un número dado es un número de Armstrong
#  * (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información
#  * al respecto.
#  */


num = input('Introduzca nº a verificar: ')
e = int(len(num))
print(f'exponente {e}')

res = 0
for digito in num:
    res = res + int(digito)**e
    print(f'{digito} elevado a {e} --> acumulado = {res}')
    

if res == int(num):
    print(f'{num} es un número de Armstrong.')
else:
    print(f'{num} NO es un número de Armstrong.')
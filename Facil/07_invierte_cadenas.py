# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invierte_cadena():
    
    cadena = input('Introduce cadena a invertir: ')
    invertida = cadena[::-1]
    print(f'El texto invertido es: {invertida}')
    
invierte_cadena()
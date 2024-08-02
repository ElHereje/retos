# /*
#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

def mayus(texto):
    
    res = ''
    nueva = True
    
    for letra in texto:
        if letra.isalpha() and nueva:
            res += letra.upper()
            nueva = False
        else:
            res += letra
            
        if letra.isspace():
            nueva = True
        
    return res
        
mayus('hola 1nd mundo')




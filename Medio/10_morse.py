# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−",
    " ": " | "
    }

def texto_a_morse(letra):
    if letra in equivalencias:
        return equivalencias[letra]
    else:
        return ''
    
def codifica_morse(texto):
    texto = texto.upper()
    morse = ''
    for caracter in texto:
        caracter_codificado = texto_a_morse(caracter)
        morse += caracter_codificado
    return morse

def morse_a_texto(morse):
    for caracter in equivalencias:
        if equivalencias[caracter] == morse:
            return caracter
    
    # si no hay equivalencia    
    return ''

def codifica_texto(morse):
    texto = ''
    for caracter_morse in morse.split(' '):
        caracter = morse_a_texto(caracter_morse)
        texto += caracter
    return texto



entrada = input('Codificar o descodificar (C - D):').upper()

match entrada:
    case 'C':
        frase = input('introduce Frase a codificar: ')
        print(f'Texto en Morse: {codifica_morse(frase)}')
    case 'D':
        codigo = input('introduce código a descifrar: ')
        print(f'Morse descifrado: {codifica_texto(codigo)}')



    
    
    
# /*
#  * Crea un programa que se encargue de calcular el aspect ratio de una
#  * imagen a partir de una url.
#  * - Url de ejemplo:
#  *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  *   imagen de 1920*1080px.
#  */

import requests
from PIL import Image
from io import BytesIO

'''requests: Biblioteca para realizar peticiones HTTP, usada para descargar la imagen desde una URL.
PIL (Python Imaging Library) a través del módulo Image de Pillow: Biblioteca para abrir, manipular y guardar imágenes.
BytesIO: Permite tratar los datos en memoria como si fueran un archivo, 
útil para manejar el contenido descargado de la imagen.'''

def gcd(a, b):
    # Calcula el máximo común divisor usando el algoritmo de Euclides
    while b:
        a, b = b, a % b
    return a

'''gcd(a, b): Calcula el máximo común divisor (MCD) de a y b usando el algoritmo de Euclides.
Es útil para simplificar la fracción del aspect ratio.'''

def get_aspect_ratio(width, height):
    # Calcula el aspect ratio simplificado
    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"

'''get_aspect_ratio(width, height): Calcula y retorna el aspect ratio simplificado de una imagen dada su width (ancho) 
y height (alto). Utiliza el MCD para simplificar la relación de aspecto.'''

def download_image(url):
    # Descarga la imagen desde la URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

'''download_image(url): Descarga la imagen desde la URL especificada.
requests.get(url): Hace una solicitud HTTP GET para obtener la imagen.
BytesIO(response.content): Convierte el contenido de la respuesta HTTP en un objeto similar a un archivo.
Image.open(BytesIO(response.content)): Abre la imagen utilizando PIL desde el contenido en memoria.
Retorna el objeto Image.'''

def main():
    url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
    
    # Descarga la imagen
    img = download_image(url)
    
    # Obtiene las dimensiones de la imagen
    width, height = img.size
    
    # Calcula el aspect ratio
    aspect_ratio = get_aspect_ratio(width, height)
    
    print(f"Dimensions: {width}x{height}")
    print(f"Aspect Ratio: {aspect_ratio}")
    
'''main(): Función principal del programa.
url: Contiene la URL de la imagen a descargar.
img = download_image(url): Descarga la imagen y la guarda en la variable img.
width, height = img.size: Obtiene las dimensiones (ancho y alto) de la imagen.
aspect_ratio = get_aspect_ratio(width, height): Calcula el aspect ratio simplificado de la imagen.
print(f"Dimensions: {width}x{height}"): Imprime las dimensiones de la imagen.
print(f"Aspect Ratio: {aspect_ratio}"): Imprime el aspect ratio de la imagen.'''

if __name__ == "__main__":
    main()
    
'''Esta línea asegura que main() se ejecuta solo si el script se ejecuta directamente,
y no si se importa como un módulo en otro script.'''


'''Resumen
Este programa descarga una imagen desde una URL, obtiene sus dimensiones (ancho y alto), 
calcula su aspect ratio simplificado, y luego imprime estas dimensiones y el aspect ratio. 
Utiliza requests para la descarga, Pillow para manipular la imagen, y un cálculo del máximo 
común divisor para simplificar el aspect ratio.'''
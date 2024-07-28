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
import math

def gcd(a, b):
    # Calcula el máximo común divisor usando el algoritmo de Euclides
    while b:
        a, b = b, a % b
    return a

def get_aspect_ratio(width, height):
    # Calcula el aspect ratio simplificado
    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"

def download_image(url):
    # Descarga la imagen desde la URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

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

if __name__ == "__main__":
    main()
    
# Explicación del código
# Importar bibliotecas necesarias:

# requests para descargar la imagen desde la URL.
# PIL (Python Imaging Library) para trabajar con imágenes.
# BytesIO para manejar los datos de imagen descargados como un archivo en memoria.
# math para el cálculo del máximo común divisor (gcd).
# Definir funciones auxiliares:

# gcd(a, b): Calcula el máximo común divisor usando el algoritmo de Euclides.
# get_aspect_ratio(width, height): Calcula y retorna el aspect ratio simplificado de la imagen.
# download_image(url): Descarga la imagen desde la URL y la convierte en un objeto Image de PIL.
# Función principal main:

# Define la URL de la imagen.
# Descarga la imagen usando download_image.
# Obtiene las dimensiones de la imagen (width, height).
# Calcula el aspect ratio usando get_aspect_ratio.
# Imprime las dimensiones y el aspect ratio de la imagen.
# Ejecución
# Al ejecutar este programa, descargará la imagen de la URL proporcionada, calculará sus dimensiones y aspect ratio, 
# y luego imprimirá estos valores. Asegúrate de tener las bibliotecas requests y Pillow instaladas, 
# que se pueden instalar usando pip install requests Pillow.
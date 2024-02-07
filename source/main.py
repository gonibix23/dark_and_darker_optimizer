import os

from character import Rogue, Ranger
from image_to_text import image_to_text
from text_to_item import text_to_item

def main():
    items = []
    directorio = 'items/'

    # Iterar sobre todos los archivos en el directorio
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            items.append(text_to_item(image_to_text(ruta_archivo)))

    for item in items:
        print(item)

def test_character():
    test_character = Ranger()
    print(test_character)

if __name__ == "__main__":
    test_character()

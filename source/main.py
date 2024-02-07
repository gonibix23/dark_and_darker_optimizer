import os

from optimizer import optimize_equipment
from character import Rogue, Ranger
from image_to_text import image_to_text
from text_to_item import text_to_item

def test_items():
    items = []
    directorio = 'items_rymux/'

    # Iterar sobre todos los archivos en el directorio
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            items.append(text_to_item(image_to_text(ruta_archivo)))

    test_character = Ranger()
    
    weights = {
        "physical_damage": 0,
        "magical_damage": 5,
        "health": 2,
        "armor": 1,
        "magic_resist": 1,
        "speed": 4
    }
    #print(test_character.equipment_to_string())
    best_items = optimize_equipment(test_character, items, weights)
    for item in best_items:
        print(item)
        test_character.equip_item(item)


def test_character():
    test_character = Ranger()
    print(test_character)

if __name__ == "__main__":
    test_items()

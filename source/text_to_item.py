from item import Item
import data
from image_to_text import separate_text_and_number

def text_to_item(text):
    
    item = {
        "class": [word for word in data.character if word in text],
        "type": next((word for word in data.type if word in text), None)
        }

    text = text.split('\n')
    text = [x.strip() for x in text]
    text = list(filter(None, text))
    item["name"] = text[0]

    item["stats"] = {}

    for stat in data.stat.values():
        item["stats"][stat] = 0

    for stat in text[1:]:
        text, number = separate_text_and_number(stat)
        if text != "Empty" and text[0].isupper() and text in data.stat:
            # Check if the stat is in the list of stats
            if data.stat[text] in item["stats"]:
                # If the stat is already in the list, add the number to the existing value
                item["stats"][data.stat[text]] += number
            else:
                # If the stat is not in the list, add it with the number
                item["stats"][data.stat[text]] = number
    
    return Item(item['class'], item['type'], item['name'], item['stats'])
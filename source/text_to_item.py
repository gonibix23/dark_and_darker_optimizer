from item import Item
import data
from image_to_text import separate_text_and_number

def text_to_item(text):
    
    item = {
        "Class": [word for word in data.character if word in text],
        "Type": next((word for word in data.type if word in text), None)
        }

    text = text.split('\n')
    text = [x.strip() for x in text]
    text = list(filter(None, text))
    item["Name"] = text[0]

    item["Stats"] = {}
    for stat in text[1:]:
        text, number = separate_text_and_number(stat)
        if text != "Empty" and text[0].isupper(): # and text in data.stat
            # Check if the stat is in the list of stats
            if text in item["Stats"]:
                # If the stat is already in the list, add the number to the existing value
                item["Stats"][text] += number
            else:
                # If the stat is not in the list, add it with the number
                item["Stats"][text] = number

    item = Item(item['Class'], item['Type'], item['Name'], item['Stats'])
    return item
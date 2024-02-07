import re
import pytesseract
import data
from item import Item

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_item(image):
    text = pytesseract.image_to_string(image)
    text = re.sub('[^A-Za-z0-9|\\n|\.|\,|-]+', ' ', text)

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
    
    return Item(item['class'], item['type'], item['name'], item['stats'], image)

def separate_text_and_number(string):
    # Define a regular expression pattern to find text and numbers in the string
    pattern = re.compile(r'([a-zA-Z\s]+)([+-]?\d*\.?\d+)')

    # Search for matches in the string
    matches = pattern.match(string)

    if matches:
        # Get the text and number from the matches
        text = matches.group(1).strip()
        number = float(matches.group(2))
        return text, number
    else:
        # Define a regular expression pattern to find text and numbers in the string
        pattern = re.compile(r'([+-]?\d*\.?\d+)([a-zA-Z\s]+)')

        # Search for matches in the string
        matches = pattern.match(string)
        if matches:
            # Get the text and number from the matches
            text = matches.group(2).strip()
            number = float(matches.group(1))
            return text, number
        else:
            return "Empty", 0
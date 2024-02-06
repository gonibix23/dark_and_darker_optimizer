from PIL import Image
import re
import pytesseract

# Configura la ubicación del ejecutable de Tesseract (si no está en tu PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Carga la imagen
    image = Image.open(image_path)

    # Usa pytesseract para extraer texto de la imagen
    detected_text = pytesseract.image_to_string(image)
    # Regex para eliminar caracteres especiales
    detected_text = re.sub('[^A-Za-z0-9|\\n|\.|\,|-]+', ' ', detected_text)    
    # A partir de la palabra Rarity, elimino el texto
    detected_text = detected_text.split('\n')
    detected_text = [x.strip() for x in detected_text]
    detected_text = list(filter(None, detected_text))
    
    return detected_text

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

def text_to_item(text):
    item = {
        'Name': text[0]
    }
    for stat in text[1:]:
        text, number = separate_text_and_number(stat)
        item[text] = number
    return item

print(image_to_text('items/test_04.png'))
print(text_to_item(image_to_text('items/test_04.png')))
from PIL import Image
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    image = Image.open(image_path)
    detected_text = pytesseract.image_to_string(image)
    detected_text = re.sub('[^A-Za-z0-9|\\n|\.|\,|-]+', ' ', detected_text)
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
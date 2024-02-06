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
    detected_text = re.sub('[^A-Za-z0-9|\\n|\.|\%|\,|-]+', ' ', detected_text)    
    # A partir de la palabra Rarity, elimino el texto
    detected_text = detected_text.split('\n')
    detected_text = [x.strip() for x in detected_text]
    detected_text = list(filter(None, detected_text))
    
    print(detected_text)

image_to_text('items/test_04.png')
try :
    from PIL import Image
except ImportError :
    import Image
    

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def readText(img_file):
    text = pytesseract.image_to_string(Image.open(img_file))
    return text

def printer():
    info = readText('quote2.jpeg')
    print(info)
    
    
from PIL import Image

import pytesseract as pt 

# Simple image to string
print(pt.image_to_string(Image.open('SakuraAP.png')))
print(pt.image_to_string(Image.open('SakuraAP2.png')))
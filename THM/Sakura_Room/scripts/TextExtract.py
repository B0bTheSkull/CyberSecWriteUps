from PIL import Image

import pytesseract as pt 

# Simple image to string
#If you're someone using this and you don't understand code at all
#you need to save the two images into the same directory as your script
#and then you need to change the name of the files so it uses whatever is on your machine
print(pt.image_to_string(Image.open('SakuraAP.png'))) #Change this file name
print(pt.image_to_string(Image.open('SakuraAP2.png'))) #Change this file name
import pytesseract
from PIL import Image
convert -resize 400% in.bmp out.bmp
a=pytesseract.image_to_string(Image.open('FINAL.jpg'))
print a